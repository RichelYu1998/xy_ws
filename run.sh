#!/bin/bash

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v1.8.0"
echo "========================================"
echo ""

log_section() {
    echo ""
    echo "========================================"
    echo "$1"
    echo "========================================"
}

log_info() {
    echo "✓ $1"
}

log_warn() {
    echo "⚠ $1"
}

log_error() {
    echo "✗ $1"
}

detect_python() {
    log_section "🔍 环境检测与配置"
    
    echo "[1/6] 检测Python环境..."
    PYTHON_CMD=""
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        log_info "Python版本：$(python3 --version 2>&1 | awk '{print $2}') (命令: python3)"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        log_info "Python版本：$(python --version 2>&1 | awk '{print $2}') (命令: python)"
    else
        log_error "Python环境检测失败"
        echo ""
        echo "请先安装Python 3.10或更高版本："
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
            echo "  CentOS/RHEL: sudo yum install python3 python3-pip"
            echo "  Arch Linux: sudo pacman -S python python-pip"
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            echo "  macOS: brew install python3"
        fi
        return 1
    fi
    
    return 0
}

detect_venv() {
    echo "[2/6] 检测虚拟环境..."
    
    if [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
        log_info "检测到虚拟环境：venv"
        VENV_EXISTS=1
        VENV_PATH="venv"
    elif [ -d ".venv" ] && [ -f ".venv/bin/activate" ]; then
        log_info "检测到虚拟环境：.venv"
        VENV_EXISTS=1
        VENV_PATH=".venv"
    else
        log_warn "未检测到虚拟环境"
        VENV_EXISTS=0
        VENV_PATH=""
    fi
    
    return 0
}

check_dependencies() {
    echo "[3/6] 检测依赖包..."
    
    if [ -n "$VENV_PATH" ]; then
        source "$VENV_PATH/bin/activate"
        if $PYTHON_CMD -c "import aiohttp" &> /dev/null; then
            log_info "aiohttp依赖正常"
        else
            log_warn "aiohttp未安装"
        fi
        deactivate
    else
        if $PYTHON_CMD -c "import aiohttp" &> /dev/null; then
            log_info "aiohttp依赖正常"
        else
            log_warn "aiohttp未安装"
        fi
    fi
    
    return 0
}

check_config() {
    echo "[4/6] 检测配置文件..."
    
    if [ -f "config/config.json" ]; then
        log_info "配置文件存在"
        return 0
    else
        log_error "配置文件不存在：config/config.json"
        return 1
    fi
}

setup_venv() {
    echo "[5/6] 设置虚拟环境..."
    
    if [ "$VENV_EXISTS" -eq 0 ]; then
        log_info "正在创建虚拟环境..."
        $PYTHON_CMD -m venv .venv
        if [ $? -ne 0 ]; then
            log_error "创建虚拟环境失败"
            return 1
        fi
        VENV_PATH=".venv"
        VENV_EXISTS=1
    fi
    
    if [ ! -d "$VENV_PATH" ]; then
        log_error "虚拟环境路径不存在：$VENV_PATH"
        return 1
    fi
    
    source "$VENV_PATH/bin/activate"
    
    if [ -f "requirements.txt" ]; then
        log_info "正在安装依赖（使用阿里云镜像加速）..."
        pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
        if [ $? -ne 0 ]; then
            log_error "安装依赖失败"
            deactivate
            return 1
        fi
    fi
    
    if command -v playwright &> /dev/null; then
        if [ -d "$HOME/.cache/ms-playwright/chromium-"* ] || [ -d "$HOME/.cache/ms-playwright/chrome-for-testing"* ]; then
            log_info "Playwright浏览器已存在，跳过下载"
        elif [ -d "$HOME/Library/Caches/ms-playwright/chromium-"* ] || [ -d "$HOME/Library/Caches/ms-playwright/chrome-for-testing"* ]; then
            log_info "Playwright浏览器已存在，跳过下载"
        elif [ -d "$HOME/Library/Caches/ms-playwright/Google Chrome for Testing.app" ]; then
            log_info "Playwright浏览器已存在，跳过下载"
        else
            log_info "正在安装Playwright浏览器..."
            playwright install chromium
        fi
    fi
    
    log_info "虚拟环境设置完成"
    return 0
}

run_program() {
    echo "[6/6] 运行程序..."
    
    if [ -n "$VENV_PATH" ]; then
        source "$VENV_PATH/bin/activate"
        $PYTHON_CMD main.py
        deactivate
    else
        $PYTHON_CMD main.py
    fi
}

main() {
    detect_python || exit 1
    detect_venv || exit 1
    check_dependencies || exit 1
    check_config || exit 1
    setup_venv || exit 1
    
    echo ""
    echo "========================================"
    echo "开始执行任务"
    echo "========================================"
    echo ""
    
    run_program
    
    echo ""
    echo "========================================"
    echo "任务完成"
    echo "========================================"
}

main