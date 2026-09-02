@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

call :check_admin_rights
if errorlevel 1 (
    echo [ERROR] 请右键"以管理员身份运行"此脚本
    pause
    exit /b 1
)

call :check_prerequisites
if errorlevel 1 (
    pause
    exit /b 1
)

set "VERSION=0.0.0"
if exist "README.md" (
    for /f "delims=" %%L in ('type README.md ^| findstr /c:"### v5." ^| findstr /c:"(2026-"') do (
        for /f "tokens=2 delims=v " %%v in ("%%L") do (
            if "!VERSION!"=="0.0.0" set "VERSION=%%v"
        )
    )
    if "!VERSION!"=="0.0.0" (
        for /f "delims=" %%L in ('type README.md ^| findstr /c:"### v4." ^| findstr /c:"(2026-"') do (
            for /f "tokens=2 delims=v " %%v in ("%%L") do (
                if "!VERSION!"=="0.0.0" set "VERSION=%%v"
            )
        )
    )
    if "!VERSION!"=="0.0.0" (
        for /f "tokens=3 delims=: " %%v in ('findstr /i "version:" README.md 2^>nul ^| findstr /r "[0-9]\.[0-9]\.[0-9]"') do (
            if "!VERSION!"=="0.0.0" set "VERSION=%%v"
        )
    )
)

if not defined WEB_PORT set "WEB_PORT=8888"

if not exist file mkdir file
set "LOG_FILE=%CD%\file\web_output.log"

goto main_start

:check_admin_rights
net session >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 需要管理员权限
    exit /b 1
)
exit /b 0

:check_prerequisites
echo [*] 检查前置条件...

where curl >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 未找到 curl.exe，需要 Windows 10 1803+ 或 Windows 11
    exit /b 1
)

where powershell >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 未找到 PowerShell
    exit /b 1
)

echo [*] 前置条件检查通过
exit /b 0

:ms_timestamp
set "TIMESTAMP="
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set "datetime=%%I"
if defined datetime set "TIMESTAMP=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%:%datetime:~12,2%.%datetime:~15,3%"
if not defined TIMESTAMP set "TIMESTAMP=%date% %time: =0%"
exit /b

:log
call :ms_timestamp
echo [%TIMESTAMP%] %*
if not "%LOG_FILE%"=="" (
    if exist "!LOG_FILE!" (
        >> "!LOG_FILE!" echo [%TIMESTAMP%] %* 2>nul
    )
)
exit /b

:log_blank
echo.
if not "%LOG_FILE%"=="" (
    if exist "!LOG_FILE!" (
        >> "!LOG_FILE!" echo. 2>nul
    )
)
exit /b

:log_console_only
call :ms_timestamp
echo [%TIMESTAMP%] %*
exit /b

:log_blank_console_only
echo.
exit /b

:main_start
echo. > "%CD%\file\web_output.log" 2>nul

call :log ========================================
call :log Szwego商品爬虫和货号对比工具 - v%VERSION%
call :log ========================================

call :log_blank
call :log [*] 清理残留进程...
call :kill_process_safe python.exe main.py
call :kill_process_safe hostc.exe
ping -n 2 127.0.0.1 >nul 2>&1

call :wait_for_port !WEB_PORT! 10
call :log [*] 残留进程清理完成

call :log_blank
call :log [*] 检查 hostc 隧道工具...
set "HOSTC_BIN=%CD%\dist\node_modules\.bin\hostc.cmd"
if not exist "!HOSTC_BIN!" (
    call :log [*] 本地未找到 hostc，开始安装...
    call :install_hostc
)
if exist "!HOSTC_BIN!" (
    for /f "delims=" %%v in ('"!HOSTC_BIN!" --version 2^>nul') do set "HOSTC_VER=%%v"
    call :log [*] hostc v!HOSTC_VER! 已就绪
) else (
    call :log [WARNING] hostc 安装失败，隧道将不可用
)

call :log_blank
call :log [*] 启动 hostc 隧道（后台运行）...
if exist "!HOSTC_BIN!" (
    start /b cmd /c ""!HOSTC_BIN!" !WEB_PORT! --local-host localhost" < nul
    call :log [*] hostc 已在后台启动
)

call :log_blank
call :log [*] 清理临时文件...
call :cleanup_temp_dir temp 3145728
call :cleanup_temp_dir playwright-browsers 0

goto detect_environments

:kill_process_safe
set "PROC_NAME=%~1"
wmic process where "name='%PROC_NAME%'" get processid,commandline 2>nul | findstr /i "xy_ws" >nul 2>&1
if not errorlevel 1 (
    for /f "tokens=2 delims=," %%p in ('wmic process where "name=\'%PROC_NAME%\' and commandlike \'%%xy_ws%%\'" get processid /format:csv 2^>nul ^| findstr /r "[0-9]"') do (
        taskkill /F /PID %%p >nul 2>&1
        call :log     已终止进程 %%p (%PROC_NAME%)
    )
)
exit /b

:wait_for_port
set "WAIT_PORT=%~1"
set "MAX_WAIT=%~2"
set "WAIT_COUNT=0"

:port_wait_loop
if %WAIT_COUNT% geq %MAX_WAIT goto port_wait_done
netstat -ano | findstr ":%WAIT_PORT%.*LISTENING" >nul 2>&1
if errorlevel 1 goto port_wait_done
set /a WAIT_COUNT+=1
call :log [*] 端口%WAIT_PORT%仍被占用，等待释放... (%WAIT_COUNT%/%MAX_WAIT%)
ping -n 2 127.0.0.1 >nul 2>&1
goto port_wait_loop

:port_wait_done
if %WAIT_COUNT% geq %MAX_WAIT% (
    call :log [WARNING] 端口%WAIT_PORT%等待超时，强制清理...
    for /f "tokens=6" %%p in ('netstat -ano ^| findstr ":%WAIT_PORT%.*LISTENING"') do taskkill /F /PID %%p >nul 2>&1
    ping -n 2 127.0.0.1 >nul 2>&1
)
exit /b

:cleanup_temp_dir
set "DIR_NAME=%~1"
set "MAX_SIZE=%~2"
if exist "%DIR_NAME%" (
    for /f "delims=" %%a in ('powershell -NoProfile -Command "(Get-ChildItem -Path \'%DIR_NAME%\' -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum" 2^>nul') do set "DIR_SIZE=%%a"
    if defined DIR_SIZE if !DIR_SIZE! gtr %MAX_SIZE% (
        del /f /s /q "%DIR_NAME%\*.*" >nul 2>&1
        call :log [*] %DIR_NAME%目录超过限制，已清理
    ) else (
        call :log [*] %DIR_NAME%目录未超过限制，跳过清理
    )
) else (
    call :log [*] %DIR_NAME%目录不存在，跳过
)
exit /b

:get_dir_size
set "TOTAL_SIZE=0"
for /f "delims=" %%a in ('powershell -NoProfile -Command "(Get-ChildItem -Path \'%~1\' -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum" 2^>nul') do set "TOTAL_SIZE=%%a"
if not defined TOTAL_SIZE set "TOTAL_SIZE=0"
if "!TOTAL_SIZE!"=="" set "TOTAL_SIZE=0"
goto :eof

:detect_environments
call :log_blank
call :log ========================================
call :log 综合环境检测与配置
call :log ========================================

set "VENV_PATH=.venv"
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

set "PYTHON_CMD="
where py >nul 2>&1 && set "PYTHON_CMD=py"
if not defined PYTHON_CMD where python >nul 2>&1 && set "PYTHON_CMD=python"

if not defined PYTHON_CMD (
    call :log Python未在PATH中，正在尝试查找或自动安装...
    
    set "PYTHON_PATH="
    for /d %%p in ("C:\Python3*") do if exist "%%p\python.exe" set "PYTHON_PATH=%%p\python.exe"
    for /d %%p in ("C:\Program Files\Python3*") do if exist "%%p\python.exe" set "PYTHON_PATH=%%p\python.exe"
    for /d %%p in ("%LOCALAPPDATA%\Programs\Python\Python3*") do if exist "%%p\python.exe" set "PYTHON_PATH=%%p\python.exe"
    
    if defined PYTHON_PATH (
        call :log [*] 找到Python: !PYTHON_PATH!
        for %%P in ("!PYTHON_PATH!") do set "PATH=!PATH!;%%~dpP"
        set "PYTHON_CMD=!PYTHON_PATH!"
    ) else (
        call :log [*] 正在自动安装Python...
        call :auto_install_python
        if errorlevel 1 exit /b 1
    )
)

call :log_blank
call :log Python版本：
if defined PYTHON_CMD (
    if exist "!PYTHON_CMD!" (
        for /f "delims=" %%v in ('"!PYTHON_CMD!" --version 2^>nul') do call :log     %%v
    ) else (
        where !PYTHON_CMD! >nul 2>&1
        if not errorlevel 1 (
            for /f "delims=" %%v in ('!PYTHON_CMD! --version 2^>nul') do call :log     %%v
        ) else (
            call :log [WARNING] Python路径不存在: !PYTHON_CMD!
        )
    )
) else (
    call :log [ERROR] 未找到Python解释器
)

call :log [*] 检测虚拟环境状态...
if defined VIRTUAL_ENV (
    call :log 当前已在虚拟环境中: %VIRTUAL_ENV%
    set "IN_VENV=1"
) else (
    call :log 未在虚拟环境中
    set "IN_VENV=0"
)
exit /b 0

:auto_install_python
call :log     尝试使用 Winget 安装...
where winget >nul 2>&1
if not errorlevel 1 (
    winget install Python.Python.3 --accept-package-agreements --accept-source-agreements --silent
    if not errorlevel 1 (
        where py >nul 2>&1 && set "PYTHON_CMD=py"
        where python >nul 2>&1 && set "PYTHON_CMD=python"
        if defined PYTHON_CMD (
            call :log [*] Python 安装成功
            exit /b 0
        )
    )
)

call :log     尝试使用 Chocolatey 安装...
where choco >nul 2>&1
if not errorlevel 1 (
    choco install python -y
    if not errorlevel 1 (
        set "PYTHON_CMD=python"
        call :log [*] Python 安装成功
        exit /b 0
    )
)

call :log     直接下载并安装Python...
set "PYTHON_VERSION=3.11.9"
if not exist "%TEMP%\python_installer.exe" (
    curl.exe -L -o "%TEMP%\python_installer.exe" https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
)

if exist "%TEMP%\python_installer.exe" (
    if not exist "%CD%\_python" mkdir "%CD%\_python"
    "%TEMP%\python_installer.exe" /quiet InstallAllUsers=0 PrependPath=0 Include_pip=1 TargetDir="%CD%\_python"
    if exist "%CD%\_python\python.exe" (
        set "PYTHON_CMD=%CD%\_python\python.exe"
        set "PATH=%CD%\_python;!PATH!"
        call :log [*] Python 已安装到本地目录: %CD%\_python
        del "%TEMP%\python_installer.exe" 2>nul
        exit /b 0
    )
)

call :log [ERROR] Python 自动安装失败
exit /b 1

:detect_node_env
call :log [2/6] 检测Node.js环境...

where node >nul 2>&1
if errorlevel 1 (
    call :log Node.js未在PATH中，正在尝试查找或自动安装...
    
    where nvm >nul 2>&1
    if not errorlevel 1 (
        call :log     使用NVM管理Node.js...
        nvm use lts >nul 2>&1 || nvm install lts
        nvm use lts
        goto :node_verify_install
    )
    
    call :log [*] 正在自动安装Node.js...
    call :auto_install_node
)

:node_verify_install
where node >nul 2>&1
if not errorlevel 1 (
    call :log_blank
    call :log Node.js版本:
    for /f "delims=" %%v in ('node --version 2^>nul') do call :log     Node %%v
    for /f "delims=" %%v in ('npm --version 2^>nul') do call :log     NPM %%v
) else (
    call :log [WARNING] Node.js 安装失败，部分功能可能不可用
)
exit /b 0

:auto_install_node
where winget >nul 2>&1
if not errorlevel 1 (
    winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements --silent
    if not errorlevel 1 goto :node_verify_install
)

where choco >nul 2>&1
if not errorlevel 1 (
    choco install nodejs -y
    if not errorlevel 1 goto :node_verify_install
)

set "NODE_VERSION=v20.11.1"
if not exist "%TEMP%\node-installer.msi" (
    curl.exe -L -o "%TEMP%\node-installer.msi" https://nodejs.org/dist/%NODE_VERSION%/node-%NODE_VERSION%-x64.msi
)

if exist "%TEMP%\node-installer.msi" (
    msiexec /i "%TEMP%\node-installer.msi" /quiet /norestart
    del "%TEMP%\node-installer.msi" 2>nul
    call :log [*] Node.js 已安装
)
exit /b 0

:test_pip_mirrors
call :log [3/6] 测试PIP加速镜像源...

if not defined PYTHON_CMD (
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
        
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 1.5 --max-time 2 "!MIRROR_URL!" 2^>nul') do set "TEST_TIME=%%t"
        
        if defined TEST_TIME if not "!TEST_TIME!"=="0" if not "!TEST_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!TEST_TIME!\'*1000)" 2^>nul') do set "PIP_INT_TIME=%%m"
            
            if defined PIP_INT_TIME if !PIP_INT_TIME! LSS !MIN_TIME! (
                set "MIN_TIME=!PIP_INT_TIME!"
                set "BEST_MIRROR=!MIRROR_URL!"
                set "BEST_NAME=!MIRROR_NAME!"
                call :log         !MIRROR_NAME!: !TEST_TIME!秒 [!PIP_INT_TIME!ms]
            )
        ) else (
            call :log         !MIRROR_NAME!: 超时/失败
        )
    )
)

if "!BEST_MIRROR!"=="" (
    call :log [WARNING] 所有镜像测试失败，使用默认PyPI源
    set "FASTEST_PIP_MIRROR=https://pypi.org/simple/"
) else (
    set "FASTEST_PIP_MIRROR=!BEST_MIRROR!"
    call :log_blank
    call :log [*] 最快PIP镜像: !BEST_NAME! [!MIN_TIME!毫秒]
)
exit /b 0

:install_hostc
call :log [*] CDN轮询安装 hostc...

set "HOSTC_MIRRORS[0]=https://registry.npmmirror.com|npmmirror淘宝"
set "HOSTC_MIRRORS[1]=https://repo.huaweicloud.com/repository/npm/|华为云"
set "HOSTC_MIRRORS[2]=https://registry.npmjs.org|官方源"

set "HOSTC_BEST_MIRROR=https://registry.npmmirror.com"

for /L %%i in (0,1,2) do (
    for /f "tokens=1,2 delims=|" %%a in ("!HOSTC_MIRRORS[%%i]!") do (
        set "H_URL=%%a"
        set "H_NAME=%%b"
        
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_total}" --connect-timeout 3 "!H_URL!" 2^>nul') do set "H_TIME=%%t"
        
        if defined H_TIME if not "!H_TIME!"=="0" if not "!H_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!H_TIME!\'*1000)" 2^>nul') do set "H_INT=%%m"
            
            if defined H_INT if !H_INT! LSS 9999 (
                set "HOSTC_BEST_MIRROR=!H_URL!"
                call :log     测试 !H_NAME!: !H_TIME!秒 [!H_INT!ms]
            )
        )
    )
)

call :log [*] 使用最佳镜像安装 hostc...
npm install hostc@latest --registry "!HOSTC_BEST_MIRROR!" --prefix dist 2>nul
if errorlevel 1 (
    call :log [ERROR] hostc 安装失败
) else (
    call :log [*] hostc 安装成功
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
        
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_total}" --connect-timeout 3 "!NPM_URL!" 2^>nul') do set "NPM_TEST_TIME=%%t"
        
        if defined NPM_TEST_TIME if not "!NPM_TEST_TIME!"=="0" if not "!NPM_TEST_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!NPM_TEST_TIME!\'*1000)" 2^>nul') do set "NPM_INT_TIME=%%m"
            
            if defined NPM_INT_TIME if !NPM_INT_TIME! LSS !NPM_MIN_TIME! (
                set "NPM_MIN_TIME=!NPM_INT_TIME!"
                set "NPM_BEST_MIRROR=!NPM_URL!"
                set "NPM_BEST_NAME=!NPM_NAME!"
                call :log         !NPM_NAME!: !NPM_TEST_TIME!秒 [!NPM_INT_TIME!ms]
            )
        ) else (
            call :log         !NPM_NAME!: 超时/失败
        )
    )
)

if "!NPM_BEST_MIRROR!"=="" (
    call :log [WARNING] NPM镜像测试失败
) else (
    set "FASTEST_NPM_MIRROR=!NPM_BEST_MIRROR!"
    call :log_blank
    call :log [*] 最快NPM镜像: !NPM_BEST_NAME! [!NPM_MIN_TIME!毫秒]
    
    npm config set registry "!NPM_BEST_MIRROR!"
    call :log [*] NPM镜像已设置为: !NPM_BEST_MIRROR!
)
exit /b 0

:detect_venv
call :log [5/6] 检测Python虚拟环境...

if exist .venv\Scripts\activate.bat (
    call :log 检测到虚拟环境：.venv
    set "VENV_EXISTS=1"
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
    call :log [*] 检查Python依赖是否需要安装...
    set "NEED_PIP_INSTALL=1"
    "!VENV_PATH!\Scripts\python.exe" main.py --check-deps >nul 2>&1
    if not errorlevel 1 (
        call :log [*] 所有Python依赖已满足，跳过安装
        set "NEED_PIP_INSTALL=0"
    )

    if "!NEED_PIP_INSTALL!"=="1" (
        call :log [*] 强制升级pip到最新版本...
        if defined FASTEST_PIP_MIRROR (
            "!VENV_PATH!\Scripts\python.exe" -m pip install --upgrade pip -i "!FASTEST_PIP_MIRROR!"
        ) else (
            "!VENV_PATH!\Scripts\python.exe" -m pip install --upgrade pip
        )
        
        call :log [*] 安装依赖...
        if defined FASTEST_PIP_MIRROR (
            "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt -i "!FASTEST_PIP_MIRROR!"
            if errorlevel 1 (
                call :log WARNING: 使用镜像源安装失败，尝试默认源...
                "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt
            )
        ) else (
            "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt
        )
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
call :log 请编辑 config\config.json 后按回车继续
pause
goto run_web

:run_web
call :log_blank
call :log ========================================
call :log 启动Web服务和隧道...
call :log ========================================

call "!VENV_PATH!\Scripts\activate.bat"

call :log_blank
call :log [*] Checking BOM...
"%VENV_PATH%\Scripts\python.exe" main.py --check-bom >NUL 2>&1
if errorlevel 1 (
    call :log [WARNING] BOM detected, auto-fixing...
    "%VENV_PATH%\Scripts\python.exe" main.py --fix-bom
)
call :log [OK] BOM check completed
call :log Starting Web service...
call :log_blank

if not defined WEB_PORT set "WEB_PORT=8888"
for /f "delims=0123456789" %%c in ("!WEB_PORT!") do set "WEB_PORT=8888"
if !WEB_PORT! lss 1 set "WEB_PORT=8888"
if !WEB_PORT! gtr 65535 set "WEB_PORT=8888"

call :ms_timestamp
call :log [!TIMESTAMP!] === Web服务启动 ===
start /b cmd /c "call "!VENV_PATH!\Scripts\activate.bat" && python main.py --web --port !WEB_PORT!" < nul

call :log 等待 Web 服务启动完成...
ping -n 2 127.0.0.1 >nul 2>&1

set "FLASK_WAIT_COUNT=0"
set "FLASK_MAX_WAIT=60"

:wait_flask
set /a FLASK_WAIT_COUNT+=1
if !FLASK_WAIT_COUNT! gtr !FLASK_MAX_WAIT! (
    call :log [ERROR] Web服务启动超时
    goto :wait_loop_entry
)
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s -o NUL -w "%%{http_code}" http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
if not defined HTTP_CODE set "HTTP_CODE=000"
if not "!HTTP_CODE!"=="200" if not "!HTTP_CODE!"=="302" (
    ping -n 1 127.0.0.1 >nul 2>&1
    goto wait_flask
)

call :log_console_only Web 服务已就绪

ping -n 4 127.0.0.1 >nul 2>&1

set "LAN_ADDR="
set "PUBLIC_URL="

for /f "delims=" %%l in ('findstr /C:"局域网地址:" "!LOG_FILE!" 2^>nul') do (
    for /f "tokens=2 delims=: " %%a in ("%%l") do set "LAN_ADDR=%%a"
)

if not defined LAN_ADDR (
    for /f "delims=" %%i in ('powershell -NoProfile -Command "Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notmatch \'^(169\.254|127\.)\' } | Select-Object -First 1 -ExpandProperty IPAddress" 2^>nul') do (
        set "LAN_ADDR=http://%%i:!WEB_PORT!"
    )
)

if not defined LAN_ADDR (
    for /f "tokens=14 delims= " %%i in ('ipconfig ^| findstr /i "IPv4" 2^>nul') do (
        if not "%%i"=="127.0.0.1" (
            set "LAN_ADDR=http://%%i:!WEB_PORT!"
        )
    )
)

call :log_blank_console_only
call :log_console_only ========================================
call :log_console_only 启动完成！
call :log_console_only ========================================
call :log_blank_console_only
call :log_console_only 本地访问: http://localhost:!WEB_PORT!
if defined LAN_ADDR (
    call :log_console_only 局域网地址: !LAN_ADDR!
) else (
    call :log_console_only 局域网地址: 检测中...
)
call :log_console_only 详细日志: !LOG_FILE!
call :log_blank_console_only
call :log_console_only 按 Ctrl+C 停止服务
call :log_blank_console_only

:wait_loop_entry
set "CHECK_INTERVAL=60"
set "CHECK_COUNTER=0"

:wait_loop
ping -n 2 127.0.0.1 >nul 2>&1
set /a CHECK_COUNTER+=1
if !CHECK_COUNTER! geq !CHECK_INTERVAL! (
    set "CHECK_COUNTER=0"
    call :check_temp_size
)
goto wait_loop

:check_temp_size
call :get_dir_size temp
set "LIMIT_SIZE=3145728"
if !TOTAL_SIZE! gtr !LIMIT_SIZE! (
    del /f /s /q temp\*.* >nul 2>&1
    call :log_console_only [AUTO] temp目录超过3MB，已自动清理
)
goto :eof

:cleanup_exit
call :log_blank
call :log 正在清理进程...
call :kill_process_safe python.exe main.py
call :kill_process_safe hostc.exe
call :log 清理完成
goto :eof