@echo off
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

echo ========================================
echo Szwego商品爬虫和货号对比工具 - v2.6.0
echo ========================================
goto run_web

:run_web
echo.
echo ========================================
echo 启动Web服务模式
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
goto check_dependencies

:check_dependencies
echo [3/6] 检测依赖包...

if defined VENV_PATH (
    call %VENV_PATH%\Scripts\activate.bat
    py -c "import aiohttp" >nul 2>&1
    if errorlevel 1 (
        echo aiohttp未安装
    ) else (
        echo aiohttp依赖正常
    )
    call deactivate
) else (
    py -c "import aiohttp" >nul 2>&1
    if errorlevel 1 (
        echo aiohttp未安装
    ) else (
        echo aiohttp依赖正常
    )
)
goto check_config

:check_config
echo [4/6] 检测配置文件...

if exist config\config.json (
    echo 配置文件存在
) else (
    echo ERROR: 配置文件不存在：config\config.json
    pause
    exit /b 1
)
goto setup_venv

:setup_venv
echo [5/6] 设置虚拟环境...

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
    %VENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt --disable-pip-version-check
    if errorlevel 1 (
        echo ERROR: 安装依赖失败
        call deactivate
        pause
        exit /b 1
    )
)

echo 虚拟环境设置完成
goto run_program

:run_program
echo [6/6] 运行程序...

echo.
echo ========================================
echo 启动Web服务...
echo 访问地址: http://localhost:8888
echo ========================================

if defined VENV_PATH (
    call %VENV_PATH%\Scripts\activate.bat
    %VENV_PATH%\Scripts\python.exe main.py --web
    call deactivate
) else (
    py main.py --web
)
goto end

:end
pause