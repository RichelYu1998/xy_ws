@echo off
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

echo ========================================
echo Szwego商品爬虫和货号对比工具 - v2.6.0
echo ========================================
goto detect_python

:detect_python
echo.
echo ========================================
echo 环境检测与配置
echo ========================================
echo [1/6] 检测Python环境...

where py >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python环境检测失败
    echo.
    echo 请先安装Python 3.10或更高版本：
    echo   下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python版本：
py --version
goto detect_venv

:detect_venv
echo [2/6] 检测虚拟环境...

if exist venv\Scripts\activate.bat (
    echo 检测到虚拟环境：venv
    set VENV_EXISTS=1
    set VENV_PATH=venv
) else if exist .venv\Scripts\activate.bat (
    echo 检测到虚拟环境：.venv
    set VENV_EXISTS=1
    set VENV_PATH=.venv
) else (
    echo 未检测到虚拟环境
    set VENV_EXISTS=0
    set VENV_PATH=
)
goto setup_venv

:setup_venv
echo [3/6] 设置虚拟环境...

if %VENV_EXISTS%==0 (
    echo 正在创建虚拟环境...
    py -m venv .venv
    if errorlevel 1 (
        echo ERROR: 创建虚拟环境失败
        pause
        exit /b 1
    )
    set VENV_PATH=.venv
    set VENV_EXISTS=1
)

if not exist %VENV_PATH% (
    echo ERROR: 虚拟环境路径不存在：%VENV_PATH%
    pause
    exit /b 1
)

call %VENV_PATH%\Scripts\activate.bat

if exist requirements.txt (
    echo 正在安装依赖...
    %VENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt --disable-pip-version-check -q
)

echo 虚拟环境设置完成
goto check_config

:check_config
echo [4/7] 检测配置文件...

if not exist config mkdir config

if exist config\config.json (
    echo 配置文件存在
    goto check_cloudflare
) else (
    echo 配置文件不存在，开始首次配置向导
    goto auto_setup
)

:auto_setup
echo [5/7] 自动配置...

echo.
echo 正在复制配置文件模板...

if exist config\config.json.example (
    copy /Y config\config.json.example config\config.json >nul
    echo [OK] config.json 已创建
) else (
    echo [WARNING] config.json.example 不存在
)

if exist config\cookies.json.example (
    copy /Y config\cookies.json.example config\cookies.json >nul
    echo [OK] cookies.json 已创建
)

echo.
echo ========================================
echo 首次配置完成！
echo ========================================
echo.
echo 请编辑 config\config.json，填写以下信息：
echo   - login.username: 用户名
echo   - login.password: 密码
echo   - target_url: 目标URL
echo   - headers.cookie: Cookie值
echo   - cookies中的token和sensorsdata值
echo.
set /p CHOICE="按回车键继续，或输入 Q 退出: "

if /i "%CHOICE%"=="Q" goto cleanup_exit

:check_cloudflare
echo [6/7] Checking Cloudflare Tunnel configuration...

if exist file\cloudflare_tunnel.txt (
    echo Cloudflare Tunnel configured
    set CLOUDFLARE_CONFIGURED=1
) else (
    echo Cloudflare Tunnel not configured
    set CLOUDFLARE_CONFIGURED=0
)

echo.
echo ========================================
echo Tunnel Service Selection
echo ========================================
echo.
echo Please select tunnel service type:
echo   1. Use hostc tunnel (default, fast startup)
echo   2. Configure Cloudflare Tunnel (auto download and install cloudflared)
echo   3. Skip tunnel configuration
echo.
set /p TUNNEL_CHOICE="Enter option (1-3, default: 1): "

if "%TUNNEL_CHOICE%"=="" set TUNNEL_CHOICE=1

if "%TUNNEL_CHOICE%"=="1" goto run_web
if "%TUNNEL_CHOICE%"=="2" goto setup_cloudflare
if "%TUNNEL_CHOICE%"=="3" goto run_web_no_tunnel

echo Invalid option, using default hostc tunnel
goto run_web

:setup_cloudflare
echo.
echo ========================================
echo Cloudflare Tunnel 配置向导
echo ========================================

REM Check if cloudflared is installed
where cloudflared >nul 2>&1
if errorlevel 1 (
    echo cloudflared not found
    echo.
    
    REM Check if cloudflared exists in local file directory (various naming patterns)
    if exist "file\cloudflared.exe" (
        echo Found cloudflared in file\cloudflared.exe
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=file\cloudflared.exe
        goto install_local_cloudflared
    )
    if exist "file\cloudflared-windows-amd64.exe" (
        echo Found cloudflared in file\cloudflared-windows-amd64.exe
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=file\cloudflared-windows-amd64.exe
        goto install_local_cloudflared
    )
    if exist "file\cloudflared-windows-arm64.exe" (
        echo Found cloudflared in file\cloudflared-windows-arm64.exe
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=file\cloudflared-windows-arm64.exe
        goto install_local_cloudflared
    )
    if exist "file\cloudflared-windows-386.exe" (
        echo Found cloudflared in file\cloudflared-windows-386.exe
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=file\cloudflared-windows-386.exe
        goto install_local_cloudflared
    )
    
    REM Check if cloudflared exists in current directory (various naming patterns)
    if exist "cloudflared.exe" (
        echo Found cloudflared in current directory
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=cloudflared.exe
        goto install_local_cloudflared
    )
    if exist "cloudflared-windows-amd64.exe" (
        echo Found cloudflared in current directory
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=cloudflared-windows-amd64.exe
        goto install_local_cloudflared
    )
    if exist "cloudflared-windows-arm64.exe" (
        echo Found cloudflared in current directory
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=cloudflared-windows-arm64.exe
        goto install_local_cloudflared
    )
    if exist "cloudflared-windows-386.exe" (
        echo Found cloudflared in current directory
        echo.
        setlocal enabledelayedexpansion
        set CLOUDFLARED_PATH=cloudflared-windows-386.exe
        goto install_local_cloudflared
    )
    
    echo cloudflared not found locally, downloading and installing...
    echo.
    
    REM Detect system architecture
    setlocal enabledelayedexpansion
    if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
        set ARCH=amd64
    ) else if "%PROCESSOR_ARCHITECTURE%"=="ARM64" (
        set ARCH=arm64
    ) else (
        set ARCH=386
    )
    
    echo Detected system architecture: !ARCH!
    echo.
    
    REM Download cloudflared
    set DOWNLOAD_URL=https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-!ARCH!.exe
    set CLOUDFLARED_PATH=%TEMP%\cloudflared.exe
    
    echo Downloading cloudflared...
    echo Download URL: !DOWNLOAD_URL!
    echo Download to: !CLOUDFLARED_PATH!
    echo.
    
    REM Use PowerShell to download with absolute path (fixed URL escaping)
    powershell -Command "$ProgressPreference = 'SilentlyContinue'; $url = '!DOWNLOAD_URL!'; $out = [System.IO.Path]::GetFullPath('!CLOUDFLARED_PATH!'); Invoke-WebRequest -Uri $url -OutFile $out"
    if errorlevel 1 (
        echo ERROR: Download failed
        echo.
        echo Please manually download and install cloudflared:
        echo   Windows: choco install cloudflared
        echo   Or manual download: https://github.com/cloudflare/cloudflared/releases
        echo   Or place cloudflared.exe in file\ directory
        echo.
        set /p CHOICE="Press Enter to return to main menu, or Q to exit: "
        if /i "%CHOICE%"=="Q" goto cleanup_exit
        endlocal
        goto check_cloudflare
    )
    
    echo Download successful!
    echo.
    
    :install_local_cloudflared
    REM Rename cloudflared to standard name
    echo Renaming cloudflared to standard name...
    
    REM Determine target path
    if "!CLOUDFLARED_PATH:~0,4!"=="file\" (
        set TARGET_PATH=file\cloudflared.exe
    ) else (
        set TARGET_PATH=cloudflared.exe
    )
    
    REM Copy and rename to standard name
    copy /Y "!CLOUDFLARED_PATH!" "!TARGET_PATH!" >nul 2>&1
    if errorlevel 1 (
        echo WARNING: Failed to rename, using original path
        set CLOUDFLARED_EXE=!CLOUDFLARED_PATH!
    ) else (
        echo Successfully renamed to: !TARGET_PATH!
        set CLOUDFLARED_EXE=!TARGET_PATH!
    )
    echo.
    
    REM Verify cloudflared works
    "!CLOUDFLARED_EXE!" --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: cloudflared verification failed
        echo.
        echo Please try one of the following:
        echo   1. Run as administrator
        echo   2. Place cloudflared.exe in file\ directory
        echo   3. Manually install to system PATH
        echo.
        set /p CHOICE="Press Enter to return to main menu, or Q to exit: "
        if /i "%CHOICE%"=="Q" goto cleanup_exit
        endlocal
        goto check_cloudflare
    )
    
    echo cloudflared is ready to use
    "!CLOUDFLARED_EXE!" --version
    echo.
    
    REM Save CLOUDFLARED_EXE for use after endlocal
    set SAVED_CLOUDFLARED_EXE=!CLOUDFLARED_EXE!
    endlocal
    set CLOUDFLARED_EXE=%SAVED_CLOUDFLARED_EXE%
    goto continue_cloudflare_setup
)

:continue_cloudflare_setup
if not defined CLOUDFLARED_EXE set CLOUDFLARED_EXE=cloudflared.exe
echo cloudflared is ready to use
echo.

REM Check if already logged in
echo Checking Cloudflare login status...
"!CLOUDFLARED_EXE!" tunnel list >nul 2>&1
if errorlevel 1 (
    echo Need to login to Cloudflare account
    echo.
    echo Browser will open, please select domain and authorize
    echo.
    pause
    echo Logging in...
    "!CLOUDFLARED_EXE!" tunnel login
    if errorlevel 1 (
        echo ERROR: Login failed
        pause
        goto check_cloudflare
    )
    echo Login successful!
) else (
    echo Already logged in to Cloudflare account
)
echo.

REM Input tunnel name
set /p TUNNEL_NAME="Enter tunnel name (default: szwego-tunnel): "
if "%TUNNEL_NAME%"=="" set TUNNEL_NAME=szwego-tunnel
echo Tunnel name: %TUNNEL_NAME%
echo.

REM Check if tunnel already exists
echo Checking if tunnel exists...
"!CLOUDFLARED_EXE!" tunnel info %TUNNEL_NAME% >nul 2>&1
if not errorlevel 1 (
    echo Tunnel "%TUNNEL_NAME%" already exists
    echo.
    set /p RECREATE="Recreate tunnel? (Y/N, default: N): "
    if /i not "%RECREATE%"=="Y" (
        echo Using existing tunnel...
        goto get_tunnel_info
    )
    echo Deleting existing tunnel...
    "!CLOUDFLARED_EXE!" tunnel delete %TUNNEL_NAME% -f
    if errorlevel 1 (
        echo ERROR: Failed to delete tunnel
        pause
        goto check_cloudflare
    )
    echo Existing tunnel deleted
)
echo.

REM Create new tunnel
echo Creating new tunnel: %TUNNEL_NAME%...
"!CLOUDFLARED_EXE!" tunnel create %TUNNEL_NAME%
if errorlevel 1 (
    echo ERROR: Failed to create tunnel
    pause
    goto check_cloudflare
)
echo Tunnel created successfully!
echo.

:get_tunnel_info
REM Get tunnel information
echo Getting tunnel information...
for /f "tokens=2" %%i in ('"!CLOUDFLARED_EXE!" tunnel info %TUNNEL_NAME% ^| findstr /C:"ID:"') do set TUNNEL_ID=%%i
for /f "tokens=2" %%i in ('"!CLOUDFLARED_EXE!" tunnel info %TUNNEL_NAME% ^| findstr /C:"Account:"') do set ACCOUNT_ID=%%i

echo Tunnel ID: %TUNNEL_ID%
echo Account ID: %ACCOUNT_ID%
echo.

REM Generate credential file
echo Generating credential file...
if not exist file mkdir file
set CREDENTIAL_FILE=file\%TUNNEL_ID%.json

echo Generating credential file: %CREDENTIAL_FILE%...
"!CLOUDFLARED_EXE!" tunnel token %TUNNEL_ID% > %CREDENTIAL_FILE%
if errorlevel 1 (
    echo ERROR: Failed to generate credential file
    pause
    goto check_cloudflare
)
echo Credential file generated successfully!
echo.

REM Create configuration file
echo Creating configuration file...
set CONFIG_FILE=file\cloudflare_tunnel.txt

echo Tunnel ID: %TUNNEL_ID% > %CONFIG_FILE%
echo Tunnel Name: %TUNNEL_NAME% >> %CONFIG_FILE%
echo Account ID: %ACCOUNT_ID% >> %CONFIG_FILE%

echo Configuration file created: %CONFIG_FILE%
echo.

REM Create cloudflared configuration file
set CONFIG_YML=file\cloudflare_config.yml
echo tunnel: %TUNNEL_ID% > %CONFIG_YML%
echo credentials-file: %CREDENTIAL_FILE% >> %CONFIG_YML%

echo cloudflared configuration file created: %CONFIG_YML%
echo.

echo ========================================
echo Cloudflare Tunnel configuration completed!
echo ========================================
echo.
echo Tunnel information:
echo   Name: %TUNNEL_NAME%
echo   ID: %TUNNEL_ID%
echo   Account ID: %ACCOUNT_ID%
echo.
echo Next steps:
echo   After starting service, click "Tunnel Sharing" -^> "Manage Tunnel" -^> "Configure Cloudflare" in web interface to confirm configuration
echo.
pause
goto run_web

:run_web
echo [7/7] 预启动隧道服务(加快首次启动速度)...
call npx -y hostc@latest --help >nul 2>&1
echo 隧道服务就绪

echo.
echo ========================================
echo 启动Web服务和隧道...
echo ========================================

call %VENV_PATH%\Scripts\activate.bat

echo.
echo 正在启动 Web 服务...
echo.
start /b cmd /c "call %VENV_PATH%\Scripts\activate.bat && python main.py --web"

echo 等待 Web 服务启动完成...
timeout /t 5 /nobreak >nul

:wait_flask
for /f %%i in ('curl -s -o nul -w "%%{http_code}" http://localhost:8888') do set "HTTP_CODE=%%i"
if not "%HTTP_CODE%"=="200" (
    if not "%HTTP_CODE%"=="302" (
        timeout /t 2 /nobreak >nul
        goto wait_flask
    )
)

echo Web 服务已就绪，正在启动隧道...
start /b cmd /c "npx -y hostc@latest 8888 --local-host 127.0.0.1 > file\tunnel_url.txt 2>&1"

echo.
echo ========================================
echo 启动完成！
echo ========================================
echo.
echo 访问地址: http://localhost:8888
echo 隧道地址: 查看 tunnel_url.txt
echo.
echo 注意：服务将继续在后台运行
echo.
echo 关闭此窗口可停止服务，或使用:
echo   taskkill /f /im python.exe
echo   taskkill /f /im node.exe
echo.
exit /b 0
:run_web_no_tunnel
echo [7/7] 启动Web服务...

echo.
echo ========================================
echo 启动Web服务（无隧道）...
echo ========================================

call %VENV_PATH%\Scripts\activate.bat

echo.
echo 正在启动 Web 服务...
echo.
start /b cmd /c "call %VENV_PATH%\Scripts\activate.bat && python main.py --web"

echo 等待 Web 服务启动完成...
timeout /t 5 /nobreak >nul

:wait_flask_no_tunnel
for /f %%i in ('curl -s -o nul -w "%%{http_code}" http://localhost:8888') do set "HTTP_CODE=%%i"
if not "%HTTP_CODE%"=="200" (
    if not "%HTTP_CODE%"=="302" (
        timeout /t 2 /nobreak >nul
        goto wait_flask_no_tunnel
    )
)

echo.
echo ========================================
echo 启动完成！
echo ========================================
echo.
echo 访问地址: http://localhost:8888
echo.
echo 注意：服务将继续在后台运行
echo.
echo 关闭此窗口可停止服务，或使用:
echo   taskkill /f /im python.exe
echo.
exit /b 0

:cleanup_exit
echo.
echo 正在清理进程...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im node.exe >nul 2>&1
echo 清理完成
exit /b 0