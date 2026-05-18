#!/bin/bash

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v2.6.0"
echo "========================================"

detect_python() {
    echo ""
    echo "========================================"
    echo "环境检测与配置"
    echo "========================================"
    echo "[1/6] 检测Python环境..."

    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        echo "Python版本：$(python3 --version 2>&1)"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        echo "Python版本：$(python --version 2>&1)"
    else
        echo "ERROR: Python环境检测失败"
        return 1
    fi
}

detect_venv() {
    echo "[2/6] 检测虚拟环境..."

    if [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
        echo "检测到虚拟环境：venv"
        VENV_EXISTS=1
        VENV_PATH="venv"
    elif [ -d ".venv" ] && [ -f ".venv/bin/activate" ]; then
        echo "检测到虚拟环境：.venv"
        VENV_EXISTS=1
        VENV_PATH=".venv"
    else
        echo "未检测到虚拟环境，将创建"
        VENV_EXISTS=0
        VENV_PATH=""
    fi
}

setup_venv() {
    echo "[3/6] 设置虚拟环境..."

    if [ "$VENV_EXISTS" -eq 0 ]; then
        echo "正在创建虚拟环境..."
        $PYTHON_CMD -m venv .venv
        VENV_PATH=".venv"
    fi

    source "$VENV_PATH/bin/activate"

    if [ -f "requirements.txt" ]; then
        echo "正在安装依赖..."
        pip install -r requirements.txt -q
    fi

    echo "虚拟环境设置完成"
}

check_config() {
    echo "[4/6] 检测配置文件..."

    mkdir -p config

    if [ -f "config/config.json" ]; then
        echo "配置文件存在"
    else
        echo "配置文件不存在，开始首次配置向导"
        auto_setup
    fi
}

auto_setup() {
    echo "[5/6] 自动配置..."

    echo ""
    echo "正在复制配置文件模板..."

    if [ -f "config/config.json.example" ]; then
        cp -f config/config.json.example config/config.json
        echo "✓ config.json 已创建"
    else
        echo "⚠ config.json.example 不存在"
    fi

    if [ -f "config/cookies.json.example" ]; then
        cp -f config/cookies.json.example config/cookies.json
        echo "✓ cookies.json 已创建"
    fi

    echo ""
    echo "========================================"
    echo "首次配置完成！"
    echo "========================================"
    echo ""
    echo "请编辑 config/config.json，填写以下信息："
    echo "  - login.username: 用户名"
    echo "  - login.password: 密码"
    echo "  - target_url: 目标URL"
    echo "  - headers.cookie: Cookie值"
    echo "  - cookies中的token和sensorsdata值"
    echo ""
    read -p "按回车键启动Web服务，或 Ctrl+C 退出: "
}

run_web() {
    echo "[6/6] 预启动隧道服务(加快首次启动速度)..."
    npx -y hostc@latest --help >/dev/null 2>&1
    echo "隧道服务就绪"

    echo ""
    echo "========================================"
    echo "启动Web服务和隧道..."
    echo "========================================"

    source "$VENV_PATH/bin/activate"

    # 后台启动 hostc 隧道并保存URL
    echo "正在启动隧道服务（公网URL会保存到 file/tunnel_url.txt）..."
    npx -y hostc@latest 8888 > file/tunnel_url.txt 2>&1 &
    HOSTC_PID=$!

    # 启动 Flask Web 服务
    echo ""
    echo "正在启动 Web 服务..."
    echo ""
    $PYTHON_CMD main.py --web

    # Flask 退出时清理 hostc 进程
    kill $HOSTC_PID 2>/dev/null
    deactivate
}

detect_python || exit 1
detect_venv || exit 1
setup_venv || exit 1
check_config || exit 1
run_web