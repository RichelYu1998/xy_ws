# -*- coding: utf-8 -*-
"""
完整版文档生成器 - 从skill.md生成skill.docx
100%动态转换 - 支持所有Markdown特性
"""
import re
from pathlib import Path
from datetime import datetime
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


class MarkdownToDocxConverter:
    def __init__(self):
        self.doc = Document()
        self._setup_styles()

    @staticmethod
    def _clean_text(text):
        if not isinstance(text, str):
            text = str(text)
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)
        return text

    def _setup_styles(self):
        style = self.doc.styles['Normal']
        font = style.font
        font.name = 'Microsoft YaHei'
        font.size = Pt(11)
        style.paragraph_format.space_after = Pt(6)
        style.paragraph_format.line_spacing = 1.5

        for i in range(0, 7):
            if i == 0:
                heading_style = self.doc.styles['Title']
            else:
                heading_style = self.doc.styles[f'Heading {i}']
            
            font = heading_style.font
            font.name = 'Microsoft YaHei'
            font.bold = True
            if i == 0:
                font.size = Pt(24)
                font.color.rgb = RGBColor(0, 51, 102)
            elif i == 1:
                font.size = Pt(18)
                font.color.rgb = RGBColor(0, 76, 153)
            elif i == 2:
                font.size = Pt(16)
                font.color.rgb = RGBColor(0, 102, 153)
            elif i == 3:
                font.size = Pt(14)
                font.color.rgb = RGBColor(51, 102, 153)
            else:
                font.size = Pt(12)
                font.color.rgb = RGBColor(51, 51, 51)

    def convert(self, md_path: str, output_path: str = 'skill.docx'):
        md_content = Path(md_path).read_text(encoding='utf-8')
        lines = md_content.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            if line.startswith('#'):
                i = self._handle_heading(lines, i)
            elif line.startswith('```'):
                i = self._handle_code_block(lines, i)
            elif line.startswith('>'):
                i = self._handle_blockquote(lines, i)
            elif line.startswith('|') and '|' in line[1:]:
                i = self._handle_table(lines, i)
            elif line.strip() == '---':
                self._add_horizontal_rule()
                i += 1
            elif re.match(r'^\s*[-*+]\s', line):
                i = self._handle_list(lines, i, ordered=False)
            elif re.match(r'^\s*\d+\.\s', line):
                i = self._handle_list(lines, i, ordered=True)
            elif line.strip():
                self._add_paragraph(line)
                i += 1
            else:
                i += 1
        
        self.doc.save(output_path)
        print(f'✅ 成功生成 {output_path}')
        return output_path

    def _handle_heading(self, lines, start_idx):
        line = lines[start_idx]
        level = len(line) - len(line.lstrip('#'))
        text = line.lstrip('#').strip()
        
        if level <= 6:
            para = self.doc.add_heading(text, level=level if level > 0 else 0)
        else:
            para = self.doc.add_paragraph()
            run = para.add_run(text)
            run.bold = True
            run.font.size = Pt(11)
        
        return start_idx + 1

    def _handle_code_block(self, lines, start_idx):
        first_line = lines[start_idx]
        language = first_line[3:].strip() if len(first_line) > 3 else ''
        
        code_lines = []
        start_idx += 1
        while start_idx < len(lines) and not lines[start_idx].startswith('```'):
            code_lines.append(lines[start_idx])
            start_idx += 1
        
        code_text = '\n'.join(code_lines)
        code_text = self._clean_text(code_text)
        
        para = self.doc.add_paragraph()
        para.paragraph_format.left_indent = Cm(1)
        para.paragraph_format.space_before = Pt(6)
        para.paragraph_format.space_after = Pt(6)
        
        run = para.add_run(code_text)
        run.font.name = 'Consolas'
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 128)
        
        run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Consolas')
        
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), 'F5F5F5')
        para._element.get_or_add_pPr().append(shading)
        
        return start_idx + 1

    def _handle_blockquote(self, lines, start_idx):
        quote_lines = []
        while start_idx < len(lines) and lines[start_idx].startswith('>'):
            quote_text = lines[start_idx].lstrip('>').strip()
            quote_lines.append(quote_text)
            start_idx += 1
        
        para = self.doc.add_paragraph()
        para.paragraph_format.left_indent = Cm(1)
        
        full_text = '\n'.join(quote_lines)
        self._add_formatted_text(para, full_text)
        
        return start_idx

    def _handle_table(self, lines, start_idx):
        table_lines = []
        while start_idx < len(lines) and lines[start_idx].startswith('|'):
            table_lines.append(lines[start_idx])
            start_idx += 1
        
        if len(table_lines) >= 2:
            rows = []
            for line in table_lines:
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                if not all(cell.replace('-', '').strip() == '' for cell in cells):
                    rows.append(cells)
            
            if rows:
                num_cols = max(len(row) for row in rows) if rows else 3
                table = self.doc.add_table(rows=1, cols=num_cols)
                table.style = 'Table Grid'
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                
                header_cells = table.rows[0].cells
                for i, cell_text in enumerate(rows[0][:num_cols]):
                    header_cells[i].text = cell_text
                    for paragraph in header_cells[i].paragraphs:
                        for run in paragraph.runs:
                            run.bold = True
                
                for row_data in rows[1:]:
                    row = table.add_row().cells
                    for i, cell_text in enumerate(row_data[:num_cols]):
                        row[i].text = cell_text
        
        return start_idx

    def _handle_list(self, lines, start_idx, ordered=False):
        while start_idx < len(lines):
            line = lines[start_idx]
            
            if ordered:
                match = re.match(r'^\s*\d+\.\s+(.*)', line)
            else:
                match = re.match(r'^\s*[-*+]\s+(.*)', line)
            
            if match:
                item_text = match.group(1).strip()
                
                para = self.doc.add_paragraph()
                if ordered:
                    pass
                else:
                    run = para.add_run("• ")
                    run.bold = True
                
                if item_text:
                    self._add_formatted_text(para, self._clean_text(item_text))
                
                start_idx += 1
            else:
                break
        
        return start_idx

    def _add_paragraph(self, text):
        para = self.doc.add_paragraph()
        self._add_formatted_text(para, self._clean_text(text))

    def _add_formatted_text(self, paragraph, text):
        pattern = r'(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\[[^\]]+\]\([^)]+\))'
        parts = re.split(pattern, text)
        
        for part in parts:
            if not part:
                continue
            
            if part.startswith('**') and part.endswith('**'):
                run = paragraph.add_run(part[2:-2])
                run.bold = True
            elif part.startswith('*') and part.endswith('*'):
                run = paragraph.add_run(part[1:-1])
                run.italic = True
            elif part.startswith('`') and part.endswith('`'):
                run = paragraph.add_run(part[1:-1])
                run.font.name = 'Consolas'
                run.font.size = Pt(10)
                run.font.color.rgb = RGBColor(128, 0, 0)
                run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Consolas')
            elif part.startswith('[') and '](' in part:
                link_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', part)
                if link_match:
                    link_text = link_match.group(1)
                    link_url = link_match.group(2)
                    
                    run = paragraph.add_run(link_text)
                    run.underline = True
                    run.font.color.rgb = RGBColor(0, 0, 255)
            else:
                paragraph.add_run(self._clean_text(part))

    def _add_horizontal_rule(self):
        para = self.doc.add_paragraph()
        para.paragraph_format.space_before = Pt(12)
        para.paragraph_format.space_after = Pt(12)
        
        pBdr = OxmlElement('w:pBdr')
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '6')
        bottom.set(qn('w:space'), '1')
        bottom.set(qn('w:color'), 'auto')
        pBdr.append(bottom)
        para._element.get_or_add_pPr().append(pBdr)


def main():
    print('📖 正在解析 skill.md...')
    
    converter = MarkdownToDocxConverter()
    
    print('📝 正在生成 skill.docx (完整版)...')
    output_file = converter.convert('skill.md', 'skill.docx')
    
    file_size = Path(output_file).stat().st_size
    print(f'✅ 完成! 文件大小: {file_size / 1024:.1f} KB')


if __name__ == '__main__':
    main()