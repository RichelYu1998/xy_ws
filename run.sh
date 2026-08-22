#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

export PYTHONIOENCODING=utf-8
export LANG=en_US.UTF-8

VERSION="0.0.0"
if command -v python3 &>/dev/null; then
    VERSION=$(python3 -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')" 2>/dev/null || echo "0.0.0")
fi

WEB_PORT="${WEB_PORT:-8888}"
if ! [[ "$WEB_PORT" =~ ^[0-9]+$ ]] || [ "$WEB_PORT" -lt 1 ] || [ "$WEB_PORT" -gt 65535 ]; then
    WEB_PORT=8888
fi

LOG_FILE="$SCRIPT_DIR/file/web_output.log"
mkdir -p file

log() {
    local ts
    ts=$(date '+%Y-%m-%d %H:%M:%S.%3N')
    echo "[$ts] $*"
    [ -f "$LOG_FILE" ] && echo "[$ts] $*" >> "$LOG_FILE"
}

log "========================================"
log "Szwego商品爬虫和货号对比工具 - v${VERSION}"
log "========================================"

# ============================================================
# 清理残留进程
# ============================================================
log "[*] 清理残留进程..."
pkill -f "playwright.*node" 2>/dev/null || true
sleep 1

# ============================================================
# 检测Python环境
# ============================================================
log "[1/6] 检测Python环境..."

PYTHON_CMD=""
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
fi

if [ -z "$PYTHON_CMD" ]; then
    log "[ERROR] Python3 未安装，请先安装 Python 3.9+"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "0.0")
log "[*] Python版本: $PYTHON_VERSION"

if [ "$PYTHON_VERSION" = "0.0" ]; then
    log "[ERROR] 无法获取Python版本"
    exit 1
fi

# ============================================================
# 检测虚拟环境
# ============================================================
log "[2/6] 检测虚拟环境..."

VENV_PATH=""
if [ -f ".venv/bin/activate" ]; then
    VENV_PATH=".venv"
    log "[*] 检测到虚拟环境: .venv"
elif [ -f "venv/bin/activate" ]; then
    VENV_PATH="venv"
    log "[*] 检测到虚拟环境: venv"
fi

if [ -z "$VENV_PATH" ]; then
    log "[*] 未检测到虚拟环境，正在创建..."
    $PYTHON_CMD -m venv .venv
    VENV_PATH=".venv"
    log "[*] 虚拟环境创建成功: .venv"
fi

source "$VENV_PATH/bin/activate"
VENV_PYTHON="$VENV_PATH/bin/python"

# ============================================================
# 安装依赖
# ============================================================
log "[3/6] 检查依赖..."

$VENV_PYTHON main.py --check-deps >/dev/null 2>&1
if [ $? -ne 0 ]; then
    log "[*] 依赖缺失，正在安装..."

    PIP_MIRRORS=(
        "https://pypi.tuna.tsinghua.edu.cn/simple|清华源"
        "https://mirrors.aliyun.com/pypi/simple/|阿里云"
        "https://pypi.org/simple|官方源"
    )

    FASTEST_PIP_MIRROR=""
    for mirror_entry in "${PIP_MIRRORS[@]}"; do
        IFS='|' read -r url name <<< "$mirror_entry"
        elapsed=$(curl -s -o /dev/null -w '%{time_total}' -m 3 "$url" 2>/dev/null || echo "999")
        int_time=$(echo "$elapsed" | awk '{printf "%d", $1 * 1000}')
        log "    $name: ${elapsed}s"
        if [ -z "$FASTEST_PIP_MIRROR" ] || [ "$int_time" -lt "$FASTEST_PIP_TIME" ]; then
            FASTEST_PIP_MIRROR="$url"
            FASTEST_PIP_TIME="$int_time"
        fi
    done

    if [ -n "$FASTEST_PIP_MIRROR" ]; then
        log "[*] 使用最快镜像安装依赖..."
        $VENV_PYTHON -m pip install --upgrade pip -i "$FASTEST_PIP_MIRROR" 2>/dev/null || true
        $VENV_PYTHON -m pip install -r requirements.txt -i "$FASTEST_PIP_MIRROR" 2>/dev/null || \
            $VENV_PYTHON -m pip install -r requirements.txt
    else
        $VENV_PYTHON -m pip install -r requirements.txt
    fi

    log "[*] 安装Playwright浏览器..."
    $VENV_PYTHON main.py --install-playwright
fi

# ============================================================
# 检测配置
# ============================================================
log "[4/6] 检测配置文件..."
mkdir -p config

if [ -f "config/config.json" ]; then
    log "[*] 配置文件已存在"
else
    log "[*] 配置文件不存在，将使用默认配置"
fi

# ============================================================
# 检测Node环境 (隧道)
# ============================================================
log "[5/6] 检测Node环境..."

HOSTC_BIN=""
if command -v npx &>/dev/null; then
    if npx hostc --version &>/dev/null 2>&1; then
        HOSTC_BIN="npx hostc"
        log "[*] hostc 已就绪"
    fi
fi

# ============================================================
# 启动服务
# ============================================================
log "[6/6] 启动服务..."

log ""
log "========================================"
log "启动Web服务和隧道..."
log "========================================"

log ""
log "正在启动 Web 服务..."
log ""

log "=== Web服务启动 ==="

$VENV_PYTHON main.py --web --port "$WEB_PORT" &
WEB_PID=$!

log "等待 Web 服务启动完成..."
sleep 2

WAIT_COUNT=0
MAX_WAIT=60
while [ $WAIT_COUNT -lt $MAX_WAIT ]; do
    WAIT_COUNT=$((WAIT_COUNT + 1))
    HTTP_CODE=$(curl -s -o /dev/null -w '%{http_code}' "http://localhost:$WEB_PORT" 2>/dev/null || echo "000")
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "302" ]; then
        break
    fi
    sleep 1
done

if [ $WAIT_COUNT -ge $MAX_WAIT ]; then
    log "[ERROR] Web服务启动超时"
    exit 1
fi

# 启动隧道
if [ -n "$HOSTC_BIN" ]; then
    log "[*] 启动 hostc 隧道..."
    $HOSTC_BIN "$WEB_PORT" --local-host localhost &
fi

log ""
log "========================================"
log "启动完成！"
log "========================================"
log ""
log "本地访问: http://localhost:$WEB_PORT"
log "公网访问: 查看 file/tunnel_url.txt"
log "Web日志:  查看 file/web_output.log"
log ""
log "按 Ctrl+C 停止服务"
log ""

# 等待
wait $WEB_PID 2>/dev/null || true