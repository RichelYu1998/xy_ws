import json

with open('file/_changelog_api.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

items = data['changelog']

# Fix v5.0.9.72 commit
for v in items:
    if v.get('version') == '5.0.9.72':
        v['meta']['commit'] = 'a565ebd8'
        print('Fixed v5.0.9.72 commit:', v['meta']['commit'])
        break

# Add new v5.0.9.82 entry
new_entry = {
    'version': '5.0.9.82',
    'date': '2026-11-05',
    'title': '依赖检查逻辑重构+镜像测速修复+hostc升级回显修复+Playwright驱动安装',
    'meta': {
        'commit': 'ceebfea8',
        'fix_date': '2026-11-05',
        'author': 'AI Assistant',
        'affected_files': '[main.py](main.py), [run.bat](run.bat)',
        'change_stats': '+46行/-35行'
    },
    'changes': [
        {
            'id': '1',
            'title': 'check_deps_satisfied()依赖检查逻辑重构',
            'tag': '功能优化',
            'problem': {
                'phenomenon': '--check-deps始终返回exit code 1，即使所有依赖版本均满足要求，仅uvicorn[standard]缺失时也误报',
                'root_cause': '原代码使用re.split正则分割uvicorn[standard]>=0.30.0，取parts[1]得到standard而非版本号0.30.0',
                'scope': 'main.py#L7903'
            },
            'solution': {
                'implementation': '改用packaging.requirements.Requirement和packaging.version.Version正确解析，支持extras标识和语义化版本约束',
                'reference': 'main.py#L7903-L7933'
            },
            'verification': ['✅ uvicorn[standard]正确解析为name=uvicorn', '✅ 所有依赖满足时返回exit code 0']
        },
        {
            'id': '2',
            'title': 'run.bat 8处PowerShell单引号语法错误修复',
            'tag': '功能优化',
            'problem': {
                'phenomenon': '所有镜像源测速结果始终为空，所有镜像被错误判定为超时',
                'root_cause': '[double]!VAR!*1000中多余的单引号包裹导致PowerShell无法正确解析数值',
                'scope': 'run.bat#L125 等8处'
            },
            'solution': {
                'implementation': '将所有[double]\'!VAR!\'*1000改为[double]!VAR!*1000，涉及8处镜像测速逻辑',
                'reference': 'run.bat#L125'
            },
            'verification': ['✅ PowerShell测试正确返回整数毫秒', '✅ 镜像测速功能恢复正常']
        },
        {
            'id': '3',
            'title': 'hostc升级后版本号未更新修复',
            'tag': 'Bug修复',
            'problem': {
                'phenomenon': 'hostc升级后版本号仍显示旧值v2.0.3',
                'root_cause': 'setlocal在for外部、endlocal在for内部，endlocal清除了变量导致主脚本无法访问',
                'scope': 'run.bat#L333-L336'
            },
            'solution': {
                'implementation': '将setlocal/endlocal都移入for循环内部正确配对',
                'reference': 'run.bat#L334'
            },
            'verification': ['✅ 升级成功后版本号正确更新']
        },
        {
            'id': '4',
            'title': 'Playwright Chromium浏览器驱动安装',
            'tag': '安全加固',
            'problem': {
                'phenomenon': 'Playwright Chromium浏览器连接失败，Connection closed while reading from the driver',
                'root_cause': 'Chromium浏览器二进制文件不存在，playwright install未执行',
                'scope': 'main.py#L2559'
            },
            'solution': {
                'implementation': '执行playwright install chromium下载136MB驱动',
                'reference': 'main.py'
            },
            'verification': ['✅ pw.chromium.launch(headless=True)成功']
        }
    ]
}

data['changelog'].insert(0, new_entry)
print('Added v5.0.9.82 entry')

with open('file/_changelog_api.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Saved')

# Verify
with open('file/_changelog_api.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)
items2 = data2['changelog']
print(f'Total versions: {len(items2)}')
print(f'First version: {items2[0]["version"]}')
print(f'v5.0.9.72 commit: {[v for v in items2 if v["version"]=="5.0.9.72"][0]["meta"]["commit"]}')
bad = [v.get("version") for v in items2 if v.get("meta",{}).get("commit","") in ("待生成","待补充","待提交","",None)]
print(f'Bad commits: {len(bad)}')
empty = [v.get("version") for v in items2 if len(v.get("changes",[])) == 0]
print(f'Empty changes: {len(empty)}')