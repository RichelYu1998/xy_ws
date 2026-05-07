#!/usr/bin/env python3
import os
import sys

def main():
    config_dir = "config"
    config_file = os.path.join(config_dir, "config.json")
    config_example = os.path.join(config_dir, "config.json.example")
    cookies_example = os.path.join(config_dir, "cookies.json.example")

    if os.path.exists(config_file):
        print("配置文件已存在，如需重新初始化请先删除 config/config.json")
        return

    print("=" * 50)
    print("首次使用向导")
    print("=" * 50)
    print()

    if os.path.exists(config_example):
        print("检测到配置文件模板，正在复制...")
        with open(config_example, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ config.json 已创建")

    if os.path.exists(cookies_example):
        cookies_file = os.path.join(config_dir, "cookies.json")
        with open(cookies_example, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(cookies_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ cookies.json 已创建")

    print()
    print("请编辑 config/config.json，填写以下信息：")
    print("  - login.username: 用户名")
    print("  - login.password: 密码")
    print("  - target_url: 目标URL")
    print("  - headers.cookie: Cookie值")
    print("  - cookies中的token和sensorsdata值")
    print()
    print("配置文件已创建在 config/ 目录")
    print("请手动编辑后运行程序")

if __name__ == "__main__":
    main()