#!/bin/bash
export LANG="zh_CN.UTF-8"
export LC_ALL="zh_CN.UTF-8"
cd "$(dirname "$0")"

# 自动检测并请求sudo权限（如果需要）
if [ "$(id -u)" -ne 0 ]; then
    if command -v sudo &> /dev/null; then
        log "[*] 检测到非root用户，部分操作可能需要sudo权限"
    fi
fi

VERSION="0.0.0"
if [ -f "README.md" ]; then
    VERSION=$(grep -m 1 -oE '###\s+v[0-9]+(\.[0-9]+)+' README.md 2>/dev/null | grep -oE '[0-9]+(\.[0-9]+)+' | head -1 || echo "0.0.0")
    if [ "$VERSION" = "0.0.0" ]; then
        VERSION=$(grep -m 1 -oE "version:[\"]?[0-9]+(\.[0-9]+)+" README.md 2>/dev/null | grep -oE '[0-9]+(\.[0-9]+)+' | head -1 || echo "0.0.0")
    fi
fi

mkdir -p file
LOG_FILE="$(pwd)/file/web_output.log"
USE_WATCHDOG_DAEMON="${USE_WATCHDOG_DAEMON:-1}"
PW_BROWSER_PATTERN="ms-playwright|playwright-core|playwright_chromiumdev_profile|remote-debugging-pipe"
PW_PROC_PATTERN="ms-playwright|playwright-core|playwright"
PW_BROWSER_NAMES="chrome|chromium|headless_shell|firefox|msedge|node"
PW_PROC_NAMES="node|playwright"
PY_PROC_NAMES="python|python3|pythonw"
NODE_PROC_NAMES="node"
CFD_PROC_NAMES="cloudflared"
> "$LOG_FILE"

log() {
    local timestamp
    if [[ "$(uname -s)" == "Darwin" ]]; then
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    else
        timestamp=$(date '+%Y-%m-%d %H:%M:%S.%3N' 2>/dev/null || date '+%Y-%m-%d %H:%M:%S')
    fi
    echo "[$timestamp] $*"
    [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ] && echo "[$timestamp] $*" >> "$LOG_FILE" 2>/dev/null
}

log_blank() {
    echo ""
    [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ] && echo "" >> "$LOG_FILE" 2>/dev/null
}

log_console_only() {
    local timestamp
    if [[ "$(uname -s)" == "Darwin" ]]; then
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    else
        timestamp=$(date '+%Y-%m-%d %H:%M:%S.%3N' 2>/dev/null || date '+%Y-%m-%d %H:%M:%S')
    fi
    echo "[$timestamp] $*"
}

log_blank_console_only() {
    echo ""
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

    if command -v git &> /dev/null; then
        local cur_git_ver=$(git --version 2>/dev/null | awk '{print $3}')
        log "    当前Git版本: v$cur_git_ver"
        
        check_git_latest_version "$cur_git_ver"
        local git_vrc=$?
        if [ "$git_vrc" -eq 2 ]; then
            log "[*] 已跳过 Git 版本升级检查"
        elif [ "$git_vrc" -eq 1 ]; then
            log "[提示] 检测到Git有新版本，如需升级请手动执行: 系统包管理器 install git"
        else
            log "[*] Git已是最新版本"
        fi
    else
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
    kill_all_interfering_processes
    sleep 1

    wait_for_port $WEB_PORT 10
    log "[*] 残留进程清理完成"

    log_blank
    log "[*] 检查 Playwright 浏览器驱动..."
    check_and_fix_playwright

    log_blank
    log "[*] 检查 hostc 隧道工具..."
    HOSTC_BIN="$(pwd)/dist/node_modules/.bin/hostc"
    if [ ! -f "$HOSTC_BIN" ]; then
        log "[*] 本地未找到 hostc，开始安装..."
        install_hostc
    fi
    if [ -f "$HOSTC_BIN" ]; then
        HOSTC_VER=$("$HOSTC_BIN" --version 2>/dev/null || echo "unknown")
        log "[*] 当前 hostc 版本: v${HOSTC_VER}"
        
        check_hostc_latest_version "$HOSTC_VER"
        local hostc_vrc=$?
        if [ "$hostc_vrc" -eq 2 ]; then
            log "[*] 已跳过 hostc 版本升级检查"
        elif [ "$hostc_vrc" -eq 1 ]; then
            log "[*] 检测到新版本，正在自动升级 hostc..."
            install_hostc
            HOSTC_VER=$("$HOSTC_BIN" --version 2>/dev/null || echo "unknown")
            log "[*] hostc 已升级到最新版: v${HOSTC_VER}"
        else
            log "[*] hostc v${HOSTC_VER} 已是最新版本"
        fi
    else
        log "[WARNING] hostc 安装失败，隧道将不可用"
    fi

    log_blank
    log "[*] 检查 cloudflared 隧道工具..."
    CFD_BIN="$(pwd)/dist/node_modules/.bin/cloudflared"
    if [ ! -f "$CFD_BIN" ]; then
        if command -v cloudflared &> /dev/null; then
            CFD_BIN="cloudflared"
        fi
    fi
    if [ -f "$CFD_BIN" ] || command -v cloudflared &> /dev/null; then
        local cur_cfd_ver=$("$CFD_BIN" --version 2>/dev/null | awk '{print $3}')
        log "    当前cloudflared版本: $cur_cfd_ver"
        
        check_cloudflared_latest_version "$cur_cfd_ver"
        local cfd_vrc=$?
        if [ "$cfd_vrc" -eq 2 ]; then
            log "[*] 已跳过 cloudflared 版本升级检查"
        elif [ "$cfd_vrc" -eq 1 ]; then
            log "[提示] 检测到cloudflared有新版本，如需升级请手动执行: npm install cloudflared@latest --prefix dist"
        else
            log "[*] cloudflared已是最新版本"
        fi
    else
        log "[*] 未找到cloudflared，正在安装..."
        install_cloudflared
    fi

    log_blank
    log "[*] 启动 hostc 隧道（后台运行）..."
    if [ -f "$HOSTC_BIN" ]; then
        "$HOSTC_BIN" "127.0.0.1:$WEB_PORT" < /dev/null &
        log "[*] hostc 已在后台启动"
    fi

    log_blank
    log "[*] 清理临时文件..."
    cleanup_temp_dir temp 3072
    cleanup_temp_dir playwright-browsers 0
}

port_listener_pids() {
    local port="$1"
    local os_name
    os_name="$(uname -s)"

    if [[ "$os_name" =~ ^MSYS|^MINGW|^CYGWIN ]]; then
        netstat -ano 2>/dev/null | tr -d '\r' \
            | awk -v port="$port" 'tolower($4) == "listening" { n = split($2, a, ":"); if (a[n] == port) print $5 }' \
            | grep -E '^[0-9]+$' | sort -u
        return 0
    fi

    if command -v lsof &> /dev/null; then
        lsof -t -i :"$port" -sTCP:LISTEN 2>/dev/null
    elif command -v ss &> /dev/null; then
        ss -ltnp 2>/dev/null | awk -v p=":$port" '$4 ~ p {print $6}' | grep -oE 'pid=[0-9]+' | cut -d= -f2
    elif command -v netstat &> /dev/null; then
        netstat -ltnp 2>/dev/null | awk -v p=":$port" '$4 ~ p {print $7}' | cut -d/ -f1 | grep -E '^[0-9]+$'
    fi
    return 0
}

port_in_use() {
    local port="$1"
    local pids
    pids=$(port_listener_pids "$port")
    [ -n "$pids" ]
}

wait_for_port() {
    local port=$1
    local max_wait=$2
    local count=0
    
    while [ $count -lt $max_wait ]; do
        if ! port_in_use "$port"; then
            break
        fi
        count=$((count + 1))
        printf -v msg "[*] 端口%s仍被占用，等待释放... (%d/%d)" "$port" "$count" "$max_wait"
        log "$msg"
        sleep 1
    done
    
    if [ $count -ge $max_wait ]; then
        printf -v msg "[WARNING] 端口%s等待超时，强制清理..." "$port"
        log "$msg"
        kill_pids "$(port_listener_pids "$port")"
        sleep 1
    fi
}

cleanup_temp_dir() {
    local dir_name=$1
    local max_size_kb=$2

    if [ -d "$dir_name" ]; then
        local size_kb
        size_kb=$(du -sk "$dir_name" 2>/dev/null | awk '{print $1}')

        if [ -z "$size_kb" ]; then
            size_kb=0
        fi

        if [ -n "$size_kb" ] && [ "$size_kb" -gt "$max_size_kb" ] 2>/dev/null; then
            rm -rf "${dir_name:?}" 2>/dev/null
            mkdir -p "${dir_name}" 2>/dev/null
            printf -v msg "[*] %s目录超过限制 (%sKB > %sKB)，已完全清空" "$dir_name" "$size_kb" "$max_size_kb"
            log "$msg"
        else
            printf -v msg "[*] %s目录未超过限制 (%sKB <= %sKB)，跳过清理" "$dir_name" "$size_kb" "$max_size_kb"
            log "$msg"
        fi
    else
        printf -v msg "[*] %s目录不存在，跳过" "$dir_name"
        log "$msg"
    fi
}

detect_python_env() {
    log_blank
    log "========================================"
    log "综合环境检测与配置"
    log "========================================"

    log "[1/6] 检测Python环境..."

    PYTHON_CMD=""

    VENV_PATH="${VENV_PATH:-.venv}"
    resolve_venv_paths
    if [ -n "$VENV_PY" ] && [ -f "$VENV_PY" ]; then
        log "[*] 检测到项目虚拟环境解释器: $VENV_PY"
        PYTHON_CMD="$VENV_PY"
    fi

    if [ -z "$PYTHON_CMD" ] && command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif [ -z "$PYTHON_CMD" ] && command -v python &> /dev/null; then
        PYTHON_CMD="python"
    elif [ -z "$PYTHON_CMD" ]; then
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

    # Python已找到，检查版本是否需要升级
    local cur_py_ver=$("$PYTHON_CMD" --version 2>&1 | awk '{print $2}')
    if [ -n "$cur_py_ver" ]; then
        log "    当前Python版本: $cur_py_ver"
        
        check_python_latest_version "$cur_py_ver"
        local py_vrc=$?
        if [ "$py_vrc" -eq 2 ]; then
            log "[*] 已跳过 Python 版本升级检查"
        elif [ "$py_vrc" -eq 1 ]; then
            log "[提示] 检测到Python有新版本，如需升级请手动执行: 系统包管理器 install python3"
        else
            log "[*] Python已是最新版本"
        fi
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
    PYTHON_LATEST_VERSION=""
    log "    正在获取Python最新版本（使用国内镜像）..."

    # 方法1: npmmirror国内镜像（优先）
    PYTHON_LATEST_VERSION=$(curl -s --connect-timeout 8 --max-time 15 https://registry.npmmirror.com/-/binary/python/ 2>/dev/null | grep -oE 'href="[^"]*python-3\.[0-9]+\.[0-9]+' | grep -oE '3\.[0-9]+\.[0-9]+' | sort -V | tail -1)

    # 方法2: 华为云镜像
    if [ -z "$PYTHON_LATEST_VERSION" ]; then
        PYTHON_LATEST_VERSION=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.huaweicloud.com/python/ 2>/dev/null | grep -oE 'href="[^"]*python-3\.[0-9]+\.[0-9]+' | grep -oE '3\.[0-9]+\.[0-9]+' | sort -V | tail -1)
    fi

    # 方法3: 清华镜像
    if [ -z "$PYTHON_LATEST_VERSION" ]; then
        PYTHON_LATEST_VERSION=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.tuna.tsinghua.edu.cn/python/ 2>/dev/null | grep -oE 'href="[^"]*python-3\.[0-9]+\.[0-9]+' | grep -oE '3\.[0-9]+\.[0-9]+' | sort -V | tail -1)
    fi

    if [ -z "$PYTHON_LATEST_VERSION" ]; then
        log "    [WARNING] 所有国内镜像获取失败，使用安全默认值"
        PYTHON_LATEST_VERSION="3.14.0"
    fi

    log "    检测到Python最新版本: $PYTHON_LATEST_VERSION"
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
        local cur_node_ver=$(node --version 2>/dev/null)
        log "    当前Node.js版本: $cur_node_ver"
        
        check_node_latest_version "$cur_node_ver"
        local node_vrc=$?
        if [ "$node_vrc" -eq 2 ]; then
            log "[*] 已跳过 Node.js 版本升级检查"
        elif [ "$node_vrc" -eq 1 ]; then
            log "[提示] 检测到Node.js有新版本，如需升级请手动执行: 系统包管理器 install nodejs"
        else
            log "[*] Node.js v$cur_node_ver 已是最新版本"
        fi
        
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

    :: 等待 node 加入 PATH（关键修复）
    log "    等待 Node.js 安装完成..."
    for w in $(seq 1 10); do
        if command -v node &> /dev/null; then
            break
        fi
        sleep 1
    done

    :: 如果还没找到，手动添加常见路径
    if ! command -v node &> /dev/null; then
        export PATH="/usr/local/bin:/usr/bin:$PATH"
    fi

    if command -v node &> /dev/null; then
        log "[*] Node.js 已安装: $(node --version 2>&1)"
    else
        log "[WARNING] Node.js 可能未完全安装，部分功能可能不可用"
    fi
}

test_mirror_latency() {
    local url="$1"
    local raw code t

    raw=$(curl -s -I -o /dev/null -w "%{http_code}:%{time_total}" --connect-timeout 5 --max-time 8 "$url" 2>/dev/null)
    [ -n "$raw" ] || return 1

    code="${raw%%:*}"
    t="${raw#*:}"

    case "$code" in
        ""|000|0000) return 1 ;;
    esac
    [ -n "$t" ] || return 1
    case "$t" in
        "0"|"0.000"|"0.000000") return 1 ;;
    esac

    awk -v v="$t" 'BEGIN { printf "%d", v * 1000 }'
    return 0
}

test_pip_mirrors() {
    log "[3/6] 测试PIP加速镜像源..."

    if [ -z "$PYTHON_CMD" ]; then
        FASTEST_PIP_MIRROR="https://mirrors.aliyun.com/pypi/simple/"
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

        local pip_ms
        pip_ms=$(test_mirror_latency "$MIRROR_URL")

        if [ -n "$pip_ms" ]; then
            log "        $MIRROR_NAME: ${pip_ms}ms"
            if [ "$pip_ms" -lt "$MIN_TIME" ] 2>/dev/null; then
                MIN_TIME=$pip_ms
                BEST_MIRROR="$MIRROR_URL"
                BEST_NAME="$MIRROR_NAME"
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
        log "[WARNING] 所有PIP镜像测试失败，使用默认阿里云源"
        FASTEST_PIP_MIRROR="https://mirrors.aliyun.com/pypi/simple/"
    fi
}

# 检查 Node.js 是否是最新版本
# 参数: $1 = 当前版本号
# 返回: 0 = 已是最新, 1 = 需要升级
check_node_latest_version() {
    local current_ver="$1"
    current_ver=${current_ver#v}
    
    if [ -z "$current_ver" ]; then
        log "[WARNING] 无法获取当前 Node.js 版本，跳过版本检查"
        return 2
    fi
    
    log "[*] 检查 Node.js 最新版本..."
    
    local latest_ver=""
    
    # 方法1: npmmirror国内镜像（优先）
    latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://npmmirror.com/mirrors/node/index.json 2>/dev/null | grep -oP '"version":\s*"v[^"]*"' | head -1 | grep -oP 'v[0-9]+\.[0-9]+\.[0-9]+' | sed 's/v//')
    
    # 方法2: 华为云镜像
    if [ -z "$latest_ver" ]; then
        latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.huaweicloud.com/nodejs/index.json 2>/dev/null | grep -oP '"version":\s*"v[^"]*"' | head -1 | grep -oP 'v[0-9]+\.[0-9]+\.[0-9]+' | sed 's/v//')
    fi
    
    # 方法3: 清华镜像
    if [ -z "$latest_ver" ]; then
        latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.tuna.tsinghua.edu.cn/nodejs-release/index.json 2>/dev/null | grep -oP '"version":\s*"v[^"]*"' | head -1 | grep -oP 'v[0-9]+\.[0-9]+\.[0-9]+' | sed 's/v//')
    fi
    
    if [ -z "$latest_ver" ]; then
        log "[WARNING] 无法获取 Node.js 最新版本信息，跳过升级检查"
        return 2
    fi
    
    log "    当前版本: v$current_ver"
    log "    最新版本: v$latest_ver"
    
    if [ "$(printf '%s\n' "$current_ver" "$latest_ver" | sort -V | head -n1)" != "$latest_ver" ]; then
        return 1
    fi
    
    return 0
}

# 检查 Python 是否是最新版本
check_python_latest_version() {
    local current_ver="$1"
    
    if [ -z "$current_ver" ]; then
        log "[WARNING] 无法获取当前 Python 版本，跳过版本检查"
        return 2
    fi
    
    log "[*] 检查 Python 最新版本..."
    
    local latest_ver=""
    
    # 方法1: npmmirror国内镜像（优先）
    latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://registry.npmmirror.com/-/binary/python/ 2>/dev/null | grep -oE 'href="[^"]*python-3\.[0-9]+\.[0-9]+' | grep -oE '3\.[0-9]+\.[0-9]+' | sort -V | tail -1)
    
    # 方法2: 华为云镜像
    if [ -z "$latest_ver" ]; then
        latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.huaweicloud.com/python/ 2>/dev/null | grep -oE 'href="[^"]*python-3\.[0-9]+\.[0-9]+' | grep -oE '3\.[0-9]+\.[0-9]+' | sort -V | tail -1)
    fi
    
    # 方法3: 清华镜像
    if [ -z "$latest_ver" ]; then
        latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.tuna.tsinghua.edu.cn/python/ 2>/dev/null | grep -oE 'href="[^"]*python-3\.[0-9]+\.[0-9]+' | grep -oE '3\.[0-9]+\.[0-9]+' | sort -V | tail -1)
    fi
    
    if [ -z "$latest_ver" ]; then
        log "[WARNING] 无法获取 Python 最新版本信息，跳过升级检查"
        return 2
    fi
    
    log "    当前版本: $current_ver"
    log "    最新版本: $latest_ver"
    
    if [ "$(printf '%s\n' "$current_ver" "$latest_ver" | sort -V | head -n1)" != "$latest_ver" ]; then
        return 1
    fi
    
    return 0
}

# 检查 Git 是否是最新版本
check_git_latest_version() {
    local current_ver="$1"
    
    if [ -z "$current_ver" ]; then
        log "[WARNING] 无法获取当前 Git 版本，跳过版本检查"
        return 2
    fi
    
    log "[*] 检查 Git 最新版本..."
    
    local latest_ver=""
    
    # 方法1: npmmirror国内镜像（优先）
    latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://registry.npmmirror.com/-/binary/git-for-windows/git/releases/latest 2>/dev/null | grep -oP '"tag_name":\s*"[^"]*"' | head -1 | grep -oP '[0-9]+\.[0-9]+\.[0-9]+')
    
    # 方法2: 华为云镜像
    if [ -z "$latest_ver" ]; then
        latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.huaweicloud.com/git-for-windows/ 2>/dev/null | grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+' | sort -V | tail -1 | sed 's/v//')
    fi
    
    # 方法3: 清华镜像
    if [ -z "$latest_ver" ]; then
        latest_ver=$(curl -s --connect-timeout 8 --max-time 15 https://mirrors.tuna.tsinghua.edu.cn/git-for-windows/ 2>/dev/null | grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+' | sort -V | tail -1 | sed 's/v//')
    fi
    
    if [ -z "$latest_ver" ]; then
        log "[WARNING] 无法获取 Git 最新版本信息，跳过升级检查"
        return 2
    fi
    
    log "    当前版本: v$current_ver"
    log "    最新版本: v$latest_ver"
    
    if [ "$(printf '%s\n' "$current_ver" "$latest_ver" | sort -V | head -n1)" != "$latest_ver" ]; then
        return 1
    fi
    
    return 0
}

# 安装 cloudflared
install_cloudflared() {
    log "[*] 安装 cloudflared..."
    npm install cloudflared@latest --prefix dist 2>/dev/null
    if [ $? -ne 0 ]; then
        log "[WARNING] cloudflared 安装失败，Cloudflare隧道将不可用"
    else
        log "[*] cloudflared 安装成功"
    fi
}

# 检查 cloudflared 是否是最新版本
check_cloudflared_latest_version() {
    local current_ver="$1"
    
    if [ -z "$current_ver" ]; then
        log "[WARNING] 无法获取当前 cloudflared 版本，跳过版本检查"
        return 2
    fi
    
    log "[*] 检查 cloudflared 最新版本..."
    
    local latest_ver=$(npm view cloudflared version 2>/dev/null || echo "")
    
    if [ -z "$latest_ver" ]; then
        log "[WARNING] 无法获取 cloudflared 最新版本信息，跳过升级检查"
        return 2
    fi
    
    log "    当前版本: $current_ver"
    log "    最新版本: $latest_ver"
    
    if [ "$(printf '%s\n' "$current_ver" "$latest_ver" | sort -V | head -n1)" != "$latest_ver" ]; then
        return 1
    fi
    
    return 0
}

install_hostc() {
    log "[*] CDN轮询安装 hostc..."

    declare -a HOSTC_MIRRORS=(
        "https://registry.npmmirror.com|npmmirror淘宝"
        "https://repo.huaweicloud.com/repository/npm/|华为云"
        "https://registry.npmjs.org|官方源"
    )

    HOSTC_BEST_MIRROR="https://registry.npmmirror.com"
    HOSTC_BEST_NAME="npmmirror淘宝"
    HOSTC_MIN_TIME=9999

    for hostc_mirror_entry in "${HOSTC_MIRRORS[@]}"; do
        IFS='|' read -r H_URL H_NAME <<< "$hostc_mirror_entry"

        local hostc_ms
        hostc_ms=$(test_mirror_latency "$H_URL")

        if [ -n "$hostc_ms" ]; then
            log "    测试 $H_NAME: ${hostc_ms}ms"
            if [ "$hostc_ms" -lt "$HOSTC_MIN_TIME" ] 2>/dev/null; then
                HOSTC_MIN_TIME=$hostc_ms
                HOSTC_BEST_MIRROR="$H_URL"
                HOSTC_BEST_NAME="$H_NAME"
            fi
        else
            log "    测试 $H_NAME: 超时/失败"
        fi
    done

    log "[*] 最快hostc镜像: $HOSTC_BEST_NAME [${HOSTC_MIN_TIME}ms]"
    log "[*] 使用最佳镜像安装 hostc..."
    npm install hostc@latest --registry "$HOSTC_BEST_MIRROR" --prefix dist 2>/dev/null
    if [ $? -ne 0 ]; then
        log "[ERROR] hostc 安装失败"
    else
        log "[*] hostc 安装成功"
    fi
}


# 检查 hostc 是否是最新版本
# 参数: $1 = 当前版本号
# 返回: 0 = 已是最新, 1 = 需要升级, 2 = 跳过检查
check_hostc_latest_version() {
    local current_ver="$1"
    
    if [ -z "$current_ver" ] || [ "$current_ver" = "unknown" ]; then
        log "[WARNING] 无法获取当前 hostc 版本，跳过版本检查"
        return 2
    fi
    
    log "[*] 检查 hostc 最新版本..."
    
    # 获取最新版本号
    local latest_ver=$(npm view hostc version 2>/dev/null || echo "")
    
    if [ -z "$latest_ver" ]; then
        log "[WARNING] 无法获取 hostc 最新版本信息，跳过升级检查"
        return 2
    fi
    
    log "    当前版本: v${current_ver}"
    log "    最新版本: v${latest_ver}"
    
    # 简单的版本比较（使用 sort -V）
    if [ "$(printf '%s\n' "$current_ver" "$latest_ver" | sort -V | head -n1)" != "$latest_ver" ]; then
        return 1  # 需要升级
    fi
    
    return 0  # 已是最新
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

        local npm_ms
        npm_ms=$(test_mirror_latency "$NPM_URL")

        if [ -n "$npm_ms" ]; then
            log "        $NPM_NAME: ${npm_ms}ms"
            if [ "$npm_ms" -lt "$NPM_MIN_TIME" ] 2>/dev/null; then
                NPM_MIN_TIME=$npm_ms
                NPM_BEST_MIRROR="$NPM_URL"
                NPM_BEST_NAME="$NPM_NAME"
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
        log "[WARNING] NPM镜像测试失败，强制使用淘宝源（范式规定：禁止官方源）"
        FASTEST_NPM_MIRROR="https://registry.npmmirror.com"
        npm config set registry "$FASTEST_NPM_MIRROR"
        log "[*] NPM镜像已设置为: $FASTEST_NPM_MIRROR"

        log "[*] 持久化NPM镜像到系统环境变量..."
        if [ -n "$HOME" ] && [ -f "$HOME/.bashrc" ]; then
            echo "export NPM_CONFIG_REGISTRY="${FASTEST_NPM_MIRROR}"" >> "$HOME/.bashrc"
            log "    已写入: ~/.bashrc"
        fi
        if command -v sudo &> /dev/null; then
            echo "NPM_CONFIG_REGISTRY="${FASTEST_NPM_MIRROR}"" | sudo tee -a /etc/environment > /dev/null 2>&1 || true
            log "    已写入: /etc/environment (Linux系统级)"
        fi
    fi
}

resolve_venv_paths() {
    VENV_PATH="${VENV_PATH:-.venv}"
    VENV_BIN_DIR=""
    VENV_PY=""
    VENV_ACTIVATE=""

    if [ -f "$VENV_PATH/Scripts/python.exe" ]; then
        VENV_BIN_DIR="$VENV_PATH/Scripts"
        VENV_PY="$VENV_PATH/Scripts/python.exe"
        VENV_ACTIVATE="$VENV_PATH/Scripts/activate"
    elif [ -f "$VENV_PATH/bin/python" ]; then
        VENV_BIN_DIR="$VENV_PATH/bin"
        VENV_PY="$VENV_PATH/bin/python"
        VENV_ACTIVATE="$VENV_PATH/bin/activate"
    elif [ -f "$VENV_PATH/bin/python3" ]; then
        VENV_BIN_DIR="$VENV_PATH/bin"
        VENV_PY="$VENV_PATH/bin/python3"
        VENV_ACTIVATE="$VENV_PATH/bin/activate"
    fi
}

activate_venv() {
    if [ -z "$VENV_ACTIVATE" ] || [ ! -f "$VENV_ACTIVATE" ]; then
        resolve_venv_paths
    fi
    if [ -n "$VENV_ACTIVATE" ] && [ -f "$VENV_ACTIVATE" ]; then
        # shellcheck disable=SC1090
        source "$VENV_ACTIVATE"
        return 0
    fi
    return 1
}

resolve_python_cmd() {
    if [ -z "$VENV_PY" ] || [ ! -f "$VENV_PY" ]; then
        resolve_venv_paths
    fi

    if [ -n "$VENV_PY" ] && [ -f "$VENV_PY" ]; then
        printf '%s' "$VENV_PY"
        return 0
    fi
    if command -v python3 &> /dev/null; then
        command -v python3
        return 0
    fi
    if command -v python &> /dev/null; then
        command -v python
        return 0
    fi
    if [ -n "$PYTHON_CMD" ] && command -v "$PYTHON_CMD" &> /dev/null; then
        printf '%s' "$PYTHON_CMD"
        return 0
    fi
    return 1
}

detect_venv() {
    log "[5/6] 检测Python虚拟环境..."

    VENV_PATH=".venv"
    resolve_venv_paths

    if [ -n "$VENV_PY" ] && [ -f "$VENV_PY" ]; then
        log "检测到虚拟环境：.venv (解释器: $VENV_PY)"
        VENV_EXISTS=1
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

    resolve_venv_paths
    activate_venv

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
        "$VENV_PY" main.py --check-deps > /dev/null 2>&1
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
                # 首次尝试：使用镜像源 + 预编译包（关键优化）
                pip install -r requirements.txt -i "$FASTEST_PIP_MIRROR" --only-binary :all:
                if [ $? -ne 0 ]; then
                    log "WARNING: 预编译包安装失败，尝试使用源码编译..."
                    pip install -r requirements.txt -i "$FASTEST_PIP_MIRROR"
                    if [ $? -ne 0 ]; then
                        log "WARNING: 使用镜像源安装失败，尝试默认源..."
                        pip install -r requirements.txt
                        if [ $? -ne 0 ]; then
                            log "[ERROR] 依赖安装失败，请查看日志或手动运行: $VENV_BIN_DIR/pip install -r requirements.txt"
                            exit 1
                        fi
                    fi
                fi
            else
                pip install -r requirements.txt
                if [ $? -ne 0 ]; then
                    log "[ERROR] 依赖安装失败，请手动检查网络或依赖兼容性"
                    exit 1
                fi
            fi
        fi

        log "[*] 安装Playwright浏览器..."
        "$VENV_PY" main.py --install-playwright
        if [ $? -ne 0 ]; then
            log "[ERROR] Playwright浏览器安装失败，部分功能可能不可用"
        else
            log "[*] Playwright 浏览器安装成功"
        fi
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

    resolve_venv_paths
    activate_venv

    log_blank
    log "[*] Checking BOM..."
    "$VENV_PY" main.py --check-bom > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        log "[WARNING] BOM detected, auto-fixing..."
        "$VENV_PY" main.py --fix-bom
    fi
    log "[OK] BOM check completed"
    log "Starting Web service..."
    log_blank

    WEB_PORT="${WEB_PORT:-8888}"
    if ! [[ "$WEB_PORT" =~ ^[0-9]+$ ]] || [ "$WEB_PORT" -lt 1 ] || [ "$WEB_PORT" -gt 65535 ]; then
        printf -v msg "[WARNING] 端口 %s 无效，使用默认端口 8888" "$WEB_PORT"
        log "$msg"
        WEB_PORT=8888
    fi
    log "[$(date '+%Y-%m-%d %H:%M:%S')] === Web服务启动 ==="
    
    if [ "$USE_WATCHDOG_DAEMON" = "1" ]; then
        log "[*] 使用内置守护进程模式启动（防闪退增强版）..."
        nohup "$VENV_PY" main.py --watchdog --web --port "$WEB_PORT" \
            >> "$(pwd)/file/watchdog_daemon.log" 2>&1 &
        PYTHON_PID=$!
        WATCHDOG_PID=$PYTHON_PID
        echo "$PYTHON_PID" > "$(pwd)/file/watchdog.pid"
        log "[*] 内置守护进程已启动 (PID: $PYTHON_PID)"
    else
        log "[*] 使用标准模式启动..."
        nohup "$VENV_PY" main.py --web --port "$WEB_PORT" < /dev/null &
        PYTHON_PID=$!
        echo "$PYTHON_PID" > "$(pwd)/file/web.pid"
        log "[*] Web服务已启动 (PID: $PYTHON_PID)"
    fi

    log "等待 Web 服务启动完成..."
    sleep 1

    FLASK_WAIT_COUNT=0
    if [ "$USE_WATCHDOG_DAEMON" = "1" ]; then
        FLASK_MAX_WAIT=120
    else
        FLASK_MAX_WAIT=60
    fi
    while [ $FLASK_WAIT_COUNT -lt $FLASK_MAX_WAIT ]; do
        if ! kill -0 $PYTHON_PID 2>/dev/null; then
            log "[ERROR] Web 服务进程已退出，请检查日志: file/web_output.log"
            exit 1
        fi
        HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 --max-time 5 "http://localhost:$WEB_PORT" 2>/dev/null)
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
        if [[ "$(uname -s)" == "Darwin" ]] && command -v ipconfig &>/dev/null; then
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

    HEALTH_CHECK_INTERVAL=30
    HEALTH_COUNTER=0
    HEALTH_FAIL_COUNT=0
    HEALTH_MAX_FAILS=3
    HEARTBEAT_SUCCESS_COUNT=0
    HEARTBEAT_WINDOW=1800
    WEB_RESTART_COUNT=0
    WEB_MAX_RESTARTS=10
    WEB_RESTART_COOLDOWN=10

    watchdog_loop() {
        while true; do
            sleep 30
            HEALTH_COUNTER=$((HEALTH_COUNTER + 1))

            if [ $HEALTH_COUNTER -ge $HEALTH_CHECK_INTERVAL ]; then
                HEALTH_COUNTER=0
                HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 --max-time 5 "http://localhost:$WEB_PORT" 2>/dev/null)
                if [ -z "$HTTP_CODE" ]; then
                    HTTP_CODE="000"
                fi

                if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "302" ]; then
                    if [ $HEALTH_FAIL_COUNT -gt 0 ]; then
                        log "[看门狗] ✅ Web服务恢复正常 (此前连续${HEALTH_FAIL_COUNT}次失败)"
                    fi
                    HEALTH_FAIL_COUNT=0
                    HEARTBEAT_SUCCESS_COUNT=$((HEARTBEAT_SUCCESS_COUNT + 1))
                    if [ $HEARTBEAT_SUCCESS_COUNT -ge 60 ]; then
                        HEARTBEAT_SUCCESS_COUNT=0
                        log "[看门狗] 💚 心跳健康 - 已连续运行30分钟无异常"
                    fi
                else
                    HEARTBEAT_SUCCESS_COUNT=0
                    HEALTH_FAIL_COUNT=$((HEALTH_FAIL_COUNT + 1))
                    log "[看门狗] ❌ Web服务异常 (HTTP ${HTTP_CODE}, 连续第${HEALTH_FAIL_COUNT}次失败, 30分钟窗口内已重置)"

                    if [ $HEALTH_FAIL_COUNT -ge $HEALTH_MAX_FAILS ]; then
                        log "[看门狗] 🔄 检测到Web服务异常，执行全面清理并重启... (第${WEB_RESTART_COUNT}次/最多${WEB_MAX_RESTARTS}次)"
                        kill_all_interfering_processes
                        sleep 3

                        log "[看门狗] ⏳ 冷却${WEB_RESTART_COOLDOWN}秒后重启..."
                        sleep $WEB_RESTART_COOLDOWN

                        log "[看门狗] 🚀 正在重新启动Web服务..."
                        resolve_venv_paths
                        activate_venv
                        "$VENV_PY" main.py --web --port "$WEB_PORT" < /dev/null &
                        PYTHON_PID=$!

                        log "[看门狗] ⏱️  等待Web服务启动..."
                        RESTART_WAIT=0
                        RESTART_MAX_WAIT=60
                        while [ $RESTART_WAIT -lt $RESTART_MAX_WAIT ]; do
                            if ! kill -0 $PYTHON_PID 2>/dev/null; then
                                log "[看门狗] ⚠️  Web服务重启后进程已退出"
                                break 2
                            fi
                            RESTART_HTTP=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 --max-time 5 "http://localhost:$WEB_PORT" 2>/dev/null)
                            if [ "$RESTART_HTTP" = "200" ] || [ "$RESTART_HTTP" = "302" ]; then
                                log "[看门狗] ✅ Web服务重启成功 (第${WEB_RESTART_COUNT}次重启, 30分钟心跳计数器已重置)"
                                break
                            fi
                            RESTART_WAIT=$((RESTART_WAIT + 1))
                            sleep 1
                        done

                        if [ $RESTART_WAIT -ge $RESTART_MAX_WAIT ]; then
                            log "[看门狗] ⚠️  Web服务重启后启动超时"
                        fi

                        HEALTH_FAIL_COUNT=0
                        HEARTBEAT_SUCCESS_COUNT=0
                    fi
                fi
            fi
        done
    }

    if [ "$USE_WATCHDOG_DAEMON" != "1" ]; then
        watchdog_loop &
        WATCHDOG_PID=$!
        log "[*] 内置看门狗已启动 (PID: $WATCHDOG_PID)"
    else
        log "[*] 使用外部守护进程模式，跳过内置看门狗"
    fi

    if [ "$USE_WATCHDOG_DAEMON" = "1" ]; then
        log "[*] 守护进程模式下运行中... (按 Ctrl+C 停止)"
        wait $PYTHON_PID 2>/dev/null
        log "[*] 守护进程已退出"
    else
        while true; do
            wait $PYTHON_PID 2>/dev/null
            EXIT_CODE=$?

            if [ $WEB_RESTART_COUNT -ge $WEB_MAX_RESTARTS ]; then
                log "[AutoRestart] 已达到最大重启次数($WEB_MAX_RESTARTS)，停止自动重启"
                break
            fi

            WEB_RESTART_COUNT=$((WEB_RESTART_COUNT + 1))
            log "[AutoRestart] Web服务已退出(退出码:$EXIT_CODE)，准备自动重启... (第${WEB_RESTART_COUNT}次/最多${WEB_MAX_RESTARTS}次)"

            log "[AutoRestart] 清理残留进程..."
            kill_all_interfering_processes
            sleep 3

            log "[AutoRestart] 冷却${WEB_RESTART_COOLDOWN}秒后重启..."
            sleep $WEB_RESTART_COOLDOWN

            log "[AutoRestart] 正在重新启动Web服务..."
            resolve_venv_paths
            activate_venv
            "$VENV_PY" main.py --web --port "$WEB_PORT" < /dev/null &
            PYTHON_PID=$!

            log "[AutoRestart] 等待Web服务启动..."
            RESTART_WAIT=0
            RESTART_MAX_WAIT=60
            while [ $RESTART_WAIT -lt $RESTART_MAX_WAIT ]; do
                if ! kill -0 $PYTHON_PID 2>/dev/null; then
                    log "[AutoRestart] Web服务重启后进程已退出"
                    break 2
                fi
                HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 --max-time 5 "http://localhost:$WEB_PORT" 2>/dev/null)
                if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "302" ]; then
                    log "[AutoRestart] Web服务重启成功 (第${WEB_RESTART_COUNT}次重启)"
                    break
                fi
                RESTART_WAIT=$((RESTART_WAIT + 1))
                sleep 1
            done

            if [ $RESTART_WAIT -ge $RESTART_MAX_WAIT ]; then
                log "[AutoRestart] Web服务重启后启动超时"
            fi
        done
    fi

    kill $CLEANUP_PID 2>/dev/null
}

check_temp_size() {
    if [ -d "temp" ]; then
        local size_kb
        size_kb=$(du -sk temp 2>/dev/null | awk '{print $1}')
        local limit_size_kb=3072

        if [ -z "$size_kb" ] || [ "$size_kb" = "0" ]; then
            size_kb=0
        fi

        if [ -n "$size_kb" ] && [ "$size_kb" -gt "$limit_size_kb" ] 2>/dev/null; then
            rm -rf temp 2>/dev/null
            mkdir -p temp 2>/dev/null
            log_console_only "[AUTO] temp目录超过3MB (${size_kb}KB > ${limit_size_kb}KB)，已完全清空（删除所有文件和子文件夹）"
        fi
    fi
}

_PROC_SNAPSHOT_CACHE=""

_proc_snapshot_raw() {
    local os_name
    os_name="$(uname -s)"

    if [[ "$os_name" =~ ^MSYS|^MINGW|^CYGWIN ]]; then
        powershell -NoProfile -NonInteractive -Command \
            "Get-CimInstance Win32_Process | ForEach-Object { '{0}|{1}' -f \$_.ProcessId, \$_.CommandLine }" \
            2>/dev/null | tr -d '\r'
        return 0
    fi

    ps -eo pid=,args= 2>/dev/null | awk '{pid=$1; $1=""; sub(/^ +/, ""); print pid "|" $0}'
}

_proc_snapshot() {
    if [ -z "$_PROC_SNAPSHOT_CACHE" ]; then
        _PROC_SNAPSHOT_CACHE=$(_proc_snapshot_raw)
    fi
    printf '%s\n' "$_PROC_SNAPSHOT_CACHE"
}

_proc_snapshot_invalidate() {
    _PROC_SNAPSHOT_CACHE=""
}

_proc_pids_by_pattern() {
    local match="$1"
    local require="$2"
    local name_re="$3"
    local snapshot
    snapshot=$(_proc_snapshot)

    [ -n "$snapshot" ] || return 0

    local lines
    lines=$(printf '%s\n' "$snapshot" | grep -E -- "$match")
    if [ -n "$require" ] && [ -n "$lines" ]; then
        lines=$(printf '%s\n' "$lines" | grep -E -- "$require")
    fi
    [ -n "$lines" ] || return 0

    if [ -n "$name_re" ]; then
        lines=$(printf '%s\n' "$lines" | awk -v name_re="$name_re" '
            {
                line = $0
                pid = line
                sub(/[|].*/, "", pid)
                sub(/^[^|]*[|]/, "", line)
                tok = line
                sub(/ .*/, "", tok)
                gsub(/"/, "", tok)
                n = split(tok, parts, /[\/\\]/)
                base = tolower(parts[n])
                sub(/\.exe$/, "", base)
                if (base ~ name_re) print pid
            }')
        [ -n "$lines" ] || return 0
    fi

    printf '%s\n' "$lines" \
        | awk -F'|' -v self="$$" '{gsub(/^ +/,"",$1); if ($1 ~ /^[0-9]+$/ && $1 != self) print $1}' \
        | sort -u
    return 0
}

kill_pids() {
    local pids="$1"
    [ -n "$pids" ] || return 0

    local os_name
    os_name="$(uname -s)"
    if [[ "$os_name" =~ ^MSYS|^MINGW|^CYGWIN ]]; then
        local ids
        ids=$(printf '%s\n' "$pids" | grep -oE '[0-9]+' | paste -sd, -)
        [ -n "$ids" ] || return 0
        powershell -NoProfile -NonInteractive -Command \
            "Stop-Process -Id $ids -Force -ErrorAction SilentlyContinue" 2>/dev/null
        return 0
    fi

    local pid
    for pid in $pids; do
        kill -9 "$pid" 2>/dev/null || true
    done
}

_proc_kill_by_pattern() {
    local match="$1"
    local require="$2"
    local pids
    pids=$(_proc_pids_by_pattern "$match" "$require")
    [ -n "$pids" ] || return 0

    kill_pids "$pids"
}

kill_browser_processes() {
    _proc_snapshot_invalidate
    local pw_pids
    pw_pids=$(_proc_pids_by_pattern "$PW_BROWSER_PATTERN" "" "$PW_BROWSER_NAMES")
    local pw_count=0
    if [ -n "$pw_pids" ]; then
        pw_count=$(printf '%s\n' "$pw_pids" | grep -cE '^[0-9]+$')
        kill_pids "$pw_pids"
    fi

    if [ "$pw_count" -gt 0 ]; then
        log "    [防护] 已清理 ${pw_count} 个浏览器僵尸进程 (Playwright Chrome/Chromium)"
    else
        log "    [防护] 未发现浏览器僵尸进程"
    fi
}

kill_playwright_processes() {
    _proc_snapshot_invalidate
    local pw_pids
    pw_pids=$(_proc_pids_by_pattern "$PW_PROC_PATTERN" "" "$PW_PROC_NAMES")
    local pw_count=0
    if [ -n "$pw_pids" ]; then
        pw_count=$(printf '%s\n' "$pw_pids" | grep -cE '^[0-9]+$')
        kill_pids "$pw_pids"
    fi

    if [ "$pw_count" -gt 0 ]; then
        log "    [防护] 已清理 ${pw_count} 个 Playwright 残留进程"
    else
        log "    [防护] 未发现 Playwright 残留进程"
    fi
}

kill_all_interfering_processes() {
    log "[*] [全面防护] 开始清理所有可能干扰的进程..."

    _proc_snapshot_invalidate
    local total_killed=0

    local py_pids
    py_pids=$(_proc_pids_by_pattern "main\.py" "main\.py" "$PY_PROC_NAMES")
    if [ -n "$py_pids" ]; then
        total_killed=$((total_killed + $(printf '%s\n' "$py_pids" | grep -cE '^[0-9]+$')))
        kill_pids "$py_pids"
    fi

    local hostc_pids
    hostc_pids=$(_proc_pids_by_pattern "hostc" "" "$NODE_PROC_NAMES")
    if [ -n "$hostc_pids" ]; then
        total_killed=$((total_killed + $(printf '%s\n' "$hostc_pids" | grep -cE '^[0-9]+$')))
        kill_pids "$hostc_pids"
    fi

    local cfd_pids
    cfd_pids=$(_proc_pids_by_pattern "cloudflared" "xy_ws" "$CFD_PROC_NAMES")
    if [ -n "$cfd_pids" ]; then
        total_killed=$((total_killed + $(printf '%s\n' "$cfd_pids" | grep -cE '^[0-9]+$')))
        kill_pids "$cfd_pids"
    fi

    local pw_pids
    pw_pids=$(_proc_pids_by_pattern "$PW_BROWSER_PATTERN" "" "$PW_BROWSER_NAMES")
    if [ -n "$pw_pids" ]; then
        total_killed=$((total_killed + $(printf '%s\n' "$pw_pids" | grep -cE '^[0-9]+$')))
        kill_pids "$pw_pids"
    fi

    local port_pids
    port_pids=$(port_listener_pids "$WEB_PORT")
    if [ -n "$port_pids" ]; then
        total_killed=$((total_killed + $(printf '%s\n' "$port_pids" | grep -cE '^[0-9]+$')))
        kill_pids "$port_pids"
    fi

    if [ "$total_killed" -gt 0 ]; then
        log "    [全面防护] ✅ 已清理 ${total_killed} 个可能干扰启动的进程"
    else
        log "    [全面防护] ✅ 系统干净，无干扰进程"
    fi

    local kill_retry=0
    while [ "$kill_retry" -lt 3 ]; do
        _proc_snapshot_invalidate
        local residual=0

        local r_py
        r_py=$(_proc_pids_by_pattern "main\.py" "main\.py" "$PY_PROC_NAMES")
        if [ -n "$r_py" ]; then
            residual=$((residual + $(printf '%s\n' "$r_py" | grep -cE '^[0-9]+$')))
            kill_pids "$r_py"
        fi

        local r_port
        r_port=$(port_listener_pids "$WEB_PORT")
        if [ -n "$r_port" ]; then
            residual=$((residual + $(printf '%s\n' "$r_port" | grep -cE '^[0-9]+$')))
            kill_pids "$r_port"
        fi

        if [ "$residual" -eq 0 ]; then
            break
        fi

        total_killed=$((total_killed + residual))
        kill_retry=$((kill_retry + 1))
        sleep 1
    done

    if [ "$kill_retry" -ge 3 ]; then
        log "    [全面防护] ⚠️  残留进程清理 ${kill_retry} 轮后仍未完全释放"
    fi

    _proc_snapshot_invalidate
}

probe_browsers_dir() {
    local probe_dir="$1"
    [ -n "$probe_dir" ] || return 1
    [ -d "$probe_dir" ] || return 1

    local d
    for d in "$probe_dir"/chromium-*; do
        [ -d "$d" ] || continue
        if [ -f "$d/chrome-win/chrome.exe" ] \
            || [ -f "$d/chrome-win64/chrome.exe" ] \
            || [ -f "$d/chrome-win/headless_shell.exe" ] \
            || [ -f "$d/chrome-win64/headless_shell.exe" ] \
            || [ -f "$d/chrome-linux/chrome" ] \
            || [ -f "$d/chrome-mac/Chromium.app/Contents/MacOS/Chromium" ]; then
            printf '%s' "$probe_dir"
            return 0
        fi
    done

    for d in "$probe_dir"/chromium_headless_shell-*; do
        [ -d "$d" ] || continue
        if [ -f "$d/chrome-win/headless_shell.exe" ] \
            || [ -f "$d/chrome-win64/headless_shell.exe" ] \
            || [ -f "$d/chrome-linux/headless_shell" ]; then
            printf '%s' "$probe_dir"
            return 0
        fi
    done

    return 1
}

detect_playwright_browsers_path() {
    PW_FOUND_PATH=""

    if [ -n "$PLAYWRIGHT_BROWSERS_PATH" ]; then
        PW_FOUND_PATH=$(probe_browsers_dir "$PLAYWRIGHT_BROWSERS_PATH")
        [ -n "$PW_FOUND_PATH" ] && return 0
    fi

    PW_FOUND_PATH=$(probe_browsers_dir "$(pwd)/playwright-browsers")
    [ -n "$PW_FOUND_PATH" ] && return 0

    PW_FOUND_PATH=$(probe_browsers_dir "$HOME/.cache/ms-playwright")
    [ -n "$PW_FOUND_PATH" ] && return 0

    PW_FOUND_PATH=$(probe_browsers_dir "$HOME/Library/Caches/ms-playwright")
    [ -n "$PW_FOUND_PATH" ] && return 0

    if [ -n "$LOCALAPPDATA" ]; then
        PW_FOUND_PATH=$(probe_browsers_dir "$LOCALAPPDATA/ms-playwright")
        [ -n "$PW_FOUND_PATH" ] && return 0
    fi

    PW_FOUND_PATH=$(probe_browsers_dir "$USERPROFILE/AppData/Local/ms-playwright")
    [ -n "$PW_FOUND_PATH" ] && return 0

    return 1
}

check_chromium_exists() {
    local browsers_path="$1"
    [ -n "$browsers_path" ] || return 1
    [ -d "$browsers_path" ] || return 1

    local found
    found=$(probe_browsers_dir "$browsers_path")
    [ -n "$found" ]
}

check_and_fix_playwright() {
    resolve_venv_paths

    PLAYWRIGHT_VER=""
    if [ -n "$VENV_PY" ] && [ -f "$VENV_PY" ]; then
        PLAYWRIGHT_VER=$("$VENV_PY" -c "from importlib.metadata import version; print(version('playwright'))" 2>/dev/null)
    fi
    if [ -z "$PLAYWRIGHT_VER" ]; then
        PLAYWRIGHT_VER="unknown"
    fi

    if detect_playwright_browsers_path; then
        PLAYWRIGHT_BROWSERS_PATH="$PW_FOUND_PATH"
        export PLAYWRIGHT_BROWSERS_PATH
        log "    [Playwright] ✅ Chromium 浏览器驱动正常 (Playwright v${PLAYWRIGHT_VER})"
        log "    [Playwright]    驱动目录: $PLAYWRIGHT_BROWSERS_PATH"
        return 0
    fi

    log "    [Playwright] ⚠️  未检测到 Chromium 浏览器驱动 (Playwright v${PLAYWRIGHT_VER})"
    log "    [Playwright] 🔄 正在自动安装 Playwright 浏览器..."

    local pw_python
    pw_python=$(resolve_python_cmd)
    if [ -z "$pw_python" ]; then
        log "    [Playwright] ❌ 未找到可用的 Python 解释器，请手动执行：python -m playwright install chromium"
        return 1
    fi

    activate_venv
    "$pw_python" -m playwright install chromium 2>&1

    if detect_playwright_browsers_path; then
        PLAYWRIGHT_BROWSERS_PATH="$PW_FOUND_PATH"
        export PLAYWRIGHT_BROWSERS_PATH
        log "    [Playwright] ✅ Chromium 浏览器安装成功"
        log "    [Playwright]    驱动目录: $PLAYWRIGHT_BROWSERS_PATH"
    else
        log "    [Playwright] ❌ Chromium 浏览器安装失败，请手动执行：$pw_python -m playwright install chromium"
    fi
}

cleanup_exit() {
    log_blank
    log "正在清理进程..."
    kill_all_interfering_processes
    if [ -n "$CLEANUP_PID" ]; then
        kill $CLEANUP_PID 2>/dev/null || true
    fi
    if [ -n "$WATCHDOG_PID" ]; then
        kill $WATCHDOG_PID 2>/dev/null || true
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