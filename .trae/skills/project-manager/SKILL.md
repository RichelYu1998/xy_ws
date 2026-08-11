 ---
name: "project-manager"
description: "微购相册项目完整管理技能。包含代码开发规范、文档生成、Git操作、版本发布等全流程管理。当需要进行代码修改、文档更新、Git提交或版本发布时调用此技能。"
---

# 微购相册项目管理器 (Project Manager)

## 📖 技能概述

本技能定义了微购相册管理系统的**完整项目管理流程和代码开发规范**，确保所有开发和维护工作都遵循统一标准。

---

## 🎯 核心职责

### 1. 代码开发规范管理
- 强制执行 [README.md](../../README.md) 中定义的版本更新格式
- 遵守 [skill.md](../../skill.md) 中的所有技术范式和最佳实践
- 确保所有代码修改符合安全标准（XSS防护、输入验证等）

### 2. 文档同步更新机制
每次代码修改后，必须同步更新以下文档：
- **README.md** - 版本历史和功能说明
- **skill.md** - 技术规范和架构设计
- **skill.docx** - Word格式完整文档（可选）

### 3. Git工作流管理
- 规范化的提交信息格式
- 版本号管理策略
- 分支管理和合并规则

---

## 📝 版本更新流程

### 版本号命名规则
```
v{主版本}.{次版本}.{修复版本}.{日期}
示例: v3.8.89.18 (2026-08-11)
```

### README.md 更新模板

```markdown
### v{版本号} {图标} {简短标题}

#### 更新内容: {详细描述}

**更新日期**: {YYYY-MM-DD}
**更新类型**: {功能新增|Bug修复|性能优化|安全修复}
**影响文件**: [文件路径1](文件路径1), [文件路径2](文件路径2)

---

##### {编号}. {功能/修复标题}

**问题描述**:
- **现象**: {用户可见的问题表现}
- **根本原因**: {技术层面的原因分析}
- **影响范围**: {受影响的模块或功能}

**修复方案**:
```javascript
// ❌ 修复前：问题代码
{旧代码}

// ✅ 修复后：正确代码
{新代码}
```

**技术改进点**:
- ✅ 改进点1
- ✅ 改进点2

**验证结果**: {测试结果描述}
```

### 提交信息格式

```
{类型}: {简洁描述} (v{版本号})

类型选项：
- feat: 新功能
- fix: Bug修复
- docs: 文档更新
- style: 代码格式调整
- refactor: 重构
- perf: 性能优化
- test: 测试相关
- chore: 构建/工具/杂项
- security: 安全修复
```

---

## 🔒 代码规范强制要求

### 前端安全编码规范（来自 skill.md）

#### XSS防护（必须遵守）
```javascript
// ✅ 正确：使用转义函数
const safeHtml = escapeHtml(userInput);
const safeAttr = escapeAttr(userInput);

// ❌ 错误：直接拼接HTML
element.innerHTML = `<div>${userInput}</div>`;
```

#### URL验证（必须遵守）
```javascript
// ✅ 正确：验证URL协议
function isValidUrl(url) {
    if (!url) return false;
    try {
        const parsed = new URL(url);
        return ['http:', 'https:'].includes(parsed.protocol);
    } catch {
        return false;
    }
}

// ❌ 错误：不验证直接使用
element.src = userInput;
```

#### 事件绑定现代化（推荐）
```javascript
// ✅ 正确：addEventListener + data-*属性
const link = document.createElement('a');
link.dataset.sku = skuValue;
link.addEventListener('click', function(e) {
    e.preventDefault();
    handleSkuClick(this.dataset.sku);
});

// ❌ 错误：内联事件处理器
link.onclick = `handleClick('${skuValue}')`;
```

### 后端安全编码规范（来自 skill.md）

#### 输入验证（必须遵守）
```python
# ✅ 正确：白名单验证
import re
if not re.match(r'^[a-zA-Z0-9._\-]+$', str(process_name)):
    logger.warning(f'无效的进程名称: {process_name}')
    return False

# ❌ 错误：直接拼接命令
subprocess.run(f'taskkill /F /IM {process_name}', shell=True)
```

#### 异常处理（必须遵守）
```python
# ✅ 正确：细粒度异常捕获
try:
    result = subprocess.run(..., timeout=TIMEOUT_CONFIG['subprocess_wait'])
except subprocess.TimeoutExpired as e:
    logger.warning(f'操作超时: {e}')
    return False

# ❌ 错误：宽泛异常捕获
try:
    result = subprocess.run(...)
except Exception as e:
    pass
```

---

## 🔄 文档生成工作流

### 步骤1：代码修改完成后
1. 确认代码符合 skill.md 中的所有技术范式
2. 运行测试验证功能正常
3. 记录所有修改的文件和行号

### 步骤2：更新 README.md
在文件顶部 `## 🔄 最新更新` 章节添加新的版本记录：
- 使用标准模板格式
- 包含问题描述、修复方案、代码对比
- 标注影响范围和验证结果

### 步骤3：更新 skill.md（如涉及新技术）
- 在相应章节添加新的技术范式
- 更新架构图或模块说明
- 补充最佳实践案例

### 步骤4：生成 skill.docx（可选）
```bash
# 使用 pandoc 转换
pandoc skill.md -o skill.docx --reference-doc=template.docx
```

### 步骤5：Git提交和推送
```bash
git add .
git commit -m "docs(readme+skill+docx): v{版本号} {标题}"
git push origin master
```

---

## 📊 本次更新记录模板

### 示例：商品描述点击功能实现

**版本**: v3.8.89.18  
**日期**: 2026-08-11  
**类型**: 功能增强

#### 更新内容摘要
为新增/高价商品表格的商品描述列添加点击查看详情功能，提升用户体验。

#### 修改文件清单
- [dist/app.js](dist/app.js) - 前端交互逻辑
  - 第1982-1983行：新增商品表格（货号+描述双击）
  - 第1997-2004行：删除商品表格（纯文本展示）
  - 第2024-2025行：高价商品表格（货号+描述双击）

#### 技术要点
1. **差异化交互设计**
   - 新增商品：可点击（数据存在）
   - 删除商品：不可点击（数据已删除）
   - 高价商品：可点击（重点监控）

2. **安全防护措施**
   - 所有动态内容使用 `escapeHtml()` 转义
   - URL参数使用 `escapeAttr()` 编码
   - 复用现有的事件绑定机制（desc-link类）

3. **用户体验优化**
   - 蓝色链接样式（#409EFF）明确提示可交互
   - 鼠标悬停显示完整描述（title属性）
   - 文本溢出自动省略（max-width: 300px）

---

## ⚠️ 重要提醒

### 必须检查项（Checklist）
- [ ] 代码符合 skill.md 安全规范
- [ ] README.md 格式正确，版本号连续
- [ ] 所有修改的文件都已列入影响列表
- [ ] 测试通过，无回归问题
- [ ] Git提交信息符合规范
- [ ] 敏感信息未泄露（密码、密钥等）

### 禁止事项
- ❌ 跳过文档更新直接提交代码
- ❌ 使用已废弃的API或方法
- ❌ 在生产环境使用 console.log 调试代码
- ❌ 提交包含硬编码敏感信息的代码
- ❌ 忽略XSS或其他安全漏洞

---

## 📞 维护说明

**维护者**: 小旭二手机（西园路）  
**创建日期**: 2026-08-11  
**最后更新**: 2026-08-11  
**适用范围**: 微购相册管理系统全栈开发

**相关文档**:
- [README.md](../../README.md) - 项目主文档
- [skill.md](../../skill.md) - 技术规范文档
- [main.py](../../main.py) - Python后端代码
- [dist/app.js](dist/app.js) - JavaScript前端代码