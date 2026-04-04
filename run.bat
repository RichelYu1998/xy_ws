@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul
echo ========================================
echo Szwego商品爬虫和货号对比工具 - v1.8.0
echo ========================================
echo.

REM 获取开始时间
set START_TIME=%time%
echo 开始时间: %START_TIME%
echo.

REM 检查虚拟环境
if not exist ".venv\Scripts\python.exe" (
    echo 虚拟环境不存在，正在创建...
    python -m venv .venv
    if errorlevel 1 (
        echo 创建虚拟环境失败，请确保已安装Python 3.7+
        pause
        exit /b 1
    )
    echo 正在安装依赖...
    .venv\Scripts\pip.exe install -r requirements.txt
    if errorlevel 1 (
        echo 安装依赖失败
        pause
        exit /b 1
    )
    echo 正在安装Playwright浏览器...
    .venv\Scripts\playwright.exe install chromium
)

REM 检查配置文件
if not exist "config\config.json" (
    echo 配置文件不存在，请先配置 config\config.json
    pause
    exit /b 1
)

REM 运行程序
.venv\Scripts\python.exe main.py

REM 获取结束时间
set END_TIME=%time%
echo.
echo ========================================
echo 结束时间: %END_TIME%
echo ========================================
pause