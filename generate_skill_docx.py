#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill.md 转 skill.docx 生成脚本
根据 skill.md 中的规范生成 Word 文档
"""

import os
import re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn


def set_chinese_font(run, font_name='宋体', size=12):
    """设置中文字体"""
    run.font.name = font_name
    run.font.size = Pt(size)
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)


def parse_markdown_to_docx(md_file, docx_file):
    """将 Markdown 文件转换为 Word 文档"""
    if not os.path.exists(md_file):
        print(f'❌ 错误: 文件不存在: {md_file}')
        return False
    
    doc = Document()
    
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f'❌ 错误: 无法读取文件 {md_file}: {e}')
        return False
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        if not line:
            i += 1
            continue
        
        if line.startswith('# '):
            p = doc.add_heading(line[2:], level=1)
            for run in p.runs:
                set_chinese_font(run, '微软雅黑', 22)
        elif line.startswith('## '):
            p = doc.add_heading(line[3:], level=2)
            for run in p.runs:
                set_chinese_font(run, '微软雅黑', 18)
        elif line.startswith('### '):
            p = doc.add_heading(line[4:], level=3)
            for run in p.runs:
                set_chinese_font(run, '微软雅黑', 16)
        elif line.startswith('#### '):
            p = doc.add_heading(line[5:], level=4)
            for run in p.runs:
                set_chinese_font(run, '微软雅黑', 14)
        elif line.startswith('##### '):
            p = doc.add_heading(line[6:], level=5)
            for run in p.runs:
                set_chinese_font(run, '微软雅黑', 12)
        elif line.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].rstrip().startswith('```'):
                code_lines.append(lines[i].rstrip())
                i += 1
            
            code_text = '\n'.join(code_lines)
            code_text = ''.join(char for char in code_text if ord(char) >= 32 or char in '\n\t')
            
            p = doc.add_paragraph(code_text)
            p.style = 'No Spacing'
            for run in p.runs:
                run.font.name = 'Consolas'
                run.font.size = Pt(10)
        elif line.startswith('- ') or line.startswith('* '):
            text = line[2:]
            p = doc.add_paragraph(text, style='List Bullet')
            for run in p.runs:
                set_chinese_font(run, '宋体', 12)
        elif re.match(r'^\d+\. ', line):
            text = re.sub(r'^\d+\. ', '', line)
            p = doc.add_paragraph(text, style='List Number')
            for run in p.runs:
                set_chinese_font(run, '宋体', 12)
        elif line.startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].rstrip().startswith('|'):
                table_lines.append(lines[i].rstrip())
                i += 1
            i -= 1
            
            if len(table_lines) > 1:
                headers = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
                rows = []
                for line in table_lines[2:]:
                    row = [cell.strip() for cell in line.split('|')[1:-1]]
                    rows.append(row)
                
                table = doc.add_table(rows=len(rows)+1, cols=len(headers))
                table.style = 'Light List Accent 1'
                
                for j, header in enumerate(headers):
                    cell = table.rows[0].cells[j]
                    cell.text = header
                    for paragraph in cell.paragraphs:
                        for run in paragraph.runs:
                            set_chinese_font(run, '微软雅黑', 11)
                            run.font.bold = True
                
                for i_row, row_data in enumerate(rows):
                    for j, cell_text in enumerate(row_data):
                        cell = table.rows[i_row+1].cells[j]
                        cell.text = cell_text
                        for paragraph in cell.paragraphs:
                            for run in paragraph.runs:
                                set_chinese_font(run, '宋体', 10)
        else:
            text = line
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            text = re.sub(r'\*(.+?)\*', r'\1', text)
            
            p = doc.add_paragraph(text)
            for run in p.runs:
                set_chinese_font(run, '宋体', 12)
        
        i += 1
    
    try:
        doc.save(docx_file)
        print(f'✅ 成功生成 {docx_file}')
        return True
    except Exception as e:
        print(f'❌ 错误: 无法保存文件 {docx_file}: {e}')
        return False


if __name__ == '__main__':
    md_file = 'skill.md'
    docx_file = 'skill.docx'
    parse_markdown_to_docx(md_file, docx_file)