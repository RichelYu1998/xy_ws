import pypandoc
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    output = pypandoc.convert_file(
        'skill.md',
        'docx',
        outputfile='skill.docx',
        extra_args=[
            '--toc',
            '--toc-depth=4',
            '--standalone'
        ]
    )
    print(f"✅ skill.docx 生成成功")
    print(f"   文件大小: {os.path.getsize('skill.docx') / 1024:.1f} KB")
except Exception as e:
    print(f"❌ 生成失败: {e}")
    sys.exit(1)