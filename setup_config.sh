#!/bin/bash

echo "========================================"
echo "   Szwego爬虫 - 配置文件初始化"
echo "========================================"
echo ""

read -p "请输入用户名: " USERNAME
read -p "请输入密码: " PASSWORD
read -p "请输入目标URL: " URL
read -p "请输入token: " TOKEN
read -p "请输入sensorsdata(可留空): " SENSORS
read -p "请输入Excel路径(可留空): " EXCEL

python3 setup_config.py -u "$USERNAME" -p "$PASSWORD" -l "$URL" -t "$TOKEN" -s "$SENSORS" -e "$EXCEL"

echo ""
echo "========================================"
echo "   初始化完成！"
echo "========================================"