@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

echo ========================================
echo Szwego Crawler and SKU Comparison Tool
echo Version: 2.9.6
echo ========================================

REM Check Python
where py >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found
    echo Install from: https://www.python.org/downloads/
    pause & exit /b 1
)
echo Python: 
py --version

REM Setup virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    py -m venv venv >nul 2>&1
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create venv
        pause & exit /b 1
    )
)

REM Set Python path
set PYTHON_EXE=venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    echo ERROR: Virtual environment Python not found
    echo Creating new venv...
    py -m venv venv >nul 2>&1
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create venv
        pause & exit /b 1
    )
)

REM Install dependencies
if exist "requirements.txt" (
    echo Installing dependencies...
    "%PYTHON_EXE%" -m pip install -r requirements.txt -q --disable-pip-version-check >nul 2>&1
)

REM Menu
echo.
echo 1 - Web Service (port 8888)
echo 2 - Web Service (custom port)
echo 3 - Scraper Task
echo 4 - SKU Comparison
echo 5 - Excel Comparison
echo 6 - Update Cookie
echo 7 - File Cleaner
echo 0 - Exit
echo ========================================

:menu
set /p CHOICE="Select option (0-7): "
set CHOICE=%CHOICE: =%
set CHOICE=%CHOICE:"=%

if "%CHOICE%"=="0" (
    exit /b 0
)

if "%CHOICE%"=="1" (
    echo.
    echo Starting Web Service on port 8888...
    echo Open: http://127.0.0.1:8888
    echo Press Ctrl+C to stop
    echo.
    "%PYTHON_EXE%" main.py --web
    goto end
)

if "%CHOICE%"=="2" (
    set /p PORT="Port (default 8888): "
    set PORT=%PORT: =%
    set PORT=%PORT:"=%
    if "%PORT%"=="" set PORT=8888
    echo.
    echo Starting Web Service on port %PORT%...
    echo Open: http://127.0.0.1:%PORT%
    echo Press Ctrl+C to stop
    echo.
    "%PYTHON_EXE%" main.py --web --port %PORT%
    goto end
)

if "%CHOICE%"=="3" (
    echo.
    echo Running Scraper Task...
    echo.
    "%PYTHON_EXE%" main.py --task 1
    goto end
)

if "%CHOICE%"=="4" (
    echo.
    echo Running SKU Comparison Task...
    echo.
    "%PYTHON_EXE%" main.py --task 2
    goto end
)

if "%CHOICE%"=="5" (
    echo.
    echo Running Excel Comparison Task...
    echo.
    "%PYTHON_EXE%" main.py --task 3
    goto end
)

if "%CHOICE%"=="6" (
    echo.
    echo Running Update Cookie Task...
    echo.
    "%PYTHON_EXE%" main.py --task 4
    goto end
)

if "%CHOICE%"=="7" (
    echo.
    echo Running File Cleaner Task...
    echo.
    "%PYTHON_EXE%" main.py --task 6
    goto end
)

echo Invalid option
goto menu

:end
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Task failed (code: %errorlevel%)
    echo Fix: "%PYTHON_EXE%" -m pip install -r requirements.txt
    pause
)