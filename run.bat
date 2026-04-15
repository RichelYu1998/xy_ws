@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul
echo ========================================
echo Szwego商品爬虫和货号对比工具 - v1.8.0
echo ========================================
echo.

call :main

:log_section
echo.
echo ========================================
echo %~1
echo ========================================
goto :eof

:log_info
echo ✓ %~1
goto :eof

:log_warn
echo ⚠ %~1
goto :eof

:log_error
echo ✗ %~1
goto :eof

:detect_python
call :log_section "🔍 环境检测与配置"

echo [1/6] 检测Python环境...
set PYTHON_CMD=

where py >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    for /f "tokens=2" %%i in ('py --version 2^>^&1') do set PYTHON_VERSION=%%i
    call :log_info "Python版本：!PYTHON_VERSION! (命令: py)"
    goto :python_found
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python3
    for /f "tokens=2" %%i in ('python3 --version 2^>^&1') do set PYTHON_VERSION=%%i
    call :log_info "Python版本：!PYTHON_VERSION! (命令: python3)"
    goto :python_found
)

where python >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
    call :log_info "Python版本：!PYTHON_VERSION! (命令: python)"
    goto :python_found
)

call :log_error "Python环境检测失败"
echo.
echo 请先安装Python 3.10或更高版本：
echo   从 https://www.python.org/downloads/ 下载安装
exit /b 1

:python_found
exit /b 0

:detect_venv
echo [2/6] 检测虚拟环境...

set VENV_EXISTS=0
set VENV_PATH=

if exist "venv\Scripts\activate.bat" (
    call :log_info "检测到虚拟环境：venv"
    set VENV_EXISTS=1
    set VENV_PATH=venv
    goto :venv_found
)

if exist ".venv\Scripts\activate.bat" (
    call :log_info "检测到虚拟环境：.venv"
    set VENV_EXISTS=1
    set VENV_PATH=.venv
    goto :venv_found
)

call :log_warn "未检测到虚拟环境"

:venv_found
exit /b 0

:check_dependencies
echo [3/6] 检测依赖包...

if defined VENV_PATH (
    call "%VENV_PATH%\Scripts\activate.bat"
    %PYTHON_CMD% -c "import aiohttp" >nul 2>&1
    if %errorlevel% equ 0 (
        call :log_info "aiohttp依赖正常"
    ) else (
        call :log_warn "aiohttp未安装"
    )
    call deactivate
) else (
    %PYTHON_CMD% -c "import aiohttp" >nul 2>&1
    if %errorlevel% equ 0 (
        call :log_info "aiohttp依赖正常"
    ) else (
        call :log_warn "aiohttp未安装"
    )
)

exit /b 0

:check_config
echo [4/6] 检测配置文件...

if exist "config\config.json" (
    call :log_info "配置文件存在"
    exit /b 0
) else (
    call :log_error "配置文件不存在：config\config.json"
    exit /b 1
)

:setup_venv
echo [5/6] 设置虚拟环境...

if %VENV_EXISTS% equ 0 (
    call :log_info "正在创建虚拟环境..."
    %PYTHON_CMD% -m venv .venv
    if %errorlevel% neq 0 (
        call :log_error "创建虚拟环境失败"
        exit /b 1
    )
    set VENV_PATH=.venv
    set VENV_EXISTS=1
)

if not exist "%VENV_PATH%" (
    call :log_error "虚拟环境路径不存在：%VENV_PATH%"
    exit /b 1
)

call "%VENV_PATH%\Scripts\activate.bat"

if exist "requirements.txt" (
    call :log_info "正在安装依赖（使用阿里云镜像加速）..."
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    if %errorlevel% neq 0 (
        call :log_error "安装依赖失败"
        call deactivate
        exit /b 1
    )
)

where playwright >nul 2>&1
if %errorlevel% equ 0 (
    set "PLAYWRIGHT_BROWSERS_PATH=%LOCALAPPDATA%\ms-playwright"
    dir /b "%PLAYWRIGHT_BROWSERS_PATH%" 2>nul | findstr /i "chromium chrome-for-testing" >nul
    if %errorlevel% equ 0 (
        call :log_info "Playwright浏览器已存在，跳过下载"
    ) else (
        call :log_info "正在安装Playwright浏览器..."
        playwright install chromium
    )
)

call :log_info "虚拟环境设置完成"
exit /b 0

:run_program
echo [6/6] 运行程序...

if defined VENV_PATH (
    call "%VENV_PATH%\Scripts\activate.bat"
    %PYTHON_CMD% main.py
    call deactivate
) else (
    %PYTHON_CMD% main.py
)

exit /b 0

:main
call :detect_python
if %errorlevel% neq 0 exit /b 1

call :detect_venv
if %errorlevel% neq 0 exit /b 1

call :check_dependencies
if %errorlevel% neq 0 exit /b 1

call :check_config
if %errorlevel% neq 0 exit /b 1

call :setup_venv
if %errorlevel% neq 0 exit /b 1

echo.
echo ========================================
echo 开始执行任务
echo ========================================
echo.

call :run_program

echo.
echo ========================================
echo 任务完成
echo ========================================
pause