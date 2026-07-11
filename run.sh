#!/bin/bash

cd "$(dirname "$0")"

VERSION="0.0.0"
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        VERSION=$("$cmd" -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')" 2>/dev/null) && break
    fi
done

mkdir -p file
LOG_FILE="$(pwd)/file/web_output.log"
> "$LOG_FILE"

_HAS_GNU_DATE=false
if date '+%3N' 2>/dev/null | grep -qE '^[0-9]{3}$'; then
    _HAS_GNU_DATE=true
fi

_ms_timestamp() {
    if $_HAS_GNU_DATE; then
        date '+%Y-%m-%d %H:%M:%S.%3N'
    else
        local ms
        ms=$(python3 -c "from datetime import datetime; print(datetime.now().microsecond//1000)" 2>/dev/null || echo "000")
        printf '%s.%03d' "$(date '+%Y-%m-%d %H:%M:%S')" "${ms:-000}"
    fi
}

log() {
    TIMESTAMP="$(_ms_timestamp)"
    echo "[$TIMESTAMP] $*"
    [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ] && echo "[$TIMESTAMP] $*" >> "$LOG_FILE" 2>/dev/null
}

log_blank() {
    echo ""
    [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ] && echo "" >> "$LOG_FILE" 2>/dev/null
}

log_console_only() {
    TIMESTAMP="$(_ms_timestamp)"
    echo "[$TIMESTAMP] $*"
}

log_blank_console_only() {
    echo ""
}

log "========================================"
log "Szwego商品爬虫和货号对比工具 - v${VERSION}"
log "========================================"

log_blank
log "[*] 清理残留进程..."
pkill -9 -f "python.*main.py" 2>/dev/null || true
pkill -9 -f "hostc" 2>/dev/null || true
sleep 1
log "[*] 残留进程清理完成"

log_blank
log "[*] 检查 hostc 隧道工具..."
HOSTC_BIN="$(pwd)/dist/node_modules/.bin/hostc"
if [ ! -f "$HOSTC_BIN" ]; then
    log "[*] 本地未找到 hostc，开始安装..."
    install_hostc
    if [ ! -f "$HOSTC_BIN" ]; then
        log "[WARNING] hostc 安装失败，隧道将不可用"
    fi
fi
if [ -f "$HOSTC_BIN" ]; then
    HOSTC_VER=$("$HOSTC_BIN" --version 2>/dev/null || echo "unknown")
    log "[*] hostc v${HOSTC_VER} 已就绪"
fi

log_blank
log "[*] 启动 hostc 隧道（后台运行，不阻塞）..."
echo -n > "file/tunnel_url.txt"
if [ -f "$HOSTC_BIN" ]; then
    "$HOSTC_BIN" 8888 --local-host localhost >> file/tunnel_url.txt 2>&1 < /dev/null &
else
    npx -y hostc@latest 8888 --local-host localhost >> file/tunnel_url.txt 2>&1 < /dev/null &
fi
log "[*] hostc 已在后台启动，将在后续步骤中获取URL"

log_blank
log "[*] 清理临时文件..."
if [ -d "temp" ]; then
    TOTAL_SIZE_KB=$(du -sk temp 2>/dev/null | awk '{print $1}')
    LIMIT_SIZE_KB=3072
    if [ -n "$TOTAL_SIZE_KB" ] && [ "$TOTAL_SIZE_KB" -gt "$LIMIT_SIZE_KB" ]; then
        rm -rf temp/*
        log "[*] temp目录超过3MB，已清理所有文件"
    else
        log "[*] temp目录未超过3MB，跳过清理"
    fi
else
    log "[*] temp目录不存在，跳过清理"
fi

log "[*] 清理浏览器临时文件..."
if [ -d "playwright-browsers" ]; then
    log "[*] 删除playwright-browsers目录中的临时zip文件..."
    rm -f playwright-browsers/*.zip
    log "[*] 浏览器临时文件清理完成"
else
    log "[*] playwright-browsers目录不存在，跳过清理"
fi

VENV_PATH=".venv"
NODE_ENV_PATH=".node_env"
FASTEST_PIP_MIRROR=""
FASTEST_NPM_MIRROR=""

detect_python_env() {
    log_blank
    log "========================================"
    log "综合环境检测与配置"
    log "========================================"

    log "[1/6] 检测Python环境..."

    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        log "Python版本：$(python3 --version 2>&1)"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        log "Python版本：$(python --version 2>&1)"
    else
        log "Python未在PATH中，正在尝试查找系统中的Python..."
        
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
                log "[*] 发现Python: $py_path"
                export PATH="$(dirname "$py_path"):$PATH"
                PYTHON_CMD="$py_path"
                break
            fi
        done
        
        if [ -z "$PYTHON_CMD" ]; then
            log "[WARNING] 系统中未找到Python，正在自动安装..."
            
            case "$(uname -s)" in
                Darwin)
                    if command -v brew &> /dev/null; then
                        log "    使用Homebrew安装Python..."
                        brew install python
                    elif [ -f "/opt/homebrew/bin/brew" ]; then
                        log "    使用Homebrew (Apple Silicon) 安装Python..."
                        /opt/homebrew/bin/brew install python
                    else
                        log "[ERROR] 未检测到Homebrew，无法自动安装Python"
                        log "请先安装Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
                        return 1
                    fi
                    ;;
                Linux)
                    if command -v apt-get &> /dev/null; then
                        log "    使用apt安装Python..."
                        sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip
                    elif command -v yum &> /dev/null; then
                        log "    使用yum安装Python..."
                        sudo yum install -y python3 python3-pip
                    elif command -v dnf &> /dev/null; then
                        log "    使用dnf安装Python..."
                        sudo dnf install -y python3 python3-pip
                    elif command -v pacman &> /dev/null; then
                        log "    使用pacman安装Python..."
                        sudo pacman -Syu --noconfirm python python-pip
                    else
                        log "[ERROR] 无法识别包管理器，请手动安装Python"
                        return 1
                    fi
                    ;;
                *)
                    log "[ERROR] 不支持的操作系统用于自动Python安装"
                    return 1
                    ;;
            esac
            
            if command -v python3 &> /dev/null; then
                PYTHON_CMD="python3"
                log "[*] Python安装成功: $(python3 --version 2>&1)"
            elif command -v python &> /dev/null; then
                PYTHON_CMD="python"
                log "[*] Python安装成功: $(python --version 2>&1)"
            else
                log "[ERROR] Python安装失败"
                return 1
            fi
        fi
    fi
    
    if [ -z "$PYTHON_CMD" ]; then
        log "[ERROR] 无法找到或安装Python"
        return 1
    fi

    log_blank
    log "[*] 检测虚拟环境状态..."
    if [ -n "$VIRTUAL_ENV" ]; then
        log "当前已在虚拟环境中: $VIRTUAL_ENV"
        IN_VENV=1
    else
        log "未在虚拟环境中"
        IN_VENV=0
    fi
    
    return 0
}

detect_node_env() {
    log "[2/6] 检测Node.js环境..."

    if command -v node &> /dev/null; then
        log "Node.js版本: $(node --version 2>&1)"
        log "NPM版本: $(npm --version 2>&1)"
        return 0
    fi
    
    log "Node.js未在PATH中，正在尝试查找或自动安装..."
    
    if command -v nvm &> /dev/null || [ -s "$HOME/.nvm/nvm.sh" ]; then
        log "    发现NVM，正在使用NVM管理Node.js..."
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        
        nvm use default &>/dev/null || nvm use lts &>/dev/null
        
        if ! command -v node &> /dev/null; then
            log "    NVM中未安装Node.js，正在安装LTS版本..."
            nvm install lts
            nvm use lts
            nvm alias default lts
        fi
        
        if command -v node &> /dev/null; then
            log_blank
            log "Node.js已就绪: $(node --version 2>&1)"
            log "NPM版本: $(npm --version 2>&1)"
            return 0
        else
            log "[WARNING] NVM 安装 Node.js 失败，部分功能可能不可用"
            return 0
        fi
    fi
    
    case "$(uname -s)" in
        Darwin)
            if command -v brew &> /dev/null; then
                log "    使用Homebrew安装Node.js..."
                brew install node
            elif [ -f "/opt/homebrew/bin/brew" ]; then
                log "    使用Homebrew (Apple Silicon) 安装Node.js..."
                /opt/homebrew/bin/brew install node
            else
                log "[WARNING] 未检测到Homebrew，无法自动安装Node.js"
                log "请先安装Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
                return 0
            fi
            ;;
        Linux)
            if command -v apt-get &> /dev/null; then
                log "    使用apt+nodesource安装Node.js..."
                curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
                sudo apt-get install -y nodejs
            elif command -v yum &> /dev/null; then
                log "    使用yum+nodesource安装Node.js..."
                curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
                sudo yum install -y nodejs
            elif command -v dnf &> /dev/null; then
                log "    使用dnf+nodesource安装Node.js..."
                curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
                sudo dnf install -y nodejs
            elif command -v pacman &> /dev/null; then
                log "    使用pacman安装Node.js..."
                sudo pacman -Syu --noconfirm nodejs npm
            else
                log "[WARNING] 无法识别包管理器，请手动安装Node.js"
                log "推荐方式：curl -fsSL https://fnm.vercel.app/install | bash"
                return 0
            fi
            ;;
        *)
            log "[WARNING] 不支持的操作系统用于自动Node.js安装，部分功能可能不可用"
            return 0
            ;;
    esac
    
    if command -v node &> /dev/null; then
        log_blank
        log "Node.js安装成功: $(node --version 2>&1)"
        log "NPM版本: $(npm --version 2>&1)"
        return 0
    else
        log "[WARNING] Node.js安装失败，部分功能可能不可用"
        return 0
    fi
}

test_pip_mirrors() {
    log "[3/6] 测试PIP加速镜像源..."

    if [ -z "$PYTHON_CMD" ]; then
        log "[WARNING] Python未安装，跳过PIP镜像测试"
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
        log "    测试 $MIRROR_NAME..."
        
        TEST_TIME=$(curl -s -o /dev/null -w "%{time_connect}" --connect-timeout 1.5 --max-time 2 "$MIRROR_URL" 2>/dev/null)

        if [ -z "$TEST_TIME" ] || [ "$TEST_TIME" = "0.000" ] || [ "$TEST_TIME" = "0" ]; then
            log "        $MIRROR_NAME: 超时/失败"
        else
            PIP_INT_TIME=$(echo "$TEST_TIME" | awk '{printf "%d", $1 * 1000}')
            log "        $MIRROR_NAME: ${TEST_TIME}秒 [${PIP_INT_TIME}ms]"
            if [ "$PIP_INT_TIME" -lt "$MIN_TIME" ] 2>/dev/null; then
                MIN_TIME=$PIP_INT_TIME
                BEST_MIRROR="$MIRROR_URL"
                BEST_NAME="$MIRROR_NAME"
            fi
        fi
    done

    if [ -n "$BEST_MIRROR" ]; then
        FASTEST_PIP_MIRROR="$BEST_MIRROR"
        log_blank
        log "[*] 最快PIP镜像: $BEST_NAME [${MIN_TIME}毫秒]"
    else
        log "[WARNING] 所有镜像测试失败，使用默认PyPI源"
        FASTEST_PIP_MIRROR="https://pypi.org/simple/"
    fi
}

install_hostc() {
    log "[*] CDN轮询安装 hostc..."

    declare -a HOSTC_MIRRORS=(
        "https://registry.npmmirror.com|npmmirror淘宝"
        "https://repo.huaweicloud.com/repository/npm/|华为云"
        "https://registry.npmjs.org|官方源"
    )

    HOSTC_MIN_TIME=9999
    HOSTC_BEST_MIRROR=""
    HOSTC_BEST_NAME=""

    for hostc_mirror_entry in "${HOSTC_MIRRORS[@]}"; do
        IFS='|' read -r H_URL H_NAME <<< "$hostc_mirror_entry"
        log "    测试 $H_NAME..."

        H_TIME=$(curl -s -o /dev/null -w "%{time_total}" --connect-timeout 3 "$H_URL" 2>/dev/null)

        if [ -z "$H_TIME" ] || [ "$H_TIME" = "0.000" ] || [ "$H_TIME" = "0" ]; then
            log "        $H_NAME: 超时/失败"
        else
            H_INT_TIME=$(echo "$H_TIME" | awk '{printf "%d", $1 * 1000}')
            log "        $H_NAME: ${H_TIME}秒 [${H_INT_TIME}ms]"
            if [ "$H_INT_TIME" -lt "$HOSTC_MIN_TIME" ] 2>/dev/null; then
                HOSTC_MIN_TIME=$H_INT_TIME
                HOSTC_BEST_MIRROR="$H_URL"
                HOSTC_BEST_NAME="$H_NAME"
            fi
        fi
    done

    if [ -z "$HOSTC_BEST_MIRROR" ]; then
        log "[WARNING] 所有CDN均不可用，尝试默认源安装..."
        HOSTC_BEST_MIRROR="https://registry.npmmirror.com"
        HOSTC_BEST_NAME="npmmirror淘宝(fallback)"
    fi

    log "[*] 使用 $HOSTC_BEST_NAME 安装 hostc..."
    npm install hostc@latest --registry "$HOSTC_BEST_MIRROR" --prefix dist 2>/dev/null
    if [ $? -ne 0 ]; then
        log "[ERROR] hostc 安装失败"
    else
        log "[*] hostc 安装成功"
    fi
}

test_npm_mirrors() {
    log "[4/6] 测试NPM加速镜像源..."

    if ! command -v npm &> /dev/null; then
        log "[WARNING] npm未安装，跳过NPM镜像测试"
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
        log "    测试 $NPM_NAME..."
        
        NPM_TEST_TIME=$(curl -s -o /dev/null -w "%{time_total}" --connect-timeout 3 "$NPM_URL" 2>/dev/null)

        if [ -z "$NPM_TEST_TIME" ] || [ "$NPM_TEST_TIME" = "0.000" ] || [ "$NPM_TEST_TIME" = "0" ]; then
            log "        $NPM_NAME: 超时/失败"
        else
            NPM_INT_TIME=$(echo "$NPM_TEST_TIME" | awk '{printf "%d", $1 * 1000}')
            log "        $NPM_NAME: ${NPM_TEST_TIME}秒 [${NPM_INT_TIME}ms]"
            if [ "$NPM_INT_TIME" -lt "$NPM_MIN_TIME" ] 2>/dev/null; then
                NPM_MIN_TIME=$NPM_INT_TIME
                NPM_BEST_MIRROR="$NPM_URL"
                NPM_BEST_NAME="$NPM_NAME"
            fi
        fi
    done

    if [ -n "$NPM_BEST_MIRROR" ]; then
        FASTEST_NPM_MIRROR="$NPM_BEST_MIRROR"
        log_blank
        log "[*] 最快NPM镜像: $NPM_BEST_NAME [${NPM_MIN_TIME}毫秒]"
        
        if command -v npm &> /dev/null; then
            npm config set registry "$NPM_BEST_MIRROR"
            log "[*] NPM镜像已设置为: $NPM_BEST_MIRROR"
        fi
    else
        log "[WARNING] NPM镜像测试失败"
    fi
}

detect_venv() {
    log "[5/6] 检测Python虚拟环境..."

    if [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
        log "检测到虚拟环境：venv"
        VENV_EXISTS=1
        VENV_PATH="venv"
    elif [ -d ".venv" ] && [ -f ".venv/bin/activate" ]; then
        log "检测到虚拟环境：.venv"
        VENV_EXISTS=1
        VENV_PATH=".venv"
    else
        log "未检测到虚拟环境"
        VENV_EXISTS=0
    fi
}

setup_venv() {
    log "[6/6] 设置Python虚拟环境并安装依赖..."

    if [ "$VENV_EXISTS" -eq 0 ]; then
        log "正在创建虚拟环境到 $VENV_PATH..."
        "$PYTHON_CMD" -m venv "$VENV_PATH"
        
        if [ $? -ne 0 ]; then
            log "ERROR: 创建虚拟环境失败"
            exit 1
        fi
        VENV_EXISTS=1
    fi

    if [ ! -d "$VENV_PATH" ]; then
        log "ERROR: 虚拟环境路径不存在：$VENV_PATH"
        exit 1
    fi

    source "$VENV_PATH/bin/activate"

    if [ -n "$FASTEST_PIP_MIRROR" ]; then
        log "[*] 配置PIP镜像源为: $FASTEST_PIP_MIRROR"
        
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
        log "[*] 检查Python依赖是否需要安装..."
        NEED_PIP_INSTALL=1
        "$VENV_PATH/bin/python" main.py --check-deps > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            log "[*] 所有Python依赖已满足，跳过安装"
            NEED_PIP_INSTALL=0
        else
            log "[*] 检测到缺失或版本不满足的依赖，开始安装..."
            NEED_PIP_INSTALL=1
        fi

        if [ "$NEED_PIP_INSTALL" -eq 1 ]; then
            PIP_INSTALL_OK=0
            
            if [ -n "$FASTEST_PIP_MIRROR" ]; then
                pip install -r requirements.txt -i "$FASTEST_PIP_MIRROR" --disable-pip-version-check
                if [ $? -ne 0 ]; then
                    log "WARNING: 使用镜像源安装失败，尝试默认源..."
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
                log "ERROR: 依赖安装完全失败"
                exit 1
            fi
        fi

        log "[*] 安装Playwright浏览器..."
        "$VENV_PATH/bin/python" main.py --install-playwright
    fi

    log "Python虚拟环境设置完成"
}

check_config() {
    log "[*] 检测配置文件..."

    mkdir -p config

    if [ -f "config/config.json" ]; then
        log "配置文件存在"
        run_web
    else
        log "配置文件不存在，开始首次配置向导"
        auto_setup
    fi
}

auto_setup() {
    log "[*] 自动配置..."

    log_blank
    log "正在复制配置文件模板..."

    if [ -f "config/config.json.example" ]; then
        cp -f config/config.json.example config/config.json
        log "[OK] config.json 已创建"
    else
        log "[WARNING] config.json.example 不存在"
    fi

    if [ -f "config/cookies.json.example" ]; then
        cp -f config/cookies.json.example config/cookies.json
        log "[OK] cookies.json 已创建"
    fi

    log_blank
    log "========================================"
    log "首次配置完成！"
    log "========================================"
    log_blank
    log "请编辑 config/config.json，填写以下信息："
    log "  - login.username: 用户名"
    log "  - login.password: 密码"
    log "  - target_url: 目标URL"
    log "  - headers.cookie: Cookie值"
    log "  - cookies中的token和sensorsdata值"
    log_blank
    read -p "按回车键继续，或 Ctrl+C 退出: "
    run_web
}

run_web() {
    log_blank
    log "========================================"
    log "启动Web服务和隧道..."
    log "========================================"

    source "$VENV_PATH/bin/activate"

    log_blank
    log "正在启动 Web 服务..."
    log_blank

    WEB_PORT="${WEB_PORT:-8888}"
    log "[$(date '+%Y-%m-%d %H:%M:%S')] === Web服务启动 ==="
    "$VENV_PATH/bin/python" main.py --web --port "$WEB_PORT" < /dev/null &
    PYTHON_PID=$!

    log "等待 Web 服务启动完成..."
    sleep 1

    FLASK_WAIT_COUNT=0
    FLASK_MAX_WAIT=30
    while [ $FLASK_WAIT_COUNT -lt $FLASK_MAX_WAIT ]; do
        if ! kill -0 $PYTHON_PID 2>/dev/null; then
            log "[ERROR] Web 服务进程已退出，请检查 file/web_output.log"
            exit 1
        fi
        HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:$WEB_PORT" 2>/dev/null)
        if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "302" ]; then
            break
        fi
        FLASK_WAIT_COUNT=$((FLASK_WAIT_COUNT + 1))
        sleep 1
    done

    if [ $FLASK_WAIT_COUNT -ge $FLASK_MAX_WAIT ]; then
        log "[WARNING] Web服务启动超时（等待了$((FLASK_MAX_WAIT * 2))秒），请检查日志: file/web_output.log"
    fi

    LOG_FILE=""
    log_console_only "Web 服务已就绪，正在启动隧道..."
# hostc已在脚本启动时启动
    TUNNEL_PID=$!

    sleep 2

    if ! kill -0 $TUNNEL_PID 2>/dev/null; then
        log_console_only "[WARNING] 隧道服务启动失败，本地访问仍可用"
    fi

    log_blank_console_only
    log_console_only "========================================"
    log_console_only "启动完成！"
    log_console_only "========================================"
    log_blank_console_only
    log_console_only "本地访问: http://localhost:$WEB_PORT"
    log_console_only "公网访问: 查看 file/tunnel_url.txt"
    log_console_only "Web日志: 查看 file/web_output.log"
    log_blank_console_only
    log_console_only "关闭此窗口可停止服务，或使用 Ctrl+C"
    log_blank_console_only

    (
        while true; do
            sleep 60
            if [ -d "temp" ]; then
                TOTAL_SIZE_KB=$(du -sk temp 2>/dev/null | awk '{print $1}')
                LIMIT_SIZE_KB=3072
                if [ -n "$TOTAL_SIZE_KB" ] && [ "$TOTAL_SIZE_KB" -gt "$LIMIT_SIZE_KB" ]; then
                    rm -rf temp/*
                    log_console_only "[AUTO] temp目录超过3MB，已清理所有文件"
                fi
            fi
        done
    ) &
    CLEANUP_PID=$!

    wait $PYTHON_PID $TUNNEL_PID 2>/dev/null
    kill $CLEANUP_PID 2>/dev/null
}

cleanup_exit() {
    log_blank
    log "正在清理进程..."
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
    log "清理完成"
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