import subprocess
import re

# 获取Git提交历史中的版本号
result = subprocess.run(
    ['git', 'log', '--oneline', '--all'],
    capture_output=True,
    encoding='utf-8',
    errors='ignore'
)
git_log = result.stdout if result.stdout else ''

# 提取版本号 (格式: v5.0.9.XX)
git_versions = re.findall(r'v5\.0\.9\.(\d+)', git_log)
git_nums = [int(v) for v in git_versions]

# 去重并排序
git_unique = sorted(list(set(git_nums)), reverse=True)

print('=' * 60)
print('GIT VERSIONS FROM COMMIT MESSAGES')
print('=' * 60)
print(f'Total commits with versions: {len(git_nums)}')
print(f'Unique versions: {len(git_unique)}')
print(f'Version range: {min(git_unique)} - {max(git_unique)}')
print()
print(f'First 10: {git_unique[:10]}')
print(f'Last 10: {git_unique[-10:]}')

# 读取README和skill的版本
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()
readme_versions = re.findall(r'### v5\.0\.9\.(\d+)', readme_content)
readme_nums = [int(v) for v in readme_versions]

with open('skill.md', 'r', encoding='utf-8') as f:
    skill_content = f.read()
skill_versions = re.findall(r'### v5\.0\.9\.(\d+)', skill_content)
skill_nums = [int(v) for v in skill_versions]

readme_set = set(readme_nums)
skill_set = set(skill_nums)
git_set = set(git_unique)

print('\n' + '=' * 60)
print('THREE-WAY COMPARISON (README vs skill vs Git)')
print('=' * 60)

only_readme = readme_set - skill_set - git_set
only_skill = skill_set - readme_set - git_set
only_git = git_set - readme_set - skill_set
all_three = readme_set & skill_set & git_set

print(f'\nAll three have ({len(all_three)}): {sorted(list(all_three), reverse=True)[:10]}...')
print(f'Only in README: {sorted(list(only_readme), reverse=True)}')
print(f'Only in skill:  {sorted(list(only_skill), reverse=True)}')
print(f'Only in Git:   {sorted(list(only_git), reverse=True)}')

# 检查顺序
readme_ok = all(readme_nums[i] >= readme_nums[i+1] for i in range(len(readme_nums)-1))
skill_ok = all(skill_nums[i] >= skill_nums[i+1] for i in range(len(skill_nums)-1))
git_ok = all(git_unique[i] >= git_unique[i+1] for i in range(len(git_unique)-1))

print('\n' + '=' * 60)
print('ORDER VALIDATION')
print('=' * 60)
print(f'README.md: {"PASS" if readme_ok else "FAIL"}')
print(f'skill.md:  {"PASS" if skill_ok else "FAIL"}')
print(f'Git:      {"PASS" if git_ok else "FAIL"}')

if len(all_three) == len(readme_nums) == len(skill_nums):
    print('\n✅ PERFECT MATCH: All three sources are 100% consistent!')
else:
    print('\n❌ INCONSISTENCIES DETECTED: Need synchronization')