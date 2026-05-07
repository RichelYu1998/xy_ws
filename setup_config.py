#!/usr/bin/env python3
import os
import json
import sys
import argparse
import asyncio
import time
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Szwego爬虫配置文件初始化")
    parser.add_argument("--username", "-u", required=True, help="登录用户名")
    parser.add_argument("--password", "-p", required=True, help="登录密码")
    parser.add_argument("--url", "-l", required=True, help="目标店铺URL")
    parser.add_argument("--excel", "-e", default="", help="Excel文件路径")

    args = parser.parse_args()

    os.makedirs("config", exist_ok=True)

    if os.path.exists("config/config.json"):
        print("config.json 已存在，跳过创建。如需重新生成请先删除。")
        return

    print("=" * 50)
    print("正在打开浏览器进行登录...")
    print("请在浏览器中完成登录")
    print("登录成功后程序将自动获取Cookie")
    print("=" * 50)

    cookie_file = "config/cookies.json"
    with open(cookie_file, "w", encoding="utf-8") as f:
        json.dump([], f)

    async def get_cookie():
        from playwright.async_api import async_playwright

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
            )

            page = await context.new_page()
            await page.goto('https://www.szwego.com', wait_until='networkidle')

            print('\n请在浏览器中登录您的账号...')

            start_time = time.time()
            timeout = 300
            login_detected = False

            while time.time() - start_time < timeout:
                try:
                    cookies = await context.cookies()
                    token_cookie = next((c for c in cookies if c['name'] == 'token'), None)

                    if token_cookie and token_cookie['value']:
                        print('\n✓ 检测到登录成功！正在获取Cookie...')
                        login_detected = True
                        break
                except:
                    pass

                await asyncio.sleep(3)
                elapsed = int(time.time() - start_time)
                print(f'等待登录中... ({elapsed}秒)', end='\r')

            if not login_detected:
                print('\n⚠️ 登录超时，将尝试获取当前Cookie')

            cookies = await context.cookies()
            szwego_cookies = [cookie for cookie in cookies if 'szwego.com' in cookie.get('domain', '')]

            for cookie in szwego_cookies:
                if cookie['domain'] == 'www.szwego.com':
                    cookie['domain'] = '.szwego.com'

            with open(cookie_file, "w", encoding="utf-8") as f:
                json.dump(szwego_cookies, f, ensure_ascii=False, indent=2)

            print(f'✓ Cookie已保存 ({len(szwego_cookies)}个)')

            await browser.close()
            return szwego_cookies

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("错误: 请先安装playwright")
        print("运行: pip install playwright && playwright install chromium")
        sys.exit(1)

    cookies = asyncio.run(get_cookie())

    token_cookie = next((c for c in cookies if c['name'] == 'token'), None)
    sensors_cookie = next((c for c in cookies if c['name'] == 'sensorsdata2015jssdkcross'), None)

    token = token_cookie['value'] if token_cookie else ""
    sensors = sensors_cookie['value'] if sensors_cookie else ""

    config = {
        "login": {
            "username": args.username,
            "password": args.password,
            "login_type": "phone"
        },
        "target_url": args.url,
        "scroll_config": {
            "max_attempts": 30,
            "same_height_limit": 8,
            "scroll_wait_time": 0.8,
            "popup_close_interval": 5,
            "popup_close_limit": 3,
            "popup_close_wait": 0.3,
            "dynamic_adjust": True
        },
        "headers": {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "connection": "keep-alive",
            "cookie": "",
            "host": "www.szwego.com",
            "sec-ch-ua": "\"Chromium\";v=\"146\", \"Not-A.Brand\";v=\"24\", \"Google Chrome\";v=\"146\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
        },
        "cookies": cookies,
        "output_file": "file/output.json",
        "cookie_file": "config/cookies.json",
        "excel_files": [args.excel] if args.excel else []
    }

    cookie_header = '; '.join([f'{c["name"]}={c["value"]}' for c in cookies])
    config["headers"]["cookie"] = cookie_header

    config_path = "config/config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    print(f'\n✓ config.json 创建成功！')
    print("\n========================================")
    print("   初始化完成！")
    print("========================================")
    print(f"\n配置信息：")
    print(f"  - 用户名: {args.username}")
    print(f"  - 目标URL: {args.url}")
    print(f"  - Cookie数量: {len(cookies)}")

if __name__ == "__main__":
    main()