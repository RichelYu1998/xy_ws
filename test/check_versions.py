import re

with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()
readme_versions = re.findall(r'### v5\.0\.9\.(\d+)', readme_content)
readme_nums = [int(v) for v in readme_versions]

with open('skill.md', 'r', encoding='utf-8') as f:
    skill_content = f.read()
skill_versions = re.findall(r'### v5\.0\.9\.(\d+)', skill_content)
skill_nums = [int(v) for v in skill_versions]

print('=' * 60)
print('VERSION COUNT')
print('=' * 60)
print(f'README.md:  {len(readme_nums)} versions')
print(f'skill.md:   {len(skill_nums)} versions')
print()

readme_set = set(readme_nums)
skill_set = set(skill_nums)

only_in_readme = sorted(list(readme_set - skill_set), reverse=True)
only_in_skill = sorted(list(skill_set - readme_set), reverse=True)

print('DIFFERENCES:')
print(f'Only in README ({len(only_in_readme)}): {only_in_readme}')
print(f'Only in skill  ({len(only_in_skill)}): {only_in_skill}')
print()

readme_ok = all(readme_nums[i] >= readme_nums[i+1] for i in range(len(readme_nums)-1))
skill_ok = all(skill_nums[i] >= skill_nums[i+1] for i in range(len(skill_nums)-1))

print('ORDER CHECK:')
status_readme = 'OK' if readme_ok else 'FAIL'
status_skill = 'OK' if skill_ok else 'FAIL'
print(f'README.md: {status_readme} (first 5: {readme_nums[:5]})')
print(f'skill.md:  {status_skill} (first 5: {skill_nums[:5]})')