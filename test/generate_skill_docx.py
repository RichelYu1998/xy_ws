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
    version_run = version_para.add_run('📌 当前版本: v4.6 (2026-08-31)')
    version_run.bold = True
    version_run.font.size = Pt(14)
    version_run.font.color.rgb = RGBColor(0, 112, 192)

    # 版本标题
    subtitle = doc.add_paragraph()
    subtitle_run = subtitle.add_run('🛡️ 全面安全审计 + Bug修复（重大安全升级）— 深度攻防审计全方位加固')
    subtitle_run.font.size = Pt(12)
    subtitle_run.italic = True

    # 重要更新标题
    update_heading = doc.add_heading('⚠️ 重要更新', level=1)

    # 版本更新列表
    updates = [
        ('v4.6', '🛡️', '全面安全审计+Bug修复（重大安全升级）',
         '对整个项目进行深度安全攻防审计修复所有发现的漏洞和Bug'
         '(SSRF防护系统_is_safe_url()禁止私有IP/云元数据/内网地址访问+并发安全_tunnel_state_lock线程锁保护全局变量'
         '+subprocess调用安全加强正则验证shell=False防命令注入+前端XSS风险修复escapeHtml转义动态HTML内容'
         '+异常信息统一化处理API不再泄露内部堆栈)'
         '(README.md/skill.md/skill.docx三份核心文档记录此次重大安全升级)，Git提交推送至仓库保持版本控制一致性'),

        ('v4.5', '🔧', '文件清理功能API修复+路径验证优化',
         '修复文件清理功能的422 Unprocessable Content错误(CleanDirectoryRequest.directory字段min_length=1改为默认空字符串)'
         '，优化路径验证逻辑(移除\'/\'和\'\\\\\'禁令允许绝对/相对路径输入)，统一所有清理请求模型行为'
         '(CleanDirectoryRequest/CleanGroupRequest新增dry_run参数)，安全性保障(sec_sp函数路径遍历防护仍然有效)'
         '，支持空目录自动处理(留空使用当前工作目录)+测试模式(dry_run参数全模式生效)'),

        ('v4.4', '🗑️', '临时修复脚本清理+项目规范化',
         '删除fix_line_endings.py行尾符修复临时脚本（已完成历史使命），严格遵循单文件架构原则'
         '（仅main.py作为主程序文件），避免额外的.py文件导致维护混乱，文档同步更新'
         '（README.md/skill.md/skill.docx三份核心文档记录此次清理操作），Git提交推送至仓库保持版本控制一致性'),

        ('v4.3', '💻', '启动脚本终端输出增强（跨平台）',
         '优化run.sh和run.bat启动脚本的终端显示功能，新增智能等待机制和多源数据提取逻辑，'
         '实现macOS/Linux和Windows双平台支持，用户体验显著提升')
    ]

    for version, emoji, title, desc in updates:
        para = doc.add_paragraph()
        version_run = para.add_run(f'- **{version}**: {emoji} **{title}** — ')
        version_run.bold = True
        desc_run = para.add_run(desc)

    # 本次更新详细内容
    detail_heading = doc.add_heading('📝 v4.6 详细更新内容', level=1)

    details = [
        {
            'title': 'SSRF防护系统新增 (安全加固-P0)',
            'content': [
                '问题现象：urllib.request.urlopen()可被利用访问内网资源、云元数据端点',
                '解决方案：实现_is_safe_url()函数进行URL安全验证',
                '防护范围：私有IP(10.x,172.16-31.x,192.168.x,127.x,169.254.x)+IPv6本地(::1,fe80::/10,fc00::/7)',
                '防护目标：云元数据(metadata.google.internal,metadata.amazonaws.com)+非法协议(非HTTP/HTTPS)',
                '集成位置：safe_urlopen()函数+send_heartbeat()心跳检测',
                '测试结果：✅ 拒绝访问私有IP/云元数据/内网地址'
            ]
        },
        {
            'title': '并发安全修复 (线程安全-P0)',
            'content': [
                '问题现象：tunnel_last_heartbeat/tunnel_heartbeat_failed等全局变量在多线程环境下缺乏保护',
                '解决方案：新增_tunnel_state_lock = threading.Lock()保护全局变量原子操作',
                '影响范围：send_heartbeat()+heartbeat_loop()两处关键位置',
                '技术实现：with _tunnel_state_lock: 语句块保证原子性',
                '防护效果：避免竞态条件导致的心跳状态不一致问题',
                '测试结果：✅ 多线程环境下状态一致性验证通过'
            ]
        },
        {
            'title': 'print语句残留修复 (规范合规-P0)',
            'content': [
                '问题现象：BOM工具(main.py:6782-6817)使用print()违反项目规范（应使用logging模块）',
                '影响位置：--fix-bom和--check-bom两个命令行功能的输出语句',
                '解决方案：所有print()调用改为_module_logger.info()调用',
                '符合规范：skill.md定义的编码标准（所有输出必须使用logging模块）',
                '附加改进：版本号从v4.1更新至v4.5反映当前版本',
                '测试结果：✅ 输出正常工作且符合项目规范'
            ]
        },
        {
            'title': 'subprocess调用安全加强 (注入防护-P1)',
            'content': [
                '问题现象：check_process_running()的process_name参数未充分验证可能存在命令注入风险',
                '解决方案：添加正则表达式验证 ^[a-zA-Z0-9._-]+$ + shell=False参数强制使用参数列表传递',
                '影响位置：Environment.check_process_running()方法',
                '防护效果：拒绝包含特殊字符的恶意进程名（如; rm -rf /等）',
                '兼容性：Windows(tasklist命令)和Linux(pgrep命令)双平台支持',
                '测试结果：✅ 恶意进程名被正则拦截，合法进程名正常工作'
            ]
        },
        {
            'title': '异常信息统一化处理 (信息泄露防护-P1)',
            'content': [
                '问题现象：security_check/security_audit/encrypt_init等API返回type(e).__name__泄露内部实现细节',
                '影响API：/api/security/check + /api/security/audit + /api/security/encrypt-init（共3个）',
                '解决方案：错误日志记录到服务端(logger.error+exc_info=True)，客户端仅返回通用错误消息',
                '安全原则：不向客户端暴露内部堆栈跟踪、类名、异常详情等技术信息',
                '用户体验：用户看到"操作失败，请查看服务器日志"而非技术性错误信息',
                '测试结果：✅ 客户端无法获取内部堆栈，服务端日志完整记录异常详情'
            ]
        },
        {
            'title': '前端XSS风险修复 (跨站脚本防护-P2)',
            'content': [
                '问题现象：changelog渲染中的item.title/item.desc动态内容直接插入innerHTML存在XSS风险',
                '影响位置：dist/app.js:1086(sectionTitle.innerHTML) + :1098-1100(itemTitle.innerHTML)',
                '解决方案：动态内容使用escapeHtml()函数转义后再插入HTML',
                '转义字符：<, >, \\", \', &, / 等特殊字符转为HTML实体',
                "防护效果：防止<script>alert('XSS')</script>等恶意脚本注入DOM",
                '测试结果：✅ 特殊字符正确转义显示为文本而非执行为脚本'
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
        ('fix_line_endings.py', '已删除', '行尾符修复临时脚本（清理）'),
        ('README.md', 'L196-L232', '新增v4.4 Changelog记录'),
        ('skill.md', 'L20-L24', '版本号升级至v4.4'),
        ('skill.docx', '重新生成', 'Word格式文档同步更新'),
        ('test/generate_skill_docx.py', 'L26-L102', '生成脚本版本信息更新')
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