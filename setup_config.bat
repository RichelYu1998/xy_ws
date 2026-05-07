@echo off
chcp 65001 >nul
echo ========================================
echo   Szwego爬虫 - 配置文件初始化
echo ========================================
echo.

if exist config\config.json (
    echo 配置文件已存在，如需重新初始化请先删除 config\config.json
    pause
    exit /b 0
)

echo 正在复制配置文件模板...

if exist config\config.json.example (
    copy /Y config\config.json.example config\config.json >nul
    echo ✓ config.json 已创建
) else (
    echo ⚠ config.json.example 不存在
)

if exist config\cookies.json.example (
    copy /Y config\cookies.json.example config\cookies.json >nul
    echo ✓ cookies.json 已创建
)

echo.
echo 请编辑 config\config.json，填写以下信息：
echo   - login.username: 用户名
echo   - login.password: 密码
echo   - target_url: 目标URL
echo   - headers.cookie: Cookie值
echo   - cookies中的token和sensorsdata值
echo.
echo 配置文件已创建完成

pause