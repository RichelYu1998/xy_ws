import re

with open('D:/ws/xy_ws/skill.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

versions = []
current = None
in_changelog = False

for i, line in enumerate(lines):
    stripped = line.strip()
    if '最新更新' in stripped and stripped.startswith('##'):
        in_changelog = True
        continue
    if not in_changelog:
        continue

    vm = re.match(r'###\s+v([\d.]+)\s+\(([^)]+)\)', stripped)
    if not vm:
        vm = re.match(r'##\s+v([\d.]+)\s+\(([^)]+)\)', stripped)

    if vm:
        if current:
            versions.append(current)
        current = {
            'version': vm.group(1),
            'date': vm.group(2),
            'line': i + 1,
            'has_changes': False,
            'commit': '',
            'change_count': 0
        }
        continue

    if current:
        if re.match(r'#####\s+\d+\.', stripped):
            current['has_changes'] = True
            current['change_count'] += 1

        cm = re.match(r'^>*\s*\*\*Commit\*\*:\s*(.*)', stripped)
        if cm:
            current['commit'] = cm.group(1).strip().strip('`')

if current:
    versions.append(current)

print(f'Total versions found: {len(versions)}')
print()

empty_changes = [v for v in versions if not v['has_changes']]
bad_commits = [v for v in versions if v['commit'] in ('待生成', '待补充', '', 'TBD')]

if empty_changes:
    print(f'VERSIONS WITH EMPTY CHANGES ({len(empty_changes)}):')
    for v in empty_changes:
        print(f'  v{v["version"]} (line {v["line"]}) - {v["change_count"]} changes')
else:
    print('All versions have non-empty changes.')

print()

if bad_commits:
    print(f'VERSIONS WITH BAD COMMIT ({len(bad_commits)}):')
    for v in bad_commits:
        print(f'  v{v["version"]} (line {v["line"]}) - commit: "{v["commit"]}"')
else:
    print('All versions have valid commit hashes.')