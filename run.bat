@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
title Szwego Crawler Tool

call :check_admin_rights
if errorlevel 1 (
    call :log [*] 正在请求管理员权限...
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
    for /f "delims=" %%L in ('type README.md ^| findstr /r /c:"^### v[0-9]"') do (
        for /f "tokens=2 delims=v " %%v in ("%%L") do (
            if "!VERSION!"=="0.0.0" set "VERSION=%%v"
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
    call :log [ERROR] 需要管理员权限
    exit /b 1
)
exit /b 0

:check_prerequisites
call :log [*] 检查前置条件...

where curl >nul 2>&1
if errorlevel 1 (
    call :log [ERROR] 未找到 curl.exe，需要 Windows 10 1803+ 或 Windows 11
    exit /b 1
)

where powershell >nul 2>&1
if errorlevel 1 (
    call :log [ERROR] 未找到 PowerShell
    exit /b 1
)

where winget >nul 2>&1
if errorlevel 1 (
    call :log [*] 未找到 Winget，正在自动安装...
    call :auto_install_winget
    where winget >nul 2>&1
    if not errorlevel 1 echo [*] Winget 安装成功
)

where choco >nul 2>&1
if errorlevel 1 (
    call :log [*] 未找到 Chocolatey，正在自动安装...
    call :auto_install_choco
    where choco >nul 2>&1
    if not errorlevel 1 echo [*] Chocolatey 安装成功
)

where git >nul 2>&1
if not errorlevel 1 (
    for /f "delims=" %%v in ('git --version 2^>nul') do set "CUR_GIT_VER=%%v"
    for /f "tokens=3 delims= " %%a in ("!CUR_GIT_VER!") do set "CUR_GIT_NUM=%%a"
    if defined CUR_GIT_NUM set "CUR_GIT_VER=!CUR_GIT_NUM!"
    call :log     当前Git版本: v!CUR_GIT_VER!
    
    call :check_git_latest_version
    if errorlevel 2 (
        call :log [*] 已跳过 Git 版本升级检查
    ) else (
        if errorlevel 1 (
            call :log [提示] 检测到Git有新版本，如需升级请手动执行: winget upgrade Git.Git
        ) else (
            call :log [*] Git已是最新版本
        )
    )
) else (
    call :log [*] 未找到 Git，正在自动安装...
    call :auto_install_git
    where git >nul 2>&1
    if errorlevel 1 (
        call :log [ERROR] Git 安装失败，请手动安装: https://git-scm.com/download/win
        exit /b 1
    )
    call :log [*] Git 安装成功
)

call :log [*] 前置条件检查通过
exit /b 0

:auto_install_winget
call :log 轮询最快Winget安装源...
set "WG_MIRRORS[0]=https://mirrors.huaweicloud.com/microsoft/winget-cli/latest/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle|华为云"
set "WG_MIRRORS[1]=https://github.com/microsoft/winget-cli/releases/latest/download/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle|GitHub官方"
set "WG_BEST_URL="
set "WG_MIN_TIME=9999"
for /L %%i in (0,1,1) do (
    set "WG_TIME="
    set "WG_INT="
    for /f "tokens=1,2 delims=|" %%a in ("!WG_MIRRORS[%%i]!") do (
        set "WG_URL=%%a"
        set "WG_NAME=%%b"
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!WG_URL!" 2^>nul') do set "WG_TIME=%%t"
        if defined WG_TIME if not "!WG_TIME!"=="0" if not "!WG_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!WG_TIME!*1000)" 2^>nul') do set "WG_INT=%%m"
        )
        if defined WG_INT (
            if !WG_INT! LSS !WG_MIN_TIME! (
                set "WG_MIN_TIME=!WG_INT!"
                set "WG_BEST_URL=!WG_URL!"
            )
            call :log     !WG_NAME!: !WG_TIME!s [!WG_INT!ms]
        ) else (
            call :log     !WG_NAME!: 超时/失败
        )
    )
)
if defined WG_BEST_URL (
    call :log 使用最快镜像下载Winget...
    curl.exe -L -o "%TEMP%\winget-installer.msixbundle" "!WG_BEST_URL!" 2>nul
    if exist "%TEMP%\winget-installer.msixbundle" (
        powershell -NoProfile -Command "Add-AppxPackage -Path '%TEMP%\winget-installer.msixbundle'" 2>nul
        del "%TEMP%\winget-installer.msixbundle" 2>nul
    )
) else (
    call :log 尝试通过Microsoft Store安装Winget...
    powershell -NoProfile -Command "Start-Process 'ms-windows-store://pdp/?ProductId=9NBLGGH4NNS2'" 2>nul
)
exit /b 0

:auto_install_choco
call :log 轮询最快Chocolatey安装源...
set "CCO_MIRRORS[0]=https://mirrors.huaweicloud.com/chocolatey/install.ps1|华为云"
set "CCO_MIRRORS[1]=https://community.chocolatey.org/install.ps1|Chocolatey官方"
set "CCO_BEST_URL=https://community.chocolatey.org/install.ps1"
set "CCO_MIN_TIME=9999"
for /L %%i in (0,1,1) do (
    set "CCO_TIME="
    set "CCO_INT="
    for /f "tokens=1,2 delims=|" %%a in ("!CCO_MIRRORS[%%i]!") do (
        set "CCO_URL=%%a"
        set "CCO_NAME=%%b"
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!CCO_URL!" 2^>nul') do set "CCO_TIME=%%t"
        if defined CCO_TIME if not "!CCO_TIME!"=="0" if not "!CCO_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!CCO_TIME!*1000)" 2^>nul') do set "CCO_INT=%%m"
        )
        if defined CCO_INT (
            if !CCO_INT! LSS !CCO_MIN_TIME! (
                set "CCO_MIN_TIME=!CCO_INT!"
                set "CCO_BEST_URL=!CCO_URL!"
            )
            call :log     !CCO_NAME!: !CCO_TIME!s [!CCO_INT!ms]
        ) else (
            call :log     !CCO_NAME!: 超时/失败
        )
    )
)
call :log 使用最快镜像安装Chocolatey...
powershell -NoProfile -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('!CCO_BEST_URL!'))" 2>nul

:: 刷新当前会话的PATH（关键修复）
call :refresh_path
exit /b 0

:refresh_path
call :log 刷新环境变量...
set "PATH=%PATH%;C:\ProgramData\chocolatey\bin"

:: 等待choco命令可用（最多等待10秒）
for /L %%w in (1,1,10) do (
    where choco >nul 2>&1 && goto :choco_ready
    ping -n 1 127.0.0.1 >nul 2>&1
)

:choco_ready
if exist "C:\ProgramData\chocolatey\bin\choco.exe" (
    call :log Chocolatey 已就绪
) else (
    call :log [WARNING] Chocolatey 可能未完全安装，部分功能可能不可用
)
exit /b

:get_latest_git_version
set "GIT_LATEST_VERSION="

:: 方法1: 华为云镜像目录列表（取最新的 v2.x.y.windows.N 标签，跳过 rc 预发布版）
for /f "delims=" %%v in ('curl.exe -sL --connect-timeout 8 --max-time 20 https://mirrors.huaweicloud.com/git-for-windows/ 2^>nul ^| powershell -NoProfile -Command "$s = ($input | Out-String); $m = [regex]::Matches($s, 'v(2\.\d+\.\d+\.windows\.\d+)/'); $v = $m | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique | Sort-Object { [version]($_ -replace '\.windows\.', '.') } -Descending | Select-Object -First 1; if ($v) { $v }"') do set "GIT_LATEST_VERSION=%%v"

:: 方法2: npmmirror国内镜像
if not defined GIT_LATEST_VERSION (
    for /f "delims=" %%v in ('curl.exe -sL --connect-timeout 8 --max-time 20 https://registry.npmmirror.com/-/binary/git-for-windows/ 2^>nul ^| powershell -NoProfile -Command "$s = ($input | Out-String); $m = [regex]::Matches($s, 'v(2\.\d+\.\d+\.windows\.\d+)/'); $v = $m | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique | Sort-Object { [version]($_ -replace '\.windows\.', '.') } -Descending | Select-Object -First 1; if ($v) { $v }"') do set "GIT_LATEST_VERSION=%%v"
)

if not defined GIT_LATEST_VERSION (
    call :log [WARNING] 所有国内镜像获取失败，跳过Git版本对比
)
exit /b

:auto_install_git
call :get_latest_git_version
if not defined GIT_LATEST_VERSION set "GIT_LATEST_VERSION=2.56.0.windows.4"
call :log 检测到Git最新版本: %GIT_LATEST_VERSION%

where winget >nul 2>&1
if not errorlevel 1 (
    call :log 使用 Winget 安装 Git...
    winget install Git.Git --accept-package-agreements --accept-source-agreements --silent >nul 2>&1
    call :refresh_git_path
    where git >nul 2>&1
    if not errorlevel 1 exit /b 0
)

where choco >nul 2>&1
if not errorlevel 1 (
    call :log 使用 Chocolatey 安装 Git...
    choco install git -y >nul 2>&1
    call :refresh_git_path
    where git >nul 2>&1
    if not errorlevel 1 exit /b 0
)

call :log 轮询最快Git镜像源并下载...
set "GIT_TAG=%GIT_LATEST_VERSION%"
set "GIT_ASSET_VER=%GIT_TAG:.windows.=.%"
set "GIT_MIRRORS[0]=https://mirrors.huaweicloud.com/git-for-windows/v%GIT_TAG%/Git-%GIT_ASSET_VER%-64-bit.exe|华为云"
set "GIT_MIRRORS[1]=https://registry.npmmirror.com/-/binary/git-for-windows/v%GIT_TAG%/Git-%GIT_ASSET_VER%-64-bit.exe|npmmirror"
set "GIT_MIRRORS[2]=https://github.com/git-for-windows/git/releases/download/v%GIT_TAG%/Git-%GIT_ASSET_VER%-64-bit.exe|GitHub官方"
set "GIT_BEST_URL=https://mirrors.huaweicloud.com/git-for-windows/v%GIT_TAG%/Git-%GIT_ASSET_VER%-64-bit.exe"
set "GIT_MIN_TIME=9999"
for /L %%i in (0,1,2) do (
    for /f "tokens=1,2 delims=|" %%a in ("!GIT_MIRRORS[%%i]!") do (
        set "GM_URL=%%a"
        set "GM_NAME=%%b"
        set "GM_TIME="
        set "GM_INT="
        for /f "delims=" %%t in ('curl.exe -sIL -o NUL -w "%%{time_connect}" --connect-timeout 3 --max-time 6 "!GM_URL!" 2^>nul') do set "GM_TIME=%%t"
        if defined GM_TIME if not "!GM_TIME!"=="0" if not "!GM_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!GM_TIME!*1000)" 2^>nul') do set "GM_INT=%%m"
        )
        if defined GM_INT (
            call :log     !GM_NAME!: !GM_TIME!s [!GM_INT!ms]
            if !GM_INT! LSS !GIT_MIN_TIME! (
                set "GIT_MIN_TIME=!GM_INT!"
                set "GIT_BEST_URL=!GM_URL!"
            )
        ) else (
            call :log     !GM_NAME!: 超时/失败
        )
    )
)
call :log 使用最快镜像下载Git...
if not exist "%TEMP%\git-installer.exe" (
    curl.exe -L -o "%TEMP%\git-installer.exe" "!GIT_BEST_URL!" 2>nul
)
if exist "%TEMP%\git-installer.exe" (
    "%TEMP%\git-installer.exe" /VERYSILENT /NORESTART /NOCANCEL /SP- /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS /COMPONENTS="assoc,assoc_sh" /PATHOPTION=NO >nul 2>&1
    del "%TEMP%\git-installer.exe" 2>nul
    call :refresh_git_path
    where git >nul 2>&1
    if not errorlevel 1 exit /b 0
)
exit /b 1

:refresh_git_path
if exist "C:\Program Files\Git\cmd\git.exe" set "PATH=!PATH!;C:\Program Files\Git\cmd"
if exist "C:\Program Files (x86)\Git\cmd\git.exe" set "PATH=!PATH!;C:\Program Files (x86)\Git\cmd"
if exist "C:\Program Files\Git\bin\git.exe" set "PATH=!PATH!;C:\Program Files\Git\bin"
if exist "C:\Program Files (x86)\Git\bin\git.exe" set "PATH=!PATH!;C:\Program Files (x86)\Git\bin"
if exist "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" set "PATH=!PATH!;%LOCALAPPDATA%\Programs\Git\cmd"
exit /b 0

:ms_timestamp
set "TIMESTAMP="
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set "datetime=%%I"
if defined datetime set "TIMESTAMP=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%:%datetime:~12,2%.%datetime:~15,3%"
if not defined TIMESTAMP set "TIMESTAMP=%date% %time: =0%"
exit /b

:log
call :ms_timestamp
set "LOGLINE=%*"
echo [%TIMESTAMP%] !LOGLINE!
if not "%LOG_FILE%"=="" (
    if exist "!LOG_FILE!" (
        >> "!LOG_FILE!" echo([%TIMESTAMP%] !LOGLINE! 2>nul
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
call :kill_all_interfering_processes
ping -n 2 127.0.0.1 >nul 2>&1

call :wait_for_port !WEB_PORT! 10
call :log [*] 残留进程清理完成

call :log_blank
call :log [*] 检查 Playwright 浏览器驱动...
call :check_and_fix_playwright

call :log_blank
call :log [*] 检查 hostc 隧道工具...
set "HOSTC_BIN=%~dp0dist\node_modules\.bin\hostc.cmd"
set "HOSTC_VER="
if not exist "%~dp0dist\node_modules\hostc\package.json" set "HOSTC_BIN="
if not defined HOSTC_BIN (
    call :log [*] 本地未找到 hostc，开始安装...
    call :install_hostc
    if exist "%~dp0dist\node_modules\.bin\hostc.cmd" set "HOSTC_BIN=%~dp0dist\node_modules\.bin\hostc.cmd"
)
if defined HOSTC_BIN (
    for /f "delims=" %%v in ('"!HOSTC_BIN!" --version 2^>nul') do if not defined HOSTC_VER set "HOSTC_VER=%%v"
)
if defined HOSTC_VER (
    call :log [*] 当前 hostc 版本: v!HOSTC_VER!
    
    call :check_hostc_latest_version "!HOSTC_VER!"
    if errorlevel 2 (
        call :log [*] 已跳过 hostc 版本升级检查
    ) else (
        if errorlevel 1 (
            call :log [*] 检测到新版本，正在自动升级 hostc...
            call :install_hostc
            set "HOSTC_VER="
            for /f "delims=" %%v in ('"!HOSTC_BIN!" --version 2^>nul') do if not defined HOSTC_VER set "HOSTC_VER=%%v"
            call :log [*] hostc 已升级到最新版: v!HOSTC_VER!
        ) else (
            call :log [*] hostc v!HOSTC_VER! 已是最新版本
        )
    )
) else (
    call :log [WARNING] hostc 安装失败，隧道将不可用
)

call :log_blank
call :log [*] 检查 cloudflared 隧道工具...
set "CFD_BIN="
set "CFD_VER="
set "CFD_FROM_TOOLS="
if exist "%~dp0tools\cloudflared\windows\cloudflared.exe" (
    set "CFD_BIN=%~dp0tools\cloudflared\windows\cloudflared.exe"
    set "CFD_FROM_TOOLS=1"
)
if not defined CFD_BIN (
    if exist "%~dp0dist\node_modules\cloudflared\package.json" (
        if exist "%~dp0dist\node_modules\.bin\cloudflared.cmd" set "CFD_BIN=%~dp0dist\node_modules\.bin\cloudflared.cmd"
    )
)
if not defined CFD_BIN (
    for /f "delims=" %%p in ('where cloudflared 2^>nul') do if not defined CFD_BIN set "CFD_BIN=%%p"
)
if defined CFD_BIN (
    for /f "delims=" %%v in ('"!CFD_BIN!" --version 2^>nul') do if not defined CFD_VER set "CFD_VER=%%v"
)
if defined CFD_VER (
    call :log     当前cloudflared版本: !CFD_VER!
    call :log     当前cloudflared路径: !CFD_BIN!
    
    if defined CFD_FROM_TOOLS (
        call :log [*] cloudflared 由 tools 目录提供，跳过版本对比
    ) else (
        call :check_cloudflared_latest_version
        if errorlevel 2 (
            call :log [*] 已跳过 cloudflared 版本升级检查
        ) else (
            if errorlevel 1 (
                call :log [提示] 检测到cloudflared有新版本，如需升级请手动执行 install_cloudflared
            ) else (
                call :log [*] cloudflared已是最新版本
            )
        )
    )
) else (
    call :log [*] 未找到可用的cloudflared，正在安装...
    call :install_cloudflared
    set "CFD_BIN="
    if exist "%~dp0tools\cloudflared\windows\cloudflared.exe" set "CFD_BIN=%~dp0tools\cloudflared\windows\cloudflared.exe"
    if not defined CFD_BIN if exist "%~dp0dist\node_modules\.bin\cloudflared.cmd" set "CFD_BIN=%~dp0dist\node_modules\.bin\cloudflared.cmd"
    if defined CFD_BIN (
        for /f "delims=" %%v in ('"!CFD_BIN!" --version 2^>nul') do if not defined CFD_VER set "CFD_VER=%%v"
        if defined CFD_VER call :log     当前cloudflared版本: !CFD_VER!
    )
)

call :log_blank
call :log [*] 启动 hostc 隧道（后台运行）...
if exist "!HOSTC_BIN!" (
    start /b cmd /c ""!HOSTC_BIN!" 127.0.0.1:!WEB_PORT!" < nul
    call :log [*] hostc 已在后台启动
)

call :log_blank
call :log [*] 清理临时文件...
call :cleanup_temp_dir temp 3145728

goto detect_environments

:kill_process_safe
set "PROC_NAME=%~1"
wmic process where "name='%PROC_NAME%'" get processid,commandline 2>nul | findstr /i "xy_ws" >nul 2>&1
if not errorlevel 1 (
    for /f "tokens=2 delims=," %%p in ('wmic process where "name='%PROC_NAME%' and commandline like '%%xy_ws%%'" get processid /format:csv 2^>nul ^| findstr /r "[0-9]"') do (
        taskkill /F /PID %%p >nul 2>&1
        call :log     已终止进程 %%p (%PROC_NAME%)
    )
)
exit /b

:kill_playwright_browsers
set "PW_BROWSER_COUNT=0"
set "PWB_FILTER=name='chrome.exe' or name='chromium.exe' or name='headless_shell.exe' or name='firefox.exe' or name='msedge.exe' or name='node.exe'"
set "PWB_MATCH=ms-playwright|playwright-core|playwright_chromiumdev_profile|remote-debugging-pipe"
for /f "delims=" %%c in ('powershell -NoProfile -Command "$n=0; Get-CimInstance Win32_Process -Filter $env:PWB_FILTER | Where-Object { $_.CommandLine -match $env:PWB_MATCH } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue; $n++ }; $n" 2^>nul') do set "PW_BROWSER_COUNT=%%c"
exit /b

:kill_browser_processes
call :kill_playwright_browsers
if !PW_BROWSER_COUNT! gtr 0 (
    call :log     [防护] 已清理 !PW_BROWSER_COUNT! 个浏览器僵尸进程 (Playwright Chrome/Chromium)
) else (
    call :log     [防护] 未发现浏览器僵尸进程
)
exit /b

:kill_playwright_processes
set "PW_COUNT=0"
set "PWP_FILTER=name='node.exe' or name='playwright.exe'"
set "PWP_MATCH=ms-playwright|playwright-core|playwright"
for /f "delims=" %%c in ('powershell -NoProfile -Command "$n=0; Get-CimInstance Win32_Process -Filter $env:PWP_FILTER | Where-Object { $_.CommandLine -match $env:PWP_MATCH } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue; $n++ }; $n" 2^>nul') do set "PW_COUNT=%%c"
if !PW_COUNT! gtr 0 (
    call :log     [防护] 已清理 !PW_COUNT! 个 Playwright 残留进程
) else (
    call :log     [防护] 未发现 Playwright 残留进程
)
exit /b

:kill_all_interfering_processes
call :log [*] [全面防护] 开始清理所有可能干扰的进程...

set "TOTAL_KILLED=0"

for /f "tokens=2 delims=," %%p in ('wmic process where "name='python.exe' and commandline like '%%main.py%%'" get processid /format:csv 2^>nul ^| findstr /r "[0-9]"') do (
    taskkill /F /PID %%p >nul 2>&1
    set /a TOTAL_KILLED+=1
)

for /f "tokens=2 delims=," %%p in ('wmic process where "name='node.exe' and commandline like '%%hostc%%'" get processid /format:csv 2^>nul ^| findstr /r "[0-9]"') do (
    taskkill /F /PID %%p >nul 2>&1
    set /a TOTAL_KILLED+=1
)

for /f "tokens=2 delims=," %%p in ('wmic process where "name='cloudflared.exe' and commandline like '%%xy_ws%%'" get processid /format:csv 2^>nul ^| findstr /r "[0-9]"') do (
    taskkill /F /PID %%p >nul 2>&1
    set /a TOTAL_KILLED+=1
)

call :kill_playwright_browsers
set /a TOTAL_KILLED+=!PW_BROWSER_COUNT!

netstat -ano | findstr ":!WEB_PORT!.*LISTENING" >nul 2>&1
if not errorlevel 1 (
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":!WEB_PORT!.*LISTENING"') do (
        taskkill /F /PID %%a >nul 2>&1
        set /a TOTAL_KILLED+=1
    )
)

if !TOTAL_KILLED! gtr 0 (
    call :log     [全面防护] ✅ 已清理 !TOTAL_KILLED! 个可能干扰启动的进程
) else (
    call :log     [全面防护] ✅ 系统干净，无干扰进程
)

set "KILL_RETRY=0"

:kill_residual_retry
set "RESIDUAL_COUNT=0"
for /f "tokens=2 delims=," %%p in ('wmic process where "name='python.exe' and commandline like '%%main.py%%'" get processid /format:csv 2^>nul ^| findstr /r "[0-9]"') do (
    taskkill /F /PID %%p >nul 2>&1
    set /a RESIDUAL_COUNT+=1
)
netstat -ano | findstr ":!WEB_PORT!.*LISTENING" >nul 2>&1
if not errorlevel 1 (
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":!WEB_PORT!.*LISTENING"') do (
        taskkill /F /PID %%a >nul 2>&1
        set /a RESIDUAL_COUNT+=1
    )
)
if !RESIDUAL_COUNT! gtr 0 (
    set /a TOTAL_KILLED+=!RESIDUAL_COUNT!
    set /a KILL_RETRY+=1
    if !KILL_RETRY! lss 3 (
        ping -n 2 127.0.0.1 >nul 2>&1
        goto kill_residual_retry
    )
    call :log     [全面防护] ⚠️  残留进程清理 !KILL_RETRY! 轮后仍未完全释放
)
exit /b

:check_and_fix_playwright
set "PLAYWRIGHT_VER="
for /f "delims=" %%v in ('python -c "from importlib.metadata import version; print(version('playwright'))" 2^>nul') do set "PLAYWRIGHT_VER=%%v"
if not defined PLAYWRIGHT_VER set "PLAYWRIGHT_VER=unknown"

set "PW_ENV_PATH="
if defined PLAYWRIGHT_BROWSERS_PATH set "PW_ENV_PATH=!PLAYWRIGHT_BROWSERS_PATH!"

call :detect_playwright_browsers_path
if defined PW_FOUND_PATH (
    set "PLAYWRIGHT_BROWSERS_PATH=!PW_FOUND_PATH!"
    call :log     [Playwright] ✅ Chromium 浏览器驱动正常 (Playwright v!PLAYWRIGHT_VER!)
    call :log     [Playwright]    驱动目录: !PLAYWRIGHT_BROWSERS_PATH!
    exit /b
)

call :log     [Playwright] ⚠️  未检测到本地 Chromium 浏览器驱动 (Playwright v!PLAYWRIGHT_VER!)
call :log     [Playwright] ℹ️  已禁用自动下载，请确保本地浏览器目录存在
exit /b 1

:detect_playwright_browsers_path
set "PW_FOUND_PATH="
call :probe_browsers_dir "!PW_ENV_PATH!"
if defined PW_FOUND_PATH exit /b
call :probe_browsers_dir "%~dp0tools\playwright\windows"
if defined PW_FOUND_PATH exit /b
call :probe_browsers_dir "%~dp0playwright-browsers"
if defined PW_FOUND_PATH exit /b
call :probe_browsers_dir "!LOCALAPPDATA!\ms-playwright"
if defined PW_FOUND_PATH exit /b
call :probe_browsers_dir "%USERPROFILE%\AppData%\Local\ms-playwright"
exit /b

:probe_browsers_dir
set "PW_PROBE_DIR=%~1"
if not defined PW_PROBE_DIR exit /b
if not exist "!PW_PROBE_DIR!" exit /b
for /d %%d in ("!PW_PROBE_DIR!\chromium-*") do (
    if exist "%%~fd\chrome-win\chrome.exe" (
        set "PW_FOUND_PATH=!PW_PROBE_DIR!"
    ) else if exist "%%~fd\chrome-win64\chrome.exe" (
        set "PW_FOUND_PATH=!PW_PROBE_DIR!"
    ) else if exist "%%~fd\chrome-win\headless_shell.exe" (
        set "PW_FOUND_PATH=!PW_PROBE_DIR!"
    ) else if exist "%%~fd\chrome-win64\headless_shell.exe" (
        set "PW_FOUND_PATH=!PW_PROBE_DIR!"
    )
)
if defined PW_FOUND_PATH exit /b
for /d %%d in ("!PW_PROBE_DIR!\chromium_headless_shell-*") do (
    if exist "%%~fd\chrome-win\headless_shell.exe" (
        set "PW_FOUND_PATH=!PW_PROBE_DIR!"
    ) else if exist "%%~fd\chrome-win64\headless_shell.exe" (
        set "PW_FOUND_PATH=!PW_PROBE_DIR!"
    )
)
exit /b

:wait_for_port
set "WAIT_PORT=%~1"
set "MAX_WAIT=%~2"
set "WAIT_COUNT=0"

:port_wait_loop
if %WAIT_COUNT% geq %MAX_WAIT% goto port_wait_done
netstat -ano | findstr ":%WAIT_PORT%.*LISTENING" >nul 2>&1
if errorlevel 1 goto port_wait_done
set /a WAIT_COUNT+=1
set "MSG=[*] 端口%WAIT_PORT%仍被占用，等待释放... (%WAIT_COUNT%/%MAX_WAIT%)"
call :log %MSG%
ping -n 2 127.0.0.1 >nul 2>&1
goto port_wait_loop

:port_wait_done
if %WAIT_COUNT% geq %MAX_WAIT% (
    set "MSG=[WARNING] 端口%WAIT_PORT%等待超时，强制清理..."
    call :log %MSG%
    for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":%WAIT_PORT%.*LISTENING"') do taskkill /F /PID %%p >nul 2>&1
    ping -n 2 127.0.0.1 >nul 2>&1
)
exit /b

:cleanup_temp_dir
set "DIR_NAME=%~1"
set "MAX_SIZE=%~2"
if exist "%DIR_NAME%" (
    for /f "delims=" %%a in ('powershell -NoProfile -Command "(Get-ChildItem -Path '%DIR_NAME%' -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum" 2^>nul') do set "DIR_SIZE=%%a"
    if defined DIR_SIZE if !DIR_SIZE! gtr %MAX_SIZE% (
        rd /s /q "%DIR_NAME%" >nul 2>&1
        mkdir "%DIR_NAME%" >nul 2>&1
        set "MSG=[*] %DIR_NAME%目录超过限制，已完全清空"
        call :log %MSG%
    ) else (
        set "MSG=[*] %DIR_NAME%目录未超过限制，跳过清理"
        call :log %MSG%
    )
) else (
    set "MSG=[*] %DIR_NAME%目录不存在，跳过"
    call :log %MSG%
)
exit /b

:get_dir_size
set "TOTAL_SIZE=0"
for /f "tokens=3" %%a in ('dir /s /a "%~1" 2^>nul ^| findstr /c:"File(s)"') do set "TOTAL_SIZE=%%a"
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
) else (
    for /f "delims=" %%v in ('"!PYTHON_CMD!" --version 2^>nul') do set "CUR_PY_VER=%%v"
    call :log     当前Python版本: !CUR_PY_VER!
    
    call :check_python_latest_version "!CUR_PY_VER!"
    if errorlevel 2 (
        call :log [*] 已跳过 Python 版本升级检查
    ) else (
        if errorlevel 1 (
            call :log [提示] 检测到Python有新版本，如需升级请手动执行: winget upgrade Python.Python.3
        ) else (
            call :log [*] Python已是最新版本
        )
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
set "PY_VER_PATTERN=3\.(\d+)\.(\d+)/"
call :log 正在获取Python最新版本（使用国内镜像）...

:: 方法1: 华为云镜像（目录名即版本号，如 3.16.0/）
for /f "delims=" %%v in ('curl.exe -sL --connect-timeout 8 --max-time 20 https://mirrors.huaweicloud.com/python/ 2^>nul ^| powershell -NoProfile -Command "$s = ($input | Out-String); $m = [regex]::Matches($s, $env:PY_VER_PATTERN); $v = $m | ForEach-Object { $_.Value.TrimEnd([char]47) } | Sort-Object { [version]$_ } -Descending | Select-Object -First 1; if ($v) { $v }"') do set "PYTHON_LATEST_VERSION=%%v"

:: 方法2: 清华镜像
if not defined PYTHON_LATEST_VERSION (
    for /f "delims=" %%v in ('curl.exe -sL --connect-timeout 8 --max-time 20 https://mirrors.tuna.tsinghua.edu.cn/python/ 2^>nul ^| powershell -NoProfile -Command "$s = ($input | Out-String); $m = [regex]::Matches($s, $env:PY_VER_PATTERN); $v = $m | ForEach-Object { $_.Value.TrimEnd([char]47) } | Sort-Object { [version]$_ } -Descending | Select-Object -First 1; if ($v) { $v }"') do set "PYTHON_LATEST_VERSION=%%v"
)

if not defined PYTHON_LATEST_VERSION (
    call :log [WARNING] 所有国内镜像获取失败，跳过Python版本对比
    exit /b 0
)

call :log 检测到Python最新版本: %PYTHON_LATEST_VERSION%
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
        set "PM_TIME="
        set "PM_INT="
        for /f "delims=" %%t in ('curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 2 --max-time 3 "!PM_URL!" 2^>nul') do set "PM_TIME=%%t"
        if defined PM_TIME if not "!PM_TIME!"=="0" if not "!PM_TIME!"=="0.000000" (
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!PM_TIME!*1000)" 2^>nul') do set "PM_INT=%%m"
        )
        if defined PM_INT (
            call :log         !PM_NAME!: !PM_TIME!s [!PM_INT!ms]
            if !PM_INT! LSS !PY_MIN_TIME! (
                set "PY_MIN_TIME=!PM_INT!"
                set "PY_BEST_URL=!PM_URL!"
            )
        ) else (
            call :log         !PM_NAME!: 超时/失败
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
if not errorlevel 1 (
    for /f "delims=" %%v in ('node --version 2^>nul') do set "CUR_NODE_VER=%%v"
    call :log     当前Node.js版本: !CUR_NODE_VER!
    
    call :check_node_latest_version !CUR_NODE_VER!
    if errorlevel 2 (
        call :log [*] 已跳过 Node.js 版本升级检查
    ) else (
        if errorlevel 1 (
            call :log [提示] 检测到Node.js有新版本，如需升级请手动执行: winget upgrade OpenJS.NodeJS.LTS
        ) else (
            call :log [*] Node.js !CUR_NODE_VER! 已是最新版本
        )
    )
    
    goto :node_verify_install
)

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
call :log 正在获取Node.js最新版本（使用国内镜像）...

:: 方法1: npmmirror国内镜像（优先，取最新的 LTS 稳定版，跳过 alpha/beta 等预发布版）
for /f "delims=" %%v in ('curl.exe -sL --connect-timeout 8 --max-time 20 https://npmmirror.com/mirrors/node/index.json 2^>nul ^| powershell -NoProfile -Command "try { $j = ($input | Out-String | ConvertFrom-Json); $v = $j | Where-Object { $_.lts -ne $false } | Select-Object -First 1; if ($v) { $v.version } } catch {}"') do set "NODE_LATEST_VERSION=%%v"

:: 方法2: 华为云镜像
if not defined NODE_LATEST_VERSION (
    for /f "delims=" %%v in ('curl.exe -sL --connect-timeout 8 --max-time 20 https://mirrors.huaweicloud.com/nodejs/index.json 2^>nul ^| powershell -NoProfile -Command "try { $j = ($input | Out-String | ConvertFrom-Json); $v = $j | Where-Object { $_.lts -ne $false } | Select-Object -First 1; if ($v) { $v.version } } catch {}"') do set "NODE_LATEST_VERSION=%%v"
)

:: 方法3: 清华镜像
if not defined NODE_LATEST_VERSION (
    for /f "delims=" %%v in ('curl.exe -sL --connect-timeout 8 --max-time 20 https://mirrors.tuna.tsinghua.edu.cn/nodejs-release/index.json 2^>nul ^| powershell -NoProfile -Command "try { $j = ($input | Out-String | ConvertFrom-Json); $v = $j | Where-Object { $_.lts -ne $false } | Select-Object -First 1; if ($v) { $v.version } } catch {}"') do set "NODE_LATEST_VERSION=%%v"
)

if not defined NODE_LATEST_VERSION (
    call :log [WARNING] 所有国内镜像获取失败，跳过Node.js版本对比
    exit /b 0
)

call :log 检测到Node.js最新版本: %NODE_LATEST_VERSION%
exit /b

:auto_install_node
call :get_latest_node_version
if not defined NODE_LATEST_VERSION set "NODE_LATEST_VERSION=v22.11.0"
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
            for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!NM_TIME!*1000)" 2^>nul') do set "NM_INT=%%m"
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
    set "FASTEST_PIP_MIRROR=https://mirrors.aliyun.com/pypi/simple/"
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
        set "TEST_TIME="
        set "PIP_INT_TIME="
        set "HTTP_CODE="
        call :log     测试 !MIRROR_NAME!...
        
        for /f "tokens=1,2 delims=:" %%c in ('curl.exe -s -I -o NUL -w "%%{http_code}:%%{time_total}" --connect-timeout 5 --max-time 8 "!MIRROR_URL!" 2^>nul') do (
            set "HTTP_CODE=%%c"
            set "TEST_TIME=%%d"
        )
        
        if defined HTTP_CODE if not "!HTTP_CODE!"=="000" if not "!HTTP_CODE!"=="0000" if defined TEST_TIME (
            if not "!TEST_TIME!"=="0" if not "!TEST_TIME!"=="0.000000" (
                for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!TEST_TIME!*1000)" 2^>nul') do set "PIP_INT_TIME=%%m"
            )
        )
        
        if defined PIP_INT_TIME (
            call :log         !MIRROR_NAME!: !TEST_TIME!秒 [!PIP_INT_TIME!ms]
            if !PIP_INT_TIME! LSS !MIN_TIME! (
                set "MIN_TIME=!PIP_INT_TIME!"
                set "BEST_MIRROR=!MIRROR_URL!"
                set "BEST_NAME=!MIRROR_NAME!"
            )
        ) else (
            call :log         !MIRROR_NAME!: 超时/失败
        )
    )
)

if "!BEST_MIRROR!"=="" (
    call :log [WARNING] 所有PIP镜像测试失败，使用默认阿里云源
    set "FASTEST_PIP_MIRROR=https://mirrors.aliyun.com/pypi/simple/"
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
set "HOSTC_BEST_NAME=npmmirror淘宝"
set "HOSTC_MIN_TIME=9999"

for /L %%i in (0,1,2) do (
    for /f "tokens=1,2 delims=|" %%a in ("!HOSTC_MIRRORS[%%i]!") do (
        set "H_URL=%%a"
        set "H_NAME=%%b"
        set "H_TIME="
        set "H_INT="
        set "H_CODE="
        
        for /f "tokens=1,2 delims=:" %%c in ('curl.exe -s -I -o NUL -w "%%{http_code}:%%{time_total}" --connect-timeout 5 --max-time 8 "!H_URL!" 2^>nul') do (
            set "H_CODE=%%c"
            set "H_TIME=%%d"
        )
        
        if defined H_CODE if not "!H_CODE!"=="000" if not "!H_CODE!"=="0000" if defined H_TIME (
            if not "!H_TIME!"=="0" if not "!H_TIME!"=="0.000000" (
                for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!H_TIME!*1000)" 2^>nul') do set "H_INT=%%m"
            )
        )
        
        if defined H_INT (
            call :log     测试 !H_NAME!: !H_TIME!秒 [!H_INT!ms]
            if !H_INT! LSS !HOSTC_MIN_TIME! (
                set "HOSTC_MIN_TIME=!H_INT!"
                set "HOSTC_BEST_MIRROR=!H_URL!"
                set "HOSTC_BEST_NAME=!H_NAME!"
            )
        ) else (
            call :log     测试 !H_NAME!: 超时/失败
        )
    )
)

call :log [*] 最快hostc镜像: !HOSTC_BEST_NAME! [!HOSTC_MIN_TIME!ms]

call :log [*] 使用最佳镜像安装 hostc...
call npm install hostc@latest --registry "!HOSTC_BEST_MIRROR!" --prefix "%~dp0dist" 2>nul
if errorlevel 1 (
    call :log [ERROR] hostc 安装失败
) else (
    call :log [*] hostc 安装成功
)
exit /b 0


:check_hostc_latest_version
call :check_hostc_latest_version_impl %1
exit /b %ERRORLEVEL%

:check_hostc_latest_version_impl
set "CURRENT_VER=%~1"
if not defined CURRENT_VER (
    call :log [WARNING] 无法获取当前 hostc 版本，跳过版本检查
    exit /b 2
)

call :log [*] 检查 hostc 最新版本...

:: 获取最新版本号（使用 npm view 命令）
set "LATEST_VER="
for /f "delims=" %%v in ('npm view hostc version 2^>nul') do set "LATEST_VER=%%v"

if not defined LATEST_VER (
    call :log [WARNING] 无法获取 hostc 最新版本信息，跳过升级检查
    exit /b 2
)

call :log     当前版本: v!CURRENT_VER!
call :log     最新版本: v!LATEST_VER!

:: 简单的版本比较（仅比较主版本号.次版本号.修订号）
set "CUR_MAJOR="
set "CUR_MINOR="
set "CUR_PATCH="
set "LAT_MAJOR="
set "LAT_MINOR="
set "LAT_PATCH="
for /f "tokens=1,2,3 delims=." %%a in ("!CURRENT_VER!") do set "CUR_MAJOR=%%a" & set "CUR_MINOR=%%b" & set "CUR_PATCH=%%c"
for /f "tokens=1,2,3 delims=." %%a in ("!LATEST_VER!") do set "LAT_MAJOR=%%a" & set "LAT_MINOR=%%b" & set "LAT_PATCH=%%c"
if not defined CUR_MAJOR set "CUR_MAJOR=0"
if not defined CUR_MINOR set "CUR_MINOR=0"
if not defined CUR_PATCH set "CUR_PATCH=0"
if not defined LAT_MAJOR set "LAT_MAJOR=0"
if not defined LAT_MINOR set "LAT_MINOR=0"
if not defined LAT_PATCH set "LAT_PATCH=0"

:: 比较主版本号
if !CUR_MAJOR! LSS !LAT_MAJOR! (
    exit /b 1
)
if !CUR_MAJOR! GTR !LAT_MAJOR! (
    exit /b 0
)

:: 比较次版本号
if !CUR_MINOR! LSS !LAT_MINOR! (
    exit /b 1
)
if !CUR_MINOR! GTR !LAT_MINOR! (
    exit /b 0
)

:: 比较修订号
if !CUR_PATCH! LSS !LAT_PATCH! (
    exit /b 1
)

exit /b 0

:check_node_latest_version
set "CUR_NODE_VER=%~1"
if not defined CUR_NODE_VER (
    call :log [WARNING] 无法获取当前 Node.js 版本，跳过版本检查
    exit /b 2
)
call :log [*] 检查 Node.js 最新版本...
call :get_latest_node_version
if not defined NODE_LATEST_VERSION exit /b 2
for /f "tokens=1 delims=v" %%a in ("!CUR_NODE_VER!") do set "CUR_NODE_NUM=%%a"
for /f "tokens=1 delims=v" %%a in ("!NODE_LATEST_VERSION!") do set "LAT_NODE_NUM=%%a"
if not defined LAT_NODE_NUM set "LAT_NODE_NUM=!NODE_LATEST_VERSION!"
call :log     当前版本: v!CUR_NODE_NUM!
call :log     最新版本: !NODE_LATEST_VERSION!
for /f "tokens=1,2,3 delims=." %%a in ("!CUR_NODE_NUM!") do set "CN_MAJ=%%a" & set "CN_MIN=%%b" & set "CN_PAT=%%c"
for /f "tokens=1,2,3 delims=." %%a in ("!LAT_NODE_NUM!") do set "LN_MAJ=%%a" & set "LN_MIN=%%b" & set "LN_PAT=%%c"
if not defined CN_MAJ set "CN_MAJ=0"
if not defined CN_MIN set "CN_MIN=0"
if not defined CN_PAT set "CN_PAT=0"
if not defined LN_MAJ set "LN_MAJ=0"
if not defined LN_MIN set "LN_MIN=0"
if not defined LN_PAT set "LN_PAT=0"
if !CN_MAJ! LSS !LN_MAJ! exit /b 1
if !CN_MAJ! GTR !LN_MAJ! exit /b 0
if !CN_MIN! LSS !LN_MIN! exit /b 1
if !CN_MIN! GTR !LN_MIN! exit /b 0
if !CN_PAT! LSS !LN_PAT! exit /b 1
exit /b 0

:check_python_latest_version
set "CUR_PY_VER_STR=%~1"
if not defined CUR_PY_VER_STR (
    call :log [WARNING] 无法获取当前 Python 版本，跳过版本检查
    exit /b 2
)
call :log [*] 检查 Python 最新版本...
call :get_latest_python_version
if not defined PYTHON_LATEST_VERSION exit /b 2
set "CUR_PY_NUM="
set "PY_CUR_PATTERN=(\d+\.\d+\.\d+)"
for /f "delims=" %%a in ('echo !CUR_PY_VER_STR! ^| powershell -NoProfile -Command "$s = ($input | Out-String).Trim(); if ($s -match $env:PY_CUR_PATTERN) { $matches[1] } else { $s }"') do set "CUR_PY_NUM=%%a"
if not defined CUR_PY_NUM set "CUR_PY_NUM=!CUR_PY_VER_STR!"
for /f "tokens=1,2,3 delims=." %%a in ("!CUR_PY_NUM!") do set "CP_MAJ=%%a" & set "CP_MIN=%%b" & set "CP_PAT=%%c"
for /f "tokens=1,2,3 delims=." %%a in ("!PYTHON_LATEST_VERSION!") do set "LP_MAJ=%%a" & set "LP_MIN=%%b" & set "LP_PAT=%%c"
if not defined CP_MAJ set "CP_MAJ=0"
if not defined CP_MIN set "CP_MIN=0"
if not defined CP_PAT set "CP_PAT=0"
if not defined LP_MAJ set "LP_MAJ=0"
if not defined LP_MIN set "LP_MIN=0"
if not defined LP_PAT set "LP_PAT=0"
call :log     当前版本: !CUR_PY_NUM!
call :log     最新版本: !PYTHON_LATEST_VERSION!
if !CP_MAJ! LSS !LP_MAJ! exit /b 1
if !CP_MAJ! GTR !LP_MAJ! exit /b 0
if !CP_MIN! LSS !LP_MIN! exit /b 1
if !CP_MIN! GTR !LP_MIN! exit /b 0
if !CP_PAT! LSS !LP_PAT! exit /b 1
exit /b 0

:check_git_latest_version
call :get_latest_git_version
if not defined GIT_LATEST_VERSION exit /b 2
set "CUR_GIT_FULL="
for /f "delims=" %%v in ('git --version 2^>nul') do set "CUR_GIT_FULL=%%v"
for /f "tokens=3 delims= " %%a in ("!CUR_GIT_FULL!") do set "CUR_GIT_NUM=%%a"
if not defined CUR_GIT_NUM (
    call :log [WARNING] 无法获取当前 Git 版本，跳过版本检查
    exit /b 2
)
set "CUR_GIT_RAW=!CUR_GIT_NUM!"
set "LAT_GIT_RAW=!GIT_LATEST_VERSION!"
set "CUR_GIT_NUM=!CUR_GIT_RAW:.windows.=.!"
set "LAT_GIT_NUM=!LAT_GIT_RAW:.windows.=.!"
call :log     当前版本: v!CUR_GIT_RAW!
call :log     最新版本: v!LAT_GIT_RAW!
set "CG_MAJ=" & set "CG_MIN=" & set "CG_PAT=" & set "CG_BLD="
set "LG_MAJ=" & set "LG_MIN=" & set "LG_PAT=" & set "LG_BLD="
set "CG_HAS_BLD=0"
for /f "tokens=1,2,3,4 delims=." %%a in ("!CUR_GIT_NUM!") do (
    set "CG_MAJ=%%a"
    set "CG_MIN=%%b"
    set "CG_PAT=%%c"
    set "CG_BLD=%%d"
)
if defined CG_BLD set "CG_HAS_BLD=1"
for /f "tokens=1,2,3,4 delims=." %%a in ("!LAT_GIT_NUM!") do (
    set "LG_MAJ=%%a"
    set "LG_MIN=%%b"
    set "LG_PAT=%%c"
    set "LG_BLD=%%d"
)
if not defined CG_MAJ set "CG_MAJ=0"
if not defined CG_MIN set "CG_MIN=0"
if not defined CG_PAT set "CG_PAT=0"
if not defined CG_BLD set "CG_BLD=0"
if not defined LG_MAJ set "LG_MAJ=0"
if not defined LG_MIN set "LG_MIN=0"
if not defined LG_PAT set "LG_PAT=0"
if not defined LG_BLD set "LG_BLD=0"
if !CG_MAJ! LSS !LG_MAJ! exit /b 1
if !CG_MAJ! GTR !LG_MAJ! exit /b 0
if !CG_MIN! LSS !LG_MIN! exit /b 1
if !CG_MIN! GTR !LG_MIN! exit /b 0
if !CG_PAT! LSS !LG_PAT! exit /b 1
if !CG_PAT! GTR !LG_PAT! exit /b 0
if not "!CG_HAS_BLD!"=="1" exit /b 0
if !CG_BLD! LSS !LG_BLD! exit /b 1
exit /b 0

:install_cloudflared
call :log [*] 安装 cloudflared...
if not exist "%~dp0tools\cloudflared\windows" mkdir "%~dp0tools\cloudflared\windows"
set "CFD_TARGET=%~dp0tools\cloudflared\windows\cloudflared.exe"
set "CFD_TAG="
for /f "delims=" %%v in ('powershell -NoProfile -Command "(Invoke-RestMethod -Uri 'https://api.github.com/repos/cloudflare/cloudflared/releases/latest' -Headers @{'User-Agent'='xy_ws'}).tag_name" 2^>nul') do if not defined CFD_TAG set "CFD_TAG=%%v"
if not defined CFD_TAG (
    call :log [WARNING] 无法从 GitHub 获取 cloudflared 最新版本
    exit /b 1
)
set "CFD_URL=https://github.com/cloudflare/cloudflared/releases/download/!CFD_TAG!/cloudflared-windows-amd64.exe"
call :log [*] 下载 cloudflared !CFD_TAG! (windows-amd64)...
powershell -NoProfile -Command "try { Invoke-WebRequest -Uri '!CFD_URL!' -OutFile '!CFD_TARGET!' -UseBasicParsing } catch { exit 1 }" 2>nul
if errorlevel 1 (
    call :log [WARNING] cloudflared 下载失败
    exit /b 1
)
set "CFD_DL_VER="
for /f "delims=" %%v in ('"!CFD_TARGET!" --version 2^>nul') do if not defined CFD_DL_VER set "CFD_DL_VER=%%v"
call :log [*] cloudflared 安装成功: !CFD_DL_VER!
exit /b 0

:check_cloudflared_latest_version
call :log [*] 检查 cloudflared 最新版本...
set "CFD_LATEST_VER="
for /f "delims=" %%v in ('powershell -NoProfile -Command "(Invoke-RestMethod -Uri 'https://api.github.com/repos/cloudflare/cloudflared/releases/latest' -Headers @{'User-Agent'='xy_ws'}).tag_name" 2^>nul') do if not defined CFD_LATEST_VER set "CFD_LATEST_VER=%%v"
if not defined CFD_LATEST_VER (
    call :log [WARNING] 无法从 GitHub 获取 cloudflared 最新版本信息，跳过升级检查
    exit /b 2
)
set "CFD_LATEST_VER=!CFD_LATEST_VER:v=!"
call :log     当前版本: !CFD_VER!
call :log     最新版本: !CFD_LATEST_VER!
if not "!CFD_VER!"=="!CFD_LATEST_VER!" exit /b 1
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
        set "NPM_TEST_TIME="
        set "NPM_INT_TIME="
        set "NPM_HTTP_CODE="
        call :log     测试 !NPM_NAME!...
        
        for /f "tokens=1,2 delims=:" %%c in ('curl.exe -s -I -o NUL -w "%%{http_code}:%%{time_total}" --connect-timeout 5 --max-time 8 "!NPM_URL!" 2^>nul') do (
            set "NPM_HTTP_CODE=%%c"
            set "NPM_TEST_TIME=%%d"
        )
        
        if defined NPM_HTTP_CODE if not "!NPM_HTTP_CODE!"=="000" if not "!NPM_HTTP_CODE!"=="0000" if defined NPM_TEST_TIME (
            if not "!NPM_TEST_TIME!"=="0" if not "!NPM_TEST_TIME!"=="0.000000" (
                for /f "delims=" %%m in ('powershell -NoProfile -Command "[int]([double]!NPM_TEST_TIME!*1000)" 2^>nul') do set "NPM_INT_TIME=%%m"
            )
        )
        
        if defined NPM_INT_TIME (
            call :log         !NPM_NAME!: !NPM_TEST_TIME!秒 [!NPM_INT_TIME!ms]
            if !NPM_INT_TIME! LSS !NPM_MIN_TIME! (
                set "NPM_MIN_TIME=!NPM_INT_TIME!"
                set "NPM_BEST_MIRROR=!NPM_URL!"
                set "NPM_BEST_NAME=!NPM_NAME!"
            )
        ) else (
            call :log         !NPM_NAME!: 超时/失败
        )
    )
)

if "!NPM_BEST_MIRROR!"=="" (
    call :log [WARNING] NPM镜像测试失败，强制使用淘宝源（范式规定：禁止官方源）
    set "FASTEST_NPM_MIRROR=https://registry.npmmirror.com"
    call npm config set registry "!FASTEST_NPM_MIRROR!"
    call :log [*] NPM镜像已设置为: !FASTEST_NPM_MIRROR!

    call :log [*] 持久化NPM镜像到系统环境变量...
    setx NPM_CONFIG_REGISTRY "!FASTEST_NPM_MIRROR!" >nul 2>&1
    call :log     已写入系统环境变量: NPM_CONFIG_REGISTRY=!FASTEST_NPM_MIRROR!
) else (
    set "FASTEST_NPM_MIRROR=!NPM_BEST_MIRROR!"
    call :log_blank
    call :log [*] 最快NPM镜像: !NPM_BEST_NAME! [!NPM_MIN_TIME!毫秒]
    
    call npm config set registry "!NPM_BEST_MIRROR!"
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

    call :log [*] 检测本地 Playwright 浏览器驱动...
    call :check_and_fix_playwright
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

netstat -ano | findstr ":!WEB_PORT!.*LISTENING" >nul 2>&1
if not errorlevel 1 (
    call :log [WARNING] 端口 !WEB_PORT! 已被占用，正在强制释放...
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":!WEB_PORT!.*LISTENING"') do taskkill /F /PID %%a >nul 2>&1
    ping -n 4 127.0.0.1 >nul 2>&1
)
netstat -ano | findstr ":!WEB_PORT!.*LISTENING" >nul 2>&1
if not errorlevel 1 (
    call :log [ERROR] 端口 !WEB_PORT! 仍被其他进程占用，已中止启动以避免端口冲突循环
    call :log [ERROR] 请手动关闭占用该端口的进程，或设置 WEB_PORT 环境变量使用其他端口
    pause
    exit /b 1
)

call :ms_timestamp
call :log [!TIMESTAMP!] === Web服务启动 ===

:: 检查是否使用守护进程模式（默认启用）
if not defined USE_WATCHDOG_DAEMON set "USE_WATCHDOG_DAEMON=1"

if "!USE_WATCHDOG_DAEMON!"=="1" (
    call :log [*] 内置看门狗守护模式（main.py --watchdog）启动中...
    start /b cmd /c "call "!VENV_PATH!\Scripts\activate.bat" && python main.py --watchdog --web --port !WEB_PORT!" < nul
) else (
    call :log [*] 使用标准模式启动Web服务...
    start /b cmd /c "call "!VENV_PATH!\Scripts\activate.bat" && python main.py --web --port !WEB_PORT!" < nul
)

call :log 等待 Web 服务启动完成...
ping -n 2 127.0.0.1 >nul 2>&1

set "FLASK_WAIT_COUNT=0"
if "!USE_WATCHDOG_DAEMON!"=="1" (
    set "FLASK_MAX_WAIT=120"
) else (
    set "FLASK_MAX_WAIT=60"
)

:wait_flask
set /a FLASK_WAIT_COUNT+=1
if !FLASK_WAIT_COUNT! gtr !FLASK_MAX_WAIT! (
    call :log [ERROR] Web服务启动超时
    goto :wait_loop_entry
)
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s --connect-timeout 3 -m 5 -o NUL -w "%%{http_code}" http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
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
    for /f "delims=" %%i in ('powershell -NoProfile -Command "Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -match '^(192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.)' -and $_.InterfaceAlias -notmatch '(vEthernet|WSL|Docker|VMware|VirtualBox|Loopback|Tailscale|ZeroTier)' } | Select-Object -First 1 -ExpandProperty IPAddress" 2^>nul') do (
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

set "HEALTH_CHECK_INTERVAL=30"

if "!USE_WATCHDOG_DAEMON!"=="1" (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [*] 内置看门狗守护模式（main.py --watchdog），跳过脚本层看门狗
    call :ms_timestamp
    call :log [!TIMESTAMP!] [*] 守护进程模式下运行中... (按 Ctrl+C 停止)
    call :log_blank
) else (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [*] 脚本层看门狗已启动 (每!HEALTH_CHECK_INTERVAL!秒探活)
)

:wait_loop_entry
set "CHECK_INTERVAL=60"
set "CHECK_COUNTER=0"
set "HEALTH_CHECK_INTERVAL=30"
set "HEALTH_COUNTER=0"
set "HEALTH_FAIL_COUNT=0"
set "HEALTH_MAX_FAILS=3"
set "HEARTBEAT_SUCCESS_COUNT=0"
set "HEARTBEAT_MILESTONE=60"
set /a HEARTBEAT_MINUTES=HEARTBEAT_MILESTONE*HEALTH_CHECK_INTERVAL/60
set "WEB_RESTART_COUNT=0"
set "WEB_MAX_RESTARTS=10"
set "WEB_RESTART_COOLDOWN=10"
set "DAEMON_MISS_COUNT=0"

:wait_loop
ping -n 2 127.0.0.1 >nul 2>&1
set /a CHECK_COUNTER+=1
set /a HEALTH_COUNTER+=1
if !CHECK_COUNTER! geq !CHECK_INTERVAL! (
    set "CHECK_COUNTER=0"
    call :check_temp_size
)
if !HEALTH_COUNTER! geq !HEALTH_CHECK_INTERVAL! (
    set "HEALTH_COUNTER=0"
    if "!USE_WATCHDOG_DAEMON!"=="1" (
        call :check_daemon_alive
    ) else (
        call :check_web_health_enhanced
    )
)
goto wait_loop

:check_web_health_enhanced
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s -o NUL -w "%%{http_code}" --connect-timeout 3 --max-time 5 http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
if not defined HTTP_CODE set "HTTP_CODE=000"

if "!HTTP_CODE!"=="200" (
    if !HEALTH_FAIL_COUNT! gtr 0 (
        call :ms_timestamp
        call :log [!TIMESTAMP!] [看门狗] ✅ Web服务恢复正常 (此前连续!HEALTH_FAIL_COUNT!次失败)
    )
    set "HEALTH_FAIL_COUNT=0"
    set /a HEARTBEAT_SUCCESS_COUNT+=1
    if !HEARTBEAT_SUCCESS_COUNT! geq !HEARTBEAT_MILESTONE! (
        set "HEARTBEAT_SUCCESS_COUNT=0"
        call :ms_timestamp
        call :log [!TIMESTAMP!] [看门狗] 💚 心跳健康 - 已连续运行!HEARTBEAT_MINUTES!分钟无异常
    )
    goto :eof
)

if "!HTTP_CODE!"=="302" (
    if !HEALTH_FAIL_COUNT! gtr 0 (
        call :ms_timestamp
        call :log [!TIMESTAMP!] [看门狗] ✅ Web服务恢复正常 (此前连续!HEALTH_FAIL_COUNT!次失败)
    )
    set "HEALTH_FAIL_COUNT=0"
    set /a HEARTBEAT_SUCCESS_COUNT+=1
    if !HEARTBEAT_SUCCESS_COUNT! geq !HEARTBEAT_MILESTONE! (
        set "HEARTBEAT_SUCCESS_COUNT=0"
        call :ms_timestamp
        call :log [!TIMESTAMP!] [看门狗] 💚 心跳健康 - 已连续运行!HEARTBEAT_MINUTES!分钟无异常
    )
    goto :eof
)

set /a HEALTH_FAIL_COUNT+=1
set "HEARTBEAT_SUCCESS_COUNT=0"
call :ms_timestamp
call :log [!TIMESTAMP!] [看门狗] ❌ Web服务异常 (HTTP !HTTP_CODE!, 连续第!HEALTH_FAIL_COUNT!次失败, 每!HEALTH_CHECK_INTERVAL!秒探活一次)

if !HEALTH_FAIL_COUNT! geq !HEALTH_MAX_FAILS! (
    call :restart_web_server_enhanced
)
goto :eof

:restart_web_server_enhanced
if !WEB_RESTART_COUNT! geq !WEB_MAX_RESTARTS! (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [看门狗] ⚠️  已达到最大重启次数(!WEB_MAX_RESTARTS!)，停止自动重启
    set "HEALTH_FAIL_COUNT=0"
    goto :eof
)
set /a WEB_RESTART_COUNT+=1
call :ms_timestamp
call :log [!TIMESTAMP!] [看门狗] 🔄 检测到Web服务异常，执行全面清理并重启... (第!WEB_RESTART_COUNT!次/最多!WEB_MAX_RESTARTS!次)
call :kill_all_interfering_processes
ping -n 3 127.0.0.1 >nul 2>&1
call :ms_timestamp
call :log [!TIMESTAMP!] [看门狗] ⏳ 冷却!WEB_RESTART_COOLDOWN!秒后重启...
ping -n !WEB_RESTART_COOLDOWN! 127.0.0.1 >nul 2>&1
call :ms_timestamp
call :log [!TIMESTAMP!] [看门狗] 🚀 正在重新启动Web服务...
call "!VENV_PATH!\Scripts\activate.bat"
start /b cmd /c "call "!VENV_PATH!\Scripts\activate.bat" && python main.py --web --port !WEB_PORT!" < nul
call :ms_timestamp
call :log [!TIMESTAMP!] [看门狗] ⏱️  等待Web服务启动...
set "RESTART_WAIT=0"
set "RESTART_MAX_WAIT=60"
:restart_wait_loop_enhanced
set /a RESTART_WAIT+=1
if !RESTART_WAIT! gtr !RESTART_MAX_WAIT! (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [看门狗] ⚠️  Web服务重启后启动超时
    goto restart_wait_done_enhanced
)
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s -o NUL -w "%%{http_code}" --connect-timeout 3 --max-time 5 http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
if not defined HTTP_CODE set "HTTP_CODE=000"
if not "!HTTP_CODE!"=="200" if not "!HTTP_CODE!"=="302" (
    ping -n 1 127.0.0.1 >nul 2>&1
    goto restart_wait_loop_enhanced
)
call :ms_timestamp
call :log [!TIMESTAMP!] [看门狗] ✅ Web服务重启成功 (第!WEB_RESTART_COUNT!次重启, 心跳计数器已重置)
:restart_wait_done_enhanced
set "HEALTH_FAIL_COUNT=0"
set "HEARTBEAT_SUCCESS_COUNT=0"
goto :eof

:restart_web_server
if !WEB_RESTART_COUNT! geq !WEB_MAX_RESTARTS! (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [AutoRestart] 已达到最大重启次数(!WEB_MAX_RESTARTS!)，停止自动重启
    set "HEALTH_FAIL_COUNT=0"
    goto :eof
)
set /a WEB_RESTART_COUNT+=1
call :ms_timestamp
call :log [!TIMESTAMP!] [AutoRestart] Web服务崩溃，准备自动重启... (第!WEB_RESTART_COUNT!次/最多!WEB_MAX_RESTARTS!次)
call :kill_all_interfering_processes
ping -n 3 127.0.0.1 >nul 2>&1
call :ms_timestamp
call :log [!TIMESTAMP!] [AutoRestart] 冷却!WEB_RESTART_COOLDOWN!秒后重启...
ping -n !WEB_RESTART_COOLDOWN! 127.0.0.1 >nul 2>&1
call :ms_timestamp
call :log [!TIMESTAMP!] [AutoRestart] 正在重新启动Web服务...
call "!VENV_PATH!\Scripts\activate.bat"
start /b cmd /c "call "!VENV_PATH!\Scripts\activate.bat" && python main.py --web --port !WEB_PORT!" < nul
call :ms_timestamp
call :log [!TIMESTAMP!] [AutoRestart] 等待Web服务启动...
set "RESTART_WAIT=0"
set "RESTART_MAX_WAIT=60"
:restart_wait_loop
set /a RESTART_WAIT+=1
if !RESTART_WAIT! gtr !RESTART_MAX_WAIT! (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [AutoRestart] Web服务重启后启动超时
    goto restart_wait_done
)
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s -o NUL -w "%%{http_code}" --connect-timeout 3 --max-time 5 http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
if not defined HTTP_CODE set "HTTP_CODE=000"
if not "!HTTP_CODE!"=="200" if not "!HTTP_CODE!"=="302" (
    ping -n 1 127.0.0.1 >nul 2>&1
    goto restart_wait_loop
)
call :ms_timestamp
call :log [!TIMESTAMP!] [AutoRestart] Web服务重启成功 (第!WEB_RESTART_COUNT!次重启)
:restart_wait_done
set "HEALTH_FAIL_COUNT=0"
goto :eof

:check_daemon_alive
set "DAEMON_COUNT=0"
for /f "delims=" %%c in ('powershell -NoProfile -Command "@(Get-CimInstance Win32_Process ^| Where-Object { $_.Name -eq 'python.exe' -and $_.CommandLine -like '*main.py*' -and $_.CommandLine -like '*--watchdog*' }).Count" 2^>nul') do set "DAEMON_COUNT=%%c"
if not defined DAEMON_COUNT set "DAEMON_COUNT=0"
if !DAEMON_COUNT! gtr 0 (
    set "DAEMON_MISS_COUNT=0"
    goto :eof
)
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s -o NUL -w "%%{http_code}" --connect-timeout 3 --max-time 5 http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
if not defined HTTP_CODE set "HTTP_CODE=000"
if "!HTTP_CODE!"=="200" (
    set "DAEMON_MISS_COUNT=0"
    goto :eof
)
if "!HTTP_CODE!"=="302" (
    set "DAEMON_MISS_COUNT=0"
    goto :eof
)
set /a DAEMON_MISS_COUNT+=1
call :ms_timestamp
call :log [!TIMESTAMP!] [DaemonGuard] ⚠️  未检测到守护进程 (连续第!DAEMON_MISS_COUNT!次)
if !DAEMON_MISS_COUNT! lss 2 goto :eof
call :restart_watchdog_daemon
goto :eof

:restart_watchdog_daemon
set "DAEMON_MISS_COUNT=0"
if !WEB_RESTART_COUNT! geq !WEB_MAX_RESTARTS! (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [DaemonGuard] ⚠️  已达到最大重启次数(!WEB_MAX_RESTARTS!)，停止自动重启
    goto :eof
)
set /a WEB_RESTART_COUNT+=1
call :ms_timestamp
call :log [!TIMESTAMP!] [DaemonGuard] 🔄 守护进程已退出，准备重新拉起... (第!WEB_RESTART_COUNT!次/最多!WEB_MAX_RESTARTS!次)
call :kill_all_interfering_processes
ping -n 3 127.0.0.1 >nul 2>&1
call :ms_timestamp
call :log [!TIMESTAMP!] [DaemonGuard] ⏳ 冷却!WEB_RESTART_COOLDOWN!秒后重启...
ping -n !WEB_RESTART_COOLDOWN! 127.0.0.1 >nul 2>&1
call :ms_timestamp
call :log [!TIMESTAMP!] [DaemonGuard] 🚀 正在重新启动守护进程...
call "!VENV_PATH!\Scripts\activate.bat"
start /b cmd /c "call "!VENV_PATH!\Scripts\activate.bat" && python main.py --watchdog --web --port !WEB_PORT!" < nul
call :ms_timestamp
call :log [!TIMESTAMP!] [DaemonGuard] ⏱️  等待Web服务启动...
set "RESTART_WAIT=0"
set "RESTART_MAX_WAIT=60"
:restart_wait_loop_daemon
set /a RESTART_WAIT+=1
if !RESTART_WAIT! gtr !RESTART_MAX_WAIT! (
    call :ms_timestamp
    call :log [!TIMESTAMP!] [DaemonGuard] ⚠️  Web服务启动超时，继续监控
    goto restart_wait_done_daemon
)
set "HTTP_CODE="
for /f "delims=" %%i in ('curl.exe -s -o NUL -w "%%{http_code}" --connect-timeout 3 --max-time 5 http://localhost:!WEB_PORT! 2^>nul') do set "HTTP_CODE=%%i"
if not defined HTTP_CODE set "HTTP_CODE=000"
if not "!HTTP_CODE!"=="200" if not "!HTTP_CODE!"=="302" (
    ping -n 1 127.0.0.1 >nul 2>&1
    goto restart_wait_loop_daemon
)
call :ms_timestamp
call :log [!TIMESTAMP!] [DaemonGuard] ✅ Web服务已就绪
:restart_wait_done_daemon
set "HEALTH_FAIL_COUNT=0"
set "HEARTBEAT_SUCCESS_COUNT=0"
goto :eof

:check_temp_size
call :get_dir_size temp
set "LIMIT_SIZE=3145728"
if !TOTAL_SIZE! gtr !LIMIT_SIZE! (
    rd /s /q temp >nul 2>&1
    mkdir temp >nul 2>&1
    call :log_console_only [AUTO] temp目录超过3MB，已完全清空（删除所有文件和子文件夹）
)
goto :eof

:cleanup_exit
call :log_blank
call :log 正在清理进程...
call :kill_process_safe python.exe main.py
call :kill_process_safe hostc.exe
call :kill_process_safe cloudflared.exe
call :kill_browser_processes
call :kill_playwright_processes
call :log 清理完成
goto :eof