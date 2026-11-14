import subprocess
import time
import re
import statistics
import json

RUNS = 30
results = []
for i in range(1, RUNS + 1):
    start = time.time()
    proc = subprocess.run(
        ['.venv/bin/python', 'main.py', '--task', '1'],
        capture_output=True, text=True, timeout=180,
    )
    elapsed = time.time() - start
    out = proc.stdout + proc.stderr
    m_cnt = re.search(r'成功获取\s*(\d+)\s*个商品', out)
    count = int(m_cnt.group(1)) if m_cnt else 0
    m_browser = re.search(r'浏览器启动耗时:\s*([\d.]+)秒', out)
    m_api = re.search(r'数据获取耗时:\s*([\d.]+)秒', out)
    browser = float(m_browser.group(1)) if m_browser else 0.0
    api = float(m_api.group(1)) if m_api else 0.0
    has_429 = '429' in out
    exit_ok = proc.returncode == 0
    results.append({
        'i': i, 'elapsed': round(elapsed, 2), 'count': count,
        'browser': browser, 'api': api, '429': has_429, 'ok': exit_ok,
    })
    print(f'{i:2d} | total{elapsed:6.2f}s | browser{browser:5.2f}s | API{api:5.2f}s | goods{count:4d} | '
          f'429={has_429} | exit={proc.returncode}', flush=True)

with open('/tmp/bench_30.json', 'w') as f:
    json.dump(results, f, ensure_ascii=False, indent=1)

times = [r['elapsed'] for r in results]
counts = set(r['count'] for r in results)
print('\n===== summary =====')
print(f'samples: {len(times)}')
print(f'mean: {statistics.mean(times):.2f}s  median: {statistics.median(times):.2f}s')
print(f'min: {min(times):.2f}s  max: {max(times):.2f}s  stdev: {statistics.pstdev(times):.3f}')
print(f'<=10s: {sum(1 for t in times if t <= 10)}/{len(times)}')
print(f'>10s: {sum(1 for t in times if t > 10)}')
print(f'goods counts: {sorted(counts)}')
print(f'429 hits: {sum(1 for r in results if r["429"])}')
print(f'non-zero exit: {sum(1 for r in results if not r["ok"])}')