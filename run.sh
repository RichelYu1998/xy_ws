#!/bin/bash

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v1.8.0"
echo "========================================"
echo ""

# 获取开始时间
START_TIME=$(date "+%Y-%m-%d %H:%M:%S")
echo "开始时间: $START_TIME"
echo ""

# 检查Python版本
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python 3"
    echo "请先安装Python 3.7或更高版本"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "检测到Python版本: $PYTHON_VERSION"

# 检查虚拟环境
if [ ! -d ".venv" ]; then
    echo "虚拟环境不存在，正在创建..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "创建虚拟环境失败"
        exit 1
    fi
    echo "正在安装依赖..."
    .venv/bin/pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "安装依赖失败"
        exit 1
    fi
    echo "正在安装Playwright浏览器..."
    .venv/bin/playwright install chromium
fi

# 检查配置文件
if [ ! -f "config/config.json" ]; then
    echo "配置文件不存在，请先配置 config/config.json"
    exit 1
fi

# 运行程序
.venv/bin/python main.py

# 获取结束时间
END_TIME=$(date "+%Y-%m-%d %H:%M:%S")
echo ""
echo "========================================"
echo "结束时间: $END_TIME"
echo "========================================"