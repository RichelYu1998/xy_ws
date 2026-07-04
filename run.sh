#!/bin/bash

VERSION="0.0.0"
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        VERSION=$("$cmd" -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')" 2>/dev/null) && break
    fi
done

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v${VERSION}"
echo "========================================"

echo ""
echo "[*] 清理临时文件..."
if [ -d "temp" ]; then
    TOTAL_SIZE_KB=$(du -sk temp 2>/dev/null | awk '{print $1}')
    LIMIT_SIZE_KB=3072
    if [ -n "$TOTAL_SIZE_KB" ] && [ "$TOTAL_SIZE_KB" -gt "$LIMIT_SIZE_KB" ]; then
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

VENV_PATH=".venv"
NODE_ENV_PATH=".node_env"
FASTEST_PIP_MIRROR=""
FASTEST_NPM_MIRROR=""

detect_python_env() {
    echo "========================================"
    echo "[1/6] 检测Python环境..."

    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        echo "Python版本：$(python3 --version 2>&1)"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        echo "Python版本：$(python --version 2>&1)"
    else
        echo "Python未在PATH中，正在尝试查找系统中的Python..."
        
        COMMON_PYTHON_PATHS=(
            "/usr/bin/python3"
            "/usr/local/bin/python3"
            "/opt/homebrew/bin/python3"
            "$HOME/.pyenv/shims/python3"
            "/usr/bin/python"
            "/usr/local/bin/python"
        )
        
        for py_path in "${COMMON_PYTHON_PATHS[@]}"; do
            if [ -x "$py_path" ]; then
                echo "[*] 发现Python: $py_path"
                export PATH="$(dirname "$py_path"):$PATH"
                PYTHON_CMD="$py_path"
                break
            fi
        done
        
        if [ -z "$PYTHON_CMD" ]; then
            echo "[WARNING] 系统中未找到Python，正在自动安装..."
            
            case "$(uname -s)" in
                Darwin)
                    if command -v brew &> /dev/null; then
                        echo "    使用Homebrew安装Python..."
                        brew install python
                    elif [ -f "/opt/homebrew/bin/brew" ]; then
                        echo "    使用Homebrew (Apple Silicon) 安装Python..."
                        /opt/homebrew/bin/brew install python
                    else
                        echo "[ERROR] 未检测到Homebrew，无法自动安装Python"
                        echo "请先安装Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
                        return 1
                    fi
                    ;;
                Linux)
                    if command -v apt-get &> /dev/null; then
                        echo "    使用apt安装Python..."
                        sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip
                    elif command -v yum &> /dev/null; then
                        echo "    使用yum安装Python..."
                        sudo yum install -y python3 python3-pip
                    elif command -v dnf &> /dev/null; then
                        echo "    使用dnf安装Python..."
                        sudo dnf install -y python3 python3-pip
                    elif command -v pacman &> /dev/null; then
                        echo "    使用pacman安装Python..."
                        sudo pacman -Syu --noconfirm python python-pip
                    else
                        echo "[ERROR] 无法识别包管理器，请手动安装Python"
                        return 1
                    fi
                    ;;
                *)
                    echo "[ERROR] 不支持的操作系统用于自动Python安装"
                    return 1
                    ;;
            esac
            
            if command -v python3 &> /dev/null; then
                PYTHON_CMD="python3"
                echo "[*] Python安装成功: $(python3 --version 2>&1)"
            elif command -v python &> /dev/null; then
                PYTHON_CMD="python"
                echo "[*] Python安装成功: $(python --version 2>&1)"
            else
                echo "[ERROR] Python安装失败"
                return 1
            fi
        fi
    fi
    
    if [ -z "$PYTHON_CMD" ]; then
        echo "[ERROR] 无法找到或安装Python"
        return 1
    fi

    echo ""
    echo "[*] 检测虚拟环境状态..."
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "当前已在虚拟环境中: $VIRTUAL_ENV"
        IN_VENV=1
    else
        echo "未在虚拟环境中"
        IN_VENV=0
    fi
    
    return 0
}

detect_node_env() {
    echo "[2/6] 检测Node.js环境..."

    if command -v node &> /dev/null; then
        echo "Node.js版本: $(node --version 2>&1)"
        echo "NPM版本: $(npm --version 2>&1)"
        return 0
    fi
    
    echo "Node.js未在PATH中，正在尝试查找或自动安装..."
    
    if command -v nvm &> /dev/null || [ -s "$HOME/.nvm/nvm.sh" ]; then
        echo "    发现NVM，正在使用NVM管理Node.js..."
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        
        nvm use default &>/dev/null || nvm use lts &>/dev/null
        
        if ! command -v node &> /dev/null; then
            echo "    NVM中未安装Node.js，正在安装LTS版本..."
            nvm install lts
            nvm use lts
            nvm alias default lts
        fi
        
        if command -v node &> /dev/null; then
            echo ""
            echo "Node.js已就绪: $(node --version 2>&1)"
            echo "NPM版本: $(npm --version 2>&1)"
            return 0
        else
            echo "[WARNING] NVM 安装 Node.js 失败，部分功能可能不可用"
            return 0
        fi
    fi
    
    case "$(uname -s)" in
        Darwin)
            if command -v brew &> /dev/null; then
                echo "    使用Homebrew安装Node.js..."
                brew install node
            elif [ -f "/opt/homebrew/bin/brew" ]; then
                echo "    使用Homebrew (Apple Silicon) 安装Node.js..."
                /opt/homebrew/bin/brew install node
            else
                echo "[WARNING] 未检测到Homebrew，无法自动安装Node.js"
                echo "请先安装Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
                return 0
            fi
            ;;
        Linux)
            if command -v apt-get &> /dev/null; then
                echo "    使用apt+nodesource安装Node.js..."
                curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
                sudo apt-get install -y nodejs
            elif command -v yum &> /dev/null; then
                echo "    使用yum+nodesource安装Node.js..."
                curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
                sudo yum install -y nodejs
            elif command -v dnf &> /dev/null; then
                echo "    使用dnf+nodesource安装Node.js..."
                curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
                sudo dnf install -y nodejs
            elif command -v pacman &> /dev/null; then
                echo "    使用pacman安装Node.js..."
                sudo pacman -Syu --noconfirm nodejs npm
            else
                echo "[WARNING] 无法识别包管理器，请手动安装Node.js"
                echo "推荐方式：curl -fsSL https://fnm.vercel.app/install | bash"
                return 0
            fi
            ;;
        *)
            echo "[WARNING] 不支持的操作系统用于自动Node.js安装，部分功能可能不可用"
            return 0
            ;;
    esac
    
    if command -v node &> /dev/null; then
        echo ""
        echo "Node.js安装成功: $(node --version 2>&1)"
        echo "NPM版本: $(npm --version 2>&1)"
        return 0
    else
        echo "[WARNING] Node.js安装失败，部分功能可能不可用"
        return 0
    fi
}

test_pip_mirrors() {
    echo "[3/6] 测试PIP加速镜像源..."

    if [ -z "$PYTHON_CMD" ]; then
        echo "[WARNING] Python未安装，跳过PIP镜像测试"
        FASTEST_PIP_MIRROR="https://pypi.org/simple/"
        return 0
    fi

    declare -a MIRRORS=(
        "https://pypi.tuna.tsinghua.edu.cn/simple|清华源"
        "https://mirrors.aliyun.com/pypi/simple/|阿里云"
        "https://pypi.douban.com/simple/|豆瓣"
        "https://pypi.mirrors.ustc.edu.cn/simple/|中科大"
    )

    MIN_TIME=9999
    BEST_MIRROR=""
    BEST_NAME=""

    for mirror_entry in "${MIRRORS[@]}"; do
        IFS='|' read -r MIRROR_URL MIRROR_NAME <<< "$mirror_entry"
        echo "    测试 $MIRROR_NAME..."
        
        TEST_TIME=$(curl -s -o /dev/null -w "%{time_connect}" --connect-timeout 1.5 --max-time 2 "$MIRROR_URL" 2>/dev/null)

        if [ -z "$TEST_TIME" ] || [ "$TEST_TIME" = "0.000" ] || [ "$TEST_TIME" = "0" ]; then
            echo "        $MIRROR_NAME: 超时/失败"
        else
            PIP_INT_TIME=$(echo "$TEST_TIME" | awk '{printf "%d", $1 * 1000}')
            echo "        $MIRROR_NAME: ${TEST_TIME}秒 (${PIP_INT_TIME}ms)"
            if [ "$PIP_INT_TIME" -lt "$MIN_TIME" ] 2>/dev/null; then
                MIN_TIME=$PIP_INT_TIME
                BEST_MIRROR="$MIRROR_URL"
                BEST_NAME="$MIRROR_NAME"
            fi
        fi
    done

    if [ -n "$BEST_MIRROR" ]; then
        FASTEST_PIP_MIRROR="$BEST_MIRROR"
        echo "[*] 最快PIP镜像: $BEST_NAME (${MIN_TIME}毫秒)"
    else
        echo "[WARNING] 所有镜像测试失败，使用默认PyPI源"
        FASTEST_PIP_MIRROR="https://pypi.org/simple/"
    fi
}

test_npm_mirrors() {
    echo "[4/6] 测试NPM加速镜像源..."

    if ! command -v npm &> /dev/null; then
        echo "[WARNING] npm未安装，跳过NPM镜像测试"
        return 0
    fi

    declare -a NPM_MIRRORS=(
        "https://registry.npmmirror.com|npmmirror淘宝"
        "https://registry.npmjs.org|官方源"
    )

    NPM_MIN_TIME=9999
    NPM_BEST_MIRROR=""
    NPM_BEST_NAME=""

    for npm_mirror_entry in "${NPM_MIRRORS[@]}"; do
        IFS='|' read -r NPM_URL NPM_NAME <<< "$npm_mirror_entry"
        echo "    测试 $NPM_NAME..."
        
        NPM_TEST_TIME=$(curl -s -o /dev/null -w "%{time_total}" --connect-timeout 3 "$NPM_URL" 2>/dev/null)

        if [ -z "$NPM_TEST_TIME" ] || [ "$NPM_TEST_TIME" = "0.000" ] || [ "$NPM_TEST_TIME" = "0" ]; then
            echo "        $NPM_NAME: 超时/失败"
        else
            NPM_INT_TIME=$(echo "$NPM_TEST_TIME" | awk '{printf "%d", $1 * 1000}')
            echo "        $NPM_NAME: ${NPM_TEST_TIME}秒 (${NPM_INT_TIME}ms)"
            if [ "$NPM_INT_TIME" -lt "$NPM_MIN_TIME" ] 2>/dev/null; then
                NPM_MIN_TIME=$NPM_INT_TIME
                NPM_BEST_MIRROR="$NPM_URL"
                NPM_BEST_NAME="$NPM_NAME"
            fi
        fi
    done

    if [ -n "$NPM_BEST_MIRROR" ]; then
        FASTEST_NPM_MIRROR="$NPM_BEST_MIRROR"
        echo "[*] 最快NPM镜像: $NPM_BEST_NAME (${NPM_MIN_TIME}毫秒)"
        
        if command -v npm &> /dev/null; then
            npm config set registry "$NPM_BEST_MIRROR"
            echo "[*] NPM镜像已设置为: $NPM_BEST_MIRROR"
        fi
    else
        echo "[WARNING] NPM镜像测试失败"
    fi
}

detect_venv() {
    echo "[5/6] 检测Python虚拟环境..."

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
    fi
}

setup_venv() {
    echo "[6/6] 设置Python虚拟环境并安装依赖..."

    if [ "$VENV_EXISTS" -eq 0 ]; then
        echo "正在创建虚拟环境到 $VENV_PATH..."
        "$PYTHON_CMD" -m venv "$VENV_PATH"
        
        if [ $? -ne 0 ]; then
            echo "ERROR: 创建虚拟环境失败"
            exit 1
        fi
        VENV_EXISTS=1
    fi

    if [ ! -d "$VENV_PATH" ]; then
        echo "ERROR: 虚拟环境路径不存在：$VENV_PATH"
        exit 1
    fi

    source "$VENV_PATH/bin/activate"

    if [ -n "$FASTEST_PIP_MIRROR" ]; then
        echo "[*] 配置PIP镜像源为: $FASTEST_PIP_MIRROR"
        
        mkdir -p "$VENV_PATH/pip_config"
        
        TRUSTED_HOST=$(echo "$FASTEST_PIP_MIRROR" | sed -E 's|^https?://([^/]+).*|\1|')
        
        cat > "$VENV_PATH/pip_config/pip.conf" << EOF
[global]
index-url = $FASTEST_PIP_MIRROR
trusted-host = $TRUSTED_HOST
[install]
trusted-host = $TRUSTED_HOST
EOF
        
        export PIP_CONFIG_FILE="$VENV_PATH/pip_config/pip.conf"
    fi

    if [ -f "requirements.txt" ]; then
        echo "正在安装Python依赖..."
        PIP_INSTALL_OK=0
        
        if [ -n "$FASTEST_PIP_MIRROR" ]; then
            pip install -r requirements.txt -i "$FASTEST_PIP_MIRROR" --disable-pip-version-check
            if [ $? -ne 0 ]; then
                echo "WARNING: 使用镜像源安装失败，尝试默认源..."
                pip install -r requirements.txt --disable-pip-version-check
                if [ $? -ne 0 ]; then
                    PIP_INSTALL_OK=1
                fi
            fi
        else
            pip install -r requirements.txt --disable-pip-version-check
            if [ $? -ne 0 ]; then
                PIP_INSTALL_OK=1
            fi
        fi

        if [ "$PIP_INSTALL_OK" -ne 0 ]; then
            echo "ERROR: 依赖安装完全失败"
            exit 1
        fi

        echo "[*] 安装Playwright浏览器..."
        "$VENV_PATH/bin/python" main.py --install-playwright
    fi

    echo "Python虚拟环境设置完成"
}

check_config() {
    echo "[*] 检测配置文件..."

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
    echo "[*] 自动配置..."

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
    echo "[*] 预启动隧道服务(加快首次启动速度)..."
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

    mkdir -p file
    WEB_PORT="${WEB_PORT:-8888}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] === Web服务启动 ===" >> file/web_output.log
    "$VENV_PATH/bin/python" main.py --web --port "$WEB_PORT" >> file/web_output.log 2>&1 &
    PYTHON_PID=$!

    echo "等待 Web 服务启动完成..."
    sleep 5

    FLASK_WAIT_COUNT=0
    FLASK_MAX_WAIT=30
    while [ $FLASK_WAIT_COUNT -lt $FLASK_MAX_WAIT ]; do
        if ! kill -0 $PYTHON_PID 2>/dev/null; then
            echo "[ERROR] Web 服务进程已退出，请检查 file/web_output.log"
            exit 1
        fi
        HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:$WEB_PORT" 2>/dev/null)
        if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "302" ]; then
            break
        fi
        FLASK_WAIT_COUNT=$((FLASK_WAIT_COUNT + 1))
        sleep 2
    done

    if [ $FLASK_WAIT_COUNT -ge $FLASK_MAX_WAIT ]; then
        echo "[WARNING] Web服务启动超时（等待了$((FLASK_MAX_WAIT * 2))秒），请检查日志: file/web_output.log"
    fi

    echo "Web 服务已就绪，正在启动隧道..."
    npx -y hostc@latest "$WEB_PORT" --local-host localhost > file/tunnel_url.txt 2>&1 &
    TUNNEL_PID=$!

    sleep 2

    if ! kill -0 $TUNNEL_PID 2>/dev/null; then
        echo "[WARNING] 隧道服务启动失败，本地访问仍可用"
    fi

    echo ""
    echo "========================================"
    echo "启动完成！"
    echo "========================================"
    echo ""
    echo "本地访问: http://localhost:$WEB_PORT"
    echo "公网访问: 查看 file/tunnel_url.txt"
    echo "Web日志: 查看 file/web_output.log"
    echo ""
    echo "关闭此窗口可停止服务，或使用 Ctrl+C"
    echo ""

    (
        while true; do
            sleep 60
            if [ -d "temp" ]; then
                TOTAL_SIZE_KB=$(du -sk temp 2>/dev/null | awk '{print $1}')
                LIMIT_SIZE_KB=3072
                if [ -n "$TOTAL_SIZE_KB" ] && [ "$TOTAL_SIZE_KB" -gt "$LIMIT_SIZE_KB" ]; then
                    rm -rf temp/*
                    echo "[*] 定时检查: temp目录超过3MB，已清理所有文件"
                fi
            fi
        done
    ) &
    CLEANUP_PID=$!

    wait $PYTHON_PID $TUNNEL_PID 2>/dev/null
    kill $CLEANUP_PID 2>/dev/null
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
    if [ -n "$CLEANUP_PID" ]; then
        kill -15 $CLEANUP_PID 2>/dev/null
    fi
    pkill -f "python main.py" >/dev/null 2>&1
    pkill -f "hostc" >/dev/null 2>&1
    echo "清理完成"
    exit 0
}

main() {
    detect_python_env || exit 1
    detect_node_env
    test_pip_mirrors
    test_npm_mirrors
    detect_venv
    setup_venv
    check_config
}

trap cleanup_exit INT TERM EXIT

main