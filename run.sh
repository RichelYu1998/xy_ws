#!/bin/bash

echo "========================================"
echo "Szwego商品爬虫和货号对比工具"
echo "========================================"
echo ""

if [ -d ".venv" ]; then
    .venv/bin/python main.py
else
    echo "虚拟环境不存在，请先创建虚拟环境"
    echo "运行: python3 -m venv .venv"
    echo "然后运行: .venv/bin/pip install -r requirements.txt"
    echo "最后运行: .venv/bin/playwright install chromium"
fi