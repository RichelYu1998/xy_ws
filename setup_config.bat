@echo off
chcp 65001 >nul
echo ========================================
echo   Szwego爬虫 - 配置文件初始化
echo ========================================
echo.

set /p USERNAME="请输入用户名: "
set /p PASSWORD="请输入密码: "
set /p URL="请输入目标URL: "
set /p EXCEL="请输入Excel路径(可留空): "

echo.
echo 正在启动浏览器进行登录...
echo 请在浏览器中登录您的账号
echo.

if exist ".venv\Scripts\python.exe" (
    set PYTHON_CMD=.venv\Scripts\python.exe
) else (
    where python >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set PYTHON_CMD=python
    ) else (
        where python3 >nul 2>&1
        if %ERRORLEVEL% EQU 0 (
            set PYTHON_CMD=python3
        ) else (
            echo 错误: 未找到Python命令
            echo 请确保Python已安装并添加到系统PATH
            pause
            exit /b 1
        )
    )
)

echo 使用Python: %PYTHON_CMD%
%PYTHON_CMD% setup_config.py -u "%USERNAME%" -p "%PASSWORD%" -l "%URL%" -e "%EXCEL%"

pause