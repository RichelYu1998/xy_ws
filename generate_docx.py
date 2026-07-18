#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 skill.md 转换为 skill.docx
遵循 skill.md 中的代码规范
"""

import re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

def set_chinese_font(run, font_name='微软雅黑', font_size=11):
    """设置中文字体"""
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)

def set_code_font(run, font_name='Consolas', font_size=10):
    """设置代码字体"""
    run.font.name = font_name
    run.font.size = Pt(font_size)

def clean_text(text):
    """清理文本，移除不兼容的 XML 字符"""
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    return text

def parse_markdown_to_docx(md_file, docx_file):
    """将 Markdown 文件转换为 Word 文档"""
    doc = Document()
    
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    in_code_block = False
    code_lines = []
    
    while i < len(lines):
        line = lines[i].rstrip()
        line = clean_text(line)
        
        if line.startswith('```'):
            if in_code_block:
                if code_lines:
                    code_text = '\n'.join(code_lines)
                    code_text = clean_text(code_text)
                    p = doc.add_paragraph()
                    run = p.add_run(code_text)
                    set_code_font(run)
                    code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            code_lines.append(line)
            i += 1
            continue
        
        if line.startswith('# '):
            text = line[2:]
            p = doc.add_heading(text, level=1)
            for run in p.runs:
                set_chinese_font(run, font_size=18)
        
        elif line.startswith('## '):
            text = line[3:]
            p = doc.add_heading(text, level=2)
            for run in p.runs:
                set_chinese_font(run, font_size=16)
        
        elif line.startswith('### '):
            text = line[4:]
            p = doc.add_heading(text, level=3)
            for run in p.runs:
                set_chinese_font(run, font_size=14)
        
        elif line.startswith('#### '):
            text = line[5:]
            p = doc.add_heading(text, level=4)
            for run in p.runs:
                set_chinese_font(run, font_size=12)
        
        elif line.startswith('---'):
            doc.add_paragraph('_' * 50)
        
        elif line.startswith('- ') or line.startswith('* '):
            text = line[2:]
            p = doc.add_paragraph(style='List Bullet')
            run = p.add_run(text)
            set_chinese_font(run)
        
        elif line.startswith('|') and '|' in line[1:]:
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if cells:
                table = doc.add_table(rows=1, cols=len(cells))
                table.style = 'Table Grid'
                row_cells = table.rows[0].cells
                for idx, cell_text in enumerate(cells):
                    row_cells[idx].text = cell_text
        
        elif line.strip():
            p = doc.add_paragraph()
            run = p.add_run(line)
            set_chinese_font(run)
        
        i += 1
    
    doc.save(docx_file)
    print(f'✅ 已生成 {docx_file}')

if __name__ == '__main__':
    parse_markdown_to_docx('skill.md', 'skill.docx')