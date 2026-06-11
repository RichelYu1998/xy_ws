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
```

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

README 中的格式：`### v3.5.7 (2026-06-07)`

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
            alert('加载失败: ' + data.error);
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
| API 响应 | 成功 `{'success': True, ...}`，失败 `{'error': '...'}` |
| 前端提示 | 使用 `showToast()`，禁止 `alert()` |
| CSS 变量 | 使用 `:root` 定义主题色 |
| 移动端适配 | 5 个断点全覆盖，按钮最小 44px |
| 版本号 | 唯一来源 `README.md`，格式 `### v3.5.7 (2026-06-07)` |
| 依赖管理 | `requirements.txt`，虚拟环境 `.venv` |
| 进程管理 | Windows: `taskkill`，Linux/Mac: `pkill` |
| 敏感信息 | 配置模板用占位符，API 返回时脱敏 |