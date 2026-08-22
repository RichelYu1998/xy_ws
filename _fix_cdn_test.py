with open(r'D:\ws\xy_ws\main.py', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# 1. Fix CDN list - add separate test URLs
old_cdns = '''    CDNS = [
        ("npmmirror", "https://npmmirror.com/mirrors/playwright"),
        ("azureedge", "https://playwright.azureedge.net/builds"),
        ("cdn", "https://cdn.playwright.dev"),
    ]

    def test_cdn(name, url):
        try:
            start = time.time()
            urllib.request.urlopen(url, timeout=3)
            return round(time.time() - start, 3)
        except Exception as e:
            print(f'[CDN] Test failed {name}: {e}')
            return None

    print("[*] 测试Playwright CDN速度...")
    results = []
    for name, url in CDNS:
        elapsed = test_cdn(name, url)
        if elapsed is not None:
            print(f"    {name}: {elapsed}秒")
            results.append((name, url, elapsed))
        else:
            print(f"    {name}: 失败")'''

new_cdns = '''    CDNS = [
        ("npmmirror", "https://npmmirror.com/mirrors/playwright", "https://npmmirror.com"),
        ("azureedge", "https://playwright.azureedge.net/builds", "https://playwright.azureedge.net"),
        ("cdn", "https://cdn.playwright.dev", "https://cdn.playwright.dev"),
    ]

    def test_cdn(name, url, test_url):
        try:
            start = time.time()
            urllib.request.urlopen(test_url, timeout=5)
            return round(time.time() - start, 3)
        except Exception as e:
            print(f'[CDN] Test failed {name}: {e}')
            return None

    print("[*] 测试Playwright CDN速度...")
    results = []
    for name, url, test_url in CDNS:
        elapsed = test_cdn(name, url, test_url)
        if elapsed is not None:
            print(f"    {name}: {elapsed}秒")
            results.append((name, url, elapsed))
        else:
            print(f"    {name}: 失败")'''

if old_cdns in content:
    content = content.replace(old_cdns, new_cdns)
    changes += 1
    print('1. SUCCESS: CDN test URLs fixed')
else:
    print('1. ERROR: CDN list not found')

# 2. Fix the fallback download order - include all 3 CDNs
old_fallback = '        download_order = [("cdn", "https://cdn.playwright.dev")]'
new_fallback = '''        download_order = [
            ("npmmirror", "https://npmmirror.com/mirrors/playwright"),
            ("azureedge", "https://playwright.azureedge.net/builds"),
            ("cdn", "https://cdn.playwright.dev"),
        ]'''

if old_fallback in content:
    content = content.replace(old_fallback, new_fallback)
    changes += 1
    print('2. SUCCESS: fallback order includes all CDNs')
else:
    print('2. ERROR: fallback not found')

# 3. Add stdout output printing for better debugging
old_stderr = '''        if result.stderr:
            for err_line in result.stderr.split('\\n'):
                if 'Error:' in err_line or '404' in err_line:
                    print(f"    {err_line.strip()}")'''

new_stderr = '''        if result.stderr:
            for err_line in result.stderr.split('\\n'):
                if 'Error:' in err_line or '404' in err_line or 'Downloading' in err_line:
                    print(f"    {err_line.strip()}")
        if result.stdout:
            for out_line in result.stdout.split('\\n'):
                if 'Downloading' in out_line or 'Downloaded' in out_line or 'already' in out_line.lower():
                    print(f"    {out_line.strip()}")'''

if old_stderr in content:
    content = content.replace(old_stderr, new_stderr)
    changes += 1
    print('3. SUCCESS: added stdout output printing')
else:
    print('3. ERROR: stderr block not found')

with open(r'D:\ws\xy_ws\main.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nTotal changes: {changes}')