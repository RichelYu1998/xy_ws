"""
dedup_paradigm.py - 将skill.md中两份PY-CORE-027范式合并为一份

第一份(9250起): 范式定义(9250-9392) + 完整示例/版本记录(9393-10669)
第二份(23365起): 完整范式定义(含反面案例/自动化脚本/相关范式)

策略:
1. 第一份的范式定义部分(9250-9392, 到"---"分隔符后)删除
2. 保留第一份9393起的"完整示例"和版本记录
3. 第二份作为唯一完整范式保留在文件末尾
"""
from pathlib import Path

ROOT = Path('..')
SKILL = ROOT / 'skill.md'


def find_section_range(lines, start_idx):
    start = start_idx
    end = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith('## '):
            end = i
            break
    return start, end


def main():
    lines = SKILL.read_text(encoding='utf-8').splitlines(keepends=True)
    idx1 = idx2 = None
    for i, ln in enumerate(lines):
        if ln.startswith('## 🔴 PY-CORE-027:'):
            if idx1 is None:
                idx1 = i
            elif idx2 is None:
                idx2 = i
                break

    s1, e1 = find_section_range(lines, idx1)
    s2, e2 = find_section_range(lines, idx2)
    print(f'第一份: 行{s1+1}-{e1} ({e1-s1}行)')
    print(f'第二份: 行{s2+1}-{e2} ({e2-s2}行)')

    cut_end = None
    for i in range(s1 + 1, e1):
        if lines[i].startswith('### 完整示例'):
            cut_end = i
            break
    if cut_end is None:
        print('未找到"### 完整示例"边界, 退出')
        return
    print(f'第一份范式定义部分: 行{s1+1}-{cut_end} (将删除)')
    print(f'第一份保留部分(完整示例+版本记录): 行{cut_end+1}-{e1}')

    del lines[s1:cut_end]
    print(f'已删除第一份范式定义部分({cut_end-s1}行)')

    remaining = sum(1 for ln in lines if ln.startswith('## 🔴 PY-CORE-027:'))
    print(f'剩余PY-CORE-027范式数量: {remaining}')

    SKILL.write_text(''.join(lines), encoding='utf-8')
    print(f'skill.md现总行数: {len(lines)}')


if __name__ == '__main__':
    main()