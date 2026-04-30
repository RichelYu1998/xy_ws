@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8

title Szwego Crawler Tool

echo ========================================
echo Szwego Crawler and SKU Comparison Tool
echo Version: 2.8.0
echo ========================================
echo.

REM Check if Python is installed
where py >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Python detected:
py --version
echo.

REM Check and create virtual environment
if not exist "venv" (
    echo Virtual environment not found, creating...
    py -m venv venv
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
) else (
    echo Virtual environment found.
)

REM Activate virtual environment and install dependencies
echo.
echo Checking and installing dependencies...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

if exist "requirements.txt" (
    echo Installing requirements from requirements.txt...
    venv\Scripts\python.exe -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo WARNING: Some dependencies failed to install, but continuing...
        echo You may need to install dependencies manually.
        echo Run: venv\Scripts\python.exe -m pip install -r requirements.txt
    )
    echo Dependencies installed.
) else (
    echo No requirements.txt found, skipping dependency installation.
)

echo.
echo ========================================
echo Select running mode:
echo ========================================
echo   1 - Web Service Mode (Default port: 8888)
echo   2 - Web Service Mode (Custom port)
echo   3 - Run Scraper Task (Task 1)
echo   4 - SKU Comparison Task (Task 2)
echo   5 - Excel Comparison Task (Task 3)
echo   6 - Update Cookie Task (Task 4)
echo   7 - File Cleaner Task (Task 6)
echo   0 - Exit
echo ========================================
echo.

:menu
set /p CHOICE="Please enter option (0-7): "

set CHOICE=%CHOICE: =%
set CHOICE=%CHOICE:"=%

if "%CHOICE%"=="0" (
    echo Exiting...
    call venv\Scripts\deactivate.bat
    exit /b 0
)

if "%CHOICE%"=="1" (
    echo.
    echo Starting Web Service Mode on port 8888...
    echo Please open http://127.0.0.1:8888 in your browser
    echo Press Ctrl+C to stop the server
    echo.
    venv\Scripts\python.exe main.py --web
    goto end
)

if "%CHOICE%"=="2" (
    echo.
    set /p PORT="Enter port number (default 8888): "
    set PORT=%PORT: =%
    set PORT=%PORT:"=%
    
    if "%PORT%"=="" (
        set PORT=8888
    )
    
    echo Starting Web Service Mode on port %PORT%...
    echo Please open http://127.0.0.1:%PORT% in your browser
    echo Press Ctrl+C to stop the server
    echo.
    venv\Scripts\python.exe main.py --web --port %PORT%
    goto end
)

if "%CHOICE%"=="3" (
    echo.
    echo Running Scraper Task (Task 1)...
    echo.
    venv\Scripts\python.exe main.py --task 1
    goto end
)

if "%CHOICE%"=="4" (
    echo.
    echo Running SKU Comparison Task (Task 2)...
    echo.
    venv\Scripts\python.exe main.py --task 2
    goto end
)

if "%CHOICE%"=="5" (
    echo.
    echo Running Excel Comparison Task (Task 3)...
    echo.
    venv\Scripts\python.exe main.py --task 3
    goto end
)

if "%CHOICE%"=="6" (
    echo.
    echo Running Update Cookie Task (Task 4)...
    echo.
    venv\Scripts\python.exe main.py --task 4
    goto end
)

if "%CHOICE%"=="7" (
    echo.
    echo Running File Cleaner Task (Task 6)...
    echo.
    venv\Scripts\python.exe main.py --task 6
    goto end
)

echo.
echo ERROR: Invalid option. Please enter 0-7.
goto menu

:end
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Task failed with error code %errorlevel%
    echo.
    echo If you see module errors, please install dependencies:
    echo   venv\Scripts\python.exe -m pip install -r requirements.txt
    echo.
    pause
) else (
    echo.
    echo Task completed successfully.
    echo.
    pause
)