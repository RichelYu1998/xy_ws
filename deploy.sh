#!/bin/bash
set -e

APP_NAME="xy_ws"
BASE_DIR="/opt/apps"
LOG_DIR="/var/log/$APP_NAME"

log_info() { echo "[INFO] $1"; }
log_error() { echo "[ERROR] $1"; }

ENVIRONMENT=${1:-staging}
log_info "部署到 $ENVIRONMENT 环境..."

# 备份、更新代码、安装依赖、重启服务
if [ -d "$BASE_DIR/$APP_NAME" ]; then
    BACKUP_DIR="$BASE_DIR/backups/$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BASE_DIR/backups"
    cp -r "$BASE_DIR/$APP_NAME" "$BACKUP_DIR"
fi

cd "$BASE_DIR/$APP_NAME"
git pull origin master

source venv/bin/activate 2>/dev/null || python3 -m venv venv && source venv/bin/activate
pip install -q -r requirements.txt

CONFIG_FILE="config/${ENVIRONMENT}.json"
[ -f "$CONFIG_FILE" ] && cp "$CONFIG_FILE" config/config.json

# 重启
[ -f "$BASE_DIR/$APP_NAME.pid" ] && kill $(cat "$BASE_DIR/$APP_NAME.pid") 2>/dev/null
nohup python main.py > "$LOG_DIR/app.log" 2>&1 &
echo $! > "$BASE_DIR/$APP_NAME.pid"

sleep 5
curl -sf http://localhost:5000/health && log_info "✓ 部署完成！" || log_error "✗ 启动失败"
