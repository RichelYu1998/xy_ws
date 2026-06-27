#!/usr/bin/env python3
import re
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(PROJECT_DIR, 'skill.md')
DOCX_PATH = os.path.join(PROJECT_DIR, 'skill.docx')

FONT_WEST = 'Consolas'
FONT_EAST = 'Microsoft YaHei'
FONT_BODY_WEST = 'Calibri'
FONT_BODY_EAST = 'Microsoft YaHei'
CODE_SIZE = Pt(9)
BODY_SIZE = Pt(10.5)
HEADING1_SIZE = Pt(22)
HEADING2_SIZE = Pt(16)
HEADING3_SIZE = Pt(13)
HEADING4_SIZE = Pt(11)
FONT_WEST_H = 'Calibri'
FONT_EAST_H = 'Microsoft YaHei'


def set_run_font(run, west=FONT_WEST, east=FONT_EAST, size=BODY_SIZE, bold=False, italic=False, color=None):
    run.font.size = size
    run.bold = bold
    run.italic = italic
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} />')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:ascii'), west)
    rFonts.set(qn('w:hAnsi'), west)
    rFonts.set(qn('w:eastAsia'), east)
    if color:
        run.font.color.rgb = color


def add_body_paragraph(doc, text, style=None):
    p = doc.add_paragraph()
    if style:
        p.style = doc.styles[style]
    run = p.add_run(text)
    set_run_font(run, west=FONT_BODY_WEST, east=FONT_BODY_EAST, size=BODY_SIZE)
    return p


def add_heading(doc, text, level):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        sizes = {1: HEADING1_SIZE, 2: HEADING2_SIZE, 3: HEADING3_SIZE, 4: HEADING4_SIZE}
        set_run_font(run, west=FONT_WEST_H, east=FONT_EAST_H, size=sizes.get(level, BODY_SIZE), bold=True)
    return h


def add_code_block(doc, code_lines):
    for line in code_lines:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.3)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = Pt(14)
        run = p.add_run(line)
        set_run_font(run, west=FONT_WEST, east=FONT_EAST, size=CODE_SIZE)
    # separate from next paragraph
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run('')
    set_run_font(run, size=Pt(1))


def add_inline_paragraph(doc, text, indent_level=0):
    p = doc.add_paragraph()
    if indent_level > 0:
        p.paragraph_format.left_indent = Inches(0.3 * indent_level)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    parse_inline_runs(p, text)
    return p


def parse_inline_runs(p, text):
    parts = re.split(r'(\*\*.*?\*\*|`.*?`)', text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = p.add_run(part[2:-2])
            set_run_font(run, west=FONT_BODY_WEST, east=FONT_BODY_EAST, size=BODY_SIZE, bold=True)
        elif part.startswith('`') and part.endswith('`'):
            run = p.add_run(part[1:-1])
            set_run_font(run, west=FONT_WEST, east=FONT_EAST, size=CODE_SIZE)
        else:
            run = p.add_run(part)
            set_run_font(run, west=FONT_BODY_WEST, east=FONT_BODY_EAST, size=BODY_SIZE)
    return p


def add_list_item(doc, text, indent_level=0):
    p = doc.add_paragraph()
    if indent_level > 0:
        p.paragraph_format.left_indent = Inches(0.3 * (indent_level + 1))
    else:
        p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    bullet = '◦' if indent_level > 0 else '•'
    run = p.add_run(bullet + ' ')
    set_run_font(run, west=FONT_BODY_WEST, east=FONT_BODY_EAST, size=BODY_SIZE)
    parse_inline_runs(p, text)
    return p


def add_quote(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    set_run_font(run, west=FONT_BODY_WEST, east=FONT_BODY_EAST, size=BODY_SIZE, italic=True,
                 color=RGBColor(128, 128, 128))
    return p


def add_table_from_md(doc, rows_data):
    if not rows_data:
        return
    num_cols = max(len(row) for row in rows_data)
    table = doc.add_table(rows=len(rows_data), cols=num_cols)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.LEFT

    for i, row_data in enumerate(rows_data):
        for j, cell_text in enumerate(row_data):
            if j >= num_cols:
                break
            cell = table.cell(i, j)
            cell.text = ''
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(cell_text.strip())
            is_header = (i == 0)
            set_run_font(run, west=FONT_BODY_WEST, east=FONT_BODY_EAST, size=Pt(9), bold=is_header)
            if is_header:
                shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="D9E2F3"/>')
                cell._element.get_or_add_tcPr().append(shading)

    doc.add_paragraph()


def add_horizontal_rule(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    pPr = p._element.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}>'
                     '<w:bottom w:val="single" w:sz="6" w:space="1" w:color="CCCCCC"/>'
                     '</w:pBdr>')
    pPr.append(pBdr)


def generate_docx():
    doc = Document()

    style = doc.styles['Normal']
    style.font.size = BODY_SIZE
    style.font.name = FONT_BODY_WEST
    rPr = style.element.get_or_add_rPr()
    rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{FONT_BODY_WEST}" '
                       f'w:hAnsi="{FONT_BODY_WEST}" w:eastAsia="{FONT_BODY_EAST}"/>')
    rPr.insert(0, rFonts)

    with open(MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    i = 0
    in_code_block = False
    code_lines = []
    in_table = False
    table_rows = []

    while i < len(lines):
        line = lines[i]

        if line.startswith('```'):
            if in_code_block:
                add_code_block(doc, code_lines)
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        if line.startswith('---'):
            add_horizontal_rule(doc)
            i += 1
            continue

        if line.startswith('> '):
            add_quote(doc, line[2:])
            i += 1
            continue

        if line.startswith('|') and line.strip().endswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            if not re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                cells = [c.strip() for c in line.strip().split('|')]
                if cells and cells[0] == '':
                    cells = cells[1:]
                if cells and cells[-1] == '':
                    cells = cells[:-1]
                table_rows.append(cells)
            i += 1
            continue
        elif in_table:
            add_table_from_md(doc, table_rows)
            table_rows = []
            in_table = False

        if line.strip() == '':
            if in_table:
                add_table_from_md(doc, table_rows)
                table_rows = []
                in_table = False
            i += 1
            continue

        stripped = line.lstrip()
        indent = (len(line) - len(stripped)) // 2

        if stripped.startswith('# '):
            add_heading(doc, stripped[2:], 1)
        elif stripped.startswith('## '):
            add_heading(doc, stripped[3:], 2)
        elif stripped.startswith('### '):
            add_heading(doc, stripped[4:], 3)
        elif stripped.startswith('#### '):
            add_heading(doc, stripped[5:], 4)
        elif stripped.startswith('- '):
            item_text = stripped[2:]
            add_list_item(doc, item_text, indent)
        elif indent > 0 and stripped.startswith('- '):
            item_text = stripped[2:]
            add_list_item(doc, item_text, indent)
        elif stripped.startswith('**') and (stripped.endswith('**') or '**' in stripped[2:]):
            add_inline_paragraph(doc, stripped)
        elif re.match(r'^\d+\.\s', stripped):
            add_inline_paragraph(doc, stripped)
        else:
            add_inline_paragraph(doc, stripped)

        i += 1

    if in_table:
        add_table_from_md(doc, table_rows)

    if in_code_block:
        add_code_block(doc, code_lines)

    doc.save(DOCX_PATH)
    print(f'skill.docx generated successfully at {DOCX_PATH}')


if __name__ == '__main__':
    generate_docx()