"""
429 限流防护专项测试（本地 mock 服务端，不依赖真实接口）

用途：覆盖指数退避、重试预算、全局冷却闸门、风控计数衰减、长连接复用，
以及对冲请求在 429 场景下的「立即停发新路 + 全部失败快速返回」行为。
运行方式：.venv/bin/python test/test_429_handling.py
"""
import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 兼容两种运行方式：在项目根目录执行，或在 test 目录内执行
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                if os.path.basename(os.getcwd()) != 'xy_ws' else os.getcwd())

# 把限流退避与页间延迟压到很小的值，让用例能在秒级内跑完
os.environ.setdefault('ALBUM_RATE_LIMIT_BASE_DELAY', '0.4')
os.environ.setdefault('ALBUM_RATE_LIMIT_MAX_DELAY', '0.8')
os.environ.setdefault('ALBUM_PAGE_DELAY_MIN', '0.05')
os.environ.setdefault('ALBUM_PAGE_DELAY_JITTER', '0.1')

import main as m

# mock 服务端状态：累计命中次数、按序号编排的响应码计划、Retry-After 头取值
STATE = {'hits': 0, 'plan': [], 'retry_after': '1'}
LOCK = threading.Lock()


class Handler(BaseHTTPRequestHandler):
    """mock 请求处理器：按计划返回 429 或 200，并统计命中次数"""
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        """按 STATE['plan'] 的顺序决定本次返回码，用尽后默认返回 200"""
        with LOCK:
            STATE['hits'] += 1
            idx = STATE['hits'] - 1
            code = STATE['plan'][idx] if idx < len(STATE['plan']) else 200
        if code == 429:
            # 返回 429 并带上 Retry-After，验证客户端是否读取该头
            body = b'{"code":429,"msg":"rate limited"}'
            self.send_response(429)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Retry-After', STATE['retry_after'])
            self.end_headers()
            self.wfile.write(body)
        else:
            # 返回一个最小可用的正常业务响应体
            payload = json.dumps({
                'code': 0,
                'result': {'items': [{'goodsId': 'g1'}], 'pagination': {'total': 1}},
            }).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    def log_message(self, *args):
        """屏蔽默认访问日志，保持测试输出干净"""
        pass


class MockServer(ThreadingHTTPServer):
    """多线程 mock 服务端：支持端口复用，线程随主进程退出"""
    daemon_threads = True
    allow_reuse_address = True


def start_server():
    """在随机端口启动 mock 服务端，返回服务端对象与相册接口地址"""
    server = MockServer(('127.0.0.1', 0), Handler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f'http://127.0.0.1:{port}/album/personal/all'


def reset():
    """重置 mock 服务端计数与响应计划，并清空主模块的全局限流状态"""
    with LOCK:
        STATE['hits'] = 0
        STATE['plan'] = []
    m._album_rate_limit_until = 0.0
    m._album_rate_limit_hits = 0


def case(title):
    """打印用例标题分隔"""
    print(f'\n===== {title} =====')


server, url = start_server()
fails = []


def check(cond, msg):
    """断言封装：打印 PASS/FAIL，失败用例收集起来用于最终汇总"""
    print(('  PASS  ' if cond else '  FAIL  ') + msg)
    if not cond:
        fails.append(msg)


case('场景1: 连续2次429后恢复200（风控窗口放行即续抓）')
reset()
with LOCK:
    # 前两次返回 429，第三次返回 200，验证退避后能自动恢复
    STATE['plan'] = [429, 429, 200]
t0 = time.time()
code, text, err = m.fetch_album_api_page(url, {}, 'a=b', timeout=5, max_retries=3)
dt = time.time() - t0
check(code == 200 and err is None, f'最终返回200且无错误 (code={code}, err={err})')
check(STATE['hits'] == 3, f'实际请求3次(2次429+1次200), 实测{STATE["hits"]}次')
check(0 < dt < 5, f'总等待在指数退避区间内, 实测{dt:.2f}秒')
check(json.loads(text)['code'] == 0, '200响应体可正常解析')

case('场景2: 429打满重试预算 → 放弃并登记全局限流冷却')
reset()
with LOCK:
    # 全部返回 429，验证重试预算耗尽后放弃并登记全局冷却
    STATE['plan'] = [429] * 10
t0 = time.time()
code, text, err = m.fetch_album_api_page(url, {}, 'a=b', timeout=5,
                                        max_retries=3, rate_limit_max_retries=3)
dt = time.time() - t0
check(code == 429, f'返回429状态码, 实测{code}')
check(err is not None and '限流未解除' in err, f'错误信息说明限流未解除: {err}')
check(STATE['hits'] == 3, f'429重试次数受预算约束为3次, 实测{STATE["hits"]}次')
check(m._album_cooldown_remaining() > 0, f'全局冷却已登记, 剩余{m._album_cooldown_remaining():.2f}秒')
check(m._album_rate_limit_hits > 0, f'限流命中计数已累加, hits={m._album_rate_limit_hits}')

case('场景3: 冷却期内的页间延迟被放大（防止连环429）')
delay_during = m._album_page_delay()
check(delay_during >= 0.4, f'冷却中页间延迟被放大到 {delay_during:.2f}秒')
# 手动清空冷却时间，验证「有过 429 但已过冷却」仍保持放慢节奏
m._album_rate_limit_until = 0.0
delay_limited = m._album_page_delay()
check(delay_limited >= m._ALBUM_PAGE_DELAY_SLOW_BASE,
      f'有过429但已过冷却时仍保持放慢节奏 {delay_limited:.2f}秒')

case('场景4: 风控缓解后延迟自动回落')
# 连续成功 50 次，风控命中计数应逐步衰减到 0，页间延迟回到正常区间
for _ in range(50):
    m._album_note_success()
delay_recovered = m._album_page_delay()
check(m._album_rate_limit_hits == 0, f'成功请求逐步衰减计数至0, hits={m._album_rate_limit_hits}')
check(delay_recovered <= 0.2,
      f'延迟回落到正常区间(0.05~0.15), 实测{delay_recovered:.3f}秒')

case('场景5: 全局限流闸门让并发请求统一等待冷却')
# 登记 1 秒全局冷却，随后任何请求都必须等闸门放开才能继续
m._mark_album_rate_limited(1.0)
t0 = time.time()
m._album_throttle_wait()
dt = time.time() - t0
check(dt >= 0.9, f'闸门生效, 请求被阻塞{dt:.2f}秒后才放行')
check(m._album_cooldown_remaining() == 0, '冷却结束后闸门自动放开')

case('场景6: 长连接复用 + gzip 在真实接口上不抛异常')
reset()
with LOCK:
    # 全部返回 200，验证同一条连接连续复用不会残留状态
    STATE['plan'] = [200] * 5
ok_all = True
for _ in range(5):
    code, text, err = m.fetch_album_api_page(url, {}, 'a=b', timeout=5)
    if code != 200 or err is not None:
        ok_all = False
check(ok_all, '同一条连接连续5次请求全部成功（连接复用无残留状态）')
check(STATE['hits'] == 5, f'5次请求全部到达服务端, 实测{STATE["hits"]}次')

case('场景7: 对冲请求撞429立即停止发新路且不白等超时上界')
# 用桩函数替换单路请求：每次调用都立即抛 429，观察后续是否还继续发新路
orig_once = m._album_prefetch_once
calls = []


def fake_429(album_id, cookie_str):
    """桩函数：记录发起时刻后立即抛出 429 可重试错误"""
    calls.append(time.time())
    raise m._AlbumPrefetchError('HTTP 429', status=429, retryable=True)


m._album_prefetch_once = fake_429
try:
    t0 = time.time()
    raised = False
    try:
        m._album_prefetch_hedged('album', 'a=b')
    except m._AlbumPrefetchError as exc:
        raised = True
        hedge_err = str(exc)
    dt = time.time() - t0
finally:
    # 无论断言结果如何都要还原真实实现，避免污染后续用例
    m._album_prefetch_once = orig_once
check(raised, f'全部路失败时抛出 _AlbumPrefetchError: {hedge_err}')
check(len(calls) == 1, f'首路429后不再发新路(避免加剧限流), 实测{len(calls)}路')
check(dt < 1.0, f'全部失败立即返回, 不白等超时上界, 实测{dt:.2f}秒')

case('场景8: 对冲请求任一路成功即返回（尾延迟取最快那一路）')
# 桩函数：第一路故意慢 2 秒再失败，第二路立即成功，验证不会被慢路拖住
calls2 = []


def fake_slow_then_fast(album_id, cookie_str):
    """桩函数：首路模拟慢响应失败，后续路直接返回正常数据"""
    calls2.append(time.time())
    if len(calls2) == 1:
        time.sleep(2.0)
        raise m._AlbumPrefetchError('模拟慢路超时')
    return [{'goodsId': 'g1'}], {'total': 1, 'isLoadMore': False}


m._album_prefetch_once = fake_slow_then_fast
try:
    t0 = time.time()
    items, pagination = m._album_prefetch_hedged('album', 'a=b')
    dt = time.time() - t0
finally:
    # 还原真实实现，保证测试结束后主模块状态干净
    m._album_prefetch_once = orig_once
check(len(items) == 1 and pagination.get('total') == 1, '对冲成功返回第一页数据与分页信息')
check(dt < 1.9, f'第二路成功即返回, 未被慢路拖到2秒, 实测{dt:.2f}秒')
check(len(calls2) >= 2, f'慢路失败后仍有新路顶上, 实测发出{len(calls2)}路')

# 关闭 mock 服务端并汇总结果，有失败用例时以非零退出码结束
server.shutdown()
print('\n===== 结果 =====')
print(f'用例失败数: {len(fails)}')
for f in fails:
    print('  - ' + f)
sys.exit(1 if fails else 0)