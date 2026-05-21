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
echo [1/5] 检测Python环境...

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
echo [2/5] 检测虚拟环境...

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
echo [3/5] 设置虚拟环境...

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
echo [4/5] 检测配置文件...

if not exist config mkdir config

if exist config\config.json (
    echo 配置文件存在
    goto run_web
) else (
    echo 配置文件不存在，开始首次配置向导
    goto auto_setup
)

:auto_setup
echo [5/5] 自动配置...

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

:run_web
echo.
echo ========================================
echo 隧道服务配置
echo ========================================
echo.
echo 正在配置 hostc 隧道服务...
echo [5/5] 预启动隧道服务(加快首次启动速度)...
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
echo 本地访问: http://localhost:8888
echo 公网访问: 查看 file\tunnel_url.txt
echo.
echo 注意：服务将继续在后台运行
echo.
echo 关闭此窗口可停止服务，或使用:
echo   taskkill /f /im python.exe
echo   taskkill /f /im node.exe
echo.
exit /b 0

:cleanup_exit
echo.
echo 正在清理进程...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im node.exe >nul 2>&1
echo 清理完成
exit /b 0