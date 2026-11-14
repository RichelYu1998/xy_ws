"""
对冲请求（Hedged Requests）诊断脚本

用途：连续 10 轮直接调用 _album_prefetch_hedged()，观察每轮耗时与返回的商品数、
分页标记，确认「谁先成功用谁」确实把尾延迟压到最快那一路的水平。
运行方式：.venv/bin/python test/diag_hedge.py
"""
import json
import os
import sys
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

ROUNDS = 10

for i in range(ROUNDS):
    t0 = time.time()
    try:
        items, pagination = m._album_prefetch_hedged(album_id, cookie_str)
        more = pagination.get('isLoadMore')
        print(f'{i:2d} | {time.time() - t0:6.2f}s | ok items={len(items)} isLoadMore={more}', flush=True)
    except m._AlbumPrefetchError as exc:
        # 所有路都失败时才会走到这里，记录异常便于判断是否服务端整体不可用
        print(f'{i:2d} | {time.time() - t0:6.2f}s | FAIL {exc}', flush=True)