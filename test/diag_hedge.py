import json
import os
import sys
import time

sys.path.insert(0, os.getcwd())
import main as m

with open('config/config.json', encoding='utf-8') as f:
    album_id = m._album_extract_id((json.load(f) or {}).get('target_url', ''))
with open('config/cookies.json', encoding='utf-8') as f:
    cookies = json.load(f)
cookie_str = '; '.join([
    f'{c.get("name", "")}={c.get("value", "")}'
    for c in cookies if isinstance(c, dict) and c.get('name') and c.get('value')
])

for i in range(10):
    t0 = time.time()
    try:
        items, pagination = m._album_prefetch_hedged(album_id, cookie_str)
        print(f'{i:2d} | {time.time() - t0:6.2f}s | ok items={len(items)} isLoadMore={pagination.get("isLoadMore")}', flush=True)
    except m._AlbumPrefetchError as exc:
        print(f'{i:2d} | {time.time() - t0:6.2f}s | FAIL {exc}', flush=True)