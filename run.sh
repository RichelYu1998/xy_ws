#!/bin/bash

echo "========================================"
echo "Szwego商品爬虫和货号对比工具 - v2.6.0"
echo "========================================"

detect_python() {
    echo ""
    echo "========================================"
    echo "环境检测与配置"
    echo "========================================"
    echo "[1/6] 检测Python环境..."

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
    echo "[2/6] 检测虚拟环境..."

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
    echo "[3/6] 设置虚拟环境..."

    if [ "$VENV_EXISTS" -eq 0 ]; then
        echo "正在创建虚拟环境..."
        $PYTHON_CMD -m venv .venv
        VENV_PATH=".venv"
    fi

    source "$VENV_PATH/bin/activate"

    if [ -f "requirements.txt" ]; then
        echo "正在安装依赖..."
        pip install -r requirements.txt -q
    fi

    echo "虚拟环境设置完成"
}

check_config() {
    echo "[4/7] 检测配置文件..."

    mkdir -p config

    if [ -f "config/config.json" ]; then
        echo "配置文件存在"
        check_cloudflare
    else
        echo "配置文件不存在，开始首次配置向导"
        auto_setup
    fi
}

auto_setup() {
    echo "[5/7] 自动配置..."

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
    check_cloudflare
}

check_cloudflare() {
    echo "[6/7] 检测 Cloudflare Tunnel 配置..."

    if [ -f "file/cloudflare_tunnel.txt" ]; then
        echo "Cloudflare Tunnel 已配置"
        CLOUDFLARE_CONFIGURED=1
    else
        echo "Cloudflare Tunnel 未配置"
        CLOUDFLARE_CONFIGURED=0
    fi

    echo ""
    echo "========================================"
    echo "隧道服务选择"
    echo "========================================"
    echo ""
    echo "请选择隧道服务类型："
    echo "  1. 使用 hostc 隧道（默认，快速启动）"
    echo "  2. 配置 Cloudflare Tunnel（会自动下载安装 cloudflared）"
    echo "  3. 跳过隧道配置"
    echo ""
    read -p "请输入选项 (1-3，默认: 1): " TUNNEL_CHOICE
    TUNNEL_CHOICE=${TUNNEL_CHOICE:-1}

    case "$TUNNEL_CHOICE" in
        1)
            run_web
            ;;
        2)
            setup_cloudflare
            ;;
        3)
            run_web_no_tunnel
            ;;
        *)
            echo "无效选项，使用默认的 hostc 隧道"
            run_web
            ;;
    esac
}

setup_cloudflare() {
    echo ""
    echo "========================================"
    echo "Cloudflare Tunnel 配置向导"
    echo "========================================"

    # 检查 cloudflared 是否安装
    if ! command -v cloudflared &> /dev/null; then
        echo "cloudflared not found"
        echo ""
        
        # Check if cloudflared exists in local file directory (various naming patterns)
        if [ -f "file/cloudflared" ]; then
            echo "Found cloudflared in file/cloudflared"
            echo ""
            install_local_cloudflared "file/cloudflared"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "file/cloudflared-linux-amd64" ]; then
            echo "Found cloudflared in file/cloudflared-linux-amd64"
            echo ""
            install_local_cloudflared "file/cloudflared-linux-amd64"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "file/cloudflared-linux-arm64" ]; then
            echo "Found cloudflared in file/cloudflared-linux-arm64"
            echo ""
            install_local_cloudflared "file/cloudflared-linux-arm64"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "file/cloudflared-linux-arm" ]; then
            echo "Found cloudflared in file/cloudflared-linux-arm"
            echo ""
            install_local_cloudflared "file/cloudflared-linux-arm"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "file/cloudflared-darwin-amd64" ]; then
            echo "Found cloudflared in file/cloudflared-darwin-amd64"
            echo ""
            install_local_cloudflared "file/cloudflared-darwin-amd64"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "file/cloudflared-darwin-arm64" ]; then
            echo "Found cloudflared in file/cloudflared-darwin-arm64"
            echo ""
            install_local_cloudflared "file/cloudflared-darwin-arm64"
            continue_cloudflare_setup
            return $?
        fi
        
        # Check if cloudflared exists in current directory (various naming patterns)
        if [ -f "cloudflared" ]; then
            echo "Found cloudflared in current directory"
            echo ""
            install_local_cloudflared "cloudflared"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "cloudflared-linux-amd64" ]; then
            echo "Found cloudflared in current directory"
            echo ""
            install_local_cloudflared "cloudflared-linux-amd64"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "cloudflared-linux-arm64" ]; then
            echo "Found cloudflared in current directory"
            echo ""
            install_local_cloudflared "cloudflared-linux-arm64"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "cloudflared-linux-arm" ]; then
            echo "Found cloudflared in current directory"
            echo ""
            install_local_cloudflared "cloudflared-linux-arm"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "cloudflared-darwin-amd64" ]; then
            echo "Found cloudflared in current directory"
            echo ""
            install_local_cloudflared "cloudflared-darwin-amd64"
            continue_cloudflare_setup
            return $?
        fi
        if [ -f "cloudflared-darwin-arm64" ]; then
            echo "Found cloudflared in current directory"
            echo ""
            install_local_cloudflared "cloudflared-darwin-arm64"
            continue_cloudflare_setup
            return $?
        fi
        
        echo "cloudflared not found locally, downloading and installing..."
        echo ""
        
        # 检测操作系统和架构
        OS_TYPE=$(uname -s)
        ARCH_TYPE=$(uname -m)
        
        echo "Detected OS: $OS_TYPE"
        echo "Detected architecture: $ARCH_TYPE"
        echo ""
        
        # 确定下载文件名
        case "$OS_TYPE" in
            Darwin)
                # Mac 系统
                case "$ARCH_TYPE" in
                    arm64|aarch64)
                        DOWNLOAD_FILE="cloudflared-darwin-arm64"
                        ;;
                    x86_64|amd64)
                        DOWNLOAD_FILE="cloudflared-darwin-amd64"
                        ;;
                    *)
                        echo "ERROR: Unsupported Mac architecture: $ARCH_TYPE"
                        echo ""
                        echo "Please manually install cloudflared:"
                        echo "  Mac: brew install cloudflared"
                        echo "  Or manual download: https://github.com/cloudflare/cloudflared/releases"
                        echo "  Or place cloudflared in file/ directory"
                        echo ""
                        read -p "Press Enter to return to main menu, or Ctrl+C to exit: "
                        check_cloudflare
                        return 1
                        ;;
                esac
                ;;
            Linux)
                # Linux 系统
                case "$ARCH_TYPE" in
                    x86_64|amd64)
                        DOWNLOAD_FILE="cloudflared-linux-amd64"
                        ;;
                    arm64|aarch64)
                        DOWNLOAD_FILE="cloudflared-linux-arm64"
                        ;;
                    armv7l|arm)
                        DOWNLOAD_FILE="cloudflared-linux-arm"
                        ;;
                    *)
                        echo "ERROR: Unsupported Linux architecture: $ARCH_TYPE"
                        echo ""
                        echo "Please manually install cloudflared:"
                        echo "  Linux: curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared && chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/"
                        echo "  Or manual download: https://github.com/cloudflare/cloudflared/releases"
                        echo "  Or place cloudflared in file/ directory"
                        echo ""
                        read -p "Press Enter to return to main menu, or Ctrl+C to exit: "
                        check_cloudflare
                        return 1
                        ;;
                esac
                ;;
            *)
                echo "ERROR: Unsupported OS: $OS_TYPE"
                echo ""
                echo "Please manually install cloudflared:"
                echo "  Mac: brew install cloudflared"
                echo "  Linux: curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared && chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/"
                echo "  Or manual download: https://github.com/cloudflare/cloudflared/releases"
                echo "  Or place cloudflared in file/ directory"
                echo ""
                read -p "Press Enter to return to main menu, or Ctrl+C to exit: "
                check_cloudflare
                return 1
                ;;
        esac
        
        DOWNLOAD_URL="https://github.com/cloudflare/cloudflared/releases/latest/download/$DOWNLOAD_FILE"
        TEMP_PATH="/tmp/cloudflared"
        
        echo "Downloading cloudflared..."
        echo "Download URL: $DOWNLOAD_URL"
        echo "Download to: $TEMP_PATH"
        echo ""
        
        # 下载文件
        if command -v curl &> /dev/null; then
            curl -L "$DOWNLOAD_URL" -o "$TEMP_PATH"
            if [ $? -ne 0 ]; then
                echo "ERROR: Download failed"
                echo ""
                echo "Please manually install cloudflared:"
                if [ "$OS_TYPE" = "Darwin" ]; then
                    echo "  Mac: brew install cloudflared"
                else
                    echo "  Linux: curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared && chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/"
                fi
                echo "  Or manual download: https://github.com/cloudflare/cloudflared/releases"
                echo "  Or place cloudflared in file/ directory"
                echo ""
                read -p "Press Enter to return to main menu, or Ctrl+C to exit: "
                check_cloudflare
                return 1
            fi
        elif command -v wget &> /dev/null; then
            wget -O "$TEMP_PATH" "$DOWNLOAD_URL"
            if [ $? -ne 0 ]; then
                echo "ERROR: Download failed"
                echo ""
                echo "Please manually install cloudflared:"
                if [ "$OS_TYPE" = "Darwin" ]; then
                    echo "  Mac: brew install cloudflared"
                else
                    echo "  Linux: curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared && chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/"
                fi
                echo "  Or manual download: https://github.com/cloudflare/cloudflared/releases"
                echo "  Or place cloudflared in file/ directory"
                echo ""
                read -p "Press Enter to return to main menu, or Ctrl+C to exit: "
                check_cloudflare
                return 1
            fi
        else
            echo "ERROR: curl or wget not found, cannot download"
            echo ""
            echo "Please manually install cloudflared:"
            if [ "$OS_TYPE" = "Darwin" ]; then
                echo "  Mac: brew install cloudflared"
            else
                echo "  Linux: curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared && chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/"
            fi
            echo "  Or manual download: https://github.com/cloudflare/cloudflared/releases"
            echo "  Or place cloudflared in file/ directory"
            echo ""
            read -p "Press Enter to return to main menu, or Ctrl+C to exit: "
            check_cloudflare
            return 1
        fi
        
        echo "Download successful!"
        echo ""
        
        # 添加执行权限
        chmod +x "$TEMP_PATH"
        
        # 安装到系统目录
        install_local_cloudflared "$TEMP_PATH"
        continue_cloudflare_setup
        return $?
    fi

    continue_cloudflare_setup
    return 0
}

continue_cloudflare_setup() {
    if [ -z "$CLOUDFLARED_EXE" ]; then
        CLOUDFLARED_EXE="cloudflared"
    fi
    echo "cloudflared is ready to use"
    echo ""
}

install_local_cloudflared() {
    local CLOUDFLARED_PATH="$1"
    
    echo "Renaming cloudflared to standard name..."
    
    # Determine target path
    if [[ "$CLOUDFLARED_PATH" == file/* ]]; then
        TARGET_PATH="file/cloudflared"
    else
        TARGET_PATH="cloudflared"
    fi
    
    # Copy and rename to standard name
    if cp "$CLOUDFLARED_PATH" "$TARGET_PATH" 2>/dev/null; then
        chmod +x "$TARGET_PATH"
        echo "Successfully renamed to: $TARGET_PATH"
        CLOUDFLARED_EXE="$TARGET_PATH"
    else
        echo "WARNING: Failed to rename, using original path"
        CLOUDFLARED_EXE="$CLOUDFLARED_PATH"
    fi
    echo ""
    
    # Verify cloudflared works
    if ! "$CLOUDFLARED_EXE" --version &> /dev/null; then
        echo "ERROR: cloudflared verification failed"
        echo ""
        echo "Please try one of the following:"
        echo "  1. Run as root/sudo"
        echo "  2. Place cloudflared in file/ directory"
        echo "  3. Manually install to system PATH"
        echo ""
        read -p "Press Enter to return to main menu, or Ctrl+C to exit: "
        check_cloudflare
        return 1
    fi
    
    echo "cloudflared is ready to use"
    "$CLOUDFLARED_EXE" --version
    echo ""
    return 0
}

    # 检查是否已经登录
    echo "检查 Cloudflare 登录状态..."
    if ! "$CLOUDFLARED_EXE" tunnel list &> /dev/null; then
        echo "需要登录 Cloudflare 账户"
        echo ""
        echo "即将打开浏览器，请选择要使用的域名并授权"
        echo ""
        read -p "按回车键继续..."
        echo "正在登录..."
        "$CLOUDFLARED_EXE" tunnel login
        if [ $? -ne 0 ]; then
            echo "ERROR: 登录失败"
            read -p "按回车键返回主菜单..."
            check_cloudflare
            return 1
        fi
        echo "登录成功！"
    else
        echo "已登录 Cloudflare 账户"
    fi
    echo ""

    # 输入隧道名称
    read -p "请输入隧道名称 (默认: szwego-tunnel): " TUNNEL_NAME
    TUNNEL_NAME=${TUNNEL_NAME:-szwego-tunnel}
    echo "隧道名称: $TUNNEL_NAME"
    echo ""

    # 检查隧道是否已存在
    echo "检查隧道是否存在..."
    if "$CLOUDFLARED_EXE" tunnel info "$TUNNEL_NAME" &> /dev/null; then
        echo "隧道 \"$TUNNEL_NAME\" 已存在"
        echo ""
        read -p "是否重新创建？(Y/N，默认: N): " RECREATE
        if [[ "$RECREATE" =~ ^[Yy]$ ]]; then
            echo "正在删除现有隧道..."
            "$CLOUDFLARED_EXE" tunnel delete "$TUNNEL_NAME" -f
            if [ $? -ne 0 ]; then
                echo "ERROR: 删除隧道失败"
                read -p "按回车键返回主菜单..."
                check_cloudflare
                return 1
            fi
            echo "现有隧道已删除"
        else
            echo "使用现有隧道..."
        fi
    fi
    echo ""

    # 创建新隧道
    echo "正在创建新隧道: $TUNNEL_NAME..."
    "$CLOUDFLARED_EXE" tunnel create "$TUNNEL_NAME"
    if [ $? -ne 0 ]; then
        echo "ERROR: 创建隧道失败"
        read -p "按回车键返回主菜单..."
        check_cloudflare
        return 1
    fi
    echo "隧道创建成功！"
    echo ""

    # 获取隧道信息
    echo "获取隧道信息..."
    TUNNEL_INFO=$("$CLOUDFLARED_EXE" tunnel info "$TUNNEL_NAME")
    TUNNEL_ID=$(echo "$TUNNEL_INFO" | grep "ID:" | awk '{print $2}')
    ACCOUNT_ID=$(echo "$TUNNEL_INFO" | grep "Account:" | awk '{print $2}')

    echo "隧道 ID: $TUNNEL_ID"
    echo "账户 ID: $ACCOUNT_ID"
    echo ""

    # 生成凭证文件
    echo "生成凭证文件..."
    mkdir -p file
    CREDENTIAL_FILE="file/${TUNNEL_ID}.json"

    echo "正在生成凭证文件: $CREDENTIAL_FILE..."
    "$CLOUDFLARED_EXE" tunnel token "$TUNNEL_ID" > "$CREDENTIAL_FILE"
    if [ $? -ne 0 ]; then
        echo "ERROR: 生成凭证文件失败"
        read -p "按回车键返回主菜单..."
        check_cloudflare
        return 1
    fi
    echo "凭证文件生成成功！"
    echo ""

    # 创建配置文件
    echo "创建配置文件..."
    CONFIG_FILE="file/cloudflare_tunnel.txt"

    cat > "$CONFIG_FILE" << EOF
Tunnel ID: $TUNNEL_ID
Tunnel Name: $TUNNEL_NAME
Account ID: $ACCOUNT_ID
EOF

    echo "配置文件创建成功: $CONFIG_FILE"
    echo ""

    # 创建 cloudflared 配置文件
    CONFIG_YML="file/cloudflare_config.yml"
    cat > "$CONFIG_YML" << EOF
tunnel: $TUNNEL_ID
credentials-file: $CREDENTIAL_FILE
EOF

    echo "cloudflared 配置文件创建成功: $CONFIG_YML"
    echo ""

    echo "========================================"
    echo "Cloudflare Tunnel 配置完成！"
    echo "========================================"
    echo ""
    echo "隧道信息:"
    echo "  名称: $TUNNEL_NAME"
    echo "  ID: $TUNNEL_ID"
    echo "  账户 ID: $ACCOUNT_ID"
    echo ""
    echo "下一步:"
    echo "  启动服务后，在Web界面点击\"隧道共享\" -> \"管理隧道\" -> \"配置 Cloudflare\" 确认配置"
    echo ""
    read -p "按回车键继续..."
    run_web
}

run_web() {
    echo "[7/7] 预启动隧道服务(加快首次启动速度)..."
    npx -y hostc@latest --help >/dev/null 2>&1
    echo "隧道服务就绪"

    echo ""
    echo "========================================"
    echo "启动Web服务和隧道..."
    echo "========================================"

    echo ""
    echo "========================================"
    echo "启动完成！"
    echo "========================================"
    echo ""
    echo "访问地址: http://localhost:8888"
    echo "隧道地址: 查看 file/tunnel_url.txt"
    echo ""
    echo "按 Ctrl+C 停止服务"
    echo ""
    echo "正在启动 Web 服务..."
    echo ""
    $PYTHON_CMD main.py --web &
    FLASK_PID=$!

    echo "等待 Web 服务启动完成..."
    sleep 5

    echo "Web 服务已就绪，正在启动隧道..."
    mkdir -p file
    npx -y hostc@latest 8888 --local-host 127.0.0.1 > file/tunnel_url.txt 2>&1 &
    HOSTC_PID=$!

    trap 'kill $FLASK_PID $HOSTC_PID 2>/dev/null; deactivate 2>/dev/null; exit 0' INT TERM

    wait $FLASK_PID
    kill $HOSTC_PID 2>/dev/null
    deactivate
}

run_web_no_tunnel() {
    echo "[7/7] 启动Web服务..."

    echo ""
    echo "========================================"
    echo "启动Web服务（无隧道）..."
    echo "========================================"

    echo ""
    echo "========================================"
    echo "启动完成！"
    echo "========================================"
    echo ""
    echo "访问地址: http://localhost:8888"
    echo ""
    echo "按 Ctrl+C 停止服务"
    echo ""
    echo "正在启动 Web 服务..."
    echo ""
    $PYTHON_CMD main.py --web &
    FLASK_PID=$!

    echo "等待 Web 服务启动完成..."
    sleep 5

    trap 'kill $FLASK_PID 2>/dev/null; deactivate 2>/dev/null; exit 0' INT TERM

    wait $FLASK_PID
    deactivate
}

detect_python || exit 1
detect_venv || exit 1
setup_venv || exit 1
check_config || exit 1