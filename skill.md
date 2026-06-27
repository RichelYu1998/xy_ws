# 项目代码规范与范式 (Skill)

> 本文档基于 xy_ws 项目提炼，可作为同类 Python + Flask + 原生JS 全栈项目的二开模版。

---

## 一、项目结构规范

```
项目根目录/
├── main.py                    # 后端主程序（爬虫 + Web 服务，单文件架构）
├── index.html                 # 前端单页面（内联 CSS + JS，无构建工具）
├── run.bat                    # Windows 启动脚本
├── run.sh                     # Linux/Mac 启动脚本
├── requirements.txt           # Python 依赖
├── README.md                  # 项目文档（含版本号，程序自动解析）
├── skill.md                   # 代码规范文档（本文件）
├── config/                    # 配置文件目录
│   ├── config.json            # 主配置（运行时生成）
│   ├── config.json.example    # 配置模板（首次运行自动复制）
│   ├── cookies.json           # Cookie 存储
│   └── cookies.json.example   # Cookie 模板
├── file/                      # 数据文件目录
│   ├── output.json            # 爬虫输出
│   ├── tunnel_url.txt         # 隧道公网地址
│   └── web_output.log         # Web 日志
├── dist/                      # 前端构建产物（iframe 嵌入的独立应用）
│   ├── index.html
│   ├── assets/
│   └── ...
└── .venv/                     # 虚拟环境（自动创建）
```

### 核心原则

1. **单文件后端**：所有 Python 逻辑集中在 `main.py`，通过类和函数组织模块
2. **单文件前端**：`index.html` 包含所有 HTML/CSS/JS，无构建工具依赖
3. **配置与代码分离**：`config/` 存放配置，`file/` 存放运行时数据
4. **模板机制**：`.example` 文件作为配置模板，首次运行自动复制为正式配置

---

## 二、后端 Python 规范

### 2.1 统一异常体系

所有业务异常继承自 `AppException`，按分类工厂方法创建：

```python
class AppException(Exception):
    CATEGORY_FILE = 'FILE'
    CATEGORY_NETWORK = 'NETWORK'
    CATEGORY_AUTH = 'AUTH'
    CATEGORY_BROWSER = 'BROWSER'
    CATEGORY_PARSE = 'PARSE'
    CATEGORY_CONFIG = 'CONFIG'
    CATEGORY_EXCEL = 'EXCEL'
    CATEGORY_EMAIL = 'EMAIL'
    CATEGORY_PERMISSION = 'PERMISSION'
    CATEGORY_RESOURCE = 'RESOURCE'
    CATEGORY_VALIDATION = 'VALIDATION'
    CATEGORY_DATABASE = 'DATABASE'

    def __init__(self, message, category=None, code=None, details=None):
        self.message = message
        self.category = category or 'APP'
        self.code = code or self._CATEGORY_CODES.get(self.category, 'APP_ERROR')
        self.details = details or {}
        super().__init__(self.message)

    @classmethod
    def file_error(cls, message, file_path=None, operation=None, **kwargs):
        details = {'file_path': file_path, 'operation': operation}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_FILE, details=details)

    @classmethod
    def network_error(cls, message, url=None, status_code=None, **kwargs):
        details = {'url': url, 'status_code': status_code}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_NETWORK, details=details)

    def to_dict(self):
        return {
            'error': self.__class__.__name__,
            'category': self.category,
            'code': self.code,
            'message': self.message,
            'details': self.details
        }
```

**使用示例**：

```python
# 抛出异常
raise AppException.file_error("配置文件不存在", file_path=config_path, operation='read')

# 捕获并转换
try:
    ...
except PermissionError as e:
    raise AppException.permission_error(
        f"文件操作失败（权限不足）",
        path=file_path,
        operation='write'
    ) from e
```

### 2.2 异常处理装饰器

为不同操作类型提供专用装饰器，自动捕获标准异常并转换为 `AppException`：

```python
@file_operation_handler(operation='读取')
def read_config(path):
    with open(path, 'r') as f:
        return f.read()

@network_handler(url='https://api.example.com')
def fetch_data(url):
    return urllib.request.urlopen(url)

@excel_handler(operation='读取货号')
def load_excel(file_path):
    return openpyxl.load_workbook(file_path)

@json_handler(context='解析配置')
def parse_config(text):
    return json.loads(text)
```

### 2.3 安全调用工具函数

```python
# 返回默认值（异常时返回 None）
result = safe_call(load_data, default=[])

# 返回 (结果, 错误信息) 元组
result, error = safe_call_with_error(fetch_api, url)

# 上下文管理器方式
with ExceptionContext("读取配置文件", default={}) as ctx:
    config = json.load(f)

# 装饰器方式
@exception_handler(context="发送邮件", default=False)
def send_email(to, subject, body):
    ...
```

### 2.4 跨平台环境类

使用静态类统一管理跨平台差异，避免散落的 `if platform.system()` 判断：

```python
class Environment:
    SYSTEM = platform.system()
    IS_WINDOWS = SYSTEM == 'Windows'
    IS_MAC = SYSTEM == 'Darwin'
    IS_LINUX = SYSTEM == 'Linux'

    @staticmethod
    def get_venv_python():
        if Environment.IS_WINDOWS:
            return os.path.join(PROJECT_DIR, '.venv', 'Scripts', 'python.exe')
        else:
            return os.path.join(PROJECT_DIR, '.venv', 'bin', 'python')

    @staticmethod
    def get_chrome_path():
        if Environment.IS_WINDOWS:
            return None  # Windows 使用 Playwright 内置浏览器
        elif Environment.IS_MAC:
            return '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        elif Environment.IS_LINUX:
            if os.path.exists('/chrome-linux64/chrome'):
                return '/chrome-linux64/chrome'
            return '/usr/bin/google-chrome'

    @staticmethod
    def kill_process_by_name(process_name):
        if Environment.IS_WINDOWS:
            subprocess.run(f'taskkill /F /IM {process_name}', shell=True, capture_output=True, timeout=10)
        else:
            subprocess.run(f'pkill -f "{process_name}"', shell=True, capture_output=True, timeout=10)

### 2.4.1 启动脚本环境检测规范

启动脚本（`run.bat` / `run.sh`）必须实现6步环境检测流程，确保零配置启动：

#### 检测流程

```
[1/6] Python 环境检测 → [2/6] Node.js/NVM 检测 → [3/6] PIP 镜像源测速
→ [4/6] NPM 镜像源测速 → [5/6] 虚拟环境管理 → [6/6] 依赖安装
```

#### Python 环境检测 + 全自动安装（跨平台）

**检测流程**：
```
PATH 搜索 → 常见路径扫描 → 自动安装（包管理器/直接下载）→ 验证安装结果
```

**Windows (BAT)** - 4层全自动安装回退：
```batch
:: 第1步：PATH 搜索（优先级最高）
where py >nul 2>&1 && set "PYTHON_CMD=py"
where python >nul 2>&1 && set "PYTHON_CMD=python"

:: 第2步：常见安装路径搜索（PATH 找不到时）
if not defined PYTHON_CMD (
    if exist "C:\Python3*\python.exe" ( ... )
    else if exist "C:\Program Files\Python3*\python.exe" ( ... )
    else if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python3*\python.exe" ( ... )
)

:: 第3步：全自动安装（4种方式按优先级尝试）
if not defined PYTHON_CMD (
    :: 方式1：Winget（推荐，Win10 1709+ 内置）
    where winget >nul 2>&1 && (
        winget install Python.Python.3 --accept-package-agreements --accept-source-agreements --silent
    )
    
    :: 方式2：Chocolatey（企业常用）
    where choco >nul 2>&1 || (
        choco install python -y
    )
    
    :: 方式3：Scoop（开发者友好）
    where scoop >nul 2>&1 || (
        scoop install python
    )
    
    :: 方式4：直接下载 MSI（最终回退，安装到 _python/ 临时目录）
    curl -L -o "%TEMP%\python_installer.exe" https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    "%TEMP%\python_installer.exe" /quiet InstallAllUsers=0 PrependPath=0 Include_pip=1 TargetDir="%CD%\_python"
)

:: 第4步：验证安装结果
:python_verify_install
if not defined PYTHON_CMD (
    where py >nul 2>&1 && set "PYTHON_CMD=py"
    where python >nul 2>&1 && set "PYTHON_CMD=python"
)
```

**Unix (SH)** - 按操作系统自动选择包管理器：
```bash
# 第1步：PATH 搜索（优先级最高）
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
fi

# 第2步：常见安装路径搜索（PATH 找不到时）
if [ -z "$PYTHON_CMD" ]; then
    COMMON_PYTHON_PATHS=(
        "/usr/bin/python3"
        "/usr/local/bin/python3"
        "/opt/homebrew/bin/python3"
        "$HOME/.pyenv/shims/python3"
    )
    for py_path in "${COMMON_PYTHON_PATHS[@]}"; do
        if [ -x "$py_path" ]; then
            PYTHON_CMD="$py_path"
            break
        fi
    done
fi

# 第3步：全自动安装（根据操作系统选择包管理器）
if [ -z "$PYTHON_CMD" ]; then
    case "$(uname -s)" in
        Darwin)  # macOS
            command -v brew &>/dev/null && brew install python
            [ -f "/opt/homebrew/bin/brew" ] && /opt/homebrew/bin/brew install python
            ;;
        Linux)
            command -v apt-get &>/dev/null && sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip
            command -v yum &>/dev/null && sudo yum install -y python3 python3-pip
            command -v dnf &>/dev/null && sudo dnf install -y python3 python3-pip
            command -v pacman &>/dev/null && sudo pacman -Syu --noconfirm python python-pip
            ;;
    esac
fi

# 第4步：验证安装结果
command -v python3 &>/dev/null && PYTHON_CMD="python3"
command -v python &>/dev/null && PYTHON_CMD="python"
```

#### Node.js/NVM 检测（跨平台）

**Windows (BAT)**:
```batch
:: 1. PATH 搜索
where node >nul 2>&1

:: 2. NVM 检测与自动安装 LTS
if errorlevel 1 (
    if exist "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" (
        call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" install lts
        call "%USERPROFILE%\AppData\Roaming\nvm\nvm.exe" use lts
    ) else (
        :: 3. MSI 下载安装到临时目录
        echo [*] 正在下载 Node.js...
        curl -L -o node.msi https://nodejs.org/dist/v20.11.0/node-v20.11.0-x64.msi
        msiexec /i node.msi INSTALLDIR="%CD%\.node_env" /quiet /norestart
        set "PATH=%CD%\.node_env;%PATH%"
    )
)
```

**Unix (SH)**:
```bash
# 1. PATH 搜索
if ! command -v node &>/dev/null; then
    # 2. NVM 检测与自动安装 LTS
    if [ -s "$HOME/.nvm/nvm.sh" ]; then
        source "$HOME/.nvm/nvm.sh"
        nvm install --lts
        nvm use --lts
    else
        # 3. 包管理器自动安装
        case "$(uname -s)" in
            Darwin)
                brew install node
                ;;
            Linux)
                if command -v apt-get &>/dev/null; then
                    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
                    sudo apt-get install -y nodejs
                elif command -v yum &>/dev/null; then
                    curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
                    sudo yum install -y nodejs
                fi
                ;;
        esac
    fi
fi
```

**关键规则**：
- ✅ 所有路径使用动态变量（`%USERNAME%`, `$HOME`, `%CD%`, `$(pwd)`），禁止硬编码用户名或绝对路径
- ✅ 操作系统检测使用标准 API（`platform.system()`, `uname -s`），禁止硬编码平台字符串
- ✅ 进程管理自动适配（Windows: `taskkill`, Unix: `pkill`）
- ✅ 虚拟环境路径动态获取（Windows: `Scripts\activate.bat`, Unix: `bin/activate`）
- ✅ pip 配置文件格式自适应（Windows: `.ini`, Unix: `.conf`）

### 2.4.2 镜像源测速规范

PIP 和 NPM 镜像源必须通过轮询测速选择最优源，禁止硬编码单一镜像。

#### PIP 镜像源列表

| 镜像名称 | URL | 适用场景 |
|----------|-----|----------|
| 清华源 | `https://pypi.tuna.tsinghua.edu.cn/simple` | 教育网 |
| 阿里云 | `https://mirrors.aliyun.com/pypi/simple/` | 全国 CDN |
| 豆瓣 | `https://pypi.douban.com/simple/` | 稳定可靠 |
| 中科大 | `https://pypi.mirrors.ustc.edu.cn/simple/` | 华南地区 |

#### 测速方法（毫秒级精度）

**使用 curl 测试 TCP 连接时间**（推荐，速度快10倍以上）：

```batch
:: Windows BAT
curl -s -o nul -w "%%{time_connect}" --connect-timeout 1.5 --max-time 2 "!MIRROR_URL!" > temp_time.txt
set /p TEST_TIME=<temp_time.txt

:: 转换为毫秒整数（修复 delims=.0 的 bug）
for /f "tokens=* delims=" %%t in ('%PYTHON_CMD% -c "print(int(float('!TEST_TIME!')*1000))"') do set "INT_TIME=%%t"

:: 选择最小值
if !INT_TIME! LSS !MIN_TIME! (
    set "MIN_TIME=!INT_TIME!"
    set "BEST_MIRROR=!MIRROR_URL!"
)
```

```bash
# Unix SH
TEST_TIME=$(curl -s -o /dev/null -w "%{time_connect}" --connect-timeout 1.5 --max-time 2 "$MIRROR_URL")

# 转换为毫秒整数
INT_TIME=${TEST_TIME%%.*}
INT_TIME=${INT_TIME#0}  # 去掉前导零

# 选择最小值
if [ "$INT_TIME" -lt "$MIN_TIME" ]; then
    MIN_TIME=$INT_TIME
    BEST_MIRROR="$MIRROR_URL"
fi
```

**❌ 禁止使用的旧方法**（Python urllib，速度慢）：
```python
# 错误示例：速度慢（每个镜像需要3秒+）
import urllib.request, time
start = time.time()
urllib.request.urlopen(mirror_url, timeout=3)
elapsed = time.time() - start
```

#### NPM 镜像源列表

| 镜像名称 | URL | 特点 |
|----------|-----|------|
| npmmirror淘宝 | `https://registry.npmmirror.com` | 国内同步快 |
| 官方源 | `https://registry.npmjs.org` | 全球 CDN |

#### 配置文件生成

**Windows**: `.venv/pip_config/pip.ini`
```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
timeout = 120
```

**Unix**: `.venv/pip_config/pip.conf`
```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
timeout = 120
```

**NPM 设置**：
```bash
npm config set registry https://registry.npmmirror.com
```

#### 回退机制

所有镜像测试失败时，回退到官方源：

```batch
if "!BEST_MIRROR!"=="" (
    echo [WARNING] 所有镜像测试失败，使用默认PyPI源
    set "FASTEST_MIRROR=https://pypi.org/simple/"
) else (
    set "FASTEST_MIRROR=!BEST_MIRROR!"
    echo [*] 最快镜像: !BEST_NAME! (!MIN_TIME!毫秒)
)
```

#### 性能要求

- **连接超时**: 1.5秒（`--connect-timeout 1.5`）
- **总超时**: 2秒（`--max-time 2`）
- **总测速时间**: <8秒（4个 PIP 镜像 + 2个 NPM 镜像）
- **显示精度**: 毫秒级（如"中科大 29ms"）
- **测速方法**: 必须使用 `curl %{time_connect}`（TCP连接时间），禁止使用完整HTTP请求

### 2.5 路径管理类

所有路径通过 `PathManager` 静态方法获取，禁止硬编码路径：

```python
class PathManager:
    @staticmethod
    def get_config_dir():
        return os.path.join(PROJECT_DIR, 'config')

    @staticmethod
    def get_config_file():
        return os.path.join(PathManager.get_config_dir(), 'config.json')

    @staticmethod
    def get_output_file():
        return os.path.join(PROJECT_DIR, 'file', 'output.json')

    @staticmethod
    def ensure_dirs_exist():
        dirs = [PathManager.get_config_dir(), PathManager.get_file_dir()]
        for dir_path in dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
```

### 2.6 配置管理类

懒加载 + 自动保存，对外提供 `get/set` 接口：

```python
class ConfigManager:
    def __init__(self, config_path=None):
        self.config_path = config_path or PathManager.get_config_file()
        self._config = None

    @property
    def config(self):
        if self._config is None:
            self._config = self._load_config()
        return self._config

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        if self._config is not None:
            self._config[key] = value
            self.save_config()
```

### 2.7 文件操作类

统一文件读写，内建异常上下文：

```python
class FileManager:
    @staticmethod
    def read_json(file_path):
        with ExceptionContext(f"FileManager.read_json({file_path})", default=None):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)

    @staticmethod
    def write_json(file_path, data, indent=2):
        with ExceptionContext(f"FileManager.write_json({file_path})", default=False):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
            return True
```

### 2.8 Flask API 路由规范

#### 路由命名

| 类型 | 前缀 | 示例 |
|------|------|------|
| 页面 | `/` | `@app.route('/')` |
| 静态资源 | `/dist/<path:filename>` | `@app.route('/dist/<path:filename>')` |
| 命令执行 | `/run`, `/kill` | `@app.route('/run', methods=['POST'])` |
| 数据 API | `/api/<模块>/<操作>` | `@app.route('/api/sku/compare')` |
| 兜底路由 | `/<path:invalid_path>` | `@app.route('/<path:invalid_path>')` |

#### 响应格式

```python
# 成功响应
return jsonify({'success': True, 'data': result})

# 错误响应（带 HTTP 状态码）
return jsonify({'error': '描述信息'}), 404
return jsonify({'error': str(e), 'detail': traceback.format_exc()}), 500

# 敏感字段脱敏
if config['smtp_password']:
    config['smtp_password'] = '******'
```

#### 静态资源服务（含 gzip）

```python
@app.route('/dist/<path:filename>')
def dist_files(filename):
    file_path = os.path.join(PROJECT_DIR, 'dist', filename)
    if not os.path.isfile(file_path):
        return "File not found", 404

    mimetype_map = {
        '.js': 'application/javascript',
        '.css': 'text/css',
        '.html': 'text/html',
        '.json': 'application/json',
        '.svg': 'image/svg+xml',
        '.woff2': 'font/woff2',
    }
    ext = os.path.splitext(filename)[1].lower()
    mimetype = mimetype_map.get(ext, 'application/octet-stream')

    accept_encoding = request.headers.get('Accept-Encoding', '')
    if 'gzip' in accept_encoding.lower() and ext in ['.js', '.css', '.html', '.json', '.svg']:
        with open(file_path, 'rb') as f:
            content = f.read()
        gzip_content = gzip.compress(content, compresslevel=6)
        response = Response(gzip_content, mimetype=mimetype)
        response.headers['Content-Encoding'] = 'gzip'
        response.headers['Cache-Control'] = 'public, max-age=86400'
        return response

    response = send_file(file_path, mimetype=mimetype)
    response.headers['Cache-Control'] = 'public, max-age=86400'
    return response
```

### 2.9 版本号管理

版本号唯一来源为 `README.md`，程序自动解析：

```python
def get_version_from_readme():
    try:
        readme_path = os.path.join(PROJECT_DIR, 'README.md')
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'###\s+v(\d+\.\d+\.\d+)', content)
        return match.group(1) if match else '0.0.0'
    except:
        return '0.0.0'
```

README 中的格式：`### v3.6.0 (2026-06-11)`

### 2.11 更新日志 API

`/api/changelog` 接口解析 README "最新更新"章节，返回结构化 JSON，支持子条目：

**README 格式**：
```markdown
### v3.6.0 (2026-06-11)
- **分类标题**
  - 子条目1
  - 子条目2
- **另一个分类**
  - 子条目3
```

**API 返回结构**：
```json
{
  "success": true,
  "changelog": [
    {
      "version": "3.6.0",
      "date": "2026-06-11",
      "items": [
        {
          "title": "分类标题",
          "desc": "",
          "sub_items": ["子条目1", "子条目2"]
        },
        {
          "title": "另一个分类",
          "desc": "",
          "sub_items": ["子条目3"]
        }
      ]
    }
  ]
}
```

**解析规则**：
- `## 最新更新` 标记章节开始
- `### v版本号 (日期)` 标记版本边界
- `- **标题**` 匹配顶层条目（支持可选的 ` - 描述` 后缀）
- 缩进的 `- 子条目` 匹配子条目（行首有2+空格或制表符）
- 遇到下一个 `## ` 标题或文件结束则停止解析

### 2.10 日志输出规范

```python
# 控制台 + 文件双输出
def log_print(*args, **kwargs):
    msg = ' '.join(str(a) for a in args)
    print(msg, **kwargs)
    if web_log_file:
        safe_execute_func(
            lambda: open(web_log_file, 'a', encoding='utf-8').write(msg + '\n'),
            context='log_print'
        )

# 日志前缀规范
# [Tunnel]  - 隧道相关
# [Email]   - 邮件相关
# [*]       - 进度提示
# [OK]      - 操作成功
# [WARNING] - 警告
# ERROR:    - 错误
print(f"[Tunnel] 隧道启动成功: {url}")
print(f"[Email] 正在发送邮件通知...")
print(f"[*] 清理临时文件...")
print(f"[OK] config.json 已创建")
```

---

## 三、前端规范

### 3.1 技术栈

- **UI 框架**：Bootstrap 4.6.2
- **图标**：Font Awesome 4.7.0
- **JS**：原生 JavaScript（无框架）
- **HTTP**：原生 `fetch` API
- **字体**：系统字体栈

### 3.2 API 调用模式

```javascript
// GET 请求
fetch('/api/products?t=' + Date.now())
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showToast('加载失败: ' + data.error, 'error');
            return;
        }
        // 处理数据
    });

// POST 请求
fetch('/api/sku/compare/txt', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ stock_numbers: inputText })
})
    .then(response => response.json())
    .then(data => { ... });

// async/await 模式
async function loadServerInfo() {
    try {
        const response = await fetch('/api/server/info');
        const data = await response.json();
        if (data.success) {
            // 处理数据
        }
    } catch (error) {
        console.error('加载失败:', error);
    }
}
```

### 3.3 Toast 提示（替代 alert）

```javascript
function showToast(message) {
    const existing = document.getElementById('copy-toast');
    if (existing) existing.remove();
    const toast = document.createElement('div');
    toast.id = 'copy-toast';
    toast.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);'
        + 'background:#28a745;color:#fff;padding:10px 20px;border-radius:5px;'
        + 'z-index:9999;font-size:14px;';
    toast.innerHTML = '<i class="fa fa-check"></i> ' + message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}
```

### 3.4 响应式设计规范

```css
/* 5 个断点 */
@media (max-width: 575.98px)  { /* 超小屏手机 */ }
@media (max-width: 767.98px)  { /* 小屏平板 */ }
@media (max-width: 991.98px)  { /* 平板/笔记本 */ }
@media (max-width: 1199.98px) { /* 大屏 */ }
@media (min-width: 1200px)    { /* 超大屏 */ }

/* 移动端关键规范 */
/* 1. 触摸友好按钮最小高度 44px（Apple HIG） */
.btn { min-height: 44px; }

/* 2. 输入框字体 16px（防止 iOS 自动缩放） */
input, textarea, select { font-size: 16px; }

/* 3. 导航栏固定顶部 z-index: 9999 */
.navbar { position: fixed; z-index: 9999; }

/* 4. body 顶部留白 56px（导航栏高度） */
body { padding-top: 56px; }
```

### 3.4.1 功能按钮统一样式规范

所有 `.func-btn` 按钮必须大小一致、文字完整显示、内容居中：

```css
/* 桌面端 */
.func-btn {
    width: 12.5rem;          /* 固定宽度，不用 min-width */
    height: 3rem;
    line-height: 2rem;
    font-size: 14px;         /* 统一字号 */
    text-align: center;
    display: inline-flex;    /* flex 居中 */
    align-items: center;
    justify-content: center;
}
.func-btn span {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;                /* 图标与文字间距统一 */
}

/* 移动端 <576px */
@media (max-width: 575.98px) {
    .func-btn {
        width: 10rem;
        height: 2.75rem;
        line-height: 1.75rem;
        font-size: 13px;
    }
}
```

**关键规则**：
- 使用固定 `width` 而非 `min-width`，确保所有按钮等宽
- 禁止 `text-overflow: ellipsis`，按钮文字必须完整显示
- 使用 `inline-flex` + `align-items/justify-content: center` 居中
- 统一 `font-size` 确保文字大小一致
- 宽度需容纳最长按钮文字（如"3. Excel与JSON对比"）

### 3.5 iframe 懒加载模式

```html
<div id="weather-iframe-wrapper" style="position: relative; width: 100%; min-height: 200px;">
    <!-- 加载占位 -->
    <div id="weather-loading" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;
         display: flex; justify-content: center; align-items: center; z-index: 1;">
        <i class="fa fa-cloud-download fa-spin"></i> 正在加载...
    </div>
    <!-- iframe 用 data-src 延迟加载 -->
    <iframe data-src="/dist/index.html"
            style="width: 100%; border: none; opacity: 0;"
            onload="this.style.opacity='1';
                     document.getElementById('weather-loading').style.display='none';">
    </iframe>
</div>

<script>
// 页面加载后激活 iframe
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('iframe[data-src]').forEach(iframe => {
        iframe.src = iframe.dataset.src;
    });
});
</script>
```

### 3.6 全局定时器管理

```javascript
let pollingInterval = null;
let tunnelPollInterval = null;

function clearAllPollingIntervals() {
    if (pollingInterval) { clearInterval(pollingInterval); pollingInterval = null; }
    if (tunnelPollInterval) { clearInterval(tunnelPollInterval); tunnelPollInterval = null; }
}
```

### 3.7 HTML 标签闭合规范

- **自闭合标签**：`<br>`, `<hr>`, `<img>`, `<input>`, `<meta>`, `<link>` 无需 `/>`
- **行内代码**：`<code>` 必须成对闭合，禁止嵌套多余的 `</code>`
- **模板字符串中的 HTML**：innerHTML 赋值时，所有标签必须正确闭合

**错误示例**：
```html
<li>默认使用 <code>hostc</code> 隧道服务</code></li>
```

**正确示例**：
```html
<li>默认使用 <code>hostc</code> 隧道服务</li>
```

### 3.7.1 JavaScript 括号闭合规范

修改代码时必须确保所有花括号 `{}` 和圆括号 `()` 成对闭合。`DOMContentLoaded` 回调闭合错误会导致整个脚本解析失败，所有功能不可用。

**验证方法**：用 `new Function(code)` 检查脚本语法是否合法。

**典型结构**：
```javascript
document.addEventListener('DOMContentLoaded', function() {   // 第1层
    // ... 所有初始化代码 ...
    document.querySelectorAll('.btn-sku-api').forEach(function(btn) {  // 第2层
        btn.onclick = function() {  // 第3层
            if (apiUrl) {  // 第4层
                // ...
            }  // 闭合 if
        };  // 闭合 onclick ← 这3行必须保留！
    });  // 闭合 forEach
});  // 闭合 DOMContentLoaded
```

**v3.7.3 修复的 Bug**：v3.7.1 中 `onclick` 和 `forEach` 的闭合行被误删，导致 `DOMContentLoaded` 回调未闭合，整个页面功能失效。

### 3.8 更新日志 API 规范

`/api/changelog` 接口解析 README "最新更新"章节，返回结构化 JSON，支持子条目：

**README 格式**：
```markdown
### v3.6.0 (2026-06-11)
- **分类标题**
  - 子条目1
  - 子条目2
- **另一个分类**
  - 子条目3
```

**API 返回结构**：
```json
{
  "success": true,
  "changelog": [
    {
      "version": "3.6.0",
      "date": "2026-06-11",
      "items": [
        {
          "title": "分类标题",
          "desc": "",
          "sub_items": ["子条目1", "子条目2"]
        },
        {
          "title": "另一个分类",
          "desc": "",
          "sub_items": ["子条目3"]
        }
      ]
    }
  ]
}
```

**解析规则**：
- `## 最新更新` 标记章节开始
- `### v版本号 (日期)` 标记版本边界
- `- **标题**` 匹配顶层条目（支持可选的 ` - 描述` 后缀）
- 缩进的 `- 子条目` 匹配子条目（行首有2+空格或制表符）
- 遇到下一个 `## ` 标题或文件结束则停止解析
- 前端"最新更新"区域仅展示最新版本的完整更新详情

### 3.9 动态展开行规范

表格中点击某行展开详情时，必须使用动态 DOM 操作，确保详情展开在被点击行的正下方。

**核心原则**：
- **禁止预创建 detail-row**：不在模板中为每个日期预创建展开行（避免同日期多项目行产生重复ID）
- **点击时动态创建**：首次点击时 `document.createElement` 创建 detail-row
- **`rowElement.after()` 定位**：将 detail-row 插入到被点击行的正下方
- **class 替代 ID 选择图标**：同日期多行使用 `querySelectorAll('.detail-toggle-icon')` 统一切换图标

**模板代码**（只生成数据行，不预创建 detail-row）：
```javascript
data.summary.forEach((item, idx) => {
    cardHtml += `
        <tr class="summary-row" data-date="${item.日期}"
            onclick="window.toggleProfitDetail('${item.日期}', this)">
            <td class="action-col">
                <i class="fa fa-plus-circle detail-toggle-icon"
                   style="color: #667eea; cursor: pointer;"></i>
            </td>
            <td>...</td>
        </tr>
    `;
});
```

**展开逻辑**（动态创建 + 定位）：
```javascript
window.toggleProfitDetail = function(dateKey, rowElement) {
    const dateId = dateKey.replace(/-/g, '');
    let detailRow = document.getElementById('detail-row-' + dateId);
    let detailContent = document.getElementById('detail-content-' + dateId);

    const wasVisible = detailRow && detailRow.style.display !== 'none';
    const allRows = document.querySelectorAll(
        '.summary-row[data-date="' + dateKey + '"]'
    );

    if (wasVisible) {
        detailRow.style.display = 'none';
        allRows.forEach(function(row) {
            var icon = row.querySelector('.detail-toggle-icon');
            if (icon) icon.className = 'fa fa-plus-circle detail-toggle-icon';
            row.style.background = '';
        });
    } else {
        if (!detailRow) {
            detailRow = document.createElement('tr');
            detailRow.id = 'detail-row-' + dateId;
            detailRow.style.background = '#fafafa';
            detailRow.innerHTML = '<td colspan="7" style="padding: 0;">'
                + '<div id="detail-content-' + dateId + '" '
                + 'style="padding: 10px; max-height: 300px; overflow-y: auto;">'
                + '</div></td>';
        }
        rowElement.after(detailRow);
        detailContent = document.getElementById('detail-content-' + dateId);
        detailRow.style.display = 'table-row';
        allRows.forEach(function(row) {
            var icon = row.querySelector('.detail-toggle-icon');
            if (icon) icon.className = 'fa fa-minus-circle detail-toggle-icon';
            row.style.background = '#e6f0ff';
        });
        // ... 填充 detailContent ...
    }
};
```

**聚合级别一致性**：
- 按天点击 → 显示月度聚合（`dateKey.substring(0, 7)` + ' 月度聚合'）
- 按月点击 → 显示月度聚合（`dateKey` + ' 月度聚合'，使用 `filteredRecords`）
- 按年点击 → 显示年度聚合（`dateKey` + ' 年度聚合'，使用 `filteredRecords`）
- 聚合数据直接使用当前行的 `filteredRecords`，不重新过滤，确保数据一致性

### 3.10 ECharts 图表与表格联动规范

利润趋势图必须与汇总视图按钮联动，禁止独立按钮控制。

**核心原则**：
- **按钮合并**：利润趋势图不设独立年/月/日按钮，通过汇总视图按钮同步控制图表维度
- **联动提示**：图表标题区域显示"（随汇总视图联动）"提示文字
- **双向联动**：点击图表数据点高亮表格行，点击表格行高亮图表数据点

**模板代码**（图表容器，无独立按钮）：
```html
<div id="profit-chart-container" style="padding: 15px; background: #fff; border-bottom: 2px solid #667eea;">
    <div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-bottom: 10px;">
        <span style="font-weight: 600; color: #333;"><i class="fa fa-bar-chart"></i> 利润趋势图</span>
        <span style="font-size: 12px; color: #999;">（随汇总视图联动）</span>
    </div>
    <div id="profit-chart" style="width: 100%; height: 400px;"></div>
</div>
```

**Y轴动态缩放**：根据数据范围自动调整，不同维度显示合理范围：
```javascript
yAxis: {
    type: 'value',
    axisLabel: {
        formatter: function(v) {
            if (v >= 10000) return (v / 10000).toFixed(1) + '万';
            return v.toFixed(0);
        }
    },
    min: function(value) { return Math.max(0, Math.floor(value.min * 0.9)); },
    max: function(value) { return Math.ceil(value.max * 1.1); }
}
```

**图表高亮联动**（点击表格行 → 高亮图表数据点）：
```javascript
window.highlightChartPoint = function(dateKey) {
    const chart = window._profitChartInstance;
    if (!chart) return;
    const option = chart.getOption();
    const categories = option.xAxis[0].data;
    const currentGroupBy = window._currentGroupBy || 'day';
    let chartKey = dateKey;
    if (currentGroupBy === 'year') chartKey = dateKey.substring(0, 4);
    else if (currentGroupBy === 'month') chartKey = dateKey.substring(0, 7);
    const dataIndex = categories.indexOf(chartKey);
    if (dataIndex === -1) return;
    chart.dispatchAction({ type: 'downplay', seriesIndex: 0 });
    chart.dispatchAction({ type: 'downplay', seriesIndex: 1 });
    chart.dispatchAction({ type: 'downplay', seriesIndex: 2 });
    chart.dispatchAction({ type: 'highlight', seriesIndex: 0, dataIndex: dataIndex });
    chart.dispatchAction({ type: 'highlight', seriesIndex: 1, dataIndex: dataIndex });
    chart.dispatchAction({ type: 'highlight', seriesIndex: 2, dataIndex: dataIndex });
    chart.dispatchAction({ type: 'showTip', seriesIndex: 0, dataIndex: dataIndex });
};
```

**表格行点击事件**（同时触发展开和高亮）：
```javascript
<tr class="summary-row" data-date="${item.日期}"
    onclick="window.toggleProfitDetail('${item.日期}', this);
             window.highlightChartPoint('${item.日期}')">
```

### 3.11 日期格式化规范

`formatDate` 函数必须处理所有可能的日期输入格式，特别是 Excel 日期序列号。

**处理优先级**：
1. `Date` 对象 → 直接格式化
2. `YYYY-MM-DD` 标准格式 → 直接返回
3. `YYYY-MM-DDTHH:mm:ss` ISO格式 → 截取前10位
4. `YYYY/M/D` 斜杠格式 → 补零转换
5. `YYYYMMDD` 紧凑格式 → 插入连字符
6. **数字类型 Excel 日期序列号**（typeof === 'number'，40000-100000）→ Excel epoch 转换
7. **字符串类型 Excel 日期序列号**（纯数字字符串，40000-100000）→ Excel epoch 转换
8. GMT/UTC/HTTP 日期格式 → `new Date()` 解析
9. 其他 → 原样返回

**后端日期预处理**（`table_data` 发送前必须转换）：
```python
for row_data in table_data:
    for col_idx, cell_val in enumerate(row_data):
        if isinstance(cell_val, datetime):
            row_data[col_idx] = cell_val.strftime('%Y-%m-%d')
        elif isinstance(cell_val, (int, float)) and not isinstance(cell_val, bool):
            if cell_val > 40000 and cell_val < 100000:
                try:
                    converted = datetime(1899, 12, 30) + timedelta(days=int(cell_val))
                    if converted.year >= 2000:
                        row_data[col_idx] = converted.strftime('%Y-%m-%d')
                except:
                    pass
```

**后端 `all_records` 年份验证**：
```python
elif isinstance(date_val, (int, float)):
    try:
        record_date = datetime(1899, 12, 30) + timedelta(days=int(date_val))
        if record_date.year < 2000:
            continue  # 拒绝2000年以前的日期
        record_date_str = record_date.strftime('%Y-%m-%d')
    except:
        continue
```

**前端 Excel 日期序列号转换**（必须在 `return str` 之前执行）：
```javascript
// 数字类型优先处理（避免String()转换丢失精度）
if (typeof value === 'number' && value > 40000 && value < 100000) {
    try {
        const excelEpoch = new Date(1899, 11, 30);
        const jsDate = new Date(excelEpoch.getTime() + value * 86400000);
        if (jsDate.getFullYear() >= 2000) {
            const y = jsDate.getFullYear();
            const m = String(jsDate.getMonth() + 1).padStart(2, '0');
            const d = String(jsDate.getDate()).padStart(2, '0');
            return y + '-' + m + '-' + d;
        }
    } catch(e) {}
}
// 字符串类型处理
if (/^\d+$/.test(str) && parseInt(str) > 40000 && parseInt(str) < 100000) {
    try {
        const excelEpoch = new Date(1899, 11, 30);
        const jsDate = new Date(excelEpoch.getTime() + parseInt(str) * 86400000);
        if (jsDate.getFullYear() >= 2000) {
            const y = jsDate.getFullYear();
            const m = String(jsDate.getMonth() + 1).padStart(2, '0');
            const d = String(jsDate.getDate()).padStart(2, '0');
            return y + '-' + m + '-' + d;
        }
    } catch(e) {}
}
return str;
```

**注意事项**：
- 正则表达式必须使用 `/^\d+$/`（带反斜杠），而非 `/^d+$/`
- Excel 日期处理代码必须放在 `return str` 之前，否则永远不会执行
- `padStart` 第二个参数为 `'0'（单个零），而非 `'00'`
- 年份验证阈值 `>= 2000`，拒绝2000年以前的Excel序列号日期
- 后端 `table_data` 必须在 `jsonify` 前预处理日期，避免前端收到datetime对象或原始序列号
- 图表渲染使用 `requestAnimationFrame` 替代 `setTimeout`，确保DOM就绪

---

## 四、启动脚本规范

### 4.1 五步启动流程

`run.bat` 和 `run.sh` 必须保持逻辑一致，遵循以下五步：

```
[1/5] 检测 Python 环境
[2/5] 测速 pip 镜像源
[3/5] 检测虚拟环境
[4/5] 设置虚拟环境 + 安装依赖
[5/5] 检测配置文件
```

### 4.2 关键差异对照

| 功能 | Windows (run.bat) | Linux/Mac (run.sh) |
|------|-------------------|---------------------|
| Python 命令 | `py` | `python3` / `python` |
| 虚拟环境 | `.venv\Scripts\activate.bat` | `source .venv/bin/activate` |
| 进程终止 | `taskkill /F /IM` | `pkill -f` |
| 进程检测 | `tasklist /FI` | `pgrep -f` |
| 睡眠 | `timeout /t 5 /nobreak >nul` | `sleep 5` |
| 环境变量 | `set VAR=value` | `export VAR=value` |
| 后台运行 | `start /b cmd /c "..."` | `command &` |
| 清理 | `del /f /s /q` | `rm -rf` |

### 4.3 版本号读取

两个脚本都从 `README.md` 解析版本号：

```batch
:: Windows
for /f "delims=" %%i in ('py -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')"') do set VERSION=%%i
```

```bash
# Linux/Mac
VERSION=$(python3 -c "import re; m=re.search(r'###\s+v(\d+\.\d+\.\d+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')")
```

### 4.4 临时文件清理

```batch
:: Windows - 检查 temp 目录大小，超过 3MB 则清理
set "LIMIT_SIZE=3145728"
if !TOTAL_SIZE! gtr !LIMIT_SIZE! (
    del /f /s /q temp\*.* >nul 2>&1
)
```

```bash
# Linux/Mac
LIMIT_SIZE=3145728
if [ "$TOTAL_SIZE" -gt "$LIMIT_SIZE" ]; then
    rm -rf temp/*
fi
```

---

## 五、配置文件规范

### 5.1 config.json 结构

```json
{
    "login": { "username": "", "password": "", "login_type": "phone" },
    "target_url": "",
    "scroll_config": {
        "max_attempts": 30,
        "same_height_limit": 8,
        "scroll_wait_time": 0.8,
        "popup_close_interval": 5,
        "dynamic_adjust": true
    },
    "headers": { "user-agent": "..." },
    "cookies": [ { "name": "token", "value": "", "domain": ".example.com" } ],
    "output_file": "file/output.json",
    "cookie_file": "config/cookies.json",
    "excel_files": ["path/to/file1.xlsx", "~/path/to/file2.xlsx"],
    "email_notification_enabled": true,
    "email_smtp_host": "smtp.qq.com",
    "email_smtp_port": 587,
    "email_smtp_user": "",
    "email_smtp_password": "",
    "email_to": ""
}
```

### 5.2 模板机制

- `.example` 文件存放默认值和占位符（如 `YOUR_USERNAME`）
- 首次运行时自动复制为正式配置文件
- 正式配置文件不纳入版本控制（含敏感信息）

---

## 六、隧道与公网访问规范

### 6.1 隧道服务

- 使用 `hostc` 隧道服务（`npx -y hostc@latest`）
- 公网地址写入 `file/tunnel_url.txt`
- 同时同步到 `file/web_output.log`
- Flask 启动后自动启动隧道

### 6.2 邮件通知

- 隧道 URL 变化时自动发送邮件
- 支持 SMTP SSL/TLS
- 敏感字段 API 返回时脱敏
- 邮件发送有冷却时间（60秒）和失败熔断（连续3次失败后冷却5分钟）

---

## 编码风格速查表

### 跨平台规范

| 规范项 | ✅ 正确做法 | ❌ 错误做法 |
|--------|------------|------------|
| 用户目录 | `%USERNAME%` (BAT) / `$HOME` (SH) | `C:\Users\Administrator` / `/home/user` |
| 当前目录 | `%CD%` (BAT) / `$(pwd)` (SH) | `D:\ws\xy_ws` / `/home/user/project` |
| 操作系统检测 | `platform.system()` / `uname -s` | 硬编码 `"Windows"` / `"Linux"` |
| 进程管理 | `taskkill` (Win) / `pkill` (Unix) | 只支持单一平台命令 |
| 虚拟环境激活 | `Scripts\activate.bat` (Win) / `bin/activate` (Unix) | 硬编码单一激活脚本 |
| pip 配置格式 | `.ini` (Win) / `.conf` (Unix) | 硬编码 `.ini` 或 `.conf` |
| 路径分隔符 | `os.path.join()` / 动态变量 | 硬编码 `\` 或 `/` |

### 镜像源测速规范

| 规范项 | ✅ 正确做法 | ❌ 错误做法 |
|--------|------------|------------|
| 测速方法 | `curl %{time_connect}` (TCP连接时间) | Python urllib (完整HTTP请求，慢10倍+) |
| 连接超时 | 1.5秒 (`--connect-timeout 1.5`) | 3秒+ |
| 显示精度 | 毫秒级（如"29ms"） | 秒级（模糊） |
| 字符串解析 | `python -c "print(int(float(t)*1000))"` | `delims=.0` (bug: 删掉所有0和点) |
| 回退机制 | 所有镜像失败时回退官方 PyPI | 直接报错退出 |
| 配置生成 | 写入 `.venv/pip_config/pip.ini或.conf` | 修改全局 pip 配置 |

### 临时环境隔离规范

| 环境 | 目录 | 用途 | 创建条件 |
|------|------|------|----------|
| Python 虚拟环境 | `.venv/` | 隔离 Python 包依赖 | 始终创建 |
| Node.js 临时环境 | `.node_env/` (仅Windows无NVM时) | 隔离 Node.js 运行时 | Windows + 无NVM |
| Python 临时安装 | `_python/` (仅Windows无包管理器时) | Python 全自动安装回退 | Windows + 无winget/choco/scoop |
| PIP 配置 | `.venv/pip_config/pip.ini或.conf` | 项目级镜像源配置 | 始终创建 |

**关键规则**：
- ❌ 禁止修改系统全局 Python/Node.js/NPM 设置
- ✅ 所有配置文件必须放在项目目录内（`.venv/`, `.node_env/`, `_python/`）
- ✅ 启动脚本结束后，临时环境不影响系统全局配置
- ✅ git 忽略规则：`.venv/`, `.node_env/`, `_python/`, `node_modules/`

### Python 全自动安装规范

| 操作系统 | 第1优先级 | 第2优先级 | 第3优先级 | 最终回退 |
|----------|----------|----------|----------|----------|
| Windows | Winget | Chocolatey | Scoop | MSI下载到 `_python/` |
| macOS | Homebrew (Intel) | Homebrew (Apple Silicon) | - | 提示手动安装Homebrew |
| Linux (Ubuntu) | apt | - | - | 提示手动安装 |
| Linux (CentOS) | yum | - | - | 提示手动安装 |
| Linux (Fedora) | dnf | - | - | 提示手动安装 |
| Linux (Arch) | pacman | - | - | 提示手动安装 |

**安装后必须验证**：
```batch
:: Windows
where py >nul 2>&1 && set "PYTHON_CMD=py"
where python >nul 2>&1 && set "PYTHON_CMD=python"
```

```bash
# Unix
command -v python3 &>/dev/null && PYTHON_CMD="python3"
command -v python &>/dev/null && PYTHON_CMD="python"
```

### 性能要求

| 指标 | 要求 | 说明 |
|------|------|------|
| PIP 测速总时间 | <6秒 | 4个镜像 × 1.5秒超时 |
| NPM 测速总时间 | <3秒 | 2个镜像 × 1.5秒超时 |
| 总测速时间 | <8秒 | PIP + NPM 合计 |
| 连接超时 | 1.5秒 | `--connect-timeout 1.5` |
| 总超时 | 2秒 | `--max-time 2` |
| 显示精度 | 毫秒级 | 如"中科大 29ms" |

---

## 七、二开模版示例

### 示例 1：新增一个 API 端点

**需求**：添加 `/api/stats` 接口，返回商品统计信息。

```python
@app.route('/api/stats', methods=['GET'])
def get_stats():
    try:
        output_file = PathManager.get_output_file()
        if not os.path.exists(output_file):
            return jsonify({'error': '数据文件不存在'}), 404

        data = FileManager.read_json(output_file)
        if not data:
            return jsonify({'error': '数据为空'}), 404

        products = data.get('商品列表', []) if isinstance(data, dict) else data
        total = len(products)
        avg_price = sum(float(p.get('价格', 0)) for p in products) / total if total > 0 else 0

        return jsonify({
            'success': True,
            'total_products': total,
            'avg_price': round(avg_price, 2)
        })
    except Exception as e:
        error_detail = str(e) + '\n' + traceback.format_exc()
        print(f'get_stats错误: {error_detail}')
        return jsonify({'error': str(e), 'detail': error_detail}), 500
```

**前端调用**：

```javascript
function loadStats() {
    fetch('/api/stats')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                showToast('加载统计失败: ' + data.error);
                return;
            }
            document.getElementById('stats-total').textContent = data.total_products;
            document.getElementById('stats-avg-price').textContent = '¥' + data.avg_price;
        });
}
```

### 示例 2：新增一个配置项

**需求**：添加 `max_retries` 配置项，控制爬虫重试次数。

1. 在 `config.json.example` 中添加默认值：

```json
{
    "max_retries": 3
}
```

2. 在代码中通过 `ConfigManager` 读取：

```python
config_manager = ConfigManager()
max_retries = config_manager.get('max_retries', 3)
```

3. 前端通过 API 读写：

```python
@app.route('/api/config/max-retries', methods=['GET'])
def get_max_retries():
    config_manager = ConfigManager()
    return jsonify({'success': True, 'value': config_manager.get('max_retries', 3)})

@app.route('/api/config/max-retries', methods=['POST'])
def set_max_retries():
    data = request.get_json()
    value = data.get('value', 3)
    if not isinstance(value, int) or value < 1 or value > 10:
        return jsonify({'error': '重试次数必须在1-10之间'}), 400
    config_manager = ConfigManager()
    config_manager.set('max_retries', value)
    return jsonify({'success': True, 'message': f'重试次数已设置为 {value}'})
```

### 示例 3：新增一个异常分类

**需求**：添加 `PAYMENT` 异常分类。

```python
class AppException(Exception):
    # 在已有分类后添加
    CATEGORY_PAYMENT = 'PAYMENT'

    _CATEGORY_CODES = {
        # ... 已有映射 ...
        CATEGORY_PAYMENT: 'PAYMENT_ERROR',
    }

    @classmethod
    def payment_error(cls, message, order_id=None, amount=None, **kwargs):
        details = {'order_id': order_id, 'amount': amount}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_PAYMENT, details=details)
```

使用：

```python
try:
    process_payment(order)
except PaymentGatewayError as e:
    raise AppException.payment_error(
        f"支付处理失败: {e}",
        order_id=order.id,
        amount=order.amount
    ) from e
```

### 示例 4：新增跨平台路径

**需求**：添加日志归档目录路径。

```python
class PathManager:
    # ... 已有方法 ...

    @staticmethod
    def get_archive_dir():
        return os.path.join(PROJECT_DIR, 'file', 'archive')

    @staticmethod
    def get_archive_file(date_str):
        return os.path.join(PathManager.get_archive_dir(), f'archive_{date_str}.json')

    @staticmethod
    def ensure_dirs_exist():
        dirs = [
            PathManager.get_config_dir(),
            PathManager.get_file_dir(),
            PathManager.get_archive_dir()  # 新增
        ]
        for dir_path in dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
```

### 示例 5：新增前端功能区块

**需求**：添加一个"数据导出"区块。

```html
<section id="export" class="py-5" style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);">
    <div class="container">
        <div class="section-title">
            <h2 style="color: #fff;">数据导出</h2>
            <div class="underline"></div>
        </div>
        <div class="row justify-content-center">
            <div class="col-12 text-center">
                <button class="btn btn-success btn-lg" onclick="exportData('csv')">
                    <i class="fa fa-file-excel-o"></i> 导出 CSV
                </button>
                <button class="btn btn-primary btn-lg ml-3" onclick="exportData('json')">
                    <i class="fa fa-file-code-o"></i> 导出 JSON
                </button>
            </div>
        </div>
    </div>
</section>

<script>
function exportData(format) {
    fetch('/api/export?format=' + format)
        .then(response => {
            if (!response.ok) throw new Error('导出失败');
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'export_' + new Date().toISOString().slice(0, 10) + '.' + format;
            a.click();
            window.URL.revokeObjectURL(url);
            showToast('导出成功');
        })
        .catch(error => showToast('导出失败: ' + error.message));
}
</script>
```

---

## 八、编码风格速查

| 项目 | 规范 |
|------|------|
| Python 版本 | 3.8+ |
| 缩进 | 4 空格 |
| 字符串 | 优先单引号，f-string 格式化 |
| 编码 | 所有文件 UTF-8 |
| 换行 | LF（`.sh`），CRLF/LF 均可（其他文件） |
| JSON 缩进 | 2 空格，`ensure_ascii=False` |
| 文件读写 | 始终指定 `encoding='utf-8'` |
| 异常处理 | 禁止裸 `except`，使用 `AppException` 体系 |
| 路径拼接 | 使用 `os.path.join()`，禁止字符串拼接 |
| 跨平台判断 | 使用 `Environment.IS_WINDOWS` 等，禁止 `platform.system()` 散落 |
| HTTP 请求头 | `user-agent` 和 `sec-ch-ua-platform` 使用 `Environment` 动态获取，禁止硬编码 |
| API 响应 | 成功 `{'success': True, ...}`，失败 `{'error': '...'}` |
| 前端提示 | 使用 `showToast()`，禁止 `alert()` |
| HTML 标签 | `<code>` 等行内标签必须成对闭合，禁止多余 `</code>` |
| JS 括号闭合 | 所有 `{}` `()` 必须成对，修改后用 `new Function(code)` 验证 |
| 功能按钮 | `.func-btn` 固定 `width`，`inline-flex` 居中，禁止 `text-overflow: ellipsis` |
| 动态展开行 | 点击时 `createElement` + `rowElement.after()`，禁止预创建 detail-row |
| 聚合级别 | 按天→月度聚合，按月→月度聚合，按年→年度聚合，使用 `filteredRecords` |
| 图标切换 | 同组多行用 `querySelectorAll('.class')` 统一切换，禁止重复 ID |
| CSS 变量 | 使用 `:root` 定义主题色 |
| 移动端适配 | 5 个断点全覆盖，按钮最小 44px，flex 居中布局，图表高度自适应 |
| 图表联动 | 利润趋势图随汇总视图按钮联动，禁止独立按钮，双向高亮 |
| 日期格式化 | `formatDate` 处理9种格式，数字类型Excel序列号优先于字符串类型 |
| 后端日期预处理 | `table_data` 在 `jsonify` 前转换 datetime 和 Excel 序列号为 `YYYY-MM-DD` |
| 图表渲染 | 使用 `requestAnimationFrame` 替代 `setTimeout`，确保 DOM 就绪 |
| 跨系统兼容 | 所有路径 `os.path.join()`，前端 `window.location.origin`，无硬编码 |
| 版本号 | 唯一来源 `README.md`，格式 `### v3.7.5 (2026-06-26)` |
| 依赖管理 | `requirements.txt`，虚拟环境 `.venv` |
| 进程管理 | Windows: `taskkill`，Linux/Mac: `pkill` |
| 敏感信息 | 配置模板用占位符，API 返回时脱敏 |

---

## 九、skill.docx 生成规范

### 9.1 字体要求

| 类型 | 字体 | XML 属性 |
|------|------|----------|
| 西文（代码/英文） | Consolas | `w:ascii` / `w:hAnsi` |
| 东亚（中文） | 微软雅黑 | `w:eastAsia` |

**关键**：每个 `w:rPr` 下的 `w:rFonts` 必须同时设置 `w:eastAsia`，否则中文显示时字体缺失。

### 9.2 生成流程

1. 从 `skill.md` 逐行解析 Markdown
2. 代码块（` ``` `）用 Consolas 9pt，左缩进 0.3 英寸
3. 表格（`| ... |`）解析为 Word Table Grid，首行加粗
4. 列表项（`- ` / `  - `）用 `•` / `◦` 符号，支持 `**粗体**` 混排
5. 引用（`> `）用斜体灰色
6. 所有 run 都通过 `set_run_font()` 统一设置字体

### 9.3 同步规则

- `skill.md` 是唯一源文件
- 修改 `skill.md` 后必须重新生成 `skill.docx`
- 两个文件一起提交到 git