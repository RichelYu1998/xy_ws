#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 版本兼容性测试
用于验证项目在不同 Python 版本下的运行情况
"""

import sys
import pytest
from pathlib import Path


# 添加项目根目录到路径
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


class TestPythonVersion:
    """测试 Python 版本兼容性"""
    
    def test_python_version_minimum(self):
        """测试 Python 版本是否 >= 3.0"""
        assert sys.version_info >= (3, 0), \
            f"需要 Python >=3.0，当前版本: {sys.version_info.major}.{sys.version_info.minor}"
    
    def test_python_3_features(self):
        """测试 Python 3 基本特性是否可用"""
        # f-string (3.6+)
        name = "test"
        result = f"Hello {name}"
        assert "test" in result
        
        # 类型注解 (3.5+)
        def func(x: int) -> int:
            return x + 1
        assert func(5) == 6
    
    def test_import_core_modules(self):
        """测试核心模块导入"""
        import asyncio
        import json
        import os
        import sys
        from pathlib import Path
    
    def test_project_requirements(self):
        """测试 requirements.txt 中的依赖是否能正确解析"""
        req_file = PROJECT_ROOT / "requirements.txt"
        assert req_file.exists(), "requirements.txt 文件不存在"
        
        content = req_file.read_text(encoding="utf-8")
        assert "fastapi" in content.lower(), "缺少 fastapi 依赖"
        assert "playwright" in content.lower(), "缺少 playwright 依赖"


class TestProjectStructure:
    """测试项目结构完整性"""
    
    def test_main_module_exists(self):
        """测试主模块是否存在"""
        main_py = PROJECT_ROOT / "main.py"
        assert main_py.exists(), "main.py 不存在"
    
    def test_check_script_exists(self):
        """测试版本检查脚本是否存在"""
        check_script = PROJECT_ROOT / "check_python_version.py"
        assert check_script.exists(), "check_python_version.py 不存在"
    
    def test_tox_config_exists(self):
        """测试 tox 配置是否存在"""
        tox_ini = PROJECT_ROOT / "tox.ini"
        assert tox_ini.exists(), "tox.ini 不存在"


class TestDependencies:
    """测试依赖项兼容性"""
    
    @pytest.mark.skipif(sys.version_info < (3, 7), reason="需要 Python 3.7+")
    def test_dataclass_support(self):
        """测试 dataclass 支持 (3.7+)"""
        from dataclasses import dataclass
        
        @dataclass
        class Point:
            x: int
            y: int
        
        p = Point(1, 2)
        assert p.x == 1 and p.y == 2
    
    @pytest.mark.skipif(sys.version_info < (3, 9), reason="需要 Python 3.9+")
    def test_dict_union_operator(self):
        """测试字典合并运算符 (3.9+)"""
        d1 = {"a": 1}
        d2 = {"b": 2}
        merged = d1 | d2
        assert merged == {"a": 1, "b": 2}


def test_python_version_info():
    """输出当前 Python 版本信息（用于调试）"""
    print(f"\n📊 当前环境:")
    print(f"   Python: {sys.version}")
    print(f"   版本号: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"   平台: {sys.platform}")
    print(f"   可执行文件: {sys.executable}")


if __name__ == "__main__":
    # 直接运行测试
    pytest.main([__file__, "-v", "-s"])