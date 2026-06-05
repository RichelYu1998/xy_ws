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

            FASTEST_MIRROR="https://mirrors.aliyun.com/pypi/simple/"
            FASTEST_HOST="mirrors.aliyun.com"
            FASTEST_NAME="阿里云"
            MIN_TIME=999

            ALIYUN_TIME=$($PYTHON_CMD -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('https://mirrors.aliyun.com/pypi/simple/', timeout=3); print(round(time.time()-start, 3))" 2>/dev/null || echo "999")
            if [ "$ALIYUN_TIME" != "999" ]; then
                MIN_TIME=$ALIYUN_TIME
                FASTEST_NAME="阿里云"
                echo "[*] 阿里云速度: ${ALIYUN_TIME}秒"
            else
                echo "[*] 阿里云速度: 失败"
            fi

            echo "[*] 测试镜像源 2/5: 清华"
            TSINGHUA_TIME=$($PYTHON_CMD -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('https://pypi.tuna.tsinghua.edu.cn/simple/', timeout=3); print(round(time.time()-start, 3))" 2>/dev/null || echo "999")
            if [ "$TSINGHUA_TIME" != "999" ]; then
                if (( $(echo "$TSINGHUA_TIME < $MIN_TIME" | bc -l) )); then
                    MIN_TIME=$TSINGHUA_TIME
                    FASTEST_MIRROR="https://pypi.tuna.tsinghua.edu.cn/simple/"
                    FASTEST_HOST="pypi.tuna.tsinghua.edu.cn"
                    FASTEST_NAME="清华"
                    echo "[*] 清华速度: ${TSINGHUA_TIME}秒 (新最快)"
                else
                    echo "[*] 清华速度: ${TSINGHUA_TIME}秒"
                fi
            else
                echo "[*] 清华速度: 失败"
            fi

            echo "[*] 测试镜像源 3/5: 腾讯云"
            TENCENT_TIME=$($PYTHON_CMD -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('https://mirrors.cloud.tencent.com/pypi/simple/', timeout=3); print(round(time.time()-start, 3))" 2>/dev/null || echo "999")
            if [ "$TENCENT_TIME" != "999" ]; then
                if (( $(echo "$TENCENT_TIME < $MIN_TIME" | bc -l) )); then
                    MIN_TIME=$TENCENT_TIME
                    FASTEST_MIRROR="https://mirrors.cloud.tencent.com/pypi/simple/"
                    FASTEST_HOST="mirrors.cloud.tencent.com"
                    FASTEST_NAME="腾讯云"
                    echo "[*] 腾讯云速度: ${TENCENT_TIME}秒 (新最快)"
                else
                    echo "[*] 腾讯云速度: ${TENCENT_TIME}秒"
                fi
            else
                echo "[*] 腾讯云速度: 失败"
            fi

            echo "[*] 测试镜像源 4/5: 中科大"
            USTC_TIME=$($PYTHON_CMD -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('https://mirrors.ustc.edu.cn/pypi/simple/', timeout=3); print(round(time.time()-start, 3))" 2>/dev/null || echo "999")
            if [ "$USTC_TIME" != "999" ]; then
                if (( $(echo "$USTC_TIME < $MIN_TIME" | bc -l) )); then
                    MIN_TIME=$USTC_TIME
                    FASTEST_MIRROR="https://mirrors.ustc.edu.cn/pypi/simple/"
                    FASTEST_HOST="mirrors.ustc.edu.cn"
                    FASTEST_NAME="中科大"
                    echo "[*] 中科大速度: ${USTC_TIME}秒 (新最快)"
                else
                    echo "[*] 中科大速度: ${USTC_TIME}秒"
                fi
            else
                echo "[*] 中科大速度: 失败"
            fi

            echo "[*] 测试镜像源 5/5: 豆瓣"
            DOUBAN_TIME=$($PYTHON_CMD -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('https://pypi.douban.com/simple/', timeout=3); print(round(time.time()-start, 3))" 2>/dev/null || echo "999")
            if [ "$DOUBAN_TIME" != "999" ]; then
                if (( $(echo "$DOUBAN_TIME < $MIN_TIME" | bc -l) )); then
                    MIN_TIME=$DOUBAN_TIME
                    FASTEST_MIRROR="https://pypi.douban.com/simple/"
                    FASTEST_HOST="pypi.douban.com"
                    FASTEST_NAME="豆瓣"
                    echo "[*] 豆瓣速度: ${DOUBAN_TIME}秒 (新最快)"
                else
                    echo "[*] 豆瓣速度: ${DOUBAN_TIME}秒"
                fi
            else
                echo "[*] 豆瓣速度: 失败"
            fi

            if [ "$MIN_TIME" = "999" ]; then
                FASTEST_MIRROR="https://mirrors.aliyun.com/pypi/simple/"
                FASTEST_HOST="mirrors.aliyun.com"
                FASTEST_NAME="阿里云"
            fi

            echo "[*] 最终选择最快镜像源: $FASTEST_NAME"
            echo "[global]" > "$VENV_PATH/pip_config/pip.conf"
            echo "index-url = $FASTEST_MIRROR" >> "$VENV_PATH/pip_config/pip.conf"
            echo "[install]" >> "$VENV_PATH/pip_config/pip.conf"
            echo "trusted-host = $FASTEST_HOST" >> "$VENV_PATH/pip_config/pip.conf"

            export PIP_CONFIG_FILE="$VENV_PATH/pip_config/pip.conf"
        fi

        pip install -r requirements.txt -q

        echo "[*] 测试Playwright CDN速度..."
        mkdir -p "$VENV_PATH/pw_cdn_test"
        FASTEST_PW_CDN=""
        FASTEST_PW_CDN_NAME=""
        MIN_PW_TIME=999

        PW_CDNS=(
            "npmmirror:https://npmmirror.com/mirrors/playwright/:npmmirror"
            "azureedge:https://playwright.azureedge.net/builds/:微软azure"
            "cdn:https://cdn.playwright.dev/:官方CDN"
        )

        for entry in "${PW_CDNS[@]}"; do
            IFS=':' read -r cdn_key cdn_url cdn_name <<< "$entry"
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