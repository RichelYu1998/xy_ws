# -*- coding: utf-8 -*-
"""
阿里巴巴代码规范合规检查脚本（Python / JavaScript 适配版）
遵循 UTF-8 编码 + 简体中文规范

功能：
1. 异常处理规范（禁止静默 pass、禁止裸 except、异常变量必须被使用）
2. 命名规范（snake_case / CamelCase / UPPER_CASE / camelCase）
3. 语句规范（禁止 var、禁止 alert、禁止 == / !=、禁止 eval）
4. 结构与体量规范（函数行数、单行字符数，存量基线冻结、只减不增）
5. 配置规范（禁止裸魔法数字超时值，必须走 TIMEOUT_CONFIG / 环境变量）
6. 编码与标记规范（UTF-8 无 BOM、禁止 TODO/FIXME 遗留标记）

扫描范围：
- Python：自动发现项目内全部 .py（排除 .venv / node_modules / tools / temp / file），
  新增文件无需手工登记，落盘即纳入扫描，基线默认 0；
- JavaScript：dist/app.js（构建产物 bundle 为压缩代码，不纳入扫描）。

用法：python test/code_style_check.py
      python test/code_style_check.py --selftest   （闸门自检：探针只写系统临时目录）
时机：每次改动代码后（含新增 .py）必须跑一遍，退出码 0 才允许提交
退出码：0 = 零问题达标；1 = 存在违规
"""

import ast
import os
import re
import sys
import tempfile
from pathlib import Path

PROJECT_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
README = PROJECT_DIR / 'README.md'

PY_REQUIRED = ['main.py', 'config/crypto_tool.py', 'test/generate_docx.py', 'test/security_audit.py',
               'test/code_style_check.py', 'test/browser_adapt_test.py']
PY_EXCLUDE_DIRS = {'.git', '.venv', '.idea', 'node_modules', 'tools', 'temp', 'file'}
JS_TARGETS = ['dist/app.js']

MAX_LINE_LEN = 120
MAX_FUNC_LINES = 80

BASELINE_LONG_FUNCS = {'main.py': 48, 'test/security_audit.py': 4}
BASELINE_LONG_LINES = {'main.py': 295, 'config/crypto_tool.py': 0, 'test/generate_docx.py': 0,
                       'test/security_audit.py': 7, 'test/code_style_check.py': 0,
                       'dist/app.js': 326}

NAME_ALLOWLIST = {'_patched_Popen', '_SECURITY_CHECKS', 'PROJECT_DIR', 'do_GET', 'do_POST',
                  'do_PUT', 'do_DELETE', 'do_HEAD', 'do_PATCH', 'do_OPTIONS'}
SILENT_MARK = '[SILENT_OK]'
PRINT_ALLOWLIST = ('log_print', 'safe_print', '_safe_print', 'print_', 'pprint')

JS_KEYWORDS = {'var', 'let', 'const', 'function', 'return', 'if', 'else', 'for', 'while', 'do',
               'switch', 'case', 'break', 'continue', 'new', 'typeof', 'instanceof', 'try',
               'catch', 'finally', 'throw', 'delete', 'in', 'of', 'this', 'void', 'yield',
               'async', 'await', 'class', 'extends', 'super', 'null', 'true', 'false',
               'undefined', 'NaN', 'Infinity', 'default', 'export', 'import', 'from'}


def read_version():
    try:
        text = README.read_text(encoding='utf-8')
    except OSError:
        return 'unknown'
    for line in text.split('\n'):
        match = re.match(r'^###\s+v([0-9]+(?:\.[0-9]+)*)', line.strip())
        if match:
            return match.group(1)
    return 'unknown'


def read_text(rel_path):
    path = PROJECT_DIR / rel_path
    if not path.is_file():
        return None
    return path.read_text(encoding='utf-8', errors='replace')


def discover_py_targets():
    targets = []
    for path in sorted(PROJECT_DIR.rglob('*.py')):
        rel_parts = path.relative_to(PROJECT_DIR).parts
        if any(part in PY_EXCLUDE_DIRS for part in rel_parts[:-1]):
            continue
        targets.append(path.relative_to(PROJECT_DIR).as_posix())
    return targets


class StyleAuditor:
    def __init__(self):
        self.issues = []
        self.checks = []

    def add(self, rule, file, line, message):
        self.issues.append({'rule': rule, 'file': file, 'line': line, 'message': message})

    def pass_check(self, rule, name, detail=''):
        self.checks.append({'rule': rule, 'name': name, 'detail': detail})

    def audit_python(self, rel_path):
        text = read_text(rel_path)
        if text is None:
            self.add('ALI-012', rel_path, 0, '目标文件不存在')
            return
        lines = text.split('\n')

        if text.startswith('\ufeff'):
            self.add('ALI-014', rel_path, 1, '文件含 BOM，必须为纯 UTF-8')

        for index, line in enumerate(lines, 1):
            code_part = line.split('#', 1)[0]
            if re.search(r'(TODO|FIXME|XXX|HACK)', code_part):
                continue
            if re.search(r'#\s*(TODO|FIXME|XXX|HACK)\b', line):
                self.add('ALI-015', rel_path, index, '存在 TODO/FIXME 遗留标记')

        tree = ast.parse(text)
        self._check_exceptions(rel_path, tree, lines)
        self._check_defaults(rel_path, tree)
        self._check_func_length(rel_path, tree)
        self._check_naming(rel_path, tree)
        self._check_print(rel_path, tree, lines)
        self._check_magic_timeout(rel_path, tree, lines)

        long_count = sum(1 for line in lines if len(line) > MAX_LINE_LEN)
        baseline = BASELINE_LONG_LINES.get(rel_path, 0)
        if long_count > baseline:
            self.add('ALI-005', rel_path, 0,
                     f'超宽行 {long_count} 行，存量基线 {baseline} 行，只允许减少不允许新增')

    def _check_exceptions(self, rel_path, tree, lines):
        for node in ast.walk(tree):
            if not isinstance(node, ast.ExceptHandler):
                continue
            if node.type is None:
                self.add('ALI-002', rel_path, node.lineno, '裸 except 必须指定异常类型')
                continue
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                src_line = lines[node.body[0].lineno - 1]
                if SILENT_MARK not in src_line:
                    self.add('ALI-001', rel_path, node.lineno,
                             '异常被静默吞掉，必须调用 _swallow_exc() 或标注 ' + SILENT_MARK)
                continue
            if node.name:
                used = any(isinstance(n, ast.Name) and n.id == node.name for stmt in node.body
                           for n in ast.walk(stmt))
                if not used:
                    self.add('ALI-016', rel_path, node.lineno,
                             f'异常变量 {node.name} 未被使用，必须记录上下文')

    def _check_defaults(self, rel_path, tree):
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for default in list(node.args.defaults) + [d for d in node.args.kw_defaults if d]:
                    if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                        self.add('ALI-003', rel_path, node.lineno,
                                 f'{node.name} 使用可变类型作为默认参数')

    def _check_func_length(self, rel_path, tree):
        long_funcs = [node for node in ast.walk(tree)
                      if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                      and node.end_lineno - node.lineno + 1 > MAX_FUNC_LINES]
        baseline = BASELINE_LONG_FUNCS.get(rel_path, 0)
        if len(long_funcs) > baseline:
            self.add('ALI-004', rel_path, 0,
                     f'超长函数 {len(long_funcs)} 个，存量基线 {baseline} 个，只允许减少不允许新增')

    def _check_naming(self, rel_path, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if not re.match(r'^_?[A-Z][A-Za-z0-9]*$', node.name):
                    self.add('ALI-011', rel_path, node.lineno, f'类名 {node.name} 必须为 CamelCase')
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name in NAME_ALLOWLIST or node.name.startswith('__'):
                    continue
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                    self.add('ALI-011', rel_path, node.lineno,
                             f'函数名 {node.name} 必须为 snake_case')

    def _check_print(self, rel_path, tree, lines):
        """服务端请求处理函数内禁止直接 print（必须走 logger / log_print）；CLI 工具与入口豁免"""
        route_ranges = []
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not node.decorator_list:
                continue
            decorator = ast.get_source_segment(
                (PROJECT_DIR / rel_path).read_text(encoding='utf-8'), node.decorator_list[0]) or ''
            if decorator.startswith('app.'):
                route_ranges.append((node.lineno, node.end_lineno))
        if not route_ranges:
            return
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
                continue
            if node.func.id != 'print':
                continue
            if not any(start <= node.lineno <= end for start, end in route_ranges):
                continue
            self.add('ALI-010', rel_path, node.lineno, '路由处理函数内禁止 print，必须走 logger')

    def _check_magic_timeout(self, rel_path, tree, lines):
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            name = func.attr if isinstance(func, ast.Attribute) else getattr(func, 'id', '')
            if name not in ('run', 'check_output', 'call', 'Popen', 'check_call'):
                continue
            for keyword in node.keywords:
                if keyword.arg != 'timeout':
                    continue
                if isinstance(keyword.value, (ast.Constant, ast.Name, ast.Attribute)):
                    if isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, (int, float)):
                        self.add('ALI-013', rel_path, keyword.value.lineno,
                                 '超时值必须取自 TIMEOUT_CONFIG / 环境变量，禁止裸数字')

    def audit_js(self, rel_path):
        text = read_text(rel_path)
        if text is None:
            self.add('ALI-012', rel_path, 0, '目标文件不存在')
            return
        lines = text.split('\n')
        if text.startswith('\ufeff'):
            self.add('ALI-014', rel_path, 1, '文件含 BOM，必须为纯 UTF-8')

        long_count = 0
        for index, line in enumerate(lines, 1):
            stripped = line.strip()
            if len(line) > MAX_LINE_LEN:
                long_count += 1
            if re.match(r'^var\s+', stripped):
                self.add('ALI-006', rel_path, index, '禁止 var，必须使用 const / let')
            if re.search(r'\bvar\s+[A-Za-z_$]', stripped) and not stripped.startswith('//'):
                self.add('ALI-006', rel_path, index, '禁止 var，必须使用 const / let')
            if re.search(r'\b(alert|confirm|prompt)\s*\(', stripped):
                self.add('ALI-007', rel_path, index, '禁止阻塞式弹窗，必须改用 showToast')
            if re.search(r'(?<![=!<>])(==|!=)(?!=)', stripped):
                self.add('ALI-008', rel_path, index, '必须使用 === / !== 严格比较')
            if re.search(r'\b(eval|Function)\s*\(', stripped) or 'document.write(' in stripped:
                self.add('ALI-009', rel_path, index, '禁止 eval / new Function / document.write')
            if re.search(r'(TODO|FIXME|XXX|HACK)', stripped.split('//', 1)[-1]) and stripped.startswith('//'):
                self.add('ALI-015', rel_path, index, '存在 TODO/FIXME 遗留标记')

        baseline = BASELINE_LONG_LINES.get(rel_path, 0)
        if long_count > baseline:
            self.add('ALI-005', rel_path, 0, f'超宽行 {long_count} 行，基线 {baseline} 行，只允许减少')

    def scan_all(self):
        for rel_path in PY_REQUIRED:
            if not (PROJECT_DIR / rel_path).is_file():
                self.add('ALI-012', rel_path, 0, '核心受检文件缺失')
        for rel_path in discover_py_targets():
            self.audit_python(rel_path)
        for rel_path in JS_TARGETS:
            self.audit_js(rel_path)

        rules = {
            'ALI-001': '禁止静默吞异常（except: pass）',
            'ALI-002': '禁止裸 except',
            'ALI-003': '禁止可变类型默认参数',
            'ALI-004': '函数长度 ≤ 80 行（存量基线冻结）',
            'ALI-005': f'单行 ≤ {MAX_LINE_LEN} 字符（存量基线冻结）',
            'ALI-006': 'JavaScript 禁止 var',
            'ALI-007': '禁止 alert / confirm / prompt',
            'ALI-008': '必须使用 === / !==',
            'ALI-009': '禁止 eval / new Function / document.write',
            'ALI-010': '禁止直接 print（走 log_print / logger）',
            'ALI-011': '命名规范（snake_case / CamelCase）',
            'ALI-012': '核心受检文件必须存在',
            'ALI-013': '禁止裸魔法超时数字',
            'ALI-014': 'UTF-8 无 BOM',
            'ALI-015': '禁止 TODO / FIXME 遗留标记',
            'ALI-016': '异常变量必须被使用',
        }
        counts = {}
        for issue in self.issues:
            counts[issue['rule']] = counts.get(issue['rule'], 0) + 1
        return {'rules': rules, 'counts': counts, 'issues': self.issues,
                'total': len(self.issues)}


SELF_TEST_PROBE = '''
import subprocess


def BadName():
    """探针：同时触发 ALI-001 / ALI-011 / ALI-013"""
    try:
        subprocess.run(['echo', 'hi'], timeout=5)
    except Exception:
        pass
'''

SELF_TEST_EXPECT = ('ALI-001', 'ALI-011', 'ALI-013')


def run_self_test():
    """自检闸门有效性：探针只写在系统临时目录，绝不落到项目扫描范围内"""
    with tempfile.TemporaryDirectory() as tmpdir:
        probe_path = Path(tmpdir) / 'probe_violation.py'
        probe_path.write_text(SELF_TEST_PROBE, encoding='utf-8')
        auditor = StyleAuditor()
        auditor.audit_python(str(probe_path))
        hit_rules = {issue['rule'] for issue in auditor.issues}

    print('=' * 68)
    print('闸门自检：用临时探针验证规则确实会命中（探针不落盘到项目目录）')
    print('=' * 68)
    for rule in SELF_TEST_EXPECT:
        mark = '✅' if rule in hit_rules else '❌'
        print(f'{mark} {rule} 命中' if rule in hit_rules else f'{mark} {rule} 未命中，闸门失效')
    missing = [rule for rule in SELF_TEST_EXPECT if rule not in hit_rules]
    if missing:
        print(f'\n⚠️ 自检失败，以下规则未触发: {missing}')
        return 1
    print('\n✅ 自检通过：三条核心规则全部命中，闸门有效且未污染项目目录')
    return 0


def main():
    if '--selftest' in sys.argv:
        return run_self_test()

    version = read_version()
    py_targets = discover_py_targets()
    print('=' * 68)
    print(f'阿里巴巴代码规范合规检查 (Python / JavaScript 适配版)  当前版本: v{version}')
    print(f'扫描范围: Python {len(py_targets)} 个文件（自动发现）+ JavaScript {len(JS_TARGETS)} 个文件')
    print('=' * 68)

    auditor = StyleAuditor()
    result = auditor.scan_all()

    for rule, name in result['rules'].items():
        count = result['counts'].get(rule, 0)
        if count == 0:
            print(f'✅ {rule} {name}')
        else:
            print(f'❌ {rule} {name} — {count} 处')
            for issue in result['issues']:
                if issue['rule'] == rule:
                    print(f'    {issue["file"]}:{issue["line"]} {issue["message"]}')

    print('-' * 68)
    if result['total'] == 0:
        print('✅ 总计问题 0，代码规范全部达标！')
        return 0
    print(f'⚠️ 发现 {result["total"]} 处规范违规，必须修复至 0！')
    return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)