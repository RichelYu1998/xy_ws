# Szwego商品爬虫和货号对比工具

## 项目介绍

这是一个跨系统的商品爬虫和货号对比工具，用于从szwego.com网站抓取商品数据，并提供货号对比功能。

## 功能特性

### 1. 商品爬虫
- 自动登录（支持Cookie保存和加载）
- 智能滚动加载所有商品
- 并发处理提高效率
- 自动提取商品信息（名称、价格、货号、备注、员工）
- 跨平台支持（Windows、Mac、Linux）
- 反爬虫检测和规避

### 2. 货号对比工具
- 交互式和简化版两种模式
- 支持多种输入格式
- 自动检测重复序列号
- 详细的对比结果展示
- JSON日志记录
- 支持从文件读取和保存
- **Excel文件支持**：直接读取Excel文件中的货号数据
- **智能工作表识别**：自动查找指定工作表（如"闲鱼"）
- **精确列读取**：支持读取指定列的数据（如E列）
- **保留前导0**：自动保留0开头的序列号

## 项目结构

```
D:\ws\xy_ws\
├── main.py                      # 主程序文件
├── run.bat                      # Windows启动脚本
├── run.sh                       # Linux/Mac启动脚本
├── config/                      # 配置文件目录
│   ├── config.json             # 主配置文件
│   ├── cookies.json            # Cookie存储文件
│   └── input_stock_numbers.txt # 货号输入文件
├── file/                       # 数据文件目录
│   ├── output.json             # 商品数据输出文件
│   └── duplicate_log.json      # 重复序列号日志
└── .venv/                      # Python虚拟环境
```

## 安装和配置

### 1. 环境要求
- Python 3.8+
- pip

### 2. 安装依赖

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 安装依赖
pip install playwright openpyxl
playwright install chromium
```

### 3. 配置文件

编辑 `config/config.json` 文件，设置登录信息和目标URL：

```json
{
  "login": {
    "username": "your_username",
    "password": "your_password",
    "login_type": "phone"
  },
  "target_url": "https://www.szwego.com/your_shop_url",
  "headers": {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
  },
  "output_file": "file/output.json",
  "cookie_file": "config/cookies.json",
  "excel_file": "C:\\Users\\YourUsername\\Desktop\\your_file.xlsx"
}
```

**配置说明：**
- `login`: 登录信息（用户名、密码、登录类型）
- `target_url`: 目标网站URL
- `headers`: HTTP请求头信息
- `output_file`: 商品数据输出文件路径
- `cookie_file`: Cookie存储文件路径
- `excel_file`: Excel文件路径（用于货号对比）

## 使用方法

### 方法1：使用启动脚本（推荐）

**Windows:**
```bash
# 双击运行
run.bat
```

**Linux/Mac:**
```bash
# 添加执行权限
chmod +x run.sh

# 运行
./run.sh
```

### 方法2：直接运行Python

```bash
# 激活虚拟环境
.venv\Scripts\activate  # Windows
# 或
source .venv/bin/activate  # Linux/Mac

# 运行程序
python main.py
```

## 功能选择

运行程序后，会显示主菜单：

```
============================================================
Szwego商品爬虫和货号对比工具 - 跨系统版本
============================================================
请选择功能：
1. 运行爬虫
2. 货号对比（交互式）
3. 货号对比（简化版）
0. 退出
============================================================
```

### 1. 运行爬虫

选择选项1，程序会：
1. 启动浏览器
2. 加载Cookie（如果有）
3. 访问目标页面
4. 自动滚动加载所有商品
5. 提取商品信息
6. 保存到 `file/output.json`

### 2. 货号对比（交互式）

选择选项2，进入交互式模式：
- 直接输入货号字符串
- 输入 `load` 从文件读取
- 输入 `save` 保存当前输入
- 输入 `help` 查看帮助
- 输入 `quit` 退出

**支持的输入格式：**
- 逗号分隔：`12345, 67890, 11111`
- 空格分隔：`12345 67890 11111`
- 混合分隔：`12345, 67890 11111; 22222`
- 包含"序列号"文字：`序列号 12345 67890`
- 大量空白字符：`12345,    67890,    11111`

### 3. 货号对比（简化版）

选择选项3，程序会自动：
1. 从 `file/output.json` 读取商品数据
2. **优先从Excel文件读取货号**（配置在 `config/config.json` 中的 `excel_file` 字段）
3. 如果Excel文件不存在，则从 `config/input_stock_numbers.txt` 读取货号
4. 进行对比分析
5. 显示结果

**Excel文件读取规则：**
- 自动查找包含指定名称的工作表（如"闲鱼"）
- 读取指定列的数据（默认为E列）
- 自动提取3-6位数字作为货号
- **保留0开头的序列号**（如 `08544` 保持原样）
- 自动去重，避免重复计算

## 配置文件说明

### config/config.json
主配置文件，包含：
- 登录信息
- 目标URL
- User-Agent
- 文件路径配置

### config/cookies.json
Cookie存储文件，用于保持登录状态

### config/input_stock_numbers.txt
货号输入文件，用于对比功能（备用，当Excel文件不存在时使用）

### file/output.json
商品数据输出文件，包含爬取的商品信息

### file/duplicate_log.json
重复序列号日志文件

### Excel文件（可选）
用于货号对比的Excel文件，路径配置在 `config/config.json` 的 `excel_file` 字段中。

**Excel文件格式要求：**
- 文件格式：`.xlsx` 或 `.xls`
- 工作表名称：程序会自动查找包含指定名称的工作表（如"闲鱼"）
- 数据列：默认读取E列（第5列）的序列号数据
- 序列号格式：支持3-6位数字，自动保留前导0

**示例Excel结构：**
```
| A列  | B列  | C列  | D列  | E列（序列号） |
|-------|-------|-------|-------|--------------|
| 商品1 | 价格1 | 备注1 | 员工1 | 12345        |
| 商品2 | 价格2 | 备注2 | 员工2 | 08544        |
| 商品3 | 价格3 | 备注3 | 员工3 | 67890        |
```

## 跨系统支持

程序自动检测操作系统并适配：

- **Windows**: 使用Windows特定的浏览器参数
- **Mac**: 适配macOS环境
- **Linux**: 适配Linux环境，包括无头模式支持

## 故障排除

### 问题1：找不到Python命令

**解决方案：**
- 使用虚拟环境中的Python：`.venv\Scripts\python.exe`（Windows）
- 或使用启动脚本：`run.bat`（Windows）/ `run.sh`（Linux/Mac）

### 问题2：Playwright浏览器未安装

**解决方案：**
```bash
pip install playwright
playwright install chromium
```

### 问题3：openpyxl库未安装

**解决方案：**
```bash
pip install openpyxl
```

### 问题4：Cookie过期

**解决方案：**
- 删除 `config/cookies.json` 文件
- 重新运行爬虫，手动登录
- Cookie会自动保存

### 问题5：Excel文件无法读取

**解决方案：**
- 检查 `config/config.json` 中的 `excel_file` 路径是否正确
- 确保Excel文件存在且格式正确（.xlsx或.xls）
- 确保工作表名称正确（如"闲鱼"）
- 确保E列包含有效的序列号数据

### 问题6：编码问题

**解决方案：**
- 确保输入文件使用UTF-8编码
- Windows批处理文件已设置编码：`chcp 65001`

### 问题7：0开头的序列号被去掉

**解决方案：**
- 程序已优化，会自动保留0开头的序列号
- 确保使用最新版本的程序

## 注意事项

1. **Cookie有效期**：Cookie会过期，需要定期更新
2. **反爬虫机制**：网站可能有反爬虫措施，请合理使用
3. **数据备份**：定期备份 `file/output.json` 数据
4. **网络连接**：确保网络连接稳定
5. **浏览器窗口**：爬虫运行时会打开浏览器窗口，请勿关闭

## 技术特点

- **异步编程**：使用asyncio提高效率
- **并发处理**：使用ThreadPoolExecutor并发处理商品
- **智能滚动**：自动检测页面加载完成
- **正则表达式**：灵活的数据提取
- **跨平台**：支持Windows、Mac、Linux
- **错误处理**：完善的异常处理机制

## 更新日志

### v1.1.0 (2026-04-03)
- **新增Excel文件支持**：可直接读取Excel文件中的货号数据
- **智能工作表识别**：自动查找指定工作表（如"闲鱼"）
- **精确列读取**：支持读取指定列的数据（如E列）
- **保留前导0**：自动保留0开头的序列号（如08544）
- **配置文件优化**：Excel文件路径配置在config.json中
- **依赖库更新**：添加openpyxl库支持Excel文件读取
- **文档完善**：更新README.md，添加Excel功能说明

### v1.0.0 (2026-04-03)
- 整合爬虫和货号对比功能
- 支持跨系统运行
- 添加启动脚本
- 优化文件结构
- 添加重复检测功能
- 改进用户交互体验

## 许可证

本项目仅供学习和研究使用。

## 联系方式

如有问题或建议，请联系开发者。