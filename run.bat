@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

call :check_admin_rights
if errorlevel 1 (
    echo [*] 正在请求管理员权限...
    powershell -NoProfile -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs"
    exit /b 0
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

where winget >nul 2>&1
if errorlevel 1 (
    echo [*] 未找到 Winget，正在自动安装...
    call :auto_install_winget
    where winget >nul 2>&1
    if not errorlevel 1 echo [*] Winget 安装成功
)

where choco >nul 2>&1
if errorlevel 1 (
    echo [*] 未找到 Chocolatey，正在自动安装...
    call :auto_install_choco
    where choco >nul 2>&1
    if not errorlevel 1 echo [*] Chocolatey 安装成功
)

where git >nul 2>&1
if errorlevel 1 (
    echo [*] 未找到 Git，正在自动安装...
    call :auto_install_git
    where git >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Git 安装失败，请手动安装: https://git-scm.com/download/win
        exit /b 1
    )
    echo [*] Git 安装成功
)

echo [*] 前置条件检查通过
exit /b 0

:auto_install_winget
echo     轮询最快Winget安装源...
set "WG_MIRRORS[0]=https://mirrors.huaweicloud.com/microsoft/winget-cli/latest/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle|华为云"
set "WG_MIRRORS[1]=https://github.com/microsoft/winget-cli/releases/latest/download/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle|GitHub官方"
set "WG_BEST_URL="
set "WG_MIN_TIME=9999"
for /L %%i in (0,1,1) do (
    for /f "tokens=1,2 delims=|" %%a in ("!WG_MIRRORS[%%i]!") do (
        set "WG_URL=%%a"
        set "WG_NAME=%%b"
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!WG_URL!" 2^>nul') do set "WG_TIME=%%t"
        if defined WG_TIME if not "!WG_TIME!"=="0" if not "!WG_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!WG_TIME!\'*1000)" 2^>nul') do set "WG_INT=%%m"
            if defined WG_INT if !WG_INT! LSS !WG_MIN_TIME! (
                set "WG_MIN_TIME=!WG_INT!"
                set "WG_BEST_URL=!WG_URL!"
                echo         !WG_NAME!: !WG_TIME!s [!WG_INT!ms]
            )
        )
    )
)
if defined WG_BEST_URL (
    echo     使用最快镜像下载Winget...
    curl.exe -L -o "%TEMP%\winget-installer.msixbundle" "!WG_BEST_URL!" 2>nul
    if exist "%TEMP%\winget-installer.msixbundle" (
        powershell -NoProfile -Command "Add-AppxPackage -Path '%TEMP%\winget-installer.msixbundle'" 2>nul
        del "%TEMP%\winget-installer.msixbundle" 2>nul
    )
) else (
    echo     尝试通过Microsoft Store安装Winget...
    powershell -NoProfile -Command "Start-Process 'ms-windows-store://pdp/?ProductId=9NBLGGH4NNS2'" 2>nul
)
exit /b 0

:auto_install_choco
echo     轮询最快Chocolatey安装源...
set "CCO_MIRRORS[0]=https://mirrors.huaweicloud.com/chocolatey/install.ps1|华为云"
set "CCO_MIRRORS[1]=https://community.chocolatey.org/install.ps1|Chocolatey官方"
set "CCO_BEST_URL=https://community.chocolatey.org/install.ps1"
set "CCO_MIN_TIME=9999"
for /L %%i in (0,1,1) do (
    for /f "tokens=1,2 delims=|" %%a in ("!CCO_MIRRORS[%%i]!") do (
        set "CCO_URL=%%a"
        set "CCO_NAME=%%b"
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!CCO_URL!" 2^>nul') do set "CCO_TIME=%%t"
        if defined CCO_TIME if not "!CCO_TIME!"=="0" if not "!CCO_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!CCO_TIME!\'*1000)" 2^>nul') do set "CCO_INT=%%m"
            if defined CCO_INT if !CCO_INT! LSS !CCO_MIN_TIME! (
                set "CCO_MIN_TIME=!CCO_INT!"
                set "CCO_BEST_URL=!CCO_URL!"
                echo         !CCO_NAME!: !CCO_TIME!s [!CCO_INT!ms]
            )
        )
    )
)
echo     使用最快镜像安装Chocolatey...
powershell -NoProfile -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('!CCO_BEST_URL!'))" 2>nul

:: 刷新当前会话的PATH（关键修复）
call :refresh_path
exit /b 0

:refresh_path
echo     刷新环境变量...
set "PATH=%PATH%;C:\ProgramData\chocolatey\bin"

:: 等待choco命令可用（最多等待10秒）
for /L %%w in (1,1,10) do (
    where choco >nul 2>&1 && goto :choco_ready
    ping -n 1 127.0.0.1 >nul 2>&1
)

:choco_ready
if exist "C:\ProgramData\chocolatey\bin\choco.exe" (
    echo     Chocolatey 已就绪
) else (
    echo     [WARNING] Chocolatey 可能未完全安装，部分功能可能不可用
)
exit /b

:get_latest_git_version
for /f "delims=" %%v in ('curl.exe -s https://api.github.com/repos/git-for-windows/git/releases/latest 2^>nul ^| powershell -NoProfile -Command "$input | ConvertFrom-Json | Select-Object -ExpandProperty tag_name"') do set "GIT_LATEST_VERSION=%%v"
if not defined GIT_LATEST_VERSION set "GIT_LATEST_VERSION=2.47.1"
exit /b

:auto_install_git
call :get_latest_git_version
echo     检测到Git最新版本: %GIT_LATEST_VERSION%

where winget >nul 2>&1
if not errorlevel 1 (
    echo     使用 Winget 安装 Git...
    winget install Git.Git --accept-package-agreements --accept-source-agreements --silent >nul 2>&1
    if not errorlevel 1 exit /b 0
)

where choco >nul 2>&1
if not errorlevel 1 (
    echo     使用 Chocolatey 安装 Git...
    choco install git -y >nul 2>&1
    if not errorlevel 1 exit /b 0
)

echo     轮询最快Git镜像源并下载...
set "GIT_VERSION=%GIT_LATEST_VERSION%"
set "GIT_MIRRORS[0]=https://mirrors.huaweicloud.com/git-for-windows/git/releases/download/v%GIT_VERSION%.windows.1/Git-%GIT_VERSION%-64-bit.exe|华为云"
set "GIT_MIRRORS[1]=https://registry.npmmirror.com/-/binary/git-for-windows/git/releases/download/v%GIT_VERSION%.windows.1/Git-%GIT_VERSION%-64-bit.exe|npmmirror"
set "GIT_MIRRORS[2]=https://github.com/git-for-windows/git/releases/download/v%GIT_VERSION%.windows.1/Git-%GIT_VERSION%-64-bit.exe|GitHub官方"
set "GIT_BEST_URL=https://github.com/git-for-windows/git/releases/download/v%GIT_VERSION%.windows.1/Git-%GIT_VERSION%-64-bit.exe"
set "GIT_MIN_TIME=9999"
for /L %%i in (0,1,2) do (
    for /f "tokens=1,2 delims=|" %%a in ("!GIT_MIRRORS[%%i]!") do (
        set "GM_URL=%%a"
        set "GM_NAME=%%b"
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!GM_URL!" 2^>nul') do set "GM_TIME=%%t"
        if defined GM_TIME if not "!GM_TIME!"=="0" if not "!GM_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!GM_TIME!\'*1000)" 2^>nul') do set "GM_INT=%%m"
            if defined GM_INT if !GM_INT! LSS !GIT_MIN_TIME! (
                set "GIT_MIN_TIME=!GM_INT!"
                set "GIT_BEST_URL=!GM_URL!"
                echo         !GM_NAME!: !GM_TIME!s [!GM_INT!ms]
            )
        )
    )
)
echo     使用最快镜像下载Git...
if not exist "%TEMP%\git-installer.exe" (
    curl.exe -L -o "%TEMP%\git-installer.exe" "!GIT_BEST_URL!" 2>nul
)
if exist "%TEMP%\git-installer.exe" (
    "%TEMP%\git-installer.exe" /VERYSILENT /NORESTART /NOCANCEL /SP- /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS /COMPONENTS="assoc,assoc_sh" /PATHOPTION=NO >nul 2>&1
    set "PATH=%PATH%;C:\Program Files\Git\cmd"
    del "%TEMP%\git-installer.exe" 2>nul
    exit /b 0
)
exit /b 1

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

:get_latest_python_version
set "PYTHON_LATEST_VERSION="
echo     正在获取Python最新版本（使用国内镜像）...

:: 方法1: 使用短超时 + 多次重试（GitHub API）
for /L %%r in (1,1,3) do (
    for /f "delims=" %%v in ('curl.exe -s --connect-timeout 5 --max-time 10 https://api.github.com/repos/python/cpython/releases/latest 2^>nul ^| powershell -NoProfile -Command "$input ^| ConvertFrom-Json ^| Select-Object -ExpandProperty tag_name"') do set "PYTHON_LATEST_VERSION=%%v"
    if defined PYTHON_LATEST_VERSION goto :python_version_done
    if %%r lss 3 echo     重试获取... (%%r/3)
)

:: 方法2: 失败时使用国内镜像源获取版本信息
if not defined PYTHON_LATEST_VERSION (
    echo     [WARNING] GitHub API 获取失败，尝试国内镜像...
    for /f "delims=" %%v in ('curl.exe -s --connect-timeout 5 --max-time 10 https://mirrors.huaweicloud.com/python/ 2^>nul ^| powershell -NoProfile -Command "$input ^| Select-String -Pattern ""python-[0-9]+\.[0-9]+\.[0-9]+"" ^| Select-Object -First 1"') do (
        for /f "tokens=2 delims=-" %%p in ("%%v") do set "PYTHON_LATEST_VERSION=%%p"
    )
)

:python_version_done
if not defined PYTHON_LATEST_VERSION (
    echo     [WARNING] 所有方式获取失败，使用安全默认值
    set "PYTHON_LATEST_VERSION=3.12.6"
)

echo     检测到Python最新版本: %PYTHON_LATEST_VERSION%
exit /b

:auto_install_python
call :get_latest_python_version
call :log     检测到Python最新版本: %PYTHON_LATEST_VERSION%

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

call :log     轮询最快Python镜像源并下载...
set "PYTHON_VERSION=%PYTHON_LATEST_VERSION%"
set "PY_MIRRORS[0]=https://mirrors.huaweicloud.com/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe|华为云"
set "PY_MIRRORS[1]=https://registry.npmmirror.com/-/binary/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe|npmmirror"
set "PY_MIRRORS[2]=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe|Python官方"
set "PY_BEST_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
set "PY_MIN_TIME=9999"
for /L %%i in (0,1,2) do (
    for /f "tokens=1,2 delims=|" %%a in ("!PY_MIRRORS[%%i]!") do (
        set "PM_URL=%%a"
        set "PM_NAME=%%b"
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!PM_URL!" 2^>nul') do set "PM_TIME=%%t"
        if defined PM_TIME if not "!PM_TIME!"=="0" if not "!PM_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!PM_TIME!\'*1000)" 2^>nul') do set "PM_INT=%%m"
            if defined PM_INT if !PM_INT! LSS !PY_MIN_TIME! (
                set "PY_MIN_TIME=!PM_INT!"
                set "PY_BEST_URL=!PM_URL!"
                call :log         !PM_NAME!: !PM_TIME!s [!PM_INT!ms]
            )
        )
    )
)
call :log     使用最快镜像下载Python...
if not exist "%TEMP%\python_installer.exe" (
    curl.exe -L -o "%TEMP%\python_installer.exe" "!PY_BEST_URL!"
)

if exist "%TEMP%\python_installer.exe" (
    if not exist "%CD%\_python" mkdir "%CD%\_python"
    "%TEMP%\python_installer.exe" /quiet InstallAllUsers=0 PrependPath=0 Include_pip=1 TargetDir="%CD%\_python"
    if exist "%CD%\_python\python.exe" (
        set "PYTHON_CMD=%CD%\_python\python.exe"
        set "PATH=%CD%\_python;!PATH!"
        call :log [*] Python 已安装到本地目录: %CD%\_python
        del "%TEMP%\python_installer.exe" 2>nul
        setx PYTHON_CMD "%CD%\_python\python.exe" >nul 2>&1
        call :log     已持久化PYTHON_CMD到系统环境变量
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

:get_latest_node_version
set "NODE_LATEST_VERSION="
echo     正在获取Node.js最新版本（使用国内镜像）...

:: 方法1: 使用短超时 + 多次重试（GitHub API）
for /L %%r in (1,1,3) do (
    for /f "delims=" %%v in ('curl.exe -s --connect-timeout 5 --max-time 10 https://api.github.com/repos/nodejs/release/releases/latest 2^>nul ^| powershell -NoProfile -Command "$input ^| ConvertFrom-Json ^| Select-Object -ExpandProperty tag_name"') do set "NODE_LATEST_VERSION=%%v"
    if defined NODE_LATEST_VERSION goto :node_version_done
    if %%r lss 3 echo     重试获取... (%%r/3)
)

:: 方法2: 失败时使用国内镜像源获取版本信息
if not defined NODE_LATEST_VERSION (
    echo     [WARNING] GitHub API 获取失败，尝试国内镜像...
    for /f "delims=" %%v in ('curl.exe -s --connect-timeout 5 --max-time 10 https://npmmirror.com/mirrors/node/ 2^>nul ^| powershell -NoProfile -Command "$input ^| Select-String -Pattern ""v[0-9]+\.[0-9]+\.[0-9]+"" ^| Select-Object -First 1"') do set "NODE_LATEST_VERSION=%%v"
)

:node_version_done
if not defined NODE_LATEST_VERSION (
    echo     [WARNING] 所有方式获取失败，使用安全默认值
    set "NODE_LATEST_VERSION=v20.17.0"
)

echo     检测到Node.js最新版本: %NODE_LATEST_VERSION%
exit /b

:auto_install_node
call :get_latest_node_version
call :log     检测到Node.js最新版本: %NODE_LATEST_VERSION%

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

set "NODE_VERSION=%NODE_LATEST_VERSION%"
call :log     轮询最快Node.js镜像源并下载...
set "ND_MIRRORS[0]=https://npmmirror.com/mirrors/node/%NODE_VERSION%/node-%NODE_VERSION%-x64.msi|npmmirror"
set "ND_MIRRORS[1]=https://mirrors.huaweicloud.com/nodejs/%NODE_VERSION%/node-%NODE_VERSION%-x64.msi|华为云"
set "ND_MIRRORS[2]=https://nodejs.org/dist/%NODE_VERSION%/node-%NODE_VERSION%-x64.msi|Node官方"
set "ND_BEST_URL=https://nodejs.org/dist/%NODE_VERSION%/node-%NODE_VERSION%-x64.msi"
set "ND_MIN_TIME=9999"
for /L %%i in (0,1,2) do (
    for /f "tokens=1,2 delims=|" %%a in ("!ND_MIRRORS[%%i]!") do (
        set "NM_URL=%%a"
        set "NM_NAME=%%b"
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!NM_URL!" 2^>nul') do set "NM_TIME=%%t"
        if defined NM_TIME if not "!NM_TIME!"=="0" if not "!NM_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]\'!NM_TIME!\'*1000)" 2^>nul') do set "NM_INT=%%m"
            if defined NM_INT if !NM_INT! LSS !ND_MIN_TIME! (
                set "ND_MIN_TIME=!NM_INT!"
                set "ND_BEST_URL=!NM_URL!"
                call :log         !NM_NAME!: !NM_TIME!s [!NM_INT!ms]
            )
        )
    )
)
call :log     使用最快镜像下载Node.js...
if not exist "%TEMP%\node-installer.msi" (
    curl.exe -L -o "%TEMP%\node-installer.msi" "!ND_BEST_URL!"
)

if exist "%TEMP%\node-installer.msi" (
    msiexec /i "%TEMP%\node-installer.msi" /quiet /norestart
    del "%TEMP%\node-installer.msi" 2>nul
    
    :: 等待 node 加入 PATH（关键修复）
    call :log     等待 Node.js 安装完成...
    for /L %%w in (1,1,10) do (
        where node >nul 2>&1 && goto :node_installed_ok
        ping -n 2 127.0.0.1 >nul 2>&1
    )
    
    :: 如果还没找到，手动添加常见路径
    :node_installed_ok
    where node >nul 2>&1 || set "PATH=%PATH%;C:\Program Files\nodejs"
    
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

    call :log [*] 持久化NPM镜像到系统环境变量...
    setx NPM_CONFIG_REGISTRY "!NPM_BEST_MIRROR!" >nul 2>&1
    call :log     已写入系统环境变量: NPM_CONFIG_REGISTRY=!NPM_BEST_MIRROR!
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

    call :log [*] 持久化PIP镜像到系统环境变量...
    setx PIP_INDEX_URL "!FASTEST_PIP_MIRROR!" >nul 2>&1
    call :log     已写入系统环境变量: PIP_INDEX_URL=!FASTEST_PIP_MIRROR!

    if not exist "%APPDATA%\pip" mkdir "%APPDATA%\pip"
    echo:[global]> "%APPDATA%\pip\pip.ini"
    echo:index-url=!FASTEST_PIP_MIRROR!>> "%APPDATA%\pip\pip.ini"
    echo:trusted-host=!TRUSTED_HOST!>> "%APPDATA%\pip\pip.ini"
    echo:[install]>> "%APPDATA%\pip\pip.ini"
    echo:trusted-host=!TRUSTED_HOST!>> "%APPDATA%\pip\pip.ini"
    call :log     已写入用户级全局: %APPDATA%\pip\pip.ini
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
            :: 首次尝试：使用镜像源 + 预编译包（关键优化）
            "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt -i "!FASTEST_PIP_MIRROR!" --only-binary :all:
            if errorlevel 1 (
                call :log WARNING: 预编译包安装失败，尝试使用源码编译...
                "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt -i "!FASTEST_PIP_MIRROR!"
                if errorlevel 1 (
                    call :log WARNING: 使用镜像源安装失败，尝试默认源...
                    "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt
                    if errorlevel 1 (
                        call :log [ERROR] 依赖安装失败，请查看日志或手动运行: .venv\Scripts\pip install -r requirements.txt
                        pause
                        exit /b 1
                    )
                )
            )
        ) else (
            "!VENV_PATH!\Scripts\python.exe" -m pip install -r requirements.txt
            if errorlevel 1 (
                call :log [ERROR] 依赖安装失败，请手动检查网络或依赖兼容性
                pause
                exit /b 1
            )
        )
    )

    call :log [*] 安装Playwright浏览器...
    "!VENV_PATH!\Scripts\python.exe" main.py --install-playwright
    if errorlevel 1 (
        call :log [ERROR] Playwright浏览器安装失败，部分功能可能不可用
    ) else (
        call :log [*] Playwright 浏览器安装成功
    )
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