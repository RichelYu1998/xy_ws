@echo off
chcp 65001 >nul
echo ========================================
echo   Szwego爬虫 - 配置文件初始化
echo ========================================
echo.

set /p USERNAME="请输入用户名: "
set /p PASSWORD="请输入密码: "
set /p URL="请输入目标URL: "
set /p TOKEN="请输入token: "
set /p SENSORS="请输入sensorsdata(可留空): "
set /p EXCEL="请输入Excel路径(可留空): "

python setup_config.py -u "%USERNAME%" -p "%PASSWORD%" -l "%URL%" -t "%TOKEN%" -s "%SENSORS%" -e "%EXCEL%"

pause