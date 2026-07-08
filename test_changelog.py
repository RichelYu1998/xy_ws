#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试 changelog API 解析"""

import json
import re

def parse_changelog():
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    changelog = []
    current_version = None
    current_date = None
    current_items = []
    current_item = None
    current_section = None
    in_changelog = False
    in_code_block = False
    
    for line in lines:
        if '最新更新' in line.strip() and line.strip().startswith('##'):
            in_changelog = True
            continue
        if not in_changelog:
            continue
        
        stripped = line.strip()
        version_match = re.match(r'###\s+v([\d.]+)\s+\(([^)]+)\)', stripped)
        if not version_match:
            version_match = re.match(r'###\s+v([\d.]+)\s+\(([^)]+)\)', line.split(' - ')[0].strip())
        
        if version_match:
            if current_version:
                if current_section:
                    current_items.append(current_section)
                    current_section = None
                elif current_item:
                    current_items.append(current_item)
                    current_item = None
                changelog.append({
                    'version': current_version,
                    'date': current_date,
                    'items': current_items
                })
            
            current_version = version_match.group(1)
            current_date = version_match.group(2)
            current_items = []
            current_item = None
            current_section = None
            in_code_block = False
            continue
        
        if stripped.startswith('## ') and in_changelog and current_version:
            break
        
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            if current_section:
                current_section['content'] += line + '\n'
            continue
        
        section_match = re.match(r'^####\s+(.+)$', stripped)
        if section_match and current_version:
            if current_section:
                current_items.append(current_section)
            elif current_item:
                current_items.append(current_item)
                current_item = None
            
            current_section = {
                'type': 'section',
                'title': section_match.group(1).strip(),
                'content': '',
                'sub_items': []
            }
            continue
        
        item_match = re.match(r'^-\s+\*\*(.+?)\*\*\s*[-–]?\s*(.*)', stripped)
        if item_match and current_version:
            if current_section:
                current_items.append(current_section)
                current_section = None
            elif current_item:
                current_items.append(current_item)
            
            current_item = {
                'type': 'item',
                'title': item_match.group(1),
                'desc': item_match.group(2).strip(),
                'sub_items': []
            }
            continue
        
        sub_match = re.match(r'^-\s+(.*)', stripped)
        if sub_match and (current_item or current_section):
            is_indented = line.startswith('  ') or line.startswith('\t')
            if current_item and is_indented:
                current_item['sub_items'].append(sub_match.group(1).strip())
            elif current_section:
                current_section['sub_items'].append(sub_match.group(1).strip())
            continue
        
        if current_section and stripped and not in_code_block:
            current_section['content'] += line + '\n'
    
    if current_section:
        current_items.append(current_section)
    elif current_item:
        current_items.append(current_item)
    
    if current_version:
        changelog.append({
            'version': current_version,
            'date': current_date,
            'items': current_items
        })
    
    return changelog

if __name__ == '__main__':
    print('=' * 80)
    print('📋 Changelog API 解析测试')
    print('=' * 80)
    
    try:
        result = parse_changelog()
        
        print(f'\n✅ 解析成功！共找到 {len(result)} 个版本\n')
        
        for idx, version in enumerate(result, 1):
            print(f'版本 {idx}: {version["version"]} ({version["date"]})')
            print(f'  包含 {len(version["items"])} 个项目:')
            
            for item_idx, item in enumerate(version['items'], 1):
                item_type = item.get('type', 'unknown')
                title = item.get('title', '')[:60]
                
                if item_type == 'section':
                    content_len = len(item.get('content', ''))
                    sub_count = len(item.get('sub_items', []))
                    print(f'  [{item_idx}] 📌 SECTION: {title}')
                    print(f'      内容长度: {content_len} 字符, 子项: {sub_count} 个')
                else:
                    desc = item.get('desc', '')[:40]
                    sub_count = len(item.get('sub_items', []))
                    print(f'  [{item_idx}] ✅ ITEM: {title} - {desc}')
                    print(f'      子项: {sub_count} 个')
            
            print()
        
        if result:
            latest = result[0]
            print('=' * 80)
            print(f'📊 最新版本 {latest["version"]} 详细信息:')
            print('=' * 80)
            print(json.dumps(latest, ensure_ascii=False, indent=2))
    
    except Exception as e:
        print(f'\n❌ 解析失败: {e}')
        import traceback
        traceback.print_exc()