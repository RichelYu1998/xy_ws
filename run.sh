#!/bin/bash

VERSION=$(python3 -c "import re; m=re.search(r'###\s+v(\d+\.\d+\.\d+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')" 2>/dev/null || python -c "import re; m=re.search(r'###\s+v(\d+\.\d+\.\d+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')")

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v${VERSION}"
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

        if [ ! -f "$VENV_PATH/pip.conf" ]; then
            echo "[*] 检测到未配置pip镜像源，正在测试镜像源速度..."
            mkdir -p "$VENV_PATH/pip_config"

            MIRRORS=(
                "https://mirrors.aliyun.com/pypi/simple/|mirrors.aliyun.com"
                "https://pypi.tuna.tsinghua.edu.cn/simple/|pypi.tuna.tsinghua.edu.cn"
                "https://mirrors.cloud.tencent.com/pypi/simple/|mirrors.cloud.tencent.com"
                "https://mirrors.ustc.edu.cn/pypi/simple/|mirrors.ustc.edu.cn"
                "https://pypi.douban.com/simple/|pypi.douban.com"
            )

            FASTEST_MIRROR="https://mirrors.aliyun.com/pypi/simple/"
            FASTEST_HOST="mirrors.aliyun.com"
            MIN_TIME=999

            for mirror in "${MIRRORS[@]}"; do
                IFS='|' read -r url host <<< "$mirror"
                echo "[*] 测试镜像源: $url"
                start_time=$(python3 -c "import time; print(time.time())" 2>/dev/null || python -c "import time; print(time.time())")
                python3 -c "import urllib.request; urllib.request.urlopen('$url', timeout=3)" 2>/dev/null || python -c "import urllib.request; urllib.request.urlopen('$url', timeout=3)" 2>/dev/null
                if [ $? -eq 0 ]; then
                    end_time=$(python3 -c "import time; print(time.time())" 2>/dev/null || python -c "import time; print(time.time())")
                    elapsed=$(python3 -c "print($end_time - $start_time)" 2>/dev/null || python -c "print($end_time - $start_time)")
                    if (( $(echo "$elapsed < $MIN_TIME" | bc -l) )); then
                        MIN_TIME=$elapsed
                        FASTEST_MIRROR=$url
                        FASTEST_HOST=$host
                        echo "[*] 更新最快镜像源: $url ($elapsed秒)"
                    else
                        echo "[*] 镜像源速度: $url ($elapsed秒)"
                    fi
                else
                    echo "[*] 镜像源不可用: $url"
                fi
            done

            echo "[*] 最终选择最快镜像源: $FASTEST_MIRROR ($MIN_TIME秒)"
            echo "[global]" > "$VENV_PATH/pip_config/pip.conf"
            echo "index-url = $FASTEST_MIRROR" >> "$VENV_PATH/pip_config/pip.conf"
            echo "[install]" >> "$VENV_PATH/pip_config/pip.conf"
            echo "trusted-host = $FASTEST_HOST" >> "$VENV_PATH/pip_config/pip.conf"

            export PIP_CONFIG_FILE="$VENV_PATH/pip_config/pip.conf"
        fi

        pip install -r requirements.txt -q

        echo "[*] 配置Playwright CDN加速..."
        export PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/

        echo "[*] 安装Playwright浏览器..."
        python3 -m playwright install chromium --with-deps 2>/dev/null || python -m playwright install chromium --with-deps 2>/dev/null
        if [ $? -ne 0 ]; then
            echo "[WARNING] Playwright浏览器安装失败，将在首次运行时自动安装"
        fi
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

    > file/web_output.log  # 清空日志文件
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