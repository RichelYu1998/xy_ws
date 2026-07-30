# 微购相册管理系统 (WegoAlbum Manager)

## 📋 项目概述
微购相册商品数据采集与分析系统，用于自动化获取闲鱼平台商品信息并进行数据分析。

---

## 🔄 最新更新

### 🔧 hostc WebSocket 安全关闭修复 — 进程崩溃根因修复

#### 问题: hostc 隧道启动时报错 `WebSocket was closed before the connection was established` 并导致进程崩溃
**现象**: 项目启动时 hostc 隧道尝试建立 WebSocket 连接，超时或失败后调用 `safeCloseWebSocket2` 关闭 socket，触发未捕获的 `error` 事件导致 Node.js 进程崩溃退出

**根本原因**:
1. **`safeCloseWebSocket2` 函数缺陷**: 当 WebSocket 处于 `CONNECTING` 状态时，直接调用 `socket.close()` 会抛异常（`ws` 库规定未完成握手的 socket 必须用 `terminate()` 强制关闭）
2. **超时处理器缺陷**: 超时后调用 `safeCloseWebSocket2` 关闭 socket，但未预先注册 `error` 事件监听器，导致 `close()` 触发的 error 事件无人处理，抛出 `Unhandled 'error' event`

**修复方案**:
```javascript
// ❌ 修复前：超时处理器直接关闭，未处理 error 事件
const timeout = setTimeout(() => {
  cleanup();
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);

// ✅ 修复后：关闭前吞掉 error 事件，防止进程崩溃
const timeout = setTimeout(() => {
  cleanup();
  socket.once("error", () => {});
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);
```

```javascript
// ❌ 修复前：不区分 socket 状态，直接调用 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
  } catch {
    socket.terminate();
  }
}

// ✅ 修复后：CONNECTING 状态用 terminate()，OPEN 状态用 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    if (socket.readyState === import_ws2.default.CONNECTING) {
      socket.once("error", () => {});
      socket.terminate();
    } else {
      socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
    }
  } catch {
    try { socket.terminate(); } catch {}
  }
}
```

**持久化保护**:
- 在 `dist/package.json` 中添加 `patch-package` 作为 `postinstall` 钩子
- 补丁文件 `dist/patches/hostc+1.3.0.patch` 确保 `npm install` 后自动应用修复

**修复效果**:
| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| **hostc 启动** | 进程崩溃 ❌ | 正常启动 ✅ |
| **WebSocket 超时** | Unhandled error ❌ | 优雅关闭 ✅ |
| **补丁持久化** | npm install 后丢失 ❌ | postinstall 自动应用 ✅ |

**技术细节**:
- `ws` 库的 `close()` 方法仅在 `OPEN` 状态下可用，`CONNECTING` 状态必须使用 `terminate()`
- `socket.once("error", () => {})` 用于吞掉因强制关闭而产生的 error 事件
- `patch-package` 确保每次 `npm install` 后补丁自动应用，不会因依赖更新而丢失修复

---

### 🔧 隧道验证修复 — hostc/CF 均不可用的根因修复

#### 问题: 项目启动后 hostc 和 CF 隧道均被判定为"不可用"
**现象**: 项目启动时 hostc 和 Cloudflare Tunnel 都能成功启动并获取到 URL，但心跳验证机制始终判定为不可用，导致反复重启隧道

**根本原因**:
1. **hostc 验证失败**: `verify_url()` 函数使用 HTTP `HEAD` 方法验证 URL，但 FastAPI 根路由 `@app.get('/')` 不支持 HEAD 请求，返回 `405 Method Not Allowed`，导致验证永远失败
2. **CF 验证失败**: 本机 DNS 无法解析 `trycloudflare.com` 域名（`Errno 8: nodename nor servname provided`），属于网络/DNS 配置问题

**修复方案**:
```python
# ❌ 修复前：只支持 GET，HEAD 请求返回 405
@app.get('/')
async def index():

# ✅ 修复后：同时支持 GET 和 HEAD，验证请求正常通过
@app.api_route('/', methods=['GET', 'HEAD'])
async def index():
```

**修复效果**:
| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| **hostc 验证** | 405 Method Not Allowed ❌ | 200 OK ✅ |
| **心跳判定** | 不可用 → 反复重启 ❌ | 可用 → 稳定运行 ✅ |
| **邮件通知** | 发送"不可用"通知 ❌ | 发送"可用"通知 ✅ |

**技术细节**:
- FastAPI 的 `@app.get()` 装饰器不会自动为路由支持 HEAD 方法（与 Flask 不同）
- `verify_url()` 使用 `urllib.request.Request(url, method='HEAD')` 发送 HEAD 请求
- 改用 `@app.api_route('/', methods=['GET', 'HEAD'])` 后，HEAD 请求返回与 GET 相同的响应头（无 body），验证通过

**CF 不可用的额外说明**:
- CF 隧道进程本身启动正常（直接连接 Cloudflare 服务器获取 URL）
- 但本机 DNS 无法解析 `*.trycloudflare.com`，导致验证请求失败
- 建议排查 DNS 设置：`nslookup xxx.trycloudflare.com`，或更换 DNS 为 `8.8.8.8` / `114.114.114.114`

---

### 🎯 高价商品数解析修复 + 按钮失效修复

#### 问题1: 高价商品数显示为0
**现象**: 爬虫日志显示"售价 >= 599 的商品: 78 个"，但界面显示高价商品数为 **0**

**根本原因**: 
- 前端正则表达式无法正确匹配Python输出的格式
- Python输出格式：`售价 >= 599 的商品: 78 个`（有空格）
- 前端正则：`/售价[》>=]+\s*599[^:：]*[:：]\s*(\d+)\s*[个件]/`（无法匹配空格）

**修复方案**:
```javascript
// ✅ 简化正则表达式，直接匹配Python输出格式
if (line.includes('售价') && line.includes('599') && line.includes('商品')) {
    // 主要匹配："售价 >= 599 的商品: 78 个"
    let match = line.match(/售价\s*>=\s*599\s*的商品\s*[:：]\s*(\d+)\s*个/);
    // 备选方案：匹配任意"商品: 数字 个"格式
    if (!match) match = line.match(/商品\s*[:：]\s*(\d+)\s*个/);
    // 最后备选：匹配行末的数字
    if (!match) match = line.match(/(\d+)\s*个\s*$/);
    
    if (match && parseInt(match[1]) > 0) {
        skuData.highPriceCount = match[1];
        console.log('[对比卡片] ✓ 高价商品数:', skuData.highPriceCount);
    }
}
```

**数据流程说明**:
1. **爬虫运行时**：前端解析日志输出实时显示统计数据
2. **爬虫完成后**：前端调用 `/api/products` API获取JSON数据（已包含 `highPriceCount` 字段）

#### 问题2: 8个按钮全部失效
**现象**: 页面加载后所有按钮点击无响应

**根本原因**: 
- `bindAllButtons()` 函数定义在作用域内，不是全局函数
- 外部无法调用，导致按钮事件绑定失败

**修复方案**:
```javascript
// ✅ 暴露为全局函数
window.bindAllButtons = bindAllButtons;
window.resetButtons = resetButtons;
```

### ✅ 修复效果
| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| **高价商品(≥599)** | 0 ❌ | 78 ✅ |
| **按钮响应** | 失效 ❌ | 正常 ✅ |
| **数据显示** | 错误 ❌ | 准确 ✅ |

### 📝 技术细节
- **文件位置**: `dist/app.js` Line 1369-1383, 1441-1453, 2707
- **修复方法**: 
  1. 简化正则表达式，精确匹配Python输出格式
  2. 暴露全局函数，确保按钮绑定成功
- **验证方式**: 
  1. Node.js语法检查通过
  2. 浏览器测试按钮响应正常
  3. 爬虫运行时实时显示正确的统计数据

---

## 📚 历史版本记录

### v3.8.89.11 (2026-07-30) - 🔧 hostc WebSocket安全关闭修复

#### 问题: hostc 隧道启动时报错 `WebSocket was closed before the connection was established` 并导致进程崩溃
**现象**: 项目启动时 hostc 隧道尝试建立 WebSocket 连接，超时或失败后调用 `safeCloseWebSocket2` 关闭 socket，触发未捕获的 `error` 事件导致 Node.js 进程崩溃退出

**根本原因**:
1. **`safeCloseWebSocket2` 函数缺陷**: 当 WebSocket 处于 `CONNECTING` 状态时，直接调用 `socket.close()` 会抛异常（`ws` 库规定未完成握手的 socket 必须用 `terminate()` 强制关闭）
2. **超时处理器缺陷**: 超时后调用 `safeCloseWebSocket2` 关闭 socket，但未预先注册 `error` 事件监听器，导致 `close()` 触发的 error 事件无人处理，抛出 `Unhandled 'error' event`

**修复方案**:
```javascript
// ❌ 修复前：超时处理器直接关闭，未处理 error 事件
const timeout = setTimeout(() => {
  cleanup();
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);

// ✅ 修复后：关闭前吞掉 error 事件，防止进程崩溃
const timeout = setTimeout(() => {
  cleanup();
  socket.once("error", () => {});
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);
```

```javascript
// ❌ 修复前：不区分 socket 状态，直接调用 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
  } catch {
    socket.terminate();
  }
}

// ✅ 修复后：CONNECTING 状态用 terminate()，OPEN 状态用 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    if (socket.readyState === import_ws2.default.CONNECTING) {
      socket.once("error", () => {});
      socket.terminate();
    } else {
      socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
    }
  } catch {
    try { socket.terminate(); } catch {}
  }
}
```

**持久化保护**:
- 在 `dist/package.json` 中添加 `patch-package` 作为 `postinstall` 钩子
- 补丁文件 `dist/patches/hostc+1.3.0.patch` 确保 `npm install` 后自动应用修复

**修复效果**:
| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| **hostc 启动** | 进程崩溃 ❌ | 正常启动 ✅ |
| **WebSocket 超时** | Unhandled error ❌ | 优雅关闭 ✅ |
| **补丁持久化** | npm install 后丢失 ❌ | postinstall 自动应用 ✅ |

**技术细节**:
- `ws` 库的 `close()` 方法仅在 `OPEN` 状态下可用，`CONNECTING` 状态必须使用 `terminate()`
- `socket.once("error", () => {})` 用于吞掉因强制关闭而产生的 error 事件
- `patch-package` 确保每次 `npm install` 后补丁自动应用，不会因依赖更新而丢失修复

### v3.8.89.10 (2026-07-30) - 🔧 隧道验证修复(hostc/CF均不可用)
- **🔧 HEAD验证修复** - FastAPI根路由添加HEAD方法支持，修复verify_url()返回405导致隧道被误判不可用
- **📝 DNS排查指引** - CF隧道DNS解析失败的排查方案
- **✅ 心跳稳定** - 隧道不再反复重启，邮件通知正常发送

### v3.8.89.9 (2026-07-30) - 🎯 高价商品数解析修复+按钮失效修复
- **🎯 高价商品数解析修复** - 简化正则表达式，精确匹配Python输出格式
- **🔘 按钮失效修复** - 暴露全局函数，确保按钮绑定成功
- **✅ 数据显示** - 高价商品数从0恢复到78

### v3.8.89.8 (2026-07-30) - 🔧 FastAPI迁移问题修复
- **🔧 FastAPI迁移修复** - 高价商品、TXT对比、请求处理、数据源、CDN日志
- **✅ 功能恢复** - 修复FastAPI迁移后的功能问题

### v3.8.89.6 (2026-07-30) - 🐛 爬虫结果卡片格式统一修复
- **🐛 格式统一** - 修复爬虫结果卡片显示格式
- **✅ UI优化** - 统一卡片显示样式

### v3.8.89.5 (2026-07-30) - 📊 代码质量完美优化
- **📊 单元测试** - 添加单元测试
- **📝 日志优化** - 日志级别优化
- **🔧 subprocess替换** - subprocess替换os.system
- **💡 Toast提示** - 前端Toast错误提示

### v3.8.89.4 (2026-07-30) - 🐛 全面隐藏Bug修复+代码质量提升
- **🐛 Bug修复** - 修复多个隐藏Bug
- **📈 代码质量** - 提升代码质量

### v3.8.89.3 (2026-07-29) - 🔧 Flask遗留代码修复+jsonify兼容层
- **🔧 Flask修复** - 修复Flask遗留代码
- **📊 jsonify兼容** - 添加jsonify兼容层
- **✅ 按钮测试** - 8个按钮测试7/8通过

### v3.8.89.2 (2026-07-29) - 🚀 FastAPI迁移100%完成
- **🚀 FastAPI迁移** - 22个路由全部转换
- **✅ 100%完成** - FastAPI迁移100%完成

### v3.8.89.1 (2026-07-29) - 🐛 修复Excel对比货号点击无响应
- **🐛 Excel对比修复** - 修复Excel对比货号点击无响应
- **📝 文档更新** - 更新文档规范

### v3.8.88.2 (2026-07-29) - 🔒 深度安全加固
- **🔒 XSS全面修复** - XSS全面修复(26处)
- **🌐 CORS收紧** - CORS收紧
- **🔐 URL注入防护** - URL注入防护
- **🐛 紧急Bug修复** - 事件绑定缺失导致商品详情和利润报表功能失效

### v3.8.88.1 (2026-07-29) - 🔐 额外安全加固
- **🔐 XSS防护** - XSS防护
- **⏰ 定时器泄漏修复** - 定时器泄漏修复

### v3.8.88 (2026-07-29) - 🔒 全面修复'Unexpected token <'错误
- **🔒 API路由安全加固** - API路由安全加固
- **🐛 错误修复** - 全面修复'Unexpected token <'错误

### v3.8.87 (2026-07-26) - 🕐 商品详情入库时间实时计算修复
- **🕐 实时计算** - 基于入库时间戳动态计算相对时间
- **✅ 不再使用静态字符串** - 不再使用源API静态字符串

### v3.8.86 (2026-07-26) - 📊 商品搜索多表联动+分表统计
- **📊 多表联动** - 搜索时4个表格联动过滤
- **📈 分表统计** - 每个表格独立统计行(售出总价/均价/手续费)
- **🏷️ 徽章更新** - 顶部徽章实时更新匹配数
- **🎨 彩色标签** - 搜索结果分表展示彩色标签

### v3.8.85 (2026-07-26) - 📊 商品搜索统计实时计算优化
- **📊 实时计算** - 商品搜索统计实时计算优化

### v3.8.84 (2026-07-25) - 🔒 安全漏洞修复+命令注入防护
- **🔒 安全漏洞修复** - 安全漏洞修复
- **🔐 命令注入防护** - 命令注入防护

### v3.8.83 (2026-07-25) - 🐛 Bug修复+代码质量提升
- **🐛 Bug修复** - Bug修复
- **📈 代码质量** - 代码质量提升

### v3.8.82 (2026-07-24) - 🔧 代码质量优化
- **🔧 代码质量** - 代码质量优化

### v3.8.81 (2026-07-24) - 🐛 变量命名规范化修复
- **🐛 变量命名** - 变量命名规范化(oldTime -> old_time)
- **🕐 字段修复** - 修复时间戳字段(time_stamp)

### v3.8.78 (2026-07-20) - 📄 skill.docx自动生成+文档更新
- **📄 自动生成** - skill.docx自动生成
- **📝 文档更新** - 文档更新

### v3.8.77 (2026-07-20) - 📊 Swagger UI集成优化
- **📊 Swagger UI** - Swagger UI集成优化

### v3.8.76 (2026-07-20) - 🔧 .trae配置优化+skill文档更新
- **🔧 .trae配置** - .trae配置优化
- **📝 skill文档** - skill文档更新

### v3.8.75 (2026-07-20) - 📚 skill文档+代码规范优化
- **📚 skill文档** - 新增skill文档
- **📈 代码规范** - 代码规范优化

### v3.8.73 (2026-07-19) - 🔒 CSP优化+README.md更新
- **🔒 CSP优化** - CSP优化，docs/目录允许CDN
- **📝 README更新** - README.md更新，补充v3.8.67-v3.8.73版本记录
- **📊 changelog API** - 新增/api/changelog API

### v3.8.71 (2026-07-19) - 📊 Swagger UI集成+Pydantic V2升级
- **📊 Swagger UI** - Swagger UI集成(自动生成swagger.json+HTML UI)
- **📈 Pydantic V2** - Pydantic V2升级(field_validator)
- **📝 requirements.txt** - 更新requirements.txt

### v3.8.70 (2026-07-19) - 🏢 企业级生产优化
- **🏢 企业级优化** - 企业级生产优化，38项改进
- **🔒 安全加固** - 安全加固

### v3.8.69 (2026-07-19) - 🔒 全面安全审计
- **🔒 安全审计** - 全面安全审计，7个关键Bug修复

### v3.8.68 (2026-07-19) - 🐛 关键Bug修复
- **🐛 缩进错误** - 修复缩进错误
- **🔌 Socket泄漏** - 修复Socket泄漏
- **📈 代码质量** - 代码质量提升

### v3.8.67 (2026-07-19) - 🐛 FastAPI迁移Bug修复
- **🐛 FastAPI迁移** - 修复FastAPI迁移后的Bug

### v3.8.66 (2026-07-18) - 🧪 CF独立性测试验证+Bug修复
- **🧪 实测验证** - 手动触发hostc进程终止测试
- **🐛 Bug修复** - 修复verify_url()参数错误
- **✅ 稳定性提升** - hostc频繁崩溃场景下CF隧道完全独立运行

### v3.8.65 (2026-07-18) - 🔒 CF隧道独立性优化+智能复用机制
- **🔒 CF隧道独立** - hostc失效不再影响Cloudflare Tunnel
- **🔄 智能复用** - 启动新CF隧道前先检查已有可用地址
- **✅ 减少重启** - hostc频繁重启时CF地址保持不变

### v2.1.9 (历史版本) - 🔧 代码精炼优化
- **🔧 代码精炼** - 代码精炼优化，简化逻辑提升可维护性

### v2.1.8 (历史版本) - 📊 滚动加载策略优化
- **📊 滚动加载** - 优化滚动加载策略，采用激进模式快速加载所有数据

### v2.1.7 (历史版本) - ⏰ 多重超时保护
- **⏰ 超时保护** - 添加多重超时保护和重试机制，防止爬虫卡死

### v2.1.6 (历史版本) - 🐛 弹窗关闭超时修复
- **🐛 弹窗修复** - 修复弹窗关闭超时问题
- **📊 时间统计** - 添加时间统计优化性能

### v2.1.5 (历史版本) - 🐛 高价商品筛选修复
- **🐛 筛选修复** - 修复高价商品筛选逻辑
- **✅ 对比准确** - 解决对比结果不准确问题

### v2.1.3 (历史版本) - 📊 JSON文件对比优化
- **📊 对比优化** - 优化JSON文件对比记录机制
- **📝 多条记录** - 支持多条对比记录

### v2.1.2 (历史版本) - 📊 JSON文件对比优化
- **📊 对比优化** - 优化JSON文件对比功能
- **💾 缓存机制** - 新增缓存文件机制

### v2.1.1 (历史版本) - 🔧 跨平台浏览器启动修复
- **🔧 浏览器启动** - 修复跨平台浏览器启动问题
- **🗑️ 调试代码** - 删除调试代码

### v2.1.0 (历史版本) - 🐛 新增调试功能
- **🐛 调试功能** - 新增调试功能
- **📈 开发体验** - 优化开发体验

### v2.0.9 (历史版本) - 📊 当天JSON文件对比
- **📊 JSON对比** - 新增当天JSON文件对比功能

### v2.0.8 (历史版本) - 🌐 跨平台浏览器启动
- **🌐 浏览器启动** - 修复跨平台浏览器启动问题

### v2.0.7 (历史版本) - 💰 高价商品筛选优化
- **💰 筛选优化** - 优化高价商品筛选
- **🌐 浏览器修复** - 修复浏览器启动

### v2.0.6 (历史版本) - 🔄 数据变化分析优化
- **🔄 分析优化** - 优化数据变化分析代码
- **📈 逻辑精简** - 精简逻辑

### v2.0.5 (历史版本) - ⏰ Cookie过期时间更新
- **⏰ Cookie更新** - 更新Cookie过期时间

### v2.0.4 (历史版本) - 🍪 Cookie自动更新
- **🍪 Cookie自动更新** - 新增Cookie自动更新功能
- **📊 Excel检查** - 优化Excel文件检查

### v2.0.3 (历史版本) - 🔨 代码重构和优化
- **🔨 代码重构** - 代码重构和优化

### v2.0.2 (历史版本) - 💎 高价商品信息写入JSON
- **💎 高价商品** - 新增高价商品信息写入JSON功能

### v2.0.1 (历史版本) - 🎯 高价商品筛选优化
- **🎯 筛选优化** - 优化高价商品筛选逻辑

### v2.0.0 (历史版本) - 🆕 货号对比高价商品筛选
- **🆕 货号对比** - 新增货号对比高价商品筛选功能

### v1.9.0 (历史版本) - 💰 高价商品筛选
- **💰 高价筛选** - 添加高价商品筛选功能

### v1.8.0 (历史版本) - ⏱️ 运行时间显示
- **⏱️ 时间显示** - 添加运行时间显示和动态调整功能

### v1.7.0 (历史版本) - ⚙️ 滚动参数可配置化
- **⚙️ 参数配置** - 滚动参数可配置化

### v1.6.2 (历史版本) - 🔧 页面加载死机修复
- **🔧 死机修复** - 修复页面加载死机问题

### v1.6.1 (历史版本) - 🔄 滚动死循环修复
- **🔄 死循环修复** - 修复滚动死循环问题

### v1.6.0 (历史版本) - ✅ 高优先级优化完成
- **✅ 优化完成** - 完成所有高优先级优化

### v1.5.0 (历史版本) - 📦 JSON数据结构简化
- **📦 结构简化** - 简化JSON数据结构为5个核心字段

### v1.4.3 (历史版本) - ⚡ 页面加载优化
- **⚡ 加载优化** - 优化页面加载逻辑，减少等待时间

### v1.4.2 (历史版本) - 🌐 跨系统环境测试
- **🌐 环境测试** - 完成跨系统环境测试和优化
- **📊 去重优化** - 优化商品去重逻辑，支持无货号商品

### v1.4.1 (历史版本) - 🔐 登录等待优化
- **🔐 登录优化** - 优化登录等待逻辑，移除手动确认步骤

### v1.4.0 (历史版本) - 📊 商品数据字段扩展
- **📊 字段扩展** - 扩展商品数据字段到20个完整字段

### v1.3.4 (历史版本) - 📝 数据变化描述
- **📝 变化描述** - 新增数据变化描述和字段说明

### v1.3.3 (历史版本) - 📊 对比结果消息
- **📊 结果消息** - 新增对比结果消息到JSON日志

### v1.3.2 (历史版本) - 🐛 JSON数据解析修复
- **🐛 解析修复** - 修复JSON数据解析错误

### v1.3.1 (历史版本) - 🆕 JSON多余货号对比
- **🆕 货号对比** - 新增JSON多余货号对比功能并优化代码结构

### v1.3.0 (历史版本) - 📊 Excel与JSON自动对比
- **📊 自动对比** - 添加Excel与JSON自动对比功能

### v1.2.0 (历史版本) - 🍪 Cookie自动更换
- **🍪 Cookie更换** - 添加了一个cookie自动更换的功能，使得东西更加的自动化

### v1.1.0 (历史版本) - 📊 Excel读取功能
- **📊 Excel读取** - 添加了一个excel读取功能，使得东西更加的自动化

### v1.0.0 (初始版本) - 🎉 项目初始化
- **🎉 项目初始化** - 项目初始化，基础功能实现

---

## 🎯 核心功能

### 1. 商品数据采集
- ✅ 闲鱼平台商品列表自动获取
- ✅ 商品价格实时抓取
- ✅ 图片URL智能解析
- ✅ 反爬虫策略处理

### 2. 数据分析
- ✅ 高价商品筛选 (≥599元)
- ✅ 价格统计与汇总
- ✅ 平台手续费计算
- ✅ 对比分析功能

### 3. 用户界面
- ✅ Web端可视化展示
- ✅ 实时数据更新
- ✅ 响应式设计支持

---

## 📂 项目结构

```
D:\ws\xy_ws\
├── dist/
│   ├── app.js              # 主应用文件 (已修复)
│   ├── assets/             # 静态资源
│   └── sw.js               # Service Worker
├── main.py                 # Python后端主程序
├── tests/                  # 测试用例
├── file/                   # 数据存储目录
├── README.md               # 项目说明文档
├── skill.md                # 开发技能文档
└── skill.docx              # Word格式文档
```

---

## 🔒 代码规范 (严格遵守)

详见 [skill.md](./skill.md)

### 关键规范要点
1. **括号匹配** - 所有函数调用、条件判断必须确保括号成对出现
2. **语法检查** - 修改 JS 文件后必须进行语法验证
3. **异常处理** - 统一使用 ExceptionContext 进行错误包装
4. **日志记录** - 关键操作必须添加详细日志输出
5. **代码注释** - 中文注释，清晰描述逻辑和意图

---

## 🛠️ 开发工具

- **前端**: HTML + CSS + JavaScript (ES6+)
- **后端**: Python 3.x
- **包管理**: npm / pip
- **版本控制**: Git
- **文档生成**: Markdown → Word (pandoc/python-docx)

---

## 📄 文档生成方法

### 方法1: 使用 Pandoc (推荐)

安装 Pandoc: https://pandoc.org/installing.html

```bash
pandoc skill.md -o skill.docx
```

### 方法2: 使用 Python python-docx

```bash
pip install python-docx markdown
python generate_docx.py
```

### 方法3: 使用在线工具

访问 https://cloudconvert.com/md-to-docx 上传 skill.md 文件

### 方法4: 使用 Microsoft Word

文件 → 打开 → 选择 skill.md → 另存为 skill.docx

---

## 📊 系统架构

```
┌─────────────────────────────────────┐
│         Web Frontend (dist/)        │
│    ┌─────────────────────────────┐  │
│    │      app.js (主逻辑)        │  │
│    │  - 数据解析                 │  │
│    │  - UI渲染                   │  │
│    │  - 事件处理                 │  │
│    └─────────────┬───────────────┘  │
│                  │ API              │
├──────────────────▼─────────────────┤
│       Python Backend (main.py)     │
│    ┌─────────────────────────────┐  │
│    │  - 商品数据采集             │  │
│    │  - 价格计算引擎             │  │
│    │  - 文件操作管理             │  │
│    └─────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## 🚀 快速开始

### 环境要求
- Node.js v20+
- Python 3.x
- Git

### 安装步骤
```bash
# 克隆仓库
git clone <repository-url>
cd xy_ws

# 安装依赖
npm install
pip install -r requirements.txt

# 启动开发服务器
npm run dev
```

---

## 📈 性能指标

| 指标 | 数值 |
|------|------|
| **总商品数** | 91 个 |
| **高价商品(≥599)** | 73 个 |
| **预计售出总价** | ¥195,468.00 |
| **平均设备均价** | ¥2,148.00 |
| **平台手续费** | ¥3,127.49 |

*数据来源: 2026-07-30微购相册(小旭数码).json*

---

## 🐛 已知问题 & 解决方案

### 当前版本 (v3.8.67)
✅ 所有关键问题已修复

### 常见问题
1. **数据显示为0** → 检查 app.js 语法是否正确
2. **CF隧道不稳定** → 查看 main.py 隧道配置
3. **Cookie失效** → 运行 CookieValidator 验证

---

## 📞 技术支持

- **文档**: [README.md](./README.md), [skill.md](./skill.md)
- **Issue**: 提交至 GitHub Issues
- **日志**: 查看 `file/` 目录下的日志文件

---

## 📝 更新日志

查看上方 **最新修复** 和 **历史版本记录** 部分。

---

**最后更新**: 2026-07-30 (v3.8.89.11)
**维护者**: 小旭数码团队  
**许可证**: MIT License