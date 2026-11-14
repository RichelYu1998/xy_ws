import asyncio
import os
import sys
import time

sys.path.insert(0, os.getcwd())
import main as m

m._album_prefetch['error'] = '模拟预热失败'
m._album_prefetch['event'].set()

scraper = m.WegoScraper()
t0 = time.time()
products, complete = asyncio.run(scraper.fetch_all_products_via_api(None))
print(f'首屏对冲兜底: {len(products)} 个商品, 完整={complete}, 耗时={time.time() - t0:.2f}s')