import json
import os
import statistics
import subprocess
import sys
import time

RUNS = 30
CHILD = r'''
import json, os, sys, time
sys.path.insert(0, os.getcwd())
import main as m
album_id = m._album_extract_id((json.load(open('config/config.json', encoding='utf-8')) or {}).get('target_url', ''))
m._start_album_prefetch()
t0 = time.time()
res = m._take_album_prefetch(album_id, wait_seconds=30)
print(json.dumps({
    'seconds': round(time.time() - t0, 2),
    'hit': res is not None,
    'count': len(res[0]) if res else 0,
    'error': m._album_prefetch.get('error'),
}, ensure_ascii=False))
'''

rows = []
for i in range(1, RUNS + 1):
    proc = subprocess.run(
        ['.venv/bin/python', '-c', CHILD], capture_output=True, text=True, timeout=120,
    )
    line = [l for l in proc.stdout.splitlines() if l.startswith('{')]
    if not line:
        print(f'{i:2d} | 子进程异常: {proc.stderr.strip()[-160:]}')
        continue
    row = json.loads(line[-1])
    rows.append(row)
    print(f'{i:2d} | {row["seconds"]:6.2f}s | 命中={row["hit"]} | 商品={row["count"]:4d} | '
          f'error={row["error"]}', flush=True)

secs = [r['seconds'] for r in rows]
print('\n===== 相册接口首包耗时（不含浏览器） =====')
print(f'样本: {len(secs)}  均值: {statistics.mean(secs):.2f}s  中位: {statistics.median(secs):.2f}s')
print(f'最小: {min(secs):.2f}s  最大: {max(secs):.2f}s  标准差: {statistics.pstdev(secs):.3f}')
print(f'>5s 次数: {sum(1 for s in secs if s > 5)}  >8s 次数: {sum(1 for s in secs if s > 8)}')
print(f'未命中次数: {sum(1 for r in rows if not r["hit"])}')
errs = {}
for r in rows:
    if r['error']:
        errs[r['error']] = errs.get(r['error'], 0) + 1
print(f'错误分布: {errs}')
print(f'商品数集合: {sorted(set(r["count"] for r in rows if r["hit"]))}')