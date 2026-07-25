#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""移除文件开头的BOM字符"""

import sys

def remove_bom(file_path):
    """移除文件开头的BOM字符"""
    try:
        # 以二进制模式读取文件
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # 检查是否有UTF-8 BOM
        if content.startswith(b'\xef\xbb\xbf'):
            print(f"发现BOM字符，正在移除...")
            content = content[3:]  # 移除前3个字节（BOM）
            
            # 写回文件
            with open(file_path, 'wb') as f:
                f.write(content)
            print(f"✅ BOM字符已移除: {file_path}")
            return True
        else:
            print(f"✅ 文件没有BOM字符: {file_path}")
            return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

if __name__ == '__main__':
    files = [
        'D:/ws/xy_ws/main.py',
        'D:/ws/xy_ws/generate_skill_docx.py',
        'D:/ws/xy_ws/README.md',
        'D:/ws/xy_ws/skill.md'
    ]
    
    for file_path in files:
        remove_bom(file_path)