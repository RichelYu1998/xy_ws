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

goto detect_environments

:cleanup_exit
echo.
echo 正在清理进程...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im node.exe >nul 2>&1
echo 清理完成
goto :eof

:detect_environments
echo.
echo ========================================
echo 综合环境检测与配置
echo ========================================

set "VENV_PATH=.venv"
set "NODE_ENV_PATH=.node_env"
set "FASTEST_PIP_MIRROR="
set "FASTEST_NPM_MIRROR="

call :detect_python_env
if errorlevel 1 (
    pause
    exit /b 1
)

call :detect_node_env
if errorlevel 1 (
    echo [WARNING] Node.js环境配置失败，部分功能可能不可用
)

call :test_pip_mirrors
call :test_npm_mirrors

goto detect_venv

:detect_python_env
echo [1/6] 检测Python环境...

where py >nul 2>&1
if errorlevel 1 (
    where python >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Python未在PATH中找到
        echo.
        echo 正在尝试查找系统中的Python...
        if exist "C:\Python3*\python.exe" (
            for /d %%p in ("C:\Python3*") do set "PYTHON_PATH=%%~dp0python.exe"
        ) else if exist "C:\Program Files\Python3*\python.exe" (
            for /d %%p in ("C:\Program Files\Python3*") do set "PYTHON_PATH=%%~dp0python.exe"
        ) else if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python3*\python.exe" (
            for /d %%p in ("C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python3*") do set "PYTHON_PATH=%%~dp0python.exe"
        )
        
        if defined PYTHON_PATH (
            echo 找到Python: %PYTHON_PATH%
            for %%P in ("%PYTHON_PATH%") do set "PYTHON_DIR=%%~dpP"
            set "PATH=%PATH%;%PYTHON_DIR%"
        ) else (
            echo ERROR: 无法找到Python安装，请手动安装
            echo   下载地址: https://www.python.org/downloads/
            exit /b 1
        )
    ) else (
        set PYTHON_CMD=python
    )
) else (
    set PYTHON_CMD=py
)

echo Python版本：
%PYTHON_CMD% --version

echo [*] 检测虚拟环境状态...
if defined VIRTUAL_ENV (
    echo 当前已在虚拟环境中: %VIRTUAL_ENV%
    set IN_VENV=1
) else (
    echo 未在虚拟环境中
    set IN_VENV=0
)
exit /b 0

:detect_node_env
echo [2/6] 检测Node.js环境...

where node >nul 2>&1
if errorlevel 1 (
    echo Node.js未在PATH中
    
    where nvm >nul 2>&1
    if errorlevel 1 (
        if exist "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" (
            echo 发现NVM，正在使用NVM管理Node.js...
            call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" use latest
            if errorlevel 1 (
                echo NVM中未安装Node.js版本，正在安装...
                call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" install lts
                call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" use lts
            )
        ) else (
            echo 未发现Node.js和NVM
            echo 正在创建临时Node.js环境到 %NODE_ENV_PATH%...
            
            if not exist "%NODE_ENV_PATH%" mkdir "%NODE_ENV_PATH%"
            
            echo 下载Node.js安装程序...
            curl -L -o "%NODE_ENV_PATH%\node-installer.msi" https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi
            
            if exist "%NODE_ENV_PATH%\node-installer.msi" (
                msiexec /i "%NODE_ENV_PATH%\node-installer.msi" INSTALLDIR="%CD%\%NODE_ENV_PATH%" /quiet /norestart
                set "PATH=%CD%\%NODE_ENV_PATH%;%PATH%"
                del "%NODE_ENV_PATH%\node-installer.msi"
                echo 临时Node.js环境已创建
            ) else (
                echo [WARNING] Node.js下载失败，跳过Node.js相关功能
                exit /b 1
            )
        )
    ) else (
        echo 使用NVM管理Node.js
        nvm list
    )
) else (
    echo Node.js版本:
    node --version
    npm --version
)
exit /b 0

:test_pip_mirrors
echo [3/6] 测试PIP加速镜像源...

set "MIRRORS[0]=https://pypi.tuna.tsinghua.edu.cn/simple|清华源"
set "MIRRORS[1]=https://mirrors.aliyun.com/pypi/simple/|阿里云"
set "MIRRORS[2]=https://pypi.douban.com/simple/|豆瓣"
set "MIRRORS[3]=https://pypi.mirrors.ustc.edu.cn/simple/|中科大"

set "MIN_TIME=9999"
set "BEST_MIRROR="
set "BEST_NAME="

for /L %%i in (0,1,3) do (
    for /f "tokens=1,2 delims=|" %%a in ("!MIRRORS[%%i]!") do (
        set "MIRROR_URL=%%a"
        set "MIRROR_NAME=%%b"
        echo     测试 !MIRROR_NAME!...
        
        curl -s -o nul -w "%%{time_connect}" --connect-timeout 1.5 --max-time 2 "!MIRROR_URL!" > temp_pip_time.txt 2>&1
        set /p TEST_TIME=<temp_pip_time.txt
        del temp_pip_time.txt 2>nul
        
        if not defined TEST_TIME set "TEST_TIME=9999"
        
        if "!TEST_TIME!"=="0" (
            echo         !MIRROR_NAME!: 超时/失败
            set "TEST_TIME=9999"
        ) else (
            for /f "tokens=* delims=" %%t in ('%PYTHON_CMD% -c "print(int(float('!TEST_TIME!')*1000))"') do set "PIP_INT_TIME=%%t"
            echo         !MIRROR_NAME!: !TEST_TIME!秒 (!PIP_INT_TIME!ms)
            if !PIP_INT_TIME! LSS !MIN_TIME! (
                set "MIN_TIME=!PIP_INT_TIME!"
                set "BEST_MIRROR=!MIRROR_URL!"
                set "BEST_NAME=!MIRROR_NAME!"
            )
        )
    )
)

if "!BEST_MIRROR!"=="" (
    echo [WARNING] 所有镜像测试失败，使用默认PyPI源
    set "FASTEST_PIP_MIRROR=https://pypi.org/simple/"
) else (
    set "FASTEST_PIP_MIRROR=!BEST_MIRROR!"
    echo.
    echo [*] 最快PIP镜像: !BEST_NAME! (!MIN_TIME!毫秒)
)
exit /b 0

:test_npm_mirrors
echo [4/6] 测试NPM加速镜像源...

set "NPM_MIRRORS[0]=https://registry.npmmirror.com|npmmirror淘宝"
set "NPM_MIRRORS[1]=https://registry.npmjs.org|官方源"

set "NPM_MIN_TIME=9999"
set "NPM_BEST_MIRROR="
set "NPM_BEST_NAME="

for /L %%i in (0,1,1) do (
    for /f "tokens=1,2 delims=|" %%a in ("!NPM_MIRRORS[%%i]!") do (
        set "NPM_URL=%%a"
        set "NPM_NAME=%%b"
        echo     测试 !NPM_NAME!...
        
        curl -s -o nul -w "%%{time_total}" --connect-timeout 3 "!NPM_URL!" > temp_npm_time.txt 2>&1
        set /p NPM_TEST_TIME=<temp_npm_time.txt
        del temp_npm_time.txt 2>nul
        
        if not defined NPM_TEST_TIME set "NPM_TEST_TIME=9999"
        
        if "!NPM_TEST_TIME!"=="0" (
            echo         !NPM_NAME!: 超时/失败
        ) else (
            for /f "tokens=* delims=" %%t in ('%PYTHON_CMD% -c "print(int(float('!NPM_TEST_TIME!')*1000))"') do set "NPM_INT_TIME=%%t"
            echo         !NPM_NAME!: !NPM_TEST_TIME!秒 (!NPM_INT_TIME!ms)
            if !NPM_INT_TIME! LSS !NPM_MIN_TIME! (
                set "NPM_MIN_TIME=!NPM_INT_TIME!"
                set "NPM_BEST_MIRROR=!NPM_URL!"
                set "NPM_BEST_NAME=!NPM_NAME!"
            )
        )
    )
)

if "!NPM_BEST_MIRROR!"=="" (
    echo [WARNING] NPM镜像测试失败
) else (
    set "FASTEST_NPM_MIRROR=!NPM_BEST_MIRROR!"
    echo.
    echo [*] 最快NPM镜像: !NPM_BEST_NAME! (!NPM_MIN_TIME!毫秒)
    
    where npm >nul 2>&1
    if not errorlevel 1 (
        npm config set registry "!NPM_BEST_MIRROR!"
        echo [*] NPM镜像已设置为: !NPM_BEST_MIRROR!
    )
)
exit /b 0

:detect_venv
echo [5/6] 检测Python虚拟环境...

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
)
goto setup_venv

:setup_venv
echo [6/6] 设置Python虚拟环境并安装依赖...

if %VENV_EXISTS%==0 (
    echo 正在创建虚拟环境到 %VENV_PATH%...
    %PYTHON_CMD% -m venv %VENV_PATH%
    if errorlevel 1 (
        echo ERROR: 创建虚拟环境失败
        pause
        exit /b 1
    )
    set VENV_EXISTS=1
)

if not exist %VENV_PATH% (
    echo ERROR: 虚拟环境路径不存在：%VENV_PATH%
    pause
    exit /b 1
)

call %VENV_PATH%\Scripts\activate.bat

if defined FASTEST_PIP_MIRROR (
    echo [*] 配置PIP镜像源为: %FASTEST_PIP_MIRROR%
    
    if not exist "%VENV_PATH%\pip_config" mkdir "%VENV_PATH%\pip_config"
    
    echo [global]> "%VENV_PATH%\pip_config\pip.ini"
    echo index-url=%FASTEST_PIP_MIRROR%>> "%VENV_PATH%\pip_config\pip.ini"
    echo trusted-host=%FASTEST_PIP_MIRROR:~8,-7%>> "%VENV_PATH%\pip_config\pip.ini"
    echo [install]>> "%VENV_PATH%\pip_config\pip.ini"
    echo trusted-host=%FASTEST_PIP_MIRROR:~8,-7%>> "%VENV_PATH%\pip_config\pip.ini"
    
    set PIP_CONFIG_FILE=%VENV_PATH%\pip_config\pip.ini
)

if exist requirements.txt (
    echo 正在安装Python依赖...
    %VENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt --disable-pip-version-check -i %FASTEST_PIP_MIRROR%

    if errorlevel 1 (
        echo ERROR: 依赖安装失败，尝试使用默认源重试...
        %VENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt --disable-pip-version-check
        
        if errorlevel 1 (
            echo ERROR: 依赖安装完全失败
            pause
            exit /b 1
        )
    )

    echo [*] 安装Playwright浏览器...
    %VENV_PATH%\Scripts\python.exe main.py --install-playwright
)

echo Python虚拟环境设置完成
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