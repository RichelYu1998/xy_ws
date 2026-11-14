import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                if os.path.basename(os.getcwd()) != 'xy_ws' else os.getcwd())

os.environ.setdefault('ALBUM_RATE_LIMIT_BASE_DELAY', '0.4')
os.environ.setdefault('ALBUM_RATE_LIMIT_MAX_DELAY', '0.8')
os.environ.setdefault('ALBUM_PAGE_DELAY_MIN', '0.05')
os.environ.setdefault('ALBUM_PAGE_DELAY_JITTER', '0.1')

import main as m

STATE = {'hits': 0, 'plan': [], 'retry_after': '1'}
LOCK = threading.Lock()


class Handler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        with LOCK:
            STATE['hits'] += 1
            idx = STATE['hits'] - 1
            code = STATE['plan'][idx] if idx < len(STATE['plan']) else 200
        if code == 429:
            body = b'{"code":429,"msg":"rate limited"}'
            self.send_response(429)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Retry-After', STATE['retry_after'])
            self.end_headers()
            self.wfile.write(body)
        else:
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
        pass


class MockServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def start_server():
    server = MockServer(('127.0.0.1', 0), Handler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f'http://127.0.0.1:{port}/album/personal/all'


def reset():
    with LOCK:
        STATE['hits'] = 0
        STATE['plan'] = []
    m._album_rate_limit_until = 0.0
    m._album_rate_limit_hits = 0


def case(title):
    print(f'\n===== {title} =====')


server, url = start_server()
fails = []


def check(cond, msg):
    print(('  PASS  ' if cond else '  FAIL  ') + msg)
    if not cond:
        fails.append(msg)


case('场景1: 连续2次429后恢复200（风控窗口放行即续抓）')
reset()
with LOCK:
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
m._album_rate_limit_until = 0.0
delay_limited = m._album_page_delay()
check(delay_limited >= m._ALBUM_PAGE_DELAY_SLOW_BASE,
      f'有过429但已过冷却时仍保持放慢节奏 {delay_limited:.2f}秒')

case('场景4: 风控缓解后延迟自动回落')
for _ in range(50):
    m._album_note_success()
delay_recovered = m._album_page_delay()
check(m._album_rate_limit_hits == 0, f'成功请求逐步衰减计数至0, hits={m._album_rate_limit_hits}')
check(delay_recovered <= 0.2,
      f'延迟回落到正常区间(0.05~0.15), 实测{delay_recovered:.3f}秒')

case('场景5: 全局限流闸门让并发请求统一等待冷却')
m._mark_album_rate_limited(1.0)
t0 = time.time()
m._album_throttle_wait()
dt = time.time() - t0
check(dt >= 0.9, f'闸门生效, 请求被阻塞{dt:.2f}秒后才放行')
check(m._album_cooldown_remaining() == 0, '冷却结束后闸门自动放开')

case('场景6: 长连接复用 + gzip 在真实接口上不抛异常')
reset()
with LOCK:
    STATE['plan'] = [200] * 5
ok_all = True
for _ in range(5):
    code, text, err = m.fetch_album_api_page(url, {}, 'a=b', timeout=5)
    if code != 200 or err is not None:
        ok_all = False
check(ok_all, '同一条连接连续5次请求全部成功（连接复用无残留状态）')
check(STATE['hits'] == 5, f'5次请求全部到达服务端, 实测{STATE["hits"]}次')

server.shutdown()
print('\n===== 结果 =====')
print(f'用例失败数: {len(fails)}')
for f in fails:
    print('  - ' + f)
sys.exit(1 if fails else 0)