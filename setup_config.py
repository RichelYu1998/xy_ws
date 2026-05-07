#!/usr/bin/env python3
import os
import json
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Szwego爬虫配置文件初始化")
    parser.add_argument("--username", "-u", required=True, help="登录用户名")
    parser.add_argument("--password", "-p", required=True, help="登录密码")
    parser.add_argument("--url", "-l", required=True, help="目标店铺URL")
    parser.add_argument("--token", "-t", required=True, help="Cookie token")
    parser.add_argument("--sensors", "-s", default="", help="sensorsdata2015jssdkcross值")
    parser.add_argument("--excel", "-e", default="", help="Excel文件路径")

    args = parser.parse_args()

    os.makedirs("config", exist_ok=True)

    if os.path.exists("config/config.json"):
        print("config.json 已存在，跳过创建。如需重新生成请先删除。")
    else:
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
                "cookie": f"sajssdk_2015_cross_new_user=1; token={args.token}; client_type=net",
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
            "cookies": [
                {
                    "name": "sajssdk_2015_cross_new_user",
                    "value": "1",
                    "domain": ".szwego.com",
                    "path": "/",
                    "expires": -1,
                    "httpOnly": False,
                    "secure": False,
                    "sameSite": "Lax"
                },
                {
                    "name": "token",
                    "value": args.token,
                    "domain": ".szwego.com",
                    "path": "/",
                    "expires": -1,
                    "httpOnly": False,
                    "secure": False,
                    "sameSite": "Lax"
                },
                {
                    "name": "client_type",
                    "value": "net",
                    "domain": ".szwego.com",
                    "path": "/",
                    "expires": -1,
                    "httpOnly": False,
                    "secure": False,
                    "sameSite": "Lax"
                }
            ],
            "output_file": "file/output.json",
            "cookie_file": "config/cookies.json",
            "excel_files": [args.excel] if args.excel else []
        }

        if args.sensors:
            config["headers"]["cookie"] += f"; sensorsdata2015jssdkcross={args.sensors}"
            config["cookies"].append({
                "name": "sensorsdata2015jssdkcross",
                "value": args.sensors,
                "domain": ".szwego.com",
                "path": "/",
                "expires": -1,
                "httpOnly": False,
                "secure": False,
                "sameSite": "Lax"
            })

        with open("config/config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print("config.json 创建成功！")

    print("\n========================================")
    print("   初始化完成！")
    print("========================================")

if __name__ == "__main__":
    main()