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
    """Markdown → DOCX 转换器：负责样式预置、导航区置顶、书签锚点与表格渲染"""

    def __init__(self):
        """初始化转换器：新建文档、预置样式、准备书签映射"""
        self.doc = Document()
        self._setup_styles()
        self.heading_bookmarks = {}  # 标题书签映射：锚点 -> 段落对象
        self.nav_table_cell = None   # 导航表格单元格引用，供后处理使用

    @staticmethod
    def _clean_text(text):
        """清洗文本：剔除 Word 不接受的非法控制字符"""
        if not isinstance(text, str):
            text = str(text)
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)
        return text

    def _setup_styles(self):
        """预置正文与各级标题样式（中文字体、字号、颜色、行距）"""
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
        """后处理：确保所有导航链接都指向有效的书签锚点"""

        # 第一遍：保证所有 H2/H3 标题都已带上书签
        for para in self.doc.paragraphs:
            if para.style.name.startswith('Heading 2') or para.style.name.startswith('Heading 3'):
                text = para.text.strip()
                if text:
                    bookmark_id = self._generate_bookmark_id(text)
                    # 检查该段落是否已有书签，避免重复插入
                    has_bookmark = False
                    for child in para._p:
                        if child.tag.endswith('bookmarkStart'):
                            has_bookmark = True
                            break
                    if not has_bookmark:
                        self._add_bookmark_to_paragraph(para, bookmark_id)

        # 第二遍：把导航表格里的链接改写为内部超链接（仅当表格存在且确为导航表）
        if self.doc.tables:
            table = self.doc.tables[0]
            # 判断首张表格是否为导航表（表头同时含「章节」与「位置/说明」）
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
                            # 解析 markdown 链接格式 [显示文本](#锚点)
                            link_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', text)
                            if link_match:
                                display_text = link_match.group(1)
                                anchor = link_match.group(2).lstrip('#')

                                # 清空原有内容，避免残留纯文本
                                para.clear()

                                # 重建为带样式的内部超链接
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
        """规整 markdown 代码围栏，统一为作者的书写习惯：
        - 带语言的 ```lang 总是开启一个新块（若上一块未关闭则先补一个关闭围栏）
        - 不带语言的 ``` 总是关闭最近一个未关闭的块
        - 未关闭的块在遇到标题或文件末尾时自动补上关闭围栏
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
        """把 markdown 源文件完整转换为 docx 文档"""
        md_content = Path(md_path).read_text(encoding='utf-8')
        raw_lines = md_content.split('\n')
        lines = self._normalize_fences(raw_lines)

        # 把导航区块从正文中抽出来，保证它固定渲染在第 1 页，
        # 不受它在 markdown 源文件里所处位置的限制。
        nav_block, lines = self._extract_nav_block(lines)

        # 第一遍：先收集所有标题的书签 ID，因为导航表出现在标题之前，
        # 必须提前建好锚点映射才能生成有效链接；同时必须跟随代码围栏状态跳过代码块内内容。
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

        # 第二遍：按行生成文档正文内容
        nav_placed = False
        i = 0
        while i < len(lines):
            line = lines[i]
            
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                i = self._handle_heading(lines, i)
                if nav_block and not nav_placed and level == 1:
                    self._render_nav_block(nav_block)
                    nav_placed = True
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
        
        if nav_block and not nav_placed:
            self._render_nav_block(nav_block)

        self.doc.save(output_path)
        print(f'✅ 成功生成 {output_path}')
        return output_path

    def _extract_nav_block(self, lines):
        """识别导航区块（标题 + 引言 + 表格）并把它从正文中剪切出来。

        返回 (nav_block, remaining_lines)；当不存在导航表
        （表头同时含「章节」与「位置/说明」）时 nav_block 为 None。
        """
        for idx, line in enumerate(lines):
            if not (line.startswith('|') and '|' in line[1:]):
                continue
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            has_chapter = any('章节' in cell for cell in cells)
            has_location_or_desc = any(('位置' in cell or '说明' in cell) for cell in cells)
            if not (has_chapter and has_location_or_desc):
                continue

            start = idx
            j = idx - 1
            while j >= 0:
                stripped = lines[j].strip()
                if stripped == '' or stripped == '---' or stripped.startswith('>'):
                    j -= 1
                    continue
                break
            if j >= 0 and re.match(r'^#{1,3}\s', lines[j]):
                start = j

            end = idx
            while end < len(lines) and lines[end].startswith('|'):
                end += 1
            while end < len(lines) and lines[end].strip() in ('', '---'):
                end += 1

            block = lines[start:end]
            remaining = lines[:start] + lines[end:]
            return block, remaining
        return None, lines

    def _render_nav_block(self, block):
        """把导航区块渲染到第 1 页顶部，随后强制分页"""
        i = 0
        while i < len(block):
            line = block[i]
            if line.startswith('#'):
                i = self._handle_heading(block, i)
            elif line.startswith('>'):
                i = self._handle_blockquote(block, i)
            elif line.startswith('|') and '|' in line[1:]:
                i = self._handle_table(block, i)
            else:
                i += 1
        self.doc.add_page_break()

    def _handle_heading(self, lines, start_idx):
        """处理 markdown 标题行：写入标题样式，并为 H2/H3 挂上书签"""
        line = lines[start_idx]
        level = len(line) - len(line.lstrip('#'))
        text = line.lstrip('#').strip()

        if level <= 6:
            para = self.doc.add_heading(text, level=level if level > 0 else 0)
            # 只有 H2/H3 标题参与导航，为其添加书签锚点
            if level >= 2 and level <= 3:
                bookmark_id = self._generate_bookmark_id(text)
                self._add_bookmark_to_paragraph(para, bookmark_id)
                # 记录锚点与段落的映射，供后续导航链接查找
                self.heading_bookmarks[bookmark_id] = para
        else:
            para = self.doc.add_paragraph()
            run = para.add_run(text)
            run.bold = True
            run.font.size = Pt(11)
        
        return start_idx + 1

    def _handle_code_block(self, lines, start_idx):
        """处理代码块：整块渲染为等宽字体 + 浅灰底纹，保留原始换行"""
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
        """处理引用块：连续以 > 开头的行合并为一个左缩进段落"""
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
        """处理表格：跳过 --- 分隔行，导航表额外补一列可点击的跳转链接"""
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
                
                # 判断是否为导航表（在所有表头单元格里检索关键词）
                has_chapter = any('章节' in cell for cell in rows[0])
                has_location_or_desc = any('位置' in cell or '说明' in cell for cell in rows[0])
                is_nav_table = has_chapter and has_location_or_desc

                # 导航表在 docx 中追加第三列「位置（点击跳转）」
                docx_num_cols = num_cols + 1 if is_nav_table and num_cols == 2 else num_cols
                table = self.doc.add_table(rows=1, cols=docx_num_cols)
                table.style = 'Table Grid'
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                
                header_cells = table.rows[0].cells
                for i, cell_text in enumerate(rows[0][:num_cols]):
                    header_cells[i].text = self._clean_text(cell_text)
                    for paragraph in header_cells[i].paragraphs:
                        for run in paragraph.runs:
                            run.bold = True
                
                # 为导航表补写第三列表头
                if is_nav_table and num_cols == 2:
                    header_cells[2].text = '位置（点击跳转）'
                    for paragraph in header_cells[2].paragraphs:
                        for run in paragraph.runs:
                            run.bold = True

                # 逐行填充数据，导航表在最后一列写入可点击链接
                for row_data in rows[1:]:
                    row = table.add_row().cells
                    for i, cell_text in enumerate(row_data[:num_cols]):
                        row[i].text = self._clean_text(cell_text)

                    # 导航表：第三列按章节名生成内部跳转链接
                    if is_nav_table and num_cols == 2:
                        chapter_name = row_data[0].strip() if len(row_data) > 0 else ''
                        self._add_clickable_link(row[2], '点击跳转', chapter_name)

        return start_idx

    def _add_clickable_link(self, cell, text, chapter_name=None):
        """在单元格内写入内部超链接，锚点优先取 markdown 链接，其次取章节名"""
        cell.text = ''
        para = cell.paragraphs[0]

        # 先尝试解析markdown链接格式
        link_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', text)

        if link_match:
            display_text = link_match.group(1)
            raw_anchor = link_match.group(2).lstrip('#')
            bookmark_id = self._find_heading_bookmark_id(raw_anchor)
        elif chapter_name:
            # 如果是纯文本，直接用章节名生成链接
            display_text = text
            bookmark_id = self._find_heading_bookmark_id(chapter_name)
        else:
            # 最后fallback：直接显示文本
            run = para.add_run(text)
            run.font.size = Pt(10)
            return

        # 生成超链接
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


    def _generate_bookmark_id(self, title_text):
        """由标题文本生成书签名（模拟 GitHub 锚点规则：小写、去标点、空格转连字符）"""
        anchor = title_text.lower()
        anchor = re.sub(r'[^\w\s\-]', '', anchor)
        anchor = anchor.replace(' ', '-')
        anchor = re.sub(r'-+', '-', anchor)
        return anchor.strip('-')

    def _find_heading_bookmark_id(self, markdown_anchor):
        """按 markdown 锚点查找真实书签 ID：精确匹配 → 去连字符匹配 → 模糊包含匹配"""
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
        """给段落挂上 Word 书签（bookmarkStart + bookmarkEnd）"""

        # 书签起始标记
        bookmark_start = OxmlElement('w:bookmarkStart')
        bookmark_start.set(qn('w:id'), str(len(self.doc.element.body) + 1000))
        bookmark_start.set(qn('w:name'), bookmark_name)

        # 书签结束标记
        bookmark_end = OxmlElement('w:bookmarkEnd')
        bookmark_end.set(qn('w:id'), str(len(self.doc.element.body) + 1000))

        # 起始标记插到段首，结束标记追加到段尾
        para._p.insert(0, bookmark_start)
        para._p.append(bookmark_end)

    def _handle_list(self, lines, start_idx, ordered=False):
        """处理列表：无序列表加圆点前缀，有序列表保留原始编号"""
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
        """写入普通段落，交由格式化方法解析行内标记"""
        para = self.doc.add_paragraph()
        self._add_formatted_text(para, self._clean_text(text))

    def _add_formatted_text(self, paragraph, text):
        """解析行内标记：加粗 **、斜体 *、反引号代码、markdown 链接"""
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
                # 先尝试解析markdown链接格式
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
        """写入一条分隔线（段落底边框实现）"""
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
    """入口函数：读取项目根目录的 skill.md，生成同目录下的 skill.docx"""
    base_dir = Path(__file__).resolve().parent.parent
    md_path = str(base_dir / 'skill.md')
    docx_path = str(base_dir / 'skill.docx')

    print('📖 正在解析 skill.md...')
    
    converter = MarkdownToDocxConverter()
    
    print('📝 正在生成 skill.docx (完整版)...')
    output_file = converter.convert(md_path, docx_path)
    
    file_size = Path(output_file).stat().st_size
    print(f'✅ 完成! 文件大小: {file_size / 1024:.1f} KB')


if __name__ == '__main__':
    main()