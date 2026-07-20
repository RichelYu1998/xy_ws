#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
skill.md 转 skill.docx 生成脚本
遵循 README.md 和 skill.md 中的代码规范
"""

import re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

def sanitize_text(text):
    """
    清理文本中的XML不兼容字符
    
    Args:
        text: 原始文本
    
    Returns:
        清理后的文本
    """
    if not isinstance(text, str):
        return str(text)
    
    illegal_chars = [
        '\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07',
        '\x08', '\x0b', '\x0c', '\x0e', '\x0f', '\x10', '\x11', '\x12',
        '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a',
        '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', '\x7f'
    ]
    
    for char in illegal_chars:
        text = text.replace(char, '')
    
    return text

def parse_markdown_to_docx(md_file_path, docx_file_path):
    """
    将 Markdown 文件转换为 Word 文档
    
    Args:
        md_file_path: Markdown 文件路径
        docx_file_path: 输出的 Word 文档路径
    """
    doc = Document()
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    i = 0
    in_code_block = False
    code_block_content = []
    code_block_lang = ''
    
    while i < len(lines):
        line = lines[i]
        
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_content = []
                code_block_lang = line.strip()[3:].strip()
            else:
                in_code_block = False
                if code_block_content:
                    code_text = '\n'.join(code_block_content)
                    code_text = sanitize_text(code_text)
                    p = doc.add_paragraph(code_text)
                    p.style = 'No Spacing'
                    for run in p.runs:
                        run.font.name = 'Courier New'
                        run.font.size = Pt(9)
                code_block_content = []
            i += 1
            continue
        
        if in_code_block:
            code_block_content.append(line)
            i += 1
            continue
        
        if line.startswith('# '):
            text = line[2:].strip()
            text = sanitize_text(text)
            p = doc.add_heading(text, level=1)
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(18)
                run.font.bold = True
                run.font.color.rgb = RGBColor(0, 51, 102)
        
        elif line.startswith('## '):
            text = line[3:].strip()
            text = sanitize_text(text)
            p = doc.add_heading(text, level=2)
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(16)
                run.font.bold = True
                run.font.color.rgb = RGBColor(0, 76, 153)
        
        elif line.startswith('### '):
            text = line[4:].strip()
            text = sanitize_text(text)
            p = doc.add_heading(text, level=3)
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(14)
                run.font.bold = True
                run.font.color.rgb = RGBColor(0, 102, 204)
        
        elif line.startswith('#### '):
            text = line[5:].strip()
            text = sanitize_text(text)
            p = doc.add_heading(text, level=4)
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(12)
                run.font.bold = True
        
        elif line.startswith('##### '):
            text = line[6:].strip()
            text = sanitize_text(text)
            p = doc.add_heading(text, level=5)
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(11)
                run.font.bold = True
        
        elif line.startswith('###### '):
            text = line[7:].strip()
            text = sanitize_text(text)
            p = doc.add_heading(text, level=6)
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(10)
                run.font.bold = True
        
        elif line.strip().startswith('>'):
            text = line.strip()[1:].strip()
            text = sanitize_text(text)
            p = doc.add_paragraph(text)
            p.style = 'Quote'
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(10)
                run.font.italic = True
        
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:].strip()
            text = process_inline_formatting(text)
            text = sanitize_text(text)
            p = doc.add_paragraph(text, style='List Bullet')
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(10)
        
        elif re.match(r'^\d+\.\s', line.strip()):
            text = re.sub(r'^\d+\.\s', '', line.strip())
            text = process_inline_formatting(text)
            text = sanitize_text(text)
            p = doc.add_paragraph(text, style='List Number')
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(10)
        
        elif line.strip().startswith('|'):
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if cells and not all(c.startswith('-') for c in cells):
                if i > 0 and not lines[i-1].strip().startswith('|'):
                    table = doc.add_table(rows=0, cols=len(cells))
                    table.style = 'Table Grid'
                if 'table' in locals():
                    row = table.add_row()
                    for j, cell_text in enumerate(cells):
                        cell_text = process_inline_formatting(cell_text)
                        cell_text = sanitize_text(cell_text)
                        row.cells[j].text = cell_text
        
        elif line.strip().startswith('---'):
            doc.add_paragraph('_' * 50)
        
        elif line.strip():
            text = process_inline_formatting(line)
            text = sanitize_text(text)
            p = doc.add_paragraph(text)
            for run in p.runs:
                run.font.name = '微软雅黑'
                run.font.size = Pt(10)
        
        i += 1
    
    doc.save(docx_file_path)
    print(f'✓ 成功生成: {docx_file_path}')

def process_inline_formatting(text):
    """
    处理行内格式（粗体、斜体、代码）
    
    Args:
        text: 原始文本
    
    Returns:
        处理后的文本
    """
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text

if __name__ == '__main__':
    import os
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(script_dir, 'skill.md')
    docx_file = os.path.join(script_dir, 'skill.docx')
    
    if not os.path.exists(md_file):
        print(f'❌ 错误: 找不到 {md_file}')
        exit(1)
    
    parse_markdown_to_docx(md_file, docx_file)