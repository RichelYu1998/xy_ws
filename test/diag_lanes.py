"""
多路并发延迟分布诊断脚本

用途：每轮同时开 4 条线程并发请求同一接口，记录每条路各自的耗时，
用来确认「最快的那一路」能把尾延迟压到什么水平（对冲参数的取值依据）。
运行方式：.venv/bin/python test/diag_lanes.py
"""
import json
import os
import sys
import threading
import time

# 先把项目根目录加入搜索路径，再导入主模块（导入必须集中在文件顶部）
sys.path.insert(0, os.getcwd())
import main as m

# 读取目标相册 ID
with open('config/config.json', encoding='utf-8') as f:
    album_id = m._album_extract_id((json.load(f) or {}).get('target_url', ''))
# 读取 cookie 并拼成请求头需要的字符串格式
with open('config/cookies.json', encoding='utf-8') as f:
    cookies = json.load(f)
cookie_str = '; '.join([
    f'{c.get("name", "")}={c.get("value", "")}'
    for c in cookies if isinstance(c, dict) and c.get('name') and c.get('value')
])

ROUNDS = 8
LANES = 4


def lane(idx, t0, out):
    """单条请求路：成功记录耗时，失败记录异常类型"""
    try:
        items, pagination = m._album_prefetch_once(album_id, cookie_str)
        out[idx] = round(time.time() - t0, 2)
    except Exception as exc:
        out[idx] = f'ERR:{type(exc).__name__}'


for r in range(ROUNDS):
    t0 = time.time()
    out = {}
    # 所有路以同一时刻为基准起跑，便于比较各自的绝对延迟
    threads = [threading.Thread(target=lane, args=(i, t0, out), daemon=True) for i in range(LANES)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=20)
    # 只把成功返回的浮点耗时纳入最小值统计
    times = [v for v in out.values() if isinstance(v, float)]
    print(f'round {r}: lanes={sorted(out.values(), key=str)}  min={min(times) if times else None}', flush=True)