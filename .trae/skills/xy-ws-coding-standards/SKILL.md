---
name: "xy-ws-coding-standards"
description: "Python + Flask + 原生JS 全栈项目代码规范。Invoke when developing or modifying xy_ws project code, or when creating similar full-stack projects."
---

# xy_ws 项目代码规范

本skill定义了xy_ws项目的完整代码规范，包括后端Python、前端JavaScript、启动脚本、配置文件等所有方面的开发标准。

## 使用场景

- 开发或修改xy_ws项目代码时
- 创建类似的Python + Flask + 原生JS全栈项目时
- 进行代码审查和规范检查时
- 新成员加入项目时快速了解编码规范

## 规范文档位置

完整的代码规范文档位于项目根目录的 `skill.md` 文件中，包含：

### 主要规范内容

1. **项目结构规范** - 单文件架构、配置与代码分离
2. **后端Python规范** - 异常处理、安全调用、跨平台环境、路径管理、配置管理、文件操作、爬虫引擎、API路由等
3. **前端规范** - 原生JS、API调用、Toast提示、响应式设计、全局函数管理等
4. **启动脚本规范** - 六步启动流程、日志双写、跨平台支持
5. **配置文件规范** - config.json结构、模板机制
6. **隧道与公网访问规范** - Cloudflare Tunnel配置、Web日志持久化、邮件通知
7. **编码风格速查** - 跨平台规范、镜像源测速、临时环境隔离等

### 核心原则

- **单文件后端**：所有Python逻辑集中在main.py
- **单文件前端**：index.html包含所有HTML/CSS/JS
- **配置与代码分离**：config/存放配置，file/存放运行时数据
- **跨平台兼容**：支持Windows/Linux/macOS
- **安全优先**：异常处理、输入验证、线程安全

## 快速参考

详细规范请查看项目根目录的 [skill.md](file:///D:/ws/xy_ws/skill.md) 文件。

## 版本信息

- **项目版本**: v3.8.74
- **更新日期**: 2026-07-20
- **技术栈**: Python 3.14 + Flask + 原生JavaScript + Playwright