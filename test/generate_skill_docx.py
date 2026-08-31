# -*- coding: utf-8 -*-
"""
从 skill.md 生成 skill.docx
遵循 UTF-8 编码规范和简体中文要求
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import re
from datetime import datetime

def create_skill_docx():
    """生成 skill.docx 文档"""

    doc = Document()

    # 设置文档默认字体为宋体（中文）
    style = doc.styles['Normal']
    font = style.font
    font.name = 'SimSun'
    font.size = Pt(11)
    style._element.rPr.rFonts.set(qn('w:eastAsia'), 'SimSun')

    # 标题
    title = doc.add_heading('微购相册开发技能文档 (Skill Documentation)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 版本信息
    version_para = doc.add_paragraph()
    version_run = version_para.add_run('📌 当前版本: v3.8.90.15 (2026-08-30)')
    version_run.bold = True
    version_run.font.size = Pt(14)
    version_run.font.color.rgb = RGBColor(0, 112, 192)

    # 版本标题
    subtitle = doc.add_paragraph()
    subtitle_run = subtitle.add_run('🎯 表格滚动联动增强 + 数据显示完整性修复 — 移动端表头固定+API数据量扩展+顶部同步检测')
    subtitle_run.font.size = Pt(12)
    subtitle_run.italic = True

    # 重要更新标题
    update_heading = doc.add_heading('⚠️ 重要更新', level=1)

    # 版本更新列表
    updates = [
        ('v3.8.90.15', '🎯', '表格滚动联动增强+数据显示完整性修复',
         '修复移动端表格表头消失问题(index.html CSS position static改sticky+top:0+z-index:10)，'
         '扩展API商品数据量限制(main.py products[:100]改[:500]两处统一500条)，'
         '增强多表格滚动联动功能(dist/app.js新增scrollTop<5顶部检测强制所有表格同步到scrollTop:0+双重requestAnimationFrame性能优化)'),

        ('v3.8.90.14', '🔒', '攻防纵深加固+隐藏Bug清零第三轮',
         '修复CSRF白名单阻断隧道回归Bug，新增日志注入防护，消除swagger版本硬编码与uvicorn host硬编码，'
         '修复8处API响应信息泄露')
    ]

    for version, emoji, title, desc in updates:
        para = doc.add_paragraph()
        version_run = para.add_run(f'- **{version}**: {emoji} **{title}** — ')
        version_run.bold = True
        desc_run = para.add_run(desc)

    # 本次更新详细内容
    detail_heading = doc.add_heading('📝 v3.8.90.15 详细更新内容', level=1)

    details = [
        {
            'title': '移动端表格表头固定修复 (UI-P1/Bug修复)',
            'content': [
                '问题：移动端(<576px)表格滚动时表头消失，用户无法看到列标题',
                '根因：index.html移动端CSS样式.change-table th设置position: static !important覆盖了sticky定位',
                '修复：将position: static !important改为position: sticky !important; top: 0; z-index: 10',
                '参考位置：index.html#L1099-L1104',
                '测试结果：✅ 移动端表格滚动时表头固定可见，桌面端无影响'
            ]
        },
        {
            'title': 'API商品数据量限制扩展 (功能-P2)',
            'content': [
                '问题：/api/products接口总商品列表仅返回前100个商品，导致部分商品无法显示',
                '根因：main.py第7762行和8029行设置products[:100]硬性截断',
                '修复：将两处products[:100]统一改为products[:500]，与高价商品数据量保持一致',
                '参考位置：main.py#L7762, main.py#L8029',
                '测试结果：✅ 总商品列表可显示前500个商品，货号35654等商品正常显示'
            ]
        },
        {
            'title': '多表格滚动联动顶部同步增强 (功能-P1)',
            'content': [
                '问题：多个商品表格滚动不同步，当下面表格滚到最上面时上面表格未同步到顶部',
                '原有逻辑：仅通过SKU行对齐进行滚动同步，未处理边界情况',
                '新增功能：检测源表格scrollTop<5时判定为"在顶部"，强制所有其他表格同步到scrollTop=0',
                '技术细节：容错5像素避免误判、遍历所有容器设置scrollTop=0、双重requestAnimationFrame性能优化',
                '参考位置：dist/app.js#L2573-L2587',
                '测试结果：✅ 高价商品表格滚到顶部时总商品列表自动同步到顶部，双向联动正常'
            ]
        }
    ]

    for detail in details:
        heading = doc.add_heading(detail['title'], level=2)
        for item in detail['content']:
            para = doc.add_paragraph(item, style='List Bullet')

    # 代码规范检查
    standard_heading = doc.add_heading('✅ 代码规范遵循 skill.md', level=1)

    standards = [
        'UTF-8编码：所有文件使用UTF-8保存，无BOM',
        '简体中文：注释、commit message、文档使用简体中文',
        '版本格式：遵循vX.X.XX.XX (YYYY-MM-DD)标准格式',
        'Changelog规范：包含影响文件、详细技术细节、参考位置、测试结果',
        '安全规范：无新增安全漏洞，CSS修改不影响CSP策略'
    ]

    for std in standards:
        para = doc.add_paragraph(std, style='List Bullet')

    # 验证结果
    test_heading = doc.add_heading('🧪 验证结果', level=1)

    tests = [
        ('移动端表头固定测试', '✅', 'Chrome DevTools模拟iPhone 12 Pro'),
        ('API数据量测试', '✅', '500条商品数据正常返回'),
        ('滚动联动测试', '✅', '顶部/中部/底部三场景均同步'),
        ('桌面端兼容性测试', '✅', 'Windows Chrome/Firefox/Edge'),
        ('语法检查', '✅', 'HTML/CSS/JS语法无误')
    ]

    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'

    header_cells = table.rows[0].cells
    headers = ['测试项', '结果', '备注']
    for i, header in enumerate(headers):
        header_cells[i].text = header
        for paragraph in header_cells[i].paragraphs:
            for run in paragraph.runs:
                run.bold = True

    for test_name, result, note in tests:
        row_cells = table.add_row().cells
        row_cells[0].text = test_name
        row_cells[1].text = result
        row_cells[2].text = note

    # 影响文件
    file_heading = doc.add_heading('📁 影响文件', level=1)

    files = [
        ('index.html', 'L1099-L1104', 'CSS表头固定样式修改'),
        ('main.py', 'L7762, L8029', 'API数据量限制扩展'),
        ('dist/app.js', 'L2573-L2587', '滚动联动顶部同步增强'),
        ('README.md', 'L385-L441', 'Changelog更新'),
        ('skill.md', 'L24-L32, L3709-L3710', '版本信息更新')
    ]

    file_table = doc.add_table(rows=1, cols=3)
    file_table.style = 'Table Grid'

    file_header_cells = file_table.rows[0].cells
    file_headers = ['文件路径', '行号', '修改说明']
    for i, header in enumerate(file_headers):
        file_header_cells[i].text = header
        for paragraph in file_header_cells[i].paragraphs:
            for run in paragraph.runs:
                run.bold = True

    for filepath, lines, desc in files:
        row_cells = file_table.add_row().cells
        row_cells[0].text = filepath
        row_cells[1].text = lines
        row_cells[2].text = desc

    # 生成时间
    time_para = doc.add_paragraph()
    time_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    time_run = time_para.add_run(f'生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    time_run.font.size = Pt(10)
    time_run.italic = True

    # 保存文档
    output_path = 'D:/ws/xy_ws/skill.docx'
    doc.save(output_path)
    print(f'✅ 成功生成 {output_path}')

if __name__ == '__main__':
    create_skill_docx()