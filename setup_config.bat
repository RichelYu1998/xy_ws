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

python setup_config.py -u "%USERNAME%" -p "%PASSWORD%" -l "%URL%" -e "%EXCEL%"

pause