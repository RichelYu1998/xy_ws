@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

for /f "delims=" %%i in ('py -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')"') do set VERSION=%%i
if not defined VERSION set VERSION=0.0.0

echo ========================================
echo Szwego商品爬虫和货号对比工具 - v%VERSION%
echo ========================================

echo.
echo [*] 清理临时文件...
if exist temp (
    set "TOTAL_SIZE=0"
    for /f "tokens=3" %%a in ('dir /s /-c temp ^| findstr /i "bytes"') do (
        set "SIZE_STR=%%a"
        set "SIZE_STR=!SIZE_STR:,=!"
        set "TOTAL_SIZE=!SIZE_STR!"
    )
    if not defined TOTAL_SIZE set "TOTAL_SIZE=0"
    set "LIMIT_SIZE=3145728"
    if !TOTAL_SIZE! gtr !LIMIT_SIZE! (
        del /f /s /q temp\*.* >nul 2>&1
        echo [*] temp目录超过3MB，已清理所有文件
    ) else (
        echo [*] temp目录未超过3MB，跳过清理
    )
) else (
    echo [*] temp目录不存在，跳过清理
)

echo [*] 清理浏览器临时文件...
if exist playwright-browsers (
    echo [*] 删除playwright-browsers目录中的临时zip文件...
    del /f /q playwright-browsers\*.zip >nul 2>&1
    echo [*] 浏览器临时文件清理完成
) else (
    echo [*] playwright-browsers目录不存在，跳过清理
)

goto detect_pip_mirror

:cleanup_exit
echo.
echo 正在清理进程...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im node.exe >nul 2>&1
echo 清理完成
goto :eof

:detect_pip_mirror
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

echo [2/5] 测速pip镜像源...
py main.py --select-pip-mirror

goto detect_venv

:detect_venv
echo [3/5] 检测虚拟环境...

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
echo [4/5] 设置虚拟环境...

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
    echo 正在配置pip镜像源...

    set PIP_CONFIG_FILE=%VENV_PATH%\pip_config\pip.ini

    if not exist "%VENV_PATH%\pip_config\pip.ini" (
        echo [*] 检测到未配置pip镜像源，调用Python测速...
        %VENV_PATH%\Scripts\python.exe main.py --select-pip-mirror
    )

    echo 正在安装依赖...
    %VENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt --disable-pip-version-check

    if errorlevel 1 (
        echo ERROR: 依赖安装失败，虚拟环境创建未完成
        pause
        exit /b 1
    )

    echo [*] 安装Playwright浏览器...
    %VENV_PATH%\Scripts\python.exe main.py --install-playwright
)

echo 虚拟环境设置完成
goto check_config

:check_config
echo [5/5] 检测配置文件...

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

set PYTHON_LOG_FILE=%CD%\file\web_output.log
echo. > %PYTHON_LOG_FILE%
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
echo Web日志: 查看 file\web_output.log
echo.
echo 按 Ctrl+C 停止服务，或关闭此窗口
echo.

set "CHECK_INTERVAL=60"
set "CHECK_COUNTER=0"

:wait_loop
timeout /t 1 /nobreak >nul
set /a CHECK_COUNTER+=1
if %CHECK_COUNTER% geq %CHECK_INTERVAL% (
    set "CHECK_COUNTER=0"
    call :check_temp_size
)
goto wait_loop

:check_temp_size
if exist temp (
    set "TOTAL_SIZE=0"
    for /f "tokens=3" %%a in ('dir /s /-c temp ^| findstr /i "bytes"') do (
        set "SIZE_STR=%%a"
        set "SIZE_STR=!SIZE_STR:,=!"
        set "TOTAL_SIZE=!SIZE_STR!"
    )
    if not defined TOTAL_SIZE set "TOTAL_SIZE=0"
    set "LIMIT_SIZE=3145728"
    if !TOTAL_SIZE! gtr !LIMIT_SIZE! (
        del /f /s /q temp\*.* >nul 2>&1
        echo [*] 定时检查: temp目录超过3MB，已清理所有文件
    )
)
goto :eof