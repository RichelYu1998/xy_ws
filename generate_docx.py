#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用skill.md生成skill.docx
遵循项目规范：只保留README.md和skill.md两个MD文件
"""
import pypandoc
import os
import sys

def generate_docx():
    """从skill.md生成skill.docx"""

    skill_md_path = 'D:/ws/xy_ws/skill.md'
    skill_docx_path = 'D:/ws/xy_ws/skill.docx'

    print("🚀 开始生成skill.docx...")

    # 检查skill.md是否存在
    if not os.path.exists(skill_md_path):
        print(f"❌ 错误: 找不到 {skill_md_path}")
        sys.exit(1)

    # 获取文件大小
    md_size = os.path.getsize(skill_md_path) / 1024
    print(f"📄 读取skill.md ({md_size:.2f} KB)...")

    try:
        # 使用pypandoc转换（使用新版本pandoc参数）
        output = pypandoc.convert_file(
            skill_md_path,
            'docx',
            outputfile=skill_docx_path,
            format='md',
            extra_args=['--wrap=none']
        )

        if output == '':
            # 转换成功，检查输出文件
            if os.path.exists(skill_docx_path):
                docx_size = os.path.getsize(skill_docx_path) / 1024
                print(f"✅ 成功生成skill.docx ({docx_size:.2f} KB)")
                print(f"📍 保存路径: {skill_docx_path}")
                return True
            else:
                print("⚠️ 转换完成但未找到输出文件")
                return False
        else:
            print(f"⚠️ pandoc输出: {output}")
            return False

    except Exception as e:
        print(f"❌ 生成失败: {e}")
        return False

if __name__ == '__main__':
    success = generate_docx()
    sys.exit(0 if success else 1)