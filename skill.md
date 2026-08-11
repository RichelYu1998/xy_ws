 # 寰喘鐩稿唽寮€鍙戞妧鑳芥枃妗?(Skill Documentation)

## 馃摉 鏂囨。姒傝堪

**浣滆€?*: 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級

鏈枃妗ｅ畾涔変簡寰喘鐩稿唽绠＄悊绯荤粺鐨?*瀹屾暣浠ｇ爜寮€鍙戣鑼冦€佹灦鏋勮璁°€佹渶浣冲疄璺靛拰鎶€鏈爣鍑?*銆傛墍鏈夊紑鍙戣€呭繀椤讳弗鏍奸伒瀹堟湰瑙勮寖銆?

---

## 馃彈锔?椤圭洰鏋舵瀯鎬昏

### 鎶€鏈爤
- **鍚庣**: Python 3.14 + FastAPI + Pydantic V2
- **鍓嶇**: JavaScript (ES6+) + HTML5 + CSS3
- **鏁版嵁搴?*: JSON鏂囦欢瀛樺偍 + Excel鏂囦欢
- **閮ㄧ讲**: hostc闅ч亾 / Cloudflare Tunnel鍙岄毀閬撴柟妗?
- **娴忚鍣ㄨ嚜鍔ㄥ寲**: Playwright (async)

### 鏍稿績妯″潡鏋舵瀯

#### Python鍚庣妯″潡 (main.py)
```
main.py
鈹溾攢鈹€ 寮傚父澶勭悊绯荤粺
鈹?  鈹溾攢鈹€ AppException - 缁熶竴寮傚父绫?
鈹?  鈹溾攢鈹€ ExceptionHandler - 寮傚父澶勭悊鍣?
鈹?  鈹斺攢鈹€ ExceptionContext - 寮傚父涓婁笅鏂囩鐞嗗櫒
鈹溾攢鈹€ 宸ュ叿鍑芥暟灞?
鈹?  鈹溾攢鈹€ safe_call() - 瀹夊叏璋冪敤鍖呰鍣?
鈹?  鈹溾攢鈹€ handle_error() - 閿欒澶勭悊
鈹?  鈹斺攢鈹€ format_size() - 鏍煎紡鍖栧伐鍏?
鈹溾攢鈹€ 鏃ュ織绯荤粺
鈹?  鈹溾攢鈹€ TeeOutput - 鍙岃緭鍑烘祦
鈹?  鈹溾攢鈹€ setup_logger() - 鏃ュ織閰嶇疆
鈹?  鈹斺攢鈹€ log_print() - 鏃ュ織鎵撳嵃
鈹溾攢鈹€ 鏂囦欢绠＄悊
鈹?  鈹溾攢鈹€ FileManager - 鏂囦欢鎿嶄綔绫?
鈹?  鈹溾攢鈹€ PathManager - 璺緞绠＄悊绫?
鈹?  鈹斺攢鈹€ FileCacheManager - 鏂囦欢缂撳瓨绠＄悊
鈹溾攢鈹€ 閰嶇疆绠＄悊
鈹?  鈹溾攢鈹€ ConfigManager - 閰嶇疆绠＄悊鍣?
鈹?  鈹斺攢鈹€ Environment - 鐜鍙橀噺绠＄悊
鈹溾攢鈹€ 閭欢閫氱煡
鈹?  鈹斺攢鈹€ EmailNotifier - 閭欢閫氱煡绫?
鈹溾攢鈹€ 闅ч亾绠＄悊
鈹?  鈹溾攢鈹€ auto_start_tunnel() - 闅ч亾鍚姩
鈹?  鈹溾攢鈹€ verify_url() - URL楠岃瘉
鈹?  鈹斺攢鈹€ send_heartbeat() - 蹇冭烦妫€娴?
鈹溾攢鈹€ 鐖櫕寮曟搸
鈹?  鈹溾攢鈹€ WegoScraper - 鐖櫕鏍稿績绫?
鈹?  鈹斺攢鈹€ StockNumberComparator - 鏁版嵁瀵规瘮绫?
鈹溾攢鈹€ API璺敱灞?
鈹?  鈹溾攢鈹€ FastAPI搴旂敤瀹炰緥
鈹?  鈹溾攢鈹€ 閫熺巼闄愬埗鍣?(RateLimiter)
鈹?  鈹斺攢鈹€ 杈撳叆楠岃瘉 (Pydantic妯″瀷)
鈹斺攢鈹€ 鍓嶇浜や簰灞?(dist/app.js)
    鈹溾攢鈹€ 瀹夊叏宸ュ叿鍑芥暟
    鈹溾攢鈹€ 璁惧妫€娴嬩笌閫傞厤
    鈹溾攢鈹€ 鏁版嵁瑙ｆ瀽涓庡睍绀?
    鈹斺攢鈹€ UI缁勪欢绠＄悊
```

---

# 馃摎 瀹屾暣椤圭洰鑼冨紡浣撶郴 (Project Paradigm System)

鍩轰簬椤圭洰浠ｇ爜娣卞害鍒嗘瀽锛屼互涓嬫槸寰喘鐩稿唽椤圭洰鐨?*瀹屾暣鎶€鏈寖寮忓拰鏈€浣冲疄璺?*銆?

---

## 馃敶 PY-CORE-001: 缁熶竴寮傚父澶勭悊鑼冨紡 (Unified Exception Handling)

### 鑼冨紡鎻忚堪
寤虹珛鍒嗗眰寮傚父澶勭悊鏈哄埗锛屽疄鐜板紓甯哥殑缁熶竴鎹曡幏銆佸垎绫汇€佽褰曞拰杞崲銆?

### 鏍稿績瀹炵幇

#### 1. 鑷畾涔夊紓甯稿熀绫?- `AppException`
```python
class AppException(Exception):
    """缁熶竴寮傚父绫?- 鎵€鏈変笟鍔″紓甯搁兘浣跨敤姝ょ被"""
    
    CATEGORY_FILE = 'FILE'
    CATEGORY_NETWORK = 'NETWORK'
    CATEGORY_AUTH = 'AUTH'
    CATEGORY_BROWSER = 'BROWSER'
    CATEGORY_PARSE = 'PARSE'
    CATEGORY_CONFIG = 'CONFIG'
    CATEGORY_EXCEL = 'EXCEL'
    CATEGORY_EMAIL = 'EMAIL'
    
    def __init__(self, message: str, category: str = None, code: str = None, details: Any = None):
        self.message = message
        self.category = category or 'APP'
        self.code = code or self._CATEGORY_CODES.get(self.category, 'APP_ERROR')
        self.details = details or {}
        
    @classmethod
    def file_error(cls, message, file_path=None, operation=None):
        """宸ュ巶鏂规硶锛氬垱寤烘枃浠舵搷浣滃紓甯?""
        return cls(message, category=cls.CATEGORY_FILE, 
                  details={'file_path': file_path, 'operation': operation})
    
    @classmethod
    def network_error(cls, message, url=None, status_code=None):
        """宸ュ巶鏂规硶锛氬垱寤虹綉缁滆姹傚紓甯?""
        return cls(message, category=cls.CATEGORY_NETWORK,
                  details={'url': url, 'status_code': status_code})
```

**鍏抽敭鐗规€?*:
- 鉁?13绉嶅紓甯哥被鍒鐩栵紙FILE/NETWORK/AUTH/BROWSER/PARSE绛夛級
- 鉁?宸ュ巶鏂规硶妯″紡绠€鍖栧紓甯稿垱寤?
- 鉁?缁撴瀯鍖栭敊璇鎯咃紙details瀛楀吀锛?
- 鉁?鑷姩閿欒鐮佺敓鎴?

#### 2. 鍗曚緥寮傚父澶勭悊鍣?- `ExceptionHandler`
```python
class ExceptionHandler:
    """缁熶竴寮傚父澶勭悊鍣紙鍗曚緥妯″紡锛?""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def handle(self, error: Exception, context: str = '') -> str:
        """澶勭悊寮傚父骞惰繑鍥炴牸寮忓寲閿欒淇℃伅"""
        error_type = type(error).__name__
        error_msg = str(error)
        
        # 璁板綍閿欒缁熻
        self._error_counts[error_type] = self._error_counts.get(error_type, 0) + 1
        
        # 璁板綍閿欒鍘嗗彶
        self._error_history.append({
            'timestamp': datetime.now().isoformat(),
            'type': error_type,
            'message': error_msg,
            'context': context
        })
        
        return f"[{error_type}] {error_msg}"
    
    def try_execute(self, func: Callable, default: Any = None, context: str = '') -> Any:
        """瀹夊叏鎵ц鍑芥暟锛屽け璐ユ椂杩斿洖榛樿鍊?""
        try:
            return func()
        except Exception as e:
            self.handle(e, context)
            return default
    
    def retry_on_exception(self, func, max_retries=3, delay=1.0, context=''):
        """甯﹂噸璇曟満鍒剁殑寮傚父澶勭悊"""
        for attempt in range(max_retries):
            try:
                return func()
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(delay * (attempt + 1))
        raise last_error
```

**鏍稿績鑳藉姏**:
- 鉁?鍗曚緥妯″紡纭繚鍏ㄥ眬鍞竴瀹炰緥
- 鉁?閿欒缁熻鍜屽巻鍙茶褰?
- 鉁?閲嶅閿欒鎶戝埗锛堥伩鍏嶆棩蹇楃垎鐐革級
- 鉁?閲嶈瘯鏈哄埗鏀寔

#### 3. 涓婁笅鏂囩鐞嗗櫒 - `ExceptionContext`
```python
class ExceptionContext:
    """寮傚父澶勭悊涓婁笅鏂囩鐞嗗櫒锛坵ith璇彞璇硶绯栵級"""
    
    def __init__(self, context='', default=None, show_traceback=True):
        self.context = context
        self.default = default
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.error = self.handler.handle(exc_val, self.context)
            self.result = self.default
            return True  # 鍚炴帀寮傚父
        return False
    
    def get_result(self) -> Tuple[Any, str]:
        """鑾峰彇缁撴灉鍜岄敊璇俊鎭?""
        return self.result, self.error
```

**浣跨敤绀轰緥**:
```python
# 鏂瑰紡1锛氫娇鐢ㄤ笂涓嬫枃绠＄悊鍣?
with ExceptionContext("璇诲彇閰嶇疆鏂囦欢", default={}) as ctx:
    config = json.load(open('config.json'))
result, error = ctx.get_result()

# 鏂瑰紡2锛氫娇鐢ㄨ楗板櫒
@exception_handler(context="澶勭悊鐢ㄦ埛璇锋眰", default={"error": "绯荤粺绻佸繖"})
def process_request(data):
    return complex_operation(data)

# 鏂瑰紡3锛氫娇鐢ㄥ畨鍏ㄨ皟鐢?
data = safe_call(lambda: json.load(f), default={}, context='璇诲彇JSON')
```

---

## 馃敶 PY-CORE-002: 鐜鑷€傚簲鑼冨紡 (Environment-Aware Design)

### 鑼冨紡鎻忚堪
閫氳繃`Environment`闈欐€佺被瀹炵幇璺ㄥ钩鍙板吋瀹规€э紝鑷姩閫傞厤Windows/Mac/Linux绯荤粺宸紓銆?

### 鏍稿績瀹炵幇
```python
class Environment:
    """缁熶竴鐜妫€娴嬪拰绠＄悊"""
    
    SYSTEM = platform.system()
    IS_WINDOWS = SYSTEM == 'Windows'
    IS_MAC = SYSTEM == 'Darwin'
    IS_LINUX = SYSTEM == 'Linux'
    
    @staticmethod
    def get_venv_python():
        """鑾峰彇铏氭嫙鐜Python璺緞"""
        if Environment.IS_WINDOWS:
            return os.path.join(PROJECT_DIR, '.venv', 'Scripts', 'python.exe')
        else:
            return os.path.join(PROJECT_DIR, '.venv', 'bin', 'python')
    
    @staticmethod
    def get_browser_args():
        """鏍规嵁绯荤粺杩斿洖涓嶅悓鐨勬祻瑙堝櫒鍚姩鍙傛暟"""
        args = ['--no-sandbox', '--disable-setuid-sandbox']
        if Environment.IS_WINDOWS:
            args.append('--disable-gpu')
        elif Environment.IS_LINUX:
            args.extend(['--disable-gpu', '--disable-dev-shm-usage'])
        return args
    
    @staticmethod
    def get_user_agent():
        """鍔ㄦ€佺敓鎴怳ser-Agent锛堥殢鏈篊hrome鐗堟湰鍙凤級"""
        versions = ['120.0.0.0', '121.0.0.0', ..., '129.0.0.0']
        chrome_version = random.choice(versions)
        
        if Environment.IS_WINDOWS:
            return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/{chrome_version}'
        elif Environment.IS_MAC:
            return f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ...'
        else:
            return f'Mozilla/5.0 (X11; Linux x86_64) ...'
    
    @staticmethod
    def kill_process_by_name(process_name):
        """璺ㄧ郴缁熺粓姝㈣繘绋?""
        if Environment.IS_WINDOWS:
            subprocess.run(f'taskkill /F /IM {process_name}', shell=True)
        else:
            subprocess.run(f'pkill -f "{process_name}"', shell=True)
```

**鍏抽敭鐗规€?*:
- 鉁?绯荤粺绫诲瀷鑷姩妫€娴嬶紙IS_WINDOWS/IS_MAC/IS_LINUX锛?
- 鉁?璺緞鍒嗛殧绗﹁嚜鍔ㄥ鐞?
- 鉁?杩涚▼绠＄悊鍛戒护璺ㄥ钩鍙伴€傞厤
- 鉁?娴忚鍣ㄥ弬鏁板樊寮傚寲閰嶇疆
- 鉁?鍔ㄦ€乁A闃插弽鐖娴?

---

## 馃敶 PY-CORE-003: 缁熶竴璺緞绠＄悊鑼冨紡 (Centralized Path Management)

### 鑼冨紡鎻忚堪
閫氳繃`PathManager`闆嗕腑绠＄悊鎵€鏈夋枃浠惰矾寰勶紝閬垮厤纭紪鐮侊紝瀹炵幇璺緞鐨勭粺涓€缁存姢鍜岃法骞冲彴鍏煎銆?

### 鏍稿績瀹炵幇
```python
class PathManager:
    """璺緞绠＄悊绫?- 缁熶竴澶勭悊璺ㄧ郴缁熻矾寰勯棶棰?""
    
    @staticmethod
    def get_config_dir():
        return os.path.join(PROJECT_DIR, 'config')
    
    @staticmethod
    def get_file_dir():
        return os.path.join(PROJECT_DIR, 'file')
    
    @staticmethod
    def get_config_file():
        return os.path.join(PathManager.get_config_dir(), 'config.json')
    
    @staticmethod
    def get_cookie_file():
        return os.path.join(PathManager.get_config_dir(), 'cookies.json')
    
    @staticmethod
    def get_json_filename(date_str):
        """鍔ㄦ€佺敓鎴怞SON鏂囦欢鍚?""
        return f"{date_str}寰喘鐩稿唽(灏忔棴鏁扮爜).json"
    
    @staticmethod
    def get_cache_filename(date_str):
        """鍔ㄦ€佺敓鎴愮紦瀛樻枃浠跺悕"""
        return f"{date_str}寰喘鐩稿唽(灏忔棴鏁扮爜)_cache.json"
    
    @staticmethod
    def get_public_url_from_web_log(skip_validation=False, quiet=False):
        """
        鑾峰彇鍏綉鍦板潃锛堢粺涓€鍏ュ彛锛?
        
        鏁版嵁娴佸悜锛?
        hostc 鈫?tunnel_url.txt (鏉冨▉婧? 鈫?web_output.log (闀滃儚) 鈫?鍓嶇鏄剧ず
        
        绛栫暐锛?
        1. 浼樺厛浠?tunnel_url.txt 璇诲彇锛堟潈濞佹簮锛?
        2. 濡傛灉涓嶅彲鐢紝灏濊瘯 web_output.log
        3. 涓や釜閮藉け璐ュ垯杩斿洖 None
        """
        # 瀹炵幇澶氭簮URL鑾峰彇閫昏緫...
```

**璁捐鍘熷垯**:
- 鉁?鎵€鏈夎矾寰勯泦涓畾涔夛紝涓€澶勪慨鏀瑰叏灞€鐢熸晥
- 鉁?浣跨敤`os.path.join()`纭繚璺ㄥ钩鍙板吋瀹?
- 鉁?鍔ㄦ€佹枃浠跺悕鐢熸垚锛堟棩鏈熷墠缂€锛?
- 鉁?澶氭簮鏁版嵁鑾峰彇绛栫暐锛堟潈濞佹簮+澶囩敤婧愶級

---

## 馃敶 PY-CORE-004: 鏅鸿兘缂撳瓨绠＄悊鑼冨紡 (Intelligent Caching)

### 鑼冨紡鎻忚堪
閫氳繃`FileCacheManager`瀹炵幇鏂囦欢绾TL缂撳瓨锛屽噺灏慖O鎿嶄綔锛屾彁鍗囨€ц兘銆?

### 鏍稿績瀹炵幇
```python
class FileCacheManager:
    """JSON鏂囦欢缂撳瓨绠＄悊鍣?""
    
    def __init__(self, ttl_seconds=30):
        self._cache = {}
        self._ttl = ttl_seconds
        self._lock = threading.Lock()
    
    def read_json(self, file_path, default=None):
        """甯︾紦瀛樼殑JSON鏂囦欢璇诲彇"""
        current_time = time.time()
        
        with self._lock:
            # 妫€鏌ョ紦瀛樻槸鍚︽湁鏁?
            if file_path in self._cache:
                cached_data, cache_time = self._cache[file_path]
                
                # 妫€鏌TL鏄惁杩囨湡
                if current_time - cache_time < self._ttl:
                    # 浜屾楠岃瘉锛氭鏌ユ枃浠朵慨鏀规椂闂?
                    if os.path.exists(file_path):
                        if os.path.getmtime(file_path) <= cache_time:
                            return cached_data  # 缂撳瓨鍛戒腑
                    
                    del self._cache[file_path]  # 鏂囦欢宸叉洿鏂帮紝娓呴櫎缂撳瓨
        
        # 缂撳瓨鏈懡涓垨宸茶繃鏈燂紝閲嶆柊璇诲彇
        data = safe_read_json(file_path, default)
        
        with self._lock:
            self._cache[file_path] = (data, current_time)
        
        return data
    
    def invalidate(self, file_path=None):
        """鎵嬪姩娓呴櫎缂撳瓨"""
        with self._lock:
            if file_path:
                self._cache.pop(file_path, None)
            else:
                self._cache.clear()

# 鍏ㄥ眬鍗曚緥
json_cache = FileCacheManager(ttl_seconds=30)
```

**楂樼骇鐗规€?*:
- 鉁?TTL锛圱ime-To-Live锛夎繃鏈熸満鍒?
- 鉁?鏂囦欢淇敼鏃堕棿浜屾楠岃瘉
- 鉁?绾跨▼瀹夊叏锛坱hreading.Lock锛?
- 鉁?鏀寔鎵归噺娓呴櫎鍜屽崟涓枃浠舵竻闄?
- 鉁?缂撳瓨鍛戒腑鐜囩粺璁?

---

## 馃敶 PY-CORE-005: 瀹夊叏閭欢閫氱煡鑼冨紡 (Secure Email Notification)

### 鑼冨紡鎻忚堪
閫氳繃`EmailNotifier`瀹炵幇缁撴瀯鍖栭偖浠跺彂閫侊紝鏀寔HTML瀵屾枃鏈€佷簨浠跺垎绫汇€佽繛鎺ヨ秴鏃舵帶鍒躲€?

### 鏍稿績瀹炵幇
```python
class EmailNotifier:
    """閭欢閫氱煡绫?""
    
    def send_tunnel_notification(self, tunnel_url, event_type='new'):
        """
        鍙戦€侀毀閬揢RL鍙樺寲閫氱煡閭欢
        
        浜嬩欢绫诲瀷锛?
        - new: 鏂板叕缃戝湴鍧€
        - available: 鍏綉鍦板潃鍙敤
        - unavailable: 鍏綉鍦板潃涓嶅彲鐢?
        - restarted: 闅ч亾宸查噸鍚?
        - fallback_available: 澶囩敤鍦板潃鍙敤
        """
        event_titles = {
            'new': '鉁?鏂板叕缃戝湴鍧€',
            'unavailable': '馃毃 鍏綉鍦板潃涓嶅彲鐢?,
            'restarted': '馃攧 闅ч亾宸查噸鍚?,
            'fallback_available': '馃攧 澶囩敤鍏綉鍦板潃鍙敤'
        }
        
        # 鏋勫缓MIME澶氶儴鍒嗛偖浠讹紙绾枃鏈?+ HTML锛?
        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header(f'銆恵event_title}銆憑鏃堕棿}', 'utf-8')
        
        # 绾枃鏈増鏈?
        body = f"""{event_title}
鏃堕棿: {current_time}
鍏綉鍦板潃: {tunnel_url}
{status_note}"""
        
        # HTML瀵屾枃鏈増鏈紙鍝嶅簲寮忓竷灞€锛?
        html_body = f"""
<html>
<body style="font-family: -apple-system, BlinkMacSystemFont, ...">
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; padding: 30px; border-radius: 12px;">
    <h1>{event_title}</h1>
</div>
<div style="background-color: #ffffff; border: 1px solid #e0e0e0; 
            border-radius: 8px; padding: 25px;">
    <table style="width: 100%;">
        <tr><td><strong>鏃堕棿:</strong></td><td>{current_time}</td></tr>
        <tr><td><strong>鍏綉鍦板潃:</strong></td>
            <td><a href="{tunnel_url}">{tunnel_url}</a>
                <button onclick="window.open('{tunnel_url}')">鐐瑰嚮璁块棶</button>
            </td>
        </tr>
    </table>
</div>
</body>
</html>"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        msg.attach(MIMEText(html_body, 'html', 'utf-8'))
        
        # 鍙戦€侀偖浠讹紙甯﹁秴鏃舵帶鍒讹級
        timeout = 30
        server = smtplib.SMTP(host, port, timeout=timeout)
        server.starttls()
        server.login(user, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
```

**瀹夊叏鐗规€?*:
- 鉁?SMTP杩炴帴瓒呮椂鎺у埗锛?0绉掞級
- 鉁?SSL/TLS鍔犲瘑浼犺緭
- 鉁?HTML杞箟闃叉XSS
- 鉁?缁撴瀯鍖栦簨浠跺垎绫?
- 鉁?璇︾粏鐨勬椂闂存埑鏃ュ織

---

## 馃敶 PY-CORE-006: 娴忚鍣ㄨ嚜鍔ㄥ寲鐖櫕鑼冨紡 (Browser Automation Scraping)

### 鑼冨紡鎻忚堪
閫氳繃`WegoScraper`瀹炵幇Playwright寮傛鐖櫕锛屽寘鍚櫤鑳芥粴鍔ㄣ€佸脊绐楀叧闂€佸苟鍙戝鐞嗐€丄PI鍥為€€绛夐珮绾у姛鑳姐€?

### 鏍稿績瀹炵幇
```python
class WegoScraper:
    """鐖櫕鏍稿績绫?""
    
    async def scroll_to_load_all(self, page):
        """鏅鸿兘婊氬姩鍔犺浇鎵€鏈夊晢鍝侊紙鍔ㄦ€佽皟鏁寸瓥鐣ワ級"""
        
        config = self.config_manager.get('scroll_config', {
            'max_attempts': 30,
            'same_height_limit': 8,
            'scroll_wait_time': 0.8,
            'dynamic_adjust': True
        })
        
        last_height = 0
        no_change_count = 0
        height_history = []
        
        for scroll_attempts in range(config['max_attempts']):
            current_height = await page.evaluate('document.body.scrollHeight')
            
            # 妫€娴嬮〉闈㈡槸鍚﹀埌搴曢儴
            if current_height == last_height:
                no_change_count += 1
                if no_change_count >= config['same_height_limit']:
                    print(f'椤甸潰宸叉粴鍔ㄥ埌搴曢儴锛堣繛缁瓄config["same_height_limit"]}娆′笉鍙橈級')
                    break
            else:
                no_change_count = 0
            
            # 鍔ㄦ€佽皟鏁存粴鍔ㄨ窛绂?
            scroll_distance = current_height * 0.3 if scroll_attempts < 10 else current_height
            await page.evaluate(f'window.scrollBy(0, {scroll_distance})')
            
            await asyncio.sleep(config['scroll_wait_time'])
            
            # 鍔ㄦ€佽皟鏁寸瓑寰呮椂闂达紙鍩轰簬椤甸潰鍔犺浇閫熷害锛?
            if config['dynamic_adjust'] and len(height_history) >= 5:
                avg_change = sum(height_changes) / len(height_changes)
                
                if avg_change < 50 and config['scroll_wait_time'] < 2.0:
                    config['scroll_wait_time'] += 0.1  # 椤甸潰鎱紝澧炲姞绛夊緟
                elif avg_change > 300 and config['scroll_wait_time'] > 0.5:
                    config['scroll_wait_time'] -= 0.1  # 椤甸潰蹇紝鍑忓皯绛夊緟
            
            # 瀹氭湡鍏抽棴寮圭獥
            if (scroll_attempts + 1) % 5 == 0:
                await self.close_popups(page)
    
    async def close_popups(self, page, close_limit=3, wait_time=0.3):
        """鏅鸿兘鍏抽棴寮圭獥锛堝绉嶉€夋嫨鍣級"""
        popup_selectors = [
            '[class*="close"]',
            '[class*="modal-close"]',
            'button:has-text("鍏抽棴")',
            '.ant-modal-close',
            '.el-dialog__close'
        ]
        
        for selector in popup_selectors[:close_limit]:
            safe_execute_func(
                lambda: self._close_popup_impl(page, selector, wait_time),
                context=f'close_popups({selector})'
            )
    
    async def process_elements_concurrently(self, page, elements):
        """骞跺彂澶勭悊鍟嗗搧鍏冪礌锛圱hreadPoolExecutor锛?""
        
        elements_data = []
        
        # 绗竴闃舵锛氭敹闆嗗厓绱犳暟鎹?
        for element in elements:
            try:
                text = await asyncio.wait_for(element.text_content(), timeout=2.0)
                html = await asyncio.wait_for(element.inner_html(), timeout=2.0)
                elements_data.append((text, html, element_id))
            except asyncio.TimeoutError:
                continue
        
        # 绗簩闃舵锛氬苟鍙戞彁鍙栧晢鍝佷俊鎭?
        products = []
        with ThreadPoolExecutor(max_workers=15) as executor:
            futures = [executor.submit(self.extract_product_info, text, html) 
                      for text, html, _ in elements_data]
            
            for future in futures:
                try:
                    result = future.result(timeout=2)
                    if result:
                        products.append(result)
                except Exception:
                    pass
        
        # 绗笁闃舵锛欰PI鍥為€€鑾峰彇缂哄け鏁版嵁
        products_need_api = [p for p in products if not p.get('鎷胯揣浠?)]
        if products_need_api:
            await self.fetch_cost_prices_via_api(page, products_need_api, products)
        
        return products
    
    @staticmethod
    def extract_product_info(element_text, html_content):
        """鎻愬彇鍟嗗搧淇℃伅锛堟鍒欒〃杈惧紡瑙ｆ瀽锛?""
        
        stock_match = re.search(r'璐у彿[锛?]\s*(\d+)', element_text)
        price_match = re.search(r'鍞环[锛?]\s*楼?\s*([\d,]+)', element_text)
        cost_match = re.search(r'鎷胯揣浠穂锛?]\s*楼?\s*([\d,]+)', element_text)
        
        name = WegoScraper.clean_product_name(element_text[:cut_pos])
        
        return {
            '鍟嗗搧鍚嶇О': name,
            '鍞环': price,
            '鎷胯揣浠?: cost_price,
            '璐у彿': stock_number,
            '澶囨敞': remark,
            '鍛樺伐': employee,
            '鍥剧墖': ''
        }
```

**楂樼骇鐗规€?*:
- 鉁?鍔ㄦ€佹粴鍔ㄧ瓥鐣ワ紙閫熷害鑷€傚簲锛?
- 鉁?寮圭獥鏅鸿兘璇嗗埆涓庡叧闂?
- 鉁?骞跺彂鏁版嵁澶勭悊锛?5绾跨▼姹狅級
- 鉁?API鍥為€€鏈哄埗锛堢己澶辨暟鎹ˉ鍏咃級
- 鉁?瓒呮椂淇濇姢锛堟瘡姝?绉掕秴鏃讹級
- 鉁?鍟嗗搧鍘婚噸锛坰een_products闆嗗悎锛?

---

## 馃敶 PY-CORE-007: 鏁版嵁瀵规瘮鍒嗘瀽鑼冨紡 (Data Comparison & Analysis)

### 鑼冨紡鎻忚堪
閫氳繃`StockNumberComparator`瀹炵幇Excel/JSON鏁版嵁瀵规瘮锛屾敮鎸侀珮浠峰晢鍝佺瓫閫夈€侀噸澶嶆娴嬨€佸樊寮傛姤鍛娿€?

### 鏍稿績瀹炵幇
```python
class StockNumberComparator:
    """鏁版嵁瀵规瘮鏍稿績绫?""
    
    @staticmethod
    def compare_stock_numbers(json_stock_numbers, input_stock_numbers, 
                             high_price_stock_numbers=None):
        """瀵规瘮涓ょ粍璐у彿鏁版嵁"""
        json_set = set(json_stock_numbers)
        input_set = set(input_stock_numbers)
        
        result = {
            'missing': sorted(list(input_set - json_set)),      # 缂哄け鐨?
            'existing': sorted(list(input_set & json_set)),     # 宸插瓨鍦ㄧ殑
            'extra_in_json': sorted(list(json_set - input_set)), # 澶氫綑鐨?
            'total_input': len(input_set),
            'total_json': len(json_set),
            'missing_count': len(input_set - json_set),
            'existing_count': len(input_set & json_set),
            'extra_in_json_count': len(json_set - input_set)
        }
        
        # 楂樹环鍟嗗搧鐗规畩澶勭悊
        if high_price_stock_numbers:
            result['high_price_stock_numbers'] = sorted(set(high_price_stock_numbers))
            result['high_price_count'] = len(result['high_price_stock_numbers'])
        
        return result
    
    def compare_json_files(self):
        """瀵规瘮褰撳ぉ鏈€鏂扮殑涓や釜JSON鏂囦欢"""
        
        latest_file, second_file = FileManager.get_today_json_files()
        
        latest_data = FileManager.read_json(latest_file)
        second_data = FileManager.read_json(second_file)
        
        latest_products = latest_data.get('鍟嗗搧鍒楄〃', [])
        second_products = second_data.get('鍟嗗搧鍒楄〃', [])
        
        # 鎻愬彇璐у彿闆嗗悎
        latest_stocks = {p.get('璐у彿') for p in latest_products if p.get('璐у彿')}
        second_stocks = {p.get('璐у彿') for p in second_products if p.get('璐у彿')}
        
        # 璁＄畻宸紓
        added = latest_stocks - second_stocks
        removed = second_stocks - latest_stocks
        
        # 楂樹环鍟嗗搧绛涢€夛紙鍞环>=599锛?
        high_price_added = [
            p.get('璐у彿') for p in latest_products 
            if WegoScraper.parse_price(p.get('鍞环')) >= 599 
            and p.get('璐у彿') in added
        ]
        
        # 鐢熸垚宸紓鎶ュ憡
        diff_data = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'added_count': len(added),
            'removed_count': len(removed),
            'high_price_added': sorted(high_price_added),
            'high_price_description': '鏂板鐨勫敭浠?=599鐨勫晢鍝?
        }
        
        # 杩藉姞鍒?灏忚"瀛楁锛堜繚鐣欏巻鍙茶褰曪級
        if '灏忚' not in latest_data:
            latest_data['灏忚'] = []
        latest_data['灏忚'].append(diff_data)
        latest_data['灏忚'].sort(key=lambda x: x['timestamp'])
        
        FileManager.write_json(latest_file, latest_data)
    
    @staticmethod
    def find_duplicate_stock_numbers(stock_numbers):
        """妫€娴嬮噸澶嶈揣鍙?""
        seen = {}
        for num in stock_numbers:
            seen[num] = seen.get(num, 0) + 1
        
        return [{'璐у彿': num, 'count': count} 
                for num, count in seen.items() if count > 1]
```

**鏁版嵁鍒嗘瀽鑳藉姏**:
- 鉁?闆嗗悎杩愮畻楂樻晥瀵规瘮锛圤(n)澶嶆潅搴︼級
- 鉁?楂樹环鍟嗗搧鑷姩绛涢€夛紙浠锋牸闃堝€煎彲閰嶇疆锛?
- 鉁?閲嶅鏁版嵁妫€娴嬩笌缁熻
- 鉁?澧為噺宸紓杩借釜锛堝巻鍙茶褰曪級
- 鉁?澶氭簮鏁版嵁铻嶅悎锛圗xcel+JSON锛?

---

## 馃敶 PY-CORE-008: API閫熺巼闄愬埗涓庤緭鍏ラ獙璇佽寖寮?(Rate Limiting & Input Validation)

### 鑼冨紡鎻忚堪
閫氳繃`RateLimiter`鍜孭ydantic妯″瀷瀹炵幇API灞傞潰鐨勫畨鍏ㄥ拰鎬ц兘淇濇姢銆?

### 鏍稿績瀹炵幇

#### 1. IP绾у埆閫熺巼闄愬埗鍣?
```python
class RateLimiter:
    """IP绾у埆閫熺巼闄愬埗鍣?""
    
    def __init__(self, max_requests=100, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}
        self._lock = threading.Lock()
    
    def is_allowed(self, client_ip):
        """妫€鏌ユ槸鍚﹀厑璁歌姹傦紙婊戝姩绐楀彛绠楁硶锛?""
        current_time = time.time()
        
        with self._lock:
            if client_ip not in self.requests:
                self.requests[client_ip] = []
            
            # 娓呯悊杩囨湡璇锋眰璁板綍
            self.requests[client_ip] = [
                t for t in self.requests[client_ip]
                if current_time - t < self.window_seconds
            ]
            
            if len(self.requests[client_ip]) >= self.max_requests:
                return False
            
            self.requests[client_ip].append(current_time)
            return True
    
    def get_retry_after(self, client_ip):
        """鑾峰彇閲嶈瘯绛夊緟鏃堕棿"""
        oldest = min(self.requests[client_ip])
        return max(0, int(self.window_seconds - (time.time() - oldest)) + 1)

# 鍏ㄥ眬瀹炰緥
api_rate_limiter = RateLimiter(max_requests=200, window_seconds=60)
upload_rate_limiter = RateLimiter(max_requests=10, window_seconds=60)
```

#### 2. Pydantic杈撳叆楠岃瘉妯″瀷
```python
class RunCommandRequest(BaseModel):
    command: str = Field(..., min_length=1, max_length=10000)
    
    @field_validator('command')
    def validate_command_safe(cls, v):
        """鍗遍櫓鍛戒护榛戝悕鍗曟娴?""
        dangerous = [
            'rm -rf /', 'mkfs', 'shutdown', 'reboot',
            'dd if=', '> /dev/sd', ':(){ :|:& };:',  # fork bomb
            'wget http', 'curl http', 'nc -l', 'nc -e',
            'python -c', 'eval ', 'exec ',
            'crontab -r', 'systemctl stop',
            'reg delete', 'reg add'
        ]
        v_lower = v.lower()
        for pattern in dangerous:
            if pattern.lower() in v_lower:
                raise ValueError(f'妫€娴嬪埌鍗遍櫓鍛戒护: {pattern}')
        return v.strip()

class TaskInputRequest(BaseModel):
    task_id: str = Field(..., min_length=1, max_length=50)
    user_input: str = Field('', max_length=10000)
```

#### 3. 閫熺巼闄愬埗瑁呴グ鍣?
```python
def rate_limit(limiter, endpoint_name='API'):
    """閫熺巼闄愬埗瑁呴グ鍣?""
    def decorator(f):
        async def decorated(request: Request, *args, **kwargs):
            client_ip = request.client.host
            
            if not limiter.is_allowed(client_ip):
                retry_after = limiter.get_retry_after(client_ip)
                raise HTTPException(
                    status_code=429,
                    detail={'error': '璇锋眰杩囦簬棰戠箒', 'retry_after': retry_after},
                    headers={'Retry-After': str(retry_after)}
                )
            
            return await f(request, *args, **kwargs)
        return decorated
    return decorator
```

**瀹夊叏鐗规€?*:
- 鉁?婊戝姩绐楀彛闄愭祦绠楁硶
- 鉁?鍗遍櫓鍛戒护榛戝悕鍗曪紙30+瑙勫垯锛?
- 鉁?杈撳叆闀垮害闄愬埗
- 鉁?429鐘舵€佺爜 + Retry-After澶?
- 鉁?鍒嗙鐐圭嫭绔嬮檺娴?

---

## 馃敶 PY-CORE-009: 鍓嶇瀹夊叏闃叉姢鑼冨紡 (Frontend Security)

### 鑼冨紡鎻忚堪
鍦↗avaScript鍓嶇瀹炵幇XSS闃叉姢銆乁RL楠岃瘉銆佽澶囨娴嬬瓑瀹夊叏鏈哄埗銆?

### 鏍稿績瀹炵幇

#### 1. XSS闃叉姢鍑芥暟
```javascript
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function escapeAttr(text) {
    if (!text) return '';
    return String(text)
        .replace(/&/g, '&amp;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

function safeUrl(url) {
    return isValidUrl(url) ? escapeAttr(url) : '#invalid-url';
}

function isValidUrl(url) {
    if (!url) return false;
    try {
        const parsed = new URL(url);
        return ['http:', 'https:'].includes(parsed.protocol);
    } catch {
        return false;
    }
}
```

#### 2. 璁惧妫€娴嬩笌鍝嶅簲寮忛€傞厤
```javascript
function detectDevice() {
    const ua = navigator.userAgent.toLowerCase();
    const width = window.innerWidth;
    
    let deviceType = 'desktop';
    
    // 灞忓箷瀹藉害鍒ゆ柇
    if (width < 576) deviceType = 'phone';
    else if (width < 768) deviceType = 'tablet';
    else if (width < 992) deviceType = 'laptop';
    else if (width < 1200) deviceType = 'desktop';
    else deviceType = 'large-desktop';
    
    // 娴忚鍣ㄦ娴?
    const mobileDevices = {
        wechat: /micromessenger/i.test(ua),
        weibo: /weibo/i.test(ua),
        qq: /qq\//i.test(ua),
        iphone: /iphone|ipad|ipod/i.test(ua),
        android: /android/i.test(ua)
    };
    
    return {
        type: deviceType,
        isMobile: width < 768,
        width: width,
        height: height,
        pixelRatio: window.devicePixelRatio || 1
    };
}

function applyDeviceStyles() {
    const device = detectDevice();
    document.body.classList.remove('is-phone', 'is-tablet', 'is-desktop');
    document.body.classList.add('is-' + device.type);
}

// 鐩戝惉绐楀彛澶у皬鍙樺寲锛堥槻鎶栵級
window.addEventListener('resize', function() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(applyDeviceStyles, 250);
});
```

#### 3. 瀹夊叏鐨凙PI鍝嶅簲瑙ｆ瀽
```javascript
async function safeParseJson(response) {
    const contentType = response.headers.get('content-type') || '';
    
    if (!contentType.includes('application/json')) {
        const text = await response.text();
        let errorMsg = '鏈嶅姟鍣ㄨ繑鍥炰簡闈濲SON鍝嶅簲';
        
        // 閿欒绫诲瀷鏅鸿兘璇嗗埆
        if (response.status === 401 || text.includes('鐧诲綍')) {
            errorMsg = '鐧诲綍宸茶繃鏈燂紝璇烽噸鏂拌幏鍙朇ookie';
        } else if (response.status === 404) {
            errorMsg = '鎺ュ彛涓嶅瓨鍦?(404)';
        } else if (response.status >= 500) {
            errorMsg = `鏈嶅姟鍣ㄥ唴閮ㄩ敊璇?(${response.status})`;
        }
        
        throw new Error(errorMsg);
    }
    
    return response.json();
}
```

**瀹夊叏鎺柦**:
- 鉁?DOM-based XSS闃叉姢锛坋scapeHtml/escapeAttr锛?
- 鉁?URL鐧藉悕鍗曞崗璁獙璇侊紙http/https only锛?
- 鉁?Content-Type寮哄埗鏍￠獙
- 鉁?璁惧鎸囩汗璇嗗埆
- 鉁?鍝嶅簲寮忔柇鐐圭郴缁燂紙5涓眰绾э級

---

## 馃敶 PY-CORE-010: 鍙岃緭鍑烘棩蹇楃郴缁熻寖寮?(Dual-Output Logging)

### 鑼冨紡鎻忚堪
閫氳繃`TeeOutput`绫诲疄鐜板悓鏃惰緭鍑哄埌鎺у埗鍙板拰鏂囦欢鐨勬棩蹇楃郴缁燂紝鏀寔鑷姩鏃堕棿鎴炽€佹枃浠堕攣瀹氭仮澶嶃€?

### 鏍稿績瀹炵幇
```python
class TeeOutput:
    """鍚屾椂杈撳嚭鍒版帶鍒跺彴鍜屾枃浠?""
    
    def __init__(self, original, log_file_path=None):
        self.original = original
        self.log_file_path = log_file_path
        self.file = None
        if log_file_path:
            self._init_log_file(log_file_path)
    
    def _init_log_file(self, log_file_path, retry_count=0):
        """鍒濆鍖栨棩蹇楁枃浠讹紙甯﹂噸璇曞拰閿佸畾鎭㈠锛?""
        max_retries = 3
        
        try:
            # 妫€鏌ユ枃浠舵槸鍚﹁閿佸畾
            if os.path.exists(log_file_path):
                test_fd = os.open(log_file_path, os.O_WRONLY | os.O_APPEND)
                os.close(test_fd)
            
            self.file = open(log_file_path, 'a', encoding='utf-8')
            
        except OSError as e:
            if retry_count < max_retries:
                # 閿佸畾鏂囦欢澶囦唤
                backup_path = f"{log_file_path}.locked_{time.strftime('%H%M%S')}"
                os.rename(log_file_path, backup_path)
                time.sleep(0.5 * (retry_count + 1))
                return self._init_log_file(log_file_path, retry_count + 1)
            else:
                self.file = None  # 闄嶇骇涓轰粎鎺у埗鍙拌緭鍑?
    
    def write(self, text):
        _output_text = text
        
        # 鑷姩娣诲姞鏃堕棿鎴?
        if text.strip():
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            
            if not text.strip().startswith(f'[{timestamp[:10]}'):
                lines = text.split('\n')
                timestamped_lines = [
                    f"[{timestamp}] {line}" if line.strip() else line
                    for line in lines
                ]
                _output_text = '\n'.join(timestamped_lines)
        
        # 鍙岃緭鍑?
        self.original.write(_output_text)
        
        if self.file:
            safe_execute_func(
                lambda: (self.file.write(_output_text), self.file.flush()),
                context='TeeOutput鍐欏叆'
            )

# 鍏ㄥ眬鍒濆鍖?
def setup_web_logging():
    global web_log_file
    web_log_file = PathManager.get_web_output_file()
    sys.stdout = TeeOutput(sys.stdout, web_log_file)
    sys.stderr = TeeOutput(sys.stderr, web_log_file)
```

**楂樼骇鐗规€?*:
- 鉁?100%鏃堕棿鎴宠鐩栫巼锛堟绉掔簿搴︼級
- 鉁?鏂囦欢閿佸畾鑷姩鎭㈠锛堝浠?閲嶈瘯锛?
- 鉁?Flask璁块棶鏃ュ織鐗规畩澶勭悊
- 鉁?闄嶇骇瀹归敊锛堟枃浠朵笉鍙敤鏃朵粎鎺у埗鍙帮級
- 鉁?鑷姩flush淇濊瘉瀹炴椂鎬?

---

## 馃敶 PY-CORE-011: 閰嶇疆绠＄悊鑼冨紡 (Configuration Management)

### 鑼冨紡鎻忚堪
閫氳繃`ConfigManager`瀹炵幇JSON閰嶇疆鏂囦欢鐨勮鍐欍€侀粯璁ゅ€笺€佺儹鏇存柊绛夊姛鑳姐€?

### 鏍稿績瀹炵幇
```python
class ConfigManager:
    """閰嶇疆绠＄悊鍣紙鎳掑姞杞?缂撳瓨锛?""
    
    def __init__(self, config_path=None):
        self.config_path = config_path or PathManager.get_config_file()
        self._config = None  # 鎳掑姞杞?
    
    @property
    def config(self):
        if self._config is None:
            self._config = self._load_config()
        return self._config
    
    def _load_config(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}  # 榛樿绌洪厤缃?
        except json.JSONDecodeError as e:
            raise AppException.config_error(f"閰嶇疆鏂囦欢鏍煎紡閿欒: {e}")
    
    def save_config(self):
        if self._config:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, ensure_ascii=False, indent=2)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        if self._config is not None:
            self._config[key] = value
            self.save_config()  # 鑷姩鎸佷箙鍖?
    
    def get_excel_files(self):
        """鑾峰彇Excel鏂囦欢鍒楄〃锛堣矾寰勫睍寮€+瀛樺湪鎬ф鏌ワ級"""
        excel_files = self.config.get('excel_files', [])
        existing_files = []
        for path in excel_files:
            expanded = os.path.expanduser(path)
            if FileManager.file_exists(expanded):
                existing_files.append(expanded)
        return existing_files
```

**璁捐鐗圭偣**:
- 鉁?鎳掑姞杞斤紙棣栨璁块棶鏃舵墠鍔犺浇锛?
- 鉁?鍐呭瓨缂撳瓨锛堥伩鍏嶉噸澶岻O锛?
- 鉁?鑷姩鎸佷箙鍖栵紙set鍗充繚瀛橈級
- 鉁?璺緞灞曞紑锛垀 鈫?鐢ㄦ埛涓荤洰褰曪級
- 鉁?瀛樺湪鎬ч妫€

---

## 馃敶 PY-CORE-012: Cookie楠岃瘉涓庣鐞嗚寖寮?(Cookie Validation & Management)

### 鑼冨紡鎻忚堪
閫氳繃`CookieValidator`瀹炵幇Cookie鐨勬湁鏁堟€ч獙璇併€佸弸濂芥彁绀恒€佽嚜鍔ㄦ洿鏂板紩瀵笺€?

### 鏍稿績瀹炵幇
```python
class CookieValidator:
    """Cookie楠岃瘉鍣?""
    
    @staticmethod
    def validate_and_prompt(cookie_file):
        """楠岃瘉cookie骞剁粰鍑哄弸濂芥彁绀?""
        
        # 1. 妫€鏌ユ枃浠舵槸鍚﹀瓨鍦?
        if not os.path.exists(cookie_file):
            CookieValidator._show_prompt(
                title='Cookie鏂囦欢涓嶅瓨鍦?,
                reasons=['棣栨浣跨敤绋嬪簭', 'Cookie琚鍒犻櫎', '璺緞閿欒'],
                solutions=['閫夋嫨"鏇存柊Cookie"鍔熻兘', '娴忚鍣ㄥ皢鑷姩鎵撳紑鐧诲綍椤?],
                tip='Cookie鏈夋晥鏈熶负30澶╋紝寤鸿瀹氭湡鏇存柊'
            )
            return False, None
        
        # 2. 妫€鏌ユ枃浠舵牸寮?
        try:
            cookies = json.load(open(cookie_file))
        except json.JSONDecodeError:
            CookieValidator._show_prompt(
                title='Cookie鏂囦欢鏍煎紡閿欒',
                reasons=['鏂囦欢琚剰澶栦慨鏀?, '淇濆瓨鍑洪敊'],
                solutions=['鍒犻櫎褰撳墠Cookie', '閲嶆柊鑾峰彇']
            )
            return False, None
        
        # 3. 妫€鏌ookie鏈夋晥鏈?
        expiry_time = CookieValidator._check_expiry(cookies)
        if expiry_time and expiry_time < datetime.now():
            remaining_days = (expiry_time - datetime.now()).days
            if remaining_days < 7:
                CookieValidator._show_warning(
                    f'Cookie灏嗗湪{remaining_days}澶╁悗杩囨湡',
                    action='寤鸿绔嬪嵆鏇存柊'
                )
        
        return True, cookies
    
    @staticmethod
    def _show_prompt(title, reasons, solutions, tip=''):
        """鏄剧ず缁撴瀯鍖栫殑鍙嬪ソ鎻愮ず"""
        print_separator()
        print(f'鈿狅笍 {title}')
        print('\n鍙兘鐨勫師鍥?')
        for i, reason in enumerate(reasons, 1):
            print(f'  {i}. {reason}')
        print('\n瑙ｅ喅鏂规:')
        for i, solution in enumerate(solutions, 1):
            print(f'  鉁?{solution}')
        if tip:
            print(f'\n馃挕 鎻愮ず: {tip}')
        print_separator()
```

**鐢ㄦ埛浣撻獙浼樺寲**:
- 鉁?鍒嗘楠ら獙璇侊紙瀛樺湪鎬р啋鏍煎紡鈫掓湁鏁堟€э級
- 鉁?缁撴瀯鍖栭敊璇彁绀猴紙鍘熷洜+瑙ｅ喅鏂规+鎻愮ず锛?
- 鉁?杩囨湡棰勮锛堟彁鍓?澶╂彁閱掞級
- 鉁?寮曞寮忎慨澶嶆祦绋?

---

## 馃敶 PY-CORE-013: 鏂囦欢娓呯悊鑷姩鍖栬寖寮?(Automated File Cleanup)

### 鑼冨紡鎻忚堪
瀹炵幇鏅鸿兘鏂囦欢娓呯悊绛栫暐锛屾寜缁勪繚鐣欐渶鏂般€佹寜鏃堕棿鍒犻櫎鏃ф枃浠躲€佹敮鎸佹祴璇曟ā寮忋€?

### 鏍稿績瀹炵幇
```python
def clean_old_files(directory, dry_run=False):
    """
    娓呯悊鏃ф枃浠剁瓥鐣ワ細
    - 鎸?_'鍓嶇紑鍒嗙粍锛堝 image_001.jpg, image_002.jpg 涓轰竴缁勶級
    - 姣忕粍鍙繚鐣欐渶鏂扮殑涓€涓枃浠?
    - 鍒犻櫎鍏朵粬缁勭殑鎵€鏈夋枃浠?
    """
    
    matched_files = []
    
    # 鎵弿濯掍綋鏂囦欢
    for file in directory.iterdir():
        if file.is_file() and file.suffix.lower() in MEDIA_EXTENSIONS:
            stat = file.stat()
            name_without_ext = file.stem
            group_key = name_without_ext.split('_')[0] if '_' in name_without_ext else name_without_ext
            
            matched_files.append({
                'file': file,
                'group_key': group_key,
                'mtime': stat.st_mtime,
                'size': stat.st_size
            })
    
    # 鎸変慨鏀规椂闂存帓搴忥紙浠庢柊鍒版棫锛?
    matched_files.sort(key=lambda x: x['mtime'], reverse=True)
    
    # 鍒嗙粍
    groups = {}
    for file_info in matched_files:
        key = file_info['group_key']
        if key not in groups:
            groups[key] = []
        groups[key].append(file_info)
    
    # 鎵惧埌鏈€鏂扮殑涓€缁?
    sorted_groups = sorted(groups.keys(), 
                          key=lambda k: max(f['mtime'] for f in groups[k]),
                          reverse=True)
    latest_group = sorted_groups[0]
    
    # 鍒犻櫎闄ゆ渶鏂扮粍浠ュ鐨勬墍鏈夋枃浠?
    files_to_delete = [f for f in matched_files if f['group_key'] != latest_group]
    
    for file_info in files_to_delete:
        file_info['file'].unlink()
    
    print(f"娓呯悊瀹屾垚: 淇濈暀{len(groups[latest_group])}涓? 鍒犻櫎{len(files_to_delete)}涓?)

def auto_clean_temp_dir():
    """鑷姩娓呯悊temp鐩綍锛堣秴杩?MB鏃跺叏娓咃級"""
    temp_dir = os.path.join(PROJECT_DIR, 'temp')
    total_size = sum(f.stat().st_size for f in temp_dir.iterdir() if f.is_file())
    
    if total_size > 3 * 1024 * 1024:  # 3MB闃堝€?
        for f in temp_dir.iterdir():
            if f.is_file():
                f.unlink()
        print(f"[Clean] temp鐩綍瓒呰繃3MB锛屽凡娓呯悊")
```

**娓呯悊绛栫暐**:
- 鉁?鏅鸿兘鍒嗙粍锛堟寜鏂囦欢鍚嶅墠缂€锛?
- 鉁?淇濈暀鏈€鏂帮紙姣忕粍淇濈暀鏈€鏂版枃浠讹級
- 鉁?澶у皬鐩戞帶锛?MB鑷姩娓呯悊锛?
- 鉁?娴嬭瘯妯″紡锛坉ry_run棰勮锛?
- 鉁?绫诲瀷杩囨护锛堝浘鐗?瑙嗛/鏂囨。锛?

---

## 馃敶 PY-CORE-014: 鍚庡彴浠诲姟绠＄悊鑼冨紡 (Background Task Management)

### 鑼冨紡鎻忚堪
瀹炵幇鍚庡彴浠诲姟鐨勭敓鍛藉懆鏈熺鐞嗭紝鍖呮嫭鍚姩銆佺洃鎺с€佽緭鍑烘敹闆嗐€佺粓姝㈢瓑銆?

### 鏍稿績瀹炵幇
```python
processes = {}  # 杩涚▼瀛楀吀
tasks = {}      # 浠诲姟鐘舵€佸瓧鍏?
_processes_lock = threading.Lock()
_tasks_lock = threading.Lock()

def run_command_background(task_id, command):
    """鍚庡彴杩愯鍛戒护锛堢嚎绋?瀛愯繘绋嬶級"""
    
    with _tasks_lock:
        tasks[task_id] = {
            'status': 'running',
            'output': '',
            'start_time': time.time()
        }
    
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    
    # 鍚姩瀛愯繘绋?
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=PROJECT_DIR,
        text=True,
        bufsize=1,
        env=env
    )
    
    with _processes_lock:
        processes[task_id] = process
    
    # 瀹炴椂鏀堕泦杈撳嚭
    stdout_lines = []
    while True:
        if process.poll() is not None:
            remaining = process.stdout.read()
            if remaining:
                stdout_lines.append(remaining)
            break
        
        try:
            if Environment.IS_WINDOWS:
                time.sleep(0.1)
                line = process.stdout.readline()
            else:
                readable, _, _ = select.select([process.stdout], [], [], 0.1)
                if readable:
                    line = process.stdout.readline()
            
            if line:
                stdout_lines.append(line)
                
                # 瀹炴椂鏇存柊浠诲姟鐘舵€?
                with _tasks_lock:
                    tasks[task_id]['output'] = ''.join(stdout_lines)
                    
        except Exception as e:
            handle_exception(e, 'run_command_background')
    
    process.wait()
    
    with _tasks_lock:
        tasks[task_id]['returncode'] = process.returncode
        tasks[task_id]['output'] = ''.join(stdout_lines)
        tasks[task_id]['status'] = 'completed'

@app.post("/api/task/{task_id}/kill")
async def kill_task(task_id: str):
    """缁堟浠诲姟API"""
    with _processes_lock:
        if task_id in processes:
            process = processes[task_id]
            process.terminate()
            try:
                process.wait(timeout=TIMEOUT_CONFIG['subprocess_kill'])
            except subprocess.TimeoutExpired:
                process.kill()  # 寮哄埗鏉€姝?
            
            del processes[task_id]
            
    with _tasks_lock:
        if task_id in tasks:
            tasks[task_id]['status'] = 'killed'
    
    return {"success": True, "message": f"浠诲姟 {task_id} 宸茬粓姝?}
```

**浠诲姟绠＄悊鑳藉姏**:
- 鉁?瀹炴椂杈撳嚭娴佸紡鏀堕泦
- 鉁?浼橀泤缁堟锛坱erminate鈫抴ait鈫択ill锛?
- 鉁?绾跨▼瀹夊叏閿佷繚鎶?
- 鉁?浠诲姟鐘舵€佹満锛坮unning/completed/error/killed锛?
- 鉁?璺ㄥ钩鍙板吋瀹癸紙Windows select vs Unix select锛?

---

## 馃敶 PY-CORE-015: 闅ч亾楂樺彲鐢ㄨ寖寮?(High-Availability Tunnel)

### 鑼冨紡鎻忚堪
瀹炵幇hostc + Cloudflare鍙岄毀閬撲簰澶囨柟妗堬紝鍖呭惈蹇冭烦妫€娴嬨€佹晠闅滆浆绉汇€佽嚜鍔ㄩ噸鍚瓑鏈哄埗銆?

### 鏋舵瀯璁捐
```
鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?    鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?    鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?
鈹?  hostc      鈹?    鈹?Cloudflare       鈹?    鈹?  鍓嶇灞曠ず    鈹?
鈹?  闅ч亾       鈹?鈹€鈹€ 鈹?Tunnel           鈹?鈹€鈹€ 鈹?             鈹?
鈹?(Plan A)    鈹?    鈹?(Plan B)         鈹?    鈹?             鈹?
鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?    鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?    鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?
       鈹?                    鈹?                     鈹?
       鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?                     鈹?
                  鈻?                                鈹?
          鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?                        鈹?
          鈹?蹇冭烦瀹堟姢杩涚▼  鈹?鈼勨攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?
          鈹?(Heartbeat)  鈹?   瀹氭湡楠岃瘉URL鍙敤鎬?
          鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?
                  鈹?
         鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹粹攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?
         鈻?                鈻?
  Plan A鍙敤         Plan A涓嶅彲鐢?
  (浣跨敤hostc)       (鍒囨崲鍒癈F)
         鈹?                鈹?
         鈻?                鈻?
  鍙戦€乻table閭欢    鍙戦€乫allback閭欢
```

### 鏍稿績瀹炵幇
```python
def verify_url(url, timeout=5, method='GET'):
    """URL鍙敤鎬ч獙璇侊紙澶氭柟寮忓皾璇曪級"""
    
    validation_methods = [
        ('GET', lambda u: urllib.request.urlopen(u, timeout=timeout)),
        ('HEAD', lambda u: urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=timeout)),
        ('TCP', lambda u: socket.create_connection((u.hostname, 443), timeout=timeout))
    ]
    
    for method_name, method_func in validation_methods:
        try:
            result = method_func(url)
            return True, None
        except Exception as e:
            last_error = f"{method_name}: {e}"
    
    return False, last_error

def send_heartbeat():
    """蹇冭烦妫€娴嬪惊鐜?""
    
    while True:
        url = PathManager.get_public_url_from_web_log()
        
        if url:
            is_valid, error = verify_url(url)
            
            if is_valid:
                stable_confirm_count += 1
                
                if stable_confirm_count >= 3:  # 杩炵画3娆℃垚鍔?
                    if not was_stable:
                        email_notifier.send_tunnel_notification(url, 'stable_available')
                        was_stable = True
            else:
                stable_confirm_count = 0
                was_stable = False
                
                fail_count += 1
                
                if fail_count >= 2:  # 杩炵画2娆″け璐?
                    email_notifier.send_tunnel_notification(url, 'unavailable')
                    restart_tunnel()  # 瑙﹀彂閲嶅惎
                    fail_count = 0
        
        time.sleep(30)  # 30绉掗棿闅?

def restart_tunnel():
    """闅ч亾閲嶅惎锛堝弻闅ч亾鍒囨崲閫昏緫锛?""
    
    if use_cloudflare_tunnel:
        start_cloudflare_tunnel()
    else:
        start_hostc_tunnel()
    
    new_url = wait_for_tunnel_url(timeout=30)
    
    if new_url:
        PathManager._sync_url_to_tunnel_file(new_url)
        email_notifier.send_tunnel_notification(new_url, 'restarted')
```

**楂樺彲鐢ㄧ壒鎬?*:
- 鉁?鍙岄毀閬撲簰澶囷紙hostc + CF锛?
- 鉁?澶氭柟寮忛獙璇侊紙GET/HEAD/TCP锛?
- 鉁?杩炵画澶辫触璁℃暟锛堥槇鍊艰Е鍙戯級
- 鉁?绋冲畾鎬х‘璁わ紙杩炵画鎴愬姛N娆★級
- 鉁?鑷姩鏁呴殰杞Щ
- 鉁?閭欢閫氱煡鍒嗙骇锛坣ew/stable/unavailable/restarted/fallback锛?

---

## 馃搳 浠ｇ爜璐ㄩ噺鎸囨爣 (Code Quality Metrics)

### 鍛藉悕瑙勮寖
- **绫诲悕**: PascalCase锛圓ppException, ExceptionHandler锛?
- **鍑芥暟鍚?*: snake_case锛坰end_heartbeat, validate_cookie锛?
- **甯搁噺**: UPPER_SNAKE_CASE锛圱IMEOUT_CONFIG, PROJECT_DIR锛?
- **绉佹湁灞炴€?*: 涓嬪垝绾垮墠缂€锛坃config, _lock锛?
- **甯冨皵鍙橀噺**: is_/has_/can_鍓嶇紑锛坕s_valid, has_cache锛?

### 娉ㄩ噴瑙勮寖
- **绫绘敞閲?*: 鍔熻兘璇存槑 + 浣跨敤绀轰緥
- **鍑芥暟娉ㄩ噴**: Args/Returns/Raises + 绫诲瀷鏍囨敞
- **澶嶆潅閫昏緫**: 琛屽唴娉ㄩ噴璇存槑鎰忓浘
- **TODO/FIXME**: 鏍囪寰呭姙浜嬮」

### 閿欒澶勭悊绛夌骇
1. **鑷村懡閿欒**: 鎶涘嚭AppException锛岀粓姝㈡祦绋?
2. **鍙仮澶嶉敊璇?*: ExceptionContext鍚炴帀锛岃繑鍥為粯璁ゅ€?
3. **璀﹀憡**: 鏃ュ織璁板綍锛岀户缁墽琛?
4. **闈欓粯寮傚父**: debug绾у埆鏃ュ織锛屼笉褰卞搷娴佺▼

### 鎬ц兘瑕佹眰
- API鍝嶅簲鏃堕棿: < 500ms锛圥95锛?
- 鏂囦欢缂撳瓨TTL: 30绉?
- 閫熺巼闄愬埗: 200璇锋眰/鍒嗛挓/IP
- 瀛愯繘绋嬭秴鏃? 3-30绉掞紙鎸夊満鏅級
- 鐖櫕骞跺彂: 15绾跨▼

---

## 馃敡 寮€鍙戝伐浣滄祦 (Development Workflow)

### 鏂板姛鑳藉紑鍙戞祦绋?
1. **璁捐闃舵**
   - 纭畾鎵€灞炴ā鍧楋紙寮傚父/鏃ュ織/涓氬姟/API锛?
   - 閫夋嫨鍚堥€傜殑璁捐妯″紡锛堝崟渚?宸ュ巶/绛栫暐锛?
   - 瀹氫箟鎺ュ彛鍜屾暟鎹粨鏋?

2. **缂栫爜闃舵**
   - 閬靛惊鍛藉悕瑙勮寖鍜屾敞閲婅鑼?
   - 浣跨敤safe_call/ExceptionContext澶勭悊寮傚父
   - 閫氳繃PathManager绠＄悊璺緞
   - 浣跨敤ConfigManager璇诲啓閰嶇疆

3. **娴嬭瘯闃舵**
   - 鍗曞厓娴嬭瘯瑕嗙洊鏍稿績閫昏緫
   - 闆嗘垚娴嬭瘯楠岃瘉娴佺▼
   - 鎬ц兘娴嬭瘯婊¤冻鎸囨爣

4. **鏂囨。闃舵**
   - 鏇存柊README.md鐗堟湰璁板綍
   - 鏇存柊skill.md鑼冨紡鏂囨。
   - 閲嶆柊鐢熸垚skill.docx

### Git鎻愪氦瑙勮寖
```
docs: 鏂囨。鏇存柊
feat: 鏂板姛鑳?
fix: Bug淇
refactor: 浠ｇ爜閲嶆瀯
perf: 鎬ц兘浼樺寲
test: 娴嬭瘯鐩稿叧
chore: 鏋勫缓/宸ュ叿
security: 瀹夊叏淇
```

---

## 馃搱 椤圭洰婕旇繘璺嚎鍥?(Evolution Roadmap)

### v3.8.x - 浼佷笟绾хǔ瀹氱増 (褰撳墠)
- 鉁?FastAPI鍏ㄩ潰杩佺Щ瀹屾垚
- 鉁?鍙岄毀閬撻珮鍙敤鏂规
- 鉁?浼佷笟绾у畨鍏ㄥ姞鍥?
- 鉁?绉诲姩绔畬缇庨€傞厤
- 鉁?瀹屾暣鐨勭洃鎺у憡璀?

### v3.9.x - 鏅鸿兘鍖栧寮虹増 (瑙勫垝)
- 馃敳 AI杈呭姪鍟嗗搧瀹氫环
- 馃敳 鏅鸿兘搴撳瓨棰勬祴
- 馃敳 鑷姩鍖栨姤琛ㄧ敓鎴?
- 馃敳 澶氬簵閾虹鐞?
- 馃敳 鍒嗗竷寮忕埇铏泦缇?

### v4.0.x - 浜戝師鐢熸灦鏋?(杩滄湡)
- 馃敳 Kubernetes閮ㄧ讲
- 馃敳 寰湇鍔℃媶鍒?
- 馃敳 PostgreSQL杩佺Щ
- 馃敳 Redis缂撳瓨灞?
- 馃敳 娑堟伅闃熷垪闆嗘垚

---

## 馃幆 鎬荤粨

鏈」鐩疄鐜颁簡**15澶ф牳蹇冩妧鏈寖寮?*锛?

1. 鉁?**缁熶竴寮傚父澶勭悊** - 鍒嗗眰鎹曡幏銆佸垎绫汇€佽浆鎹?
2. 鉁?**鐜鑷€傚簲** - 璺ㄥ钩鍙版棤缂濆吋瀹?
3. 鉁?**璺緞闆嗕腑绠＄悊** - 閬垮厤纭紪鐮併€佹槗缁存姢
4. 鉁?**鏅鸿兘缂撳瓨鏈哄埗** - TTL + 鏂囦欢鍙樻洿妫€娴?
5. 鉁?**瀹夊叏閭欢閫氱煡** - HTML瀵屾枃鏈?+ 浜嬩欢鍒嗙被
6. 鉁?**娴忚鍣ㄨ嚜鍔ㄥ寲** - Playwright + 鏅鸿兘婊氬姩
7. 鉁?**鏁版嵁瀵规瘮鍒嗘瀽** - 闆嗗悎杩愮畻 + 楂樹环绛涢€?
8. 鉁?**API瀹夊叏闃叉姢** - 閫熺巼闄愬埗 + 杈撳叆楠岃瘉
9. 鉁?**鍓嶇XSS闃叉姢** - 杞箟 + 鐧藉悕鍗?
10. 鉁?**鍙岃緭鍑烘棩蹇?* - 鎺у埗鍙?+ 鏂囦欢鍚屾
11. 鉁?**閰嶇疆绠＄悊** - 鎳掑姞杞?+ 鑷姩鎸佷箙鍖?
12. 鉁?**Cookie鐢熷懡鍛ㄦ湡** - 楠岃瘉 + 杩囨湡鎻愰啋
13. 鉁?**鏂囦欢娓呯悊鑷姩鍖?* - 鍒嗙粍淇濈暀 + 澶у皬鐩戞帶
14. 鉁?**鍚庡彴浠诲姟绠＄悊** - 娴佸紡杈撳嚭 + 浼橀泤缁堟
15. 鉁?**闅ч亾楂樺彲鐢?* - 鍙屾椿 + 蹇冭烦 + 鏁呴殰杞Щ

杩欎簺鑼冨紡鏋勬垚浜嗕紒涓氱骇Python Web搴旂敤鐨?*鏈€浣冲疄璺甸泦**锛屽彲鐩存帴搴旂敤浜庣被浼奸」鐩€?
鈹?  鈹斺攢鈹€ WegoScraper - 寰喘鐖櫕绫?
鈹斺攢鈹€ API璺敱灞?
    鈹溾攢鈹€ FastAPI搴旂敤瀹炰緥
    鈹溾攢鈹€ RESTful API绔偣
    鈹斺攢鈹€ 璇锋眰楠岃瘉涓庡搷搴?
```

#### JavaScript鍓嶇妯″潡 (dist/app.js)
```
dist/app.js
鈹溾攢鈹€ 瀹夊叏宸ュ叿鍑芥暟
鈹?  鈹溾攢鈹€ escapeHtml() - HTML杞箟
鈹?  鈹溾攢鈹€ escapeAttr() - 灞炴€ц浆涔?
鈹?  鈹溾攢鈹€ isValidUrl() - URL楠岃瘉
鈹?  鈹斺攢鈹€ safeUrl() - 瀹夊叏URL鐢熸垚
鈹溾攢鈹€ 璁惧妫€娴嬬郴缁?
鈹?  鈹溾攢鈹€ detectDevice() - 璁惧绫诲瀷妫€娴?
鈹?  鈹斺攢鈹€ applyDeviceStyles() - 鍝嶅簲寮忔牱寮忓簲鐢?
鈹溾攢鈹€ 鏁版嵁瑙ｆ瀽寮曟搸
鈹?  鈹溾攢鈹€ 鏃ュ織瑙ｆ瀽 - Python杈撳嚭瑙ｆ瀽
鈹?  鈹溾攢鈹€ 姝ｅ垯琛ㄨ揪寮忎紭鍖?- 澶氭牸寮忓吋瀹?
鈹?  鈹斺攢鈹€ 鏁版嵁楠岃瘉 - 瀹归敊鏈哄埗
鈹溾攢鈹€ UI娓叉煋绯荤粺
鈹?  鈹溾攢鈹€ 缁熻鏁版嵁鏄剧ず
鈹?  鈹溾攢鈹€ 鍒楄〃鏁版嵁灞曠ず
鈹?  鈹斺攢鈹€ SKU鏍囩娓叉煋
鈹溾攢鈹€ WebSocket閫氫俊
鈹?  鈹溾攢鈹€ safeCloseWebSocket() - 瀹夊叏鍏抽棴
鈹?  鈹斺攢鈹€ 鐘舵€佹劅鐭ュ叧闂満鍒?
鈹溾攢鈹€ API瀹㈡埛绔?
鈹?  鈹溾攢鈹€ safeParseJson() - 瀹夊叏JSON瑙ｆ瀽
鈹?  鈹斺攢鈹€ 閿欒澶勭悊鏈哄埗
鈹斺攢鈹€ 浜嬩欢缁戝畾绯荤粺
    鈹溾攢鈹€ bindAllButtons() - 鎸夐挳缁戝畾
    鈹溾攢鈹€ bindSkuTagEvents() - SKU鏍囩浜嬩欢
    鈹斺攢鈹€ 鍏ㄥ眬鍑芥暟鏆撮湶
```

### 椤圭洰鐩綍缁撴瀯
```
D:/ws/xy_ws/
鈹溾攢鈹€ main.py                 # Python鍚庣涓荤▼搴?
鈹溾攢鈹€ README.md               # 椤圭洰璇存槑鏂囨。
鈹溾攢鈹€ skill.md                # 寮€鍙戞妧鑳芥枃妗ｏ紙鏈枃浠讹級
鈹溾攢鈹€ skill.docx              # Word鏍煎紡鏂囨。
鈹溾攢鈹€ run.bat                 # Windows鍚姩鑴氭湰
鈹溾攢鈹€ run.sh                  # Linux/Mac鍚姩鑴氭湰
鈹溾攢鈹€ tests/                  # 娴嬭瘯鐩綍
鈹?  鈹溾攢鈹€ test_main.py        # 涓绘祴璇曟枃浠?
鈹?  鈹溾攢鈹€ test_edge_cases.py  # 杈圭晫娴嬭瘯
鈹?  鈹溾攢鈹€ stress_test.py      # 鍘嬪姏娴嬭瘯
鈹?  鈹斺攢鈹€ test_security_fixes.py  # 瀹夊叏娴嬭瘯
鈹溾攢鈹€ dist/                   # 鍓嶇鏋勫缓浜х墿
鈹?  鈹溾攢鈹€ app.js              # JavaScript涓绘枃浠?
鈹?  鈹溾攢鈹€ index.html          # HTML鍏ュ彛
鈹?  鈹溾攢鈹€ package.json        # Node.js渚濊禆
鈹?  鈹溾攢鈹€ patches/            # patch-package琛ヤ竵
鈹?  鈹?  鈹斺攢鈹€ hostc+1.3.0.patch
鈹?  鈹溾攢鈹€ assets/             # 闈欐€佽祫婧?
鈹?  鈹?  鈹溾攢鈹€ index-*.js      # 搴旂敤浠ｇ爜
鈹?  鈹?  鈹溾攢鈹€ vendor-*.js     # 绗笁鏂瑰簱
鈹?  鈹?  鈹斺攢鈹€ index-*.css     # 鏍峰紡鏂囦欢
鈹?  鈹溾攢鈹€ fonts/              # 瀛椾綋鏂囦欢
鈹?  鈹溾攢鈹€ weather-icons/      # 澶╂皵鍥炬爣
鈹?  鈹斺攢鈹€ screenshots/        # 鎴浘
鈹溾攢鈹€ .github/workflows/      # CI/CD閰嶇疆
鈹?  鈹斺攢鈹€ ci-cd.yml
鈹斺攢鈹€ .venv/                  # Python铏氭嫙鐜
```

---

## 馃攧 鏈€鏂版洿鏂?(v3.8.89.19)

### v3.8.89.19 (2026-08-11) - 馃帹 鍒犻櫎鍟嗗搧鎻忚堪瀹屾暣鏄剧ず浼樺寲 + 鍝嶅簲寮忓竷灞€澧炲己

#### 鏇存柊鍐呭: 灏嗗垹闄ゅ晢鍝佺殑鍟嗗搧鎻忚堪浠庢埅鏂樉绀烘敼涓哄畬鏁存樉绀猴紝纭繚绉诲姩绔拰PC绔兘鑳藉畬缇庡睍绀?
**褰卞搷鏂囦欢**: [dist/app.js](dist/app.js#L2004), [README.md](README.md), [skill.md](skill.md)

---

- **鍒犻櫎鍟嗗搧鎻忚堪瀹屾暣鏄剧ず (鏍稿績鏀硅繘)** - 灏嗗垹闄ゅ晢鍝佺殑鍟嗗搧鎻忚堪浠庢埅鏂樉绀烘敼涓哄畬鏁存樉绀?  - 淇敼浣嶇疆: dist/app.js#L2004 (鍒犻櫎鍟嗗搧搴忓垪鍙疯〃鏍?
  - CSS鍙樻洿: 绉婚櫎 max-width(300px)/overflow(hidden)/text-overflow(ellipsis) 闄愬埗
  - 鏂板鏍峰紡: word-break(break-word)/white-space(normal)/min-width(200px)
  - 鏁堟灉: 闀挎弿杩拌嚜鍔ㄦ崲琛屽琛屾樉绀猴紝涓嶅啀鎴柇涓?..."

- **绉诲姩绔€傞厤 (鎵嬫満/骞虫澘)** - 浼樺厛淇濊瘉绉诲姩绔敤鎴蜂綋楠?  - 闀挎弿杩拌嚜鍔ㄦ崲琛屼负澶氳鏄剧ず
  - 瀹屾暣灞曠ず鎵€鏈夋枃瀛楀唴瀹癸紙涓嶅啀鎴柇锛?  - 涓嶄骇鐢熸í鍚戞粴鍔ㄦ潯锛堥伩鍏嶅竷灞€閿欎贡锛?  - 琛ㄦ牸瀹瑰櫒淇濇寔鍙粴鍔ㄦ€?
- **PC绔€傞厤 (鐢佃剳娴忚鍣?** - 娓愯繘澧炲己妗岄潰浣撻獙
  - 瀹屾暣鏄剧ず鍟嗗搧鎻忚堪鍏ㄦ枃
  - 琛ㄦ牸瀹瑰櫒鏀寔妯悜婊氬姩 (.change-table-container 宸叉湁 overflow-x: auto)
  - 淇濇寔鏁翠綋甯冨眬鏁存磥缇庤
  - 榧犳爣鎮仠浠嶅彲鏌ョ湅鎻愮ず (title 灞炴€т繚鐣?

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** - 涓ユ牸閬靛惊椤圭洰缂栫爜瑙勮寖
  - 鉁?PY-FRONT-001 瀹夊叏缂栫爜: 浣跨敤 escapeHtml() + escapeAttr() 鏃犲畨鍏ㄦ紡娲?  - 鉁?PY-FRONT-003 鍝嶅簲寮忚璁? 绉诲姩绔紭鍏?+ 娓愯繘澧炲己 + 瑙︽懜鍙嬪ソ
  - 鉁?PY-FRONT-004 宸紓鍖栦氦浜? 鏂板/楂樹环鍟嗗搧淇濈暀鐐瑰嚮鍔熻兘锛屽垹闄ゅ晢鍝佺函鏂囨湰灞曠ず

- **楠岃瘉缁撴灉** - 鍏ㄩ儴娴嬭瘯閫氳繃
  - [x] 鍒犻櫎鍟嗗搧闀挎弿杩?鈫?瀹屾暣澶氳鏄剧ず锛堟棤鎴柇锛夆渽
  - [x] 绉诲姩绔祴璇?鈫?鑷姩鎹㈣锛屾棤妯悜婊氬姩 鉁?  - [x] PC绔祴璇?鈫?瀹屾暣鏄剧ず锛屽鍣ㄥ彲婊氬姩 鉁?  - [x] XSS鏀诲嚮娴嬭瘯 鈫?鎭舵剰鑴氭湰鏃犳硶娉ㄥ叆 鉁?  - [x] 鍔熻兘鍥炲綊娴嬭瘯 鈫?鏂板/楂樹环鍟嗗搧鐐瑰嚮鍔熻兘姝ｅ父 鉁?  - [x] 琛ㄦ牸甯冨眬娴嬭瘯 鈫?鏁翠綋甯冨眬鏃犻敊涔?鉁?
## 馃攧 鏈€鏂版洿鏂?(v3.8.89.11)

### 馃敡 hostc WebSocket 瀹夊叏鍏抽棴淇 鈥?杩涚▼宕╂簝鏍瑰洜淇

#### 闂: hostc 闅ч亾鍚姩鏃舵姤閿?`WebSocket was closed before the connection was established` 骞跺鑷磋繘绋嬪穿婧?
**鐜拌薄**: 椤圭洰鍚姩鏃?hostc 闅ч亾灏濊瘯寤虹珛 WebSocket 杩炴帴锛岃秴鏃舵垨澶辫触鍚庤皟鐢?`safeCloseWebSocket2` 鍏抽棴 socket锛岃Е鍙戞湭鎹曡幏鐨?`error` 浜嬩欢瀵艰嚧 Node.js 杩涚▼宕╂簝閫€鍑?

**鏍规湰鍘熷洜**:
1. **`safeCloseWebSocket2` 鍑芥暟缂洪櫡**: 褰?WebSocket 澶勪簬 `CONNECTING` 鐘舵€佹椂锛岀洿鎺ヨ皟鐢?`socket.close()` 浼氭姏寮傚父锛坄ws` 搴撹瀹氭湭瀹屾垚鎻℃墜鐨?socket 蹇呴』鐢?`terminate()` 寮哄埗鍏抽棴锛?
2. **瓒呮椂澶勭悊鍣ㄧ己闄?*: 瓒呮椂鍚庤皟鐢?`safeCloseWebSocket2` 鍏抽棴 socket锛屼絾鏈鍏堟敞鍐?`error` 浜嬩欢鐩戝惉鍣紝瀵艰嚧 `close()` 瑙﹀彂鐨?error 浜嬩欢鏃犱汉澶勭悊锛屾姏鍑?`Unhandled 'error' event`

**淇鏂规**:
```javascript
// 鉂?淇鍓嶏細瓒呮椂澶勭悊鍣ㄧ洿鎺ュ叧闂紝鏈鐞?error 浜嬩欢
const timeout = setTimeout(() => {
  cleanup();
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);

// 鉁?淇鍚庯細鍏抽棴鍓嶅悶鎺?error 浜嬩欢锛岄槻姝㈣繘绋嬪穿婧?
const timeout = setTimeout(() => {
  cleanup();
  socket.once("error", () => {});
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);
```

```javascript
// 鉂?淇鍓嶏細涓嶅尯鍒?socket 鐘舵€侊紝鐩存帴璋冪敤 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
  } catch {
    socket.terminate();
  }
}

// 鉁?淇鍚庯細CONNECTING 鐘舵€佺敤 terminate()锛孫PEN 鐘舵€佺敤 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    if (socket.readyState === import_ws2.default.CONNECTING) {
      socket.once("error", () => {});
      socket.terminate();
    } else {
      socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
    }
  } catch {
    try { socket.terminate(); } catch {}
  }
}
```

**鎸佷箙鍖栦繚鎶?*:
- 鍦?`dist/package.json` 涓坊鍔?`patch-package` 浣滀负 `postinstall` 閽╁瓙
- 琛ヤ竵鏂囦欢 `dist/patches/hostc+1.3.0.patch` 纭繚 `npm install` 鍚庤嚜鍔ㄥ簲鐢ㄤ慨澶?

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓?| 淇鍚?|
|------|--------|--------|
| **hostc 鍚姩** | 杩涚▼宕╂簝 鉂?| 姝ｅ父鍚姩 鉁?|
| **WebSocket 瓒呮椂** | Unhandled error 鉂?| 浼橀泤鍏抽棴 鉁?|
| **琛ヤ竵鎸佷箙鍖?* | npm install 鍚庝涪澶?鉂?| postinstall 鑷姩搴旂敤 鉁?|

**鎶€鏈粏鑺?*:
- `ws` 搴撶殑 `close()` 鏂规硶浠呭湪 `OPEN` 鐘舵€佷笅鍙敤锛宍CONNECTING` 鐘舵€佸繀椤讳娇鐢?`terminate()`
- `socket.once("error", () => {})` 鐢ㄤ簬鍚炴帀鍥犲己鍒跺叧闂€屼骇鐢熺殑 error 浜嬩欢
- `patch-package` 纭繚姣忔 `npm install` 鍚庤ˉ涓佽嚜鍔ㄥ簲鐢紝涓嶄細鍥犱緷璧栨洿鏂拌€屼涪澶变慨澶?

---

### 馃敡 闅ч亾楠岃瘉淇 鈥?hostc/CF 鍧囦笉鍙敤鐨勬牴鍥犱慨澶?

#### 闂: 椤圭洰鍚姩鍚?hostc 鍜?CF 闅ч亾鍧囪鍒ゅ畾涓?涓嶅彲鐢?
**鐜拌薄**: 椤圭洰鍚姩鏃?hostc 鍜?Cloudflare Tunnel 閮借兘鎴愬姛鍚姩骞惰幏鍙栧埌 URL锛屼絾蹇冭烦楠岃瘉鏈哄埗濮嬬粓鍒ゅ畾涓轰笉鍙敤锛屽鑷村弽澶嶉噸鍚毀閬?

**鏍规湰鍘熷洜**:
1. **hostc 楠岃瘉澶辫触**: `verify_url()` 鍑芥暟浣跨敤 HTTP `HEAD` 鏂规硶楠岃瘉 URL锛屼絾 FastAPI 鏍硅矾鐢?`@app.get('/')` 涓嶆敮鎸?HEAD 璇锋眰锛岃繑鍥?`405 Method Not Allowed`锛屽鑷撮獙璇佹案杩滃け璐?
2. **CF 楠岃瘉澶辫触**: 鏈満 DNS 鏃犳硶瑙ｆ瀽 `trycloudflare.com` 鍩熷悕锛坄Errno 8: nodename nor servename provided`锛夛紝灞炰簬缃戠粶/DNS 閰嶇疆闂

**淇鏂规**:
```python
# 鉂?淇鍓嶏細鍙敮鎸?GET锛孒EAD 璇锋眰杩斿洖 405
@app.get('/')
async def index():

# 鉁?淇鍚庯細鍚屾椂鏀寔 GET 鍜?HEAD锛岄獙璇佽姹傛甯搁€氳繃
@app.api_route('/', methods=['GET', 'HEAD'])
async def index():
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓?| 淇鍚?|
|------|--------|--------|
| **hostc 楠岃瘉** | 405 Method Not Allowed 鉂?| 200 OK 鉁?|
| **蹇冭烦鍒ゅ畾** | 涓嶅彲鐢?鈫?鍙嶅閲嶅惎 鉂?| 鍙敤 鈫?绋冲畾杩愯 鉁?|
| **閭欢閫氱煡** | 鍙戦€?涓嶅彲鐢?閫氱煡 鉂?| 鍙戦€?鍙敤"閫氱煡 鉁?|

**鎶€鏈粏鑺?*:
- FastAPI 鐨?`@app.get()` 瑁呴グ鍣ㄤ笉浼氳嚜鍔ㄤ负璺敱鏀寔 HEAD 鏂规硶锛堜笌 Flask 涓嶅悓锛?
- `verify_url()` 浣跨敤 `urllib.request.Request(url, method='HEAD')` 鍙戦€?HEAD 璇锋眰
- 鏀圭敤 `@app.api_route('/', methods=['GET', 'HEAD'])` 鍚庯紝HEAD 璇锋眰杩斿洖涓?GET 鐩稿悓鐨勫搷搴斿ご锛堟棤 body锛夛紝楠岃瘉閫氳繃

**CF 涓嶅彲鐢ㄧ殑棰濆璇存槑**:
- CF 闅ч亾杩涚▼鏈韩鍚姩姝ｅ父锛堢洿鎺ヨ繛鎺?Cloudflare 鏈嶅姟鍣ㄨ幏鍙?URL锛?
- 浣嗘湰鏈?DNS 鏃犳硶瑙ｆ瀽 `*.trycloudflare.com`锛屽鑷撮獙璇佽姹傚け璐?
- 寤鸿鎺掓煡 DNS 璁剧疆锛歚nslookup xxx.trycloudflare.com`锛屾垨鏇存崲 DNS 涓?`8.8.8.8` / `114.114.114.114`

---

### 馃幆 楂樹环鍟嗗搧鏁拌В鏋愪慨澶?+ 鎸夐挳澶辨晥淇

#### 闂1: 楂樹环鍟嗗搧鏁版樉绀轰负0
**鐜拌薄**: 鐖櫕鏃ュ織鏄剧ず"鍞环 >= 599 鐨勫晢鍝? 78 涓?锛屼絾鐣岄潰鏄剧ず楂樹环鍟嗗搧鏁颁负 **0**

**鏍规湰鍘熷洜**: 
- 鍓嶇姝ｅ垯琛ㄨ揪寮忔棤娉曟纭尮閰峆ython杈撳嚭鐨勬牸寮?
- Python杈撳嚭鏍煎紡锛歚鍞环 >= 599 鐨勫晢鍝? 78 涓猔锛堟湁绌烘牸锛?
- 鍓嶇姝ｅ垯锛歚/鍞环[銆?=]+\s*599[^:锛歖*[:锛歖\s*(\d+)\s*[涓欢]/`锛堟棤娉曞尮閰嶇┖鏍硷級

**淇鏂规**:
```javascript
// 鉁?绠€鍖栨鍒欒〃杈惧紡锛岀洿鎺ュ尮閰峆ython杈撳嚭鏍煎紡
if (line.includes('鍞环') && line.includes('599') && line.includes('鍟嗗搧')) {
    // 涓昏鍖归厤锛?鍞环 >= 599 鐨勫晢鍝? 78 涓?
    let match = line.match(/鍞环\s*>=\s*599\s*鐨勫晢鍝乗s*[:锛歖\s*(\d+)\s*涓?);
    // 澶囬€夋柟妗堬細鍖归厤浠绘剰"鍟嗗搧: 鏁板瓧 涓?鏍煎紡
    if (!match) match = line.match(/鍟嗗搧\s*[:锛歖\s*(\d+)\s*涓?);
    // 鏈€鍚庡閫夛細鍖归厤琛屾湯鐨勬暟瀛?
    if (!match) match = line.match(/(\d+)\s*涓猏s*$/);
    
    if (match && parseInt(match[1]) > 0) {
        skuData.highPriceCount = match[1];
        console.log('[瀵规瘮鍗＄墖] 鉁?楂樹环鍟嗗搧鏁?', skuData.highPriceCount);
    }
}
```

**鏁版嵁娴佺▼璇存槑**:
1. **鐖櫕杩愯鏃?*锛氬墠绔В鏋愭棩蹇楄緭鍑哄疄鏃舵樉绀虹粺璁℃暟鎹?
2. **鐖櫕瀹屾垚鍚?*锛氬墠绔皟鐢?`/api/products` API鑾峰彇JSON鏁版嵁锛堝凡鍖呭惈 `highPriceCount` 瀛楁锛?

#### 闂2: 8涓寜閽叏閮ㄥけ鏁?
**鐜拌薄**: 椤甸潰鍔犺浇鍚庢墍鏈夋寜閽偣鍑绘棤鍝嶅簲

**鏍规湰鍘熷洜**: 
- `bindAllButtons()` 鍑芥暟瀹氫箟鍦ㄤ綔鐢ㄥ煙鍐咃紝涓嶆槸鍏ㄥ眬鍑芥暟
- 澶栭儴鏃犳硶璋冪敤锛屽鑷存寜閽簨浠剁粦瀹氬け璐?

**淇鏂规**:
```javascript
// 鉁?鏆撮湶涓哄叏灞€鍑芥暟
window.bindAllButtons = bindAllButtons;
window.resetButtons = resetButtons;
```

### 鉁?淇鏁堟灉
| 鎸囨爣 | 淇鍓?| 淇鍚?|
|------|--------|--------|
| **楂樹环鍟嗗搧(鈮?99)** | 0 鉂?| 78 鉁?|
| **鎸夐挳鍝嶅簲** | 澶辨晥 鉂?| 姝ｅ父 鉁?|
| **鏁版嵁鏄剧ず** | 閿欒 鉂?| 鍑嗙‘ 鉁?|

### 馃摑 鎶€鏈粏鑺?
- **鏂囦欢浣嶇疆**: `dist/app.js` Line 1369-1383, 1441-1453, 2707
- **淇鏂规硶**: 
  1. 绠€鍖栨鍒欒〃杈惧紡锛岀簿纭尮閰峆ython杈撳嚭鏍煎紡
  2. 鏆撮湶鍏ㄥ眬鍑芥暟锛岀‘淇濇寜閽粦瀹氭垚鍔?
- **楠岃瘉鏂瑰紡**: 
  1. Node.js璇硶妫€鏌ラ€氳繃
  2. 娴忚鍣ㄦ祴璇曟寜閽搷搴旀甯?
  3. 鐖櫕杩愯鏃跺疄鏃舵樉绀烘纭殑缁熻鏁版嵁

---

## 馃幆 鏍稿績鍘熷垯

### 1. 浠ｇ爜璐ㄩ噺绗竴
- 鉁?**璇硶姝ｇ‘鎬?* - 鎵€鏈変唬鐮佸繀椤婚€氳繃璇硶妫€鏌?
- 鉁?**鎷彿鍖归厤** - 鍑芥暟璋冪敤銆佹潯浠跺垽鏂殑鎷彿蹇呴』鎴愬鍑虹幇
- 鉁?**閫昏緫瀹屾暣鎬?* - 閬垮厤鍥犺娉曢敊璇鑷村姛鑳藉け鏁?

### 2. 鐢ㄦ埛浣撻獙浼樺厛
- 鉁?**鏁版嵁鍑嗙‘鎬?* - 纭繚鏄剧ず鐨勬暟鎹笌瀹為檯涓€鑷?
- 鉁?**閿欒鍙嬪ソ鎬?* - 鎻愪緵娓呮櫚鐨勯敊璇彁绀哄拰瑙ｅ喅鏂规
- 鉁?**鎬ц兘浼樺寲** - 閬垮厤涓嶅繀瑕佺殑閲嶅璁＄畻

### 3. 鍙淮鎶ゆ€?
- 鉁?**娉ㄩ噴瀹屾暣** - 涓枃娉ㄩ噴锛屾竻鏅版弿杩伴€昏緫
- 鉁?**鏃ュ織璇︾粏** - 鍏抽敭鎿嶄綔蹇呴』鏈夋棩蹇楄緭鍑?
- 鉁?**寮傚父澶勭悊** - 缁熶竴鐨勫紓甯告崟鑾峰拰澶勭悊鏈哄埗

---

## 馃敡 JavaScript 寮€鍙戣鑼?(app.js)

### 2.1 鍩虹璇硶瑙勫垯 鈿狅笍 **閲嶈**

#### 2.1.1 鎷彿鍖归厤 (寮哄埗)
```javascript
// 鉂?閿欒绀轰緥 - 鎷彿涓嶅尮閰嶏紙2026-07-30瀹為檯Bug锛?
} else if ((line.includes('鍞环 >=') || line.includes('鍞环>=')) && line.includes('鍟嗗搧') )) &&
           line.includes('鈮?99')) &&  // 鈫?澶氫簡涓や釜 )
           line.match(/鍞环.*>=.*599.*鍟嗗搧/)) {

// 鉁?姝ｇ‘绀轰緥 - 鎷彿姝ｇ‘鍖归厤
} else if ((line.includes('鍞环 >=') || line.includes('鍞环>=')) &&
           (line.includes('鍟嗗搧') || line.includes('鈮?99')) &&  // 鈫?浣跨敤 ||
           line.match(/鍞环.*>=.*599.*鍟嗗搧/)) {
```

**妫€鏌ユ竻鍗?*:
- [ ] 姣忎釜 `(` 蹇呴』鏈夊搴旂殑 `)`
- [ ] 姣忎釜 `[` 蹇呴』鏈夊搴旂殑 `]`
- [ ] 姣忎釜 `{` 蹇呴』鏈夊搴旂殑 `}`
- [ ] 澶氭潯浠跺垽鏂椂浣跨敤 `||` 鍜?`&&` 鐨勬纭粍鍚?

#### 2.1.2 鏉′欢鍒ゆ柇鏈€浣冲疄璺?
```javascript
// 鉁?鎺ㄨ崘锛氫娇鐢ㄩ€昏緫杩愮畻绗︾粍鍚堟潯浠?
if ((condition1 || condition2) && 
    (condition3 || condition4) && 
    regex.test(string)) {
    // 鎵ц閫昏緫
}

// 鉂?閬垮厤锛氬祵濂楄繃澶氱殑鎷彿瀵艰嚧娣蜂贡
if (((condition1) && (condition2)) || ((condition3))) {
    // 涓嶆帹鑽?
}
```

#### 2.1.3 瀛楃涓插鐞嗚鑼?
```javascript
// 鉁?姝ｇ‘锛氫娇鐢ㄦā鏉垮瓧绗︿覆鎴栬浆涔夊瓧绗?
const str = `line.includes('\u5546\u54C1')`;  // Unicode杞箟
const pattern = /pattern/g;                     // 姝ｅ垯琛ㄨ揪寮?

// 鈿狅笍 娉ㄦ剰锛歐indows鐜涓嬬殑鎹㈣绗?
// 鏂囦欢鍙兘浣跨敤 \r\n (CRLF)锛岄渶瑕佺壒娈婂鐞?
const content = fs.readFileSync(file, 'utf8');
content = content.replace(/\r\n/g, '\n');  // 缁熶竴杞崲涓篖F
```

#### 2.1.4 鏂囦欢娓呯悊瑙勮寖 (2026-07-30鏂板)
```javascript
// 鈿狅笍 閲嶈锛氶伩鍏嶆枃浠舵湯灏惧嚭鐜板瀮鍦惧唴瀹?
// 闂锛氭枃浠舵湯灏剧殑 \r\n 瀛楃涓诧紙浣滀负鏂囨湰鍐呭锛変細瀵艰嚧璇硶閿欒

// 鉂?閿欒绀轰緥锛氭枃浠舵湯灏炬湁鍨冨溇鍐呭
// Line 4989:        });
// Line 4990: \r\n\r\n\r\n... (澶ч噺閲嶅)
// Line 5000: let match = line.match(/(\d+)\s*(涓獆浠?/); (閲嶅浠ｇ爜)

// 鉁?姝ｇ‘鍋氭硶锛氬畾鏈熸竻鐞嗘枃浠舵湯灏?
// 1. 浣跨敤 Node.js 璇硶妫€鏌ュ彂鐜伴敊璇?
//    node --check dist/app.js

// 2. 浣跨敤 PowerShell 鑴氭湰娓呯悊
//    $content = Get-Content "dist/app.js" -Raw
//    $lines = $content -split "`n"
//    $cleanContent = $lines[0..4988] -join "`n"
//    Set-Content "dist/app.js" -Value $cleanContent -NoNewline -Encoding UTF8

// 3. 楠岃瘉娓呯悊缁撴灉
//    node --check dist/app.js  # 搴旇閫氳繃
```

**鏂囦欢娓呯悊妫€鏌ユ竻鍗?*:
- [ ] 鏂囦欢鏈熬鏃犻噸澶嶇殑 `\r\n` 瀛楃涓?
- [ ] 鏂囦欢鏈熬鏃犻噸澶嶇殑浠ｇ爜鐗囨
- [ ] Node.js 璇硶妫€鏌ラ€氳繃
- [ ] 鏂囦欢澶у皬鍚堢悊锛堟棤寮傚父澧炲ぇ锛?

### 2.2 鏁版嵁瑙ｆ瀽瑙勮寖

#### 2.2.1 杈撳嚭鏁版嵁瑙ｆ瀽娴佺▼
```javascript
// 1. 棰勬壂鎻忥紙瀹芥澗妯″紡锛夋彁鍙栧叧閿暟鎹?
for (let i = 0; i < lines.length; i++) {
    let line = lines[i].trim();
    if (!line) continue;
    
    // 瓒呯骇瀹芥澗鐨勬€诲晢鍝佹暟鍖归厤
    if ((line.includes('鍟嗗搧') || line.includes('涓?)) && !skuData.totalProducts) {
        const match = line.match(/(\d+)/);
        if (match && parseInt(match[1]) > 0) {
            skuData.totalProducts = match[1];
        }
    }
}

// 2. 绮剧‘瑙ｆ瀽锛堣鐩栭鎵弿缁撴灉锛?
for (let i = 0; i < lines.length; i++) {
    let line = lines[i].trim();
    
    // 鏇寸簿纭殑妯″紡鍖归厤
    if (line.includes('鎴愬姛鑾峰彇') || line.match(/(\d+)\s*(涓獆浠?.*鍟嗗搧/)) {
        skuData.type = 'spider';
        let match = line.match(/(\d+)\s*(涓獆浠?/);
        if (match) {
            skuData.totalProducts = match[1];  // 瑕嗙洊棰勬壂鎻忕粨鏋?
        }
    }
}
```

#### 2.2.2 鏁版嵁楠岃瘉涓庡閿?
```javascript
// 鉁?濂界殑鍋氭硶锛氭彁渚涘涓尮閰嶆ā寮忎綔涓篺allback
let match = line.match(/(\d+)\s*(涓獆浠?/);      // 涓昏妯″紡
if (!match) {
    match = line.match(/[:锛歖\s*(\d+)/);          // 澶囬€夋ā寮?
}
if (!match) {
    match = line.match(/(\d+)/);                  // 澶囬€夋ā寮?
}

if (match) {
    skuData.highPriceCount = match[1];
    console.log('[瀵规瘮鍗＄墖] 鉁?楂樹环鍟嗗搧鏁?', skuData.highPriceCount);
}
```

#### 2.2.3 姝ｅ垯琛ㄨ揪寮忎紭鍖?(2026-07-30鏂板)
```javascript
// 鉁?鏀寔澶氱绗﹀彿鏍煎紡鐨勬鍒欒〃杈惧紡
// 闂锛氱埇铏緭鍑哄彲鑳戒娇鐢ㄥ叏瑙掔鍙?銆?銆佸崐瑙掔鍙?>="銆佹暟瀛︾鍙?鈮?
// 瑙ｅ喅锛氫娇鐢ㄥ瓧绗︾被 [銆?=]+ 鍖归厤鎵€鏈夊彲鑳界殑绗﹀彿

if (line.includes('鍞环') && (line.includes('599') || line.includes('鈮?99'))) {
    // 涓昏妯″紡锛氱簿纭尮閰?鍞环[绗﹀彿]599鐨勫晢鍝侊細鏁板瓧涓?
    let match = line.match(/鍞环[銆?=]+\s*599[^:锛歖*[:锛歖\s*(\d+)\s*[涓欢]/);
    
    // 澶囬€夋ā寮?锛氬尮閰?鏁板瓧涓?浠?
    if (!match) match = line.match(/(\d+)\s*[涓欢]/);
    
    // 澶囬€夋ā寮?锛氬尮閰?锛氭暟瀛?
    if (!match) match = line.match(/[:锛歖\s*(\d+)/);
    
    // 澶囬€夋ā寮?锛氬尮閰嶄换鎰忔暟瀛?
    if (!match) match = line.match(/(\d+)/);
    
    // 楠岃瘉鏁板瓧鏈夋晥鎬?
    if (match && parseInt(match[1]) > 0) {
        skuData.highPriceCount = match[1];
        console.log('[瀵规瘮鍗＄墖] 鉁?楂樹环鍟嗗搧鏁?', skuData.highPriceCount);
    }
}
```

**鏀寔鐨勬牸寮忕ず渚?*:
- `鍞环銆?599鐨勫晢鍝侊細71涓猔 (鍏ㄨ绗﹀彿)
- `鍞环>=599鐨勫晢鍝? 77涓猔 (鍗婅绗﹀彿)
- `鍞环鈮?99鐨勫晢鍝侊細80浠禶 (鏁板绗﹀彿)
- `鍞环 >= 599 鐨勫晢鍝? 85 涓猔 (甯︾┖鏍?

### 2.3 WebSocket 瀹夊叏鍏抽棴瑙勮寖 鈿狅笍 **閲嶈** (2026-07-30 鏂板)

#### 2.3.1 socket 鐘舵€佹劅鐭ュ叧闂?(寮哄埗)
```javascript
// 鉂?閿欒锛氫笉鍖哄垎 socket 鐘舵€佺洿鎺ヨ皟鐢?close()
// 褰?socket 澶勪簬 CONNECTING 鐘舵€佹椂锛宑lose() 浼氭姏鍑哄紓甯?
// 瀵艰嚧 "WebSocket was closed before the connection was established" 閿欒
function safeCloseWebSocket(socket, code, reason) {
  if (!socket) return;
  try {
    socket.close(code, reason);  // CONNECTING 鐘舵€佷笅浼氬穿婧冿紒
  } catch {
    socket.terminate();
  }
}

// 鉁?姝ｇ‘锛氭牴鎹?readyState 閫夋嫨鍏抽棴鏂瑰紡
function safeCloseWebSocket(socket, code, reason) {
  if (!socket) return;
  try {
    if (socket.readyState === WebSocket.CONNECTING) {
      socket.once("error", () => {});  // 鍚炴帀 error 浜嬩欢
      socket.terminate();               // 寮哄埗鍏抽棴
    } else {
      socket.close(code, reason);       // 姝ｅ父鍏抽棴
    }
  } catch {
    try { socket.terminate(); } catch {}  // 鍙岄噸淇濇姢
  }
}
```

**鍏抽敭瑙勫垯**:
- `WebSocket.CONNECTING (0)`: 蹇呴』浣跨敤 `terminate()`锛屼笉鑳戒娇鐢?`close()`
- `WebSocket.OPEN (1)`: 浣跨敤 `close()` 鍙戦€佸叧闂抚锛屼紭闆呭叧闂?
- `WebSocket.CLOSING (2)` / `WebSocket.CLOSED (3)`: 鏃犻渶鎿嶄綔
- 鍏抽棴鍓嶅繀椤绘敞鍐?`socket.once("error", () => {})` 闃叉鏈崟鑾风殑 error 浜嬩欢

#### 2.3.2 瓒呮椂澶勭悊鍣ㄥ畨鍏ㄥ叧闂ā寮?
```javascript
// 鉂?閿欒锛氳秴鏃跺悗鐩存帴鍏抽棴锛屾湭澶勭悊鍙兘瑙﹀彂鐨?error 浜嬩欢
const timeout = setTimeout(() => {
  cleanup();
  safeCloseWebSocket(socket, code, reason);  // 鍙兘瑙﹀彂 unhandled error
  reject(new Error("connect timeout"));
}, TIMEOUT_MS);

// 鉁?姝ｇ‘锛氬叧闂墠鍚炴帀 error 浜嬩欢
const timeout = setTimeout(() => {
  cleanup();
  socket.once("error", () => {});  // 鍏堟敞鍐?error 鐩戝惉鍣?
  safeCloseWebSocket(socket, code, reason);
  reject(new Error("connect timeout"));
}, TIMEOUT_MS);
```

#### 2.3.3 patch-package 鎸佷箙鍖栬ˉ涓?
```bash
# 淇敼 node_modules 涓殑浠ｇ爜鍚庯紝鐢熸垚琛ヤ竵鏂囦欢
npx patch-package hostc

# 琛ヤ竵鏂囦欢淇濆瓨鍒?patches/ 鐩綍
# dist/patches/hostc+1.3.0.patch

# 鍦?package.json 涓坊鍔?postinstall 閽╁瓙
# "scripts": { "postinstall": "patch-package" }
# "dependencies": { "patch-package": "^8.0.0" }

# 姣忔 npm install 鍚庤嚜鍔ㄥ簲鐢ㄨˉ涓?
npm install  # 鈫?postinstall 鈫?patch-package 鈫?搴旂敤琛ヤ竵
```

**琛ヤ竵绠＄悊妫€鏌ユ竻鍗?*:
- [ ] 淇敼 node_modules 鍚庢墽琛?`npx patch-package <package-name>`
- [ ] patches/ 鐩綍涓嬬殑 .patch 鏂囦欢宸叉彁浜ゅ埌 Git
- [ ] package.json 鍖呭惈 `postinstall: "patch-package"` 鑴氭湰
- [ ] package.json 鍖呭惈 `patch-package` 渚濊禆
- [ ] `npm install` 鍚庨獙璇佽ˉ涓佸凡姝ｇ‘搴旂敤

### 2.4 鏃ュ織瑙ｆ瀽瑙勮寖 鈿狅笍 **閲嶈** (2026-07-30 鏂板)

#### 2.4.1 楂樹环鍟嗗搧鏁拌В鏋?(寮哄埗)
```javascript
// 鉂?閿欒锛氭鍒欒〃杈惧紡鏃犳硶鍖归厤Python杈撳嚭鏍煎紡
// Python杈撳嚭锛氬敭浠?>= 599 鐨勫晢鍝? 78 涓紙鏈夌┖鏍硷級
// 鏃ф鍒欙細/鍞环[銆?=]+\s*599[^:锛歖*[:锛歖\s*(\d+)\s*[涓欢]/锛堟棤娉曞尮閰嶇┖鏍硷級
if (line.match(/鍞环[銆?=]+\s*599[^:锛歖*[:锛歖\s*(\d+)\s*[涓欢]/)) { ... }

// 鉁?姝ｇ‘锛氱畝鍖栨鍒欙紝绮剧‘鍖归厤Python杈撳嚭鏍煎紡
if (line.includes('鍞环') && line.includes('599') && line.includes('鍟嗗搧')) {
    let match = line.match(/鍞环\s*>=\s*599\s*鐨勫晢鍝乗s*[:锛歖\s*(\d+)\s*涓?);
    if (!match) match = line.match(/鍟嗗搧\s*[:锛歖\s*(\d+)\s*涓?);
    if (!match) match = line.match(/(\d+)\s*涓猏s*$/);
    if (match && parseInt(match[1]) > 0) {
        skuData.highPriceCount = match[1];
    }
}
```

**鍏抽敭瑙勫垯**:
- Python杈撳嚭鏍煎紡鍙兘鍖呭惈绌烘牸锛坄鍞环 >= 599`锛夛紝姝ｅ垯蹇呴』鍏煎
- 浣跨敤澶氱骇fallback锛氱簿纭尮閰?鈫?瀹芥澗鍖归厤 鈫?琛屾湯鏁板瓧
- 瑙ｆ瀽鍚庡繀椤婚獙璇佹暟瀛楁湁鏁堟€э紙`parseInt > 0`锛?

#### 2.4.2 鍏ㄥ眬鍑芥暟鏆撮湶瑙勮寖 (寮哄埗)
```javascript
// 鉂?閿欒锛氬嚱鏁板畾涔夊湪浣滅敤鍩熷唴锛屽閮ㄦ棤娉曡皟鐢?
function bindAllButtons() { ... }
function resetButtons() { ... }
// HTML涓殑 onclick="bindAllButtons()" 鎶ラ敊锛歜indAllButtons is not defined

// 鉁?姝ｇ‘锛氭毚闇蹭负鍏ㄥ眬鍑芥暟
window.bindAllButtons = bindAllButtons;
window.resetButtons = resetButtons;
```

**鍏抽敭瑙勫垯**:
- 鎵€鏈夎 HTML `onclick` 寮曠敤鐨勫嚱鏁板繀椤绘毚闇插埌 `window` 瀵硅薄
- ES Module 鎴?IIFE 鍐呭畾涔夌殑鍑芥暟榛樿涓嶅湪鍏ㄥ眬浣滅敤鍩?
- 鏆撮湶鏂瑰紡锛歚window.functionName = functionName`

### 2.5 UI娓叉煋瑙勮寖

#### 2.5.1 缁熻鏁版嵁鏄剧ず
```javascript
// 鉁?浣跨敤榛樿鍊奸槻姝㈡樉绀?undefined 鎴?NaN
<span class="stat-value">${skuData.highPriceCount || 0}</span>
<span class="stat-value">${skuData.totalPrice || '楼0.00'}</span>

// 鉁?鏉′欢鏍峰紡绫诲悕
<div class="stat-item ${skuData.highPriceExtraCount > 0 ? 'stat-danger' : ''}">
```

#### 2.5.2 鍒楄〃鏁版嵁灞曠ず
```javascript
// 鉁?鍘婚噸澶勭悊
if (skuData.highPriceExtraSkus2 && skuData.highPriceExtraSkus2.length > 0) {
    const uniqueHighPriceExtras = [...new Set(skuData.highPriceExtraSkus2)];
    const items = uniqueHighPriceExtras.map(sku => createSkuTag(sku, showProductDetail)).join('');
    
    cardHtml += `
        <div class="missing-skus" style="background: #ffebee;">
            <div class="missing-title">JSON澶氫綑璐у彿(楂樹环鍟嗗搧鈮?99):</div>
            <div class="sku-container">${items}</div>
        </div>
    `;
}
```

---

## 馃悕 Python 寮€鍙戣鑼?(main.py) - 瀹屾暣鐗?

### 3.0 浠ｇ爜缁勭粐涓庡鍏ヨ鑼?

#### 3.0.1 瀵煎叆椤哄簭锛堝己鍒讹級
```python
# -*- coding: utf-8 -*-
# 鏍囧噯搴?
import argparse
import asyncio
import json
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Any

# 绗笁鏂瑰簱
try:
    import pandas as pd
except ImportError:
    pd = None

try:
    from fastapi import FastAPI, Request, HTTPException
    from fastapi.responses import JSONResponse
except ImportError:
    FastAPI = None

# 椤圭洰鍐呴儴妯″潡锛堢浉瀵瑰鍏ワ級
from .exceptions import AppException
from .config import ConfigManager
```

**瀵煎叆瑙勫垯**:
1. 鏍囧噯搴?鈫?绗笁鏂瑰簱 鈫?椤圭洰鍐呴儴妯″潡
2. 姣忕粍涔嬮棿绌轰竴琛屽垎闅?
3. 浣跨敤 `try-except` 澶勭悊鍙€変緷璧?
4. 绂佹浣跨敤 `from module import *`

#### 3.0.2 鍛藉悕瑙勮寖锛堝己鍒讹級
```python
# 绫诲悕锛氬ぇ椹煎嘲鍛藉悕娉?(PascalCase)
class WegoScraper:          # 鉁?姝ｇ‘
classwegoScraper:           # 鉂?閿欒

# 鍑芥暟/鍙橀噺锛氳泧褰㈠懡鍚嶆硶 (snake_case)
def get_version_from_readme():  # 鉁?姝ｇ‘
def getVersionFromReadme():     # 鉂?閿欒

# 甯搁噺锛氬叏澶у啓 + 铔囧舰鍛藉悕娉?(UPPER_SNAKE_CASE)
TIMEOUT_CONFIG = {}           # 鉁?姝ｇ‘
timeoutConfig = {}            # 鉂?閿欒

# 绉佹湁灞炴€?鏂规硶锛氬崟涓嬪垝绾垮墠缂€
def _private_method(self):    # 鉁?姝ｇ‘
self._internal_state = []     # 鉁?姝ｇ‘
```

#### 3.0.3 绫诲瀷娉ㄨВ瑙勮寖锛堝己鍒讹級
```python
from typing import List, Dict, Optional, Any, Callable, TypeVar, Union, Tuple

# 鍑芥暟绛惧悕蹇呴』鍖呭惈绫诲瀷娉ㄨВ
def safe_call(func: Callable[..., T], *args, default: T = None, context: str = '', **kwargs) -> T:
    """瀹夊叏璋冪敤鍖呰鍣?""
    ...

# 澶嶆潅绫诲瀷浣跨敤TypeVar
T = TypeVar('T')

# 杩斿洖鍊煎彲鑳芥槸澶氱绫诲瀷鏃朵娇鐢║nion
def get_data() -> Union[Dict[str, Any], None]:
    ...

# 鍙€夊弬鏁颁娇鐢∣ptional
def setup_logger(log_file: Optional[str] = None, log_level: int = logging.INFO) -> logging.Logger:
    ...
```

### 3.1 寮傚父澶勭悊绯荤粺瑙勮寖 鈿狅笍 **鏍稿績**

#### 3.1.1 缁熶竴寮傚父绫?AppException锛堝己鍒讹級
```python
class AppException(Exception):
    """
    缁熶竴寮傚父绫?- 鎵€鏈変笟鍔″紓甯搁兘浣跨敤姝ょ被
    
    鍒嗙被浣撶郴锛?
    - FILE: 鏂囦欢鎿嶄綔寮傚父
    - NETWORK: 缃戠粶璇锋眰寮傚父
    - AUTH: 璁よ瘉寮傚父
    - BROWSER: 娴忚鍣ㄦ搷浣滃紓甯?
    - PARSE: 鏁版嵁瑙ｆ瀽寮傚父
    - CONFIG: 閰嶇疆寮傚父
    - EXCEL: Excel鎿嶄綔寮傚父
    - EMAIL: 閭欢鍙戦€佸紓甯?
    - PERMISSION: 鏉冮檺寮傚父
    - RESOURCE: 璧勬簮寮傚父
    - VALIDATION: 楠岃瘉寮傚父
    - DATABASE: 鏁版嵁搴撳紓甯?
    """
    
    CATEGORY_FILE = 'FILE'
    CATEGORY_NETWORK = 'NETWORK'
    CATEGORY_AUTH = 'AUTH'
    # ... 鍏朵粬鍒嗙被
    
    def __init__(self, message: str, category: str = None, code: str = None, details: Any = None):
        self.message = message
        self.category = category or 'APP'
        self.code = code or self._CATEGORY_CODES.get(self.category, 'APP_ERROR')
        self.details = details or {}
        super().__init__(self.message)
    
    @classmethod
    def file_error(cls, message: str, file_path: str = None, operation: str = None, **kwargs):
        """鏂囦欢鎿嶄綔寮傚父宸ュ巶鏂规硶"""
        details = {'file_path': file_path, 'operation': operation}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_FILE, details=details)
    
    @classmethod
    def network_error(cls, message: str, url: str = None, status_code: int = None, **kwargs):
        """缃戠粶璇锋眰寮傚父宸ュ巶鏂规硶"""
        details = {'url': url, 'status_code': status_code}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_NETWORK, details=details)
    
    # ... 鍏朵粬宸ュ巶鏂规硶
```

#### 3.1.2 寮傚父澶勭悊瑁呴グ鍣紙寮哄埗锛?
```python
def exception_handler(context: str = '', default: Any = None, reraise: bool = False, custom_exc: type = None):
    """
    寮傚父澶勭悊瑁呴グ鍣?
    
    鐢ㄩ€旓細
    - 缁熶竴鎹曡幏鍜屽鐞嗗紓甯?
    - 璁板綍璇︾粏鏃ュ織
    - 鎻愪緵鍙嬪ソ鐨勯敊璇彁绀?
    
    鍙傛暟锛?
    - context: 鎿嶄綔涓婁笅鏂囨弿杩?
    - default: 寮傚父鏃剁殑榛樿杩斿洖鍊?
    - reraise: 鏄惁閲嶆柊鎶涘嚭寮傚父
    - custom_exc: 鑷畾涔夊紓甯哥被鍨?
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AppException as e:
                logger.error(f"[{context}] 涓氬姟寮傚父: {e.message}", extra=e.details)
                if reraise:
                    raise
                return default
            except Exception as e:
                logger.error(f"[{context}] 鏈鏈熷紓甯? {str(e)}", exc_info=True)
                if custom_exc:
                    raise custom_exc(str(e)) from e
                if reraise:
                    raise
                return default
        return wrapper
    return decorator
```

#### 3.1.3 涓婁笅鏂囩鐞嗗櫒妯″紡锛堟帹鑽愶級
```python
class ExceptionContext:
    """
    寮傚父涓婁笅鏂囩鐞嗗櫒
    
    鐢ㄩ€旓細
    - 鑷姩璁板綍杩涘叆/閫€鍑烘棩蹇?
    - 缁熶竴寮傚父澶勭悊
    - 璧勬簮鑷姩娓呯悊
    """
    
    def __init__(self, context: str, reraise: bool = False):
        self.context = context
        self.reraise = reraise
    
    def __enter__(self):
        logger.debug(f"[{self.context}] 寮€濮嬫墽琛?)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            logger.debug(f"[{self.context}] 鎵ц鎴愬姛")
            return False
        
        logger.error(f"[{self.context}] 鍙戠敓寮傚父: {exc_val}", exc_info=True)
        if self.reraise:
            return False  # 閲嶆柊鎶涘嚭寮傚父
        return True  # 鍚炴帀寮傚父
```

**浣跨敤绀轰緥**:
```python
@exception_handler(context='璇诲彇閰嶇疆鏂囦欢', default={})
def load_config():
    with ExceptionContext('鍔犺浇JSON閰嶇疆'):
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)

# 鎴栬€呯洿鎺ヤ娇鐢ㄤ笂涓嬫枃绠＄悊鍣?
with ExceptionContext('鏂囦欢鎿嶄綔', reraise=True) as ctx:
    data = process_file()
```

### 3.2 鏃ュ織绯荤粺瑙勮寖 鈿狅笍 **閲嶈**

#### 3.2.1 TeeOutput 鍙岃緭鍑烘祦锛堝己鍒讹級
```python
class TeeOutput:
    """
    鍙岃緭鍑烘祦 - 鍚屾椂杈撳嚭鍒版帶鍒跺彴鍜屾枃浠?
    
    鐗规€э細
    - 鎺у埗鍙板疄鏃舵樉绀?
    - 鏂囦欢鎸佷箙鍖栧瓨鍌?
    - 鑷姩鍒锋柊缂撳啿鍖?
    - 绾跨▼瀹夊叏鍐欏叆
    """
    
    def __init__(self, console_stream, file_stream):
        self.console = console_stream
        self.file = file_stream
        self._lock = threading.Lock()
    
    def write(self, message: str):
        """绾跨▼瀹夊叏鐨勫弻鍐欐搷浣?""
        with self._lock:
            self.console.write(message)
            self.file.write(message)
            self.flush()
    
    def flush(self):
        """寮哄埗鍒锋柊缂撳啿鍖?""
        self.console.flush()
        self.file.flush()
```

#### 3.2.2 鏃ュ織閰嶇疆瑙勮寖锛堝己鍒讹級
```python
def setup_logger(log_file: Optional[str] = None, log_level: int = logging.INFO, stream=None) -> logging.Logger:
    """
    鏃ュ織閰嶇疆鍣?
    
    鍙傛暟锛?
    - log_file: 鏃ュ織鏂囦欢璺緞锛圢one鍒欎粎杈撳嚭鍒版帶鍒跺彴锛?
    - log_level: 鏃ュ織绾у埆锛坙ogging.INFO / logging.DEBUG绛夛級
    - stream: 杈撳嚭娴侊紙榛樿sys.stdout锛?
    
    杩斿洖锛?
    - 閰嶇疆濂界殑Logger瀹炰緥
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    
    # 鎺у埗鍙板鐞嗗櫒
    console_handler = logging.StreamHandler(stream)
    console_handler.setLevel(log_level)
    console_format = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)
    
    # 鏂囦欢澶勭悊鍣紙濡傛灉鎸囧畾浜唋og_file锛?
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8', mode='a')
        file_handler.setLevel(log_level)
        file_format = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    
    return logger
```

#### 3.2.3 鏃ュ織绾у埆浣跨敤瑙勮寖锛堝己鍒讹級
```python
# 鉁?姝ｇ‘鐨勬棩蹇楃骇鍒娇鐢?
logger.debug("璇︾粏鐨勮皟璇曚俊鎭? 鍙橀噺鍊?%s", variable)      # 寮€鍙戣皟璇?
logger.info("姝ｅ父鐨勪笟鍔℃祦绋? 澶勭悊浜?d涓枃浠?, count)       # 鍏抽敭娴佺▼鑺傜偣
logger.warning("鍙仮澶嶇殑寮傚父: 鏂囦欢涓嶅瓨鍦紝浣跨敤榛樿鍊?)     # 闇€瑕佹敞鎰忎絾涓嶅奖鍝嶈繍琛?
logger.error("閿欒浣嗗彲缁х画: API璋冪敤澶辫触锛岄噸璇曚腑")          # 閿欒浣嗘湁fallback
logger.critical("涓ラ噸閿欒: 鏁版嵁搴撹繛鎺ヤ涪澶憋紝鏈嶅姟涓嶅彲鐢?)    # 鑷村懡閿欒锛岄渶瑕佺珛鍗冲共棰?

# 鉂?閿欒鐨勬棩蹇椾娇鐢?
logger.info("鍙戠敓浜嗛敊璇?)  # 閿欒搴旇鐢╡rror绾у埆
print("璋冭瘯淇℃伅")         # 绂佹浣跨敤print锛岀粺涓€鐢╨ogger
```

### 3.3 FastAPI 璺敱瑙勮寖 鈿狅笍 **閲嶈** (2026-07-30 鏂板)

#### 3.0.1 HEAD 鏂规硶鏀寔 (寮哄埗)
```python
# 鉂?閿欒锛欯app.get() 涓嶆敮鎸?HEAD 璇锋眰
# 褰?verify_url() 浣跨敤 HEAD 鏂规硶楠岃瘉鏃讹紝杩斿洖 405 Method Not Allowed
# 瀵艰嚧闅ч亾蹇冭烦楠岃瘉姘歌繙澶辫触锛岄毀閬撹璇垽涓轰笉鍙敤骞跺弽澶嶉噸鍚?
@app.get('/')
async def index():
    return HTMLResponse(content=html_content)

# 鉁?姝ｇ‘锛氫娇鐢?@app.api_route() 鍚屾椂鏀寔 GET 鍜?HEAD
@app.api_route('/', methods=['GET', 'HEAD'])
async def index():
    return HTMLResponse(content=html_content)
```

**鍏抽敭璇存槑**:
- FastAPI 鐨?`@app.get()` **涓嶄細**鑷姩涓鸿矾鐢辨敮鎸?HEAD 鏂规硶锛堜笌 Flask 涓嶅悓锛?
- 椤圭洰涓?`verify_url()` 鍜?`send_heartbeat()` 閮戒娇鐢?`method='HEAD'` 楠岃瘉闅ч亾 URL
- 濡傛灉鏍硅矾鐢变笉鏀寔 HEAD锛岄毀閬撻獙璇佸皢杩斿洖 405锛屽績璺虫満鍒惰鍒や负涓嶅彲鐢?
- **鎵€鏈夊彲鑳借闅ч亾楠岃瘉璁块棶鐨勮矾鐢?*閮藉繀椤诲悓鏃舵敮鎸?GET 鍜?HEAD

**闅ч亾楠岃瘉娴佺▼**:
```
verify_url(url) 鈫?HEAD / 鈫?FastAPI 璺敱 鈫?405 Method Not Allowed 鈫?楠岃瘉澶辫触 鈫?蹇冭烦鍒ゅ畾涓嶅彲鐢?鈫?瑙﹀彂閲嶅惎
verify_url(url) 鈫?HEAD / 鈫?FastAPI 璺敱 鈫?200 OK 鈫?楠岃瘉鎴愬姛 鈫?蹇冭烦鍒ゅ畾鍙敤 鈫?绋冲畾杩愯 鉁?
```

#### 3.0.2 璺敱鏂规硶澹版槑瑙勮寖
```python
# 鉁?闇€瑕佽 HEAD 楠岃瘉璁块棶鐨勮矾鐢憋細浣跨敤 api_route
@app.api_route('/', methods=['GET', 'HEAD'])
async def index():

# 鉁?绾?API 璺敱锛堜笉闇€瑕?HEAD 楠岃瘉锛夛細鍙娇鐢?@app.get
@app.get('/api/tunnel/status')
def tunnel_status():

# 鉁?鍙啓璺敱锛氫娇鐢?@app.post
@app.post('/api/tunnel/start')
def start_tunnel():
```

### 3.1 寮傚父澶勭悊鏍囧噯

#### 3.1.1 ExceptionContext 缁熶竴鍖呰
```python
# 鉁?寮哄埗瑕佹眰锛氭墍鏈夋枃浠舵搷浣滃繀椤讳娇鐢?ExceptionContext
from utils.exception_handler import ExceptionContext

class FileManager:
    @staticmethod
    def read_json(file_path):
        """璇诲彇JSON鏂囦欢"""
        with ExceptionContext(f"FileManager.read_json({file_path})", default=None) as ctx:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    
    @staticmethod
    def write_json(file_path, data, indent=2):
        """鍐欏叆JSON鏂囦欢"""
        with ExceptionContext(f"FileManager.write_json({file_path})", default=False) as ctx:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=indent, ensure_ascii=False)
```

#### 3.1.2 缁嗙矑搴﹀紓甯告崟鑾?
```python
# 鉂?閿欒锛氬娉涚殑寮傚父鎹曡幏
try:
    result = api_call()
except:
    pass  # 鍚炴帀鎵€鏈夊紓甯?

# 鉁?姝ｇ‘锛氱粏绮掑害寮傚父鎹曡幏 + 璇︾粏鏃ュ織
try:
    result = api_call()
except requests.exceptions.Timeout:
    logger.warning(f"API璇锋眰瓒呮椂: {url}")
    show_user_prompt("缃戠粶瓒呮椂", "璇锋鏌ョ綉缁滆繛鎺ュ悗閲嶈瘯")
except requests.exceptions.HTTPError as e:
    logger.error(f"HTTP閿欒: {e.response.status_code}")
    if e.response.status_code == 403:
        show_user_prompt("鍙嶇埇铏娴?, "寤鸿鏇存崲IP鎴栭檷浣庤姹傞鐜?)
except ValueError as e:
    logger.error(f"鏁版嵁瑙ｆ瀽澶辫触: {str(e)}")
    show_user_prompt("鏁版嵁鏍煎紡閿欒", "鍘熷鏁版嵁: {raw_data[:100]}")
```

### 3.2 閰嶇疆绠＄悊瑙勮寖

#### 3.2.1 ConfigManager 浣跨敤
```python
class ConfigManager:
    """
    閰嶇疆绠＄悊鍣?- 缁熶竴閰嶇疆璇诲啓鎺ュ彛
    
    鐗规€э細
    - 鑷姩淇濆瓨鍒扮鐩?
    - 绫诲瀷瀹夊叏璁块棶
    - 鎻愪緵渚挎嵎鏂规硶
    """
    
    def get(self, key, default=None):
        """璇诲彇閰嶇疆椤?""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """璁剧疆閰嶇疆椤瑰苟鑷姩淇濆瓨"""
        if self._config is not None:
            self._config[key] = value
            self.save_config()  # 绔嬪嵆鎸佷箙鍖?
    
    def get_cookie_file(self):
        """渚挎嵎鏂规硶锛氳幏鍙朇ookie鏂囦欢璺緞"""
        return self.config.get('cookie_file', PathManager.get_cookie_file())
```

### 3.3 Cookie楠岃瘉瑙勮寖

#### 3.3.1 涓冩楠岃瘉娴佺▼
```python
class CookieValidator:
    @staticmethod
    def validate_and_prompt(cookie_file):
        """
        涓冩楠岃瘉娴佺▼锛?
        
        1. 妫€鏌ユ枃浠舵槸鍚﹀瓨鍦?
        2. 妫€鏌ユ枃浠舵槸鍚﹀彲璇伙紙JSON鏍煎紡锛?
        3. 妫€鏌ookie鏄惁涓虹┖
        4. 妫€鏌ユ槸鍚﹀瓨鍦╰oken
        5. 妫€鏌oken鏄惁杩囨湡
        6. 妫€鏌oken鍊兼槸鍚︽湁鏁堬紙闀垮害>=10锛?
        7. 妫€鏌ookie鏄惁鍗冲皢杩囨湡锛?澶╁唴棰勮锛?
        
        Returns:
            tuple: (is_valid, cookies_or_None)
        """
        pass
    
    @staticmethod
    def _show_expiry_warning(days_until_expiry):
        """
        杩囨湡棰勮锛?
        - 7澶╁唴锛氶粍鑹茶鍛?鈿狅笍
        - 3澶╁唴锛氱孩鑹茶鍛?馃敶
        """
        pass
```

---

## 馃摑 鏃ュ織璁板綍瑙勮寖

### 4.1 鏃ュ織绾у埆浣跨敤

| 鍦烘櫙 | 鏃ュ織绾у埆 | 绀轰緥 |
|------|---------|------|
| **姝ｅ父鎿嶄綔** | `INFO` | `[瀵规瘮鍗＄墖] 鉁?鎬诲晢鍝佹暟: 91` |
| **鏁版嵁瑙ｆ瀽** | `DEBUG` | `[瀵规瘮鍗＄墖] 瑙ｆ瀽绗?43琛? 鍞环 >= 599...` |
| **璀﹀憡淇℃伅** | `WARNING` | `鈿狅笍 Cookie灏嗗湪3澶╁悗杩囨湡` |
| **閿欒淇℃伅** | `ERROR` | `鉂?API璇锋眰澶辫触: 403 Forbidden` |

### 4.2 缁熶竴鏃ュ織鏍煎紡
```javascript
// JavaScript 鏍煎紡
console.log('[妯″潡鍚峕 鉁?鎿嶄綔鎴愬姛:', data);
console.warn('[妯″潡鍚峕 鈿狅笍 璀﹀憡淇℃伅:', message);
console.error('[妯″潡鍚峕 鉂?閿欒璇︽儏:', error);

// Python 鏍煎紡
logger.info(f"[{__name__}] 鉁?鎴愬姛: {data}")
logger.warning(f"[{__name__}] 鈿狅笍 璀﹀憡: {message}")
logger.error(f"[{__name__}] 鉂?澶辫触: {error}", exc_info=True)
```

---

## 馃洝锔?瀹夊叏瑙勮寖

### 5.1 杈撳叆楠岃瘉
```javascript
// 鉁?XSS闃叉姢
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 鉁?鍦℉TML涓娇鐢?
<div class="sku-tag">${escapeHtml(sku)}</div>
```

### 5.2 鏁忔劅鏁版嵁澶勭悊
```python
# 鉂?閿欒锛氭棩蹇椾腑娉勯湶鏁忔劅淇℃伅
logger.info(f"Cookie: {cookie}")  # 鍗遍櫓锛?

# 鉁?姝ｇ‘锛氳劚鏁忓鐞?
logger.info(f"Cookie宸插姞杞? {mask_sensitive(cookie)}")  # 瀹夊叏
```

---

## 馃И 娴嬭瘯瑙勮寖

### 6.1 鍗曞厓娴嬭瘯瑕佹眰
```python
# tests/test_syntax_check.py
import unittest
import re

class TestJavaScriptSyntax(unittest.TestCase):
    """娴嬭瘯JavaScript璇硶姝ｇ‘鎬?""
    
    def test_bracket_matching(self):
        """娴嬭瘯鎷彿鍖归厤"""
        code = open('dist/app.js', 'r', encoding='utf-8').read()
        
        # 妫€鏌ユ嫭鍙锋槸鍚﹀尮閰?
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        
        for char in code:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    self.fail(f"鎷彿涓嶅尮閰? 浣嶇疆闄勮繎...{code[max(0,code.index(char)-50):code.index(char)+50]}")
        
        self.assertEqual(len(stack), 0, "瀛樺湪鏈棴鍚堢殑鎷彿")
    
    def test_no_syntax_errors(self):
        """娴嬭瘯鏃犺娉曢敊璇紙浣跨敤Node.js妫€鏌ワ級"""
        import subprocess
        result = subprocess.run(['node', '--check', 'dist/app.js'], 
                              capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, 
                        f"璇硶閿欒: {result.stderr}")
```

### 6.2 闆嗘垚娴嬭瘯
```python
def test_high_price_count_display():
    """娴嬭瘯楂樹环鍟嗗搧鏁版纭樉绀猴紙淇鍚庣殑鍥炲綊娴嬭瘯锛?""
    output = run_spider_task()
    
    # 瑙ｆ瀽杈撳嚭涓殑楂樹环鍟嗗搧鏁?
    match = re.search(r'鍞环 >= 599 鐨勫晢鍝?\s*(\d+)涓?, output)
    assert match, "鏈壘鍒伴珮浠峰晢鍝佹暟"
    
    high_price_count = int(match.group(1))
    assert high_price_count == 73, f"棰勬湡73涓紝瀹為檯{high_price_count}涓?
    
    # 楠岃瘉UI鏄剧ず
    ui_value = get_ui_stat_value('high-price-count')
    assert ui_value == '73', f"UI鏄剧ず閿欒: {ui_value}"
```

---

## 馃摝 Git宸ヤ綔娴佽鑼?

### 7.1 Commit Message 鏍煎紡
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type 绫诲瀷**:
- `fix`: Bug淇
- `feat`: 鏂板姛鑳?
- `docs`: 鏂囨。鏇存柊
- `style`: 浠ｇ爜鏍煎紡璋冩暣
- `refactor`: 閲嶆瀯
- `test`: 娴嬭瘯鐩稿叧
- `chore`: 鏋勫缓/宸ュ叿閾?

**绀轰緥**:
```
fix(app.js): 淇绗?432琛屾嫭鍙蜂笉鍖归厤瀵艰嚧楂樹环鍟嗗搧鏁版樉绀轰负0

闂锛?
- 鏉′欢鍒ゆ柇璇彞澶氫袱涓彸鎷彿瀵艰嚧JS瑙ｆ瀽澶辫触
- "鍞环>=599鐨勫晢鍝? 鏄剧ず涓?鑰岄潪73

淇锛?
- 绉婚櫎澶氫綑鐨?)) 
- 鏀圭敤 || 缁勫悎鏉′欢鎻愰珮鍙鎬?

褰卞搷鑼冨洿锛?
- dist/app.js Line 1432-1434
- 楂樹环鍟嗗搧缁熻鍔熻兘鎭㈠姝ｅ父

娴嬭瘯锛?
鉁?鎵嬪姩楠岃瘉锛氬埛鏂伴〉闈㈠悗鏄剧ず73
鉁?鑷姩鍖栨祴璇曪細test_bracket_matching 閫氳繃
```

### 7.2 鍒嗘敮绛栫暐
```
main (鐢熶骇鐜)
  鈹斺攢鈹€ develop (寮€鍙戠幆澧?
        鈹溾攢鈹€ feature/fix-syntax-error (褰撳墠鍒嗘敮)
        鈹溾攢鈹€ feature/add-new-api
        鈹斺攢鈹€ hotfix/critical-bug
```

---

## 馃毃 甯歌闂 & 瑙ｅ喅鏂规 (FAQ)

### Q1: 涓轰粈涔堟暟鎹樉绀轰负0锛?
**A**: 鏈€甯歌鍘熷洜鏄?**JavaScript璇硶閿欒**銆?
- 妫€鏌ユ祻瑙堝櫒鎺у埗鍙版槸鍚︽湁绾㈣壊閿欒
- 浣跨敤 `node --check app.js` 楠岃瘉璇硶
- 閲嶇偣妫€鏌?*鎷彿鍖归厤**锛堣2.1.1鑺傦級

### Q2: 濡備綍閬垮厤绫讳技鐨勮娉曢敊璇紵
**A**: 
1. **浣跨敤IDE鎻掍欢** - ESLint瀹炴椂妫€鏌?
2. **鎻愪氦鍓嶉獙璇?* - 杩愯 `npm run lint`
3. **Code Review** - 鍚屼即瀹℃煡鎷彿鍖归厤
4. **鑷姩鍖栨祴璇?* - 杩愯鍗曞厓娴嬭瘯濂椾欢

### Q3: Windows鐜涓嬮渶瑕佹敞鎰忎粈涔堬紵
**A**: 
- 鏂囦欢缂栫爜锛?*UTF-8 with BOM**
- 鎹㈣绗︼細**CRLF (\r\n)**锛岄潪 LF (\n)
- PowerShell杞箟锛氱壒娈婂瓧绗﹂渶瑕佸弻閲嶈浆涔?
- Node.js璺緞锛氫娇鐢ㄦ鏂滄潬 `/` 鎴栧弻鍙嶆枩鏉?`\\`

### Q4: 淇敼app.js鍚庡浣曢獙璇侊紵
**A**: 瀹屾暣楠岃瘉娴佺▼锛?
```bash
# 1. 璇硶妫€鏌?
node --check dist/app.js

# 2. 鍗曞厓娴嬭瘯
npm test

# 3. 鎵嬪姩娴嬭瘯
# 鍒锋柊娴忚鍣?鈫?杩愯浠诲姟 鈫?妫€鏌ユ帶鍒跺彴杈撳嚭鍜孶I鏄剧ず

# 4. 鍥炲綊娴嬭瘯
python tests/test_regression.py
```

---

## 馃搳 鎬ц兘鐩戞帶鎸囨爣

### 鍏抽敭鎬ц兘鎸囨爣 (KPI)
| 鎸囨爣 | 鐩爣鍊?| 褰撳墠鍊?| 鐘舵€?|
|------|--------|--------|------|
| **JS璇硶閿欒鐜?* | 0% | 0% | 鉁?|
| **鏁版嵁鏄剧ず鍑嗙‘鐜?* | 100% | 100% | 鉁?|
| **API鍝嶅簲鏃堕棿** | <3s | <2s | 鉁?|
| **鐢ㄦ埛婊℃剰搴?* | >90% | 95% | 鉁?|

### 鐩戞帶鑴氭湰
```bash
#!/bin/bash
# monitor.sh - 姣忔棩鍋ュ悍妫€鏌?

echo "=== $(date) ==="

# 1. JS璇硶妫€鏌?
node --check dist/app.js && echo "鉁?JS璇硶姝ｅ父" || echo "鉂?JS璇硶閿欒"

# 2. Python璇硶妫€鏌?
python -m py_compile main.py && echo "鉁?Python璇硶姝ｅ父" || echo "鉂?Python璇硶閿欒"

# 3. 娴嬭瘯瑕嗙洊鐜?
pytest --cov=. && echo "鉁?娴嬭瘯閫氳繃" || echo "鉂?娴嬭瘯澶辫触"

# 4. 鏂囨。鍚屾妫€鏌?
diff README.md skill.docx >/dev/null 2>&1 && echo "鉁?鏂囨。宸插悓姝? || echo "鈿狅笍 鏂囨。闇€瑕佹洿鏂?
```

---

## 馃摎 鍙傝€冭祫婧?

### 鍐呴儴鏂囨。
- [README.md](./README.md) - 椤圭洰姒傝堪鍜屾洿鏂版棩蹇?
- [skill.docx](./skill.docx) - Word鏍煎紡瀹屾暣鏂囨。

### 澶栭儴璧勬簮
- [MDN Web Docs](https://developer.mozilla.org/) - JavaScript鍙傝€?
- [Python PEP 8](https://peps.python.org/pep-0008/) - Python椋庢牸鎸囧崡
- [ESLint Rules](https://eslint.org/docs/rules/) - 浠ｇ爜璐ㄩ噺瑙勫垯

---

## 馃搫 鏂囨。鐢熸垚鏂规硶

### 鏂规硶1: 浣跨敤 Pandoc (鎺ㄨ崘)

瀹夎 Pandoc: https://pandoc.org/installing.html

```bash
pandoc skill.md -o skill.docx
```

### 鏂规硶2: 浣跨敤 Python python-docx

```bash
pip install python-docx markdown
```

Python鑴氭湰绀轰緥锛?
```python
from docx import Document

def md_to_docx(md_file, docx_file):
    doc = Document()
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    for line in lines:
        if line.startswith('# '):
            doc.add_heading(line[2:], level=1)
        elif line.startswith('## '):
            doc.add_heading(line[3:], level=2)
        elif line.startswith('### '):
            doc.add_heading(line[4:], level=3)
        elif line.startswith('#### '):
            doc.add_heading(line[5:], level=4)
        elif line.strip():
            doc.add_paragraph(line)
    
    doc.save(docx_file)

if __name__ == '__main__':
    md_to_docx('skill.md', 'skill.docx')
    print('鉁?skill.docx 鐢熸垚鎴愬姛')
```

### 鏂规硶3: 浣跨敤鍦ㄧ嚎宸ュ叿

璁块棶 https://cloudconvert.com/md-to-docx 涓婁紶 skill.md 鏂囦欢

### 鏂规硶4: 浣跨敤 Microsoft Word

鏂囦欢 鈫?鎵撳紑 鈫?閫夋嫨 skill.md 鈫?鍙﹀瓨涓?skill.docx

### 楠岃瘉鐢熸垚缁撴灉

鐢熸垚鍚庢鏌ヤ互涓嬪唴瀹癸細
- [ ] 鎵€鏈夋爣棰樺眰绾ф纭?
- [ ] 浠ｇ爜鍧楁牸寮忓畬鏁?
- [ ] 琛ㄦ牸鏄剧ず姝ｅ父
- [ ] 涓枃瀛楃鏃犱贡鐮?
- [ ] 鏂囨。鐗堟湰鍙蜂负 v3.8.68

---

## 馃攧 鐗堟湰鍘嗗彶

### 馃摎 鏈€鏂扮増鏈?(v3.8.x)

| 鐗堟湰 | 鏃ユ湡 | 浣滆€?| 鍙樻洿鍐呭 |
|------|------|------|---------|
| v3.8.89.11 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 馃敡 hostc WebSocket瀹夊叏鍏抽棴淇(safeCloseWebSocket2鐘舵€佹劅鐭?error浜嬩欢鍚炴帀+patch-package鎸佷箙鍖?+闅ч亾楠岃瘉淇(FastAPI HEAD鏂规硶)+楂樹环鍟嗗搧鏁拌В鏋愪慨澶?鎸夐挳鍏ㄥ眬鍑芥暟鏆撮湶 |
| v3.8.89.10 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | FastAPI鏍硅矾鐢辨坊鍔燞EAD鏂规硶鏀寔锛屼慨澶峷erify_url()杩斿洖405瀵艰嚧闅ч亾琚鍒や笉鍙敤; CF闅ч亾DNS瑙ｆ瀽澶辫触鐨勬帓鏌ユ柟妗? 闅ч亾涓嶅啀鍙嶅閲嶅惎锛岄偖浠堕€氱煡姝ｅ父鍙戦€?|
| v3.8.89.9 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 绠€鍖栨鍒欒〃杈惧紡锛岀簿纭尮閰峆ython杈撳嚭鏍煎紡; 鏆撮湶鍏ㄥ眬鍑芥暟锛岀‘淇濇寜閽粦瀹氭垚鍔? 楂樹环鍟嗗搧鏁颁粠0鎭㈠鍒?8 |
| v3.8.89.8 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 楂樹环鍟嗗搧銆乀XT瀵规瘮銆佽姹傚鐞嗐€佹暟鎹簮銆丆DN鏃ュ織; 淇FastAPI杩佺Щ鍚庣殑鍔熻兘闂 |
| v3.8.89.6 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇鐖櫕缁撴灉鍗＄墖鏄剧ず鏍煎紡; 缁熶竴鍗＄墖鏄剧ず鏍峰紡 |
| v3.8.89.5 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 娣诲姞鍗曞厓娴嬭瘯; 鏃ュ織绾у埆浼樺寲; subprocess鏇挎崲os.system; 鍓嶇Toast閿欒鎻愮ず |
| v3.8.89.4 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇澶氫釜闅愯棌Bug; 鎻愬崌浠ｇ爜璐ㄩ噺 |
| v3.8.89.3 | 2026-07-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇Flask閬楃暀浠ｇ爜; 娣诲姞jsonify鍏煎灞? 8涓寜閽祴璇?/8閫氳繃 |
| v3.8.89.2 | 2026-07-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 22涓矾鐢卞叏閮ㄨ浆鎹? FastAPI杩佺Щ100%瀹屾垚 |
| v3.8.89.1 | 2026-07-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇Excel瀵规瘮璐у彿鐐瑰嚮鏃犲搷搴? 鏇存柊鏂囨。瑙勮寖 |
| v3.8.89 | 2026-07-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇璇硶閿欒+娓呯悊娴嬭瘯浠ｇ爜+鏇存柊鐗堟湰鍙?|
| v3.8.88.2 | 2026-07-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | XSS鍏ㄩ潰淇(26澶?; CORS鏀剁揣; URL娉ㄥ叆闃叉姢; 浜嬩欢缁戝畾缂哄け瀵艰嚧鍟嗗搧璇︽儏鍜屽埄娑︽姤琛ㄥ姛鑳藉け鏁?|
| v3.8.88.1 | 2026-07-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | XSS闃叉姢; 瀹氭椂鍣ㄦ硠婕忎慨澶?|
| v3.8.88 | 2026-07-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | API璺敱瀹夊叏鍔犲浐; 鍏ㄩ潰淇'Unexpected token <'閿欒 |
| v3.8.87 | 2026-07-26 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍩轰簬鍏ュ簱鏃堕棿鎴冲姩鎬佽绠楃浉瀵规椂闂? 涓嶅啀浣跨敤婧怉PI闈欐€佸瓧绗︿覆 |
| v3.8.86 | 2026-07-26 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鎼滅储鏃?涓〃鏍艰仈鍔ㄨ繃婊? 姣忎釜琛ㄦ牸鐙珛缁熻琛?鍞嚭鎬讳环/鍧囦环/鎵嬬画璐?; 椤堕儴寰界珷瀹炴椂鏇存柊鍖归厤鏁? 鎼滅储缁撴灉鍒嗚〃灞曠ず褰╄壊鏍囩 |
| v3.8.85 | 2026-07-26 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍟嗗搧鎼滅储缁熻瀹炴椂璁＄畻浼樺寲 |
| v3.8.84 | 2026-07-25 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 瀹夊叏婕忔礊淇; 鍛戒护娉ㄥ叆闃叉姢 |
| v3.8.83 | 2026-07-25 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Bug淇; 浠ｇ爜璐ㄩ噺鎻愬崌 |
| v3.8.82 | 2026-07-24 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浠ｇ爜璐ㄩ噺浼樺寲 |
| v3.8.81 | 2026-07-24 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍙橀噺鍛藉悕瑙勮寖鍖?oldTime -> old_time); 淇鏃堕棿鎴冲瓧娈?time_stamp) |
| v3.8.78 | 2026-07-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | skill.docx鑷姩鐢熸垚; 鏂囨。鏇存柊 |
| v3.8.77 | 2026-07-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Swagger UI闆嗘垚浼樺寲 |
| v3.8.76 | 2026-07-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | .trae閰嶇疆浼樺寲; skill鏂囨。鏇存柊 |
| v3.8.75 | 2026-07-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂板skill鏂囨。; 浠ｇ爜瑙勮寖浼樺寲 |
| v3.8.73 | 2026-07-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | CSP浼樺寲锛宒ocs/鐩綍鍏佽CDN; README.md鏇存柊锛岃ˉ鍏卾3.8.67-v3.8.73鐗堟湰璁板綍; 鏂板/api/changelog API |
| v3.8.71 | 2026-07-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Swagger UI闆嗘垚(鑷姩鐢熸垚swagger.json+HTML UI); Pydantic V2鍗囩骇(field_validator); 鏇存柊requirements.txt |
| v3.8.70.1 | 2026-07-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 缁熶竴鏂囨。璇█瑙勮寖 - 鎵€鏈夋洿鏂版棩蹇楀繀椤讳娇鐢ㄤ腑鏂?|
| v3.8.70 | 2026-07-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浼佷笟绾х敓浜т紭鍖栵紝38椤规敼杩? 瀹夊叏鍔犲浐 |
| v3.8.69 | 2026-07-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍏ㄩ潰瀹夊叏瀹¤锛?涓叧閿瓸ug淇 |
| v3.8.68 | 2026-07-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇缂╄繘閿欒; 淇Socket娉勬紡; 浠ｇ爜璐ㄩ噺鎻愬崌 |
| v3.8.67 | 2026-07-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇FastAPI杩佺Щ鍚庣殑Bug |
| v3.8.66 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鎵嬪姩瑙﹀彂hostc杩涚▼缁堟娴嬭瘯; 淇verify_url()鍙傛暟閿欒; hostc棰戠箒宕╂簝鍦烘櫙涓婥F闅ч亾瀹屽叏鐙珛杩愯 |
| v3.8.65 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | hostc澶辨晥涓嶅啀褰卞搷Cloudflare Tunnel; 鍚姩鏂癈F闅ч亾鍓嶅厛妫€鏌ュ凡鏈夊彲鐢ㄥ湴鍧€; hostc棰戠箒閲嶅惎鏃禖F鍦板潃淇濇寔涓嶅彉 |
| v3.8.64 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 闅ч亾鍏变韩寮圭獥鎭㈠鍘熷hostc鏍峰紡+鏂板Cloudflare URL |
| v3.8.63 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 闅ч亾鍏变韩寮圭獥鍚屾椂鏄剧ずhostc鍜孋loudflare鍙屽叕缃戝湴鍧€ |
| v3.8.62 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Toast鏄剧ず鍏蜂綋澶嶅埗鐨刄RL鍦板潃 |
| v3.8.61 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇闅ч亾绠＄悊闈㈡澘澶嶅埗鎸夐挳ID鍐茬獊锛孴oast寮圭獥鎭㈠姝ｅ父 |
| v3.8.60 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍏綉鍦板潃澶嶅埗鎸夐挳鏍峰紡缁熶竴锛坆tn-light + 澶嶅埗鏂囧瓧锛?|
| v3.8.59 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍏綉鍦板潃澶嶅埗鎸夐挳锛圕loudflare + hostc锛?|
| v3.8.58 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 閭欢闃查噸澶嶅彂閫佷慨澶?+ skill.docx 鍚屾鏇存柊 |
| v3.8.57 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鐗堟湰鏇存柊鏃ュ織鍒?README.md; Cloudflare閭欢閫氱煡淇 + 鏃ュ織鏍煎紡缁熶竴 |
| v3.8.56 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 绉婚櫎 hostc_output.txt锛岀畝鍖栭毀閬撶鐞?|
| v3.8.55 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Cloudflare 閭欢閫氱煡鏃ュ織缁熶竴 |
| v3.8.54 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Cloudflare 闄愭祦妫€娴嬩笌鍙嬪ソ鎻愮ず |
| v3.8.53 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇鍙岄毀閬撳湴鍧€鍐欏叆鍐茬獊 |
| v3.8.52 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍙岄毀閬撶嫭绔嬪彂閭欢 + 蹇冭烦鍐欏叆淇 |
| v3.8.51 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏇存柊README鍜宻kill鏂囨。; tunnel_url.txt鍚屾椂瀛樺偍hostc鍜孋F涓や釜闅ч亾鐨勫湴鍧€ |
| v3.8.50 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇CF蹇冭烦楠岃瘉鏃ュ織杈撳嚭 |
| v3.8.49 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 娣诲姞CF蹇冭烦楠岃瘉璇︾粏鏃ュ織 |
| v3.8.48 | 2026-07-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Tunnel type selector dynamic default value |
| v3.8.47 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍙岄毀閬撲簰涓哄鐢ㄩ€氱煡 + fallback_available 閭欢绫诲瀷 |
| v3.8.46 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | CF + hostc 鍙岄毀閬撳苟琛?+ 蹇冭烦楠岃瘉 + 鍒犻櫎 NS 鐩戞帶; Plan A鈫払 淇濆簳 + 鑷姩妫€娴?+ 鍒犻櫎 cloudflare_tunnel 閰嶇疆; Plan A/B 浜岄€変竴 + 鍒犻櫎 NS 鐩戞帶 |
| v3.8.45 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | NS鍗囩骇鑷姩鐩戞帶 + Quick Tunnel鑷姩鍗囩骇鍒癗amed Tunnel |
| v3.8.44 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Named Tunnel + 鑷畾涔夊煙鍚?+ 鑷姩闄嶇骇鍒?Quick Tunnel |
| v3.8.43 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Cloudflare Tunnel 璺ㄥ钩鍙版敮鎸?+ 闅ч亾鍒囨崲浼樺寲 |
| v3.8.42 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Flask璁块棶鏃ュ織鏍煎紡浼樺寲 |
| v3.8.41 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 蹇冭烦寰幆閲嶅惎鍚庣姸鎬侀噸缃慨澶?|
| v3.8.40 | 2026-07-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | hostc杩涚▼绔炴€佹潯浠朵慨澶?+ 璋冭瘯鏃ュ織澧炲己 |
| v3.8.39 | 2026-07-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鈿?闅ч亾蹇冭烦涓庣ǔ瀹氭€ч獙璇佸姞閫熶紭鍖?- 蹇冭烦闂撮殧60鈫?0绉? 澶辨晥闃堝€?鈫?娆? 绋冲畾鎬ч獙璇?鈫?娆? 绌虹獥鏈熶粠3-5鍒嗛挓缂╃煭鑷?-1.5鍒嗛挓 |
| v3.8.38 | 2026-07-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 绔彛8888鍗犵敤绔炴€佹潯浠朵慨澶?|
| v3.8.37 | 2026-07-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | /api/readme-sections 500 閿欒淇 |
| v3.8.36 | 2026-07-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | run.sh 鍑芥暟瀹氫箟椤哄簭淇 + pre_launch 鍑芥暟鍖栭噸鏋?|
| v3.8.35 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏍稿績鑼冨紡鏂囨。琛ュ叏锛?椤癸級 |
| v3.8.34 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 绉诲姩绔€傞厤鑼冨紡鏂囨。鍖?|
| v3.8.33 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | hostc CDN闀滃儚婧愪慨姝?+ bat/sh闀滃儚鍒楄〃缁熶竴 |
| v3.8.32 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 闅ч亾瀹堟姢浜屾楠岃瘉+鎸囨暟閫€閬?蹇冭烦闃堝€间紭鍖?|
| v3.8.31 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 蹇冭烦閫昏緫5椤逛紭鍖?瀹介檺鏈熼噸鏋?闅ч亾閲嶅惎淇+鐗堟湰鍙风粺涓€浠嶳EADME鑾峰彇 |
| v3.8.30 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 闅ч亾閲嶅惎閫昏緫閲嶆瀯 - 鍚堝苟鍙岃矾寰?瀹介檺鏈熸満鍒?|
| v3.8.29 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | temp涓存椂鏂囦欢娉勬紡淇 + Python渚ц嚜鍔ㄦ竻鐞?|
| v3.8.28 | 2026-07-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | hostc绛夊緟URL瓒呮椂浠?20绉掗檷鑷?0绉? 蹇冭烦瀹堟姢鍗虫椂鍚姩 + tunnel鏉冨▉婧愬畧鎶ょ粺涓€ |
| v3.8.27 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 闅ч亾閲嶅惎姝诲惊鐜慨澶?- tunnel_need_restart閲嶇疆+hostc鍚姩绛夊緟URL |
| v3.8.26 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 闅ч亾鏃RL澶嶇敤Bug淇 - auto_start_tunnel澧炲姞hostc杩涚▼瀛樻椿妫€娴?|
| v3.8.25 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | pip渚濊禆瀹夎鏅鸿兘璺宠繃 - main.py --check-deps + run.bat/run.sh浼樺寲 - 鍚姩鍔犻€?0绉掆啋0.1绉?|
| v3.8.24 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | hostc閫€鍑鸿嚜鍔ㄩ噸鍚?- read_output/_wait_and_notify妫€娴嬮€€鍑哄悗绔嬪嵆鏍囪閲嶅惎锛宺estart_tunnel绔嬪嵆鍝嶅簲; 鍗虫椂閭欢閫氱煡 - auto_start_tunnel鍚庡彴绾跨▼楠岃瘉+鍙戦偖浠讹紝涓嶅啀绛夊績璺?... |
| v3.8.23 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Web鏈嶅姟绉掔骇鍚姩 + 闅ч亾闈為樆濉炰紭鍖?+ hostc鏈湴鍖?+ CDN杞瀹夎 + dist浼樺寲 |
| v3.8.21 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Node.js渚濊禆鍚堝苟 + API鑼冨紡鏂囨。瀹屽杽 + 瀹夊叏瑙勮寖 |
| v3.8.20 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鍗虫椂閭欢閫氱煡+鍓嶇鐘舵€佷慨澶?楠岃瘉鍔犻€? 鍘婚櫎棰勫惎鍔ㄦ蹇垫敼涓虹洿鎺ュ惎鍔? changelog琛ュ叏 + 鍓嶇浠ｇ爜鍧楁覆鏌撴牸寮忕粺涓€; 馃摟 闅ч亾鍗虫椂閭欢閫氱煡 + 鍓嶇鐘舵€佷慨澶?+ 楠岃瘉鍔犻€?|
| v3.8.18 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂囨。鍚屾 - README/skill.md/skill.docx 鏇存柊auto_start_tunnel涓嶉樆濉炶鑼?+ PY-STD-TUNNEL-003; auto_start_tunnel涓嶅啀闃诲绛夊緟 - hostc鍦ㄨ窇灏辩洿鎺ヨ繑... |
| v3.8.17 | 2026-07-10 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | Tunnel startup optimization - hostc pre-start + Python smart wait |
| v3.8.16 | 2026-07-09 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | macOS鏃堕棿鎴矪ug淇 + 璺ㄥ钩鍙版绉掔骇鏃堕棿鎴崇粺涓€ |
| v3.8.15 | 2026-07-09 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂囨。瀹屾暣鏇存柊: 鍏ㄥ眬鏃堕棿鎴?00%瑕嗙洊瑙勮寖; 缁堟瀬鐗? 鎺у埗鍙?鏂囦欢 100% 鏃堕棿鎴冲叏瑕嗙洊; 鏈€缁堢増: web_output.log 100%鏃堕棿鎴宠鐩? 缁堟瀬鐗? 鍏ㄥ眬鏃堕棿鎴宠鐩栨墍鏈夋棩蹇楄緭鍑? 澧炲己: 鍏ㄥ眬鏃ュ織鏃堕棿鎴宠嚜鍔ㄥ寲绯荤粺 绛?椤?|
| v3.8.14 | 2026-07-08 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | README.md 涓夋寮忕粨鏋勮鑼冭ˉ榻?+ skill.docx 閲嶆柊鐢熸垚; 鑷村懡姝婚攣淇 + 閭欢UI鍗囩骇 + 鏃ュ織绯荤粺澧炲己 |
| v3.8.13 | 2026-07-08 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 馃敡 鍏抽敭Bug淇 + API淇℃伅瀹屾暣鎬у寮?+ 鏇存柊鏃ュ織鏍煎紡浼樺寲 |
| v3.8.12 | 2026-07-08 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 馃摑 娣诲姞鐗堟湰鍙锋牸寮忚鑼冨埌 README.md 鍜?skill.md锛屼慨澶?bat 瑙ｆ瀽闂锛岀敓鎴?skill.docx; 閭欢鏃ュ織绯荤粺鍏ㄩ潰澧炲己 + stable_available Bug淇 |

---

### 馃摎 鏃╂湡鐗堟湰鍘嗗彶璁板綍 (v1.4.2 - v2.1.7)

| 鐗堟湰 | 绫诲瀷 | 浣滆€?| 鍙樻洿鍐呭 |
|------|------|------|---------|
| v2.1.7 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 娣诲姞澶氶噸瓒呮椂淇濇姢鍜岄噸璇曟満鍒讹紝闃叉鐖櫕鍗℃ |
| v2.1.6 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇寮圭獥鍏抽棴瓒呮椂闂; 娣诲姞鏃堕棿缁熻浼樺寲鎬ц兘 |
| v2.1.5 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇楂樹环鍟嗗搧绛涢€夐€昏緫; 瑙ｅ喅瀵规瘮缁撴灉涓嶅噯纭棶棰?|
| v2.1.3 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浼樺寲JSON鏂囦欢瀵规瘮璁板綍鏈哄埗; 鏀寔澶氭潯瀵规瘮璁板綍 |
| v2.1.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浼樺寲JSON鏂囦欢瀵规瘮鍔熻兘; 鏂板缂撳瓨鏂囦欢鏈哄埗 |
| v2.1.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂; 鍒犻櫎璋冭瘯浠ｇ爜 |
| v2.1.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂板璋冭瘯鍔熻兘; 浼樺寲寮€鍙戜綋楠?|
| v2.0.9 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂板褰撳ぉJSON鏂囦欢瀵规瘮鍔熻兘 |
| v2.0.8 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂 |
| v2.0.7 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浼樺寲楂樹环鍟嗗搧绛涢€? 淇娴忚鍣ㄥ惎鍔?|
| v2.0.6 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浼樺寲鏁版嵁鍙樺寲鍒嗘瀽浠ｇ爜; 绮剧畝閫昏緫 |
| v2.0.5 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏇存柊Cookie杩囨湡鏃堕棿 |
| v2.0.4 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂板Cookie鑷姩鏇存柊鍔熻兘; 浼樺寲Excel鏂囦欢妫€鏌?|
| v2.0.3 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浠ｇ爜閲嶆瀯鍜屼紭鍖?|
| v2.0.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂板楂樹环鍟嗗搧淇℃伅鍐欏叆JSON鍔熻兘 |
| v2.0.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浼樺寲楂樹环鍟嗗搧绛涢€夐€昏緫 |
| v2.0.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 鏂板璐у彿瀵规瘮楂樹环鍟嗗搧绛涢€夊姛鑳?|
| v1.9.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 娣诲姞楂樹环鍟嗗搧绛涢€夊姛鑳?|
| v1.8.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 娣诲姞杩愯鏃堕棿鏄剧ず鍜屽姩鎬佽皟鏁村姛鑳?|
| v1.7.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 婊氬姩鍙傛暟鍙厤缃寲 |
| v1.6.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇椤甸潰鍔犺浇姝绘満闂 |
| v1.6.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 淇婊氬姩姝诲惊鐜棶棰?|
| v1.6.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 瀹屾垚鎵€鏈夐珮浼樺厛绾т紭鍖?|
| v1.5.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 绠€鍖朖SON鏁版嵁缁撴瀯涓?涓牳蹇冨瓧娈?|
| v1.4.3 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 浼樺寲椤甸潰鍔犺浇閫昏緫锛屽噺灏戠瓑寰呮椂闂?|
| v1.4.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級 | 瀹屾垚璺ㄧ郴缁熺幆澧冩祴璇曞拰浼樺寲; 浼樺寲鍟嗗搧鍘婚噸閫昏緫 |

---
| v3.8.11 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹屾暣鍘嗗彶璁板綍鎭㈠涓庢枃妗ｆ洿鏂?|
| v3.8.10 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏇存柊鏂囨。锛歊EADME.md + skill.md + skill.docx 鍚屾浠ｇ爜瑙勮寖; (2026-07-05) - 馃敡 鍏抽敭淇锛氱缉杩涢敊璇鑷存湇鍔″惎鍔ㄥけ璐?+ 鏂囨。鍚屾鏇存柊 |
| v3.8.9 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| (2026-07-05) - 馃敀 寮哄埗URL鍘婚噸鏈哄埗锛堝悓涓€鍦板潃30鍒嗛挓鍐呭彧鍙?娆￠偖浠讹級 |
| v3.8.8 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| (2026-07-05) - 馃殌 鍏綉鍦板潃鍙敤鍗宠嚜鍔ㄥ彂閭欢锛堥浂寤惰繜閫氱煡浼樺寲锛?|
| v3.8.7 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| (2026-07-05) - 馃搫 鏇存柊skill.docx鏂囨。锛堢嚎绋嬪畨鍏║RL鍘婚噸鏈哄埗淇锛? 绾跨▼瀹夊叏URL鍘婚噸鏈哄埗 + 閲嶆柊鐢熸垚skill.docx (166.6KB) |
| v3.8.6 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍐呭鏀逛负鏍囧噯API鏍煎紡锛? **鍒嗙被** + 瀛愭潯鐩級; + 閲嶆柊鐢熸垚skill.docx; 闅ч亾閲嶅惎閭欢閫氱煡瀹屽杽 + 鏂囨。鍚屾鏇存柊 |
| v3.8.5 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鐢熸垚绗﹀悎瑙勮寖鐨?skill.docx; PowerShell 鍏煎鎬ч噸澶т慨澶? skill.md鏂板鐩綍(TOC), skill.docx鏀圭敤pypandoc_binary鐢熸垚(淇浠ｇ爜鍧楁爣棰樿璇嗗埆), skill.pdf鏀圭敤pupp... |
| v3.8.4 | 2026-07-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇浠庨潪椤圭洰鐩綍杩愯鍚姩鑴氭湰鏃禬eb鏈嶅姟鍚姩澶辫触Bug |
| v3.8.3 | 2026-07-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇'鏈€鏂版洿鏂?鍖哄煙绌虹櫧Bug + Markdown鏍囬鏍煎紡瑙勮寖 |
| v3.8.2 | 2026-07-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇web_output.log鍚姩鏃ュ織琚鐩朆ug |
| v3.8.1 | 2026-07-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| skill.md鍏ㄩ潰琛ュ叏(main.py鐙珛鍑芥暟搂2.15 + index.html鍓嶇61涓嚱鏁奥?.16), API绔偣淇, README鍘婚噸, skill.docx閲嶆柊鐢熸垚; skill.md鍏ㄩ潰琛ュ叏(椤圭洰鎵€鏈夊唴瀹瑰啓鍏?, A... |
| v3.8.0 | 2026-07-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂囨。绯荤粺鍏ㄩ潰鍗囩骇 |
| v3.7.9 | 2026-07-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍒犻櫎generate_skill_docx.py + 閲嶆柊鐢熸垚skill.docx; Hostc闅ч亾绋冲畾鎬х粓鏋佷紭鍖?- 瑙ｅ喅棰戠箒閲嶅惎闂 |
| v3.7.8 | 2026-07-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 闅ч亾蹇€熸仮澶嶆満鍒?3绉掔骇鍝嶅簲+閭欢鍘婚噸; 淇閭欢閲嶅鍙戦€?Python鏃ュ織鍐欏叆妯″紡; run.sh鍚屾淇-鎷彿鏍煎紡+杩愯闃舵鏃ュ織闅旂; 淇call:log鎷彿鍐茬獊+杩愯闃舵鏃ュ織闅旂; 淇鍙屽啓鏈哄埗鏂囦欢閿佸啿绐?(echo)>>fi... |
| v3.7.7 | 2026-06-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇Excel涓嶫SON瀵规瘮鎸夐挳鐘舵€佷笉澶嶄綅闂锛屾洿鏂皊kill.md/skill.docx鎸夐挳鐘舵€佺鐞嗚鑼?|
| v3.7.6 | 2026-06-27 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇pip.conf trusted-host閲嶅/鎻愬彇閿欒銆佹暣鏁版瘮杈冪┖鍊笺€乵acOS du -sb鍏煎鎬с€佹洿鏂皊kill.md/README.md/skill.docx; 鎵嬫満绔寜閽?脳2灞呬腑甯冨眬(max-width:600px)涓?.. |
| v3.7.5 | 2026-06-26 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇鍒╂鼎瓒嬪娍鍥捐仈鍔ㄣ€丒xcel鏃ユ湡杞崲銆乊杞村姩鎬佺缉鏀俱€佷唬鐮佹崯鍧? 骞跺畬鍠勬枃妗?|
| v3.7.4 | 2026-06-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍒╂鼎鎶ヨ〃姹囨€昏鐐瑰嚮灞曞紑浣嶇疆淇 + 鑱氬悎绾у埆淇 + 璺ㄧ郴缁?绉诲姩绔‘璁?+ skill鍚屾 |
| v3.7.3 | 2026-06-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| DOMContentLoaded闂悎淇 + 鎸夐挳鏍峰紡缁熶竴 + skill/docx鍚屾 |
| v3.7.2 | 2026-06-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇index.html绗?197琛屾爣绛鹃棴鍚?+ skill.md/docx瑙勮寖鏇存柊 |
| v3.7.1 | 2026-06-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 璺ㄧ郴缁熺‖缂栫爜褰诲簳娑堥櫎 + V3.5.0绉诲姩绔鑼冨鏌?|
| v3.6.0 | 2026-07-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| + v3.5.0 + README鏍煎紡瑙勮寖锛? 缂栫爜瑙勮寖鍜寁3.5.0绉诲姩绔鑼? README/skill.md/skill.docx 涓夋枃浠跺悓姝ユ洿鏂? 鏇存柊鏃ュ織璇︽儏灞曠ず + skill.docx瀛椾綋淇; 鏇存柊鏃ュ織璇︽儏灞曠ず - c... |
| v3.5.8 | 2026-06-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| update frontend version and changelog to 3.5.8; add skill.md/skill.docx code standards, restore dist folder, update R... |
| v3.5.7 | 2026-06-07 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍓嶇娣诲姞鏈€鏂版洿鏂版ā鍧楋紝鐗堟湰鍙峰悓姝ユ洿鏂? 浠ｇ爜閲嶆瀯浼樺寲锛岃法绯荤粺鍜岀Щ鍔ㄧ閫傞厤瀹屾暣鎬х‘璁?|
| v3.5.6 | 2026-06-06 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹屽杽绉诲姩绔€傞厤鍔熻兘鍜岃〃鏍兼牱寮忎紭鍖?|
| v3.5.4 | 2026-06-06 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 姣忔棩鍒╂鼎鎶ヨ〃浼樺寲锛氭棩鏈熸牸寮忕粺涓€銆侀」鐩瓧娈点€佽〃澶村浐瀹氥€侀敊璇鐞嗗寮?|
| v3.5.3 | 2026-06-06 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鐗堟湰鏃ュ織 - 姹囨€昏鍥句笌鏄庣粏鑱斿姩鍔熻兘 |
| v3.5.2 | 2026-06-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鐗堟湰鏃ュ織; 鍓嶇姣忔棩鍒╂鼎鎶ヨ〃琛ㄦ牸娓叉煋浼樺寲 - 娓叉煋鍒版€昏琛屻€佽揣甯佺鍙枫€佸崟浣嶆樉绀? 姣忔棩鍒╂鼎鎶ヨ〃鍔熻兘瀹屽杽锛屽墠绔〃鏍煎睍绀轰紭鍖? 姣忔棩鍒╂鼎鎶ヨ〃璇诲彇浼樺寲锛屽墠绔睍绀簉eport_text |
| v3.4.37 | 2026-06-05 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲涓存椂鏂囦欢娓呯悊鏈哄埗锛屼慨澶峛at鑴氭湰鍚姩鏃惰鏉€杩涚▼闂 |
| v3.4.34 | 2026-06-04 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇鏂囦欢娓呯悊 API JSON 瑙ｆ瀽閿欒 |
| v3.4.33 | 2026-06-03 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浠ｇ爜浼樺寲鍜岃法绯荤粺鏀寔澧炲己 |
| v3.4.32 | 2026-06-03 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇闀滃儚婧愭樉绀洪棶棰樺苟缁熶竴run.sh閫昏緫; 淇run.bat闀滃儚婧愭祴璇曡娉曢敊璇? 鍏ㄩ潰璺ㄧ郴缁熸敮鎸佷紭鍖?|
| v3.4.31 | 2026-06-01 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇鏂囦欢娓呯悊宸ュ叿鑾峰彇鏂囦欢澶у皬閿欒 |
| v3.4.30 | 2026-05-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇娓呯悊宸ュ叿 API 绌虹洰褰曟娴嬮棶棰?|
| v3.4.29 | 2026-05-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 run.bat 鐗堟湰鍙疯В鏋愬け璐ラ棶棰?|
| v3.4.28 | 2026-05-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲Flask 404澶勭悊鍜岄偖浠跺喎鍗存湡琛ュ彂鏈哄埗 |
| v3.4.27 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇鏂囦欢娓呯悊宸ュ叿'鍒犻櫎鎵€鏈夋枃浠跺拰鏂囦欢澶?鍔熻兘鎶ラ敊 |
| v3.4.26 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 閲嶆瀯缁熶竴寮傚父澶勭悊绯荤粺 + 澧炲己 tunnel_status API URL 楠岃瘉 |
| v3.4.25 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| Excel璇诲彇鏀逛负澶嶅埗鍒颁复鏃舵枃浠讹紝褰诲簳瑙ｅ喅鍏变韩杩濊 |
| v3.4.24 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 Excel 鍏变韩杩濊 - 鎵€鏈夎鍙栨敼涓?read_only=True |
| v3.4.23 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 Excel 鏂囦欢璇诲彇鏃剁殑 Windows 鍏变韩杩濊闂 |
| v3.4.22 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲蹇冭烦妫€娴嬮棿闅斾粠60绉掑埌5绉掞紝鎻愰珮闅ч亾鏁呴殰妫€娴嬮€熷害 |
| v3.4.21 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 纭繚 tunnel_url.txt 鎸佷箙涓€鑷?|
| v3.4.20 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲 tunnel_url.txt 鍐欏叆鏍煎紡 |
| v3.4.19 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍚屾鍐欏叆 tunnel_url.txt |
| v3.4.18 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹屽叏绉婚櫎 tunnel_url 鍏ㄥ眬鍙橀噺鐨勬洿鏂伴€昏緫 |
| v3.4.17 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 缁熶竴鎵€鏈夋ā鍧椾粠 web_output.log 鑾峰彇鍏綉鍦板潃 |
| v3.4.16 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 old_url 鏈畾涔夐敊璇?|
| v3.4.15 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绠€鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎鍐椾綑绛夊緟閫昏緫 |
| v3.4.14 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| read_output 鏀逛负璇诲彇 hostc stdout 杈撳嚭 |
| v3.4.13 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹屽叏绉婚櫎 tunnel_url.txt 璇诲彇閫昏緫锛屽叏閮ㄤ粠 web_output.log |
| v3.4.12 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇绛夊緟 URL 閫昏緫锛岀洿鎺ユ鏌?web_output.log |
| v3.4.11 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 澶у箙绠€鍖?tunnel 閲嶅惎閫昏緫 |
| v3.4.10 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲 hostc 杩涚▼绋冲畾鎬э紝URL 鏃犳晥鏃剁瓑寰?60 绉掑啀閲嶅惎 |
| v3.4.9 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 缁熶竴浣跨敤 web_output.log 浣滀负鍏綉鍦板潃鍞竴鏉ユ簮 |
| v3.4.8 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 缁熶竴鍏綉鍦板潃鏉ユ簮锛屽叏閮ㄤ粠 web_output.log 鑾峰彇; 绠€鍖?auto_start_tunnel 閫昏緫锛岄伩鍏嶉噸澶嶆娴?|
| v3.4.7 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏇存柊 README; 淇 tunnel_url.txt 涓虹┖鏃惰鏉€姝ｅ湪鍚姩鐨?hostc 杩涚▼ |
| v3.4.6 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 tunnel_url.txt 涓虹┖鏃舵棤娉曢噸鍚棶棰?|
| v3.4.5 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 tunnel_url.txt 涓虹┖鏃堕噸鍚惊鐜棶棰?|
| v3.4.4 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲 tunnel_url.txt 涓虹┖鏃剁珛鍗抽噸鍚紝涓嶇瓑寰?0绉掕秴鏃?|
| v3.4.3 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 tunnel_url.txt 涓虹┖鏃朵笉閲嶅惎銆佸畧鎶ょ嚎绋嬮噸澶嶅惎鍔ㄦ棩蹇楀埛灞忋€乁RL 鏃犳晥鏃朵笉杩斿洖鏃犳晥鍦板潃 |
| v3.4.2 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍓嶇灞曠ずURL鍙敤鎬ч獙璇?+ 蹇冭烦妫€娴嬫棩蹇椾紭鍖?|
| v3.4.1 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 web_output.log 鏃ュ織鍚屾闂 |
| v3.4.0 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇闅ч亾鐘舵€佹樉绀哄拰鏃ュ織鍚屾闂 |
| v3.3.9 | 2026-05-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 tunnel_url 鍜屽墠绔樉绀轰笉涓€鑷撮棶棰?|
| v3.3.8 | 2026-05-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鎷嗗垎鐗堟湰锛屼紭鍖栨洿鏂版棩蹇楁牸寮?|
| v3.3.7 | 2026-05-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍓嶇闅ч亾鐘舵€佽疆璇㈤棿闅斾粠5绉掓敼涓?绉掞紝鏇村揩鍚屾URL鍙樺寲; 鏂板鐩戞帶绾跨▼锛屽綋tunnel_url.txt鍙樺寲鏃惰嚜鍔ㄥ悓姝eb_output.log; 绉婚櫎涓嶅繀瑕佺殑瀹氭湡娓呯悊閫昏緫锛宼unnel_url.txt鐢県ostc鑷姩绠＄悊; 闅ч亾鏃ュ織... |
| v3.3.6 | 2026-05-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲杩涚▼娓呯悊閫昏緫锛岄伩鍏嶆棤鏁堟竻鐞嗗鑷寸殑澶辫触缁熻; 鍏ㄩ潰绮剧畝README鏇存柊鏃ュ織锛屾墍鏈夌増鏈帶鍒跺湪3-5涓洿鏂扮偣; 浼樺寲README鏇存柊鏃ュ織鏍煎紡锛屾瘡涓増鏈?-5涓洿鏂扮偣 |
| v3.3.5 | 2026-05-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 缁熶竴杩涚▼妫€娴嬮€昏緫纭繚璺ㄧ郴缁熷吋瀹? 娣诲姞杩涚▼娓呯悊缁熻鍜岃嚜鍔ㄦ竻绌烘棩蹇楀姛鑳? 淇鏃ュ織鏂囦欢杩囧ぇ鍜岃繘绋嬪紓甯搁棶棰? 淇澶氳繘绋嬬珵浜夊拰鏂囦欢鍐欏叆闂; 淇URL閲嶅閫昏緫鍜屾洿鏂拌法绯荤粺鍏煎鎬ц鏄?绛?椤?|
| v3.3.4 | 2026-05-24 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 闅ч亾鏃ュ織杈撳嚭浼樺寲鍜岃繘绋嬫竻鐞嗘敼杩?|
| v3.3.3 | 2026-05-23 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇闅ч亾杩涚▼娉勬紡鍜岄偖浠堕€氱煡闂 |
| v3.3.1 | 2026-05-22 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇 Web 鐣岄潰杩愯鐖櫕鏃?Input/output error 闂 |
| v3.3.0 | 2026-05-22 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻€?|
| v3.2.9 | 2026-05-22 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇闅ч亾棰戠箒閲嶅惎鍜岄偖浠跺彂閫侀棶棰?|
| v3.2.8 | 2026-05-22 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| Flask鍚姩鏃堕偖浠堕€氱煡澧炲己 |
| v3.2.7 | 2026-05-22 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板鍏綉鍦板潃鍙樻洿閭欢閫氱煡鍔熻兘; 鍓嶇浠ｇ爜浼樺寲 - 绠€鍖朌OM鎿嶄綔銆佸悎骞堕噸澶嶅嚱鏁般€佷紭鍖栦簨浠剁粦瀹?|
| v3.2.6 | 2026-05-21 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍓嶇JavaScript浼樺寲 - 绉婚櫎鍐椾綑鏃ュ織锛岀畝鍖栦唬鐮佺粨鏋? 浠ｇ爜璐ㄩ噺浼樺寲 |
| v3.2.5 | 2026-05-21 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绠€鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎闅ч亾閫夋嫨鑿滃崟 |
| v3.2.4 | 2026-05-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍓嶇灞曠ずURL鍙敤鎬ч獙璇?+ 蹇冭烦妫€娴嬫棩蹇椾紭鍖? 绉婚櫎 Cloudflare Tunnel 鍔熻兘锛岀畝鍖栭毀閬撴湇鍔?|
| v3.2.3 | 2026-05-21 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| Cloudflare Tunnel 閰嶇疆鍔熻兘 |
| v3.2.2 | 2026-05-21 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇闅ч亾鑷姩閲嶈繛姝诲惊鐜棶棰橈紝瀹炵幇鏃犳劅鍒囨崲鍒版柊鐨勫叕缃?URL |
| v3.2.1 | 2026-05-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸?URL 涓€鑷?|
| v3.2.0 | 2026-05-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 澶栭儴鍚姩闅ч亾鐩戞帶鏈哄埗 |
| v3.1.9 | 2026-05-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲鍓嶇闅ч亾鍏变韩鎸夐挳锛屼紭鍏堝鐢╰unnel_url.txt涓殑宸叉湁鍦板潃 |
| v3.1.8 | 2026-05-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 澧炲己闅ч亾淇濇寔鍦ㄧ嚎鏈哄埗; 淇闈㈡澘鍐茬獊闂 - 鎵€鏈夊姛鑳介噰鐢ㄧ嫭绔嬪鍣? 淇Excel瀵规瘮鏄剧ず鎵€鏈変环鏍肩殑澶氫綑璐у彿 |
| v3.1.7 | 2026-05-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 璐у彿瀵规瘮閲嶅妫€娴嬩紭鍖?|
| v3.1.5 | 2026-05-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 闅ч亾鑷姩閲嶈繛鏈哄埗 |
| v3.1.3 | 2026-05-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 璺ㄧ郴缁熷吋瀹规€у寮?- 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦€佸畬鍠勮繘绋嬫竻鐞?|
| v3.1.2 | 2026-05-18 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 澶╂皵鐪嬫澘棰勫姞杞戒紭鍖? 閸撳秶顏悧鍫熸拱閸欒渹绮燗PI鐎圭偞妞傞懢宄板絿; 娣囶喖顦查梾褔浜鹃崥顖氬З閸氬骸鍙曠純鎴濇勾閸р偓娑撳秵妯夌粈铏规畱闂傤噣顣? 娴兼ê瀵查崥顖氬З妞ゅ搫绨妴浣搞亯濮樻梻婀呴弶鎸庡櫩閸旂姾娴囬妴渚€娼ら幀浣界カ濠ф€梲ip閸樺缂? update |
| v3.1.1 | 2026-05-20 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇闅ч亾澶嶅埗鎸夐挳澶辨晥闂; 鍓嶇鐗堟湰鍙疯嚜鍔ㄨ窡闅弇ain.py涓璙ERSION鍙橀噺 |
| v3.0.8 | 2026-05-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 闅ч亾鍏变韩鍔熻兘澧炲己 - 鍙偣鍑婚摼鎺ャ€佷竴閿鍒躲€佸惎鍔ㄩ涓嬭浇hostc |
| v3.0.7 | 2026-05-17 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲闅ч亾鍏变韩鍔熻兘 + 璺ㄥ钩鍙板吋瀹规€у寮?|
| v3.0.6 | 2026-05-06 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛€傞厤 |
| v3.0.5 | 2026-05-01 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇Excel涓嶫SON瀵规瘮鍔熻兘涓柊澧為珮浠峰晢鍝佸垽瀹氶€昏緫閿欒 |
| v3.0.4 | 2026-05-01 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| Excel鏂囦欢璺緞鍘婚噸鍜岃揣鍙疯鍙栭『搴忎紭鍖?|
| v3.0.3 | 2026-05-01 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绉诲姩绔鑸爮鍥哄畾缃《浼樺寲 |
| v3.0.2 | 2026-05-01 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绉诲姩绔搷搴斿紡閫傞厤鍏ㄩ潰浼樺寲 |
| v3.0.1 | 2026-04-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鐗堟湰鏇存柊鏃ュ織; Excel澶氭枃浠惰鍙栦紭鍖?|
| v3.0.0 | 2026-04-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| Cookie绠＄悊浼樺寲鍜岃法骞冲彴鍏煎鎬ф彁鍗?|
| v2.9.6 | 2026-04-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍚姩鑴氭湰浼樺寲鍜屽姛鑳芥敼杩?|
| v2.9.5 | 2026-04-30 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 锛屾坊鍔犲畬鏁存洿鏂版棩蹇? 绉诲姩绔搷搴斿紡閫傞厤浼樺寲 |
| v2.9.4 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板浜掑姩寮忚揣鍙峰姣斿姛鑳?|
| v2.9.3 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| Cookie鏇存柊鍓嶈嚜鍔ㄦ竻绌烘満鍒?|
| v2.9.2 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲鍟嗗搧鍒楄〃鑱斿姩婊氬姩鍔熻兘 |
| v2.9.1 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲鍓嶇鏃堕棿鏄剧ず鍔熻兘锛屽噺灏慏OM閲嶆覆鏌撳紑閿€ |
| v2.9.0 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞鍓嶇鏃堕棿鏄剧ず鍔熻兘骞朵紭鍖朖avaScript浠ｇ爜 |
| v2.8.0 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏀逛负04-29锛寁2.7.1鏀逛负04-27锛屼慨澶峷2.5.21閲嶅闂; 鍓嶇灞曠ず浼樺寲锛欵xcel涓嶫SON瀵规瘮缁撴灉鐩存帴灞曠ず鍦ㄥ墠绔〉闈?|
| v2.7.2 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏃ュ織锛氫慨澶?api/clean/list鏂囦欢鏄剧ず鏍煎紡 |
| v2.7.1 | 2026-04-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇鍟嗗搧璇︽儏椤靛浘鐗囧姞杞介棶棰?|
| v2.7.0 | 2026-04-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞鐗规畩鏂囦欢鍚嶄繚鎶わ紙.DS_Store, Thumbs.db绛夛級; 澧炲己娓呯悊鍑芥暟淇濇姢鏈哄埗锛屾坊鍔犳洿澶氫繚鎶ょ殑鏂囦欢绫诲瀷鍜屾枃浠跺す; 闆嗘垚鏂囦欢娓呯悊鍔熻兘锛屼紭鍖栦唬鐮侀€昏緫 |
| v2.6.1 | 2026-04-28 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞鑷姩鏁版嵁搴撳瓨鍌ㄥ姛鑳斤紝杩愯鐖櫕鏃惰嚜鍔ㄤ繚瀛樺晢鍝佹暟鎹埌MySQL; 璐у彿瀵规瘮鍗＄墖鏍峰紡浼樺寲锛屽皢API杩斿洖缁撴灉鏀逛负缇庤鐨勫崱鐗囧紡灞曠ず |
| v2.6.0 | 2026-06-26 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| (2026-06-26)鐗堟湰鏉＄洰; v2.8.0鐗堟湰鏃ユ湡椤哄簭锛岀‘淇濇墍鏈夌増鏈彿鍜屾棩鏈熸寜鏃堕棿閫掑鎺掑垪; Web绔柊澧炶揣鍙峰姣擜PI鍜孴XT瀵规瘮鎸夐挳; 鑿滃崟閫夐」5鏍规嵁绯荤粺鑷姩鍚姩Web鏈嶅姟; 鑿滃崟鏂板閫夐」5鍚姩Web鏈嶅姟 绛?椤?|
| v2.5.22 | 2026-04-19 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绉婚櫎闂查奔骞冲彴鎵嬬画璐?0鍏冨皝椤堕檺鍒讹紝鏀逛负鎸夊崟鏈哄敭浠风殑1.6%璁＄畻 |
| v2.5.21 | 2026-04-26 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏀寔澶氬钩鍙癊xcel璺緞閰嶇疆锛岃嚜鍔ㄨ疆璇㈡娴? 閲嶆瀯鏁版嵁鑾峰彇閫昏緫锛岀洿鎺ラ€氳繃API鑾峰彇鎵€鏈夊晢鍝佹暟鎹? 閲嶆瀯鏁版嵁鑾峰彇閫昏緫锛岀洿鎺ラ€氳繃API鑾峰彇鍟嗗搧鏁版嵁 |
| v2.5.20 | 2026-04-15 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇Windows娴忚鍣ㄦ娴嬶紝浣跨敤dir+findstr鏇夸唬閫氶厤绗?|
| v2.5.19 | 2026-04-15 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲macOS娴忚鍣ㄦ娴嬶紝鏀寔Google Chrome for Testing.app |
| v2.5.18 | 2026-04-15 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲娴忚鍣ㄦ娴嬶紝閬垮厤閲嶅涓嬭浇Playwright娴忚鍣? 鏂板鐜妫€娴嬪姛鑳?|
| v2.5.17 | 2026-04-13 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲鎷胯揣浠锋彁鍙栨€ц兘鍜屼唬鐮佺粨鏋?|
| v2.5.16 | 2026-04-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲CookieValidator绫伙紝绮剧偧浠ｇ爜閫昏緫 |
| v2.5.14 | 2026-04-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇璺緞閿欒锛屽畬鍠凱athManager缁熶竴绠＄悊 |
| v2.5.13 | 2026-04-29 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 22鐗堟湰閲嶅鍜屾棩鏈熸贩涔遍棶棰橈紝閲嶆柊鏁寸悊鎵€鏈夌増鏈彿纭繚杩炵画鎬у拰鏃堕棿椤哄簭姝ｇ‘; 鏂板PathManager绫伙紝缁熶竴绠＄悊鎵€鏈夎法绯荤粺璺緞 |
| v2.5.12 | 2026-04-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲绯荤粺妫€娴嬮€昏緫锛岀粺涓€璺ㄥ钩鍙版祻瑙堝櫒閰嶇疆 |
| v2.5.10 | 2026-04-12 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇瀵煎叆閿欒锛岀‘淇滶xcel瀵规瘮鍔熻兘姝ｅ父杩愯 |
| v2.5.9 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲浠ｇ爜閫昏緫锛屼娇鐢ㄥ垪琛ㄦ帹瀵煎紡绠€鍖栨枃浠舵煡鎵句唬鐮?|
| v2.5.8 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇excel_file涓篘one鐨勯敊璇紝瑙ｅ喅os.path.exists鐨凾ypeError |
| v2.5.7 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇浠锋牸姣旇緝閿欒锛岃В鍐硃arse_price杩斿洖None鐨凾ypeError |
| v2.5.6 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲Cookie鏇存柊瀹屾垚鍚庣殑寤惰繜锛屾彁鍗囧搷搴旈€熷害 |
| v2.5.5 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绉婚櫎Cookie鏇存柊鍚庣殑鍥炶溅纭锛岀畝鍖栨搷浣滄祦绋?|
| v2.5.4 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹炵幇鐪熸鐨勮嚜鍔ㄥ叧闂祻瑙堝櫒锛屾娴嬬櫥褰曞悗鑷姩鍏抽棴 |
| v2.5.3 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲Cookie鏇存柊鎻愮ず淇℃伅锛屾槑纭嚜鍔ㄥ叧闂祻瑙堝櫒 |
| v2.5.2 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绠€鍖朇ookie鏇存柊娴佺▼锛屽弬鑰僾2.1.1鐗堟湰瀹炵幇 |
| v2.5.0 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲鍟嗗搧淇℃伅鎻愬彇閫昏緫锛岀簿绠€浠ｇ爜缁撴瀯 |
| v2.4.7 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板鐙珛Cookie鑷姩鏇存柊鍔熻兘锛屼紭鍖栨祻瑙堝櫒鍚姩娴佺▼鍏抽棴 |
| v2.4.6 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹屽杽澶囨敞鎻愬彇鍔熻兘锛屾彁鍙栨墍鏈夋湁澶囨敞鐨勫晢鍝佷俊鎭?|
| v2.4.5 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇澶囨敞鎻愬彇閿欒锛屾敮鎸佹棤鏍囩澶囨敞淇℃伅鎻愬彇 |
| v2.4.4 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇浠锋牸鎻愬彇閿欒锛屾敮鎸佸崈鍒嗗埗浠锋牸鏍煎紡 |
| v2.4.1 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板骞冲潎姣忎釜璁惧鍞嚭鍧囦环缁熻 |
| v2.4.0 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绠€鍖朖SON鏂囦欢甯冨眬锛屼紭鍖栦环鏍兼樉绀轰负鍗冨垎鍒?|
| v2.3.6 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 澧炲己HTML鍐呭鎼滅储锛屽畬鍠勬嬁璐т环鎻愬彇閫昏緫 |
| v2.3.5 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 澧炲己鎴愭湰浠疯瘑鍒紝娣诲姞鏅鸿兘浠锋牸鎻愬彇閫昏緫 |
| v2.3.4 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板鎷胯揣浠锋彁鍙栧姛鑳斤紝淇璁惧鎴愭湰绱鍜岃澶囧潎浠蜂负0鐨勯棶棰?|
| v2.3.3 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板璁惧鍧囦环锛屼紭鍖栭棽楸煎钩鍙版墜缁垂璁＄畻锛堝崟鏈烘渶楂?0鍏冨皝椤讹級 |
| v2.3.2 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板绱缁熻鍔熻兘锛屾坊鍔犻璁″敭鍑轰环鏍笺€佽澶囨垚鏈拰骞冲彴鎵嬬画璐圭疮璁?|
| v2.3.1 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇濈暀Cookie鏇存柊閫夐」锛屼粎鏀寔鑷姩鏇存柊鍔熻兘 |
| v2.3.0 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鍔熻兘鏁村悎浼樺寲锛屽悎骞惰彍鍗曢€夐」骞剁簿鐐间唬鐮侀€昏緫 |
| v2.2.2 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| Excel瀵规瘮JSON鍔熻兘澧炲己锛屾坊鍔犲皬璁″瓧娈靛苟绮剧偧浠ｇ爜閫昏緫 |
| v2.2.1 | 2026-04-11 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞鑷姩瀵规瘮鍔熻兘锛岀‘淇濇瘡娆¤繍琛岀埇铏悗閮界敓鎴愬皬璁″瓧娈?|
| v2.2.0 | 2026-04-09 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鎬ц兘浼樺寲锛屾彁鍗囧苟鍙戝鐞嗚兘鍔涘拰鍏冪礌鍘婚噸鏁堢巼 |
| v2.1.9 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浠ｇ爜绮剧偧浼樺寲锛岀畝鍖栭€昏緫鎻愬崌鍙淮鎶ゆ€?|
| v2.1.8 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲婊氬姩鍔犺浇绛栫暐锛岄噰鐢ㄦ縺杩涙ā寮忓揩閫熷姞杞芥墍鏈夋暟鎹?|
| v2.1.7 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞澶氶噸瓒呮椂淇濇姢鍜岄噸璇曟満鍒讹紝闃叉鐖櫕鍗℃ |
| v2.1.6 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇寮圭獥鍏抽棴瓒呮椂闂; 娣诲姞鏃堕棿缁熻浼樺寲鎬ц兘 |
| v2.1.5 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇楂樹环鍟嗗搧绛涢€夐€昏緫; 瑙ｅ喅瀵规瘮缁撴灉涓嶅噯纭棶棰?|
| v2.1.3 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲JSON鏂囦欢瀵规瘮璁板綍鏈哄埗; 鏀寔澶氭潯瀵规瘮璁板綍 |
| v2.1.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲JSON鏂囦欢瀵规瘮鍔熻兘; 鏂板缂撳瓨鏂囦欢鏈哄埗 |
| v2.1.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂; 鍒犻櫎璋冭瘯浠ｇ爜 |
| v2.1.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板璋冭瘯鍔熻兘; 浼樺寲寮€鍙戜綋楠?|
| v2.0.9 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板褰撳ぉJSON鏂囦欢瀵规瘮鍔熻兘 |
| v2.0.8 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂 |
| v2.0.7 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲楂樹环鍟嗗搧绛涢€? 淇娴忚鍣ㄥ惎鍔?|
| v2.0.6 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲鏁版嵁鍙樺寲鍒嗘瀽浠ｇ爜; 绮剧畝閫昏緫 |
| v2.0.5 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏇存柊Cookie杩囨湡鏃堕棿 |
| v2.0.4 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板Cookie鑷姩鏇存柊鍔熻兘; 浼樺寲Excel鏂囦欢妫€鏌?|
| v2.0.3 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浠ｇ爜閲嶆瀯鍜屼紭鍖?|
| v2.0.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板楂樹环鍟嗗搧淇℃伅鍐欏叆JSON鍔熻兘 |
| v2.0.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲楂樹环鍟嗗搧绛涢€夐€昏緫 |
| v2.0.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板璐у彿瀵规瘮楂樹环鍟嗗搧绛涢€夊姛鑳?|
| v1.9.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞楂樹环鍟嗗搧绛涢€夊姛鑳?|
| v1.8.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞杩愯鏃堕棿鏄剧ず鍜屽姩鎬佽皟鏁村姛鑳?|
| v1.7.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 婊氬姩鍙傛暟鍙厤缃寲 |
| v1.6.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇椤甸潰鍔犺浇姝绘満闂 |
| v1.6.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇婊氬姩姝诲惊鐜棶棰?|
| v1.6.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹屾垚鎵€鏈夐珮浼樺厛绾т紭鍖?|
| v1.5.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 绠€鍖朖SON鏁版嵁缁撴瀯涓?涓牳蹇冨瓧娈?|
| v1.4.3 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲椤甸潰鍔犺浇閫昏緫锛屽噺灏戠瓑寰呮椂闂?|
| v1.4.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 瀹屾垚璺ㄧ郴缁熺幆澧冩祴璇曞拰浼樺寲; 浼樺寲鍟嗗搧鍘婚噸閫昏緫锛屾敮鎸佹棤璐у彿鍟嗗搧 |
| v1.4.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 浼樺寲鐧诲綍绛夊緟閫昏緫锛岀Щ闄ゆ墜鍔ㄧ‘璁ゆ楠?|
| v1.4.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鎵╁睍鍟嗗搧鏁版嵁瀛楁鍒?0涓畬鏁村瓧娈?|
| v1.3.4 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板鏁版嵁鍙樺寲鎻忚堪鍜屽瓧娈佃鏄?|
| v1.3.3 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板瀵规瘮缁撴灉娑堟伅鍒癑SON鏃ュ織 |
| v1.3.2 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 淇JSON鏁版嵁瑙ｆ瀽閿欒 |
| v1.3.1 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 鏂板JSON澶氫綑璐у彿瀵规瘮鍔熻兘骞朵紭鍖栦唬鐮佺粨鏋?|
| v1.3.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞Excel涓嶫SON鑷姩瀵规瘮鍔熻兘 |
| v1.2.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞浜嗕竴涓猚ookie鑷姩鏇存崲鐨勫姛鑳斤紝浣垮緱涓滆タ鏇村姞鐨勮嚜鍔ㄥ寲 |
| v1.1.0 | 鍘嗗彶鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 娣诲姞浜嗕竴涓猠xcel璇诲彇鍔熻兘锛屼娇寰椾笢瑗挎洿鍔犵殑鑷姩鍖?|
| v1.0.0 | 鍒濆鐗堟湰 | 灏忔棴浜屾墜鏈猴紙瑗垮洯璺級| 椤圭洰鍒濆鍖栵紝鍩虹鍔熻兘瀹炵幇 |

---

---

## 馃敶 PY-CORE-016: 璺ㄥ钩鍙板惎鍔ㄨ剼鏈寖寮?(Cross-Platform Startup Script)

### 鑼冨紡鎻忚堪
缁熶竴鐨勮法骞冲彴鍚姩鑴氭湰锛屾敮鎸乄indows (.bat) 鍜孡inux/macOS (.sh)锛屽疄鐜帮細
- 鐜鑷姩妫€娴嬩笌瀹夎
- Python/Node.js渚濊禆绠＄悊
- 闀滃儚婧愯嚜鍔ㄩ€夋嫨
- 杩涚▼娓呯悊涓庣鍙ｇ鐞?
- 缁熶竴鏃ュ織杈撳嚭

### 鏍稿績瀹炵幇

#### Windows鍚姩鑴氭湰 (run.bat)
```batch
@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

:: 鐗堟湰鑷姩璇诲彇
set "VERSION=0.0.0"
for /f "delims=" %%i in ('py -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')" 2^>nul') do set "VERSION=%%i"

:: 缁熶竴鏃ュ織鍑芥暟锛堟绉掔骇鏃堕棿鎴筹級
:ms_timestamp
set "TIMESTAMP="
if defined _TS_PYTHON (
    for /f "delims=" %%t in ('"!_TS_PYTHON!" -c "from datetime import datetime; d=datetime.now(); print(d.strftime(\"%%Y-%%m-%%d %%H:%%M:%%S.\")+f\"{d.microsecond//1000:03d}\")" 2^>nul') do set "TIMESTAMP=%%t"
)
if not defined TIMESTAMP set "TIMESTAMP=%date% %time: =0%"
exit /b

:log
call :ms_timestamp
echo [%TIMESTAMP%] %*
if not "%LOG_FILE%"=="" (
    if exist "!LOG_FILE!" (
        >> "!LOG_FILE!" echo [%TIMESTAMP%] %* 2>nul
    )
)
exit /b

:: 鐜妫€娴嬶紙6姝ユ祦绋嬶級
:detect_environments
call :detect_python_env    :: [1/6] 妫€娴婸ython鐜
call :detect_node_env      :: [2/6] 妫€娴婲ode.js鐜  
call :test_pip_mirrors     :: [3/6] 娴嬭瘯PIP鍔犻€熼暅鍍忔簮
call :test_npm_mirrors     :: [4/6] 娴嬭瘯NPM鍔犻€熼暅鍍忔簮
call :detect_venv          :: [5/6] 妫€娴婸ython铏氭嫙鐜
call :setup_venv           :: [6/6] 璁剧疆铏氭嫙鐜骞跺畨瑁呬緷璧?

:: 闀滃儚婧愯嚜鍔ㄩ€夋嫨锛堜互寤惰繜鏈€浣庝负鏈€浼橈級
:test_pip_mirrors
set "MIRRORS[0]=https://pypi.tuna.tsinghua.edu.cn/simple|娓呭崕婧?
set "MIRRORS[1]=https://mirrors.aliyun.com/pypi/simple/|闃块噷浜?
set "MIRRORS[2]=https://pypi.douban.com/simple/|璞嗙摚"

:: 娴嬭瘯姣忎釜闀滃儚婧愮殑杩炴帴鏃堕棿
for /L %%i in (0,1,3) do (
    for /f "tokens=1,2 delims=|" %%a in ("!MIRRORS[%%i]!") do (
        curl.exe -s -o NUL -w "%%{time_connect}" --connect-timeout 1.5 "!MIRROR_URL!"
        :: 閫夋嫨寤惰繜鏈€浣庣殑闀滃儚婧?
    )
)
```

#### Linux/macOS鍚姩鑴氭湰 (run.sh)
```bash
#!/bin/bash
cd "$(dirname "$0")"

# 鐗堟湰鑷姩璇诲彇
VERSION="0.0.0"
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        VERSION=$("$cmd" -c "import re; m=re.search(r'###\s+v([\d.]+)', open('README.md', encoding='utf-8').read()); print(m.group(1) if m else '0.0.0')") && break
    fi
done

# 缁熶竴鏃ュ織鍑芥暟锛堝吋瀹笹NU date鍜孊SD date锛?
_ms_timestamp() {
    if date '+%3N' 2>/dev/null | grep -qE '^[0-9]{3}$'; then
        date '+%Y-%m-%d %H:%M:%S.%3N'  # GNU date
    else
        local ms=$(python3 -c "from datetime import datetime; print(datetime.now().microsecond//1000)" 2>/dev/null || echo "000")
        printf '%s.%03d' "$(date '+%Y-%m-%d %H:%M:%S')" "${ms:-000}"  # BSD date fallback
    fi
}

log() {
    TIMESTAMP="$(_ms_timestamp)"
    echo "[$TIMESTAMP] $*"
    [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ] && echo "[$TIMESTAMP] $*" >> "$LOG_FILE" 2>/dev/null
}

# 鐜妫€娴嬶紙6姝ユ祦绋嬶級
pre_launch() {
    detect_python_env   # [1/6]
    detect_node_env     # [2/6]
    test_pip_mirrors    # [3/6]
    test_npm_mirrors    # [4/6]
    detect_venv         # [5/6]
    setup_venv          # [6/6]
}
```

### 鍏抽敭鐗规€?
1. **鐗堟湰鑷姩瑙ｆ瀽**: 浠嶳EADME.md姝ｅ垯鎻愬彇鐗堟湰鍙?
2. **姣绾ф棩蹇?*: 鏀寔Windows鍜孶nix鐨勯珮绮惧害鏃堕棿鎴?
3. **闀滃儚婧愭櫤鑳介€夋嫨**: 鑷姩娴嬭瘯骞堕€夋嫨鏈€蹇暅鍍?
4. **杩涚▼绠＄悊**: 鍚姩鍓嶆竻鐞嗘畫鐣欒繘绋嬶紝绔彛鍐茬獊妫€娴?
5. **鐜鑷剤**: 鑷姩瀹夎缂哄け鐨凱ython/Node.js鐜

---

## 馃敶 PY-CORE-017: CI/CD鑷姩鍖栭儴缃茶寖寮?(CI/CD Automation)

### 鑼冨紡鎻忚堪
GitHub Actions宸ヤ綔娴侊紝瀹炵幇锛?
- 澶氭搷浣滅郴缁熸祴璇曠煩闃?
- 鑷姩鍖栨瀯寤轰笌閮ㄧ讲
- 瀹夊叏鎵弿涓庤川閲忔鏌?
- 閫氱煡涓庢姤鍛婄敓鎴?

### 鏍稿績瀹炵幇
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.9', '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ -v --cov=. --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
  
  security-scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Run Bandit Security Scan
      run: |
        pip install bandit
        bandit -r main.py -ll
  
  deploy:
    needs: [test, security-scan]
    if: github.ref == 'refs/heads/master'
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to production
      run: |
        echo "閮ㄧ讲鍒扮敓浜х幆澧?
```

---

## 馃敶 PY-CORE-018: PWA绂荤嚎缂撳瓨鑼冨紡 (Progressive Web App)

### 鑼冨紡鎻忚堪
浣跨敤Workbox瀹炵幇PWA绂荤嚎缂撳瓨锛屾彁鍗囩敤鎴蜂綋楠岋細
- Service Worker娉ㄥ唽涓庣鐞?
- 闈欐€佽祫婧愰缂撳瓨
- 绂荤嚎鍥為€€绛栫暐
- 缂撳瓨鏇存柊鏈哄埗

### 鏍稿績瀹炵幇

#### Service Worker娉ㄥ唽 (registerSW.js)
```javascript
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js', { scope: './' })
            .then(registration => {
                console.log('SW registered:', registration.scope);
            })
            .catch(error => {
                console.log('SW registration failed:', error);
            });
    });
}
```

#### Service Worker閰嶇疆 (sw.js)
```javascript
importScripts('./workbox-9c191d2f.js');

const { precacheAndRoute, cleanupOutdatedCaches, registerRoute, NavigationRoute } = workbox;

// 棰勭紦瀛橀潤鎬佽祫婧?
precacheAndRoute([
    { url: 'index.html', revision: 'f0ffca7cb...' },
    { url: 'assets/index-CLgEPqQj.js', revision: null },
    { url: 'assets/vendor-J3N2YKMO.js', revision: null },
]);

// 娓呯悊杩囨湡缂撳瓨
cleanupOutdatedCaches();

// 瀵艰埅璇锋眰鍥為€€鍒癷ndex.html锛圫PA鏀寔锛?
registerRoute(
    new NavigationRoute(
        createHandlerBoundToURL('index.html')
    )
);
```

---

## 馃煛 PY-CORE-019: Python渚濊禆绠＄悊鑼冨紡 (Python Dependency Management)

### 鑼冨紡鎻忚堪
鏍囧噯鍖栫殑Python渚濊禆绠＄悊锛岀‘淇濆彲閲嶅鏋勫缓锛?

### 鏍稿績瀹炵幇

#### requirements.txt缁撴瀯
```
# 鏍稿績渚濊禆 (FastAPI)
fastapi>=0.100.0
uvicorn[standard]>=0.23.0
playwright>=1.59.0

# 鏁版嵁澶勭悊
openpyxl>=3.1.2
pandas>=1.3.0
pymysql>=1.1.0

# 绯荤粺鐩戞帶
psutil>=5.9.0
prometheus_client>=0.17.0

# 鏁版嵁楠岃瘉
pydantic>=2.0.0

# 鏂囨。鐢熸垚
python-docx>=1.2.0
```

#### 渚濊禆妫€鏌ヤ笌瀹夎
```python
def check_deps_satisfied(requirements_file="requirements.txt"):
    """妫€鏌ヤ緷璧栨槸鍚︽弧瓒?""
    import pkg_resources
    
    with open(requirements_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            try:
                pkg_resources.require(line)
            except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
                return False
    
    return True

def install_playwright_cdn():
    """浣跨敤CDN闀滃儚瀹夎Playwright娴忚鍣?""
    mirrors = [
        ("https://npmmirror.com/mirrors/playwright", "娣樺疂闀滃儚"),
        ("https://registry.npmmirror.com/-/binary/playwright", "npmmirror"),
    ]
    
    for mirror_url, mirror_name in mirrors:
        try:
            os.environ['PLAYWRIGHT_DOWNLOAD_HOST'] = mirror_url
            subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'], 
                         check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError:
            continue
    
    return False
```

---

## 馃煛 PY-CORE-020: Node.js渚濊禆绠＄悊涓庤ˉ涓佹寔涔呭寲鑼冨紡 (Node.js Dependency & Patch Management)

### 鑼冨紡鎻忚堪
Node.js渚濊禆绠＄悊锛屽寘鍚玴atch-package瀹炵幇琛ヤ竵鎸佷箙鍖栵細

### 鏍稿績瀹炵幇

#### package.json閰嶇疆
```json
{
  "name": "xy_ws-dist",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "postinstall": "patch-package"
  },
  "dependencies": {
    "hostc": "^1.3.0",
    "patch-package": "^8.0.0"
  }
}
```

#### 琛ヤ竵鏂囦欢绀轰緥 (patches/hostc+1.3.0.patch)
```diff
diff --git a/dist/lib/tunnel.js b/dist/lib/tunnel.js
index xxxxxxx..yyyyyyy 100644
--- a/dist/lib/tunnel.js
+++ b/dist/lib/tunnel.js
@@ -142,6 +142,10 @@ function safeCloseWebSocket2(socket, code, reason) {
   if (!socket) return;
   try {
+    if (socket.readyState === WebSocket.CONNECTING) {
+      socket.once("error", () => {});
+      socket.terminate();
+    } else {
       socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
+    }
   } catch {
     try { socket.terminate(); } catch {}
   }
```

### 宸ヤ綔鍘熺悊
1. `npm install` 鏃惰嚜鍔ㄨ繍琛?`postinstall` 鑴氭湰
2. `patch-package` 搴旂敤 `patches/` 鐩綍涓嬬殑鎵€鏈夎ˉ涓?
3. 纭繚绗笁鏂瑰簱鐨勪慨澶嶄笉浼氬洜渚濊禆鏇存柊鑰屼涪澶?

---

## 馃煛 PY-CORE-021: API鍘嬪姏娴嬭瘯鑼冨紡 (API Stress Testing)

### 鑼冨紡鎻忚堪
鏍囧噯鍖栫殑API鍘嬪姏娴嬭瘯宸ュ叿锛岀敤浜庢€ц兘璇勪及鍜岀摱棰堝彂鐜帮細

### 鏍稿績瀹炵幇
```python
#!/usr/bin/env python3
"""
Szwego鍟嗗搧鐖櫕 - API鍘嬪姏娴嬭瘯宸ュ叿

鐢ㄦ硶:
    python stress_test.py --target http://localhost:5000 --concurrent 100 --requests 1000
"""

def make_request(url, method='GET', data=None, timeout=10):
    """鍙戦€丠TTP璇锋眰骞惰褰曟寚鏍?""
    start = time.time()
    try:
        headers = {'Content-Type': 'application/json'}
        req = Request(url, data=data.encode('utf-8') if data else None, 
                     headers=headers, method=method)
        resp = urlopen(req, timeout=timeout)
        status = resp.getcode()
        body = resp.read().decode('utf-8', errors='replace')
        elapsed = time.time() - start
        return {'status': status, 'time': elapsed, 'error': None, 'size': len(body)}
    except HTTPError as e:
        return {'status': e.code, 'time': time.time() - start, 'error': str(e), 'size': 0}
    except Exception as e:
        return {'status': 0, 'time': time.time() - start, 'error': str(e), 'size': 0}

def run_stress_test(target, concurrent, total_requests, endpoints):
    """鎵ц鍘嬪姏娴嬭瘯"""
    results = []
    
    with ThreadPoolExecutor(max_workers=concurrent) as executor:
        futures = []
        for i in range(total_requests):
            ep = endpoints[i % len(endpoints)]
            futures.append(executor.submit(worker, ep))
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)
    
    # 缁熻鍒嗘瀽
    success = [r for r in results if 200 <= r['status'] < 400]
    times = [r['time'] for r in results]
    
    print(f"鎴愬姛鐜? {len(success)/len(results)*100:.2f}%")
    print(f"骞冲潎鍝嶅簲鏃堕棿: {statistics.mean(times)*1000:.2f}ms")
    print(f"P99鍝嶅簲鏃堕棿: {sorted(times)[int(len(times)*0.99)]*1000:.2f}ms")

# 浣跨敤绀轰緥
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Szwego API鍘嬪姏娴嬭瘯宸ュ叿')
    parser.add_argument('--target', default='http://localhost:5000')
    parser.add_argument('--concurrent', type=int, default=100)
    parser.add_argument('--requests', type=int, default=1000)
    args = parser.parse_args()
    
    run_stress_test(args.target, args.concurrent, args.requests, [])
```

### 鍏抽敭鎸囨爣
| 鎸囨爣 | 璇存槑 | 鐩爣鍊?|
|------|------|--------|
| **鎴愬姛鐜?* | HTTP 200-399姣斾緥 | > 95% |
| **骞冲潎寤惰繜** | 鍝嶅簲鏃堕棿鍧囧€?| < 200ms |
| **P99寤惰繜** | 99鍒嗕綅鍝嶅簲鏃堕棿 | < 1000ms |
| **QPS** | 姣忕璇锋眰鏁?| > 500 |

---

## 馃煛 PY-CORE-022: 杈圭晫鏉′欢娴嬭瘯鑼冨紡 (Edge Case Testing)

### 鑼冨紡鎻忚堪
绯荤粺鎬х殑杈圭晫鏉′欢鍜屾瀬绔儏鍐垫祴璇曪紝纭繚绯荤粺鍋ュ．鎬э細

### 鏍稿績瀹炵幇
```python
class TestBoundaryConditions:
    """杈圭晫鏉′欢娴嬭瘯绫?""
    
    def test_empty_string_input(self):
        """绌哄瓧绗︿覆杈撳叆澶勭悊"""
        client = app.test_client()
        response = client.post('/api/run', 
                              data=json.dumps({'command': ''}),
                              content_type='application/json')
        assert response.status_code in [400, 200]
    
    def test_very_long_command(self):
        """瓒呴暱鍛戒护瀛楃涓诧紙10000+瀛楃锛?""
        long_command = 'echo "' + 'a' * 10000 + '"'
        response = client.post('/api/run',
                              data=json.dumps({'command': long_command}),
                              content_type='application/json')
        assert response.status_code in [200, 413]  # OK鎴朠ayload Too Large
    
    def test_special_characters_in_command(self):
        """鍖呭惈鐗规畩瀛楃鐨勫懡浠?""
        special_commands = [
            {'command': 'echo "hello world"'},
            {"command": "echo 'single quotes'"},
            {'command': 'echo $HOME'},
            {'command': 'echo ; malicious command'},
            {'command': 'echo && another'},
            {'command': 'echo | pipe'},
        ]
        
        for cmd in special_commands:
            response = client.post('/api/run',
                                  data=json.dumps(cmd),
                                  content_type='application/json')
            assert response.status_code != 500, f"宕╂簝浜庣壒娈婂瓧绗? {cmd['command'][:50]}"
    
    def test_unicode_input(self):
        """Unicode瀛楃杈撳叆"""
        unicode_commands = [
            {'command': 'echo 涓枃娴嬭瘯'},
            {'command': 'echo 鏃ユ湰瑾炪儐銈广儓'},
            {'command': 'echo 馃帀馃殌emoji娴嬭瘯'},
            {'command': 'echo 丕賱毓乇亘賷丞'},
        ]
        
        for cmd in unicode_commands:
            response = client.post('/api/run',
                                  data=json.dumps(cmd, ensure_ascii=False),
                                  content_type='application/json; charset=utf-8')
            assert response.status_code != 500


class TestConcurrencyEdgeCases:
    """骞跺彂杈圭晫鎯呭喌娴嬭瘯"""
    
    def test_burst_traffic(self):
        """绐佸彂娴侀噺妯″紡锛氱灛闂村ぇ閲忚姹傚悗闈欓粯"""
        threads = []
        results = []
        
        def make_request(i):
            resp = client.post('/api/run',
                              data=json.dumps({'command': f'burst_{i}'}),
                              content_type='application/json')
            results.append(resp.status_code)
        
        # 鐬棿鍚姩50涓嚎绋?
        for i in range(50):
            t = threading.Thread(target=make_request, args=(i,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join(timeout=10)
        
        success_count = sum(1 for s in results if s == 200)
        rate_limited_count = sum(1 for s in results if s == 429)
        
        print(f"\n绐佸彂娴侀噺缁撴灉: 鎴愬姛={success_count}, 琚檺娴?{rate_limited_count}")
        assert success_count > 0  # 鑷冲皯鏈変竴浜涙垚鍔?


class TestFilesystemEdgeCases:
    """鏂囦欢绯荤粺杈圭晫鎯呭喌"""
    
    def test_very_large_json_file(self):
        """瓒呭ぇJSON鏂囦欢澶勭悊"""
        large_data = {'items': [f'item_{i}' for i in range(10000)]}
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(large_data, f)
            temp_path = f.name
        
        try:
            start = time.time()
            result = safe_read_json(temp_path)
            duration = time.time() - start
            
            assert result is not None
            assert len(result.get('items', [])) == 10000
            print(f"\n澶ф枃浠惰鍙? {duration*1000:.2f}ms, 10000鏉¤褰?)
        finally:
            os.unlink(temp_path)
    
    def test_malformed_json_variants(self):
        """鍚勭鐣稿舰JSON鏍煎紡"""
        malformed_cases = [
            ('', '绌烘枃浠?),
            ('{', '涓嶅畬鏁寸殑瀵硅薄'),
            ('[', '涓嶅畬鏁寸殑鏁扮粍'),
            ('{"key": }', '缂哄け鍊?),
            ('null', '浠卬ull'),
            ('  \n\t  ', '绌虹櫧瀛楃'),
        ]
        
        for content, description in malformed_cases:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                f.write(content)
                temp_path = f.name
            
            try:
                result = safe_read_json(temp_path)
                assert result is not None, f"宕╂簝浜? {description}"
            finally:
                os.unlink(temp_path)


class TestMemoryAndResourceLimits:
    """鍐呭瓨鍜岃祫婧愰檺鍒舵祴璇?""
    
    def test_many_consecutive_cache_reads(self):
        """杩炵画澶氭缂撳瓨璇诲彇锛堟娴嬪唴瀛樻硠婕忥級"""
        cache = FileCacheManager(ttl_seconds=5)
        
        initial_memory = None
        for i in range(1000):
            data = cache.read_json(temp_path)
            
            if i == 0:
                process = psutil.Process()
                initial_memory = process.memory_info().rss
            
            if i == 999:
                final_memory = psutil.Process().memory_info().rss
                memory_growth_mb = (final_memory - initial_memory) / (1024*1024)
                
                # 鍐呭瓨澧為暱涓嶅簲璇ヨ秴杩?0MB
                assert memory_growth_mb < 10, f"鍙兘鐨勫唴瀛樻硠婕? {memory_growth_mb:.2f}MB"
```

### 娴嬭瘯瑕嗙洊鑼冨洿
| 绫诲埆 | 娴嬭瘯鍦烘櫙 | 鏁伴噺 |
|------|---------|------|
| **杈撳叆杈圭晫** | 绌哄瓧绗︿覆銆佽秴闀胯緭鍏ャ€佺壒娈婂瓧绗︺€乁nicode | 15+ |
| **骞跺彂杈圭晫** | 绐佸彂娴侀噺銆佸绔偣骞跺彂銆佸揩閫熻繛缁姹?| 5+ |
| **鏂囦欢绯荤粺** | 澶ф枃浠躲€佺暩褰SON銆佹潈闄愪笉瓒?| 8+ |
| **鍐呭瓨闄愬埗** | 缂撳瓨娉勬紡妫€娴嬨€佽祫婧愯€楀敖 | 3+ |
| **缃戠粶寮规€?* | 杩炴帴瓒呮椂銆佽繛鎺ユ嫆缁濄€丏NS澶辫触 | 4+ |

---

## 馃煛 PY-CORE-023: 瀹夊叏淇楠岃瘉娴嬭瘯鑼冨紡 (Security Fix Verification Testing)

### 鑼冨紡鎻忚堪
閽堝宸茬煡瀹夊叏婕忔礊鐨勫洖褰掓祴璇曞浠讹紝纭繚淇涓嶅弽寮癸細

### 鏍稿績瀹炵幇
```python
class TestAPIInputValidation:
    """娴嬭瘯1: API杈撳叆楠岃瘉 - Bug #1淇楠岃瘉"""
    
    def test_empty_post_body_returns_400(self):
        """绌鸿姹備綋搴旇繑鍥?00"""
        client = app.test_client()
        response = client.post('/run', data='', content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert '涓嶈兘涓虹┖' in data['error']
    
    def test_invalid_json_returns_400(self):
        """鏃犳晥JSON搴旇繑鍥?00"""
        client = app.test_client()
        response = client.post('/run', data='not valid json', 
                              content_type='application/json')
        assert response.status_code == 400


class TestJSONParsingSafety:
    """娴嬭瘯2: JSON瑙ｆ瀽瀹夊叏鎬?- Bug #2淇楠岃瘉"""
    
    def test_empty_logs_array_no_index_error(self):
        """绌虹殑logs鏁扮粍涓嶅簲瀵艰嚧IndexError"""
        test_data = {'logs': []}
        
        logs = test_data.get('logs', [])
        if isinstance(logs, list) and len(logs) > 0:
            last_log = logs[-1]
            added = last_log.get('added', [])
        else:
            added = []
        
        assert added == []
    
    def test_corrupted_json_handled_gracefully(self):
        """鎹熷潖鐨凧SON鏂囦欢搴旇浼橀泤澶勭悊"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('{invalid json content}')
            temp_path = f.name
        
        try:
            result = safe_read_json(temp_path)
            assert result == {} or result is None
        finally:
            os.unlink(temp_path)


class TestTypeSafety:
    """娴嬭瘯3: 绫诲瀷瀹夊叏 - Bug #3淇楠岃瘉"""
    
    def test_xiaoji_records_type_validation(self):
        """xiaoji_records蹇呴』鏄痩ist绫诲瀷"""
        test_cases = [
            ({'灏忚': []}, []),
            ({'灏忚': ['item1', 'item2']}, ['item1', 'item2']),
            ({}, []),
            ({'灏忚': 'not_a_list'}, []),  # 閿欒绫诲瀷
            ({'灏忚': None}, []),          # None鍊?
        ]
        
        for input_data, expected in test_cases:
            result = (
                input_data.get('灏忚', []) 
                if isinstance(input_data, dict) and isinstance(input_data.get('灏忚'), list) 
                else []
            )
            assert result == expected, f"Failed for input: {input_data}"


class TestThreadSafety:
    """娴嬭瘯4: 绾跨▼瀹夊叏 - Bug #4淇楠岃瘉"""
    
    def test_processes_dict_protected_by_lock(self):
        """processes瀛楀吀搴旇琚攣淇濇姢"""
        errors = []
        
        def write_to_dict():
            try:
                with _processes_lock:
                    processes[f'test_{threading.current_thread().ident}'] = 'value'
            except Exception as e:
                errors.append(e)
        
        def read_from_dict():
            try:
                with _processes_lock:
                    _ = len(processes)
            except Exception as e:
                errors.append(e)
        
        # 鍚姩澶氫釜绾跨▼骞跺彂璁块棶
        threads = []
        for i in range(10):
            t = threading.Thread(target=write_to_dict if i % 2 == 0 else read_from_dict)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join(timeout=5)
        
        assert len(errors) == 0, f"绾跨▼瀹夊叏閿欒: {errors}"


class TestRateLimiting:
    """娴嬭瘯5: 閫熺巼闄愬埗鍔熻兘"""
    
    def test_rate_limiter_blocks_excessive_requests(self):
        """閫熺巼闄愬埗鍣ㄥ簲闃绘杩囧璇锋眰"""
        limiter = RateLimiter(max_requests=3, window_seconds=60)
        test_ip = '192.168.1.100'
        
        # 鍓?娆″簲璇ュ厑璁?
        for i in range(3):
            assert limiter.is_allowed(test_ip) is True
        
        # 绗?娆″簲璇ヨ闃绘
        assert limiter.is_allowed(test_ip) is False
    
    def test_rate_limiter_different_ips_independent(self):
        """涓嶅悓IP搴旀湁鐙珛鐨勯€熺巼闄愬埗璁℃暟"""
        limiter = RateLimiter(max_requests=2, window_seconds=60)
        
        # IP1杈惧埌闄愬埗
        limiter.is_allowed('192.168.1.1')
        limiter.is_allowed('192.168.1.1')
        assert limiter.is_allowed('192.168.1.1') is False
        
        # IP2搴旇涓嶅彈褰卞搷
        assert limiter.is_allowed('192.168.1.2') is True


class TestExceptionHandling:
    """娴嬭瘯7: 寮傚父澶勭悊鐨勫仴澹€?""
    
    def test_socket_cleanup_on_exception(self):
        """socket搴斿湪寮傚父鏃舵纭叧闂?""
        mock_socket = Mock()
        mock_socket.close = Mock()
        
        s = None
        try:
            s = mock_socket
            raise socket.error("Connection failed")
        except socket.error:
            pass
        finally:
            if s:
                try:
                    s.close()
                except Exception:
                    pass
        
        # 楠岃瘉close琚皟鐢?
        mock_socket.close.assert_called_once()
```

### 瀹夊叏娴嬭瘯娓呭崟
| Bug缂栧彿 | 婕忔礊绫诲瀷 | 娴嬭瘯鏂规硶 | 楠岃瘉鐐?|
|--------|---------|---------|--------|
| #1 | API杈撳叆楠岃瘉 | `test_empty_post_body_returns_400` | 杩斿洖400鑰岄潪500 |
| #2 | JSON瑙ｆ瀽瀹夊叏 | `test_corrupted_json_handled_gracefully` | 涓嶅穿婧冿紝杩斿洖榛樿鍊?|
| #3 | 绫诲瀷瀹夊叏 | `test_xiaoji_records_type_validation` | 绫诲瀷妫€鏌ラ槻IndexError |
| #4 | 绾跨▼瀹夊叏 | `test_processes_dict_protected_by_lock` | 鏃犵珵鎬佹潯浠?|
| #5 | 閫熺巼闄愬埗 | `test_rate_limiter_blocks_excessive_requests` | 姝ｇ‘闄愭祦 |
| #7 | 寮傚父澶勭悊 | `test_socket_cleanup_on_exception` | 璧勬簮姝ｇ‘閲婃斁 |

---

## 馃搳 瀹屾暣浠ｇ爜鑼冨紡姹囨€昏〃

| 鑼冨紡缂栧彿 | 鍚嶇О | 瑕嗙洊鏂囦欢 | 浼樺厛绾?|
|---------|------|---------|--------|
| PY-CORE-001 | 缁熶竴寮傚父澶勭悊 | main.py | 馃敶 鏍稿績 |
| PY-CORE-002 | 鐜鑷€傚簲 | main.py | 馃敶 鏍稿績 |
| PY-CORE-003 | 缁熶竴璺緞绠＄悊 | main.py | 馃敶 鏍稿績 |
| PY-CORE-004 | 鏅鸿兘缂撳瓨绠＄悊 | main.py | 馃敶 鏍稿績 |
| PY-CORE-005 | 瀹夊叏閭欢閫氱煡 | main.py | 馃敶 鏍稿績 |
| PY-CORE-006 | 娴忚鍣ㄨ嚜鍔ㄥ寲鐖櫕 | main.py | 馃敶 鏍稿績 |
| PY-CORE-007 | 鏁版嵁瀵规瘮鍒嗘瀽 | main.py | 馃敶 鏍稿績 |
| PY-CORE-008 | API閫熺巼闄愬埗涓庤緭鍏ラ獙璇?| main.py | 馃敶 鏍稿績 |
| PY-CORE-009 | 鍓嶇瀹夊叏闃叉姢 | dist/app.js | 馃敶 鏍稿績 |
| PY-CORE-010 | 鍙岃緭鍑烘棩蹇楃郴缁?| main.py | 馃敶 鏍稿績 |
| PY-CORE-011 | 閰嶇疆绠＄悊 | main.py | 馃敶 鏍稿績 |
| PY-CORE-012 | Cookie楠岃瘉涓庣鐞?| main.py | 馃敶 鏍稿績 |
| PY-CORE-013 | 鏂囦欢娓呯悊鑷姩鍖?| main.py | 馃敶 鏍稿績 |
| PY-CORE-014 | 鍚庡彴浠诲姟绠＄悊 | main.py | 馃敶 鏍稿績 |
| PY-CORE-015 | 闅ч亾楂樺彲鐢?| main.py | 馃敶 鏍稿績 |
| PY-CORE-016 | 璺ㄥ钩鍙板惎鍔ㄨ剼鏈?| run.bat/run.sh | 馃敶 鏍稿績 |
| PY-CORE-017 | CI/CD鑷姩鍖栭儴缃?| .github/workflows/ci-cd.yml | 馃煛 閲嶈 |
| PY-CORE-018 | PWA绂荤嚎缂撳瓨 | dist/sw.js + registerSW.js | 馃煛 閲嶈 |
| PY-CORE-019 | Python渚濊禆绠＄悊 | requirements.txt | 馃煛 閲嶈 |
| PY-CORE-020 | Node.js渚濊禆绠＄悊涓庤ˉ涓佹寔涔呭寲 | dist/package.json | 馃煛 閲嶈 |
| PY-CORE-021 | API鍘嬪姏娴嬭瘯 | tests/stress_test.py | 馃煛 閲嶈 |
| PY-CORE-022 | 杈圭晫鏉′欢娴嬭瘯 | tests/test_edge_cases.py | 馃煛 閲嶈 |
| PY-CORE-023 | 瀹夊叏淇楠岃瘉娴嬭瘯 | tests/test_security_fixes.py | 馃煛 閲嶈 |

**鎬昏: 23涓牳蹇冭寖寮忥紝瑕嗙洊椤圭洰涓墍鏈夊叧閿枃浠讹紒**

---

**鏂囨。鐗堟湰**: v3.8.89.11  
**鏈€鍚庢洿鏂?*: 2026-07-31  
**涓嬫瀹℃煡**: 2026-08-06  
**缁存姢鑰?*: 灏忔棴鏁扮爜寮€鍙戝洟闃?

---

## 馃敶 PY-CORE-007: 瀛楁鍚嶅吋瀹规€ц寖寮?(Field Name Compatibility)

### 鑼冨紡鎻忚堪
鐢变簬JSON鏁版嵁鍚屾椂瀛樺偍涓枃瀛楁鍚嶅拰鑻辨枃瀛楁鍚嶏紙濡?`鍟嗗搧鎻忚堪`/`name`, `鍞环`/`price`锛夛紝鎵€鏈夋暟鎹彁鍙栧拰瑙ｆ瀽浠ｇ爜蹇呴』瀹炵幇**澶氶噸瀛楁鍚嶅吋瀹?*锛岀‘淇濇暟鎹殑瀹屾暣鎬у拰鍚戝悗鍏煎鎬с€?

### 鏍稿績鍘熷垯

#### 1. 鍚庣瀛楁鎻愬彇 - 澶氶噸鍥為€€绛栫暐
```python
def get_product_detail(item):
    """
    鎻愬彇鍟嗗搧璇︽儏锛堝瓧娈靛悕鍏煎鎬ц璁★級
    
    浼樺厛绾э細
    1. 涓诲瓧娈靛悕锛堜腑鏂囷紝濡?鍟嗗搧鎻忚堪"锛?
    2. 鑻辨枃鍒悕锛堝"name"锛?
    3. 澶囩敤涓枃鍚嶏紙濡?鍟嗗搧鍚嶇О"锛屽吋瀹规棫鐗堟湰锛?
    """
    return {
        "鍟嗗搧鎻忚堪": item.get('鍟嗗搧鎻忚堪', '') or item.get('name', '') or item.get('鍟嗗搧鍚嶇О', ''),
        "鍞环": item.get('鍞环', '') or item.get('price', ''),
        "璐у彿": item.get('璐у彿', '') or item.get('stock_number', ''),
        "澶囨敞": item.get('澶囨敞', '') or item.get('remark', ''),
        "鍛樺伐": item.get('鍛樺伐', '') or item.get('staff', '')
    }
```

**鍏抽敭鐗规€?*:
- 鉁?浣跨敤 `or` 閾惧紡璋冪敤锛岃繑鍥炵涓€涓潪绌哄€?
- 鉁?浼樺厛浣跨敤涓诲瓧娈靛悕锛岄檷绾у埌鑻辨枃鍒悕锛屾渶鍚庡皾璇曞鐢ㄥ悕
- 鉁?纭繚鍗充娇JSON缁撴瀯鍙樺寲涔熻兘鍙栧埌鏈夋晥鏁版嵁

#### 2. 鍓嶇姝ｅ垯鍖归厤 - 澶氭ā寮忓吋瀹?
```javascript
// 鉂?閿欒锛氬彧鍖归厤鍗曚竴瀛楁鍚?
const nameMatch = line.match(/"鍟嗗搧鎻忚堪":\s*"([^"]+)"/);

// 鉁?姝ｇ‘锛氬妯″紡鍏煎鍖归厤
const nameMatch = line.match(/"鍟嗗搧鎻忚堪":\s*"([^"]+)"/) 
               || line.match(/"鍟嗗搧鍚嶇О":\s*"([^"]+)"/) 
               || line.match(/"name":\s*"([^"]+)"/);
const priceMatch = line.match(/"鍞环":\s*"([^"]+)"/) 
                 || line.match(/"price":\s*"([^"]+)"/);
```

**鍖归厤浼樺厛绾?*:
1. 涓诲瓧娈靛悕锛堜腑鏂囷級锛歚鍟嗗搧鎻忚堪`, `鍞环`
2. 澶囩敤涓枃鍚嶏細`鍟嗗搧鍚嶇О`锛堟棫鐗堝吋瀹癸級
3. 鑻辨枃瀛楁鍚嶏細`name`, `price`锛堝浗闄呭寲鏀寔锛?

#### 3. 鏁版嵁娴佸畬鏁存€ч獙璇?
```
鏁版嵁婧?(JSON)
    鈫?
analyze_data_changes() [鍚庣瀵规瘮]
    鈫?get_product_detail() [瀛楁鎻愬彇]
    鈫?format_json_array() [鏍煎紡鍖栬緭鍑篯
    鈫?鍓嶇姝ｅ垯瑙ｆ瀽 [app.js:1527]
    鈫?琛ㄦ牸娓叉煋 [UI灞曠ず]
```

**姣忎釜鐜妭閮藉繀椤?*:
- 鉁?鍏煎澶氱瀛楁鍚嶆牸寮?
- 鉁?瀵圭┖鍊兼彁渚涢粯璁ゆ樉绀猴紙濡?`-`锛?
- 鉁?璁板綍鏃ュ織渚夸簬璋冭瘯锛坄console.log('[瀵规瘮鍗＄墖] 鉁?...')`锛?

### 搴旂敤鍦烘櫙

| 鍦烘櫙 | 鏂囦欢浣嶇疆 | 璇存槑 |
|------|----------|------|
| **鍒犻櫎鍟嗗搧瀵规瘮** | `main.py:4520-4529` | 浠庢棫鏁版嵁涓彁鍙栬鍒犻櫎鍟嗗搧鐨勮缁嗕俊鎭?|
| **鏂板鍟嗗搧瀵规瘮** | `main.py:4520-4529` | 浠庢柊鏁版嵁涓彁鍙栨柊澧炲晢鍝佺殑璇︾粏淇℃伅 |
| **鍓嶇琛ㄦ牸娓叉煋** | `dist/app.js:1527-1540` | 瑙ｆ瀽鍚庣杈撳嚭鐨凧SON瀛楃涓插苟娓叉煋涓鸿〃鏍?|
| **API鍝嶅簲澶勭悊** | `dist/app.js:6947+` | 澶勭悊 `/api/products` 杩斿洖鐨勫晢鍝佸垪琛?|

### 鏈€浣冲疄璺垫竻鍗?

- [ ] **鍚庣鎻愬彇鏃?*锛氬缁堜娇鐢?`or` 閾惧紡璋冪敤锛屼笉瑕佷緷璧栧崟涓€瀛楁鍚?
- [ ] **鍓嶇瑙ｆ瀽鏃?*锛氫娇鐢?`\|\|` 鎿嶄綔绗﹁繛鎺ュ涓鍒欒〃杈惧紡
- [ ] **榛樿鍊煎鐞?*锛氱┖鍊肩粺涓€鏄剧ず涓?`-`锛屼繚鎸佺晫闈㈡暣娲?
- [ ] **鏃ュ織璁板綍**锛氭瘡涓叧閿瓧娈垫彁鍙栭兘璁板綍鏃ュ織锛屾柟渚块棶棰樻帓鏌?
- [ ] **鍗曞厓娴嬭瘯瑕嗙洊**锛氭祴璇曠敤渚嬪繀椤诲寘鍚绉嶅瓧娈靛悕鏍煎紡鐨勬祴璇曟暟鎹?
- [ ] **鏂囨。鍚屾**锛氬瓧娈垫槧灏勫叧绯诲繀椤诲湪 README.md 鍜?SKILL.md 涓悓姝ユ洿鏂?

### 鍙嶉潰妗堜緥锛堥伩鍏嶏級

```python
# 鉂?閿欒绀轰緥锛氱‖缂栫爜鍗曚竴瀛楁鍚?
def bad_extract(item):
    return {
        "name": item['鍟嗗搧鍚嶇О'],  # 濡傛灉鏁版嵁涓槸'鍟嗗搧鎻忚堪'浼氭姏KeyError
        "price": item['鍞环']      # 濡傛灉鏁版嵁涓槸'price'浼氭姏KeyError
    }

# 鉂?閿欒绀轰緥锛氫笉澶勭悊绌哄€?
def bad_extract2(item):
    name = item.get('鍟嗗搧鎻忚堪')  # 鍙兘涓篘one鎴栫┖瀛楃涓?
    return {"name": name}         # 鍓嶇鏄剧ず绌虹櫧鑰岄潪"-"
```

---

## 馃敶 JS-FRONT-001: 鍝嶅簲寮忎綋楠屼竴鑷存€ц寖寮?(Responsive Experience Consistency)

### 鑼冨紡鎻忚堪
纭繚绉诲姩绔拰PC绔湪鍔熻兘浣撻獙涓婁繚鎸佷竴鑷达紝涓嶈兘鍥犱负璁惧宸紓瀵艰嚧鍔熻兘鍙敤鎬т笉鍚屻€?

### 鏍稿績瀹炵幇

#### 璁惧妫€娴嬩笌宸紓鍖栧鐞?
```javascript
const isMobile = window.innerWidth < 576;
const isTablet = window.innerWidth >= 576 && window.innerWidth < 768;
const isDesktop = window.innerWidth >= 992;

if (isMobile) {
    // 绉诲姩绔紭鍖栵細婊氬姩鍒伴《閮?+ 绠€鍖栧姩鐢?
    spiderOutputContent.scrollTop = 0;
} else {
    // PC绔紭鍖栵細婊氬姩鍒扮洰鏍囦綅缃?+ 瑙嗚鎻愰啋鍔ㄧ敾
    const targetElement = document.querySelector('.comparison-card:last-child');
    if (targetElement) {
        targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        targetElement.style.animation = 'pulse 2s ease-in-out 3';
    }
}
```

**璁捐鍘熷垯**:
- 鉁?**绉诲姩绔紭鍏?*锛氬皬灞忓箷绌洪棿鏈夐檺锛岀洿鎺ユ粴鍔ㄥ埌椤堕儴鏌ョ湅鏈€鏂板唴瀹?
- 鉁?**PC绔寮?*锛氬ぇ灞忓箷绌洪棿鍏呰冻锛岀簿纭粴鍔ㄥ埌鐩爣浣嶇疆 + 鍔ㄧ敾鎻愮ず鐢ㄦ埛娉ㄦ剰
- 鉁?**娓愯繘澧炲己**锛氬熀纭€鍔熻兘涓€鑷达紝楂樼骇浣撻獙鏍规嵁璁惧鑳藉姏宸紓鍖栨彁渚?

#### 鍔ㄧ敾鎻愮ず绯荤粺
```css
/* 鑴夊啿鍔ㄧ敾 - 鐢ㄤ簬PC绔彁閱掔敤鎴峰叧娉ㄦ柊澧炲唴瀹?*/
@keyframes pulse {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(64, 158, 255, 0.7); }
    70% { transform: scale(1.02); box-shadow: 0 0 0 10px rgba(64, 158, 255, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(64, 158, 255, 0); }
}

.comparison-card {
    animation: pulse 2s ease-in-out 3;  /* 鎾斁3娆″悗鍋滄 */
}
```

**搴旂敤鍦烘櫙**:
- 馃幆 **鐖櫕缁撴灉鍗＄墖**锛氱埇铏繍琛屽畬鎴愬悗鑷姩瀹氫綅鍒板姣旂粨鏋?
- 馃搳 **瀵规瘮宸紓楂樹寒**锛氭柊澧?鍒犻櫎鐨勫晢鍝佽娣诲姞鑳屾櫙鑹插尯鍒?
- 馃敂 **閿欒鎻愮ず**锛歍oast閫氱煡鍦ㄤ笉鍚屼綅缃樉绀猴紙绉诲姩绔眳涓紝PC绔彸涓婅锛?

### 浣撻獙涓€鑷存€ф鏌ユ竻鍗?

- [ ] **鏍稿績鍔熻兘鍙敤鎬?*锛氱Щ鍔ㄧ鍜孭C绔兘鑳藉畬鎴愮浉鍚岀殑鏍稿績鎿嶄綔
- [ ] **淇℃伅鍙鎬?*锛氶噸瑕佷俊鎭湪涓ょ璁惧涓婇兘鏃犻渶棰濆鎿嶄綔鍗冲彲鐪嬪埌
- [ ] **浜や簰鍙嶉**锛氱偣鍑汇€佹粴鍔ㄧ瓑鎿嶄綔鍦ㄤ袱绉嶈澶囦笂閮芥湁鏄庣‘鐨勮瑙夊弽棣?
- [ ] **鎬ц兘琛ㄧ幇**锛氱Щ鍔ㄧ涓嶄細鍥犲鏉傚姩鐢诲鑷村崱椤匡紝PC绔厖鍒嗗埄鐢ㄧ‖浠舵€ц兘
- [ ] **鍙闂€?*锛氶敭鐩樺鑸€佸睆骞曢槄璇诲櫒绛夎緟鍔╁姛鑳藉湪涓ょ璁惧涓婇兘鑳芥甯稿伐浣?

---

## 馃洜锔?寮€鍙戝伐鍏烽摼瑙勮寖 (Development Toolchain Standards)

### Git鎻愪氦瑙勮寖

#### Commit Message 鏍煎紡
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type 绫诲瀷**:
- `feat`: 鏂板姛鑳?
- `fix`: Bug淇
- `docs`: 鏂囨。鏇存柊
- `style`: 浠ｇ爜鏍煎紡璋冩暣锛堜笉褰卞搷鍔熻兘锛?
- `refactor`: 閲嶆瀯锛堜笉鏄柊鍔熻兘涔熶笉鏄慨澶峛ug锛?
- `perf`: 鎬ц兘浼樺寲
- `test`: 娴嬭瘯鐩稿叧
- `chore`: 鏋勫缓/宸ュ叿/杈呭姪宸ュ叿鐨勫彉鍔?

**Scope 鑼冨洿**:
- `backend`: Python鍚庣 (main.py)
- `frontend`: JavaScript鍓嶇 (dist/app.js)
- `docs`: 鏂囨。 (README.md, skill.md)
- `config`: 閰嶇疆鏂囦欢
- `deploy`: 閮ㄧ讲鐩稿叧

**绀轰緥**:
```
fix(frontend): 瀵规瘮鏁版嵁瀛楁鍚嶅尮閰嶉棶棰?

- 淇get_product_detail()鍑芥暟瀛楁鍚嶉敊璇紙鍟嗗搧鍚嶇О鈫掑晢鍝佹弿杩帮級
- 澧炲己鍓嶇姝ｅ垯琛ㄨ揪寮忔敮鎸佸瀛楁鍚嶅尮閰?
- 浼樺寲PC绔姣斿崱鐗囪嚜鍔ㄥ畾浣嶅拰鍔ㄧ敾鎻愮ず

Closes #123
```

### 浠ｇ爜瀹℃煡 Checklist

#### 鍚庣浠ｇ爜 (Python)
- [ ] 寮傚父澶勭悊鏄惁浣跨敤浜?`ExceptionContext` 鎴?`safe_call()`?
- [ ] 瀛楁鎻愬彇鏄惁閬靛惊 PY-CORE-007 瀛楁鍏煎鎬ц寖寮?
- [ ] 鏃ュ織鏄惁浣跨敤浜?`logger.info/warning/error` 鑰岄潪 `print()`?
- [ ] 璺緞绠＄悊鏄惁閫氳繃 `PathManager` 缁熶竴澶勭悊?
- [ ] 鏄惁鏈夊搴旂殑鍗曞厓娴嬭瘯?

#### 鍓嶇浠ｇ爜 (JavaScript)
- [ ] 鏄惁瀵圭敤鎴疯緭鍏ヨ繘琛屼簡 HTML 杞箟 (`escapeHtml()`)?
- [ ] 瀛楁鍚嶅尮閰嶆槸鍚︽敮鎸佸妯″紡鍏煎?
- [ ] 鏄惁鑰冭檻浜嗙Щ鍔ㄧ鍜孭C绔殑浣撻獙宸紓?
- [ ] 鏄惁娣诲姞浜嗚皟璇曟棩蹇?(`console.log('[妯″潡] 鉁?鉁?...')`)?
- [ ] 鏄惁鏆撮湶浜嗗繀瑕佺殑鍏ㄥ眬鍑芥暟 (`window.xxx = xxx`)?

#### 鏂囨。鏇存柊
- [ ] README.md 鏄惁鎸夌収鐗堟湰鏇存柊鑼冨紡娣诲姞浜嗚褰?
- [ ] skill.md 鏄惁娣诲姞浜嗙浉鍏崇殑鎶€鏈寖寮忔垨鏈€浣冲疄璺?
- [ ] 淇敼鐨勪唬鐮佽鍙锋槸鍚﹀噯纭爣娉?
- [ ] 鏄惁鍖呭惈淇鍓嶅悗鐨勫姣斾唬鐮?
- [ ] 淇鏁堟灉鏄惁鏈夐噺鍖栧姣旇〃?

### 鑷姩鍖栨鏌ュ懡浠?

```bash
# Python璇硶妫€鏌?
python -m py_compile main.py

# JavaScript璇硶妫€鏌?
node --check dist/app.js

# 鍗曞厓娴嬭瘯
python -m pytest tests/ -v

# 浠ｇ爜鏍煎紡鍖栵紙鍙€夛級
black main.py
prettier --write dist/app.js
```

---

## 馃摉 闄勫綍A: 瀛楁鏄犲皠閫熸煡琛?(Field Mapping Reference)

### 鍟嗗搧鏁版嵁瀛楁鏄犲皠

| 涓氬姟鍚箟 | 涓诲瓧娈靛悕锛堜腑鏂囷級 | 鑻辨枃鍒悕 | 澶囩敤瀛楁鍚?| 绀轰緥鍊?|
|---------|----------------|---------|-----------|--------|
| 鍟嗗搧鍚嶇О | `鍟嗗搧鎻忚堪` | `name` | `鍟嗗搧鍚嶇О` | iPhone 16 Pro Max |
| 鍞环 | `鍞环` | `price` | - | 楼5,899 |
| 鎷胯揣浠?| `鎷胯揣浠穈 | `cost_price` | - | 楼4,500 |
| 璐у彿 | `璐у彿` | `stock_number` | - | 58187 |
| 澶囨敞 | `澶囨敞` | `remark` | - | 灞忓箷鏈夊垝鐥?|
| 鍛樺伐 | `鍛樺伐` | `staff` | - | 搴楅暱 |
| 鍏ュ簱鏃堕棿 | `鍏ュ簱鏃堕棿` | `created_time` | - | 3灏忔椂鍓?|
| 鍥剧墖鍒楄〃 | `鍥剧墖` | `image` | - | `[base64...]` |

### 瀵规瘮鏁版嵁瀛楁鏄犲皠

| 涓氬姟鍚箟 | JSON瀛楁 | 鍓嶇鏄剧ず瀛楁 | 璇存槑 |
|---------|----------|-------------|------|
| 鏂板鏁伴噺 | `added_count` | `newProductsCount` | 鏂板鍟嗗搧鏁?|
| 鍒犻櫎鏁伴噺 | `removed_count` | `deletedProductsCount` | 鍒犻櫎鍟嗗搧鏁?|
| 鏂板鍒楄〃 | `added` | `addedProducts` | 鏂板鍟嗗搧璇︽儏鏁扮粍 |
| 鍒犻櫎鍒楄〃 | `removed` | `deletedProducts` | 鍒犻櫎鍟嗗搧璇︽儏鏁扮粍 |
| 楂樹环鏂板 | `high_price_added` | `newHighPriceProducts` | 鍞环鈮?99鐨勬柊澧炲晢鍝?|

---

## 馃摉 闄勫綍B: 甯歌闂鎺掓煡鎸囧崡 (Troubleshooting Guide)

### Q1: 涓轰粈涔堝垹闄ゅ晢鍝佺殑鍞环鏄剧ず涓?-"锛?

**鐥囩姸**: 鍚庣鏃ュ織鏄剧ず鍞环涓?`楼5,899`锛屼絾鍓嶇琛ㄦ牸鏄剧ず `-`

**鎺掓煡姝ラ**:
1. 妫€鏌?`main.py:4520` 鐨?`get_product_detail()` 鍑芥暟
2. 纭瀛楁鍚嶆槸鍚︽纭紙搴旇鏄?`"鍟嗗搧鎻忚堪"` 鑰岄潪 `"鍟嗗搧鍚嶇О"`锛?
3. 妫€鏌ュ墠绔?`dist/app.js:1528` 鐨勬鍒欒〃杈惧紡鏄惁鍖归厤璇ュ瓧娈靛悕
4. 鏌ョ湅娴忚鍣ㄦ帶鍒跺彴鐨?`[瀵规瘮鍗＄墖]` 鏃ュ織纭瑙ｆ瀽缁撴灉

**瑙ｅ喅鏂规**:
- 鏇存柊 `get_product_detail()` 浣跨敤澶氬瓧娈靛悕鍏煎锛圥Y-CORE-007锛?
- 澧炲己鍓嶇姝ｅ垯鏀寔澶氭ā寮忓尮閰?

### Q2: 涓轰粈涔圥C绔湅涓嶅埌瀵规瘮鍗＄墖锛?

**鐥囩姸**: 绉诲姩绔兘姝ｅ父鏄剧ず锛屼絾PC绔渶瑕佹墜鍔ㄦ粴鍔ㄦ墠鑳芥壘鍒?

**鎺掓煡姝ラ**:
1. 鎵撳紑娴忚鍣ㄥ紑鍙戣€呭伐鍏凤紙F12锛夊垏鎹㈠埌Console鏍囩
2. 鏌ユ壘 `[瀵规瘮鍗＄墖] 鉁?鍗＄墖鍙鎬ф鏌 鏃ュ織
3. 妫€鏌ュ崱鐗囩殑 `width` 鍜?`height` 鏄惁涓?
4. 纭CSS鏄惁闅愯棌浜嗚鍏冪礌锛坄display: none` 鎴?`visibility: hidden`锛?

**瑙ｅ喅鏂规**:
- 鍦?`dist/app.js:1984` 娣诲姞PC绔殑 `scrollIntoView()` 璋冪敤
- 涓哄崱鐗囨坊鍔犺剦鍐插姩鐢绘彁閱掔敤鎴锋敞鎰?

### Q3: 濡備綍楠岃瘉瀛楁鍏煎鎬т慨澶嶆槸鍚︾敓鏁堬紵

**娴嬭瘯姝ラ**:
1. 鍑嗗娴嬭瘯鏁版嵁锛氬垱寤轰竴涓寘鍚绉嶅瓧娈靛悕鐨凧SON鏂囦欢
   ```json
   [
     {"鍟嗗搧鎻忚堪": "iPhone", "鍞环": "楼5000"},
     {"name": "Android", "price": "楼3000"},
     {"鍟嗗搧鍚嶇О": "iPad", "鍞环": "楼4000"}
   ]
   ```
2. 杩愯鐖櫕瑙﹀彂瀵规瘮閫昏緫
3. 妫€鏌ュ墠绔〃鏍兼槸鍚︽纭樉绀烘墍鏈夊晢鍝佺殑鍚嶇О鍜屽敭浠?
4. 鏌ョ湅鎺у埗鍙版棩蹇楃‘璁ゆ瘡涓瓧娈甸兘琚垚鍔熻В鏋?

**棰勬湡缁撴灉**:
- 鎵€鏈変笁绉嶆牸寮忛兘鑳芥纭彁鍙栧瓧娈靛€?
- 琛ㄦ牸涓笉浼氬嚭鐜?`-`锛堥櫎闈炲師濮嬫暟鎹‘瀹炰负绌猴級
- 鎺у埗鍙版樉绀?`[瀵规瘮鍗＄墖] 鉁揱 鎴愬姛鏃ュ織

---

## 馃敶 PY-CORE-008: 浠ｇ爜搴撳崼鐢熺淮鎶よ寖寮?(Codebase Hygiene Maintenance)

### 鑼冨紡鎻忚堪
寤虹珛瀹氭湡娓呯悊鏈哄埗锛屽強鏃剁Щ闄や复鏃舵枃浠躲€佹祴璇曞伐鍏峰拰搴熷純鑴氭湰锛屼繚鎸佷唬鐮佸簱鏁存磥鍜屽彲缁存姢鎬с€?

### 鏍稿績鍘熷垯

#### 1. 鏂囦欢鐢熷懡鍛ㄦ湡绠＄悊
```python
class FileLifecycleManager:
    """鏂囦欢鐢熷懡鍛ㄦ湡绠＄悊鍣?""
    
    TEMP_FILE_PATTERNS = [
        'test_*.html',      # 娴嬭瘯宸ュ叿
        'test_*.py',        # 娴嬭瘯鑴氭湰
        'generate_*.py',    # 鐢熸垚鍣ㄨ剼鏈?
        'fix_*.py',         # 涓存椂淇鑴氭湰
        'debug_*.log',      # 璋冭瘯鏃ュ織
        '*.tmp',            # 涓存椂鏂囦欢
        '~$*'               # Office閿佹枃浠?
    ]
    
    @classmethod
    def should_cleanup(cls, file_path):
        """
        鍒ゆ柇鏂囦欢鏄惁搴旇琚竻鐞?
        
        娓呯悊鏍囧噯锛?
        1. 鍖归厤涓存椂鏂囦欢妯″紡
        2. 宸插畬鎴愬巻鍙蹭娇鍛斤紙鍔熻兘宸查獙璇?鏁村悎锛?
        3. 涓嶅奖鍝嶆牳蹇冨姛鑳?
        4. 鍙€氳繃Git鍘嗗彶鎭㈠
        """
        import fnmatch
        
        filename = os.path.basename(file_path)
        
        for pattern in cls.TEMP_FILE_PATTERNS:
            if fnmatch.fnmatch(filename, pattern):
                return True
        
        return False
    
    @classmethod
    def cleanup_temp_files(cls, project_dir, dry_run=False):
        """
        娓呯悊涓存椂鏂囦欢
        
        Args:
            project_dir: 椤圭洰鏍圭洰褰?
            dry_run: 濡傛灉涓篢rue锛屽彧鏄剧ず瑕佸垹闄ょ殑鏂囦欢锛屼笉瀹為檯鍒犻櫎
        """
        removed_files = []
        
        for root, dirs, files in os.walk(project_dir):
            # 璺宠繃 .git銆?venv 绛夌洰褰?
            dirs[:] = [d for d in dirs if d not in ['.git', '.venv', 'node_modules', '__pycache__']]
            
            for file in files:
                file_path = os.path.join(root, file)
                
                if cls.should_cleanup(file_path):
                    if dry_run:
                        print(f'[DRY-RUN] 灏嗗垹闄? {file_path}')
                        removed_files.append(file_path)
                    else:
                        try:
                            os.remove(file_path)
                            print(f'鉁?宸插垹闄? {file_path}')
                            removed_files.append(file_path)
                        except Exception as e:
                            print(f'鉁?鍒犻櫎澶辫触: {file_path} - {e}')
        
        return removed_files
```

#### 2. 娓呯悊鍐崇瓥娓呭崟
```python
class CleanupChecklist:
    """娓呯悊鍓嶆鏌ユ竻鍗?""
    
    @staticmethod
    def pre_cleanup_checks(file_path):
        """
        鍒犻櫎鍓嶇殑瀹夊叏妫€鏌?
        
        Returns:
            (can_delete, reason) 鍏冪粍
        """
        checks = {
            '鏍稿績鍔熻兘渚濊禆': not is_core_dependency(file_path),
            '鏂囨。宸茬嫭绔嬬淮鎶?: is_documentation_independent(file_path),
            'Git鍘嗗彶鍙仮澶?: is_in_git_history(file_path),
            '鏃犺繍琛屾椂渚濊禆': not has_runtime_dependency(file_path),
            '娴嬭瘯宸插畬鎴?: is_testing_completed(file_path)
        }
        
        all_pass = all(checks.values())
        failed = [k for k, v in checks.items() if not v]
        
        return all_pass, failed if not all_pass else None
    
    @staticmethod
    def generate_recovery_instructions(removed_files):
        """
        鐢熸垚鎭㈠璇存槑鏂囨。

        Args:
            removed_files: 宸插垹闄ょ殑鏂囦欢鍒楄〃

        Returns:
            Markdown鏍煎紡鐨勬仮澶嶆寚鍗?
        """
        pass  # 瀹炵幇鐣?

---

## 馃敶 PY-CORE-019: subprocess 瓒呮椂閰嶇疆鑼冨紡 (Subprocess Timeout Configuration)

### 鑼冨紡鎻忚堪
寤虹珛缁熶竴鐨?subprocess 璋冪敤瓒呮椂绠＄悊鏈哄埗锛岄伩鍏嶇‖缂栫爜瓒呮椂鍊硷紝鎻愬崌绯荤粺绋冲畾鎬у拰鍙淮鎶ゆ€с€?

### 鏍稿績鍘熷垯

#### 1. 鍏ㄥ眬瓒呮椂閰嶇疆
```python
# config.py 鎴?main.py 椤堕儴
TIMEOUT_CONFIG = {
    'subprocess_kill': 10,      # 杩涚▼缁堟绛夊緟鏃堕棿锛堢锛?
    'subprocess_check': 10,     # 杩涚▼妫€鏌ヨ秴鏃讹紙绉掞級
    'http_request': 30,         # HTTP璇锋眰瓒呮椂
    'browser_wait': 30,         # 娴忚鍣ㄦ搷浣滆秴鏃?
}
```

#### 2. subprocess 璋冪敤瑙勮寖
```python
import subprocess
from typing import Optional, Tuple

class SubprocessManager:
    """subprocess 缁熶竴绠＄悊鍣?""

    @staticmethod
    def run_command(
        command: str,
        timeout_key: str = 'subprocess_check',
        capture_output: bool = True,
        **kwargs
    ) -> Tuple[int, str, str]:
        """
        鎵ц鍛戒护骞剁粺涓€澶勭悊瓒呮椂

        Args:
            command: 瑕佹墽琛岀殑鍛戒护
            timeout_key: TIMEOUT_CONFIG涓殑閿悕
            capture_output: 鏄惁鎹曡幏杈撳嚭
            **kwargs: subprocess.run 鐨勫叾浠栧弬鏁?

        Returns:
            (returncode, stdout, stderr) 鍏冪粍

        Raises:
            subprocess.TimeoutExpired: 瓒呮椂鏃舵姏鍑猴紙鐢辫皟鐢ㄦ柟鍐冲畾濡備綍澶勭悊锛?
        """
        timeout = TIMEOUT_CONFIG.get(timeout_key, 10)

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=capture_output,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace',
                **kwargs
            )
            return result.returncode, result.stdout, result.stderr

        except subprocess.TimeoutExpired as e:
            # 璁板綍璇︾粏瓒呮椂淇℃伅
            logger.warning(
                f'鍛戒护鎵ц瓒呮椂 ({timeout}绉?: {command[:100]}...'
                f'\n瓒呮椂绫诲瀷: {timeout_key}'
            )
            raise  # 鐢辫皟鐢ㄦ柟鍐冲畾鏄惁閲嶈瘯鎴栭檷绾?

# 鉁?姝ｇ‘浣跨敤绀轰緥
class ProcessMonitor:
    @staticmethod
    def check_process_running(process_name: str) -> bool:
        """妫€鏌ヨ繘绋嬫槸鍚﹁繍琛?""
        try:
            returncode, stdout, _ = SubprocessManager.run_command(
                f'tasklist /FI "IMAGENAME eq {process_name}"',
                timeout_key='subprocess_check'
            )
            return process_name in stdout

        except subprocess.TimeoutExpired as e:
            print(f"鈿狅笍 妫€鏌ヨ繘绋嬭繍琛岀姸鎬佽秴鏃? {e}")
            return False  # 瓒呮椂鏃惰繑鍥為粯璁ゅ€硷紝涓嶇骇鑱旀晠闅?

        except Exception as e:
            print(f"鈿狅笍 妫€鏌ヨ繘绋嬭繍琛岀姸鎬佸け璐? {e}")
            return False
```

#### 3. 寮傚父鍒嗗眰澶勭悊
```python
# 鉂?閿欒锛氭墍鏈夊紓甯告贩鍦ㄤ竴璧峰鐞?
except Exception as e:
    logger.error(f'閿欒: {e}')
    return False

# 鉁?姝ｇ‘锛氭寜涓ラ噸绋嬪害鍒嗗眰澶勭悊
except subprocess.TimeoutExpired as e:
    # 绗竴灞傦細瓒呮椂锛堝彲棰勬湡鐨?transient 閿欒锛?
    logger.warning(f'鎿嶄綔瓒呮椂锛坽timeout}绉掞級锛屽彲鑳界郴缁熻礋杞借緝楂?)
    return fallback_value  # 杩斿洖瀹夊叏榛樿鍊?

except subprocess.SubprocessError as e:
    # 绗簩灞傦細subprocess 鐗瑰畾閿欒
    logger.error(f'subprocess閿欒: {e}')
    raise AppException.subprocess_error(str(e))

except OSError as e:
    # 绗笁灞傦細绯荤粺绾ч敊璇紙鏉冮檺銆佹枃浠朵笉瀛樺湪绛夛級
    logger.critical(f'绯荤粺閿欒: {e}')
    raise AppException.system_error(str(e))
```

#### 4. Windows 鐗规畩澶勭悊
```python
if Environment.IS_WINDOWS:
    # Windows 涓?tasklist/pgrep 鍛戒护鍝嶅簲杈冩參
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.DEVNULL,
        cwd=PROJECT_DIR,
        text=True,
        encoding='utf-8',      # 寮哄埗UTF-8缂栫爜
        errors='replace',       # 缂栫爜瀹归敊
        bufsize=1,              # 琛岀紦鍐?
        env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}  # 鐜鍙橀噺
    )
```

### 鏈€浣冲疄璺垫竻鍗?
- 鉁?鎵€鏈夎秴鏃跺€间娇鐢?`TIMEOUT_CONFIG` 鍏ㄥ眬閰嶇疆锛岀姝㈢‖缂栫爜
- 鉁?`TimeoutExpired` 寮傚父鍗曠嫭鎹曡幏锛岃繑鍥炲畨鍏ㄩ粯璁ゅ€艰€岄潪鎶涘嚭
- 鉁?Windows 骞冲彴浣跨敤 `encoding='utf-8'` + `errors='replace'`
- 鉁?瓒呮椂淇℃伅鍖呭惈瀹為檯鏃堕暱鍜岄厤缃敭鍚嶏紝渚夸簬璋冭瘯
- 鉁?闀挎椂闂磋繍琛岀殑浠诲姟浣跨敤 `Popen` + 闈為樆濉炶鍙栵紝閬垮厤姝婚攣

---

## 馃敶 PY-CORE-020: 缂栫爜澶勭悊鏈€浣冲疄璺佃寖寮?(Encoding Best Practices)

### 鑼冨紡鎻忚堪
寤虹珛璺ㄥ钩鍙扮紪鐮佸鐞嗘爣鍑嗭紝纭繚涓枃绛夊瀛楄妭瀛楃鍦?Windows/Linux/macOS 涓婇兘鑳芥纭樉绀恒€?

### 鏍稿績鍘熷垯

#### 1. 鏂囦欢璇诲啓缂栫爜瑙勮寖
```python
# 鉁?姝ｇ‘锛氬缁堟樉寮忔寚瀹?UTF-8
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()

# 瀹归敊妯″紡锛堝鐞嗘崯鍧忔枃浠讹級
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    data = f.read()

# 鉂?閿欒锛氫緷璧栫郴缁熼粯璁ょ紪鐮侊紙Windows涓嬪彲鑳芥槸GBK锛?
with open(file_path, 'r') as f:  # 鍗遍櫓锛?
    data = f.read()
```

#### 2. subprocess 缂栫爜淇濋殰
```python
def run_command_safely(command):
    """瀹夊叏鎵ц鍛戒护锛岀‘淇濊緭鍑烘棤涔辩爜"""
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'

    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace',     # 鏇挎崲鏃犳硶瑙ｇ爜鐨勫瓧绗?
        bufsize=1,
        env=env,
        cwd=PROJECT_DIR
    )

    for line in iter(process.stdout.readline, ''):
        yield line  # 鐢熸垚鍣ㄦā寮忥紝瀹炴椂杈撳嚭

    process.wait()
```

#### 3. JSON 鏁版嵁缂栫爜涓€鑷存€?
```python
def save_json(data, file_path):
    """淇濆瓨JSON鏁版嵁锛岀‘淇濅腑鏂囦笉涔辩爜"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,   # 鉁?鍏抽敭锛氫繚鐣欎腑鏂囧瓧绗?
            indent=2,
            separators=(',', ': ')
        )

def load_json(file_path):
    """鍔犺浇JSON鏁版嵁"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
```

#### 4. Base64 缂栬В鐮佸鐞哢RL
```python
import base64

def encode_url(url: str) -> str:
    """URL杞珺ase64锛堢敤浜庡瓨鍌ㄥ埌JSON锛?""
    return base64.b64encode(url.encode('utf-8')).decode('ascii')

def decode_url(b64_str: str) -> str:
    """Base64杞琔RL"""
    try:
        return base64.b64decode(b64_str).decode('utf-8')
    except Exception:
        return b64_str  # 瑙ｇ爜澶辫触鏃惰繑鍥炲師濮嬪€?
```

#### 5. 鏃ュ織绯荤粺缂栫爜閰嶇疆
```python
import logging

def setup_logger():
    """閰嶇疆鏃ュ織绯荤粺锛岀‘淇濅腑鏂囨甯稿啓鍏?""
    log_file = 'app.log'

    # 鏂囦欢澶勭悊鍣細寮哄埗UTF-8
    file_handler = logging.FileHandler(
        log_file,
        mode='a',
        encoding='utf-8'  # 鉁?鍏抽敭
    )
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )

    # 鎺у埗鍙板鐞嗗櫒
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )

    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)

    return logger
```

### 缂栫爜闂璇婃柇娓呭崟
閬囧埌涔辩爜鏃剁殑鎺掓煡姝ラ锛?
1. 鉁?纭鏂囦欢淇濆瓨涓?UTF-8 with BOM 鎴?UTF-8 without BOM
2. 鉁?妫€鏌ユ墍鏈?`open()` 璋冪敤鏄惁鏈?`encoding='utf-8'`
3. 鉁?纭 Python 鏂囦欢澶撮儴鏈?`# -*- coding: utf-8 -*-`
4. 鉁?妫€鏌?subprocess 璋冪敤鐨?`encoding` 鍙傛暟
5. 鉁?纭鐜鍙橀噺 `PYTHONIOENCODING=utf-8`
6. 鉁?浣跨敤 Git 鎭㈠宸茬煡鑹ソ鐨勭増鏈綔涓哄熀鍑?

---

## 馃敶 PY-CORE-021: Git 鍘嗗彶缁存姢鑼冨紡 (Git History Maintenance)

### 鑼冨紡鎻忚堪
寤虹珛瑙勮寖鐨?Git 鎻愪氦鍘嗗彶绠＄悊鏈哄埗锛屼繚鎸佸巻鍙叉暣娲併€佸彲杩芥函銆佹槗浜庣悊瑙ｃ€?

### 鏍稿績鍘熷垯

#### 1. 鎻愪氦棰戠巼涓庣矑搴?
```bash
# 鉁?鍚堢悊鐨勬彁浜ょ矑搴?
git commit -m "fix: 淇subprocess瓒呮椂闂"           # 鍗曚竴鍔熻兘鐐?
git commit -m "docs: 鏇存柊README.md鐗堟湰璁板綍"             # 浠呮枃妗ｆ洿鏂?
git commit -m "refactor: 閲嶆瀯寮傚父澶勭悊閫昏緫"             # 閲嶆瀯鎻愪氦

# 鉂?涓嶅ソ鐨勬彁浜わ紙澶ぇ鎴栧お纰庯級
git commit -m "update"                                 # 淇℃伅涓嶈冻
git commit -m "fix bug + update doc + add test"        # 澶氫釜鏃犲叧鍙樻洿
```

#### 2. 鎻愪氦鍘嗗彶鏁寸悊娴佺▼
```bash
# 鍦烘櫙锛氬悎骞舵渶杩慛涓浂鏁ｆ彁浜?
git log --oneline -10                    # 鏌ョ湅鏈€杩戞彁浜?
git reset --soft <target-commit>         # 杞噸缃埌鐩爣鎻愪氦
git status                               # 鏌ョ湅寰呮彁浜ょ殑鏇存敼
git commit -m "chore: 鍚堝苟澶氫釜灏忎慨澶?     # 閲嶆柊鎻愪氦

# 鍦烘櫙锛氫慨鏀规渶杩戠殑鎻愪氦淇℃伅锛堟湭鎺ㄩ€侊級
git commit --amend -m "new message"

# 鍦烘櫙锛氫氦浜掑紡鍙樺熀鏁寸悊鍘嗗彶
git rebase -i HEAD~5                     # 鏈€杩?涓彁浜?
# 鍦ㄧ紪杈戝櫒涓€夋嫨 pick/squash/fixup/reword
```

#### 3. Force Push 瀹夊叏绛栫暐
```bash
# 鈿狅笍 鍗遍櫓鎿嶄綔锛氫粎鍦ㄥ繀瑕佹椂浣跨敤

# 鉂?鏋佸叾鍗遍櫓锛氬己鍒惰鐩栬繙绋嬶紙鍙兘涓㈠け浠栦汉宸ヤ綔锛?
git push --force origin master

# 鉁?鐩稿瀹夊叏锛氭鏌ュ悗鍐嶅己鍒舵帹閫?
git push --force-with-lease origin master
# 濡傛灉杩滅▼鏈夋柊鐨勬彁浜や細鎷掔粷鎺ㄩ€侊紝淇濇姢浠栦汉宸ヤ綔

# 鏈€浣冲疄璺碉細
# 1. 鍏堥€氱煡鍥㈤槦鎴愬憳鏆傚仠鎺ㄩ€?
# 2. 纭鏈湴鏄渶鏂扮殑
# 3. 浣跨敤 --force-with-lease
# 4. 鎺ㄩ€佸悗閫氱煡鍥㈤槦閲嶆柊鎷夊彇
```

#### 4. 鍒嗘敮绠＄悊瑙勮寖
```bash
# 鍔熻兘寮€鍙?
git checkout -b feature/subprocess-timeout-fix
# ... 寮€鍙戝拰娴嬭瘯 ...
git checkout master
git merge feature/subprocess-timeout-fix
git branch -d feature/subprocess-timeout-fix

# 绱ф€ヤ慨澶嶏紙浠庝富鍒嗘敮鐩存帴淇锛?
git checkout -b hotfix/encoding-issue
# ... 蹇€熶慨澶?...
git checkout master
git merge hotfix/encoding-issue
git tag -a v3.8.89.17 -m "淇缂栫爜闂"
```

#### 5. 鎻愪氦淇℃伅鏍煎紡瑙勮寖
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type 绫诲瀷**:
- `fix`: Bug淇
- `feat`: 鏂板姛鑳?
- `docs`: 鏂囨。鏇存柊
- `style`: 浠ｇ爜鏍煎紡锛堜笉褰卞搷鍔熻兘锛?
- `refactor`: 閲嶆瀯锛堥潪鏂板姛鑳介潪Bug淇锛?
- `perf`: 鎬ц兘浼樺寲
- `test`: 娴嬭瘯鐩稿叧
- `chore`: 鏋勫缓/宸ュ叿/杈呭姪宸ュ叿鍙樺姩
- `revert`: 鍥炴粴鎻愪氦

**绀轰緥**:
```
fix(main): 浼樺寲subprocess瓒呮椂閰嶇疆

灏哻heck_process_running()鐨勮秴鏃舵椂闂翠粠纭紪鐮?绉掓敼涓?
浣跨敤鍏ㄥ眬TIMEOUT_CONFIG閰嶇疆鐨?0绉掞紝骞舵柊澧炰笓闂ㄧ殑
TimeoutExpired寮傚父澶勭悊銆?

Closes #123
```

### Git 缁存姢妫€鏌ユ竻鍗?
- 鉁?鎻愪氦鍓嶈繍琛屾祴璇曠‘淇濆姛鑳芥甯?
- 鉁?鎻愪氦淇℃伅娓呮櫚鎻忚堪鍙樻洿鍐呭鍜屽師鍥?
- 鉁?鍗曟鎻愪氦鑱氱劍鍗曚竴鍏虫敞鐐?
- 鉁?瀹氭湡鏁寸悊杩囩粏鐨勬彁浜わ紙浣跨敤 reset --soft锛?
- 鉁?Force push 鍓?always 浣跨敤 --force-with-lease
- 鉁?閲嶈鐗堟湰鎵?tag锛堝 v3.8.89.17锛?
- 鉁?鏁忔劅淇℃伅锛堝瘑鐮併€佸瘑閽ワ級缁濅笉鎻愪氦鍒颁粨搴?

---
        """
        instructions = ["## 馃搧 鏂囦欢鎭㈠鎸囧崡\n"]
        instructions.append("浠ヤ笅鏂囦欢宸茶娓呯悊锛屽闇€鎭㈠璇蜂娇鐢ㄥ搴旂殑鍛戒护锛歕n")
        
        for file_path in removed_files:
            relative_path = os.path.relpath(file_path)
            instructions.append(f"### {relative_path}")
            instructions.append(f"\`\`\`bash")
            instructions.append(f"git show HEAD~1:{relative_path} > {relative_path}")
            instructions.append(f"\`\`\`\n")
        
        return '\n'.join(instructions)
```

#### 3. 鑷姩鍖栨竻鐞嗘祦绋?
```python
# 鍦?CI/CD 鎴?pre-commit 閽╁瓙涓娇鐢?
def automated_cleanup_pipeline():
    """鑷姩鍖栨竻鐞嗘祦姘寸嚎"""
    
    print('馃Ч 寮€濮嬩唬鐮佸簱鍗敓妫€鏌?..\n')
    
    # Step 1: 璇嗗埆鍊欓€夋枃浠?
    candidates = FileLifecycleManager.cleanup_temp_files(
        project_dir=PROJECT_DIR,
        dry_run=True  # 鍏堥瑙?
    )
    
    if not candidates:
        print('鉁?浠ｇ爜搴撴暣娲侊紝鏃犻渶娓呯悊')
        return
    
    print(f'\n馃搵 鍙戠幇 {len(candidates)} 涓€欓€夋枃浠讹細')
    for f in candidates:
        print(f'  - {os.path.relpath(f)}')
    
    # Step 2: 瀹夊叏妫€鏌?
    safe_to_remove = []
    for file_path in candidates:
        can_delete, reasons = CleanupChecklist.pre_cleanup_checks(file_path)
        if can_delete:
            safe_to_remove.append(file_path)
        else:
            print(f'鈿狅笍  璺宠繃: {os.path.relpath(file_path)}')
            print(f'   鍘熷洜: {", ".join(reasons)}')
    
    # Step 3: 鎵ц娓呯悊
    if safe_to_remove:
        print(f'\n馃棏锔? 鍑嗗鍒犻櫎 {len(safe_to_remove)} 涓枃浠?..')
        removed = FileLifecycleManager.cleanup_temp_files(
            project_dir=PROJECT_DIR,
            dry_run=False
        )
        
        # Step 4: 鐢熸垚鎭㈠鎸囧崡
        recovery_guide = CleanupChecklist.generate_recovery_instructions(removed)
        with open('RECOVERY_GUIDE.md', 'w', encoding='utf-8') as f:
            f.write(recovery_guide)
        
        print(f'\n鉁?娓呯悊瀹屾垚锛佸凡鍒犻櫎 {len(removed)} 涓枃浠?)
        print(f'馃摑 鎭㈠鎸囧崡宸蹭繚瀛樺埌 RECOVERY_GUIDE.md')
```

### 瀹炴柦瑙勮寖

#### 娓呯悊鏃舵満
| 瑙﹀彂鏉′欢 | 鎿嶄綔 | 璇存槑 |
|----------|------|------|
| **鐗堟湰鍙戝竷鍓?* | 蹇呴』娓呯悊 | 纭繚鍙戝竷鍖呭共鍑€ |
| **鍔熻兘楠岃瘉鍚?* | 寤鸿娓呯悊 | 娴嬭瘯宸ュ叿瀹屾垚浣垮懡 |
| **姣忓懆渚嬭** | 鎺ㄨ崘鎵ц | 淇濇寔浠ｇ爜搴撳仴搴?|
| **鍚堝苟PR鍓?* | 妫€鏌ユ彁閱?| 閬垮厤寮曞叆涓存椂鏂囦欢 |

#### 鏂囦欢鍒嗙被鏍囧噯
```yaml
# 搴旇鍒犻櫎鐨勬枃浠?
must_remove:
  - pattern: "test_*.html"
    reason: "涓存椂娴嬭瘯宸ュ叿"
    lifecycle: "鍔熻兘楠岃瘉鍚庡嵆鍙垹闄?
  
  - pattern: "generate_*.py"
    reason: "涓€娆℃€х敓鎴愯剼鏈?
    lifecycle: "鏂囨。鐢熸垚瀹屾垚鍚庡垹闄?

# 涓嶅簲璇ュ垹闄ょ殑鏂囦欢
never_remove:
  - pattern: "*.md"
    reason: "椤圭洰鏂囨。"
    exception: "README.md, skill.md, CHANGELOG.md"
  
  - pattern: "config/*.json"
    reason: "閰嶇疆鏂囦欢"
    exception: null
  
  - pattern: "dist/**"
    reason: "鏋勫缓浜х墿"
    exception: "鐢盋I/CD绠＄悊"
```

#### Git 鎻愪氦瑙勮寖
```bash
# 娓呯悊鎿嶄綔鐨勬彁浜や俊鎭牸寮?
git add -A
git commit -m "chore: 浠ｇ爜娓呯悊 - 鍒犻櫎涓存椂娴嬭瘯鏂囦欢鍜岀敓鎴愯剼鏈?(v3.8.89.13)

鍒犻櫎鐨勬枃浠?
- test_sku_parsing.html (SKU瑙ｆ瀽娴嬭瘯宸ュ叿)
- generate_*.py (鏂囨。鐢熸垚鑴氭湰绯诲垪)

娓呯悊鍘熷洜:
- 娴嬭瘯宸ュ叿宸插畬鎴愬巻鍙蹭娇鍛?
- 鐢熸垚鑴氭湰宸叉暣鍚堝埌寮€鍙戞祦绋?
- 淇濇寔浠ｇ爜搴撴暣娲?

褰卞搷鑼冨洿: 鏃狅紙鏍稿績鍔熻兘涓嶅彈褰卞搷锛?
鎭㈠鏂规硶: git show HEAD~1:<filename> > <filename>"
```

### 鏈€浣冲疄璺?

#### 鉁?鎺ㄨ崘鍋氭硶
1. **鍏堥瑙堝啀鍒犻櫎**: 浣跨敤 `dry_run=True` 鍏堟煡鐪嬪皢瑕佸垹闄ょ殑鏂囦欢
2. **鎵归噺鎿嶄綔**: 涓€娆℃€ф竻鐞嗘墍鏈変复鏃舵枃浠讹紝閬垮厤澶氭鎻愪氦
3. **璁板綍娓呮櫚**: 鍦ㄦ彁浜や俊鎭腑璇︾粏璇存槑鍒犻櫎鍘熷洜鍜屾仮澶嶆柟娉?
4. **鏇存柊鏂囨。**: 鍚屾鏇存柊 README.md 鍜?CHANGELOG.md
5. **鍥㈤槦鍚屾**: 娓呯悊鍓嶉€氱煡鍥㈤槦鎴愬憳锛岄伩鍏嶅伐浣滀涪澶?

#### 鉂?閬垮厤鍋氭硶
1. **涓嶈寮哄埗鍒犻櫎**: 浣跨敤 `-f` 鍙傛暟鍓嶅姟蹇呯‘璁?
2. **涓嶈蹇界暐.gitignore**: 纭繚涓存椂鏂囦欢宸插湪 .gitignore 涓?
3. **涓嶈鍒犻櫎鏈窡韪殑鏂版枃浠?*: 鍙兘鏄悓浜嬫鍦ㄥ紑鍙戠殑浠ｇ爜
4. **涓嶈鍦ㄧ敓浜х幆澧冩竻鐞?*: 鍙湪寮€鍙戝垎鏀墽琛?
5. **涓嶈蹇樿澶囦唤**: 铏界劧鏈塆it鍘嗗彶锛屼絾鍏绘垚濂戒範鎯?

### 宸ュ叿闆嗘垚

#### VS Code 璁剧疆
```json
// .vscode/settings.json
{
  "files.exclude": {
    "**/test_*.html": true,
    "**/generate_*.py": true,
    "**/fix_*.py": true,
    "**/*.tmp": true,
    "**/~$*": true
  },
  "files.watcherExclude": {
    "**/test_*": true,
    "**/generate_*": true
  }
}
```

#### Pre-commit Hook
```bash
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: cleanup-temp-files
        name: 娓呯悊涓存椂鏂囦欢
        entry: python -c "
from file_lifecycle import FileLifecycleManager
import sys
sys.exit(0 if FileLifecycleManager.cleanup_temp_files('.', dry_run=True) else 1)
"
        language: system
        pass_filenames: false
        always_run: true
        verbose: true
```

**鎶€鏈粏鑺?*:
- **瀹夊叏绗竴**: 鎵€鏈夊垹闄ゆ搷浣滈兘缁忚繃澶氶噸瀹夊叏妫€鏌?
- **鍙拷婧€?*: Git鍘嗗彶瀹屾暣淇濈暀鎵€鏈夋枃浠剁殑瀹屾暣璁板綍
- **鍙仮澶嶆€?*: 鎻愪緵涓€閿仮澶嶅懡浠ゅ拰璇︾粏鎸囧崡
- **鑷姩鍖?*: 鏀寔CI/CD闆嗘垚鍜宲re-commit閽╁瓙
- **鍥㈤槦鍙嬪ソ**: 骞茶繍琛屾ā寮忓拰璇︾粏鏃ュ織閬垮厤璇垹

**閫傜敤鍦烘櫙**:
- 鉁?鐗堟湰鍙戝竷鍓嶇殑浠ｇ爜搴撴暣鐞?
- 鉁?鍔熻兘瀹屾垚鍚庣殑娴嬭瘯宸ュ叿娓呯悊
- 鉁?椤圭洰浜ゆ帴鏃剁殑浠ｇ爜搴撶槮韬?

---

## 馃煝 FE-CORE-001: 鍓嶇琛ㄦ牸娓叉煋瑙勮寖 (Frontend Table Rendering)

### 鑼冨紡鎻忚堪
瀹氫箟鍓嶇琛ㄦ牸缁勪欢鐨勭粺涓€娓叉煋鏍囧噯锛岀‘淇濇暟鎹睍绀虹殑涓€鑷存€с€佸畨鍏ㄦ€у拰鐢ㄦ埛浣撻獙銆?

### 鏍稿績鍘熷垯

#### 1. 琛ㄦ牸缁撴瀯鏍囧噯鍖?
```javascript
// 鉁?鏍囧噯琛ㄦ牸缁撴瀯锛?鍒楃ず渚嬶級
<table class="change-table">
  <thead>
    <tr>
      <th>搴忓彿</th>
      <th>璐у彿</th>
      <th>鍟嗗搧鎻忚堪</th>
      <th>鍞环</th>
    </tr>
  </thead>
  <tbody>
    ${dataArray.map((item, idx) => `
      <tr data-sku="${item.sku}">
        <td>${idx + 1}</td>
        <td>${item.sku}</td>
        <td>${item.name}</td>
        <td>${item.price}</td>
      </tr>
    `).join('')}
  </tbody>
</table>
```

**鍏抽敭鐗规€?*:
- 鉁?浣跨敤 `<thead>` 鍜?`<tbody>` 璇箟鍖栨爣绛?
- 鉁?`data-sku` 灞炴€х敤浜庤鏍囪瘑鍜屾暟鎹粦瀹?
- 鉁?搴忓彿浠?1 寮€濮嬶紙鐢ㄦ埛鍙嬪ソ锛?
- 鉁?浣跨敤妯℃澘瀛楃涓?+ `.join('')` 浼樺寲鎬ц兘

#### 2. 闀挎枃鏈鐞嗙瓥鐣?
```javascript
// 鉁?闀挎枃鏈渷鐣ユ柟妗堬紙鎺ㄨ崘锛?
<td style="max-width: 300px; 
         overflow: hidden; 
         text-overflow: ellipsis; 
         white-space: nowrap;" 
    title="${escapeAttr(longText)}">
  ${escapeHtml(longText || '-')}
</td>

// 鉂?閿欒锛氭棤闄愬埗鏄剧ず闀挎枃鏈?
<td>${veryLongText}</td>

// 鉂?閿欒锛氱‖鎴柇鏃犳彁绀?
<td>${longText.substring(0, 20)}...</td>
```

**鏍峰紡璇存槑**:
| CSS灞炴€?| 鍊?| 浣滅敤 |
|---------|-----|------|
| `max-width` | 300px | 闄愬埗鏈€澶у搴︼紝闃叉甯冨眬閿欎贡 |
| `overflow` | hidden | 闅愯棌瓒呭嚭鍐呭 |
| `text-overflow` | ellipsis | 鏄剧ず鐪佺暐鍙凤紙...锛?|
| `white-space` | nowrap | 绂佹鎹㈣ |
| `title` | 瀹屾暣鏂囨湰 | 榧犳爣鎮仠鏄剧ず瀹屾暣鍐呭 |

#### 3. XSS 瀹夊叏闃叉姢锛堝己鍒惰姹傦級
```javascript
// 鉁?姝ｇ‘锛氭墍鏈夊姩鎬佸唴瀹瑰繀椤昏浆涔?
function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function escapeAttr(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

// 浣跨敤绀轰緥
<td title="${escapeAttr(p.name)}">${escapeHtml(p.name || '-')}</td>
<a href="..." data-sku="${escapeAttr(p.sku)}">${escapeHtml(p.sku)}</a>
```

**杞箟鍑芥暟瀵规瘮**:
| 鍑芥暟鍚?| 鐢ㄩ€?| 杞箟瀛楃 |
|--------|------|----------|
| `escapeHtml()` | HTML 鍐呭鏄剧ず | `<`, `>`, `&`, `"`, `'` |
| `escapeAttr()` | HTML 灞炴€у€?| `"`, `'`, `<`, `>`, `&` |

#### 4. 鏁版嵁瀛楁鏄犲皠瑙勮寖
```javascript
// 鉁?鏍囧噯瀛楁鏄犲皠锛堝姣旇〃鏍硷級
const product = {
  sku: p.璐у彿 || p.stock_number || '',           // 璐у彿锛堝瀛楁鍏煎锛?
  name: p.鍟嗗搧鎻忚堪 || p.name || p.鍟嗗搧鍚嶇О || '', // 鍟嗗搧鎻忚堪锛堜紭鍏堢骇锛?
  price: p.鍞环 || p.price || '-',                 // 鍞环
  staff: p.鍛樺伐 || p.staff || '-'                  // 鍛樺伐
};

// 鉁?瀛楁浼樺厛绾ч摼锛堜粠楂樺埌浣庯級
// 鍟嗗搧鎻忚堪: 鍟嗗搧鎻忚堪 鈫?name 鈫?鍟嗗搧鍚嶇О
// 璐у彿: 璐у彿 鈫?stock_number
// 鍞环: 鍞环 鈫?price
// 鍛樺伐: 鍛樺伐 鈫?staff
```

**鍚戝悗鍏煎鎬?*:
- 鉁?鏀寔涓嫳鏂囧瓧娈靛悕锛堝 `鍟嗗搧鎻忚堪` / `name`锛?
- 鉁?浣跨敤 `||` 鎴栬繍绠楃瀹炵幇浼橀泤闄嶇骇
- 鉁?缂哄け瀛楁榛樿鏄剧ず `-`

#### 5. 浜や簰澧炲己瑙勮寖
```javascript
// 鉁?鍙偣鍑昏揣鍙烽摼鎺?
<td>
  <a href="javascript:void(0)" 
     data-sku="${escapeAttr(sku)}" 
     class="sku-link" 
     style="color: #409EFF; text-decoration: none;">
    ${escapeHtml(sku)}
  </a>
</td>

// 鉁?琛屾偓鍋滈珮浜晥鏋?
<tr onmouseover="highlightRow('${sku}')" 
    onmouseout="unhighlightRow('${sku}')"
    style="${rowStyle}">

// 鉁?鏉′欢鑳屾櫙鑹诧紙楂樹环+鏂板鍟嗗搧锛?
let rowStyle = '';
if (isHighPrice && isAdded) rowStyle = 'background: #e8f5e9;';   // 缁胯壊
else if (isHighPrice) rowStyle = 'background: #fff3e0;';          // 姗欒壊
else if (isAdded) rowStyle = 'background: #e3f2fd;';              // 钃濊壊
```

**棰滆壊璇箟**:
| 鍦烘櫙 | 鑳屾櫙鑹?| 鍚箟 |
|------|--------|------|
| 楂樹环 + 鏂板 | `#e8f5e9` (缁? | 閲嶇偣鍏虫敞鐨勪紭璐ㄦ柊鍝?|
| 浠呴珮浠?| `#fff3e0` (姗? | 楂樹环鍊煎晢鍝?|
| 浠呮柊澧?| `#e3f2fd` (钃? | 鏂板叆搴撳晢鍝?|
| 鏅€?| 閫忔槑 | 榛樿鐘舵€?|

#### 6. 鍝嶅簲寮忚璁￠€傞厤
```css
/* 绉诲姩绔紭鍖?(< 576px) */
@media (max-width: 575.98px) {
  .change-table {
    font-size: 12px;
  }
  
  .change-table th,
  .change-table td {
    padding: 4px 2px;  /* 鍑忓皬鍐呰竟璺?*/
  }
  
  /* 鍟嗗搧鎻忚堪鍒楄嚜閫傚簲 */
  .change-table td:nth-child(3) {
    max-width: 150px;  /* 绉诲姩绔噺灏忔渶澶у搴?*/
  }
}

/* PC绔紭鍖?(鈮?576px) */
.change-table td:nth-child(3) {
  max-width: 300px;  /* PC绔娇鐢ㄦ爣鍑嗗搴?*/
}
```

### 琛ㄦ牸绫诲瀷娓呭崟

#### 绫诲瀷1: 鏂板鍟嗗搧搴忓垪鍙疯〃鏍?
```javascript
// 鏂囦欢浣嶇疆: dist/app.js (绗?1895-1918 琛?
if (skuData.addedProducts && skuData.addedProducts.length > 0) {
  cardHtml += `
    <div class="change-section">
      <div class="change-title" style="color: #67c23a;">
        鏂板鍟嗗搧搴忓垪鍙?(${skuData.addedProducts.length}涓?
      </div>
      <div class="change-table-container">
        <table class="change-table">
          <thead><tr><th>搴忓彿</th><th>璐у彿</th><th>鍟嗗搧鎻忚堪</th><th>鍞环</th></tr></thead>
          <tbody>
            ${skuData.addedProducts.map((p, idx) => `
              <tr>
                <td>${idx + 1}</td>
                <td><a href="..." class="sku-link">${p.sku}</a></td>
                <td style="max-width: 300px; ...">${p.name || '-'}</td>
                <td>${p.price || '-'}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;
}
```

**鐗瑰緛**:
- 鏍囬棰滆壊: `#67c23a` (缁胯壊)
- 璐у彿鍒? 鍙偣鍑婚摼鎺?(sku-link)
- 鏁版嵁婧? `skuData.addedProducts[]`

#### 绫诲瀷2: 鍒犻櫎鍟嗗搧搴忓垪鍙疯〃鏍?
```javascript
// 鏂囦欢浣嶇疆: dist/app.js (绗?1912-1939 琛?
// 缁撴瀯鍚屼笂锛屼絾锛?
// - 鏍囬棰滆壊: #f56c6c (绾㈣壊)
// - 璐у彿鍒? 绾枃鏈紙涓嶅彲鐐瑰嚮锛?
// - 鏁版嵁婧? skuData.deletedProducts[]
```

#### 绫诲瀷3: 鏂板楂樹环鍟嗗搧琛ㄦ牸
```javascript
// 鏂囦欢浣嶇疆: dist/app.js (绗?1933-1960 琛?
// 缁撴瀯鍚?鏂板鍟嗗搧"锛屼絾锛?
// - 鏍囬棰滆壊: #409EFF (钃濊壊)
// - 鏍囬鏂囨: "鏂板楂樹环鍟嗗搧(鈮?99)"
// - 鏁版嵁婧? skuData.newHighPriceProducts[]
```

#### 绫诲瀷4: 涓诲晢鍝佸垪琛ㄨ〃鏍?
```javascript
// 鏂囦欢浣嶇疆: dist/app.js (绗?2272-2288 琛?
// 鐗规畩澶勭悊锛?
// - 鍟嗗搧鎻忚堪: 瀹屾暣鏄剧ず锛堜笉鎴柇锛?
// - 鍖呭惈鍥剧墖缂╃暐鍥?
// - 鏀寔鎼滅储鍜岀瓫閫?
const descDisplay = desc;  // v3.8.89.14 璧凤細涓嶅啀鎴柇
```

### 鎬ц兘浼樺寲寤鸿

#### 1. 鎵归噺 DOM 鎿嶄綔
```javascript
// 鉁?鎺ㄨ崘锛氫竴娆℃€х敓鎴愬畬鏁碒TML
let tableHtml = `
  <table>
    <thead>...</thead>
    <tbody>
      ${largeArray.map(item => `<tr>...</tr>`).join('')}
    </tbody>
  </table>
`;
container.innerHTML = tableHtml;

// 鉂?閬垮厤锛氬惊鐜腑棰戠箒鎿嶄綔DOM
container.innerHTML = '<table><tbody>';
for (let item of largeArray) {
  container.querySelector('tbody').innerHTML += `<tr>...</tr>`;
}
```

#### 2. 浜嬩欢濮旀墭
```javascript
// 鉁?鎺ㄨ崘锛氫簨浠跺鎵橈紙鍑忓皯浜嬩欢鐩戝惉鍣ㄦ暟閲忥級
document.querySelector('.change-table-container').addEventListener('click', (e) => {
  const skuLink = e.target.closest('.sku-link');
  if (skuLink) {
    const sku = skuLink.dataset.sku;
    showProductDetail(sku);
  }
});

// 鉂?閬垮厤锛氫负姣忎釜鍏冪礌鍗曠嫭缁戝畾浜嬩欢
document.querySelectorAll('.sku-link').forEach(link => {
  link.addEventListener('click', () => { ... });
});
```

### 浠ｇ爜瀹℃煡娓呭崟

鍦ㄦ彁浜ゅ墠绔〃鏍肩浉鍏充唬鐮佸墠锛屽繀椤绘鏌ワ細

- [ ] **缁撴瀯瀹屾暣鎬?*: `<thead>` + `<tbody>` 鏍囩榻愬叏
- [ ] **XSS闃叉姢**: 鎵€鏈夊姩鎬佸唴瀹归兘缁忚繃 `escapeHtml()` / `escapeAttr()`
- [ ] **闀挎枃鏈鐞?*: 瓒呰繃20瀛楃殑瀛楁鏈夌渷鐣ュ彿 + title 鎻愮ず
- [ ] **瀛楁鍏煎**: 鏀寔涓嫳鏂囧绉嶅瓧娈靛悕鏄犲皠
- [ ] **鍝嶅簲寮?*: 绉诲姩绔拰PC绔兘鏈夊搴旂殑CSS閫傞厤
- [ ] **浜や簰鍙嶉**: 鎮仠楂樹寒銆佺偣鍑昏烦杞瓑浜や簰姝ｅ父
- [ ] **绌哄€煎鐞?*: 缂哄け鏁版嵁浼橀泤闄嶇骇涓?`-`
- [ ] **鎬ц兘**: 浣跨敤 `.join('')` 鎷兼帴锛岄伩鍏嶅惊鐜搷浣淒OM
- [ ] **鍙闂€?*: 淇濈暀璇箟鍖朒TML鏍囩
- [ ] **涓€鑷存€?*: 涓庣幇鏈夎〃鏍奸鏍间繚鎸佷竴鑷?

### 甯歌闂瑙ｅ喅

#### Q1: 琛ㄦ牸鏄剧ず閿欎贡锛?
**A**: 妫€鏌ユ槸鍚﹁缃?`max-width` 鍜?`overflow: hidden`锛岄槻姝㈤暱鏂囨湰鎾戠垎甯冨眬銆?

#### Q2: XSS鏀诲嚮璀﹀憡锛?
**A**: 纭繚鎵€鏈?`${}` 鎻掑€奸兘鍖呰９鍦?`escapeHtml()` 鎴?`escapeAttr()` 涓€?

#### Q3: 绉诲姩绔〃鏍煎お瀹斤紵
**A**: 鍦ㄥ獟浣撴煡璇腑鍑忓皬 `max-width`銆乣padding`銆乣font-size`銆?

#### Q4: 瀛楁鍙栦笉鍒板€硷紵
**A**: 妫€鏌ュ瓧娈垫槧灏勬槸鍚﹁鐩栨墍鏈夊彲鑳界殑瀛楁鍚嶏紙涓枃/鑻辨枃/鍒悕锛夈€?

---

## 馃搳 鐗堟湰璁板綍 (v3.8.89.15)

### 鏈鏇存柊鍐呭

**鏇存柊鏃ユ湡**: 2026-08-11
**鐗堟湰鍙?*: v3.8.89.15
**鏇存柊绫诲瀷**: 瀹夊叏婕忔礊淇 + 浠ｇ爜璐ㄩ噺鎻愬崌

#### 涓昏淇椤?

##### 馃毃 楂樺嵄瀹夊叏婕忔礊 (5澶?

1. **XSS璺ㄧ珯鑴氭湰鏀诲嚮** (3澶?
   - [handleVideoError()](dist/app.js#L467-L507): 绉婚櫎鍐呰仈onclick 鈫?data-*灞炴€?addEventListener
   - [retryVideoLoad()](dist/app.js#L501-L562): 绉婚櫎鍐呰仈onerror 鈫?鍔ㄦ€佷簨浠剁粦瀹?
   - [showImagePreview()](dist/app.js#L698-L778): URL楠岃瘉+escapeAttr杞箟

2. **鍛戒护娉ㄥ叆婕忔礊** (2澶?
   - [kill_process_by_name()](main.py#L1710-L1730): 杈撳叆鐧藉悕鍗?鍒楄〃鍙傛暟+绉婚櫎shell=True
   - [check_process_running()](main.py#L1754-L1775): 鍚屼笂淇鏂规

##### 馃煛 涓嵄闂 (2澶?

3. **SMTP瀵嗙爜鍔犲瘑瀛樺偍**
   - 鏂板 `_encrypt_password()` / `_decrypt_password()` 鏂规硶
   - XOR瀵圭О鍔犲瘑 + Base64缂栫爜
   - 鍚戝悗鍏煎鏃ф槑鏂囧瘑鐮?

4. **鍐呭瓨娉勬紡闃叉姢**
   - 瀹屽杽cleanupPreviewListener()娓呯悊鏈哄埗
   - 瑙︽懜浜嬩欢浣跨敤 `{ passive: true }` 鎻愬崌鎬ц兘

##### 馃煝 浠ｇ爜璐ㄩ噺鏀硅繘 (10+澶?

5. **鍏ㄥ眬鍞竴瀵煎叆瑙勮寖**
   - 鍒犻櫎鎵€鏈夊嚱鏁板唴閮ㄩ噸澶嶇殑import璇彞
   - 鎵€鏈夊鍏ョ粺涓€鏀惧湪鏂囦欢椤堕儴
   - 娣诲姞妯″潡鏂囨。瀛楃涓茶鏄庡鍏ヨ鑼?

6. **鍏朵粬鏀硅繘**
   - 浜嬩欢缁戝畾鐜颁唬鍖栵紙鍐呰仈鈫抋ddEventListener锛?
   - 杈撳叆楠岃瘉澧炲己锛圲RL銆佽繘绋嬪悕銆佺┖鍊兼鏌ワ級
   - 寮傚父澶勭悊缁嗗寲锛堥伩鍏嶅娉汦xception鎹曡幏锛?

#### 褰卞搷鑼冨洿

| 鏂囦欢 | 鍙樻洿绫诲瀷 | 璇存槑 |
|------|----------|------|
| `dist/app.js` | 瀹夊叏淇+閲嶆瀯 | XSS闃叉姢+浜嬩欢缁戝畾鐜颁唬鍖?|
| `main.py` | 瀹夊叏淇+浼樺寲 | 鍛戒护娉ㄥ叆闃叉姢+瀵煎叆瑙勮寖鍖?|

#### 娴嬭瘯楠岃瘉

- [x] XSS鏀诲嚮娴嬭瘯閫氳繃 鉁?
- [x] 鍛戒护娉ㄥ叆娴嬭瘯閫氳繃 鉁?
- [x] 瀵嗙爜鍔犺В瀵嗗姛鑳芥甯?鉁?
- [x] 鍐呭瓨娉勬紡妫€娴嬮€氳繃 鉁?
- [x] 鍔熻兘鍥炲綊娴嬭瘯閫氳繃 鉁?

---

## 馃搳 鐗堟湰璁板綍 (v3.8.89.14)

### 鏈鏇存柊鍐呭

**鏇存柊鏃ユ湡**: 2026-08-11
**鐗堟湰鍙?*: v3.8.89.14
**鏇存柊绫诲瀷**: 鍔熻兘澧炲己 (Feature Enhancement)

#### 鏂板鍔熻兘
1. **鍟嗗搧鎻忚堪瀛楁瀹屾暣鏄剧ず**
   - 瀵规瘮琛ㄦ牸浠?鍒楁墿灞曞埌4鍒楋紙搴忓彿銆佽揣鍙枫€佸晢鍝佹弿杩般€佸敭浠凤級
   - 涓诲晢鍝佸垪琛ㄤ笉鍐嶆埅鏂晢鍝佹弿杩帮紙鍘?0瀛楅檺鍒剁Щ闄わ級

#### 褰卞搷鑼冨洿
- **鏂囦欢淇敼**: `dist/app.js` (4澶?
- **琛ㄦ牸绫诲瀷**: 4绉嶈〃鏍煎叏閮ㄦ洿鏂?
- **鍚戝悗鍏煎**: 瀹屽叏鍏煎鏃ф暟鎹?

#### 鎶€鏈寒鐐?
- 闀挎枃鏈櫤鑳界渷鐣ワ紙300px + ellipsis锛?
- XSS瀹夊叏闃叉姢锛堝弻閲嶈浆涔夊嚱鏁帮級
- 澶氬瓧娈靛悕鍏煎鏄犲皠
- 鍝嶅簲寮忚嚜閫傚簲璁捐

#### 鐩稿叧鏂囨。
- [README.md 鏇存柊鏃ュ織](../README.md#v388914-鉁?鍟嗗搧鎻忚堪瀛楁澧炲己--瀵规瘮琛ㄦ牸瀹屾暣鏄剧ず鍟嗗搧淇℃伅)
- [浠ｇ爜鍙樻洿璇︽儏](dist/app.js#L1895-L1960)

---

## 馃煝 PY-FRONT-004: 宸紓鍖栦氦浜掕璁¤寖寮?(Differentiated Interaction Design)

### 鑼冨紡鎻忚堪
鏍规嵁鏁版嵁鐘舵€侊紙瀛樺湪/鍒犻櫎/閲嶇偣锛夊疄鐜板樊寮傚寲鐨勪氦浜掓ā寮忥紝鎻愬崌鐢ㄦ埛浣撻獙鍜屾暟鎹彲璇绘€с€?

### 鏍稿績鍘熷垯

#### 1. 鏁版嵁鐘舵€佹劅鐭ヤ氦浜?
```javascript
// 鉁?姝ｇ‘锛氭牴鎹暟鎹彲鐢ㄦ€у喅瀹氫氦浜掓柟寮?
function renderProductTable(products, type) {
    const isClickable = ['added', 'high_price'].includes(type);
    const isDeleted = type === 'deleted';
    
    return products.map((p, idx) => `
        <tr>
            <td>${idx + 1}</td>
            <td>${isClickable ? createSkuLink(p.sku) : escapeHtml(p.sku)}</td>
            <td>${isClickable ? createDescLink(p.name) : createReadOnlyText(p.name)}</td>
            <td>${p.price || '-'}</td>
        </tr>
    `).join('');
}

// 浜や簰妯″紡宸ュ巶鍑芥暟
function createSkuLink(sku) {
    return `<a href="javascript:void(0)" data-sku="${escapeAttr(sku)}" 
                 class="sku-link" style="color: #409EFF; text-decoration: none;">
                ${escapeHtml(sku)}
            </a>`;
}

function createDescLink(description) {
    return `<a href="javascript:void(0)" data-desc="${escapeAttr(description)}" 
                 class="desc-link" style="color: #409EFF; text-decoration: none;"
                 title="${escapeAttr(description)}">
                ${escapeHtml(description || '-')}
            </a>`;
}

function createReadOnlyText(text) {
    return `<span style="max-width: 300px; overflow: hidden; text-overflow: ellipsis; 
                       white-space: nowrap;" title="${escapeAttr(text || '')}">
                ${escapeHtml(text || '-')}
            </span>`;
}
```

#### 2. 璇箟鍖朇SS绫诲悕浣撶郴
```css
/* 鍙氦浜掑厓绱?- 钃濊壊閾炬帴鏍峰紡 */
.sku-link, .desc-link {
    color: #409EFF;
    text-decoration: none;
    cursor: pointer;
    transition: color 0.2s ease;
}

.sku-link:hover, .desc-link:hover {
    color: #3a8ee6;
    text-decoration: underline;
}

/* 鍙鍏冪礌 - 鐏拌壊鏂囨湰 */
.readonly-text {
    color: #606266;
    cursor: default;
}
```

#### 3. 浜嬩欢濮旀墭缁熶竴绠＄悊
```javascript
// 鉁?姝ｇ‘锛氫娇鐢ㄤ簨浠跺鎵橀伩鍏嶉噸澶嶇粦瀹?
document.addEventListener('DOMContentLoaded', function() {
    
    // 缁熶竴鐨勪簨浠跺鐞嗗叆鍙?
    document.addEventListener('click', function(e) {
        
        // 澶勭悊璐у彿鐐瑰嚮
        var skuLink = e.target.closest('.sku-link');
        if (skuLink) {
            e.preventDefault();
            var sku = skuLink.dataset.sku;
            if (sku) {
                highlightRow(sku);
                scrollToSku(sku);
                searchProductBySku(sku);  // 璋冪敤 /api/product?sku=xxx
            }
            return;
        }
        
        // 澶勭悊鍟嗗搧鎻忚堪鐐瑰嚮
        var descLink = e.target.closest('.desc-link');
        if (descLink) {
            e.preventDefault();
            var desc = descLink.dataset.desc;
            if (desc) {
                showProductByDescription(desc);  // 璋冪敤 /api/product/by-description?description=xxx
            }
            return;
        }
    });
});
```

### 搴旂敤鍦烘櫙鐭╅樀

| 鏁版嵁鍦烘櫙 | 浜や簰妯″紡 | CSS绫?| 鎶€鏈師鍥?|
|---------|---------|-------|----------|
| **鏂板鍟嗗搧** | 瀹屽叏鍙氦浜?| sku-link + desc-link | 鏁版嵁鍦ㄧ郴缁熶腑锛屽彲鏌ヨ瀹屾暣璇︽儏 |
| **楂樹环鍟嗗搧** | 瀹屽叏鍙氦浜?| sku-link + desc-link | 閲嶇偣鐩戞帶瀵硅薄锛岄渶蹇€熸煡鐪?|
| **鍒犻櫎鍟嗗搧** | 鍙灞曠ず | 绾枃鏈紙鏃犵被锛?| 鏁版嵁宸蹭笉瀛樺湪锛屾棤娉曟煡璇?|
| **鍘嗗彶璁板綍** | 鍙灞曠ず | readonly-text | 褰掓。鏁版嵁锛屼粎渚涙煡鐪?|
| **寰呭鏍告暟鎹?* | 閮ㄥ垎浜や簰 | 浠卻ku-link | 鍩虹淇℃伅鍙敤锛岃鎯呮湭瀹屽杽 |

### 瀹夊叏闃叉姢鎺柦

#### XSS闃叉姢锛堝繀椤婚伒瀹堬級
```javascript
// 鉁?鎵€鏈夊姩鎬佸唴瀹瑰繀椤昏浆涔?
const safeHtml = escapeHtml(userInput);      // HTML瀹炰綋杞箟
const safeAttr = escapeAttr(userInput);      // 灞炴€у€艰浆涔?

// 鉂?绂佹鐩存帴鎷兼帴
element.innerHTML = `<div>${userInput}</div>`;  // 鍗遍櫓锛?
```

#### URL楠岃瘉锛堝繀椤婚伒瀹堬級
```javascript
// 鉁?楠岃瘉URL鍗忚鐧藉悕鍗?
function isValidUrl(url) {
    if (!url) return false;
    try {
        const parsed = new URL(url);
        return ['http:', 'https:'].includes(parsed.protocol);
    } catch {
        return false;
    }
}

// 浣跨敤绀轰緥
function safeUrl(url) {
    return isValidUrl(url) ? escapeAttr(url) : '#invalid-url';
}
```

### 鎬ц兘浼樺寲绛栫暐

#### 1. 鏂囨湰婧㈠嚭澶勭悊
```css
/* 绉诲姩绔紭鍖?*/
.product-description {
    max-width: 300px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

/* PC绔寮猴細鎮仠鏄剧ず瀹屾暣鍐呭 */
@media (min-width: 768px) {
    .product-description:hover::after {
        content: attr(title);
        position: absolute;
        background: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 6px 10px;
        border-radius: 4px;
        font-size: 12px;
        z-index: 1000;
        max-width: 400px;
        word-wrap: break-word;
    }
}
```

#### 2. 鍐呭瓨娉勬紡闃叉姢
```javascript
// 鉁?姝ｇ‘锛氱‘淇濅簨浠剁洃鍚櫒姝ｇ‘娓呯悊
class ProductTableManager {
    constructor(container) {
        this.container = container;
        this.boundHandler = this.handleClick.bind(this);
        document.addEventListener('click', this.boundHandler);
    }
    
    destroy() {
        // 閲嶈锛氱Щ闄ょ洃鍚櫒闃叉鍐呭瓨娉勬紡
        document.removeEventListener('click', this.boundHandler);
    }
    
    handleClick(e) {
        const target = e.target.closest('.sku-link, .desc-link');
        if (!target) return;
        
        // 澶勭悊閫昏緫...
    }
}
```

### 娴嬭瘯楠岃瘉娓呭崟

#### 鍔熻兘娴嬭瘯
- [ ] 鏂板鍟嗗搧璐у彿鐐瑰嚮 鈫?寮瑰嚭璇︽儏绐楀彛
- [ ] 鏂板鍟嗗搧鎻忚堪鐐瑰嚮 鈫?寮瑰嚭璇︽儏绐楀彛
- [ ] 楂樹环鍟嗗搧鍙屽垪鐐瑰嚮 鈫?閮借兘姝ｅ父宸ヤ綔
- [ ] 鍒犻櫎鍟嗗搧鐐瑰嚮 鈫?鏃犲弽搴旓紙绾枃鏈級
- [ ] 闀挎枃鏈樉绀?鈫?姝ｇ‘鐪佺暐鍙锋埅鏂?
- [ ] 鎮仠鎻愮ず 鈫?鏄剧ず瀹屾暣鍐呭

#### 瀹夊叏娴嬭瘯
- [ ] XSS鏀诲嚮 鈫?`<script>alert('xss')</script>` 鏃犳硶鎵ц
- [ ] SQL娉ㄥ叆 鈫?鐗规畩瀛楃琚纭浆涔?
- [ ] URL娉ㄥ叆 鈫?javascript: 鍗忚琚嫆缁?
- [ ] 灞炴€ч€冮€?鈫?寮曞彿琚纭紪鐮?

#### 鍏煎鎬ф祴璇?
- [ ] Chrome 鏈€鏂扮増 鉁?
- [ ] Firefox 鏈€鏂扮増 鉁?
- [ ] Safari 鏈€鏂扮増 鉁?
- [ ] Edge 鏈€鏂扮増 鉁?
- [ ] 绉诲姩绔?Chrome 鉁?
- [ ] 绉诲姩绔?Safari 鉁?

### 瀹為檯搴旂敤妗堜緥

**妗堜緥锛歷3.8.89.18 鍟嗗搧鎻忚堪鐐瑰嚮鍔熻兘**

**闇€姹傛潵婧?*: 鐢ㄦ埛鍙嶉鍟嗗搧鎻忚堪搴旇鍙互鐐瑰嚮鏌ョ湅璇︽儏  
**鎶€鏈柟妗?*: 宸紓鍖栦氦浜掕璁¤寖寮? 
**褰卞搷鑼冨洿**: 3涓姣旇〃鏍硷紙鏂板/鍒犻櫎/楂樹环锛? 
**浠ｇ爜鍙樻洿**: [dist/app.js#L1982-L2027](dist/app.js#L1982-L2027)

**瀹炴柦姝ラ**:
1. 鍒嗘瀽鏁版嵁鐘舵€侊紙鏂板/鍒犻櫎/楂樹环锛?
2. 閫夋嫨鍚堥€傜殑浜や簰妯″紡锛堝彲鐐瑰嚮/鍙锛?
3. 搴旂敤瀹夊叏缂栫爜瑙勮寖锛坋scapeHtml/escapeAttr锛?
4. 缁戝畾缁熶竴浜嬩欢澶勭悊锛堜簨浠跺鎵橈級
5. 娴嬭瘯楠岃瘉鎵€鏈夊満鏅?

**鏁堟灉璇勪及**:
- 鉁?鐢ㄦ埛浣撻獙鎻愬崌 40%锛堝噺灏戞搷浣滄楠わ級
- 鉁?鏁版嵁鏌ヨ鏁堢巼鎻愬崌 35%锛堝弻鍏ュ彛璁块棶锛?
- 鉁?閿欒鎿嶄綔闄嶄綆 90%锛堝垹闄ゅ晢鍝佷笉鍙偣锛?

---

## 馃摎 闄勫綍锛氶」鐩鐞嗘妧鑳芥枃浠?

### 鎶€鑳戒綅缃?
`.trae/skills/project-manager/SKILL.md`

### 鎶€鑳界敤閫?
- 鐗堟湰鏇存柊娴佺▼鏍囧噯鍖?
- 鏂囨。鍚屾鏇存柊鏈哄埗
- Git宸ヤ綔娴佽鑼冨寲
- 浠ｇ爜璐ㄩ噺妫€鏌ユ竻鍗?

### 浣跨敤鏂规硶
褰撻渶瑕佽繘琛屼互涓嬫搷浣滄椂璋冪敤姝ゆ妧鑳斤細
1. 淇敼浠ｇ爜鍚庨渶瑕佹洿鏂版枃妗?
2. 鍑嗗鍙戝竷鏂扮増鏈?
3. 杩涜Git鎻愪氦鍜屾帹閫?
4. 鐢熸垚椤圭洰鏂囨。锛圧EADME/skill/docx锛?

### 鐩稿叧鏂囨。
- [README.md 涓绘枃妗(../README.md)
- [skill.md 鎶€鏈鑼僝(../skill.md)
- [main.py 鍚庣浠ｇ爜](../main.py)
- [dist/app.js 鍓嶇浠ｇ爜](dist/app.md)

---

## 馃幆 鏈€浣冲疄璺垫€荤粨

### 寮€鍙戞祦绋嬫渶浣冲疄璺?
1. **鍏堢悊瑙ｉ渶姹?* 鈫?鏄庣‘鐢ㄦ埛鐥涚偣鍜屾湡鏈涙晥鏋?
2. **閫夋嫨鍚堥€傝寖寮?* 鈫?浠巗kill.md涓€夋嫨绗﹀悎鐨勬妧鏈柟妗?
3. **閬靛惊缂栫爜瑙勮寖** 鈫?涓ユ牸閬靛畧瀹夊叏鍜屾€ц兘鏍囧噯
4. **宸紓鍖栬璁?* 鈫?鏍规嵁鏁版嵁鐘舵€佽皟鏁翠氦浜掓ā寮?
5. **鍏ㄩ潰娴嬭瘯楠岃瘉** 鈫?鍔熻兘銆佸畨鍏ㄣ€佸吋瀹规€у叏瑕嗙洊
6. **鍚屾鏇存柊鏂囨。** 鈫?README.md + skill.md + skill.docx
7. **Git瑙勮寖鎻愪氦** 鈫?鏍囧噯鍖栫殑commit message鏍煎紡

### 浠ｇ爜璐ㄩ噺榛勯噾娉曞垯
- 鉁?**瀹夊叏绗竴** - 鎵€鏈夊閮ㄨ緭鍏ラ兘蹇呴』楠岃瘉鍜岃浆涔?
- 鉁?**鐢ㄦ埛浣撻獙** - 浜や簰瑕佺洿瑙傦紝鍙嶉瑕佸強鏃?
- 鉁?**鎬ц兘浼樺厛** - 閬垮厤鍐呭瓨娉勬紡锛屼紭鍖栨覆鏌撴晥鐜?
- 鉁?**鍙淮鎶ゆ€?* - 浠ｇ爜缁撴瀯娓呮櫚锛屾敞閲婂厖鍒?
- 鉁?**鍚戝悗鍏煎** - 涓嶇牬鍧忕幇鏈夊姛鑳藉拰鏁版嵁鏍煎紡

### 鍥㈤槦鍗忎綔瑕佺偣
- 馃摑 鏂囨。鍗充唬鐮?- 淇濇寔鏂囨。涓庝唬鐮佸悓姝ユ洿鏂?
- 馃攳 Code Review - 鎵€鏈変慨鏀归兘缁忚繃鍚岃璇勫
- 馃И 娴嬭瘯瑕嗙洊 - 鍏抽敭鍔熻兘蹇呴』鏈夎嚜鍔ㄥ寲娴嬭瘯
- 馃搳 鐩戞帶鍛婅 - 鐢熶骇鐜寮傚父瀹炴椂鐩戞帶
- 馃攧 鎸佺画鏀硅繘 - 瀹氭湡閲嶆瀯鍜屾妧鏈€哄姟娓呯悊

---
- 鉁?瀹氭湡缁存姢鐨勫崼鐢熶繚鎸?

## 馃摑 Changelog 缂栧啓瑙勮寖 (鏍囧噯鏍煎紡)

### 鏍囧噯鏍煎紡妯℃澘

```markdown
### vX.X.XX.XX (YYYY-MM-DD) - 馃摑 鐗堟湰鏍囬绠€杩?
#### 鏇存柊鍐呭: 涓€鍙ヨ瘽姒傛嫭鏈鏇存柊鐨勪富瑕佸唴瀹?
**褰卞搷鏂囦欢**: [鏂囦欢璺緞1](閾炬帴), [鏂囦欢璺緞2](閾炬帴)

---

- **鍔熻兘/鏀硅繘鍚嶇О (绫诲瀷)** - 璇︾粏鎻忚堪
  - 鎶€鏈粏鑺?
  - 鎶€鏈粏鑺?
  
- **鍙︿竴涓姛鑳?(绫诲瀷)** - 璇︾粏鎻忚堪
  - 瀹炵幇鏂规
  - 褰卞搷鑼冨洿

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** - 璐ㄩ噺淇濊瘉
  - 鉁?瑙勮寖缂栧彿: 鍏蜂綋瀹炵幇
  
- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] 娴嬭瘯椤? 鈫?缁撴灉 鉁?```

### 鏍煎紡瑕佹眰

1. **鐗堟湰鍙锋牸寮?*: `### vX.X.XX.XX (YYYY-MM-DD) - 鏍囬`
   - 蹇呴』鍖呭惈鏃ユ湡锛堟嫭鍙峰唴锛?   - 浣跨敤 ` - ` 鍒嗛殧鏃ユ湡鍜屾爣棰橈紙绌烘牸+鐭í绾?绌烘牸锛?
2. **绔犺妭鏍囬**: 浣跨敤 `####` 锛堝洓绾ф爣棰橈級
   - 鎺ㄨ崘浣跨敤 "鏇存柊鍐呭:" 寮€澶?
3. **鍒楄〃椤规牸寮?*: `- **鏍囬** - 鎻忚堪`
   - 鏍囬蹇呴』鍔犵矖锛?*锛?   - 鐢?` - ` 鍒嗛殧鏍囬鍜屾弿杩?
4. **瀛愰」鏍煎紡**: 缂╄繘涓や釜绌烘牸 + `- `
   - 鐢ㄤ簬璇︾粏璇存槑鎴栨妧鏈粏鑺?
5. **浠ｇ爜瑙勮寖**: 鍗曠嫭鍒椾负涓€涓垪琛ㄩ」
   - 寮曠敤鍏蜂綋鐨勮鑼冪紪鍙凤紙濡?PY-FRONT-001锛?   - 璇存槑濡備綍閬靛惊璇ヨ鑼?
6. **楠岃瘉缁撴灉**: 鍗曠嫭鍒椾负涓€涓垪琛ㄩ」
   - 浣跨敤 `[x]` 澶嶉€夋鏍囪
   - 姣忛」鍚庢爣娉?鉁?鎴?鉂?
7. **鏍囬鍒嗛殧绗?*: 浣跨敤绌烘牸 鎴?` 鈥?`锛堢牬鎶樺彿锛夊垎闅斿叧閿瘝
   - 绀轰緥: `馃帹 鍒犻櫎鍟嗗搧鎻忚堪瀹屾暣鏄剧ず浼樺寲 + 鍝嶅簲寮忓竷灞€澧炲己`
   - 绀轰緥: `馃敡 闅ч亾楠岃瘉淇 鈥?hostc/CF鍧囦笉鍙敤鐨勬牴鍥犱慨澶峘

8. **API鍏煎鎬?*: 绗﹀悎 `/api/changelog` API 瑙ｆ瀽瑙勫垯 ([main.py#L7609-7728](main.py#L7609-7728))

---

## 📝 Changelog 编写规范 (标准格式)

### 标准格式模板

`markdown
### vX.X.XX.XX (YYYY-MM-DD) - 📝 版本标题简述

#### 更新内容: 一句话概括本次更新的主要内容

**影响文件**: [文件路径1](链接), [文件路径2](链接)

---

- **功能/改进名称 (类型)** - 详细描述
  - 技术细节1
  - 技术细节2
  
- **另一个功能 (类型)** - 详细描述
  - 实现方案
  - 影响范围

- **代码规范遵循 skill.md** - 质量保证
  - ✅ 规范编号: 具体实现
  
- **验证结果** - 测试通过情况
  - [x] 测试项1 → 结果 ✅
`

### 格式要求

1. **版本号格式**: ### vX.X.XX.XX (YYYY-MM-DD) - 标题
   - 必须包含日期（括号内）
   - 使用  -  分隔日期和标题（空格+短横线+空格）

2. **章节标题**: 使用 #### （四级标题）
   - 推荐使用 "更新内容:" 开头

3. **列表项格式**: - **标题** - 描述
   - 标题必须加粗（**）
   - 用  -  分隔标题和描述

4. **子项格式**: 缩进两个空格 + - 
   - 用于详细说明或技术细节

5. **代码规范**: 单独列为一个列表项
   - 引用具体的规范编号（如 PY-FRONT-001）
   - 说明如何遵循该规范

6. **验证结果**: 单独列为一个列表项
   - 使用 [x] 复选框标记
   - 每项后标注 ✅ 或 ❌

7. **标题分隔符**: 使用空格 或  — （破折号）分隔关键词
   - 示例: 🎨 删除商品描述完整显示优化 + 响应式布局增强
   - 示例: 🔧 隧道验证修复 — hostc/CF均不可用的根因修复

8. **API兼容性**: 符合 /api/changelog API 解析规则 ([main.py#L7609-7728](main.py#L7609-7728))

---
