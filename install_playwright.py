#!/usr/bin/env python3
import os, subprocess, sys, urllib.request, time

CDNS = [
    ("npmmirror", "https://npmmirror.com/mirrors/playwright/"),
    ("azureedge", "https://playwright.azureedge.net/builds/"),
    ("cdn", "https://cdn.playwright.dev/"),
]

def test_cdn(name, url):
    try:
        start = time.time()
        urllib.request.urlopen(url, timeout=3)
        return round(time.time() - start, 3)
    except Exception:
        return None

print("[*] 测试Playwright CDN速度...")
results = []
for name, url in CDNS:
    print(f"    测试 {name}...", end="", flush=True)
    elapsed = test_cdn(name, url)
    if elapsed is not None:
        print(f" {elapsed}秒")
        results.append((name, url, elapsed))
    else:
        print(" 失败")

if not results:
    print("[WARNING] 所有Playwright CDN均无法访问，将尝试默认安装")
    fastest_url = ""
else:
    results.sort(key=lambda x: x[2])
    fastest_name, fastest_url, fastest_time = results[0]
    print(f"[*] 最终选择最快Playwright CDN: {fastest_name} ({fastest_time}秒)")

print("[*] 安装Playwright浏览器...")
installed = False

for name, url, _ in results:
    print(f"    尝试从 {name} 下载...", flush=True)
    env = os.environ.copy()
    env["PLAYWRIGHT_DOWNLOAD_HOST"] = url
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        capture_output=True, text=True, env=env
    )
    if result.returncode == 0:
        print(f"[*] Playwright浏览器安装成功 (来源: {name})")
        installed = True
        break
    err = (result.stderr or result.stdout)
    print(f"    {name} 下载失败: {err[-300:] if err else 'unknown error'}")

if not installed and fastest_url:
    print(f"    尝试从 {fastest_name} 下载...", flush=True)
    env = os.environ.copy()
    env["PLAYWRIGHT_DOWNLOAD_HOST"] = fastest_url
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        capture_output=True, text=True, env=env
    )
    if result.returncode == 0:
        print(f"[*] Playwright浏览器安装成功 (来源: {fastest_name})")
        installed = True

if not installed:
    print("[WARNING] Playwright浏览器安装失败，将在首次运行时自动安装")
PYEOF 