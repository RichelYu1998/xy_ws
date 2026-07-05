# xy_ws - Szwego商品爬虫系统

> **版本**: v3.8.10
> **更新日期**: 2026-07-05
> **技术栈**: Python 3.14 + Flask + 原生JavaScript + Playwright

---

## 📋 项目简介

xy_ws 是一个基于 Python + Flask 的全栈商品爬虫系统，专门用于 Szwego 平台的商品数据采集、对比和管理。项目采用单文件架构设计，具有跨平台支持、智能隧道管理、实时邮件通知等特性。

### ✨ 核心功能

- 🔍 **智能爬虫引擎**: 基于 Playwright 的动态页面抓取，支持智能滚动策略
- 📊 **货号对比系统**: 自动化货号差异检测与报表生成
- 🌐 **公网隧道服务**: Hostc 隧道自动管理与 URL 智能切换
- 📧 **实时邮件通知**: 隧道状态变更、异常告警邮件推送
- 🌍 **跨平台支持**: Windows/Linux/Mac 全平台兼容
- 📱 **响应式前端**: 自适应移动端和桌面端界面
- 🔄 **自动化运维**: 环境检测、依赖安装、服务自愈

---

## 🚀 快速启动

### 环境要求

- **Python**: 3.10+ (推荐 3.14)
- **Node.js**: 18+ (可选，用于前端构建)
- **操作系统**: Windows 10+/Linux/macOS

### 一键启动

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

启动脚本会自动完成：
1. ✅ 工作目录自动切换
2. ✅ Python 环境检测与安装
3. ✅ 虚拟环境创建 (.venv)
4. ✅ 依赖自动安装 (requirements.txt)
5. ✅ Node.js/NVM 环境检测
6. ✅ 镜像源测速与配置
7. ✅ 服务启动 (Flask Web + 爬虫引擎)

---

## 📁 项目结构

```
xy_ws/
├── main.py                    # 后端主程序（爬虫 + Web 服务）
├── index.html                 # 前端单页面应用
├── run.bat                    # Windows 启动脚本
├── run.sh                     # Linux/Mac 启动脚本
├── requirements.txt           # Python 依赖清单
├── readme.md                  # 项目说明文档（本文件）
├── skill.md                   # 代码规范与开发指南
├── skill.docx                 # Word 格式的代码规范文档
├── config/                    # 配置文件目录
│   ├── config.json            # 主配置文件（运行时生成）
│   ├── config.json.example    # 配置模板
│   ├── cookies.json           # Cookie 存储
│   └── cookies.json.example   # Cookie 模板
├── file/                      # 数据文件目录
│   ├── output.json            # 爬虫输出数据
│   ├── tunnel_url.txt         # 隧道公网地址
│   └── web_output.log         # Web 运行日志
├── dist/                      # 前端构建产物
│   ├── index.html
│   └── assets/
└── .venv/                     # Python 虚拟环境
```

---

## 🔧 核心模块说明

### 后端模块 (main.py)

| 模块 | 功能描述 |
|------|----------|
| **AppException** | 统一异常体系，13种异常分类 |
| **ExceptionHandler** | 单例模式异常处理器，错误统计与历史记录 |
| **WegoScraper** | 核心爬虫引擎，Playwright 动态抓取 |
| **StockNumberComparator** | 货号对比算法，智能差异检测 |
| **FileCleaner** | 文件清理系统，多策略清理机制 |
| **EmailNotifier** | 邮件通知服务，SMTP 队列发送 |
| **ConfigManager** | 配置管理器，模板机制 |
| **FileManager** | 文件操作类，安全读写封装 |

### 前端模块 (index.html)

| 功能模块 | 函数数量 | 说明 |
|----------|----------|------|
| 设备检测与适配 | 3 | 移动端/桌面端自适应 |
| 商品展示 | 8 | 商品列表渲染与交互 |
| 视频处理 | 3 | 视频预览与管理 |
| 利润报表 | 8 | ECharts 图表 + 表格联动 |
| 隧道管理 | 5 | 隧道状态监控与控制 |
| 货号对比 | 2 | 实时货号比对 |
| 文件清理 | 2 | 磁盘空间管理 |
| 天气时钟 | 2 | 实时天气时间显示 |

---

## 🌐 API 接口文档

系统提供 33 个 RESTful API 端点，主要分类：

### 爬虫相关
- `POST /api/scrape/start` - 启动爬虫任务
- `POST /api/scrape/stop` - 停止爬虫任务
- `GET /api/scrape/status` - 获取爬虫状态
- `GET /api/products` - 获取商品列表

### 货号对比
- `POST /api/compare/start` - 开始货号对比
- `GET /api/compare/result` - 获取对比结果
- `POST /api/compare/upload` - 上传对比文件

### 隧道管理
- `POST /api/tunnel/start` - 启动隧道服务
- `POST /api/tunnel/stop` - 停止隧道服务
- `GET /api/tunnel/status` - 获取隧道状态
- `GET /api/tunnel/url` - 获取当前隧道URL

### 文件操作
- `POST /api/clean/logs` - 清理日志文件
- `POST /api/clean/cache` - 清理缓存文件
- `POST /api/clean/temp` - 清理临时文件
- `GET /api/disk/usage` - 获取磁盘使用情况

### 系统管理
- `GET /api/system/info` - 系统信息
- `GET /api/config` - 获取配置
- `PUT /api/config` - 更新配置
- `GET /api/logs` - 获取日志
- `GET /api/version` - 版本信息

**完整 API 文档请查看 [skill.md](skill.md) §2.13**

---

## ⚙️ 配置说明

### 主配置文件 (config/config.json)

```json
{
  "scraper": {
    "max_concurrent": 5,
    "scroll_delay": 1.5,
    "timeout": 30
  },
  "tunnel": {
    "auto_restart": true,
    "health_check_interval": 300,
    "max_retries": 3
  },
  "email": {
    "enabled": true,
    "smtp_host": "smtp.qq.com",
    "smtp_port": 465,
    "sender": "your@qq.com",
    "recipients": ["notify@example.com"]
  },
  "server": {
    "host": "0.0.0.0",
    "port": 5000,
    "debug": false
  }
}
```

### 首次运行

首次启动会自动从 `.example` 模板复制配置文件：

```bash
# 自动复制流程
config/config.json.example → config/config.json
config/cookies.json.example → config/cookies.json
```

---

## 📧 邮件通知配置

### QQ邮箱授权码获取

1. 登录 QQ邮箱网页版
2. 进入 设置 → 账户 → POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务
3. 开启 SMTP 服务
4. 生成授权码（16位字符串）

### 配置示例

```python
email_config = {
    'smtp_host': 'smtp.qq.com',
    'smtp_port': 465,
    'use_ssl': True,
    'sender': 'your@qq.com',
    'password': 'xxxxxxxxxxxxxxxx',  # 授权码，非QQ密码
    'recipients': ['admin@example.com']
}
```

---

## 🔒 安全特性

### 异常处理体系

项目实现了完整的异常处理框架：

- **13种异常分类**: FILE, NETWORK, AUTH, BROWSER, PARSE, CONFIG, EXCEL, EMAIL, PERMISSION, RESOURCE, VALIDATION, DATABASE
- **统一异常类**: `AppException` 所有业务异常的基类
- **单例处理器**: `ExceptionHandler` 错误统计和历史记录
- **装饰器模式**: `@exception_handler`, `@file_operation_handler`, `@network_handler`
- **上下文管理器**: `ExceptionContext` with语句方式异常捕获
- **安全调用函数**: `safe_call()`, `safe_call_with_error()`

### 代码规范

项目严格遵循以下编码规范（详见 [skill.md](skill.md)）：

- **PY-STD-001**: Python基础编码规范（PEP 8）
- **PY-STD-002**: 统一异常处理规范
- **PY-STD-003**: 日志输出规范
- **FE-STD-001**: 前端JavaScript编码规范
- **FE-STD-002**: API调用模式规范
- **API-STD-001**: Flask路由命名规范

---

## 🛠️ 开发指南

### 二开模版示例

#### 新增API端点

```python
@app.route('/api/custom/endpoint', methods=['POST'])
@exception_handler(context='自定义接口')
def custom_endpoint():
    data = request.get_json()
    result = safe_call(process_data, data, default={})
    return jsonify({'success': True, 'data': result})
```

#### 新增前端功能

```javascript
async function customFunction() {
    try {
        showLoading('处理中...');
        const response = await fetch('/api/custom/endpoint', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ key: 'value' })
        });
        const result = await response.json();
        if (result.success) {
            showToast('操作成功', 'success');
        } else {
            showToast(result.message, 'error');
        }
    } catch (error) {
        showToast('网络错误', 'error');
    } finally {
        hideLoading();
        resetButtons();
    }
}
```

**更多示例请查看 [skill.md](skill.md) 第七章**

---

## 📊 性能指标

### 爬虫性能
- **并发数**: 可配置（默认5）
- **滚动策略**: 智能滚动，动态延迟
- **超时设置**: 30秒（可配置）
- **内存占用**: < 200MB（正常运行）

### 隧道服务
- **健康检查间隔**: 300秒（5分钟）
- **最大重试次数**: 3次
- **URL去重窗口**: 30分钟
- **自动重启**: 支持

### 邮件通知
- **发送队列**: 异步队列，不阻塞主线程
- **重试机制**: 3次重试，指数退避
- **频率限制**: 同一URL 30分钟内仅发1次

---

## 🐛 故障排查

### 常见问题

**Q1: 启动时报 IndentationError**
```
原因：Python缩进错误（多了/少了空格）
解决：检查 main.py 对应行数的缩进，确保为4的倍数
工具：使用 autopep8 或 black 自动格式化
```

**Q2: 隧道URL无法访问**
```
1. 检查进程：ps aux | grep hostc (Linux) 或 tasklist | findstr hostc (Windows)
2. 测试连通性：curl http://localhost:4040/api/tunnels
3. 查看日志：tail -f file/web_output.log
4. 手动重启：访问 /api/tunnel/restart
```

**Q3: 邮件收不到**
```
1. 检查授权码是否正确（非QQ密码）
2. 确认SMTP服务已开启
3. 测试端口连通性：telnet smtp.qq.com 465
4. 检查垃圾邮件箱
```

**Q4: 依赖安装失败**
```
1. 切换镜像源：pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
2. 升级pip：python -m pip install --upgrade pip
3. 清除缓存：pip cache purge
4. 使用虚拟环境：python -m venv .venv && .venv\Scripts\activate
```

**完整FAQ请查看 [skill.md](skill.md) 附录C**

---

## 📈 更新日志

### v3.8.10 (2026-07-05) - 🔧 关键修复
- **修复致命错误**: 缩进错误导致服务完全无法启动（第6433行）
- **影响范围**: 仅影响 auto_start_tunnel() 函数内的URL验证逻辑
- **修复方案**: 修正缩进从29个空格改为28个空格（符合PEP 8标准）
- **预防措施**: 
  - IDE显示空白字符
  - 启动前执行 python -m py_compile main.py
  - CI/CD集成 flake8 --select=E999 检查

### v3.8.9 (2026-07-05) - 🔒 强制URL去重
- **新增功能**: 同一地址30分钟内只发1次邮件
- **优化项**: 避免邮件轰炸，提升用户体验

### v3.8.8 (2026-07-05) - 🚀 零延迟通知
- **性能优化**: 公网地址可用即自动发邮件
- **响应速度**: 从轮询检测改为事件驱动

### v3.8.7 (2026-07-05) - 🔒 线程安全
- **核心修复**: URL去重机制的并发竞态条件
- **技术方案**: 引入线程锁（threading.Lock）

### v3.8.5 (2026-07-04) - 🌐 隧道优化
- **Hostc集成**: 智能URL读取与切换
- **邮件增强**: 多条件触发机制
- **稳定性提升**: 自动故障恢复

**历史版本更新请查看 [skill.md](skill.md) 最新更新章节**

---

## 📝 代码规范文档

本项目有详细的代码规范文档：

- **[skill.md](skill.md)**: Markdown格式，包含完整的编码规范、API文档、二开模版
- **[skill.docx](skill.docx)**: Word格式，适合打印和离线阅读

### 主要内容

1. **项目结构规范** - 目录组织、核心原则
2. **后端Python规范** - 异常体系、装饰器、工具类、API路由
3. **前端规范** - 技术栈、API调用、响应式设计、按钮状态管理
4. **启动脚本规范** - 六步启动流程、跨平台实现
5. **配置文件规范** - JSON结构、模板机制
6. **隧道与公网访问** - Hostc集成、邮件通知
7. **二开模版示例** - 5个典型场景的完整代码示例
8. **编码风格速查** - 快速参考表

---

## 👥 贡献指南

### 提交代码规范

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 遵循 [skill.md](skill.md) 中的编码规范
4. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
5. 推送到分支 (`git push origin feature/AmazingFeature`)
6. 开启 Pull Request

### 代码质量要求

- ✅ 使用 `AppException` 抛出业务异常
- ✅ 使用 `@exception_handler` 装饰器处理异常
- ✅ 使用 `safe_call()` 进行安全调用
- ✅ 遵循 PEP 8 编码风格
- ✅ 添加必要的注释和文档字符串
- ✅ 确保跨平台兼容性（Windows/Linux/Mac）

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

## 📞 技术支持

- **问题反馈**: 请提交 Issue
- **功能建议**: 欢迎 Pull Request
- **技术咨询**: 查看文档或联系维护者

---

## 🙏 致谢

- **Playwright** - 强大的浏览器自动化框架
- **Flask** - 轻量级Web框架
- **ECharts** - 数据可视化库
- **Hostc** - 公网隧道服务

---

> **最后更新**: 2026-07-05
> **文档版本**: v3.8.10
> **维护者**: xy_ws 开发团队