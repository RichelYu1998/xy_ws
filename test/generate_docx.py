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
        self.heading_bookmarks = {}  # Store heading -> bookmark mapping for second pass
        self.nav_table_cell = None   # Reference to navigation table cell for post-processing

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


    def _post_process_navigation_links(self):
        """Post-process to ensure all navigation links have valid bookmarks"""
        from docx.oxml.shared import OxmlElement, qn
        
        # First pass: ensure all H2/H3 headings have bookmarks
        for para in self.doc.paragraphs:
            if para.style.name.startswith('Heading 2') or para.style.name.startswith('Heading 3'):
                text = para.text.strip()
                if text:
                    bookmark_id = self._generate_bookmark_id(text)
                    # Check if bookmark already exists
                    has_bookmark = False
                    for child in para._p:
                        if child.tag.endswith('bookmarkStart'):
                            has_bookmark = True
                            break
                    if not has_bookmark:
                        self._add_bookmark_to_paragraph(para, bookmark_id)
        
        # Second pass: update navigation table hyperlinks (if table exists and is nav table)
        if self.doc.tables:
            table = self.doc.tables[0]
            # Check if this is navigation table
            is_nav = False
            for cell in table.rows[0].cells:
                if '章节' in cell.text and ('位置' in cell.text or '说明' in cell.text):
                    is_nav = True
                    break
            
            if is_nav:
                for row in table.rows[1:]:
                    if len(row.cells) >= 3:
                        cell = row.cells[2]
                        for para in cell.paragraphs:
                            text = para.text.strip()
                            # Parse markdown link format
                            link_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', text)
                            if link_match:
                                display_text = link_match.group(1)
                                anchor = link_match.group(2).lstrip('#')
                                
                                # Clear existing content
                                para.clear()
                                
                                # Create new hyperlink with proper styling
                                hyperlink = OxmlElement('w:hyperlink')
                                hyperlink.set(qn('w:anchor'), anchor)
                                
                                run = OxmlElement('w:r')
                                rPr = OxmlElement('w:rPr')
                                
                                color = OxmlElement('w:color')
                                color.set(qn('w:val'), '0066CC')
                                rPr.append(color)
                                
                                u = OxmlElement('w:u')
                                u.set(qn('w:val'), 'single')
                                rPr.append(u)
                                
                                b = OxmlElement('w:b')
                                rPr.append(b)
                                
                                sz = OxmlElement('w:sz')
                                sz.set(qn('w:val'), '20')
                                rPr.append(sz)
                                
                                run.append(rPr)
                                
                                t_elem = OxmlElement('w:t')
                                t_elem.set(qn('xml:space'), 'preserve')
                                t_elem.text = f'🔗 {display_text}'
                                run.append(t_elem)
                                
                                hyperlink.append(run)
                                para._p.append(hyperlink)
                                
                                hint = para.add_run(' (点击跳转)')
                                hint.font.size = Pt(9)
                                hint.font.color.rgb = RGBColor(128, 128, 128)
                                hint.font.italic = True
    def _normalize_fences(self, lines):
        """Normalize markdown fences to match author's convention:
        - ```lang always opens a new block (close previous if open)
        - ``` always closes the nearest open block
        - Unclosed blocks auto-close at headings or EOF
        """
        result = []
        is_open = False

        for line in lines:
            if line.startswith('```'):
                lang = line[3:].strip()
                if lang:
                    if is_open:
                        result.append('```')
                    result.append(line)
                    is_open = True
                else:
                    if is_open:
                        result.append(line)
                        is_open = False
            elif is_open and re.match(r'^#{1,6}\s', line):
                result.append('```')
                is_open = False
                result.append(line)
            else:
                result.append(line)

        if is_open:
            result.append('```')

        return result

    def convert(self, md_path: str, output_path: str = 'skill.docx'):
        md_content = Path(md_path).read_text(encoding='utf-8')
        raw_lines = md_content.split('\n')
        lines = self._normalize_fences(raw_lines)

        # First pass: collect all heading bookmark IDs so navigation links
        # can reference them even though the nav table appears BEFORE the headings
        # Must also respect fence state!
        is_open = False
        for line in lines:
            if line.startswith('```'):
                lang = line[3:].strip()
                is_open = not is_open
            elif line.startswith('#') and not is_open:
                level = len(line) - len(line.lstrip('#'))
                text = line.lstrip('#').strip()
                if 2 <= level <= 3:
                    bookmark_id = self._generate_bookmark_id(text)
                    self.heading_bookmarks[bookmark_id] = None
        
        # Second pass: generate doc content
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
            # Add bookmark for navigation links (only for H2 and H3 headings)
            if level >= 2 and level <= 3:
                bookmark_id = self._generate_bookmark_id(text)
                self._add_bookmark_to_paragraph(para, bookmark_id)
                # Store mapping for later use
                self.heading_bookmarks[bookmark_id] = para
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
                    header_cells[i].text = self._clean_text(cell_text)
                    for paragraph in header_cells[i].paragraphs:
                        for run in paragraph.runs:
                            run.bold = True
                
                # Check if navigation table (detect keywords across ALL header cells)
                has_chapter = any('章节' in cell for cell in rows[0])
                has_location_or_desc = any('位置' in cell or '说明' in cell for cell in rows[0])
                is_nav_table = has_chapter and has_location_or_desc

                # Process data rows (add clickable links to last column)
                for row_data in rows[1:]:
                    row = table.add_row().cells
                    for i, cell_text in enumerate(row_data[:num_cols]):
                        if is_nav_table and i == num_cols - 1:
                            self._add_clickable_link(row[i], cell_text)
                        else:
                            row[i].text = self._clean_text(cell_text)

        return start_idx

    def _add_clickable_link(self, cell, text):
        cell.text = ''
        para = cell.paragraphs[0]

        link_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', text)

        if link_match:
            display_text = link_match.group(1)
            raw_anchor = link_match.group(2).lstrip('#')

            bookmark_id = self._find_heading_bookmark_id(raw_anchor)

            hyperlink = OxmlElement('w:hyperlink')
            hyperlink.set(qn('w:anchor'), bookmark_id)

            run = OxmlElement('w:r')
            rPr = OxmlElement('w:rPr')

            color = OxmlElement('w:color')
            color.set(qn('w:val'), '0066CC')
            rPr.append(color)

            u = OxmlElement('w:u')
            u.set(qn('w:val'), 'single')
            rPr.append(u)

            b = OxmlElement('w:b')
            rPr.append(b)

            run.append(rPr)

            t_elem = OxmlElement('w:t')
            t_elem.set(qn('xml:space'), 'preserve')
            t_elem.text = f'🔗 {display_text}'
            run.append(t_elem)

            hyperlink.append(run)
            para._p.append(hyperlink)
        else:
            run = para.add_run(text)
            run.font.size = Pt(10)


    def _generate_bookmark_id(self, title_text):
        """Generate bookmark ID from title text (GitHub-style)"""
        anchor = title_text.lower()
        anchor = re.sub(r'[^\w\s\-]', '', anchor)
        anchor = anchor.replace(' ', '-')
        anchor = re.sub(r'-+', '-', anchor)
        return anchor.strip('-')

    def _find_heading_bookmark_id(self, markdown_anchor):
        direct_id = self._generate_bookmark_id(markdown_anchor)
        if direct_id in self.heading_bookmarks:
            return direct_id
        if markdown_anchor in self.heading_bookmarks:
            return markdown_anchor
        direct_no_dash = direct_id.replace('-', '')
        for heading_bm_id in self.heading_bookmarks:
            if heading_bm_id in direct_id or direct_id in heading_bm_id:
                return heading_bm_id
            hb_no_dash = heading_bm_id.replace('-', '')
            if hb_no_dash == direct_no_dash:
                return heading_bm_id
            if hb_no_dash and direct_no_dash:
                if hb_no_dash in direct_no_dash or direct_no_dash in hb_no_dash:
                    return heading_bm_id
        return direct_id

    def _add_bookmark_to_paragraph(self, para, bookmark_name):
        """Add a Word bookmark to a paragraph"""
        from docx.oxml.shared import OxmlElement, qn
        
        # Create bookmark start
        bookmark_start = OxmlElement('w:bookmarkStart')
        bookmark_start.set(qn('w:id'), str(len(self.doc.element.body) + 1000))
        bookmark_start.set(qn('w:name'), bookmark_name)
        
        # Create bookmark end
        bookmark_end = OxmlElement('w:bookmarkEnd')
        bookmark_end.set(qn('w:id'), str(len(self.doc.element.body) + 1000))
        
        # Insert at beginning of paragraph
        para._p.insert(0, bookmark_start)
        para._p.append(bookmark_end)
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