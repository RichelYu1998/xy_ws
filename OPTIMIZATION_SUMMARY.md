# 代码优化建议总结

## 模拟运行结果

✅ **程序可以正常启动**
- 主菜单显示正常
- 所有选项都可用
- 版本号显示正确（v1.5.0）

## 发现的问题

### 1. 空的异常处理（3处）

**位置：**
- [main.py:203](file:///D:\ws\xy_ws\main.py#L203) - 关闭弹窗时
- [main.py:1046](file:///D:\ws\xy_ws\main.py#L1046) - 等待页面关闭时
- [main.py:1057](file:///D:\ws\xy_ws\main.py#L1057) - 关闭浏览器时

**问题：** 空的except块会隐藏错误，不利于调试

**建议：** 至少记录日志

```python
# 修改前
except:
    pass

# 修改后
except Exception as e:
    pass  # 或者 logging.debug(f"忽略错误: {e}")
```

### 2. 重复的代码（24处）

**问题：** `print('='*60)` 出现24次

**建议：** 提取为常量或函数

```python
# 添加常量
SEPARATOR = '=' * 60

# 或者添加函数
def print_separator():
    print('=' * 60)

# 使用
print(SEPARATOR)
# 或
print_separator()
```

### 3. 主菜单没有循环

**位置：** [main.py:950-975](file:///D:\ws\xy_ws\main.py#L950-L975)

**问题：** 选择一个选项后程序就退出了，需要重新启动

**建议：** 添加while循环

```python
def main():
    while True:
        print('='*60)
        print(f'Szwego商品爬虫和货号对比工具 - v{VERSION}')
        print('='*60)
        print('请选择功能：')
        print('1. 运行爬虫')
        print('2. 货号对比（交互式）')
        print('3. 货号对比（简化版）')
        print('4. Excel与JSON对比（自动保存差异日志）')
        print('5. 更新Cookie')
        print('0. 退出')
        print('='*60)
        
        try:
            choice = input('请输入选项 (0-5): ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n程序已退出')
            return
        
        if choice == '1':
            run_scraper()
        elif choice == '2':
            StockNumberComparator().run_interactive()
        elif choice == '3':
            StockNumberComparator().run_simple()
        elif choice == '4':
            StockNumberComparator().compare_excel_with_json()
        elif choice == '5':
            update_cookie()
        elif choice == '0':
            print('程序已退出')
            break
        else:
            print('无效的选项')
            input('按回车键继续...')
```

### 4. run.bat 没有检查虚拟环境

**位置：** [run.bat:6](file:///D:\ws\xy_ws\run.bat#L6)

**问题：** 如果虚拟环境不存在会直接报错

**建议：** 添加检查和自动创建

```batch
@echo off
chcp 65001 > nul
echo ========================================
echo Szwego商品爬虫和货号对比工具 - v1.5.0
echo ========================================
echo.

REM 检查虚拟环境
if not exist ".venv\Scripts\python.exe" (
    echo 虚拟环境不存在，正在创建...
    python -m venv .venv
    if errorlevel 1 (
        echo 创建虚拟环境失败，请确保已安装Python 3.7+
        pause
        exit /b 1
    )
    echo 正在安装依赖...
    .venv\Scripts\pip.exe install -r requirements.txt
    if errorlevel 1 (
        echo 安装依赖失败
        pause
        exit /b 1
    )
    echo 正在安装Playwright浏览器...
    .venv\Scripts\playwright.exe install chromium
)

REM 检查配置文件
if not exist "config\config.json" (
    echo 配置文件不存在，请先配置 config\config.json
    pause
    exit /b 1
)

.venv\Scripts\python.exe main.py
pause
```

### 5. 没有配置文件检查

**位置：** [main.py:950](file:///D:\ws\xy_ws\main.py#L950)

**问题：** 如果配置文件不存在，程序会在运行时报错

**建议：** 在主菜单中添加检查

```python
def main():
    while True:
        print('='*60)
        print(f'Szwego商品爬虫和货号对比工具 - v{VERSION}')
        print('='*60)
        
        # 检查配置文件
        if not FileManager.file_exists('config/config.json'):
            print('⚠️  警告: 配置文件不存在 (config/config.json)')
            print('请先配置 config/config.json 文件')
            print('='*60)
            input('按回车键退出...')
            return
        
        # 检查Cookie文件
        if not FileManager.file_exists('config/cookies.json'):
            print('⚠️  警告: Cookie文件不存在 (config/cookies.json)')
            print('建议先运行"更新Cookie"功能')
            print('='*60)
        
        print('请选择功能：')
        # ... 其余代码
```

### 6. Cookie更新菜单没有循环

**位置：** [main.py:986-1010](file:///D:\ws\xy_ws\main.py#L986-L1010)

**问题：** 选择一个选项后返回主菜单，无法连续操作

**建议：** 添加while循环

```python
def update_cookie():
    while True:
        print('='*60)
        print('Cookie更新工具')
        print('='*60)
        print('请选择方式：')
        print('1. 自动获取（推荐）- 程序启动浏览器，登录后自动保存')
        print('2. 手动粘贴 - 从浏览器复制Cookie字符串')
        print('0. 返回')
        print('='*60)
        
        try:
            choice = input('请输入选项 (0-2): ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n已取消')
            return
        
        if choice == '1':
            auto_get_cookie()
        elif choice == '2':
            manual_update_cookie()
        elif choice == '0':
            return
        else:
            print('无效的选项')
            input('按回车键继续...')
```

## 优化优先级

### 🔴 高优先级（建议立即优化）

1. **主菜单添加循环** - 提升用户体验
2. **run.bat 添加虚拟环境检查** - 防止直接报错
3. **添加配置文件检查** - 提前发现问题
4. **修复空的异常处理** - 避免隐藏错误

### 🟡 中优先级（建议近期优化）

5. **Cookie更新菜单添加循环** - 提升用户体验
6. **提取重复代码** - 提高代码可维护性
7. **添加错误处理函数** - 统一错误处理

### 🟢 低优先级（可选优化）

8. **添加日志记录** - 便于问题排查
9. **添加进度显示** - 提升用户体验
10. **添加单元测试** - 保证代码质量

## 快速优化方案

如果时间有限，建议优先实施以下3个优化：

### 1. 主菜单循环（5分钟）
```python
def main():
    while True:
        # ... 现有代码 ...
        if choice == '0':
            print('程序已退出')
            break
        else:
            print('无效的选项')
            input('按回车键继续...')
```

### 2. run.bat 检查虚拟环境（3分钟）
```batch
if not exist ".venv\Scripts\python.exe" (
    echo 虚拟环境不存在，正在创建...
    python -m venv .venv
    .venv\Scripts\pip.exe install -r requirements.txt
)
```

### 3. 修复空的异常处理（2分钟）
```python
except Exception as e:
    pass  # 或者 logging.debug(f"忽略错误: {e}")
```

**总时间：约10分钟即可完成核心优化**

## 总结

当前代码质量：⭐⭐⭐⭐☆ (4/5)

**优点：**
- ✅ 功能完整
- ✅ 代码结构清晰
- ✅ 错误处理较好
- ✅ 跨系统兼容

**需要改进：**
- ❌ 主菜单没有循环
- ❌ 启动脚本缺少检查
- ❌ 有空的异常处理
- ❌ 代码重复较多

**建议：** 优先实施高优先级优化，可以显著提升用户体验和代码质量。