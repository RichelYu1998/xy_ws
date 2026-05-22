#!/bin/bash

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v2.6.0"
echo "========================================"

detect_python() {
    echo ""
    echo "========================================"
    echo "环境检测与配置"
    echo "========================================"
    echo "[1/5] 检测Python环境..."

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
    echo "[2/5] 检测虚拟环境..."

    if [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
        echo "检测到虚拟环境：venv"
        VENV_EXISTS=1
        VENV_PATH="venv"
    elif [ -d ".venv" ] && [ -f ".venv/bin/activate" ]; then
        echo "检测到虚拟环境：.venv"
        VENV_EXISTS=1
        VENV_PATH=".venv"
    else
        echo "未检测到虚拟环境"
        VENV_EXISTS=0
        VENV_PATH=""
    fi
}

setup_venv() {
    echo "[3/5] 设置虚拟环境..."

    if [ "$VENV_EXISTS" -eq 0 ]; then
        echo "正在创建虚拟环境..."
        $PYTHON_CMD -m venv .venv
        VENV_PATH=".venv"
    fi

    source "$VENV_PATH/bin/activate"

    if [ -f "requirements.txt" ]; then
        echo "正在安装依赖..."

        ALIYUN_MIRROR="https://mirrors.aliyun.com/pypi/simple/"
        USE_ALIYUN=0

        if [ -f "$VENV_PATH/pip.conf" ]; then
            if grep -q "aliyun" "$VENV_PATH/pip.conf" 2>/dev/null; then
                USE_ALIYUN=1
            fi
        fi

        if [ "$USE_ALIYUN" -eq 0 ]; then
            echo "[*] 检测到未配置pip镜像源，启用阿里云加速..."
            mkdir -p "$VENV_PATH/pip_config"
            echo "[global]" > "$VENV_PATH/pip_config/pip.conf"
            echo "index-url = $ALIYUN_MIRROR" >> "$VENV_PATH/pip_config/pip.conf"
            echo "[install]" >> "$VENV_PATH/pip_config/pip.conf"
            echo "trusted-host = mirrors.aliyun.com" >> "$VENV_PATH/pip_config/pip.conf"

            export PIP_CONFIG_FILE="$VENV_PATH/pip_config/pip.conf"
        fi

        pip install -r requirements.txt -q
    fi

    echo "虚拟环境设置完成"
}

check_config() {
    echo "[4/5] 检测配置文件..."

    mkdir -p config

    if [ -f "config/config.json" ]; then
        echo "配置文件存在"
        run_web
    else
        echo "配置文件不存在，开始首次配置向导"
        auto_setup
    fi
}

auto_setup() {
    echo "[5/5] 自动配置..."

    echo ""
    echo "正在复制配置文件模板..."

    if [ -f "config/config.json.example" ]; then
        cp -f config/config.json.example config/config.json
        echo "[OK] config.json 已创建"
    else
        echo "[WARNING] config.json.example 不存在"
    fi

    if [ -f "config/cookies.json.example" ]; then
        cp -f config/cookies.json.example config/cookies.json
        echo "[OK] cookies.json 已创建"
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
    read -p "按回车键继续，或 Ctrl+C 退出: "
    run_web
}

run_web() {
    echo "[5/5] 预启动隧道服务(加快首次启动速度)..."
    npx -y hostc@latest --help >/dev/null 2>&1
    echo "隧道服务就绪"

    echo ""
    echo "========================================"
    echo "启动Web服务和隧道..."
    echo "========================================"

    source "$VENV_PATH/bin/activate"

    echo ""
    echo "正在启动 Web 服务..."
    echo ""

    python main.py --web 2>&1 | tee file/web_output.log &
    PYTHON_PID=$!

    echo "等待 Web 服务启动完成..."
    sleep 5

    if ! kill -0 $PYTHON_PID 2>/dev/null; then
        echo "Web 服务启动失败，请检查 file/web_output.log"
        exit 1
    fi

    echo "Web 服务已就绪，正在启动隧道..."
    npx -y hostc@latest 8888 --local-host 127.0.0.1 > file/tunnel_url.txt 2>&1 &
    TUNNEL_PID=$!

    sleep 2

    if ! kill -0 $TUNNEL_PID 2>/dev/null; then
        echo "隧道服务启动失败"
        kill $PYTHON_PID 2>/dev/null
        exit 1
    fi

    echo ""
    echo "========================================"
    echo "启动完成！"
    echo "========================================"
    echo ""
    echo "本地访问: http://localhost:8888"
    echo "公网访问: 查看 file/tunnel_url.txt"
    echo "Web日志: 查看 file/web_output.log"
    echo ""
    echo "关闭此窗口可停止服务，或使用 Ctrl+C"
    echo ""

    wait $PYTHON_PID $TUNNEL_PID
}

cleanup_exit() {
    echo ""
    echo "正在清理进程..."
    if [ -n "$PYTHON_PID" ]; then
        kill -15 $PYTHON_PID 2>/dev/null
    fi
    if [ -n "$TUNNEL_PID" ]; then
        kill -15 $TUNNEL_PID 2>/dev/null
    fi
    pkill -f "python main.py" >/dev/null 2>&1
    pkill -f "hostc" >/dev/null 2>&1
    echo "清理完成"
    exit 0
}

main() {
    detect_python || exit 1
    detect_venv
    setup_venv
    check_config
}

trap cleanup_exit INT TERM EXIT

main