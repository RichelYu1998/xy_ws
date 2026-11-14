"""
预热失败兜底路径诊断脚本

用途：人为把预热状态置为失败，验证「预热未命中时首屏走对冲兜底」这条路径
仍能拿到商品数据，并记录兜底耗时。
运行方式：.venv/bin/python test/diag_fallback.py
"""
import asyncio
import os
import sys
import time

# 先把项目根目录加入搜索路径，再导入主模块（导入必须集中在文件顶部）
sys.path.insert(0, os.getcwd())
import main as m

# 构造预热失败的现场：写入错误信息并立即置位完成事件
m._album_prefetch['error'] = '模拟预热失败'
m._album_prefetch['event'].set()

scraper = m.WegoScraper()
t0 = time.time()
products, complete = asyncio.run(scraper.fetch_all_products_via_api(None))
print(f'首屏对冲兜底: {len(products)} 个商品, 完整={complete}, 耗时={time.time() - t0:.2f}s')