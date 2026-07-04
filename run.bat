@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

set "VERSION=0.0.0"
for /f "delims=" %%i in ('py -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')" 2^>nul') do set "VERSION=%%i"

if not exist file mkdir file
set "LOG_FILE=%CD%\file\web_output.log"
echo. > "!LOG_FILE!"

goto main_start

:log
echo %*
(echo %*) >> "!LOG_FILE!" 2>nul
exit /b

:log_blank
echo.
(echo.) >> "!LOG_FILE!" 2>nul
exit /b

:main_start
call :log ========================================
call :log Szwego商品爬虫和货号对比工具 - v%VERSION%
call :log ========================================

call :log_blank
call :log [*] 清理临时文件...
if exist temp (
    call :get_dir_size temp
    set "LIMIT_SIZE=3145728"
    if !TOTAL_SIZE! gtr !LIMIT_SIZE! (
        del /f /s /q temp\*.* >nul 2>&1
        call :log [*] temp目录超过3MB，已清理所有文件
    ) else (
        call :log [*] temp目录未超过3MB，跳过清理
    )
) else (
    call :log [*] temp目录不存在，跳过清理
)

call :log [*] 清理浏览器临时文件...
if exist playwright-browsers (
    call :log [*] 删除playwright-browsers目录中的临时zip文件...
    del /f /q playwright-browsers\*.zip >nul 2>&1
    call :log [*] 浏览器临时文件清理完成
) else (
    call :log [*] playwright-browsers目录不存在，跳过清理
)

goto detect_environments

:get_dir_size
set "TOTAL_SIZE=0"
for /f "delims=" %%a in ('powershell -NoProfile -Command "(Get-ChildItem -Path '%~1' -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum" 2^>nul') do set "TOTAL_SIZE=%%a"
if not defined TOTAL_SIZE set "TOTAL_SIZE=0"
if "!TOTAL_SIZE!"=="" set "TOTAL_SIZE=0"
goto :eof

:cleanup_exit
call :log_blank
call :log 正在清理进程...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im node.exe >nul 2>&1
call :log 清理完成
goto :eof

:detect_environments
call :log_blank
call :log ========================================
call :log 综合环境检测与配置
call :log ========================================

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

call :test_pip_mirrors
call :test_npm_mirrors

goto detect_venv

:detect_python_env
call :log [1/6] 检测Python环境...

where py >nul 2>&1
if errorlevel 1 (
    where python >nul 2>&1
    if errorlevel 1 (
        call :log Python未在PATH中，正在尝试查找系统中的Python...
        
        set "PYTHON_PATH="
        for /d %%p in ("C:\Python3*") do if exist "%%p\python.exe" set "PYTHON_PATH=%%p\python.exe"
        if not defined PYTHON_PATH for /d %%p in ("C:\Program Files\Python3*") do if exist "%%p\python.exe" set "PYTHON_PATH=%%p\python.exe"
        if not defined PYTHON_PATH for /d %%p in ("C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python3*") do if exist "%%p\python.exe" set "PYTHON_PATH=%%p\python.exe"
        
        if defined PYTHON_PATH (
            call :log [*] 找到Python: !PYTHON_PATH!
            for %%P in ("!PYTHON_PATH!") do set "PYTHON_DIR=%%~dpP"
            set "PATH=!PATH!;!PYTHON_DIR!"
            set "PYTHON_CMD=!PYTHON_PATH!"
        ) else (
            call :log [WARNING] 系统中未找到Python，正在自动安装...
            
            where winget >nul 2>&1
            if not errorlevel 1 (
                call :log     使用 Winget 安装 Python...
                winget install Python.Python.3 --accept-package-agreements --accept-source-agreements --silent
                if not errorlevel 1 (
                    goto :python_verify_install
                )
                call :log [ERROR] Winget 安装失败
            )
            
            where choco >nul 2>&1
            if not errorlevel 1 (
                call :log     使用 Chocolatey 安装 Python...
                choco install python -y
                if not errorlevel 1 (
                    goto :python_verify_install
                )
                call :log [ERROR] Chocolatey 安装失败
            )
            
            where scoop >nul 2>&1
            if not errorlevel 1 (
                call :log     使用 Scoop 安装 Python...
                scoop install python
                if not errorlevel 1 (
                    goto :python_verify_install
                )
                call :log [ERROR] Scoop 安装失败
            )
            
            call :log     正在查询最新 Python 版本...
            set "PYTHON_LATEST_VERSION=3.11.9"
            for /f "delims=" %%v in ('curl.exe -s https://www.python.org/ftp/python/ 2^>nul ^| findstr /r "^3\.[0-9]*\.[0-9]*/$" ^| sort /r ^| findstr /n "^" ^| findstr "^[1]:"') do (
                for /f "tokens=1 delims=/" %%a in ("%%v") do set "PYTHON_LATEST_VERSION=%%a"
            )
            call :log     检测到最新Python版本: !PYTHON_LATEST_VERSION!

            call :log     直接下载 Python !PYTHON_LATEST_VERSION! 安装程序...
            if not exist "%TEMP%\python_installer.exe" (
                curl.exe -L -o "%TEMP%\python_installer.exe" https://www.python.org/ftp/python/!PYTHON_LATEST_VERSION!/python-!PYTHON_LATEST_VERSION!-amd64.exe
            )
            
            if exist "%TEMP%\python_installer.exe" (
                call :log     正在静默安装 Python 到 %CD%\_python...
                "%TEMP%\python_installer.exe" /quiet InstallAllUsers=0 PrependPath=0 Include_pip=1 TargetDir="%CD%\_python"
                if exist "%CD%\_python\python.exe" (
                    set "PYTHON_CMD=%CD%\_python\python.exe"
                    set "PATH=%CD%\_python;!PATH!"
                    call :log [*] Python 已安装到临时目录: %CD%\_python
                    del "%TEMP%\python_installer.exe" 2>nul
                ) else (
                    call :log [ERROR] Python 安装失败
                    exit /b 1
                )
            ) else (
                call :log [ERROR] Python 下载失败
                exit /b 1
            )
        )
    ) else (
        set "PYTHON_CMD=python"
    )
) else (
    set "PYTHON_CMD=py"
)

:python_verify_install
if not defined PYTHON_CMD (
    where py >nul 2>&1 && set "PYTHON_CMD=py"
    if not defined PYTHON_CMD where python >nul 2>&1 && set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    call :log [ERROR] 无法找到或安装Python
    exit /b 1
)

call :log_blank
call :log Python版本：
"!PYTHON_CMD!" --version

call :log [*] 检测虚拟环境状态...
if defined VIRTUAL_ENV (
    call :log 当前已在虚拟环境中: %VIRTUAL_ENV%
    set "IN_VENV=1"
) else (
    call :log 未在虚拟环境中
    set "IN_VENV=0"
)
exit /b 0

:detect_node_env
call :log [2/6] 检测Node.js环境...

where node >nul 2>&1
if errorlevel 1 (
    call :log Node.js未在PATH中，正在尝试查找或自动安装...
    
    where nvm >nul 2>&1
    if not errorlevel 1 (
        call :log     使用NVM管理Node.js...
        nvm list
        nvm use latest >nul 2>&1 || nvm use lts >nul 2>&1
        if errorlevel 1 (
            call :log     NVM中未安装Node.js，正在安装LTS版本...
            nvm install lts
            nvm use lts
        )
        goto :node_verify_install
    )
    
    if exist "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" (
        call :log     发现NVM（注册表路径），正在使用NVM管理Node.js...
        call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" use latest
        if errorlevel 1 (
            call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" install lts
            call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" use lts
        )
        goto :node_verify_install
    )
    
    call :log [WARNING] 未发现Node.js和NVM，正在全自动安装...
    
    where winget >nul 2>&1
    if not errorlevel 1 (
        call :log     使用 Winget 安装 Node.js...
        winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements --silent
        if not errorlevel 1 (
            goto :node_verify_install
        )
    )
    
    where choco >nul 2>&1
    if not errorlevel 1 (
        call :log     使用 Chocolatey 安装 Node.js...
        choco install nodejs -y
        if not errorlevel 1 (
            goto :node_verify_install
        )
    )
    
    where scoop >nul 2>&1
    if not errorlevel 1 (
        call :log     使用 Scoop 安装 Node.js...
        scoop install nodejs-lts
        if not errorlevel 1 (
            goto :node_verify_install
        )
    )
    
    call :log     正在查询最新 Node.js LTS 版本...
    set "NODE_LTS_VERSION=v20.11.1"
    for /f "delims=" %%v in ('curl.exe -s https://nodejs.org/dist/index.tab 2^>nul ^| findstr /i "LTS" ^| findstr /v "headers" ^| findstr /v "src" ^| findstr /r "^[v]?[0-9]" ^| sort /r ^| findstr /n "^" ^| findstr "^[1]:"') do (
        for /f "tokens=1 delims= " %%a in ("%%v") do set "NODE_LTS_VERSION=%%a"
    )
    call :log     检测到最新Node.js LTS版本: !NODE_LTS_VERSION!

    call :log     直接下载 Node.js !NODE_LTS_VERSION! 安装程序到 %NODE_ENV_PATH%...
    if not exist "%NODE_ENV_PATH%" mkdir "%NODE_ENV_PATH%"

    curl.exe -L -o "%NODE_ENV_PATH%\node-installer.msi" https://nodejs.org/dist/!NODE_LTS_VERSION!/node-!NODE_LTS_VERSION!-x64.msi
    
    if exist "%NODE_ENV_PATH%\node-installer.msi" (
        call :log     正在静默安装 Node.js 到 %CD%\%NODE_ENV_PATH%...
        msiexec /i "%NODE_ENV_PATH%\node-installer.msi" INSTALLDIR="%CD%\%NODE_ENV_PATH%" /quiet /norestart
        set "PATH=%CD%\%NODE_ENV_PATH%;!PATH!"
        del "%NODE_ENV_PATH%\node-installer.msi" 2>nul
        call :log [*] Node.js 已安装到临时目录: %CD%\%NODE_ENV_PATH%
    ) else (
        call :log [ERROR] Node.js 下载失败
    )
) else (
    call :log Node.js版本:
    node --version
    npm --version
)

:node_verify_install
where node >nul 2>&1
if not errorlevel 1 (
    call :log_blank
    call :log Node.js版本:
    node --version
    npm --version
) else (
    call :log [WARNING] Node.js 安装失败，部分功能可能不可用
)
exit /b 0

:test_pip_mirrors
call :log [3/6] 测试PIP加速镜像源...

if not defined PYTHON_CMD (
    call :log [WARNING] Python未安装，跳过PIP镜像测试
    set "FASTEST_PIP_MIRROR=https://pypi.org/simple/"
    exit /b 0
)

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
        call :log     测试 !MIRROR_NAME!...
        
        set "TEST_TIME=9999"
        curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 1.5 --max-time 2 "!MIRROR_URL!" > temp_pip_time.txt 2>nul
        if exist temp_pip_time.txt (
            set /p TEST_TIME=<temp_pip_time.txt
            del temp_pip_time.txt 2>nul
        )
        
        if not defined TEST_TIME set "TEST_TIME=9999"
        
        set "PIP_INT_TIME=9999"
        if not "!TEST_TIME!"=="0" if not "!TEST_TIME!"=="0.000000" (
            "!PYTHON_CMD!" -c "print(int(float('!TEST_TIME!')*1000))" > temp_pip_int.txt 2>nul
            if exist temp_pip_int.txt (
                set /p PIP_INT_TIME=<temp_pip_int.txt
                del temp_pip_int.txt 2>nul
            )
        )
        if "!PIP_INT_TIME!"=="" set "PIP_INT_TIME=9999"
        if "!PIP_INT_TIME!"=="0" set "PIP_INT_TIME=9999"
        
        if !PIP_INT_TIME! equ 9999 (
            call :log         !MIRROR_NAME!: 超时/失败
        ) else (
            call :log         !MIRROR_NAME!: !TEST_TIME!秒 ^(!PIP_INT_TIME!ms^)
            if !PIP_INT_TIME! LSS !MIN_TIME! (
                set "MIN_TIME=!PIP_INT_TIME!"
                set "BEST_MIRROR=!MIRROR_URL!"
                set "BEST_NAME=!MIRROR_NAME!"
            )
        )
    )
)

if exist temp_pip_time.txt del temp_pip_time.txt 2>nul
if exist temp_pip_int.txt del temp_pip_int.txt 2>nul

if "!BEST_MIRROR!"=="" (
    call :log [WARNING] 所有镜像测试失败，使用默认PyPI源
    set "FASTEST_PIP_MIRROR=https://pypi.org/simple/"
) else (
    set "FASTEST_PIP_MIRROR=!BEST_MIRROR!"
    call :log_blank
    call :log [*] 最快PIP镜像: !BEST_NAME! ^(!MIN_TIME!毫秒^)
)
exit /b 0

:test_npm_mirrors
call :log [4/6] 测试NPM加速镜像源...

where npm >nul 2>&1
if errorlevel 1 (
    call :log [WARNING] npm未安装，跳过NPM镜像测试
    exit /b 0
)

set "NPM_MIRRORS[0]=https://registry.npmmirror.com|npmmirror淘宝"
set "NPM_MIRRORS[1]=https://registry.npmjs.org|官方源"

set "NPM_MIN_TIME=9999"
set "NPM_BEST_MIRROR="
set "NPM_BEST_NAME="

for /L %%i in (0,1,1) do (
    for /f "tokens=1,2 delims=|" %%a in ("!NPM_MIRRORS[%%i]!") do (
        set "NPM_URL=%%a"
        set "NPM_NAME=%%b"
        call :log     测试 !NPM_NAME!...
        
        set "NPM_TEST_TIME=9999"
        curl.exe -s -o NUL -w "%%{time_total}" --connect-timeout 3 "!NPM_URL!" > temp_npm_time.txt 2>nul
        if exist temp_npm_time.txt (
            set /p NPM_TEST_TIME=<temp_npm_time.txt
            del temp_npm_time.txt 2>nul
        )
        
        if not defined NPM_TEST_TIME set "NPM_TEST_TIME=9999"
        
        set "NPM_INT_TIME=9999"
        if not "!NPM_TEST_TIME!"=="0" if not "!NPM_TEST_TIME!"=="0.000000" (
            "!PYTHON_CMD!" -c "print(int(float('!NPM_TEST_TIME!')*1000))" > temp_npm_int.txt 2>nul
            if exist temp_npm_int.txt (
                set /p NPM_INT_TIME=<temp_npm_int.txt
                del temp_npm_int.txt 2>nul
            )
        )
        if "!NPM_INT_TIME!"=="" set "NPM_INT_TIME=9999"
        if "!NPM_INT_TIME!"=="0" set "NPM_INT_TIME=9999"
        
        if !NPM_INT_TIME! equ 9999 (
            call :log         !NPM_NAME!: 超时/失败
        ) else (
            call :log         !NPM_NAME!: !NPM_TEST_TIME!秒 ^(!NPM_INT_TIME!ms^)
            if !NPM_INT_TIME! LSS !NPM_MIN_TIME! (
                set "NPM_MIN_TIME=!NPM_INT_TIME!"
                set "NPM_BEST_MIRROR=!NPM_URL!"
                set "NPM_BEST_NAME=!NPM_NAME!"
            )
        )
    )
)

if exist temp_npm_time.txt del temp_npm_time.txt 2>nul
if exist temp_npm_int.txt del temp_npm_int.txt 2>nul

if "!NPM_BEST_MIRROR!"=="" (
    call :log [WARNING] NPM镜像测试失败
) else (
    set "FASTEST_NPM_MIRROR=!NPM_BEST_MIRROR!"
    call :log_blank
    call :log [*] 最快NPM镜像: !NPM_BEST_NAME! ^(!NPM_MIN_TIME!毫秒^)
    
    where npm >nul 2>&1
    if not errorlevel 1 (
        npm config set registry "!NPM_BEST_MIRROR!"
        call :log [*] NPM镜像已设置为: !NPM_BEST_MIRROR!
    )
)
exit /b 0

:detect_venv
call :log [5/6] 检测Python虚拟环境...

if exist venv\Scripts\activate.bat (
    call :log 检测到虚拟环境：venv
    set "VENV_EXISTS=1"
    set "VENV_PATH=venv"
) else if exist .venv\Scripts\activate.bat (
    call :log 检测到虚拟环境：.venv
    set "VENV_EXISTS=1"
    set "VENV_PATH=.venv"
) else (
    call :log 未检测到虚拟环境
    set "VENV_EXISTS=0"
)
goto setup_venv

:setup_venv
call :log [6/6] 设置Python虚拟环境并安装依赖...

if "!VENV_EXISTS!"=="0" (
    call :log 正在创建虚拟环境到 !VENV_PATH!...
    "!PYTHON_CMD!" -m venv "!VENV_PATH!"
    if errorlevel 1 (
        call :log ERROR: 创建虚拟环境失败
        pause
        exit /b 1
    )
    set "VENV_EXISTS=1"
)

if not exist "!VENV_PATH!\Scripts\activate.bat" (
    call :log ERROR: 虚拟环境路径不存在：!VENV_PATH!
    pause
    exit /b 1
)

call "!VENV_PATH!\Scripts\activate.bat"

if defined FASTEST_PIP_MIRROR (
    call :log [*] 配置PIP镜像源为: !FASTEST_PIP_MIRROR!
    
    if not exist "!VENV_PATH!\pip_config" mkdir "!VENV_PATH!\pip_config"
    
    set "TRUSTED_HOST=!FASTEST_PIP_MIRROR!"
    set "TRUSTED_HOST=!TRUSTED_HOST:https://=!"
    set "TRUSTED_HOST=!TRUSTED_HOST:http://=!"
    for /f "delims=/" %%h in ("!TRUSTED_HOST!") do set "TRUSTED_HOST=%%h"
    
    echo:[global]> "!VENV_PATH!\pip_config\pip.ini"
    echo:index-url=!FASTEST_PIP_MIRROR!>> "!VENV_PATH!\pip_config\pip.ini"
    echo:trusted-host=!TRUSTED_HOST!>> "!VENV_PATH!\pip_config\pip.ini"
    echo:[install]>> "!VENV_PATH!\pip_config\pip.ini"
    echo:trusted-host=!TRUSTED_HOST!>> "!VENV_PATH!\pip_config\pip.ini"
    
    set "PIP_CONFIG_FILE=!VENV_PATH!\pip_config\pip.ini"
)

if exist requirements.txt (
    call :log 正在安装Python依赖...
    set "PIP_INSTALL_OK=0"
    if defined FASTEST_PIP_MIRROR (
        "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt --disable-pip-version-check -i "!FASTEST_PIP_MIRROR!"
        if errorlevel 1 (
            call :log WARNING: 使用镜像源安装失败，尝试默认源...
            "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt --disable-pip-version-check
            if errorlevel 1 set "PIP_INSTALL_OK=1"
        )
    ) else (
        "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt --disable-pip-version-check
        if errorlevel 1 set "PIP_INSTALL_OK=1"
    )

    if "!PIP_INSTALL_OK!"=="1" (
        call :log ERROR: 依赖安装完全失败
        pause
        exit /b 1
    )

    call :log [*] 安装Playwright浏览器...
    "!VENV_PATH!\Scripts\python.exe" main.py --install-playwright
)

call :log Python虚拟环境设置完成
goto check_config

:check_config
call :log [*] 检测配置文件...

if not exist config mkdir config

if exist config\config.json (
    call :log 配置文件存在
    goto run_web
) else (
    call :log 配置文件不存在，开始首次配置向导
    goto auto_setup
)

:auto_setup
call :log [*] 自动配置...

call :log_blank
call :log 正在复制配置文件模板...

if exist config\config.json.example (
    copy /Y config\config.json.example config\config.json >nul
    call :log [OK] config.json 已创建
) else (
    call :log [WARNING] config.json.example 不存在
)

if exist config\cookies.json.example (
    copy /Y config\cookies.json.example config\cookies.json >nul
    call :log [OK] cookies.json 已创建
)

call :log_blank
call :log ========================================
call :log 首次配置完成！
call :log ========================================
call :log_blank
call :log 请编辑 config\config.json，填写以下信息：
call :log   - login.username: 用户名
call :log   - login.password: 密码
call :log   - target_url: 目标URL
call :log   - headers.cookie: Cookie值
call :log   - cookies中的token和sensorsdata值
call :log_blank
set /p CHOICE="按回车键继续，或输入 Q 退出: "

if /i "!CHOICE!"=="Q" goto cleanup_exit

:run_web
call :log_blank
call :log ========================================
call :log 隧道服务配置
call :log ========================================
call :log_blank
call :log 正在配置 hostc 隧道服务...
call :log [*] 预启动隧道服务(加快首次启动速度)...
call npx -y hostc@latest --help >nul 2>&1
call :log 隧道服务就绪

call :log_blank
call :log ========================================
call :log 启动Web服务和隧道...
call :log ========================================

call "!VENV_PATH!\Scripts\activate.bat"

call :log_blank
call :log 正在启动 Web 服务...
call :log_blank

if not defined WEB_PORT set "WEB_PORT=8888"
call :log [!date! !time!] === Web服务启动 ===
start /b cmd /c "call "!VENV_PATH!\Scripts\activate.bat" && python main.py --web --port !WEB_PORT! >> "!LOG_FILE!" 2>&1"

call :log 等待 Web 服务启动完成...
timeout /t 5 /nobreak >nul

set "FLASK_WAIT_COUNT=0"
set "FLASK_MAX_WAIT=60"

:wait_flask
set /a FLASK_WAIT_COUNT+=1
if !FLASK_WAIT_COUNT! gtr !FLASK_MAX_WAIT! (
    call :log [ERROR] Web服务启动超时（等待了!FLASK_MAX_WAIT!次），请检查日志: !LOG_FILE!
    goto :wait_loop_entry
)
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s -o NUL -w "%%{http_code}" http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
if not defined HTTP_CODE set "HTTP_CODE=000"
if not "!HTTP_CODE!"=="200" (
    if not "!HTTP_CODE!"=="302" (
        timeout /t 2 /nobreak >nul
        goto wait_flask
    )
)

call :log Web 服务已就绪，正在启动隧道...
start /b cmd /c "npx -y hostc@latest !WEB_PORT! --local-host localhost > file\tunnel_url.txt 2>&1"

call :log_blank
call :log ========================================
call :log 启动完成！
call :log ========================================
call :log_blank
call :log 本地访问: http://localhost:!WEB_PORT!
call :log 公网访问: 查看 file\tunnel_url.txt
call :log Web日志: 查看 file\web_output.log
call :log_blank
call :log 按 Ctrl+C 停止服务，或关闭此窗口
call :log_blank

:wait_loop_entry
set "CHECK_INTERVAL=60"
set "CHECK_COUNTER=0"

:wait_loop
timeout /t 1 /nobreak >nul
set /a CHECK_COUNTER+=1
if !CHECK_COUNTER! geq !CHECK_INTERVAL! (
    set "CHECK_COUNTER=0"
    call :check_temp_size
)
goto wait_loop

:check_temp_size
if exist temp (
    call :get_dir_size temp
    set "LIMIT_SIZE=3145728"
    if !TOTAL_SIZE! gtr !LIMIT_SIZE! (
        del /f /s /q temp\*.* >nul 2>&1
        call :log [AUTO] temp目录超过3MB，已自动清理
    )
)
goto :eof