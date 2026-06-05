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

call :cleanup_exit >nul 2>&1

goto detect_python

:cleanup_exit
echo.
echo 正在清理进程...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im node.exe >nul 2>&1
echo 清理完成
goto :eof

:detect_python
echo.
echo ========================================
echo 环境检测与配置
echo ========================================
echo [1/5] 检测Python环境...

where py >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python环境检测失败
    echo.
    echo 请先安装Python 3.10或更高版本：
    echo   下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python版本：
py --version
goto detect_venv

:detect_venv
echo [2/5] 检测虚拟环境...

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
    set VENV_PATH=
)
goto setup_venv

:setup_venv
echo [3/5] 设置虚拟环境...

if %VENV_EXISTS%==0 (
    echo 正在创建虚拟环境...
    py -m venv .venv
    if errorlevel 1 (
        echo ERROR: 创建虚拟环境失败
        pause
        exit /b 1
    )
    set VENV_PATH=.venv
    set VENV_EXISTS=1
)

if not exist %VENV_PATH% (
    echo ERROR: 虚拟环境路径不存在：%VENV_PATH%
    pause
    exit /b 1
)

call %VENV_PATH%\Scripts\activate.bat

if exist requirements.txt (
    echo 正在安装依赖...

    echo [*] 检测pip镜像源配置...
    set PIP_CONFIG_FILE=%VENV_PATH%\pip_config\pip.ini

    if not exist "%VENV_PATH%\pip_config\pip.ini" (
        echo [*] 检测到未配置pip镜像源，正在测试镜像源速度...
        if not exist "%VENV_PATH%\pip_config" mkdir "%VENV_PATH%\pip_config"

        set FASTEST_MIRROR=https://mirrors.aliyun.com/pypi/simple/
        set FASTEST_HOST=mirrors.aliyun.com
        set FASTEST_NAME=阿里云
        set MIN_TIME=999999

        echo [*] 测试镜像源 1/5: 阿里云
        for /f "delims=" %%T in ('%VENV_PATH%\Scripts\python.exe -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('\''https://mirrors.aliyun.com/pypi/simple/'\'', timeout=3); print(round(time.time()-start, 3))" 2^>nul') do (
            if not "%%T"=="" (
                set "MIN_TIME=%%T"
                set "FASTEST_NAME=阿里云"
                echo [*] 阿里云速度: %%T秒
            )
        )
        if "!MIN_TIME!"=="999999" (
            set "FASTEST_MIRROR=https://mirrors.aliyun.com/pypi/simple/"
            set "FASTEST_HOST=mirrors.aliyun.com"
            set "FASTEST_NAME=阿里云"
        )

        echo [*] 测试镜像源 2/5: 清华
        for /f "delims=" %%T in ('%VENV_PATH%\Scripts\python.exe -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('\''https://pypi.tuna.tsinghua.edu.cn/simple/'\'', timeout=3); print(round(time.time()-start, 3))" 2^>nul') do (
            if not "%%T"=="" (
                if %%T lss !MIN_TIME! (
                    set "MIN_TIME=%%T"
                    set "FASTEST_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/"
                    set "FASTEST_HOST=pypi.tuna.tsinghua.edu.cn"
                    set "FASTEST_NAME=清华"
                    echo [*] 清华速度: %%T秒 ^(新最快^)
                ) else (
                    echo [*] 清华速度: %%T秒
                )
            )
        )

        echo [*] 测试镜像源 3/5: 腾讯云
        for /f "delims=" %%T in ('%VENV_PATH%\Scripts\python.exe -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('\''https://mirrors.cloud.tencent.com/pypi/simple/'\'', timeout=3); print(round(time.time()-start, 3))" 2^>nul') do (
            if not "%%T"=="" (
                if %%T lss !MIN_TIME! (
                    set "MIN_TIME=%%T"
                    set "FASTEST_MIRROR=https://mirrors.cloud.tencent.com/pypi/simple/"
                    set "FASTEST_HOST=mirrors.cloud.tencent.com"
                    set "FASTEST_NAME=腾讯云"
                    echo [*] 腾讯云速度: %%T秒 ^(新最快^)
                ) else (
                    echo [*] 腾讯云速度: %%T秒
                )
            )
        )

        echo [*] 测试镜像源 4/5: 中科大
        for /f "delims=" %%T in ('%VENV_PATH%\Scripts\python.exe -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('\''https://mirrors.ustc.edu.cn/pypi/simple/'\'', timeout=3); print(round(time.time()-start, 3))" 2^>nul') do (
            if not "%%T"=="" (
                if %%T lss !MIN_TIME! (
                    set "MIN_TIME=%%T"
                    set "FASTEST_MIRROR=https://mirrors.ustc.edu.cn/pypi/simple/"
                    set "FASTEST_HOST=mirrors.ustc.edu.cn"
                    set "FASTEST_NAME=中科大"
                    echo [*] 中科大速度: %%T秒 ^(新最快^)
                ) else (
                    echo [*] 中科大速度: %%T秒
                )
            )
        )

        echo [*] 测试镜像源 5/5: 豆瓣
        for /f "delims=" %%T in ('%VENV_PATH%\Scripts\python.exe -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('\''https://pypi.douban.com/simple/'\'', timeout=3); print(round(time.time()-start, 3))" 2^>nul') do (
            if not "%%T"=="" (
                if %%T lss !MIN_TIME! (
                    set "MIN_TIME=%%T"
                    set "FASTEST_MIRROR=https://pypi.douban.com/simple/"
                    set "FASTEST_HOST=pypi.douban.com"
                    set "FASTEST_NAME=豆瓣"
                    echo [*] 豆瓣速度: %%T秒 ^(新最快^)
                ) else (
                    echo [*] 豆瓣速度: %%T秒
                )
            )
        )

        if not defined FASTEST_MIRROR set "FASTEST_MIRROR=https://mirrors.aliyun.com/pypi/simple/"
        if not defined FASTEST_HOST set "FASTEST_HOST=mirrors.aliyun.com"
        if not defined FASTEST_NAME set "FASTEST_NAME=阿里云"

        echo [*] 最终选择最快镜像源: !FASTEST_NAME!
        (
            echo [global]
            echo index-url = %FASTEST_MIRROR%
            echo [install]
            echo trusted-host = %FASTEST_HOST%
        ) > "%VENV_PATH%\pip_config\pip.ini"
    )

    %VENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt --disable-pip-version-check -q

    echo [*] 测试Playwright CDN速度...

    set FASTEST_PW_CDN=
    set FASTEST_PW_CDN_NAME=
    set MIN_PW_TIME=999999

    set PW_CDN_1=npmmirror
    set PW_URL_1=https://npmmirror.com/mirrors/playwright/
    set PW_CDN_2=azureedge
    set PW_URL_2=https://playwright.azureedge.net/builds/
    set PW_CDN_3=cdn
    set PW_URL_3=https://cdn.playwright.dev/

    for %%A in (1,2,3) do (
        set CDN_NAME=!PW_CDN_%%A!
        set CDN_URL=!PW_URL_%%A!
        echo     测试 !CDN_NAME!...
        for /f "delims=" %%T in ('%VENV_PATH%\Scripts\python.exe -c "import urllib.request, time; start=time.time(); urllib.request.urlopen('\''!CDN_URL!'\'', timeout=3); print(round(time.time()-start, 3))" 2^>nul') do (
            if not "%%T"=="" (
                echo     !CDN_NAME!: %%T秒
                if %%T lss !MIN_PW_TIME! (
                    set "MIN_PW_TIME=%%T"
                    set "FASTEST_PW_CDN=!CDN_URL!"
                    set "FASTEST_PW_CDN_NAME=!CDN_NAME!"
                )
            ) else (
                echo     !CDN_NAME!: 失败
            )
        )
    )

    if not defined FASTEST_PW_CDN (
        echo [WARNING] 所有Playwright CDN均无法访问，将尝试默认安装
    ) else (
        echo [*] 最终选择最快Playwright CDN: !FASTEST_PW_CDN_NAME! ^(!MIN_PW_TIME!秒^)
    )

    echo [*] 安装Playwright浏览器...
    %VENV_PATH%\Scripts\python.exe main.py --install-playwright
)

echo 虚拟环境设置完成
goto check_config

:check_config
echo [4/5] 检测配置文件...

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