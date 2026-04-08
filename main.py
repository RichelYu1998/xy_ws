import json
import time
import asyncio
import os
import re
import platform
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


VERSION = "2.1.0"


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


class ConfigManager:
    def __init__(self, config_path='config/config.json'):
        self.config_path = config_path
        self._config = None

    @property
    def config(self):
        if self._config is None:
            self._config = self._load_config()
        return self._config

    def _load_config(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f'加载配置文件失败: {e}')
            return {}

    def save_config(self):
        if self._config:
            try:
                with open(self.config_path, 'w', encoding='utf-8') as f:
                    json.dump(self._config, f, ensure_ascii=False, indent=2)
                return True
            except Exception as e:
                print(f'保存配置文件失败: {e}')
        return False

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        if self._config is not None:
            self._config[key] = value
            self.save_config()

    def get_cookie_file(self):
        return self.config.get('cookie_file', 'config/cookies.json')

    def get_output_file(self):
        return self.config.get('output_file', 'file/output.json')

    def get_excel_file(self):
        return self.config.get('excel_file', '')

    def get_target_url(self):
        return self.config.get('target_url', '')

    def get_user_agent(self):
        return self.config.get('user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')


class FileManager:
    @staticmethod
    def read_json(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f'读取JSON文件失败 {file_path}: {e}')
            return None

    @staticmethod
    def write_json(file_path, data, indent=2):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
            return True
        except Exception as e:
            print(f'写入JSON文件失败 {file_path}: {e}')
            return False

    @staticmethod
    def read_text(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f'读取文本文件失败 {file_path}: {e}')
            return None

    @staticmethod
    def write_text(file_path, content):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f'写入文本文件失败 {file_path}: {e}')
            return False

    @staticmethod
    def file_exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def get_latest_json_file(directory='file', pattern='微购相册'):
        try:
            if not os.path.exists(directory):
                print(f'目录 {directory} 不存在')
                return None
            
            json_files = []
            for file in os.listdir(directory):
                if file.endswith('.json') and pattern in file:
                    file_path = os.path.join(directory, file)
                    json_files.append((file_path, os.path.getmtime(file_path)))
            
            if not json_files:
                print(f'未找到包含"{pattern}"的JSON文件')
                return None
            
            json_files.sort(key=lambda x: x[1], reverse=True)
            latest_file = json_files[0][0]
            print(f'找到最新的JSON文件: {latest_file}')
            return latest_file
        except Exception as e:
            print(f'获取最新JSON文件失败: {e}')
            return None

    @staticmethod
    def get_today_json_files(directory='file', pattern='微购相册'):
        """
        获取当天最新的两个JSON文件
        """
        try:
            if not os.path.exists(directory):
                print(f'目录 {directory} 不存在')
                return None, None
            
            today = datetime.now().strftime('%Y%m%d')
            json_files = []
            for file in os.listdir(directory):
                if file.endswith('.json') and pattern in file and today in file:
                    file_path = os.path.join(directory, file)
                    json_files.append((file_path, os.path.getmtime(file_path)))
            
            if len(json_files) < 2:
                print(f'当天未找到至少2个包含"{pattern}"的JSON文件')
                return None, None
            
            json_files.sort(key=lambda x: x[1], reverse=True)
            latest_file = json_files[0][0]
            second_latest_file = json_files[1][0]
            print(f'找到当天最新的JSON文件: {latest_file}')
            print(f'找到当天次新的JSON文件: {second_latest_file}')
            return latest_file, second_latest_file
        except Exception as e:
            print(f'获取当天JSON文件失败: {e}')
            return None, None

    @staticmethod
    def list_files(directory, pattern=None):
        try:
            if not os.path.exists(directory):
                return []
            
            files = os.listdir(directory)
            if pattern:
                files = [f for f in files if pattern in f]
            return files
        except Exception as e:
            print(f'列出文件失败: {e}')
            return []


class WegoScraper:
    def __init__(self, config_path='config/config.json'):
        self.config_manager = ConfigManager(config_path)

    @staticmethod
    def get_system_info():
        system = platform.system()
        return {'Windows': 'Windows', 'Darwin': 'Mac', 'Linux': 'Linux'}.get(system, 'Unknown')

    @staticmethod
    def clean_product_name(text):
        if not text:
            return None
        
        text = re.sub(r'¥\d+', '', text)
        
        for pattern in [r'删除下载刷新编辑分享商品属性标签', r'售价：', r'昨天分享']:
            text = re.sub(pattern, '', text)
        
        text = re.sub(r'\s+', ' ', text).strip()
        return text if text else None

    async def close_popups(self, page, close_limit=3, wait_time=0.3):
        popup_selectors = [
            '[class*="close"]', '[class*="modal-close"]', '[class*="dialog-close"]',
            'button:has-text("关闭")', 'button:has-text("×")', 'button:has-text("✕")',
            '.ant-modal-close', '.el-dialog__close',
        ]
        
        closed_count = 0
        for selector in popup_selectors:
            try:
                close_button = await page.query_selector(selector)
                if close_button:
                    await close_button.click()
                    print(f'关闭了弹窗: {selector}')
                    await asyncio.sleep(wait_time)
                    closed_count += 1
                    if closed_count >= close_limit:
                        break
            except Exception as e:
                pass

    async def scroll_to_load_all(self, page):
        print('开始滚动加载所有商品...')
        
        scroll_config = self.config_manager.get('scroll_config', {})
        max_attempts = scroll_config.get('max_attempts', 20)
        same_height_limit = scroll_config.get('same_height_limit', 5)
        scroll_wait_time = scroll_config.get('scroll_wait_time', 1.5)
        popup_close_interval = scroll_config.get('popup_close_interval', 5)
        popup_close_limit = scroll_config.get('popup_close_limit', 3)
        popup_close_wait = scroll_config.get('popup_close_wait', 0.3)
        
        print(f'滚动配置: 最大尝试{max_attempts}次, 高度不变限制{same_height_limit}次, 等待时间{scroll_wait_time}秒')
        
        last_height = 0
        scroll_attempts = 0
        no_change_count = 0
        height_history = []
        dynamic_adjust = scroll_config.get('dynamic_adjust', True)
        
        while scroll_attempts < max_attempts:
            try:
                start_time = time.time()
                current_height = await page.evaluate('document.body.scrollHeight')
                load_time = time.time() - start_time
                
                height_history.append(current_height)
                if len(height_history) > 10:
                    height_history.pop(0)
                
                if current_height == last_height:
                    no_change_count += 1
                    if no_change_count >= same_height_limit:
                        print(f'页面已滚动到底部（高度连续{same_height_limit}次不变: {current_height}），停止滚动')
                        break
                else:
                    no_change_count = 0
                    last_height = current_height
                
                await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                await asyncio.sleep(scroll_wait_time)
                scroll_attempts += 1
                
                progress_percent = min(100, int((scroll_attempts / max_attempts) * 100))
                print(f'滚动 {scroll_attempts}/{max_attempts} ({progress_percent}%) - 当前高度: {current_height} - 加载耗时: {load_time:.2f}秒')
                
                if dynamic_adjust and len(height_history) >= 5:
                    height_changes = [abs(height_history[i] - height_history[i-1]) for i in range(1, len(height_history))]
                    avg_change = sum(height_changes) / len(height_changes)
                    
                    if avg_change < 100 and scroll_wait_time < 3.0:
                        scroll_wait_time = min(3.0, scroll_wait_time + 0.2)
                        print(f'  ⚠️  页面加载较慢，增加等待时间至 {scroll_wait_time:.1f}秒')
                    elif avg_change > 500 and scroll_wait_time > 0.5:
                        scroll_wait_time = max(0.5, scroll_wait_time - 0.2)
                        print(f'  ✅ 页面加载较快，减少等待时间至 {scroll_wait_time:.1f}秒')
                
                if scroll_attempts % popup_close_interval == 0:
                    await self.close_popups(page, popup_close_limit, popup_close_wait)
            except Exception as e:
                print(f'滚动时出错: {e}')
                break
        
        print('滚动完成')

    @staticmethod
    def extract_product_info(element_text, html_content):
        try:
            stock_match = re.search(r'货号[：:]\s*(\d+)', element_text)
            stock_number = stock_match.group(1) if stock_match else ''
            
            price_patterns = [
                r'售价[：:]\s*¥?\s*(\d{3,6})',
                r'¥(\d{4,6})',
                r'(\d{4,6})\s*$',
                r'货号[：:]\s*\d+\s*(\d{4,6})'
            ]
            
            price = None
            for pattern in price_patterns:
                match = re.search(pattern, element_text)
                if match:
                    price = '¥' + match.group(1)
                    break
            
            remark_match = re.search(r'备注[：:]\s*(.+?)(?:\s*员工[：:]|$)', element_text, re.DOTALL)
            remark = re.sub(r'\s+', ' ', remark_match.group(1).strip()) if remark_match else None
            
            employee_match = re.search(r'员工[：:]\s*(.+)', element_text)
            employee = employee_match.group(1).strip() if employee_match else None
            
            cut_pos = min(
                len(element_text),
                *(pos for pos in [element_text.find('¥'), element_text.find('删除'), element_text.find('货号')] if pos > 0)
            )
            
            if cut_pos < len(element_text) and cut_pos > 10:
                name_part = re.sub(r'\s+', ' ', element_text[:cut_pos].strip())
                name = WegoScraper.clean_product_name(name_part) if name_part else None
            else:
                name = WegoScraper.clean_product_name(element_text)
            
            if name:
                cleaned_name = WegoScraper.clean_product_name(name)
                if cleaned_name:
                    return {
                        '商品名称': cleaned_name,
                        '售价': price if price else '',
                        '货号': stock_number,
                        '备注': remark if remark else '',
                        '员工': employee if employee else ''
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
            futures = [executor.submit(self.extract_product_info, text, html) for text, html in elements_data]
            
            for i, future in enumerate(futures):
                try:
                    result = future.result(timeout=5)
                    if result:
                        product_key = result['货号'] if result['货号'] else result['商品名称']
                        if product_key not in seen_products:
                            seen_products.add(product_key)
                            products.append(result)
                            
                            if len(products) <= 10:
                                print(f'商品 {len(products)}: {result["商品名称"][:50]}...')
                                print(f'  售价: {result["售价"]}')
                                print(f'  货号: {result["货号"]}\n')
                except Exception as e:
                    print(f'处理商品 {i} 时出错: {e}')
                    continue
        
        return products

    async def get_data_with_playwright(self, page):
        try:
            target_url = self.config_manager.get_target_url()
            print(f'正在访问目标页面: {target_url}')
            print(f'当前系统: {self.get_system_info()}')
            
            try:
                await page.goto(target_url, timeout=60000, wait_until='domcontentloaded')
                print('页面DOM已加载')
            except Exception as e:
                print(f'页面导航出错: {e}')
                print('尝试继续执行...')
                await asyncio.sleep(2)
            
            print('等待页面完全加载...')
            await asyncio.sleep(2)
            
            await self.close_popups(page)
            print('滚动加载所有商品...')
            await self.scroll_to_load_all(page)
            
            print('等待页面完全加载...')
            await asyncio.sleep(5)
            
            # 等待商品元素加载
            print('等待商品元素加载...')
            try:
                await page.wait_for_selector('.normal_item-module_normalItemContent_mrLg3', timeout=30000)
                print('商品元素已加载')
            except Exception as e:
                print(f'等待商品元素超时: {e}')
                print('尝试继续执行...')
            
            page_text = await page.content()
            
            total_count = None
            new_count = None
            
            total_patterns = [
                (r'上新\s*(\d+)\s*\|\s*总数\s*(\d+)', lambda m: (int(m.group(1)), int(m.group(2)))),
                (r'总数\s*[：:]\s*(\d+)', lambda m: (None, int(m.group(1)))),
                (r'总\s*数\s*[：:]\s*(\d+)', lambda m: (None, int(m.group(1)))),
            ]
            
            for pattern, extractor in total_patterns:
                match = re.search(pattern, page_text)
                if match:
                    result = extractor(match)
                    if len(result) == 2:
                        new_count, total_count = result
                        if new_count:
                            print(f'网页显示上新: {new_count}, 总数: {total_count}')
                        else:
                            print(f'网页显示总数: {total_count}')
                        break
            
            if not new_count:
                new_match = re.search(r'上新\s*[：:]\s*(\d+)', page_text)
                if new_match:
                    new_count = int(new_match.group(1))
                    print(f'网页显示上新: {new_count}')
            
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
                        item_elements.extend(elements)
                except Exception as e:
                    print(f'使用选择器 {selector} 时出错: {e}')
                    continue
            
            item_elements = list(dict.fromkeys(item_elements))
            print(f'总共找到 {len(item_elements)} 个商品项')
            
            if not item_elements:
                print('警告: 未找到任何商品项，可能页面加载失败或选择器不正确')
                print('建议检查页面URL和Cookie是否有效')
            
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

    @staticmethod
    def parse_price(price_str):
        """解析价格字符串，返回整数价格或None"""
        if not price_str:
            return None
        price_clean = price_str.replace('¥', '').replace(',', '').strip()
        if not price_clean.isdigit():
            return None
        return int(price_clean)

    def filter_high_price_products(self, data, min_price=599):
        """筛选高价商品"""
        return [p for p in data if self.parse_price(p.get('售价', '')) and self.parse_price(p.get('售价', '')) >= min_price]

    def analyze_data_changes(self, data, previous_file):
        """分析数据变化"""
        if not previous_file:
            return ""
        
        try:
            old_data = FileManager.read_json(f'file/{previous_file}')
            if not old_data:
                return ""
            
            old_items = old_data.get('商品列表', [])
            old_nums = {item.get('货号', '') for item in old_items if item.get('货号')}
            current_nums = {item.get('货号', '') for item in data if item.get('货号')}
            
            added = current_nums - old_nums
            removed = old_nums - current_nums
            
            if not added and not removed:
                return "数据无变化"
            
            def get_product_detail(item):
                return {
                    "商品名称": item.get('商品名称', ''),
                    "售价": item.get('售价', ''),
                    "货号": item.get('货号', ''),
                    "备注": item.get('备注', ''),
                    "员工": item.get('员工', '')
                }
            
            def format_json_array(items):
                if not items:
                    return "[]"
                lines = ["["]
                for i, item in enumerate(items):
                    lines.append('  {')
                    for j, (k, v) in enumerate(item.items()):
                        lines.append(f'    "{k}": "{v}"' + (',' if j < len(item) - 1 else ''))
                    lines.append('  }' + (',' if i < len(items) - 1 else ''))
                lines.append("]")
                return '\n'.join(lines)
            
            added_details = [get_product_detail(item) for item in data if item.get('货号') in added]
            removed_details = [get_product_detail(item) for item in old_items if item.get('货号') in removed]
            
            return f"对比 {old_data.get('生成日期', 'N/A')} 新增 {len(added)} 个，删除 {len(removed)} 个\n【新增商品】({len(added)}个):\n{format_json_array(added_details)}\n【删除商品】({len(removed)}个):\n{format_json_array(removed_details)}"
        except Exception as e:
            return f"对比分析失败: {str(e)}"

    def save_data(self, data, filename=None):
        today = datetime.now().strftime('%Y%m%d')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_filename = f"file/{today}微购相册(小旭数码).json"
        
        total_count = len(data)
        high_price_products = self.filter_high_price_products(data)
        high_price_count = len(high_price_products)
        
        existing_files = sorted(FileManager.list_files('file', '微购相册'), reverse=True)
        
        previous_file = None
        for f in existing_files:
            if f != f"{today}微购相册(小旭数码).json":
                previous_file = f
                break
        
        change_summary = self.analyze_data_changes(data, previous_file)
        
        output_data = {
            "生成日期": today,
            "时间戳": current_time,
            "成功获取": f"{total_count} 个商品",
            "商品列表": data,
            "统计": f"共计获取到 {total_count} 个商品",
        }
        
        if change_summary:
            output_data["小计"] = change_summary
        
        output_data["高价商品统计"] = {
            "筛选条件": "售价 >= 599",
            "数量": high_price_count,
            "商品列表": high_price_products
        }
        
        FileManager.write_json(new_filename, output_data)
        print(f'数据已保存到 {new_filename}')
        print(f'成功获取 {total_count} 个商品')
        print(f'售价 >= 599 的商品: {high_price_count} 个')
        if change_summary:
            print(f'{change_summary}')

    async def run(self):
        start_time = time.time()
        start_datetime = datetime.now()
        
        try:
            print('='*50)
            print(f'Szwego商品爬虫 - v{VERSION}')
            print(f'当前系统: {self.get_system_info()}')
            print(f'Python版本: {platform.python_version()}')
            print(f'开始时间: {start_datetime.strftime("%Y-%m-%d %H:%M:%S")}')
            print('='*50)
            print('开始运行...')
            
            async with async_playwright() as p:
                print('正在启动浏览器...')
                
                system = self.get_system_info()
                browser_args = ['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled', '--disable-dev-shm-usage']
                
                chrome_path = None
                if system == 'Windows':
                    browser_args.append('--disable-gpu')
                    if os.path.exists(r'C:\Program Files\Google\Chrome\Application\chrome.exe'):
                        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                elif system == 'Linux':
                    browser_args.extend(['--disable-gpu', '--disable-dev-shm-usage'])
                    if os.path.exists('/usr/bin/google-chrome'):
                        chrome_path = '/usr/bin/google-chrome'
                elif system == 'Mac':
                    if os.path.exists('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'):
                        chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                
                print(f'检测到系统: {system}')
                if chrome_path:
                    print(f'使用系统Chrome: {chrome_path}')
                else:
                    print(f'使用Playwright内置Chromium')
                
                browser = await p.chromium.launch(headless=False, args=browser_args, executable_path=chrome_path)
                context = await browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent=self.config_manager.get_user_agent()
                )
                
                cookie_file = self.config_manager.get_cookie_file()
                if FileManager.file_exists(cookie_file):
                    cookies = FileManager.read_json(cookie_file)
                    if cookies:
                        print(f'已加载 {len(cookies)} 个Cookie')
                        await context.add_cookies(cookies)
                
                page = await context.new_page()
                products = await self.get_data_with_playwright(page)
                
                if products:
                    self.save_data(products)
                
                cookies = await context.cookies()
                FileManager.write_json(cookie_file, cookies)
                print(f'Cookie已保存到 {cookie_file}')
                
                await browser.close()
                
        except Exception as e:
            print(f'运行失败: {e}')
            import traceback
            traceback.print_exc()
        finally:
            end_time = time.time()
            end_datetime = datetime.now()
            total_time = end_time - start_time
            
            print('='*50)
            print(f'结束时间: {end_datetime.strftime("%Y-%m-%d %H:%M:%S")}')
            print(f'总运行时间: {total_time:.2f} 秒 ({total_time/60:.2f} 分钟)')
            print('='*50)


class StockNumberComparator:
    def __init__(self, output_file='file/output.json', input_file='config/input_stock_numbers.txt', config_path='config/config.json'):
        self.output_file = output_file
        self.input_file = input_file
        self.config_manager = ConfigManager(config_path)
        self.excel_file = self._get_excel_file()

    def _get_excel_file(self):
        excel_file = self.config_manager.get_excel_file()
        if excel_file and FileManager.file_exists(excel_file):
            return excel_file
        return None

    def load_json_data(self):
        return FileManager.read_json(self.output_file) or []

    @staticmethod
    def extract_stock_numbers(data):
        return {item.get('货号') for item in data if item.get('货号') and item['货号'] != 'N/A'}

    @staticmethod
    def parse_input_string(input_str):
        if not input_str:
            return []
        
        cleaned = re.sub(r'序列号', '', input_str)
        numbers = re.split(r'[,，\s;；\n\t]+', cleaned)
        return [num.strip() for num in numbers if num.strip()]

    def load_excel_data(self, excel_file=None):
        if excel_file is None:
            excel_file = self.excel_file
        
        if not excel_file:
            return None
        
        try:
            if not FileManager.file_exists(excel_file):
                return None
            
            print(f'正在读取Excel文件: {excel_file}')
            workbook = openpyxl.load_workbook(excel_file)
            
            sheet = next((workbook[sheet_name] for sheet_name in workbook.sheetnames if '闲鱼' in sheet_name), None)
            
            if sheet is None:
                print('未找到"闲鱼"工作表，使用第一个工作表')
                sheet = workbook.active
            else:
                print(f'使用工作表: {sheet.title}')
            
            stock_numbers = []
            for row in sheet.iter_rows(min_col=5, max_col=5, values_only=True):
                cell_value = row[0]
                if cell_value:
                    cell_str = str(cell_value).strip()
                    number_match = re.search(r'(\d{3,6})', cell_str)
                    if number_match:
                        stock_numbers.append(cell_str if cell_str.startswith('0') else number_match.group(1))
            
            stock_numbers = list(set(stock_numbers))
            print(f'从Excel文件的E列中读取到 {len(stock_numbers)} 个货号')
            return stock_numbers
        except Exception as e:
            print(f'读取Excel文件失败: {e}')
            import traceback
            traceback.print_exc()
            return None

    def save_input_to_file(self, input_str):
        if FileManager.write_text(self.input_file, input_str):
            print(f'输入已保存到 {self.input_file}')
            return True
        return False

    def load_input_from_file(self):
        return FileManager.read_text(self.input_file)

    @staticmethod
    def compare_stock_numbers(json_stock_numbers, input_stock_numbers, high_price_stock_numbers=None):
        json_set = set(json_stock_numbers)
        input_set = set(input_stock_numbers)
        
        result = {
            'missing': sorted(list(input_set - json_set)),
            'existing': sorted(list(input_set & json_set)),
            'extra_in_json': sorted(list(json_set - input_set)),
            'total_input': len(input_set),
            'total_json': len(json_set),
            'missing_count': len(input_set - json_set),
            'existing_count': len(input_set & json_set),
            'extra_in_json_count': len(json_set - input_set)
        }
        
        if high_price_stock_numbers:
            result['high_price_stock_numbers'] = sorted(list(set(high_price_stock_numbers)))
            result['high_price_count'] = len(result['high_price_stock_numbers'])
        
        return result

    @staticmethod
    def find_duplicate_stock_numbers(input_stock_numbers):
        seen = {}
        for num in input_stock_numbers:
            seen[num] = seen.get(num, 0) + 1
        
        return [{'货号': num, 'count': count, 'positions': count} 
                for num, count in seen.items() if count > 1]

    def save_duplicate_log(self, duplicates, log_file='file/duplicate_log.json'):
        try:
            log_data = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_duplicates': len(duplicates),
                'duplicates': duplicates
            }
            
            if FileManager.file_exists(log_file):
                existing_data = FileManager.read_json(log_file)
                if isinstance(existing_data, list):
                    log_data['history'] = existing_data
                elif isinstance(existing_data, dict) and 'history' in existing_data:
                    log_data['history'] = existing_data['history']
            
            FileManager.write_json(log_file, log_data)
            print(f'重复序列号日志已保存到 {log_file}')
            return True
        except Exception as e:
            print(f'保存重复日志失败: {e}')
            return False

    def compare_json_files(self):
        """
        对比当天最新的两个JSON文件，将差异写进最新的JSON文件中
        """
        try:
            print('='*60)
            print('当天JSON文件对比工具')
            print('='*60)
            
            # 获取当天最新的两个JSON文件
            latest_json_file, second_latest_json_file = FileManager.get_today_json_files()
            if not latest_json_file or not second_latest_json_file:
                print('无法获取当天的JSON文件')
                return False
            
            # 读取最新的JSON文件
            latest_json_data = FileManager.read_json(latest_json_file)
            if not latest_json_data:
                print('无法读取最新的JSON文件')
                return False
            
            # 读取次新的JSON文件
            second_json_data = FileManager.read_json(second_latest_json_file)
            if not second_json_data:
                print('无法读取次新的JSON文件')
                return False
            
            # 提取商品列表
            latest_products = latest_json_data.get('商品列表', [])
            second_products = second_json_data.get('商品列表', [])
            
            if not latest_products or not second_products:
                print('JSON文件中没有商品列表')
                return False
            
            # 提取货号
            latest_stock_numbers = {item.get('货号', '') for item in latest_products if item.get('货号')}
            second_stock_numbers = {item.get('货号', '') for item in second_products if item.get('货号')}
            
            print(f'从最新JSON文件中读取到 {len(latest_stock_numbers)} 个货号')
            print(f'从次新JSON文件中读取到 {len(second_stock_numbers)} 个货号\n')
            
            # 计算差异
            added = latest_stock_numbers - second_stock_numbers
            removed = second_stock_numbers - latest_stock_numbers
            
            # 找出售价>=599的商品货号
            high_price_stock_numbers = []
            for product in latest_products:
                price = WegoScraper.parse_price(product.get('售价', ''))
                if price and price >= 599:
                    stock_num = product.get('货号', '')
                    if stock_num:
                        high_price_stock_numbers.append(stock_num)
            
            # 筛选新增的高价商品
            high_price_added = []
            if high_price_stock_numbers and added:
                for stock_num in high_price_stock_numbers:
                    if stock_num in added:
                        high_price_added.append(stock_num)
            
            # 生成差异报告
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_str = datetime.now().strftime('%Y%m%d')
            
            diff_data = {
                'timestamp': timestamp,
                'date': date_str,
                'latest_file': os.path.basename(latest_json_file),
                'second_file': os.path.basename(second_latest_json_file),
                'added_count': len(added),
                'removed_count': len(removed),
                'added': sorted(list(added)),
                'removed': sorted(list(removed)),
                'high_price_added': sorted(list(high_price_added)),
                'high_price_added_count': len(high_price_added),
                'high_price_description': '新增的售价>=599的商品'
            }
            
            # 将差异信息写入最新的JSON文件
            latest_json_data['对比差异'] = diff_data
            FileManager.write_json(latest_json_file, latest_json_data)
            print(f'\n对比差异已写入 {latest_json_file}')
            
            # 打印对比结果
            print('\n' + '='*60)
            print('对比结果')
            print('='*60)
            print(f'对比文件: {os.path.basename(second_latest_json_file)} -> {os.path.basename(latest_json_file)}')
            print(f'新增商品数: {len(added)}')
            print(f'删除商品数: {len(removed)}')
            print(f'新增高价商品数: {len(high_price_added)}')
            print('='*60)
            
            if added:
                print('\n新增的商品:')
                for i, num in enumerate(added, 1):
                    print(f'  {i}. {num}')
            
            if removed:
                print('\n删除的商品:')
                for i, num in enumerate(removed, 1):
                    print(f'  {i}. {num}')
            
            if high_price_added:
                print(f'\n新增的售价>=599的商品:')
                for i, num in enumerate(high_price_added, 1):
                    print(f'  {i}. {num}')
            
            print('='*60 + '\n')
            return True
        except Exception as e:
            print(f'对比失败: {e}')
            import traceback
            traceback.print_exc()
            return False

    def compare_excel_with_json(self):
        try:
            print('='*60)
            print('Excel与JSON数据对比工具')
            print('='*60)
            
            latest_json_file = FileManager.get_latest_json_file()
            if not latest_json_file:
                print('无法获取最新的JSON文件')
                return False
            
            json_data = FileManager.read_json(latest_json_file)
            if not json_data:
                print('无法读取JSON文件')
                return False
            
            if isinstance(json_data, dict) and '商品列表' in json_data:
                json_data = json_data['商品列表']
            
            json_stock_numbers = self.extract_stock_numbers(json_data)
            print(f'从JSON文件中读取到 {len(json_stock_numbers)} 个货号\n')
            
            # 找出售价>=599的商品货号
            high_price_stock_numbers = []
            if isinstance(json_data, list):
                for product in json_data:
                    price = WegoScraper.parse_price(product.get('售价', ''))
                    if price and price >= 599:
                        stock_num = product.get('货号', '')
                        if stock_num:
                            high_price_stock_numbers.append(stock_num)
            
            excel_stock_numbers = self.load_excel_data()
            
            # 筛选只在JSON中存在但不在Excel中的售价>=599的商品货号
            high_price_extra_in_json = []
            if high_price_stock_numbers and excel_stock_numbers:
                json_set = set(json_stock_numbers)
                excel_set = set(excel_stock_numbers)
                extra_in_json_set = json_set - excel_set
                for stock_num in high_price_stock_numbers:
                    if stock_num in extra_in_json_set:
                        high_price_extra_in_json.append(stock_num)
            
            if not excel_stock_numbers:
                print('无法从Excel文件读取货号')
                return False
            
            result = self.compare_stock_numbers(json_stock_numbers, excel_stock_numbers, high_price_extra_in_json)
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_str = datetime.now().strftime('%Y%m%d')
            
            result_message = self.get_result_message(result, [])
            
            if result['missing_count'] == 0 and result.get('extra_in_json_count', 0) == 0:
                data_change = "数据无变化"
            else:
                data_change = f"数据有变化：缺失 {result['missing_count']} 个货号，多余 {result.get('extra_in_json_count', 0)} 个货号"
            
            comparison_with_descriptions = {
                'missing_description': '微购相册比本地表格多出的序列号仅供参考',
                'existing_description': '本地表格比微购相册上多的序列号，请仔细核对后删除多出的地方',
                'extra_in_json_description': '微购相册比本地表格多出的序列号',
                'high_price_extra_in_json': high_price_extra_in_json,
                'high_price_extra_in_json_count': len(high_price_extra_in_json),
                'high_price_extra_in_json_description': '只在JSON中存在但不在Excel中的售价>=599的货号',
                **result
            }
            
            def get_product_detail(item, stock_num=None):
                return {
                    "商品名称": item.get('商品名称', ''),
                    "售价": item.get('售价', ''),
                    "货号": stock_num or item.get('货号', ''),
                    "备注": item.get('备注', ''),
                    "员工": item.get('员工', '')
                }
            
            added_products = [get_product_detail(p, p.get('货号')) for p in json_data if p.get('货号') and p.get('货号') not in set(excel_stock_numbers)] if isinstance(json_data, list) and excel_stock_numbers else []
            
            prev_file = FileManager.get_latest_json_file('微购相册')
            removed_products = []
            if prev_file and prev_file != latest_json_file:
                old_data = FileManager.read_json(prev_file)
                if old_data and isinstance(old_data, dict):
                    old_items = old_data.get('商品列表', [])
                    removed_products = [get_product_detail(item) for item in old_items if item.get('货号') and item.get('货号') not in set(json_stock_numbers)]
            
            diff_data = {
                'timestamp': timestamp,
                'date': date_str,
                'json_file': os.path.basename(latest_json_file),
                'excel_file': os.path.basename(self.excel_file),
                'comparison': comparison_with_descriptions,
                'result_message': result_message,
                'data_change': data_change,
                'high_price_extra_in_json': high_price_extra_in_json,
                'high_price_extra_in_json_count': len(high_price_extra_in_json),
                'high_price_extra_in_json_description': '只在JSON中存在但不在Excel中的售价>=599的货号',
                '新增商品': added_products,
                '新增商品数量': len(added_products),
                '删除商品': removed_products,
                '删除商品数量': len(removed_products)
            }
            
            diff_log_file = f'file/diff_log_{date_str}.json'
            
            if FileManager.file_exists(diff_log_file):
                existing_data = FileManager.read_json(diff_log_file)
                if isinstance(existing_data, list):
                    existing_data.append(diff_data)
                elif isinstance(existing_data, dict) and 'logs' in existing_data:
                    existing_data['logs'].append(diff_data)
                else:
                    existing_data = {'logs': [existing_data, diff_data]}
            else:
                existing_data = {'logs': [diff_data]}
            
            FileManager.write_json(diff_log_file, existing_data)
            print(f'\n差异日志已保存到 {diff_log_file}')
            
            # 将高价商品信息写入原始JSON文件
            self.add_high_price_info_to_json(latest_json_file, high_price_extra_in_json)
            
            self.print_comparison_result(result, [])
            return True
        except Exception as e:
            print(f'对比失败: {e}')
            import traceback
            traceback.print_exc()
            return False

    @staticmethod
    def get_result_message(result, duplicates):
        if result['missing_count'] == 0 and len(duplicates) == 0:
            return '对比结果: 成功 - 所有货号都存在且无重复'
        elif result['missing_count'] > 0 and len(duplicates) == 0:
            return f'对比结果: 部分成功 - 缺失 {result["missing_count"]} 个货号'
        elif result['missing_count'] == 0 and len(duplicates) > 0:
            return f'对比结果: 部分成功 - 发现 {len(duplicates)} 个重复序列号'
        else:
            return f'对比结果: 失败 - 缺失 {result["missing_count"]} 个货号，发现 {len(duplicates)} 个重复序列号'

    @staticmethod
    def print_comparison_result(result, duplicates):
        print('\n' + '='*60)
        print('货号对比结果')
        print('='*60)
        print(f'输入货号总数: {result["total_input"]}')
        print(f'JSON中货号总数: {result["total_json"]}')
        print(f'已存在货号数: {result["existing_count"]}')
        print(f'缺失货号数: {result["missing_count"]}')
        print(f'JSON中多余货号数: {result.get("extra_in_json_count", 0)}')
        print(f'重复序列号数: {len(duplicates)}')
        if result.get('high_price_count'):
            print(f'只在JSON中存在但不在Excel中的售价>=599货号数: {result["high_price_count"]}')
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
            print('\n所有输入货号都已存在！')
        
        if result.get('extra_in_json'):
            print('\nJSON中多余的货号:')
            for i, num in enumerate(result['extra_in_json'], 1):
                print(f'  {i}. {num}')
        
        if result.get('high_price_stock_numbers'):
            print(f'\n只在JSON中存在但不在Excel中的售价>=599的货号:')
            for i, num in enumerate(result['high_price_stock_numbers'], 1):
                print(f'  {i}. {num}')
        
        if duplicates:
            print('\n重复的序列号:')
            for i, dup in enumerate(duplicates, 1):
                print(f'  {i}. 序列号: {dup["货号"]} (重复次数: {dup["count"]})')
        
        print('='*60)
        
        print('\n' + '='*60)
        print(StockNumberComparator.get_result_message(result, duplicates))
        print('='*60 + '\n')

    def add_high_price_info_to_json(self, json_file_path, high_price_stock_numbers):
        """
        将高价商品信息写入原始JSON文件
        """
        try:
            # 读取原始JSON数据
            json_data = FileManager.read_json(json_file_path)
            if not json_data:
                print(f'无法读取JSON文件: {json_file_path}')
                return
            
            # 获取商品列表
            products = json_data.get('商品列表', [])
            if not products:
                print(f'JSON文件中没有商品列表')
                return
            
            # 为高价商品添加备注
            high_price_count = 0
            for product in products:
                stock_num = product.get('货号', '')
                if stock_num in high_price_stock_numbers:
                    # 添加高价商品备注
                    product['备注'] = f'高价商品(≥599) - 只在JSON中存在但不在Excel中'
                    high_price_count += 1
            
            # 更新统计信息
            if '统计信息' not in json_data:
                json_data['统计信息'] = {}
            
            json_data['统计信息']['高价商品数量'] = high_price_count
            json_data['统计信息']['高价商品货号'] = high_price_stock_numbers
            json_data['统计信息']['高价商品描述'] = '只在JSON中存在但不在Excel中的售价>=599的货号'
            
            # 保存更新后的JSON文件
            FileManager.write_json(json_file_path, json_data)
            print(f'已为 {high_price_count} 个高价商品添加备注，并更新统计信息到 {json_file_path}')
            
        except Exception as e:
            print(f'添加高价商品信息失败: {e}')

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
                if FileManager.file_exists(self.excel_file):
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
        
        if FileManager.file_exists(self.excel_file):
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
        
        if FileManager.file_exists(self.input_file):
            print(f'从文件 {self.input_file} 读取输入...')
            input_str = FileManager.read_text(self.input_file)
            
            if input_str:
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
                print('文件读取失败\n')
        else:
            print(f'文件 {self.excel_file} 和 {self.input_file} 都不存在')
            print('请创建 config/input_stock_numbers.txt 文件或确保Excel文件存在\n')


def main():
    while True:
        print('='*60)
        print(f'Szwego商品爬虫和货号对比工具 - v{VERSION}')
        print('='*60)
        
        if not FileManager.file_exists('config/config.json'):
            print('⚠️  警告: 配置文件不存在 (config/config.json)')
            print('请先配置 config/config.json 文件')
            print('='*60)
            input('按回车键退出...')
            return
        
        if not FileManager.file_exists('config/cookies.json'):
            print('⚠️  警告: Cookie文件不存在 (config/cookies.json)')
            print('建议先运行"更新Cookie"功能')
            print('='*60)
        
        print('请选择功能：')
        print('1. 运行爬虫')
        print('2. 货号对比（交互式）')
        print('3. 货号对比（简化版）')
        print('4. Excel与JSON对比（自动保存差异日志）')
        print('5. 当天JSON文件对比（对比当天最新两个文件）')
        print('6. 更新Cookie')
        print('0. 退出')
        print('='*60)
        
        try:
            choice = input('请输入选项 (0-6): ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n程序已退出')
            return
        
        actions = {
            '1': lambda: run_scraper() or True,
            '2': lambda: StockNumberComparator().run_interactive() or True,
            '3': lambda: StockNumberComparator().run_simple() or True,
            '4': lambda: StockNumberComparator().compare_excel_with_json() or True,
            '5': lambda: StockNumberComparator().compare_json_files() or True,
            '6': lambda: update_cookie() or True,
        }
        
        if choice == '0':
            print('程序已退出')
            break
        elif choice in actions:
            actions[choice]()
        else:
            print('无效的选项')
            input('按回车键继续...')


def run_scraper():
    try:
        scraper = WegoScraper()
        asyncio.run(scraper.run())
    except Exception as e:
        print(f'运行爬虫时出错: {e}')
        import traceback
        traceback.print_exc()
        input('按回车键继续...')


def update_cookie():
    while True:
        print('='*60)
        print('Cookie更新工具')
        print('='*60)
        print('请选择方式：')
        print('1. 自动获取（推荐）- 程序启动浏览器，登录后自动保存')
        print('2. 手动粘贴 - 从浏览器复制Cookie字符串')
        print('0. 返回')
        print('='*60)
        
        try:
            choice = input('请输入选项 (0-2): ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n已取消')
            return
        
        if choice == '1':
            auto_get_cookie()
        elif choice == '2':
            manual_update_cookie()
        elif choice == '0':
            return
        else:
            print('无效的选项')
            input('按回车键继续...')


def auto_get_cookie():
    print('='*60)
    print('自动获取Cookie')
    print('='*60)
    print('请稍候，浏览器即将打开...')
    print('='*60)
    
    async def get_cookie():
        try:
            async with async_playwright() as p:
                system = WegoScraper.get_system_info()
                browser_args = ['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled', '--disable-dev-shm-usage']
                
                chrome_path = None
                if system == 'Windows':
                    browser_args.append('--disable-gpu')
                    if os.path.exists(r'C:\Program Files\Google\Chrome\Application\chrome.exe'):
                        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                elif system == 'Linux':
                    browser_args.extend(['--disable-gpu', '--disable-dev-shm-usage'])
                    if os.path.exists('/usr/bin/google-chrome'):
                        chrome_path = '/usr/bin/google-chrome'
                elif system == 'Mac':
                    if os.path.exists('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'):
                        chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                
                print(f'检测到系统: {system}')
                if chrome_path:
                    print(f'使用系统Chrome: {chrome_path}')
                else:
                    print(f'使用Playwright内置Chromium')
                
                browser = await p.chromium.launch(headless=False, args=browser_args, executable_path=chrome_path)
                context = await browser.new_context()
                
                cookie_file = 'config/cookies.json'
                if FileManager.file_exists(cookie_file):
                    existing_cookies = FileManager.read_json(cookie_file)
                    if existing_cookies:
                        print(f'已加载 {len(existing_cookies)} 个现有Cookie')
                        await context.add_cookies(existing_cookies)
                
                page = await context.new_page()
                await page.goto('https://www.szwego.com/')
                
                print('='*60)
                print('浏览器已打开')
                print('请在浏览器中完成以下操作：')
                print('1. 如果需要登录，请完成登录')
                print('2. 登录后刷新一下页面')
                print('3. 确认登录成功后，关闭浏览器窗口')
                print('='*60)
                print('等待关闭浏览器...')
                print('='*60)
                
                try:
                    await page.wait_for_event('close', timeout=120000)
                except Exception as e:
                    pass
                
                if browser.is_connected():
                    cookies = await context.cookies()
                    FileManager.write_json(cookie_file, cookies)
                    print(f'✓ Cookie已保存到 {cookie_file}')
                    print(f'✓ 共保存 {len(cookies)} 个Cookie')
                    
                    try:
                        await browser.close()
                    except Exception as e:
                        pass
                else:
                    print('浏览器已关闭')
                    
        except Exception as e:
            print(f'✗ 获取失败: {e}')
            import traceback
            traceback.print_exc()
    
    asyncio.run(get_cookie())


def manual_update_cookie():
    print('='*60)
    print('手动更新Cookie')
    print('='*60)
    print('步骤：')
    print('1. 打开浏览器，访问 Szwego 网站并登录')
    print('2. 按 F12 打开开发者工具')
    print('3. 切换到 Application（应用）标签')
    print('4. 展开左侧 Cookies > https://www.szwego.com')
    print('5. 复制 cookie 的 name 和 value 值')
    print('')
    print('请在下方粘贴完整的 cookie 字符串（格式：key1=value1; key2=value2）')
    print('或者直接按回车退出')
    print('='*60)
    
    try:
        cookie_str = input('请输入Cookie: ').strip()
        if not cookie_str:
            print('已取消')
            return
        
        cookies = parse_cookie_string(cookie_str)
        
        if cookies:
            config_manager = ConfigManager()
            cookie_file = config_manager.get_cookie_file()
            
            FileManager.write_json(cookie_file, cookies)
            print(f'✓ Cookie已保存到 {cookie_file}')
            print(f'✓ 共保存 {len(cookies)} 个Cookie')
        else:
            print('✗ Cookie解析失败，请检查格式')
            
    except Exception as e:
        print(f'✗ 更新失败: {e}')


def parse_cookie_string(cookie_str):
    import urllib.parse
    
    cookies = []
    
    for item in cookie_str.split(';'):
        item = item.strip()
        if '=' in item:
            key, value = item.split('=', 1)
            cookies.append({
                'name': key.strip(),
                'value': value.strip(),
                'domain': '.szwego.com',
                'path': '/'
            })
    
    return cookies


if __name__ == '__main__':
    main()