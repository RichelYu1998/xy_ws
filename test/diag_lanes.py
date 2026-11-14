import json
import os
import sys
import threading
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

ROUNDS = 8
LANES = 4


def lane(idx, t0, out):
    try:
        items, pagination = m._album_prefetch_once(album_id, cookie_str)
        out[idx] = round(time.time() - t0, 2)
    except Exception as exc:
        out[idx] = f'ERR:{type(exc).__name__}'


for r in range(ROUNDS):
    t0 = time.time()
    out = {}
    threads = [threading.Thread(target=lane, args=(i, t0, out), daemon=True) for i in range(LANES)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=20)
    times = [v for v in out.values() if isinstance(v, float)]
    print(f'round {r}: lanes={sorted(out.values(), key=str)}  min={min(times) if times else None}', flush=True)