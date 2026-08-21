#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 版本兼容性检查工具
用于验证当前 Python 版本是否满足项目要求
"""

import sys


def get_version_info():
    """获取详细的 Python 版本信息"""
    return {
        "version": sys.version.split()[0],
        "version_info": sys.version_info[:3],
        "major": sys.version_info.major,
        "minor": sys.version_info.minor,
        "micro": sys.version_info.micro,
        "releaselevel": sys.version_info.releaselevel,
        "serial": sys.version_info.serial,
    }


def check_python_version(min_version=(3, 0)):
    """
    检查 Python 版本是否满足最低要求
    
    Args:
        min_version: 最低支持的 Python 版本元组，如 (3, 9)
    
    Returns:
        bool: 是否满足要求
    """
    current = sys.version_info[:2]
    
    print("=" * 60)
    print("🐍 Python 版本兼容性检查")
    print("=" * 60)
    print(f"✅ 当前 Python 版本: {sys.version}")
    print(f"✅ 版本号: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"✅ 要求最低版本: {'.'.join(map(str, min_version))}+")
    print("-" * 60)
    
    if current < min_version:
        print(f"❌ 错误: Python 版本过低!")
        print(f"   需要: >={'.'.join(map(str, min_version))}")
        print(f"   当前: {'.'.join(map(str, current))}")
        print()
        print("💡 请升级 Python 版本或使用正确的 Python 解释器运行")
        print("=" * 60)
        return False
    
    print(f"✅ 版本检查通过! (>={'.'.join(map(str, min_version))})")
    
    # 检查具体特性支持
    check_features(current)
    
    print("=" * 60)
    return True


def check_features(version):
    """检查特定版本的特性支持"""
    print("\n📋 特性支持检查:")
    print("-" * 40)
    
    features = {
        (3, 6): "f-string, 变量注解",
        (3, 7): "dataclass, asyncio.run()",
        (3, 8): "海象运算符(:=), positional-only参数",
        (3, 9): "字典合并运算符(|), 类型泛型",
        (3, 10): "模式匹配(match/case), 更好的错误消息",
        (3, 11): "异常组(ExceptGroup*), Tomllib",
        (3, 12): "类型参数语法, 改进的错误消息",
        (3, 13): "实验性的自由线程CPython",
        (3, 14): "即将发布的特性",
    }
    
    for min_ver, feature in sorted(features.items()):
        status = "✅" if version >= min_ver else "⚠️"
        print(f"{status} Python {'.'.join(map(str, min_ver))}: {feature}")


def main():
    """主函数"""
    # 从 requirements.txt 读取的最低版本要求
    MIN_VERSION = (3, 0)  # 支持 Python >=3.0 的所有版本
    
    # 执行检查
    success = check_python_version(MIN_VERSION)
    
    if not success:
        sys.exit(1)
    
    print("\n🎉 所有检查通过！可以安全运行本项目。")
    return 0


if __name__ == "__main__":
    sys.exit(main())