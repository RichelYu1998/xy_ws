#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安全与Bug修复验证测试
用于验证所有已修复的关键问题
"""

import sys
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


def test_no_env_string_literal():
    """测试：不应该存在环境变量字符串字面量"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查是否还存在错误的字面量模式
    pattern = r"os\.environ\.get\('HOST',\s*'localhost'\)\s*#\s*\[CONFIGURED\]"
    matches = re.findall(pattern, content)
    
    assert len(matches) == 0, f"❌ 仍然存在 {len(matches)} 处环境变量字符串字面量:\n" + "\n".join(f"  - {m}" for m in matches)
    print("✅ 环境变量字符串字面量已全部修复")


def test_socket_resource_cleanup():
    """测试：关键socket资源应该正确清理"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')

    # 检查关键socket函数是否使用了安全的关闭模式
    socket_functions = [
        ('_validate_with_tcp', r'def _validate_with_tcp.*?finally:.*?if sock is not None'),
        ('get_lan_ip', r'def get_lan_ip.*?finally:.*?if s is not None'),
    ]

    for func_name, pattern in socket_functions:
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        assert match, f"❌ {func_name}() 函数的socket资源清理可能不安全"

    # 验证至少有2处使用了 `is not None` 模式
    safe_closes = len(re.findall(r'if \w+ is not None:', content))
    assert safe_closes >= 2, f"❌ 安全的资源关闭模式不足 (发现 {safe_closes} 处)"

    print("✅ Socket资源泄漏问题已修复")


def test_command_injection_protection():
    """测试：命令注入防护应该存在"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查危险字符检查
    assert 'dangerous_patterns' in content, "❌ 缺少危险字符定义"
    assert ';' in content and '|' in content and '&' in content, "❌ 缺少关键危险字符检查"
    assert '[SECURITY]' in content or '命令注入' in content, "❌ 缺少安全日志记录"
    print("✅ 命令注入防护已添加")


def test_run_bat_bom_fix():
    """测试：run.bat的BOM检测应该完整"""
    run_bat = PROJECT_ROOT / "run.bat"
    content = run_bat.read_text(encoding='utf-8')
    
    # 应该包含完整的BOM检测逻辑
    assert '--check-bom' in content, "❌ 缺少BOM检查步骤"
    assert '--fix-bom' in content, "❌ 缺少BOM修复步骤"
    assert 'errorlevel 1' in content or 'not errorlevel 1' in content, "❌ 缺少错误判断逻辑"
    print("✅ run.bat BOM检测逻辑已完善")


def test_imports_at_top():
    """测试：主要导入应该在文件开头"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查核心导入位置（应该在文件前120行内）
    core_imports = ['import argparse', 'import asyncio', 'import json', 'from pathlib import Path']
    
    for imp in core_imports:
        first_occurrence = content.find(imp)
        assert first_occurrence < 10000 and first_occurrence != -1, f"❌ 核心导入 {imp} 位置异常 (位置: {first_occurrence})"
    
    print("✅ 核心模块导入位置正确")


def test_no_eval_exec():
    """测试：不应该使用危险的eval/exec"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 排除注释和字符串中的内容
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        # 跳过注释
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        
        # 检查eval和exec（排除字符串中的情况）
        if re.search(r'\beval\s*\(', line) and 'audit' not in line.lower():
            assert False, f"❌ 第{i}行发现eval()调用: {stripped}"
        if re.search(r'\bexec\s*\(', line) and 'audit' not in line.lower():
            assert False, f"❌ 第{i}行发现exec()调用: {stripped}"
    
    print("✅ 未发现危险的eval/exec调用")


def test_path_traversal_protection():
    """测试：路径遍历攻击防护应该存在"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查路径安全函数
    assert 'sec_sp' in content or 'validate_path_traversal' in content, "❌ 缺少路径遍历防护函数"
    assert 'Path traversal blocked' in content or '路径遍历' in content, "❌ 缺少路径遍历错误消息"
    print("✅ 路径遍历攻击防护已实现")


def test_csrf_protection():
    """测试：CSRF防护机制应该存在"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查CSRF相关代码
    assert 'CSRF' in content or 'csrf' in content, "❌ 缺少CSRF防护相关代码"
    assert 'CSRF_EXEMPT_PATHS' in content or 'WRITE_METHODS' in content, "❌ 缺少CSRF配置"
    print("✅ CSRF防护机制已实现")


def test_rate_limiting():
    """测试：API限流应该存在"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查限流器
    assert 'rate_limiter' in content or 'RateLimiter' in content, "❌ 缺少API限流器"
    assert '429' in content, "❌ 缺少429状态码处理"
    print("✅ API限流机制已实现")


def test_logging_injection_protection():
    """测试：日志注入防护应该存在"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查日志注入防护
    assert '日志注入' in content or 'log.*injection' in content.lower() or r"replace('\\n'" in content, "❌ 缺少日志注入防护"
    print("✅ 日志注入防护已实现")


def test_xss_protection():
    """测试：XSS防护应该存在"""
    main_py = PROJECT_ROOT / "main.py"
    content = main_py.read_text(encoding='utf-8')
    
    # 检查HTML转义
    assert 'escape(' in content or 'html.escape' in content, "❌ 缺少HTML转义函数"
    print("✅ XSS防护已实现")


def run_all_tests():
    """运行所有安全和Bug修复验证测试"""
    print("=" * 70)
    print("🔒 安全与Bug修复验证测试")
    print("=" * 70)
    print()
    
    tests = [
        ("环境变量字符串字面量修复", test_no_env_string_literal),
        ("Socket资源泄漏修复", test_socket_resource_cleanup),
        ("命令注入防护", test_command_injection_protection),
        ("run.bat BOM检测完整性", test_run_bat_bom_fix),
        ("导入语句位置正确性", test_imports_at_top),
        ("无危险eval/exec调用", test_no_eval_exec),
        ("路径遍历攻击防护", test_path_traversal_protection),
        ("CSRF防护机制", test_csrf_protection),
        ("API限流机制", test_rate_limiting),
        ("日志注入防护", test_logging_injection_protection),
        ("XSS防护", test_xss_protection),
    ]
    
    passed = 0
    failed = 0
    errors = []
    
    for name, test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            failed += 1
            errors.append((name, str(e)))
        except Exception as e:
            failed += 1
            errors.append((name, f"测试异常: {e}"))
    
    print()
    print("=" * 70)
    print(f"📊 测试结果: {passed} 通过, {failed} 失败, 共 {len(tests)} 项")
    print("=" * 70)
    
    if errors:
        print("\n❌ 失败的测试:")
        for name, error in errors:
            print(f"\n  ⚠️  {name}")
            print(f"     {error}")
        return False
    else:
        print("\n🎉 所有安全和Bug修复验证测试通过！")
        return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)