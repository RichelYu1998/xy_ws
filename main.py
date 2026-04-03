import json
import time
import asyncio
import os
import re
import platform
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import threading
from datetime import datetime

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("请安装playwright: pip install playwright")
    print("然后运行: playwright install chromium")
    sys.exit(1)

try:
    import openpyxl
except ImportError:
    print("请安装openpyxl: pip install openpyxl")
    sys.exit(1)


class WegoScraper:
    def __init__(self, config_path='config/config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_config(self):
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def save_cookies(self, cookies):
        cookie_file = self.config.get('cookie_file', 'config/cookies.json')
        with open(cookie_file, 'w', encoding='utf-8') as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)
        print(f'Cookie已保存到 {cookie_file}')

    def load_cookies(self):
        cookie_file = self.config.get('cookie_file', 'config/cookies.json')
        if os.path.exists(cookie_file):
            with open(cookie_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def get_system_info(self):
        system = platform.system()
        if system == 'Windows':
            return 'Windows'
        elif system == 'Darwin':
            return 'Mac'
        elif system == 'Linux':
            return 'Linux'
        return 'Unknown'

    def clean_product_name(self, text):
        if not text:
            return None
        
        text = re.sub(r'¥\d+', '', text)
        
        useless_patterns = [
            r'删除下载刷新编辑分享商品属性标签',
            r'售价：',
            r'昨天分享',
        ]
        
        cleaned_text = text
        for pattern in useless_patterns:
            cleaned_text = re.sub(pattern, '', cleaned_text)
        
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        
        return cleaned_text if cleaned_text else None

    async def close_popups(self, page):
        try:
            popup_selectors = [
                '[class*="close"]',
                '[class*="modal-close"]',
                '[class*="dialog-close"]',
                'button:has-text("关闭")',
                'button:has-text("×")',
                'button:has-text("✕")',
                '.ant-modal-close',
                '.el-dialog__close',
            ]
            
            for selector in popup_selectors:
                try:
                    close_button = await page.query_selector(selector)
                    if close_button:
                        await close_button.click()
                        print(f'关闭了弹窗: {selector}')
                        await asyncio.sleep(0.5)
                except:
                    pass
        except Exception as e:
            print(f'关闭弹窗时出错: {e}')

    async def scroll_to_load_all(self, page):
        print('开始滚动加载所有商品...')
        
        last_height = 0
        scroll_attempts = 0
        max_attempts = 30
        no_change_count = 0
        same_height_limit = 3
        
        while scroll_attempts < max_attempts:
            try:
                current_height = await page.evaluate('document.body.scrollHeight')
                
                if current_height == last_height:
                    no_change_count += 1
                    if no_change_count >= same_height_limit:
                        print(f'页面已滚动到底部（高度连续{same_height_limit}次不变: {current_height}），停止滚动')
                        break
                else:
                    no_change_count = 0
                    last_height = current_height
                
                await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                await asyncio.sleep(1)
                
                scroll_attempts += 1
                print(f'滚动 {scroll_attempts}/{max_attempts}，当前高度: {current_height}')
                
                await self.close_popups(page)
                    
            except Exception as e:
                print(f'滚动时出错: {e}')
                break
        
        print('滚动完成')

    def extract_product_info_sync(self, element_text, html_content):
        try:
            stock_number = None
            stock_match = re.search(r'货号[：:]\s*(\d+)', element_text)
            if stock_match:
                stock_number = stock_match.group(1)
            
            if not stock_number:
                return None
            
            price = None
            
            price_match = re.search(r'售价[：:]\s*¥?\s*(\d{3,6})', element_text)
            if price_match:
                price = '¥' + price_match.group(1)
            
            if not price:
                price_match = re.search(r'¥(\d{4,6})', element_text)
                if price_match:
                    price = '¥' + price_match.group(1)
            
            if not price:
                price_match = re.search(r'(\d{4,6})\s*$', element_text)
                if price_match:
                    price = '¥' + price_match.group(1)
            
            if not price:
                price_match = re.search(r'货号[：:]\s*\d+\s*(\d{4,6})', element_text)
                if price_match:
                    price = '¥' + price_match.group(1)
            
            remark = None
            remark_match = re.search(r'备注[：:]\s*(.+?)(?:\s*员工[：:]|$)', element_text, re.DOTALL)
            if remark_match:
                remark = remark_match.group(1).strip()
                remark = re.sub(r'\s+', ' ', remark)
            
            employee = None
            employee_match = re.search(r'员工[：:]\s*(.+)', element_text)
            if employee_match:
                employee = employee_match.group(1).strip()
            
            name = None
            
            price_pos = element_text.find('¥')
            delete_pos = element_text.find('删除')
            stock_pos = element_text.find('货号')
            
            cut_pos = len(element_text)
            if price_pos > 0:
                cut_pos = min(cut_pos, price_pos)
            if delete_pos > 0:
                cut_pos = min(cut_pos, delete_pos)
            if stock_pos > 0:
                cut_pos = min(cut_pos, stock_pos)
            
            if cut_pos < len(element_text) and cut_pos > 10:
                name_part = element_text[:cut_pos].strip()
                if name_part:
                    name_part = re.sub(r'\s+', ' ', name_part)
                    name = name_part
            
            if not name:
                name = self.clean_product_name(element_text)
            
            if name:
                cleaned_name = self.clean_product_name(name)
                if cleaned_name:
                    return {
                        'name': cleaned_name,
                        'price': price if price else 'N/A',
                        'stock_number': stock_number if stock_number else 'N/A',
                        'remark': remark if remark else 'N/A',
                        'employee': employee if employee else 'N/A'
                    }
            
            return None
        except Exception as e:
            print(f'提取商品信息时出错: {e}')
            return None

    async def process_elements_concurrently(self, page, elements):
        print(f'开始并发处理 {len(elements)} 个商品元素...')
        
        elements_data = []
        for i, element in enumerate(elements):
            try:
                element_text = await element.text_content()
                html_content = await element.inner_html()
                
                if not element_text or not element_text.strip():
                    continue
                
                if '试试批量' in element_text or '暂无搭配' in element_text:
                    continue
                
                if re.match(r'^\d{2}月 \d{4}$', element_text.strip()):
                    continue
                
                if len(element_text.strip()) < 30:
                    continue
                
                elements_data.append((element_text, html_content))
                
            except Exception as e:
                print(f'收集元素 {i} 数据时出错: {e}')
                continue
        
        print(f'收集了 {len(elements_data)} 个有效商品数据')
        
        products = []
        seen_products = set()
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for i, (element_text, html_content) in enumerate(elements_data):
                future = executor.submit(self.extract_product_info_sync, element_text, html_content)
                futures.append((future, i))
            
            for future, i in futures:
                try:
                    result = future.result(timeout=5)
                    if result:
                        stock_number = result.get('stock_number')
                        if stock_number and stock_number not in seen_products:
                            seen_products.add(stock_number)
                            products.append(result)
                            
                            if len(products) <= 10:
                                print(f'商品 {len(products)}: {result["name"][:50]}...')
                                print(f'  售价: {result["price"]}')
                                print(f'  货号: {result["stock_number"]}')
                                print()
                except Exception as e:
                    print(f'处理商品 {i} 时出错: {e}')
                    continue
        
        return products

    async def get_data_with_playwright(self, page):
        try:
            target_url = self.config['target_url']
            print(f'正在访问目标页面: {target_url}')
            print(f'当前系统: {self.get_system_info()}')
            
            try:
                await page.goto(target_url, timeout=120000, wait_until='networkidle')
            except Exception as e:
                print(f'页面导航出错: {e}')
                await asyncio.sleep(5)
            
            print('等待页面初始加载...')
            await asyncio.sleep(15)
            
            await self.close_popups(page)
            
            print('滚动加载所有商品...')
            await self.scroll_to_load_all(page)
            
            print('等待页面完全加载...')
            await asyncio.sleep(10)
            
            print('开始获取数据...')
            
            page_text = await page.content()
            
            total_count = None
            new_count = None
            
            try:
                total_patterns = [
                    r'总数\s*[：:]\s*(\d+)',
                    r'上新\s*(\d+)\s*\|\s*总数\s*(\d+)',
                    r'总\s*数\s*[：:]\s*(\d+)',
                ]
                
                for pattern in total_patterns:
                    match = re.search(pattern, page_text)
                    if match:
                        if len(match.groups()) == 2:
                            new_count = int(match.group(1))
                            total_count = int(match.group(2))
                            print(f'网页显示上新: {new_count}, 总数: {total_count}')
                        else:
                            total_count = int(match.group(1))
                            print(f'网页显示总数: {total_count}')
                        break
                
                new_match = re.search(r'上新\s*[：:]\s*(\d+)', page_text)
                if new_match and not new_count:
                    new_count = int(new_match.group(1))
                    print(f'网页显示上新: {new_count}')
            except Exception as e:
                print(f'获取总数信息时出错: {e}')
            
            print('查找所有商品项...')
            item_selectors = [
                '.normal_item-module_normalItemContent_mrLg3',
                '.normal_item-module_timeline_common_item_eMbm2',
            ]
            
            item_elements = []
            for selector in item_selectors:
                try:
                    elements = await page.query_selector_all(selector)
                    if elements:
                        print(f'使用选择器 {selector} 找到 {len(elements)} 个元素')
                        for element in elements:
                            if element not in item_elements:
                                item_elements.append(element)
                except Exception as e:
                    print(f'使用选择器 {selector} 时出错: {e}')
                    continue
            
            print(f'总共找到 {len(item_elements)} 个商品项')
            
            products = await self.process_elements_concurrently(page, item_elements)
            
            print(f'\n数量统计：')
            print(f'网页显示总数: {total_count}')
            print(f'网页显示上新: {new_count}')
            print(f'实际获取商品数量: {len(products)}')
            
            print(f'\n成功获取 {len(products)} 个商品')
            return products
        except Exception as e:
            print(f'获取数据失败: {e}')
            import traceback
            traceback.print_exc()
            return []

    def save_data(self, data, filename=None):
        if not filename:
            filename = self.config.get('output_file', 'file/output.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f'数据已保存到 {filename}')

    async def run(self):
        try:
            print('='*50)
            print('Szwego商品爬虫 - 跨系统版本')
            print(f'当前系统: {self.get_system_info()}')
            print(f'Python版本: {platform.python_version()}')
            print('='*50)
            print('开始运行...')
            
            async with async_playwright() as p:
                print('正在启动浏览器...')
                
                system = self.get_system_info()
                
                browser_args = [
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-blink-features=AutomationControlled',
                    '--disable-dev-shm-usage',
                ]
                
                if system == 'Windows':
                    browser_args.extend([
                        '--disable-gpu',
                    ])
                elif system == 'Linux':
                    browser_args.extend([
                        '--disable-gpu',
                        '--disable-dev-shm-usage',
                    ])
                
                browser = await p.chromium.launch(
                    headless=False,
                    args=browser_args
                )
                
                context = await browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent=self.config.get('user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
                )
                
                cookies = self.load_cookies()
                if cookies:
                    print(f'找到 {len(cookies)} 个Cookie，正在添加到浏览器...')
                    await context.add_cookies(cookies)
                    print('Cookie已添加')
                else:
                    print('未找到Cookie，需要手动登录')
                
                page = await context.new_page()
                
                data = await self.get_data_with_playwright(page)
                self.save_data(data)
                
                if data:
                    print(f'成功获取 {len(data)} 个商品')
                else:
                    print('未获取到商品数据')
                
                input('\n按回车键关闭浏览器...')
                await browser.close()
        except Exception as e:
            print(f'发生错误: {e}')
            import traceback
            traceback.print_exc()
            input('\n按回车键退出...')


class StockNumberComparator:
    def __init__(self, output_file='file/output.json', input_file='config/input_stock_numbers.txt', config_path='config/config.json'):
        self.output_file = output_file
        self.input_file = input_file
        self.config_path = config_path
        self.config = self.load_config()
        self.excel_file = self.config.get('excel_file', 'C:\\Users\\Administrator\\Desktop\\小旭二手机.xlsx')

    def load_config(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f'加载配置文件失败: {e}')
            return {}

    def load_json_data(self):
        try:
            with open(self.output_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f'加载JSON文件失败: {e}')
            return []

    def extract_stock_numbers(self, data):
        stock_numbers = set()
        for item in data:
            if 'stock_number' in item and item['stock_number'] != 'N/A':
                stock_numbers.add(item['stock_number'])
        return stock_numbers

    def parse_input_string(self, input_str):
        if not input_str:
            return []
        
        cleaned = re.sub(r'序列号', '', input_str)
        
        separators = r'[,，\s;；\n\t]+'
        numbers = re.split(separators, cleaned)
        
        result = []
        for num in numbers:
            if num.strip():
                result.append(num.strip())
        
        return result
    def load_excel_data(self, excel_file=None):
        """从Excel文件读取货号数据"""
        if excel_file is None:
            excel_file = self.excel_file
        
        try:
            if not os.path.exists(excel_file):
                print(f'Excel文件 {excel_file} 不存在')
                return None
            
            print(f'正在读取Excel文件: {excel_file}')
            workbook = openpyxl.load_workbook(excel_file)
            
            # 查找"闲鱼"工作表
            sheet = None
            for sheet_name in workbook.sheetnames:
                if '闲鱼' in sheet_name:
                    sheet = workbook[sheet_name]
                    print(f'找到工作表: {sheet_name}')
                    break
            
            if sheet is None:
                print('未找到"闲鱼"工作表，使用第一个工作表')
                sheet = workbook.active
            else:
                print(f'使用工作表: {sheet.title}')
            
            # 读取E列（第5列）的数据
            stock_numbers = []
            for row in sheet.iter_rows(min_col=5, max_col=5, values_only=True):
                cell_value = row[0]
                if cell_value:
                    # 将单元格值转换为字符串，保留前导0
                    cell_str = str(cell_value).strip()
                    
                    # 提取数字（货号），保留前导0
                    # 使用更宽松的正则表达式，匹配包含数字的内容
                    number_match = re.search(r'(\d{3,6})', cell_str)
                    if number_match:
                        # 如果原始字符串以0开头，保留前导0
                        if cell_str.startswith('0'):
                            stock_numbers.append(cell_str)
                        else:
                            stock_numbers.append(number_match.group(1))
            
            # 去重
            stock_numbers = list(set(stock_numbers))
            print(f'从Excel文件的E列中读取到 {len(stock_numbers)} 个货号')
            
            return stock_numbers
        except Exception as e:
            print(f'读取Excel文件失败: {e}')
            import traceback
            traceback.print_exc()
            return None

    def save_input_to_file(self, input_str):
        try:
            with open(self.input_file, 'w', encoding='utf-8') as f:
                f.write(input_str)
            print(f'输入已保存到 {self.input_file}')
            return True
        except Exception as e:
            print(f'保存输入文件失败: {e}')
            return False

    def load_input_from_file(self):
        try:
            if os.path.exists(self.input_file):
                with open(self.input_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f'已从 {self.input_file} 读取输入')
                return content
            else:
                print(f'文件 {self.input_file} 不存在')
                return None
        except Exception as e:
            print(f'读取输入文件失败: {e}')
            return None

    def compare_stock_numbers(self, json_stock_numbers, input_stock_numbers):
        json_set = set(json_stock_numbers)
        input_set = set(input_stock_numbers)
        
        missing = input_set - json_set
        existing = input_set & json_set
        
        return {
            'missing': sorted(list(missing)),
            'existing': sorted(list(existing)),
            'total_input': len(input_set),
            'total_json': len(json_set),
            'missing_count': len(missing),
            'existing_count': len(existing)
        }

    def find_duplicate_stock_numbers(self, input_stock_numbers):
        seen = {}
        duplicates = []
        
        for num in input_stock_numbers:
            if num in seen:
                duplicates.append({
                    'stock_number': num,
                    'count': seen[num] + 1,
                    'positions': seen[num] + 1
                })
            else:
                seen[num] = 1
        
        return duplicates

    def save_duplicate_log(self, duplicates, log_file='file/duplicate_log.json'):
        try:
            log_data = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_duplicates': len(duplicates),
                'duplicates': duplicates
            }
            
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                if isinstance(existing_data, list):
                    log_data['history'] = existing_data
                elif isinstance(existing_data, dict) and 'history' in existing_data:
                    log_data['history'] = existing_data['history']
            
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, ensure_ascii=False, indent=2)
            
            print(f'重复序列号日志已保存到 {log_file}')
            return True
        except Exception as e:
            print(f'保存重复日志失败: {e}')
            return False

    def print_comparison_result(self, result, duplicates):
        print('\n' + '='*60)
        print('货号对比结果')
        print('='*60)
        print(f'输入货号总数: {result["total_input"]}')
        print(f'JSON中货号总数: {result["total_json"]}')
        print(f'已存在货号数: {result["existing_count"]}')
        print(f'缺失货号数: {result["missing_count"]}')
        print(f'重复序列号数: {len(duplicates)}')
        print('='*60)
        
        if result['existing']:
            print('\n已存在的货号:')
            for i, num in enumerate(result['existing'], 1):
                print(f'  {i}. {num}')
        
        if result['missing']:
            print('\n缺失的货号:')
            for i, num in enumerate(result['missing'], 1):
                print(f'  {i}. {num}')
        else:
            print('\n所有货号都已存在！')
        
        if duplicates:
            print('\n重复的序列号:')
            for i, dup in enumerate(duplicates, 1):
                print(f'  {i}. 序列号: {dup["stock_number"]} (重复次数: {dup["count"]})')
        
        print('='*60)
        
        print('\n' + '='*60)
        if result['missing_count'] == 0 and len(duplicates) == 0:
            print('对比结果: 成功 - 所有货号都存在且无重复')
        elif result['missing_count'] > 0 and len(duplicates) == 0:
            print(f'对比结果: 部分成功 - 缺失 {result["missing_count"]} 个货号')
        elif result['missing_count'] == 0 and len(duplicates) > 0:
            print(f'对比结果: 部分成功 - 发现 {len(duplicates)} 个重复序列号')
        else:
            print(f'对比结果: 失败 - 缺失 {result["missing_count"]} 个货号，发现 {len(duplicates)} 个重复序列号')
        print('='*60 + '\n')

    def run_interactive(self):
        print('\n' + '='*60)
        print('货号对比工具')
        print('='*60)
        print('功能说明：')
        print('  1. 直接输入货号字符串')
        print('  2. 输入 "load" 从本地文件读取 (config/input_stock_numbers.txt)')
        print('  3. 输入 "save" 保存当前输入到本地文件')
        print('  4. 输入 "quit" 或 "exit" 退出程序')
        print('\n输入格式支持：')
        print('  - 逗号分隔: 12345, 67890, 11111')
        print('  - 空格分隔: 12345 67890 11111')
        print('  - 混合分隔: 12345, 67890 11111; 22222')
        print('  - 多行输入: 12345\\n67890\\n11111')
        print('  - 包含"序列号"文字: 序列号 12345 67890')
        print('  - 大量空白字符: 12345,    67890,    11111')
        print('='*60 + '\n')
        
        data = self.load_json_data()
        json_stock_numbers = self.extract_stock_numbers(data)
        print(f'已加载 {len(json_stock_numbers)} 个货号\n')
        
        current_input = ''
        
        while True:
            try:
                user_input = input('请输入货号字符串 (输入 "help" 查看帮助): ').strip()
            except (EOFError, KeyboardInterrupt):
                print('\n\n程序已退出')
                break
            
            if user_input.lower() in ['quit', 'exit', 'q', '退出']:
                print('\n程序已退出')
                break
            
            if user_input.lower() in ['help', 'h', '帮助']:
                print('\n' + '='*60)
                print('帮助信息')
                print('='*60)
                print('可用命令：')
                print('  load    - 从本地文件读取（优先Excel，其次TXT）')
                print('  save    - 保存当前输入到本地文件')
                print('  quit    - 退出程序')
                print('  help    - 显示此帮助信息')
                print('\n输入格式：')
                print('  - 直接输入货号字符串')
                print('  - 支持包含"序列号"文字')
                print('  - 支持大量空白字符')
                print('  - 支持多种分隔符')
                print('  - 自动检测重复序列号')
                print(f'  - 支持Excel文件（{self.excel_file}）')
                print('  - 支持文本文件（config/input_stock_numbers.txt）')
                print('='*60 + '\n')
                continue
            
            if user_input.lower() in ['load', '读取']:
                # 优先尝试读取Excel文件
                if os.path.exists(self.excel_file):
                    print(f'检测到Excel文件: {self.excel_file}')
                    input_stock_numbers = self.load_excel_data()
                    
                    if input_stock_numbers:
                        print(f'从Excel文件读取到 {len(input_stock_numbers)} 个货号\n')
                        duplicates = self.find_duplicate_stock_numbers(input_stock_numbers)
                        if duplicates:
                            self.save_duplicate_log(duplicates)
                        
                        result = self.compare_stock_numbers(json_stock_numbers, input_stock_numbers)
                        self.print_comparison_result(result, duplicates)
                        continue
                    else:
                        print('Excel文件中未找到有效的货号\n')
                
                # 如果没有Excel文件，尝试读取文本文件
                file_content = self.load_input_from_file()
                if file_content:
                    current_input = file_content
                    input_stock_numbers = self.parse_input_string(current_input)
                    if input_stock_numbers:
                        duplicates = self.find_duplicate_stock_numbers(input_stock_numbers)
                        if duplicates:
                            self.save_duplicate_log(duplicates)
                        
                        result = self.compare_stock_numbers(json_stock_numbers, input_stock_numbers)
                        self.print_comparison_result(result, duplicates)
                    else:
                        print('文件中未找到有效的货号\n')
                else:
                    print(f'文件 {self.excel_file} 和 {self.input_file} 都不存在\n')
                continue
            
            if user_input.lower() in ['save', '保存']:
                if current_input:
                    self.save_input_to_file(current_input)
                else:
                    print('没有可保存的输入内容\n')
                continue
            
            if not user_input:
                print('输入不能为空，请重新输入或输入 "quit" 退出\n')
                continue
            
            current_input = user_input
            
            input_stock_numbers = self.parse_input_string(user_input)
            
            if not input_stock_numbers:
                print('未能解析出货号，请检查输入格式\n')
                continue
            
            duplicates = self.find_duplicate_stock_numbers(input_stock_numbers)
            if duplicates:
                self.save_duplicate_log(duplicates)
            
            result = self.compare_stock_numbers(json_stock_numbers, input_stock_numbers)
            
            self.print_comparison_result(result, duplicates)

    def run_simple(self):
        print('='*60)
        print('货号对比工具（简化版）')
        print('='*60)
        
        data = self.load_json_data()
        json_stock_numbers = self.extract_stock_numbers(data)
        print(f'已加载 {len(json_stock_numbers)} 个货号\n')
        
        # 优先尝试读取Excel文件
        if os.path.exists(self.excel_file):
            print(f'检测到Excel文件: {self.excel_file}')
            input_stock_numbers = self.load_excel_data()
            
            if input_stock_numbers:
                print(f'从Excel文件读取到 {len(input_stock_numbers)} 个货号\n')
                duplicates = self.find_duplicate_stock_numbers(input_stock_numbers)
                if duplicates:
                    self.save_duplicate_log(duplicates)
                
                result = self.compare_stock_numbers(json_stock_numbers, input_stock_numbers)
                self.print_comparison_result(result, duplicates)
                return
            else:
                print('Excel文件中未找到有效的货号\n')
        
        # 如果没有Excel文件，尝试读取文本文件
        input_file = self.input_file
        if os.path.exists(input_file):
            print(f'从文件 {input_file} 读取输入...')
            with open(input_file, 'r', encoding='utf-8') as f:
                input_str = f.read()
            
            input_stock_numbers = self.parse_input_string(input_str)
            
            if input_stock_numbers:
                print(f'解析出 {len(input_stock_numbers)} 个货号\n')
                duplicates = self.find_duplicate_stock_numbers(input_stock_numbers)
                if duplicates:
                    self.save_duplicate_log(duplicates)
                
                result = self.compare_stock_numbers(json_stock_numbers, input_stock_numbers)
                self.print_comparison_result(result, duplicates)
            else:
                print('文件中未找到有效的货号\n')
        else:
            print(f'文件 {self.excel_file} 和 {self.input_file} 都不存在')
            print('请创建 config/input_stock_numbers.txt 文件或确保Excel文件存在\n')


def main():
    print('='*60)
    print('Szwego商品爬虫和货号对比工具 - 跨系统版本')
    print('='*60)
    print('请选择功能：')
    print('1. 运行爬虫')
    print('2. 货号对比（交互式）')
    print('3. 货号对比（简化版）')
    print('0. 退出')
    print('='*60)
    
    try:
        choice = input('请输入选项 (0-3): ').strip()
    except (EOFError, KeyboardInterrupt):
        print('\n程序已退出')
        return
    
    if choice == '1':
        scraper = WegoScraper()
        asyncio.run(scraper.run())
    elif choice == '2':
        comparator = StockNumberComparator()
        comparator.run_interactive()
    elif choice == '3':
        comparator = StockNumberComparator()
        comparator.run_simple()
    elif choice == '0':
        print('程序已退出')
    else:
        print('无效的选项')


if __name__ == '__main__':
    main()