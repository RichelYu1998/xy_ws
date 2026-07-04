import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

def set_run_font(run, font_name='微软雅黑', font_size=11, bold=False, italic=False, color=None):
    """统一设置字体"""
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font_name
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    if color:
        run.font.color.rgb = RGBColor(*color)

def parse_markdown_to_docx(md_file_path, docx_file_path):
    doc = Document()
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    in_code_block = False
    code_lines = []
    
    while i < len(lines):
        line = lines[i].rstrip('\n')
        
        # 代码块处理
        if line.startswith('```'):
            if in_code_block:
                # 结束代码块，写入文档
                for code_line in code_lines:
                    p = doc.add_paragraph()
                    p.paragraph_format.left_indent = Inches(0.3)
                    run = p.add_run(code_line)
                    set_run_font(run, 'Consolas', 9)
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
        
        # 空行
        if not line.strip():
            i += 1
            continue
        
        # 标题处理
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('#').strip()
            
            if level == 1:
                p = doc.add_heading(text, level=1)
            elif level == 2:
                p = doc.add_heading(text, level=2)
            elif level == 3:
                p = doc.add_heading(text, level=3)
            else:
                p = doc.add_paragraph()
                run = p.add_run(text)
                set_run_font(run, '微软雅黑', 14 - level, bold=True)
            
            i += 1
            continue
        
        # 表格处理
        if '|' in line and line.strip().startswith('|'):
            table_lines = []
            while i < len(lines) and '|' in lines[i] and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].rstrip('\n'))
                i += 1
            
            if len(table_lines) >= 2:
                # 解析表格
                rows = []
                for tl in table_lines[1:]:  # 跳过表头分隔符
                    cells = [c.strip() for c in tl.split('|')[1:-1]]
                    if cells and not all(c.replace('-', '').replace(':', '') == '' for c in cells):
                        rows.append(cells)
                
                if rows:
                    # 创建表格
                    num_cols = max(len(row) for row in rows)
                    table = doc.add_table(rows=len(rows), cols=num_cols)
                    table.style = 'Table Grid'
                    
                    for row_idx, row_data in enumerate(rows):
                        for col_idx, cell_text in enumerate(row_data):
                            if col_idx < num_cols:
                                cell = table.cell(row_idx, col_idx)
                                cell.text = ''
                                p = cell.paragraphs[0]
                                run = p.add_run(cell_text)
                                if row_idx == 0:
                                    set_run_font(run, '微软雅黑', 10, bold=True)
                                else:
                                    set_run_font(run, '微软雅黑', 10)
                
            continue
        
        # 引用处理
        if line.startswith('>'):
            quote_text = line.lstrip('> ').strip()
            p = doc.add_paragraph()
            run = p.add_run(quote_text)
            set_run_font(run, '微软雅黑', 10, italic=True, color=(128, 128, 128))
            i += 1
            continue
        
        # 列表处理
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            indent_level = (len(line) - len(line.lstrip())) // 2
            list_text = line.strip()[2:]
            
            # 处理 **粗体** 和 `代码`
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.left_indent = Inches(0.25 * indent_level)
            
            # 使用 • 或 ◦ 符号
            bullet_char = '◦' if indent_level > 0 else '•'
            
            # 解析格式化文本
            parts = re.split(r'(\*\*.*?\*\*|`[^`]+`)', list_text)
            for part in parts:
                if part.startswith('**') and part.endswith('**'):
                    run = p.add_run(part[2:-2])
                    set_run_font(run, '微软雅黑', 10, bold=True)
                elif part.startswith('`') and part.endswith('`'):
                    run = p.add_run(part[1:-1])
                    set_run_font(run, 'Consolas', 9)
                elif part == bullet_char or part.strip() == '':
                    continue
                else:
                    run = p.add_run(part)
                    set_run_font(run, '微软雅黑', 10)
            
            i += 1
            continue
        
        # 有序列表处理
        if re.match(r'^\s*\d+\.\s', line):
            match = re.match(r'^\s*(\d+)\.\s(.*)$', line)
            if match:
                num = match.group(1)
                list_text = match.group(2)
                p = doc.add_paragraph(style='List Number')
                
                parts = re.split(r'(\*\*.*?\*\*|`[^`]+`)', list_text)
                for part in parts:
                    if part.startswith('**') and part.endswith('**'):
                        run = p.add_run(part[2:-2])
                        set_run_font(run, '微软雅黑', 10, bold=True)
                    elif part.startswith('`') and part.endswith('`'):
                        run = p.add_run(part[1:-1])
                        set_run_font(run, 'Consolas', 9)
                    else:
                        run = p.add_run(part)
                        set_run_font(run, '微软雅黑', 10)
                
                i += 1
                continue
        
        # 普通段落
        p = doc.add_paragraph()
        
        # 处理内联格式
        parts = re.split(r'(\*\*.*?\*\*|`[^`]+`|\*.*?\*)', line)
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                run = p.add_run(part[2:-2])
                set_run_font(run, '微软雅黑', 11, bold=True)
            elif part.startswith('`') and part.endswith('`'):
                run = p.add_run(part[1:-1])
                set_run_font(run, 'Consolas', 9)
            elif part.startswith('*') and part.endswith('*'):
                run = p.add_run(part[1:-1])
                set_run_font(run, '微软雅黑', 11, italic=True)
            else:
                run = p.add_run(part)
                set_run_font(run, '微软雅黑', 11)
        
        i += 1
    
    # 保存文档
    doc.save(docx_file_path)
    print(f'✅ 已生成: {docx_file_path}')

if __name__ == '__main__':
    md_path = 'D:/ws/xy_ws/skill.md'
    docx_path = 'D:/ws/xy_ws/skill.docx'
    
    print('📝 开始生成 skill.docx...')
    parse_markdown_to_docx(md_path, docx_path)
    print(f'✅ 完成！共转换 {len(open(md_path, "r", encoding="utf-8").readlines())} 行 Markdown')