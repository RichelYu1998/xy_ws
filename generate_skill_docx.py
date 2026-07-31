# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import os
import shutil

def create_skill_document():
    doc = Document()
    
    # 设置文档标题
    title = doc.add_heading('微购相册开发技能文档 (Skill Documentation)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # 添加概述
    doc.add_paragraph('作者：小旭二手机（西园路）')
    doc.add_paragraph('本文档定义了微购相册管理系统的完整代码开发规范、架构设计、最佳实践和技术标准。')
    doc.add_paragraph('')
    
    # 添加版本信息
    doc.add_heading('📋 版本信息', level=1)
    version_table = doc.add_table(rows=4, cols=2)
    version_table.style = 'Table Grid'
    version_data = [
        ('文档版本', 'v3.8.89.12'),
        ('最后更新', '2026-07-31'),
        ('适用范围', '微购相册管理系统全栈开发'),
        ('维护者', '小旭数码开发团队')
    ]
    for i, (key, value) in enumerate(version_data):
        version_table.rows[i].cells[0].text = key
        version_table.rows[i].cells[1].text = value
    
    doc.add_paragraph('')
    
    # 添加最新更新记录
    doc.add_heading('🔄 最新更新 - v3.8.89.12', level=1)
    
    update_para = doc.add_paragraph()
    update_para.add_run('🎯 对比数据字段匹配修复 + PC端显示优化').bold = True
    
    doc.add_paragraph('')
    doc.add_paragraph('问题：删除/新增商品对比中售价显示为"-", 且PC端难以查看对比结果', style='Intense Quote')
    
    doc.add_heading('现象', level=2)
    phenomena = [
        '爬虫运行日志显示删除商品 58187 的售价为 ¥5,899，但前端表格显示为 -',
        '新增商品的售价、商品名称等字段也显示为 -',
        '移动端能正常看到对比卡片，但PC端需要手动滚动才能看到'
    ]
    for p in phenomena:
        doc.add_paragraph(p, style='List Bullet')
    
    doc.add_heading('根本原因', level=2)
    reasons = [
        '后端字段名错误：get_product_detail() 函数使用 "商品名称" 字段，但实际JSON数据中使用的是 "商品描述"',
        '前端解析不健壮：前端正则只匹配单一字段名，未兼容其他可能的字段名',
        'PC端体验缺失：移动端会自动滚动到顶部查看对比结果，但PC端没有类似优化'
    ]
    for r in reasons:
        doc.add_paragraph(r, style='List Number')
    
    doc.add_heading('修复方案', level=2)
    
    # 修复1
    doc.add_paragraph('修复1：后端字段名兼容 (main.py:4520-4529)', style='Heading 3')
    code1 = '''# ❌ 修复前：使用错误的字段名
def get_product_detail(item):
    return {
        "商品名称": item.get('商品名称', ''),  # 数据中是"商品描述"
        ...
    }

# ✅ 修复后：多字段名兼容 + 中英文段别名支持
def get_product_detail(item):
    return {
        "商品描述": item.get('商品描述', '') or item.get('name', '') or item.get('商品名称', ''),
        "售价": item.get('售价', '') or item.get('price', ''),
        "货号": item.get('货号', '') or item.get('stock_number', ''),
        "备注": item.get('备注', '') or item.get('remark', ''),
        "员工": item.get('员工', '') or item.get('staff', '')
    }'''
    doc.add_paragraph(code1, style='No Spacing')
    
    # 修复2
    doc.add_paragraph('修复2：前端正则增强 (dist/app.js:1527-1540)', style='Heading 3')
    code2 = '''// ❌ 修复前：只匹配单一字段名
const nameMatch = line.match(/"商品描述":\\s*"([^"]+)"/);
const priceMatch = line.match(/"售价":\\s*"([^"]+)"/);

// ✅ 修复后：多字段名兼容匹配
const nameMatch = line.match(/"商品描述":\\s*"([^"]+)"/) 
               || line.match(/"商品名称":\\s*"([^"]+)"/) 
               || line.match(/"name":\\s*"([^"]+)"/);
const priceMatch = line.match(/"售价":\\s*"([^"]+)"/) 
                 || line.match(/"price":\\s*"([^"]+)"/);'''
    doc.add_paragraph(code2, style='No Spacing')
    
    # 修复3
    doc.add_paragraph('修复3：PC端自动定位 (dist/app.js:1984-1997)', style='Heading 3')
    code3 = '''// ❌ 修复前：只有移动端才自动滚动
const isMobile = window.innerWidth < 576;
if (isMobile) {
    spiderOutputContent.scrollTop = 0;
}

// ✅ 修复后：移动端滚动到顶，PC端滚动到卡片位置+动画提示
if (isMobile) {
    spiderOutputContent.scrollTop = 0;
} else {
    const comparisonCard = spiderOutputContent.querySelector('.comparison-card:last-child');
    if (comparisonCard) {
        comparisonCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
        comparisonCard.style.animation = 'pulse 2s ease-in-out 3';
    }
}'''
    doc.add_paragraph(code3, style='No Spacing')
    
    # 修复效果表
    doc.add_heading('修复效果', level=2)
    effect_table = doc.add_table(rows=6, cols=3)
    effect_table.style = 'Table Grid'
    effect_headers = ['指标', '修复前', '修复后']
    effect_data = [
        ['删除商品售价', '显示 - ❌', '显示 ¥5,899 ✅'],
        ['新增商品名称', '为空 ❌', '正确显示 ✅'],
        ['字段匹配率', '单一匹配 ❌', '多重兼容 ✅'],
        ['移动端体验', '自动滚动 ✅', '保持不变 ✅'],
        ['PC端体验', '需手动查找 ❌', '自动定位+动画 ✅']
    ]
    for j, header in enumerate(effect_headers):
        effect_table.rows[0].cells[j].text = header
        effect_table.rows[0].cells[j].paragraphs[0].runs[0].bold = True
    for i, row_data in enumerate(effect_data, 1):
        for j, cell_text in enumerate(row_data):
            effect_table.rows[i].cells[j].text = cell_text
    
    doc.add_paragraph('')
    
    # 添加技术范式章节
    doc.add_heading('🔴 PY-CORE-007: 字段名兼容性范式', level=1)
    
    doc.add_paragraph('由于JSON数据同时存储中文字段名和英文字段名，所有数据提取和解析代码必须实现多重字段名兼容。')
    
    doc.add_heading('核心原则', level=2)
    
    principles = [
        ('后端字段提取', '使用 or 链式调用，返回第一个非空值'),
        ('前端正则匹配', '使用 || 操作符连接多个正则表达式'),
        ('数据流完整性', '每个环节都必须兼容多种字段名格式'),
        ('默认值处理', '空值统一显示为 -，保持界面整洁')
    ]
    for principle, desc in principles:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(principle + ': ').bold = True
        p.add_run(desc)
    
    doc.add_heading('应用场景', level=2)
    scenarios_table = doc.add_table(rows=5, cols=3)
    scenarios_table.style = 'Table Grid'
    scenarios_headers = ['场景', '文件位置', '说明']
    scenarios_data = [
        ['删除商品对比', 'main.py:4520-4529', '从旧数据中提取被删除商品的详细信息'],
        ['新增商品对比', 'main.py:4520-4529', '从新数据中提取新增商品的详细信息'],
        ['前端表格渲染', 'dist/app.js:1527-1540', '解析后端输出的JSON字符串并渲染为表格'],
        ['API响应处理', 'dist/app.js:6947+', '处理 /api/products 返回的商品列表']
    ]
    for j, header in enumerate(scenarios_headers):
        scenarios_table.rows[0].cells[j].text = header
        scenarios_table.rows[0].cells[j].paragraphs[0].runs[0].bold = True
    for i, row_data in enumerate(scenarios_data, 1):
        for j, cell_text in enumerate(row_data):
            scenarios_table.rows[i].cells[j].text = cell_text
    
    doc.add_paragraph('')
    
    # 添加响应式体验一致性范式
    doc.add_heading('🔴 JS-FRONT-001: 响应式体验一致性范式', level=1)
    
    doc.add_paragraph('确保移动端和PC端在功能体验上保持一致，不能因为设备差异导致功能可用性不同。')
    
    doc.add_heading('设计原则', level=2)
    design_principles = [
        ('移动端优先', '小屏幕空间有限，直接滚动到顶部查看最新内容'),
        ('PC端增强', '大屏幕空间充足，精确滚动到目标位置 + 动画提示用户注意'),
        ('渐进增强', '基础功能一致，高级体验根据设备能力差异化提供')
    ]
    for principle, desc in design_principles:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(principle + ': ').bold = True
        p.add_run(desc)
    
    doc.add_paragraph('')
    
    # 添加Git提交规范
    doc.add_heading('🛠️ Git提交规范', level=1)
    
    doc.add_heading('Commit Message 格式', level=2)
    commit_format = '<type>(<scope>): <subject>\n\n<body>\n\n<footer>'
    doc.add_paragraph(commit_format, style='No Spacing')
    
    doc.add_heading('Type 类型', level=3)
    types = [
        'feat: 新功能',
        'fix: Bug修复',
        'docs: 文档更新',
        'style: 代码格式调整（不影响功能）',
        'refactor: 重构（不是新功能也不是修复bug）',
        'perf: 性能优化',
        'test: 测试相关',
        'chore: 构建/工具/辅助工具的变动'
    ]
    for t in types:
        doc.add_paragraph(t, style='List Bullet')
    
    doc.add_heading('Scope 范围', level=3)
    scopes = [
        'backend: Python后端 (main.py)',
        'frontend: JavaScript前端 (dist/app.js)',
        'docs: 文档 (README.md, skill.md)',
        'config: 配置文件',
        'deploy: 部署相关'
    ]
    for s in scopes:
        doc.add_paragraph(s, style='List Bullet')
    
    doc.add_paragraph('')
    
    # 添加字段映射速查表
    doc.add_heading('📖 附录A: 字段映射速查表', level=1)
    
    doc.add_heading('商品数据字段映射', level=2)
    field_mapping_table = doc.add_table(rows=9, cols=4)
    field_mapping_table.style = 'Table Grid'
    field_headers = ['业务含义', '主字段名（中文）', '英文别名', '示例值']
    field_data = [
        ['商品名称', '商品描述', 'name', 'iPhone 16 Pro Max'],
        ['售价', '售价', 'price', '¥5,899'],
        ['拿货价', '拿货价', 'cost_price', '¥4,500'],
        ['货号', '货号', 'stock_number', '58187'],
        ['备注', '备注', 'remark', '屏幕有划痕'],
        ['员工', '员工', 'staff', '店长'],
        ['入库时间', '入库时间', 'created_time', '3小时前'],
        ['图片列表', '图片', 'image', '[base64...]']
    ]
    for j, header in enumerate(field_headers):
        field_mapping_table.rows[0].cells[j].text = header
        field_mapping_table.rows[0].cells[j].paragraphs[0].runs[0].bold = True
    for i, row_data in enumerate(field_data, 1):
        for j, cell_text in enumerate(row_data):
            field_mapping_table.rows[i].cells[j].text = cell_text
    
    doc.add_paragraph('')
    
    # 添加常见问题排查指南
    doc.add_heading('📖 附录B: 常见问题排查指南', level=1)
    
    doc.add_heading('Q1: 为什么删除商品的售价显示为"-"？', level=2)
    q1_content = '''
症状：后端日志显示售价为 ¥5,899，但前端表格显示 -

排查步骤：
1. 检查 main.py:4520 的 get_product_detail() 函数
2. 确认字段名是否正确（应该是 "商品描述" 而非 "商品名称"）
3. 检查前端 dist/app.js:1528 的正则表达式是否匹配该字段名
4. 查看浏览器控制台的 [对比卡片] 日志确认解析结果

解决方案：
- 更新 get_product_detail() 使用多字段名兼容（PY-CORE-007）
- 增强前端正则支持多模式匹配'''
    doc.add_paragraph(q1_content)
    
    doc.add_heading('Q2: 为什么PC端看不到对比卡片？', level=2)
    q2_content = '''
症状：移动端能正常显示，但PC端需要手动滚动才能找到

排查步骤：
1. 打开浏览器开发者工具（F12）切换到Console标签
2. 查找 [对比卡片] ✅ 卡片可见性检查 日志
3. 检查卡片的 width 和 height 是否为0
4. 确认CSS是否隐藏了该元素

解决方案：
- 在 dist/app.js:1984 添加PC端的 scrollIntoView() 调用
- 为卡片添加脉冲动画提醒用户注意'''
    doc.add_paragraph(q2_content)
    
    # 保存文档（先保存到临时文件，再移动）
    import tempfile
    temp_fd, temp_path = tempfile.mkstemp(suffix='.docx')
    os.close(temp_fd)
    
    doc.save(temp_path)
    
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skill.docx')
    
    # 如果目标文件存在，尝试删除
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
        except:
            pass
    
    # 移动临时文件到目标位置
    shutil.move(temp_path, output_path)
    
    print(f'✅ skill.docx 已成功生成: {output_path}')
    return output_path

if __name__ == '__main__':
    create_skill_document()