import re, os, sys

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
readme_path = os.path.join(base_dir, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.split('\n')

changelog = []
current_entry = None
current_change_count = 0
in_changelog = False

for i, line in enumerate(lines):
    stripped = line.strip()
    if '最新更新' in stripped and stripped.startswith('##'):
        in_changelog = True
        continue
    if not in_changelog:
        continue
    version_match = re.match(r'###\s+v([\d.]+)\s+\(([^)]+)\)', stripped)
    if version_match:
        if current_entry:
            current_entry['change_count'] = current_change_count
            changelog.append(current_entry)
        current_entry = {
            'version': version_match.group(1),
            'date': version_match.group(2),
            'line': i + 1,
            'commit': '',
            'has_update_content': False
        }
        current_change_count = 0
        continue
    if current_entry:
        if stripped.startswith('##### '):
            current_change_count += 1
        if stripped.startswith('#### 更新内容:'):
            current_entry['has_update_content'] = True
        m = re.match(r'\*\*Commit\*\*:\s*(.*)', stripped)
        if m:
            current_entry['commit'] = m.group(1)

if current_entry:
    current_entry['change_count'] = current_change_count
    changelog.append(current_entry)

print(f'Total versions: {len(changelog)}')

no_changes = [e for e in changelog if e['change_count'] == 0]
print(f'\nVersions with 0 ##### change blocks: {len(no_changes)}')
for e in no_changes[:20]:
    print(f'  v{e["version"]} ({e["date"]}) line={e["line"]} commit={e["commit"]}')

no_update = [e for e in changelog if not e['has_update_content']]
print(f'\nVersions missing #### 更新内容: {len(no_update)}')
for e in no_update[:20]:
    print(f'  v{e["version"]} ({e["date"]}) line={e["line"]}')

pending = [e for e in changelog if '待生成' in e.get('commit', '')]
print(f'\nPending (待生成) commit: {len(pending)}')
for e in pending:
    print(f'  v{e["version"]} ({e["date"]}) commit={e["commit"]}')

pending2 = [e for e in changelog if '待补充' in e.get('commit', '')]
print(f'\nNeed supplement (待补充) commit: {len(pending2)}')
for e in pending2:
    print(f'  v{e["version"]} ({e["date"]}) commit={e["commit"]}')

print(f'\nLatest 5 versions:')
for e in changelog[:5]:
    print(f'  v{e["version"]} ({e["date"]}) changes={e["change_count"]} commit={e["commit"][:30]}')