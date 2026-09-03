#!/bin/bash
cd "$(dirname "$0")"

VERSION="0.0.0"
if [ -f "README.md" ]; then
    VERSION=$(grep -m 1 -oE '###\s+v[0-9]+(\.[0-9]+)+' README.md 2>/dev/null | grep -oE '[0-9]+(\.[0-9]+)+' | head -1 || echo "0.0.0")
    if [ "$VERSION" = "0.0.0" ]; then
        VERSION=$(grep -m 1 -oE "version:[\"]?[0-9]+(\.[0-9]+)+" README.md 2>/dev/null | grep -oE '[0-9]+(\.[0-9]+)+' | head -1 || echo "0.0.0")
    fi
fi

mkdir -p file
LOG_FILE="$(pwd)/file/web_output.log"
> "$LOG_FILE"

log() {
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S.%3N' 2>/dev/null || date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] $*"
    [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ] && echo "[$timestamp] $*" >> "$LOG_FILE" 2>/dev/null
}

log_blank() {
    echo ""
    [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ] && echo "" >> "$LOG_FILE" 2>/dev/null
}

log_console_only() {
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S.%3N' 2>/dev/null || date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] $*"
}

check_prerequisites() {
    log "[*] 检查前置条件..."

    if ! command -v curl &> /dev/null; then
        log "[*] 未检测到curl，正在自动安装..."
        case "$(uname -s)" in
            Darwin)
                if command -v brew &> /dev/null || [ -f "/opt/homebrew/bin/brew" ] || [ -f "/usr/local/bin/brew" ]; then
                    log "    使用Homebrew安装curl..."
                    if [ -f "/opt/homebrew/bin/brew" ]; then
                        /opt/homebrew/bin/brew install curl
                    elif [ -f "/usr/local/bin/brew" ]; then
                        /usr/local/bin/brew install curl
                    else
                        brew install curl
                    fi
                else
                    log "    未检测到Homebrew，先安装Homebrew（使用国内镜像）..."
                    auto_install_homebrew
                    if command -v brew &> /dev/null || [ -f "/opt/homebrew/bin/brew" ] || [ -f "/usr/local/bin/brew" ]; then
                        log "    使用Homebrew安装curl..."
                        if [ -f "/opt/homebrew/bin/brew" ]; then
                            /opt/homebrew/bin/brew install curl
                        elif [ -f "/usr/local/bin/brew" ]; then
                            /usr/local/bin/brew install curl
                        else
                            brew install curl
                        fi
                    else
                        log "[ERROR] Homebrew安装失败，无法安装curl"
                        return 1
                    fi
                fi
                ;;
            Linux)
                if command -v apt-get &> /dev/null; then
                    sudo apt-get update && sudo apt-get install -y curl
                elif command -v yum &> /dev/null; then
                    sudo yum install -y curl
                elif command -v dnf &> /dev/null; then
                    sudo dnf install -y curl
                elif command -v pacman &> /dev/null; then
                    sudo pacman -Syu --noconfirm curl
                else
                    log "[ERROR] 无法识别包管理器，请手动安装: apt/yum/dnf/pacman install curl"
                    return 1
                fi
                ;;
            *)
                log "[ERROR] 不支持的操作系统，无法自动安装curl"
                return 1
                ;;
        esac

        if ! command -v curl &> /dev/null; then
            log "[ERROR] curl 安装失败"
            return 1
        fi
        log "[✅] curl 安装成功"
    fi

    if ! command -v git &> /dev/null; then
        log "[*] 未检测到git，正在自动安装..."
        case "$(uname -s)" in
            Darwin)
                if command -v brew &> /dev/null; then
                    brew install git
                elif [ -f "/opt/homebrew/bin/brew" ]; then
                    /opt/homebrew/bin/brew install git
                elif [ -f "/usr/local/bin/brew" ]; then
                    /usr/local/bin/brew install git
                else
                    log "    未检测到Homebrew，先安装Homebrew（使用国内镜像）..."
                    auto_install_homebrew
                    if command -v brew &> /dev/null || [ -f "/opt/homebrew/bin/brew" ] || [ -f "/usr/local/bin/brew" ]; then
                        log "    使用Homebrew安装git..."
                        if [ -f "/opt/homebrew/bin/brew" ]; then
                            /opt/homebrew/bin/brew install git
                        elif [ -f "/usr/local/bin/brew" ]; then
                            /usr/local/bin/brew install git
                        else
                            brew install git
                        fi
                    else
                        log "[ERROR] Homebrew安装失败，无法安装git"
                        return 1
                    fi
                fi
                ;;
            Linux)
                if command -v apt-get &> /dev/null; then
                    sudo apt-get update && sudo apt-get install -y git
                elif command -v yum &> /dev/null; then
                    sudo yum install -y git
                elif command -v dnf &> /dev/null; then
                    sudo dnf install -y git
                elif command -v pacman &> /dev/null; then
                    sudo pacman -Syu --noconfirm git
                else
                    log "[ERROR] 无法自动安装git，请手动安装"
                    return 1
                fi
                ;;
            *)
                log "[ERROR] 不支持的操作系统，无法自动安装git"
                return 1
                ;;
        esac

        if ! command -v git &> /dev/null; then
            log "[ERROR] git 安装失败，请手动安装"
            return 1
        fi
        log "[✅] git 安装成功"
    fi
    
    log "[*] 前置条件检查通过"
    return 0
}

pre_launch() {
    log "========================================"
    log "Szwego商品爬虫和货号对比工具 - v${VERSION}"
    log "========================================"

    WEB_PORT="${WEB_PORT:-8888}"

    log_blank
    log "[*] 清理残留进程..."
    pkill -9 -f "python.*main.py" 2>/dev/null || true
    pkill -9 -f "hostc" 2>/dev/null || true
    sleep 1

    wait_for_port $WEB_PORT 10
    log "[*] 残留进程清理完成"

    log_blank
    log "[*] 检查 hostc 隧道工具..."
    HOSTC_BIN="$(pwd)/dist/node_modules/.bin/hostc"
    if [ ! -f "$HOSTC_BIN" ]; then
        log "[*] 本地未找到 hostc，开始安装..."
        install_hostc
    fi
    if [ -f "$HOSTC_BIN" ]; then
        HOSTC_VER=$("$HOSTC_BIN" --version 2>/dev/null || echo "unknown")
        log "[*] hostc v${HOSTC_VER} 已就绪"
    else
        log "[WARNING] hostc 安装失败，隧道将不可用"
    fi

    log_blank
    log "[*] 启动 hostc 隧道（后台运行）..."
    if [ -f "$HOSTC_BIN" ]; then
        "$HOSTC_BIN" $WEB_PORT --local-host localhost < /dev/null &
        log "[*] hostc 已在后台启动"
    fi

    log_blank
    log "[*] 清理临时文件..."
    cleanup_temp_dir temp 3072
    cleanup_temp_dir playwright-browsers 0
}

wait_for_port() {
    local port=$1
    local max_wait=$2
    local count=0
    
    while [ $count -lt $max_wait ]; do
        if ! lsof -i :$port -sTCP:LISTEN &>/dev/null; then
            break
        fi
        count=$((count + 1))
        log "[*] 端口$port仍被占用，等待释放... ($count/$max_wait)"
        sleep 1
    done
    
    if [ $count -ge $max_wait ]; then
        log "[WARNING] 端口$port等待超时，强制清理..."
        lsof -t -i :$port -sTCP:LISTEN 2>/dev/null | xargs kill -9 2>/dev/null || true
        sleep 1
    fi
}

cleanup_temp_dir() {
    local dir_name=$1
    local max_size_kb=$2
    
    if [ -d "$dir_name" ]; then
        local size_kb
        size_kb=$(du -sk "$dir_name" 2>/dev/null | awk '{print $1}')
        
        if [ -n "$size_kb" ] && [ "$size_kb" -gt "$max_size_kb" ]; then
            rm -rf "${dir_name:?}"/*
            log "[*] $dir_name目录超过限制，已清理"
        else
            log "[*] $dir_name目录未超过限制，跳过清理"
        fi
    else
        log "[*] $dir_name目录不存在，跳过"
    fi
}

detect_python_env() {
    log_blank
    log "========================================"
    log "综合环境检测与配置"
    log "========================================"

    log "[1/6] 检测Python环境..."

    PYTHON_CMD=""
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        log "Python未在PATH中，正在尝试查找或自动安装..."
        
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
            log "[*] 正在自动安装Python..."
            auto_install_python
            if [ $? -ne 0 ]; then
                return 1
            fi
        fi
    fi
    
    if [ -z "$PYTHON_CMD" ]; then
        log "[ERROR] 无法找到或安装Python"
        return 1
    fi

    log_blank
    log "Python版本："
    if [ -x "$PYTHON_CMD" ]; then
        local py_version
        py_version=$("$PYTHON_CMD" --version 2>&1)
        if [ -n "$py_version" ]; then
            log "    $py_version"
        else
            log "[WARNING] Python执行成功但无法获取版本信息: $PYTHON_CMD"
        fi
    elif command -v "$PYTHON_CMD" &> /dev/null; then
        local py_version
        py_version=$("$PYTHON_CMD" --version 2>&1)
        if [ -n "$py_version" ]; then
            log "    $py_version"
        else
            log "[WARNING] Python在PATH中但无法获取版本信息: $PYTHON_CMD"
        fi
    else
        log "[WARNING] Python路径不存在或不可执行: $PYTHON_CMD"
    fi

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

test_brew_mirror() {
    log "[*] 测试Homebrew国内镜像源速度..."
    
    local mirrors=(
        "阿里云|https://mirrors.aliyun.com/homebrew/brew.git"
        "中科大|https://mirrors.ustc.edu.cn/homebrew/brew.git"
        "清华|https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
        "腾讯|https://mirrors.cloud.tencent.com/homebrew/brew.git"
    )
    
    local fastest_mirror=""
    local fastest_time=99999
    
    for mirror_info in "${mirrors[@]}"; do
        local mirror_name="${mirror_info%%|*}"
        local mirror_url="${mirror_info##*|}"
        
        log "    测试 ${mirror_name}..."
        local start_time=$(date +%s%N 2>/dev/null || date +%s)
        local http_code=$(curl -o /dev/null -s -w "%{http_code}" --connect-timeout 3 --max-time 5 "$mirror_url" 2>/dev/null)
        local end_time=$(date +%s%N 2>/dev/null || date +%s)
        
        if [ "$http_code" = "200" ] || [ "$http_code" = "301" ] || [ "$http_code" = "302" ]; then
            local elapsed=$(( (end_time - start_time) / 1000000 ))
            if [ $elapsed -lt 1 ]; then
                elapsed=1
            fi
            log "        ${mirror_name}: ${elapsed}ms ✅"
            
            if [ $elapsed -lt $fastest_time ]; then
                fastest_time=$elapsed
                fastest_mirror="$mirror_name"
            fi
        else
            log "        ${mirror_name}: 超时或不可用 ❌"
        fi
    done
    
    if [ -n "$fastest_mirror" ]; then
        log "[*] 最快Homebrew镜像: ${fastest_mirror} [${fastest_time}ms]"
        echo "$fastest_mirror"
        return 0
    else
        log "[WARNING] 所有Homebrew镜像测试失败，使用官方源"
        echo "official"
        return 1
    fi
}

auto_install_homebrew() {
    log "[*] 正在全自动安装Homebrew..."

    local fastest_mirror
    fastest_mirror=$(test_brew_mirror)

    local brew_remote=""
    local core_remote=""
    local cask_remote=""
    local bottle_domain=""

    case "$fastest_mirror" in
        "阿里云")
            brew_remote="https://mirrors.aliyun.com/homebrew/brew.git"
            core_remote="https://mirrors.aliyun.com/homebrew-core.git"
            cask_remote="https://mirrors.aliyun.com/homebrew-cask.git"
            bottle_domain="https://mirrors.aliyun.com/homebrew-bottles"
            ;;
        "中科大")
            brew_remote="https://mirrors.ustc.edu.cn/homebrew/brew.git"
            core_remote="https://mirrors.ustc.edu.cn/homebrew-core.git"
            cask_remote="https://mirrors.ustc.edu.cn/homebrew-cask.git"
            bottle_domain="https://mirrors.ustc.edu.cn/homebrew-bottles"
            ;;
        "清华")
            brew_remote="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
            core_remote="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
            cask_remote="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git"
            bottle_domain="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
            ;;
        "腾讯")
            brew_remote="https://mirrors.cloud.tencent.com/homebrew/brew.git"
            core_remote="https://mirrors.cloud.tencent.com/homebrew/homebrew-core.git"
            cask_remote="https://mirrors.cloud.tencent.com/homebrew/homebrew-cask.git"
            bottle_domain="https://mirrors.cloud.tencent.com/homebrew-bottles"
            ;;
        *)
            brew_remote="https://github.com/Homebrew/brew.git"
            core_remote="https://github.com/homebrew/homebrew-core.git"
            cask_remote="https://github.com/homebrew/homebrew-cask.git"
            bottle_domain=""
            ;;
    esac

    log "[*] 安装前设置Homebrew镜像环境变量（安装脚本会使用这些变量）..."
    export HOMEBREW_BREW_GIT_REMOTE="$brew_remote"
    export HOMEBREW_CORE_GIT_REMOTE="$core_remote"
    if [ -n "$cask_remote" ]; then
        export HOMEBREW_CASK_GIT_REMOTE="$cask_remote"
    fi
    if [ -n "$bottle_domain" ]; then
        export HOMEBREW_BOTTLE_DOMAIN="$bottle_domain"
    fi

    log "[*] 下载Homebrew安装脚本（轮询国内镜像）..."
    local install_script=""
    local install_mirrors=(
        "https://ghproxy.com/https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh|ghproxy"
        "https://mirror.ghproxy.com/https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh|mirror.ghproxy"
        "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh|GitHub官方"
    )

    for m in "${install_mirrors[@]}"; do
        local m_name="${m##*|}"
        local m_url="${m%|*}"
        log "    尝试 ${m_name}..."
        install_script=$(curl -fsSL --connect-timeout 5 --max-time 15 "$m_url" 2>/dev/null)
        if [ -n "$install_script" ]; then
            log "    ${m_name} 下载成功 ✅"
            break
        else
            log "    ${m_name} 下载失败 ❌"
        fi
    done

    if [ -z "$install_script" ]; then
        log "[ERROR] 无法下载Homebrew安装脚本，请检查网络"
        return 1
    fi

    log "[*] 执行Homebrew安装（镜像环境变量已设置）..."
    NONINTERACTIVE=1 /bin/bash -c "$install_script"

    if [ $? -ne 0 ]; then
        log "[ERROR] Homebrew 安装失败"
        return 1
    fi

    if [ -f "/opt/homebrew/bin/brew" ]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [ -f "/usr/local/bin/brew" ]; then
        eval "$(/usr/local/bin/brew shellenv)"
    fi

    if command -v brew &> /dev/null; then
        if [ -n "$core_remote" ] && [ "$core_remote" != "https://github.com/homebrew/homebrew-core.git" ]; then
            brew tap --custom-remote --force homebrew/core "$core_remote" 2>/dev/null || true
        fi
        if [ -n "$cask_remote" ] && [ "$cask_remote" != "https://github.com/homebrew/homebrew-cask.git" ]; then
            brew tap --custom-remote --force homebrew/cask "$cask_remote" 2>/dev/null || true
        fi
    fi

    persist_brew_mirror "$fastest_mirror" "$brew_remote" "$core_remote" "$cask_remote" "$bottle_domain"

    log "[✅] Homebrew 安装成功（${fastest_mirror}加速源）"
    return 0
}

persist_brew_mirror() {
    local mirror_name="$1"
    local brew_remote="$2"
    local core_remote="$3"
    local cask_remote="$4"
    local bottle_domain="$5"

    log "[*] 持久化Homebrew镜像配置到系统环境..."

    local profile_files=("$HOME/.zshrc" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile")

    for profile in "${profile_files[@]}"; do
        if [ -f "$profile" ]; then
            sed -i.bak '/^export HOMEBREW_BREW_GIT_REMOTE=/d; /^export HOMEBREW_CORE_GIT_REMOTE=/d; /^export HOMEBREW_CASK_GIT_REMOTE=/d; /^export HOMEBREW_BOTTLE_DOMAIN=/d' "$profile" 2>/dev/null || true
            rm -f "${profile}.bak" 2>/dev/null || true
        fi

        {
            echo ""
            echo "# Homebrew镜像源配置 (由run.sh自动设置)"
            echo "export HOMEBREW_BREW_GIT_REMOTE="${brew_remote}""
            echo "export HOMEBREW_CORE_GIT_REMOTE="${core_remote}""
            if [ -n "$cask_remote" ]; then
                echo "export HOMEBREW_CASK_GIT_REMOTE="${cask_remote}""
            fi
            if [ -n "$bottle_domain" ]; then
                echo "export HOMEBREW_BOTTLE_DOMAIN="${bottle_domain}""
            fi
        } >> "$profile"

        log "    已冕入: $profile"
    done

    if [ "$(uname -s)" = "Linux" ]; then
        if [ -w "/etc/environment" ] || command -v sudo &> /dev/null; then
            sudo sed -i '/^HOMEBREW_BREW_GIT_REMOTE=/d; /^HOMEBREW_CORE_GIT_REMOTE=/d; /^HOMEBREW_CASK_GIT_REMOTE=/d; /^HOMEBREW_BOTTLE_DOMAIN=/d' /etc/environment 2>/dev/null || true
            {
                echo "HOMEBREW_BREW_GIT_REMOTE="${brew_remote}""
                echo "HOMEBREW_CORE_GIT_REMOTE="${core_remote}""
                if [ -n "$cask_remote" ]; then
                    echo "HOMEBREW_CASK_GIT_REMOTE="${cask_remote}""
                fi
                if [ -n "$bottle_domain" ]; then
                    echo "HOMEBREW_BOTTLE_DOMAIN="${bottle_domain}""
                fi
            } | sudo tee -a /etc/environment > /dev/null 2>&1 || true
            log "    已冕入: /etc/environment (Linux系统级)"
        fi
    fi

    log "[✅] Homebrew镜像配置已持久化"]
}


auto_install_python() {
    case "$(uname -s)" in
        Darwin)
            if command -v brew &> /dev/null; then
                log "    使用Homebrew安装Python..."
                brew install python
            elif [ -f "/opt/homebrew/bin/brew" ]; then
                log "    使用Homebrew (Apple Silicon) 安装Python..."
                /opt/homebrew/bin/brew install python
            else
                log "[*] 未检测到Homebrew，正在全自动安装（使用国内加速源）..."
                auto_install_homebrew
                if [ $? -ne 0 ]; then
                    return 1
                fi

                log "    使用Homebrew安装Python..."
                if [ -f "/opt/homebrew/bin/brew" ]; then
                    /opt/homebrew/bin/brew install python
                elif command -v brew &> /dev/null; then
                    brew install python
                else
                    log "[ERROR] Homebrew 安装后仍不可用"
                    return 1
                fi
            fi
            ;;
        Linux)
            if command -v apt-get &> /dev/null; then
                log "    使用apt安装Python..."
                sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip nodejs npm curl
            elif command -v yum &> /dev/null; then
                log "    使用yum安装Python..."
                sudo yum install -y python3 python3-pip nodejs npm curl
            elif command -v dnf &> /dev/null; then
                log "    使用dnf安装Python..."
                sudo dnf install -y python3 python3-pip nodejs npm curl
            elif command -v pacman &> /dev/null; then
                log "    使用pacman安装Python..."
                sudo pacman -Syu --noconfirm python python-pip nodejs npm curl
            elif command -v apk &> /dev/null; then
                log "    使用apk安装Python..."
                sudo apk add python3 py3-pip nodejs npm curl
            elif command -v zypper &> /dev/null; then
                log "    使用zypper安装Python..."
                sudo zypper install -y python3 python3-pip nodejs npm curl
get_latest_python_version() {
    PYTHON_LATEST_VERSION=$(curl -s https://api.github.com/repos/python/cpython/releases/latest 2>/dev/null | grep -oE '"tag_name":\s*"v[0-9]+\.[0-9]+\.[0-9]+"' | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
    if [ -z "$PYTHON_LATEST_VERSION" ]; then
        PYTHON_LATEST_VERSION="3.11.9"
    fi
}

            else
                log "[WARNING] 无法识别Linux包管理器，尝试下载独立Python..."
                if [ "$(uname -m)" = "x86_64" ]; then
                    get_latest_python_version
                    log "    下载Python ${PYTHON_LATEST_VERSION} standalone版本..."
                    log "    轮询最快Python镜像源..."
                    PY_MIRRORS=(
                        "https://mirrors.huaweicloud.com/python/${PYTHON_LATEST_VERSION}/python-${PYTHON_LATEST_VERSION}-amd64.tar.xz|华为云"
                        "https://registry.npmmirror.com/-/binary/python/${PYTHON_LATEST_VERSION}/python-${PYTHON_LATEST_VERSION}-amd64.tar.xz|npmmirror"
                        "https://www.python.org/ftp/python/${PYTHON_LATEST_VERSION}/python-${PYTHON_LATEST_VERSION}-amd64.tar.xz|Python官方"
                    )
                    PY_BEST_URL="https://www.python.org/ftp/python/${PYTHON_LATEST_VERSION}/python-${PYTHON_LATEST_VERSION}-amd64.tar.xz"
                    PY_MIN_TIME=99999
                    for m in "${PY_MIRRORS[@]}"; do
                        m_name="${m##*|}"
                        m_url="${m%|*}"
                        m_time=$(curl -s -o /dev/null -w "%{time_connect}" --connect-timeout 2 --max-time 3 "$m_url" 2>/dev/null)
                        if [ -n "$m_time" ] && [ "$m_time" != "0" ]; then
                            m_ms=$(echo "$m_time" | awk '{printf "%d", $1*1000}')
                            log "        $m_name: ${m_ms}ms"
                            if [ "$m_ms" -lt "$PY_MIN_TIME" ]; then
                                PY_MIN_TIME=$m_ms
                                PY_BEST_URL="$m_url"
                            fi
                        fi
                    done
                    log "    使用最快镜像下载Python..."
                    curl -fsSL "$PY_BEST_URL" -o /tmp/python.tar.xz || {
                        log "[ERROR] Python下载失败，请手动安装: https://www.python.org/downloads/"
                        return 1
                    }
                    cd /tmp && tar xf python.tar.xz
                    export PATH="/tmp/python-${PYTHON_LATEST_VERSION}/bin:$PATH"
                    export PYTHON_CMD="/tmp/python-${PYTHON_LATEST_VERSION}/bin/python3"
                    cd -
                else
                    log "[ERROR] 不支持的架构或操作系统，请手动安装Python"
                    return 1
                fi
            fi
            ;;
        *)
            log "[ERROR] 不支持的操作系统"
            return 1
            ;;
    esac
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        log "[*] Python 安装成功: $($PYTHON_CMD --version 2>&1)"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        log "[*] Python 安装成功: $($PYTHON_CMD --version 2>&1)"
    else
        log "[ERROR] Python 安装失败"
        return 1
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
        log "    使用NVM管理Node.js..."
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
            log "Node.js版本: $(node --version 2>&1)"
            log "NPM版本: $(npm --version 2>&1)"
            return 0
        fi
    fi
    
    auto_install_node
    return 0
}

auto_install_node() {
    case "$(uname -s)" in
        Darwin)
            if command -v brew &> /dev/null; then
                log "    使用Homebrew安装Node.js..."
                brew install node
            elif [ -f "/opt/homebrew/bin/brew" ]; then
                log "    使用Homebrew (Apple Silicon) 安装Node.js..."
                /opt/homebrew/bin/brew install node
            else
                log "[WARNING] 未检测到Homebrew，Node.js安装失败"
                return 0
            fi
            ;;
        Linux)
            if command -v apt-get &> /dev/null; then
                log "    使用apt+nodesource安装Node.js..."
                log "    轮询最快NodeSource镜像..."
                NS_MIRRORS=(
                    "https://mirrors.tuna.tsinghua.edu.cn/nodesource/deb/setup_lts.x|清华"
                    "https://deb.nodesource.com/setup_lts.x|NodeSource官方"
                )
                NS_BEST_URL="https://deb.nodesource.com/setup_lts.x"
                NS_MIN_TIME=99999
                for m in "${NS_MIRRORS[@]}"; do
                    m_name="${m##*|}"
                    m_url="${m%|*}"
                    m_time=$(curl -s -o /dev/null -w "%{time_connect}" --connect-timeout 2 --max-time 3 "$m_url" 2>/dev/null)
                    if [ -n "$m_time" ] && [ "$m_time" != "0" ]; then
                        m_ms=$(echo "$m_time" | awk '{printf "%d", $1*1000}')
                        if [ "$m_ms" -lt "$NS_MIN_TIME" ]; then
                            NS_MIN_TIME=$m_ms
                            NS_BEST_URL="$m_url"
                        fi
                    fi
                done
                curl -fsSL "$NS_BEST_URL" | sudo -E bash -
                sudo apt-get install -y nodejs
            elif command -v yum &> /dev/null; then
                log "    使用yum+nodesource安装Node.js..."
                log "    轮询最快NodeSource RPM镜像..."
                NSR_MIRRORS=(
                    "https://mirrors.tuna.tsinghua.edu.cn/nodesource/rpm/setup_lts.x|清华"
                    "https://rpm.nodesource.com/setup_lts.x|NodeSource官方"
                )
                NSR_BEST_URL="https://rpm.nodesource.com/setup_lts.x"
                NSR_MIN_TIME=99999
                for m in "${NSR_MIRRORS[@]}"; do
                    m_name="${m##*|}"
                    m_url="${m%|*}"
                    m_time=$(curl -s -o /dev/null -w "%{time_connect}" --connect-timeout 2 --max-time 3 "$m_url" 2>/dev/null)
                    if [ -n "$m_time" ] && [ "$m_time" != "0" ]; then
                        m_ms=$(echo "$m_time" | awk '{printf "%d", $1*1000}')
                        if [ "$m_ms" -lt "$NSR_MIN_TIME" ]; then
                            NSR_MIN_TIME=$m_ms
                            NSR_BEST_URL="$m_url"
                        fi
                    fi
                done
                curl -fsSL "$NSR_BEST_URL" | sudo bash -
                sudo yum install -y nodejs
            elif command -v dnf &> /dev/null; then
                log "    使用dnf+nodesource安装Node.js..."
                log "    轮询最快NodeSource RPM镜像..."
                NSR_MIRRORS=(
                    "https://mirrors.tuna.tsinghua.edu.cn/nodesource/rpm/setup_lts.x|清华"
                    "https://rpm.nodesource.com/setup_lts.x|NodeSource官方"
                )
                NSR_BEST_URL="https://rpm.nodesource.com/setup_lts.x"
                NSR_MIN_TIME=99999
                for m in "${NSR_MIRRORS[@]}"; do
                    m_name="${m##*|}"
                    m_url="${m%|*}"
                    m_time=$(curl -s -o /dev/null -w "%{time_connect}" --connect-timeout 2 --max-time 3 "$m_url" 2>/dev/null)
                    if [ -n "$m_time" ] && [ "$m_time" != "0" ]; then
                        m_ms=$(echo "$m_time" | awk '{printf "%d", $1*1000}')
                        if [ "$m_ms" -lt "$NSR_MIN_TIME" ]; then
                            NSR_MIN_TIME=$m_ms
                            NSR_BEST_URL="$m_url"
                        fi
                    fi
                done
                curl -fsSL "$NSR_BEST_URL" | sudo bash -
                sudo dnf install -y nodejs
            elif command -v pacman &> /dev/null; then
                log "    使用pacman安装Node.js..."
                sudo pacman -Syu --noconfirm nodejs npm
            else
                log "[WARNING] 无法识别包管理器，Node.js安装失败"
                return 0
            fi
            ;;
        *)
            log "[WARNING] 不支持的操作系统，Node.js安装失败"
            return 0
            ;;
    esac
}

test_pip_mirrors() {
    log "[3/6] 测试PIP加速镜像源..."

    if [ -z "$PYTHON_CMD" ]; then
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

        if [ -n "$TEST_TIME" ] && [ "$TEST_TIME" != "0.000" ] && [ "$TEST_TIME" != "0" ]; then
            PIP_INT_TIME=$(echo "$TEST_TIME" | awk '{printf "%d", $1 * 1000}')
            
            if [ -n "$PIP_INT_TIME" ] && [ "$PIP_INT_TIME" -lt "$MIN_TIME" ] 2>/dev/null; then
                MIN_TIME=$PIP_INT_TIME
                BEST_MIRROR="$MIRROR_URL"
                BEST_NAME="$MIRROR_NAME"
                log "        $MIRROR_NAME: ${TEST_TIME}秒 [${PIP_INT_TIME}ms]"
            fi
        else
            log "        $MIRROR_NAME: 超时/失败"
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

    HOSTC_BEST_MIRROR="https://registry.npmmirror.com"

    for hostc_mirror_entry in "${HOSTC_MIRRORS[@]}"; do
        IFS='|' read -r H_URL H_NAME <<< "$hostc_mirror_entry"
        
        H_TIME=$(curl -s -o /dev/null -w "%{time_total}" --connect-timeout 3 "$H_URL" 2>/dev/null)

        if [ -n "$H_TIME" ] && [ "$H_TIME" != "0.000" ] && [ "$H_TIME" != "0" ]; then
            H_INT_TIME=$(echo "$H_TIME" | awk '{printf "%d", $1 * 1000}')
            
            if [ -n "$H_INT_TIME" ] && [ "$H_INT_TIME" -lt 9999 ] 2>/dev/null; then
                HOSTC_BEST_MIRROR="$H_URL"
                log "    测试 $H_NAME: ${H_TIME}秒 [${H_INT_TIME}ms]"
            fi
        fi
    done

    log "[*] 使用最佳镜像安装 hostc..."
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

        if [ -n "$NPM_TEST_TIME" ] && [ "$NPM_TEST_TIME" != "0.000" ] && [ "$NPM_TEST_TIME" != "0" ]; then
            NPM_INT_TIME=$(echo "$NPM_TEST_TIME" | awk '{printf "%d", $1 * 1000}')
            
            if [ -n "$NPM_INT_TIME" ] && [ "$NPM_INT_TIME" -lt "$NPM_MIN_TIME" ] 2>/dev/null; then
                NPM_MIN_TIME=$NPM_INT_TIME
                NPM_BEST_MIRROR="$NPM_URL"
                NPM_BEST_NAME="$NPM_NAME"
                log "        $NPM_NAME: ${NPM_TEST_TIME}秒 [${NPM_INT_TIME}ms]"
            fi
        else
            log "        $NPM_NAME: 超时/失败"
        fi
    done

    if [ -n "$NPM_BEST_MIRROR" ]; then
        FASTEST_NPM_MIRROR="$NPM_BEST_MIRROR"
        log_blank
        log "[*] 最快NPM镜像: $NPM_BEST_NAME [${NPM_MIN_TIME}毫秒]"
        
        npm config set registry "$NPM_BEST_MIRROR"
        log "[*] NPM镜像已设置为: $NPM_BEST_MIRROR"

        log "[*] 持久化NPM镜像到系统环境..."

        for profile in "$HOME/.zshrc" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile"; do
            if [ -f "$profile" ]; then
                sed -i.bak '/^export NPM_CONFIG_REGISTRY=/d' "$profile" 2>/dev/null || true
                rm -f "${profile}.bak" 2>/dev/null || true
                echo "" >> "$profile"
                echo "# NPM镜像配置 (由run.sh自动设置)" >> "$profile"
                echo "export NPM_CONFIG_REGISTRY="${NPM_BEST_MIRROR}"" >> "$profile"
                log "    已写入NPM_REGISTRY到: $profile"
                break
            fi
        done

        if [ "$(uname -s)" = "Linux" ]; then
            if [ -w "/etc/environment" ] || command -v sudo &> /dev/null; then
                sudo sed -i '/^NPM_CONFIG_REGISTRY=/d' /etc/environment 2>/dev/null || true
                echo "NPM_CONFIG_REGISTRY="${NPM_BEST_MIRROR}"" | sudo tee -a /etc/environment > /dev/null 2>&1 || true
                log "    已写入: /etc/environment (Linux系统级)"
            fi
        fi
    else
        log "[WARNING] NPM镜像测试失败"
    fi
}

detect_venv() {
    log "[5/6] 检测Python虚拟环境..."

    if [ -d ".venv" ] && [ -f ".venv/bin/activate" ]; then
        log "检测到虚拟环境：.venv"
        VENV_EXISTS=1
        VENV_PATH=".venv"
    else
        log "未检测到虚拟环境"
        VENV_EXISTS=0
        VENV_PATH=".venv"
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

        log "[*] 持久化PIP镜像到系统环境..."
        mkdir -p "$HOME/.pip" 2>/dev/null || true
        cat > "$HOME/.pip/pip.conf" << EOF2
[global]
index-url = $FASTEST_PIP_MIRROR
trusted-host = $TRUSTED_HOST
[install]
trusted-host = $TRUSTED_HOST
EOF2
        log "    已写入: $HOME/.pip/pip.conf (用户级全局)"

        for profile in "$HOME/.zshrc" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile"; do
            if [ -f "$profile" ]; then
                sed -i.bak '/^export PIP_INDEX_URL=/d' "$profile" 2>/dev/null || true
                rm -f "${profile}.bak" 2>/dev/null || true
                echo "" >> "$profile"
                echo "# PIP镜像配置 (由run.sh自动设置)" >> "$profile"
                echo "export PIP_INDEX_URL="${FASTEST_PIP_MIRROR}"" >> "$profile"
                log "    已写入PIP_INDEX_URL到: $profile"
                break
            fi
        done

        if [ "$(uname -s)" = "Linux" ]; then
            if [ -w "/etc/environment" ] || command -v sudo &> /dev/null; then
                sudo sed -i '/^PIP_INDEX_URL=/d' /etc/environment 2>/dev/null || true
                echo "PIP_INDEX_URL="${FASTEST_PIP_MIRROR}"" | sudo tee -a /etc/environment > /dev/null 2>&1 || true
                log "    已写入: /etc/environment (Linux系统级)"
            fi
        fi    fi

    if [ -f "requirements.txt" ]; then
        log "[*] 检查Python依赖是否需要安装..."
        NEED_PIP_INSTALL=1
        "$VENV_PATH/bin/python" main.py --check-deps > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            log "[*] 所有Python依赖已满足，跳过安装"
            NEED_PIP_INSTALL=0
        fi

        if [ "$NEED_PIP_INSTALL" -eq 1 ]; then
            log "[*] 强制升级pip到最新版本..."
            if [ -n "$FASTEST_PIP_MIRROR" ]; then
                pip install --upgrade pip -i "$FASTEST_PIP_MIRROR"
            else
                pip install --upgrade pip
            fi
            
            log "[*] 安装依赖..."
            if [ -n "$FASTEST_PIP_MIRROR" ]; then
                pip install -r requirements.txt -i "$FASTEST_PIP_MIRROR"
                if [ $? -ne 0 ]; then
                    log "WARNING: 使用镜像源安装失败，尝试默认源..."
                    pip install -r requirements.txt
                fi
            else
                pip install -r requirements.txt
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
    log "请编辑 config/config.json 后按回车继续"
    read -p ""
    run_web
}

run_web() {
    log_blank
    log "========================================"
    log "启动Web服务和隧道..."
    log "========================================"

    source "$VENV_PATH/bin/activate"

    log_blank
    log "[*] Checking BOM..."
    "$VENV_PATH/bin/python" main.py --check-bom > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        log "[WARNING] BOM detected, auto-fixing..."
        "$VENV_PATH/bin/python" main.py --fix-bom
    fi
    log "[OK] BOM check completed"
    log "Starting Web service..."
    log_blank

    WEB_PORT="${WEB_PORT:-8888}"
    if ! [[ "$WEB_PORT" =~ ^[0-9]+$ ]] || [ "$WEB_PORT" -lt 1 ] || [ "$WEB_PORT" -gt 65535 ]; then
        log "[WARNING] 端口 $WEB_PORT 无效，使用默认端口 8888"
        WEB_PORT=8888
    fi
    log "[$(date '+%Y-%m-%d %H:%M:%S')] === Web服务启动 ==="
    "$VENV_PATH/bin/python" main.py --web --port "$WEB_PORT" < /dev/null &
    PYTHON_PID=$!

    log "等待 Web 服务启动完成..."
    sleep 1

    FLASK_WAIT_COUNT=0
    FLASK_MAX_WAIT=60
    while [ $FLASK_WAIT_COUNT -lt $FLASK_MAX_WAIT ]; do
        if ! kill -0 $PYTHON_PID 2>/dev/null; then
            log "[ERROR] Web 服务进程已退出，请检查日志: file/web_output.log"
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
        log "[WARNING] Web服务启动超时（等待了$((FLASK_MAX_WAIT))秒），请检查日志: file/web_output.log"
    fi

    log_console_only "Web 服务已就绪"

    sleep 2

    LAN_ADDR=""
    
    if [ -f "$LOG_FILE" ]; then
        LAN_ADDR=$(grep -oP '局域网地址: \Khttp://[0-9.]+' "$LOG_FILE" | tail -1)
    fi

    if [ -z "$LAN_ADDR" ]; then
        if command -v ipconfig &>/dev/null; then
            LAN_IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)
        elif [ -f "/sbin/ifconfig" ]; then
            LAN_IP=$(/sbin/ifconfig 2>/dev/null | grep -E "inet (192\.168|10\.|172\.(1[6-9]|2[0-9]|3[01]))" | awk '{print $2}' | head -1)
        fi
        
        if [ -n "$LAN_IP" ]; then
            LAN_ADDR="http://${LAN_IP}:${WEB_PORT}"
        fi
    fi

    log_blank_console_only
    log_console_only "========================================"
    log_console_only "启动完成！"
    log_console_only "========================================"
    log_blank_console_only
    log_console_only "本地访问: http://localhost:$WEB_PORT"
    if [ -n "$LAN_ADDR" ]; then
        log_console_only "局域网地址: $LAN_ADDR"
    else
        log_console_only "局域网地址: 检测中..."
    fi
    log_console_only "详细日志: $LOG_FILE"
    log_blank_console_only
    log_console_only "按 Ctrl+C 停止服务"
    log_blank_console_only

    (
        while true; do
            sleep 60
            check_temp_size
        done
    ) &
    CLEANUP_PID=$!

    wait $PYTHON_PID 2>/dev/null
    kill $CLEANUP_PID 2>/dev/null
}

check_temp_size() {
    if [ -d "temp" ]; then
        local size_kb
        size_kb=$(du -sk temp 2>/dev/null | awk '{print $1}')
        LIMIT_SIZE_KB=3072
        
        if [ -n "$size_kb" ] && [ "$size_kb" -gt "$LIMIT_SIZE_KB" ]; then
            rm -rf temp/*
            log_console_only "[AUTO] temp目录超过3MB，已自动清理"
        fi
    fi
}

cleanup_exit() {
    log_blank
    log "正在清理进程..."
    pkill -9 -f "python.*main.py" 2>/dev/null || true
    pkill -9 -f "hostc" 2>/dev/null || true
    if [ -n "$CLEANUP_PID" ]; then
        kill $CLEANUP_PID 2>/dev/null || true
    fi
    log "清理完成"
    exit 0
}

main() {
    check_prerequisites || exit 1
    detect_python_env || exit 1
    detect_node_env
    test_pip_mirrors
    test_npm_mirrors
    detect_venv
    setup_venv
    check_config
}

trap cleanup_exit INT TERM EXIT

pre_launch
main