#!/bin/bash

echo "========================================"
echo "   Szwego爬虫 - 配置文件初始化脚本"
echo "========================================"
echo ""

if [ ! -f "config/config.json" ]; then
    echo "正在创建 config.json..."
    cp config/config.json.example config/config.json

    echo ""
    echo "请编辑 config/config.json，填写以下信息："
    echo "  - login.username: 用户名"
    echo "  - login.password: 密码"
    echo "  - target_url: 目标URL"
    echo "  - headers.cookie: Cookie值"
    echo "  - cookies中的token和sensorsdata值"
    echo ""
else
    echo "config.json 已存在，跳过创建。"
fi

if [ ! -f "config/cookies.json" ]; then
    echo "正在创建 cookies.json..."
    cp config/cookies.json.example config/cookies.json

    echo ""
    echo "请编辑 config/cookies.json，填写以下信息："
    echo "  - token值"
    echo "  - sensorsdata2015jssdkcross值"
    echo ""
else
    echo "cookies.json 已存在，跳过创建。"
fi

echo "========================================"
echo "   初始化完成！"
echo "========================================"