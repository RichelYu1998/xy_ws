#!/bin/bash

VERSION=$(python3 -c "import re; m=re.search(r'###\s+v(\d+\.\d+\.\d+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')" 2>/dev/null || python -c "import re; m=re.search(r'###\s+v(\d+\.\d+\.\d+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')")

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v${VERSION}"
echo "========================================"

echo ""
echo "[*] 清理临时文件..."
if [ -d "temp" ]; then
    TOTAL_SIZE=$(du -sb temp | awk '{print $1}')
    LIMIT_SIZE=3145728
    if [ "$TOTAL_SIZE" -gt "$LIMIT_SIZE" ]; then
        rm -rf temp/*
        echo "[*] temp目录超过3MB，已清理所有文件"
    else
        echo "[*] temp目录未超过3MB，跳过清理"
    fi
else
    echo "[*] temp目录不存在，跳过清理"
fi

echo "[*] 清理浏览器临时文件..."
if [ -d "playwright-browsers" ]; then
    echo "[*] 删除playwright-browsers目录中的临时zip文件..."
    rm -f playwright-browsers/*.zip
    echo "[*] 浏览器临时文件清理完成"
else
    echo "[*] playwright-browsers目录不存在，跳过清理"
fi

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
            echo "[*] 检测到未配置pip镜像源，调用Python测速..."
            VIRTUAL_ENV="$VENV_PATH" $PYTHON_CMD main.py --select-pip-mirror
        fi

        export PIP_CONFIG_FILE="$VENV_PATH/pip.conf"

        pip install -r requirements.txt -q

        echo "[*] 测试Playwright CDN速度..."
        FASTEST_PW_CDN=""
        FASTEST_PW_CDN_NAME=""
        MIN_PW_TIME=999

        for cdn_entry in \
            "npmmirror https://npmmirror.com/mirrors/playwright/ npmmirror" \
            "azureedge https://playwright.azureedge.net/builds/ azureedge" \
            "cdn https://cdn.playwright.dev/ cdn"; do
            cdn_key=$(echo "$cdn_entry" | cut -d' ' -f1)
            cdn_url=$(echo "$cdn_entry" | cut -d' ' -f2)
            cdn_name=$(echo "$cdn_entry" | cut -d' ' -f3)
            echo "    测试 $cdn_name..."
            CDN_TIME=$($PYTHON_CMD -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('${cdn_url}', timeout=3); print(round(time.time()-start, 3))" 2>/dev/null || echo "999")
            if [ "$CDN_TIME" != "999" ]; then
                echo "    $cdn_name: ${CDN_TIME}秒"
                if (( $(echo "$CDN_TIME < $MIN_PW_TIME" | bc -l) )); then
                    MIN_PW_TIME=$CDN_TIME
                    FASTEST_PW_CDN="$cdn_url"
                    FASTEST_PW_CDN_NAME="$cdn_name"
                fi
            else
                echo "    $cdn_name: 失败"
            fi
        done

        if [ -z "$FASTEST_PW_CDN" ]; then
            echo "[WARNING] 所有Playwright CDN均无法访问，将尝试默认安装"
            unset PLAYWRIGHT_DOWNLOAD_HOST
        else
            echo "[*] 最终选择最快Playwright CDN: $FASTEST_PW_CDN_NAME (${MIN_PW_TIME}秒)"
            export PLAYWRIGHT_DOWNLOAD_HOST="$FASTEST_PW_CDN"
        fi

        echo "[*] 安装Playwright浏览器..."
        
        # 创建浏览器目录
        BROWSER_DIR="playwright-browsers"
        mkdir -p "$BROWSER_DIR"
        
        # 下载Playwright浏览器zip
        echo "[*] 下载Playwright Chromium浏览器..."
        PW_VERSION="1.59.0"
        BROWSER_URL="${FASTEST_PW_CDN}builds/chromium/1200/chromium-linux.zip"
        BROWSER_ZIP="$BROWSER_DIR/chromium-linux.zip"
        
        if [ ! -f "$BROWSER_DIR/chrome-linux64/chrome" ]; then
            echo "[*] 从 $FASTEST_PW_CDN_NAME 下载浏览器..."
            curl -L -o "$BROWSER_ZIP" "$BROWSER_URL" || wget -O "$BROWSER_ZIP" "$BROWSER_URL"
            
            if [ -f "$BROWSER_ZIP" ]; then
                echo "[*] 解压浏览器到 $BROWSER_DIR..."
                unzip -o "$BROWSER_ZIP" -d "$BROWSER_DIR"
                
                if [ -d "$BROWSER_DIR/chrome-linux64" ]; then
                    echo "[*] 浏览器解压成功: $BROWSER_DIR/chrome-linux64/chrome"
                    chmod +x "$BROWSER_DIR/chrome-linux64/chrome" 2>/dev/null
                    echo "[*] 删除临时zip文件..."
                    rm -f "$BROWSER_ZIP"
                else
                    echo "[WARNING] 浏览器解压失败，目录结构不正确"
                fi
            else
                echo "[WARNING] 浏览器下载失败"
            fi
        else
            echo "[*] 浏览器已存在，跳过下载"
        fi
        
        # 安装Python playwright包
        $PYTHON_CMD main.py --install-playwright
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

    (
        while true; do
            sleep 60
            if [ -d "temp" ]; then
                TOTAL_SIZE=$(du -sb temp 2>/dev/null | awk '{print $1}')
                LIMIT_SIZE=3145728
                if [ "$TOTAL_SIZE" -gt "$LIMIT_SIZE" ]; then
                    rm -rf temp/*
                    echo "[*] 定时检查: temp目录超过3MB，已清理所有文件"
                fi
            fi
        done
    ) &
    CLEANUP_PID=$!

    wait $PYTHON_PID $TUNNEL_PID
    kill $CLEANUP_PID 2>/dev/null
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