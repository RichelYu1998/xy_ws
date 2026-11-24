---
name: "product-media-download"
description: "商品媒体下载与品类/品牌分类范式：手机/笔记本/平板/手表四大类判定、其余归其他、品牌自动摘出分层（保存目录/品类/品牌/商品文件夹名）、文件夹命名、配置文件热读取、逐文件直落磁盘下载、以及 SSRF/CSRF/限流/路径穿越等攻防校验。Invoke when 需要实现或改造商品数据抓取、分类、品牌分层、图片视频下载、配置热更新、Web 接口安全加固时。"
---

# 商品媒体下载与品类分类范式（SKILL）

本范式来自 `xy_ws`（微购相册商品抓取/下载工具）已跑通全量数据的实现，可直接复用到同类项目。

---

## 一、品类分类范式（四大类 + 品牌分层 + 其他兜底）

### 0. 目录分层（核心诉求）

```
保存目录/品类/品牌/商品文件夹名
```

示例：

```
~/Downloads/微购/手机/华为/华为Nova 12活力版 电池97%
~/Downloads/微购/笔记本/联想/联想小新Air15 2021款
~/Downloads/微购/平板/苹果/iPad Pro 11英寸第四代
~/Downloads/微购/手表/苹果/Apple Watch SE3 40mm
~/Downloads/微购/其他/大疆/大疆Pocket3
```

要点：
- 第一层永远是四大类之一，**品牌必须从商品描述里摘出来单独成层**，不能混在商品文件夹名里。
- 不属于四大类的一律落到 `其他`，品牌同样分层（`其他/大疆/...`），仍识别不出品牌时用 `其他/其他/...`。
- 目录名逐层过 `_safe_folder_name`，防止 `/`、`:` 等非法字符破坏层级。

### 1. 分类目标

| 大类 | 判定依据 | 文件夹命名 |
| --- | --- | --- |
| 手机 | iPhone / 华为 / 荣耀 / 小米 / 红米 / OPPO / vivo / 一加 / 三星 … | **型号 + 电池** |
| 笔记本 | macbook / 笔记本 / 游戏本 / 拯救者 / 小新 / 机械革命 / thinkpad / 天选 / ROG … | 仅型号 |
| 平板 | ipad / 平板 / matepad / pad / tab / Y700 … | 仅型号 |
| 手表 | watch / 手表 / 腕表 / 手环 / iwatch / band …（含智能穿戴） | 仅型号 |
| 其他 | 音箱 / 耳机 / AirPods / HomePod / 相机 / 大疆 / 键盘 / 鼠标 / 配件 / 显示器 … | 仅型号 |

### 2. 判定顺序（先具体后笼统，顺序错了必然误判）

```
手表 → 平板 → 笔记本 → 其他 → 手机 → 兜底「其他」
```

关键原因：
- 「联想拯救者平板 Y700」同时命中 `拯救者`(笔记本) 与 `平板`，必须**平板优先**。
- 「iPhone 17 Pro Max 原装手机壳」同时命中 `iphone`(手机) 与 `手机壳`(配件)，必须**配件优先**。
- 裸苹果型号（如 `13 128 白色 电池效率75%`）没有品牌词，只有「型号 + 电池信息」，靠「裸苹果型号正则 + 电池信息」兜底判为手机。

### 3. 判定实现模板

```python
_PRODUCT_CATEGORY_PHONE   = '手机'
_PRODUCT_CATEGORY_LAPTOP  = '笔记本'
_PRODUCT_CATEGORY_TABLET  = '平板'
_PRODUCT_CATEGORY_WATCH   = '手表'
_PRODUCT_CATEGORY_SMART   = '其他'      # 不属于四大类的一律落这里

_CATEGORY_MATCH_ORDER = ('watch', 'tablet', 'laptop', 'smart')   # 手机最后判

_CATEGORY_KEY_TO_NAME = {
    'watch': _PRODUCT_CATEGORY_WATCH,
    'tablet': _PRODUCT_CATEGORY_TABLET,
    'laptop': _PRODUCT_CATEGORY_LAPTOP,
    'smart': _PRODUCT_CATEGORY_SMART,
}

def _product_category(text, rules=None, model=''):
    lower = str(text or '').lower()
    rules = rules or _folder_rules()
    for key in _CATEGORY_MATCH_ORDER:
        if any(kw in lower for kw in rules.get(key, ())):
            return _CATEGORY_KEY_TO_NAME[key]
    if any(kw in lower for kw in rules['phone']):
        return _PRODUCT_CATEGORY_PHONE
    if model and _BARE_APPLE_RE.match(model.strip()) and _BATTERY_RE.search(str(text or '')):
        return _PRODUCT_CATEGORY_PHONE
    return _PRODUCT_CATEGORY_SMART      # 兜底：不认识的一律其他
```

要点：
- 关键词**全部小写**、`in` 子串匹配，天然不区分大小写。
- 兜底必须是「其他」，不能是「手机」，否则配件/未知品类会被塞进手机。
- 判定结果要**回填到商品对象**（`_category`、`_brand`），前端列表/详情直接用，避免前后端各判一套。

### 4. 品牌识别（品牌层的数据来源）

```python
_BRAND_DEFAULT_TABLE = {
    'phone': (('苹果', ('iphone', 'apple', '苹果')), ('华为', ('华为', 'huawei', 'mate', 'pura', 'nova'))),
    'laptop': (('联想', ('联想', 'lenovo', 'thinkpad', '拯救者', '小新', 'yoga')), ...),
    'tablet': (('苹果', ('ipad', 'apple')), ('联想', ('联想', 'lenovo', 'y700'))),
    'watch': (('苹果', ('apple watch', 'iwatch')), ('华为', ('huawei', 'watch gt', 'gt2', 'gt3'))),
    'other': (('大疆', ('大疆', 'dji', 'pocket', 'osmo')), ('索尼', ('索尼', 'sony'))),
}

def _product_brand(text, category='', rules=None):
    """先按品类品牌表匹配，再全表兜底，仍找不到返回空串"""
    lower = str(text or '').lower()
    rules = rules or _brand_rules()
    category_key = {'手机': 'phone', '笔记本': 'laptop', '平板': 'tablet',
                    '手表': 'watch', '其他': 'other'}.get(category, 'other')
    keys = [category_key] + [k for k in ('phone', 'laptop', 'tablet', 'watch', 'other')
                             if k != category_key]
    for key in keys:
        for alias, name in _brand_match_pairs(rules.get(key, ())):
            if alias in lower:
                return name
    return ''

def _brand_match_pairs(entries):
    """(别名, 品牌) 按别名长度降序 —— 保证 watch gt 先于 watch 命中"""
    pairs = [(alias, name) for name, aliases in entries for alias in aliases if alias]
    pairs.sort(key=lambda item: len(item[0]), reverse=True)
    return pairs
```

要点：
- **按品类查表优先**：手机品类先查手机品牌表，避免「联想小新」被手机表里的别名误伤。
- **别名长度降序**：`watch gt` 必须先于 `watch` 命中，否则品牌会判错。
- **裸苹果型号兜底**：`16 Pro Max 电池92%` 没有品牌词，但品类已判为手机且型号命中裸苹果正则时，品牌补「苹果」。实测这一条把 33 个「手机/其他」降到 1 个。

### 5. 目录路径生成

```python
def _product_folder_relpath(name_source, category='', brand=''):
    text = str(name_source or '').strip()
    category = category or _product_category(text)
    brand = brand or _product_brand(text, category) or '其他'
    folder = _product_folder_name(text, category)
    return '/'.join((_safe_folder_name(category), _safe_folder_name(brand), folder))
```

创建目录时必须支持多级路径，且同名序号只追加到**最后一层**：

```python
def _resolve_product_folder(base_dir, folder_name, product_id):
    rel_dir, base_name = os.path.split(folder_name)      # 拆出「品类/品牌」与「商品名」
    for cand in [base_name] + [f'{base_name}-{n}' for n in range(2, 100)]:
        root = os.path.join(base_dir, rel_dir, cand)
        ...
```

---

## 二、文件夹命名范式

### 1. 规则

- 型号 = 商品描述中**第一个规格词之前**的内容（规格词：容量 / 颜色 / 成色 / 电池 / 保修 / 拆修 / 版本 / CPU …）
- 手机：`型号 + 电池`，电池统一成 `电池92%`
- 其它品类：**只留型号**，不带容量、颜色、成色、电池

### 2. 规格词截断要覆盖的边界

| 场景 | 描述 | 型号截断点 |
| --- | --- | --- |
| 容量 | `256G` / `1TB` / `16+512G` | 容量正则 |
| 颜色 | `白色` / `深空灰` / `远峰蓝` | 颜色词表 |
| 成色 | `成色九九新` / `准新` / `靓机` | 规格词表 |
| 电池 | `电池92%` / `电池容量100%` / `电池健康79%` | 电池正则 |
| 版本 | `国行` / `港版` / `美版` / `日版` | 规格词表 |
| CPU | `i5-1155G7` / `R7-7735H` / `Core7-245HX` | CPU 正则（`i3/i5/i7/i9`、`R7`、`core`） |
| 苹果型号 | `14pro256白色` | `14pro` 后紧跟容量，容量正则切开 |

### 3. 命名实现模板

```python
def _product_folder_name(name_source, category=None):
    text = str(name_source or '').strip()
    rules = _folder_rules()
    model = _pretty_model(_folder_model(text, rules))     # 型号
    if category is None:
        category = _product_category(text, rules, model)
    if category == _PRODUCT_CATEGORY_PHONE:
        battery = _folder_battery_label(text)             # 电池92%
        if battery:
            model = f'{model} {battery}'.strip()
    return _safe_folder_name(model or text)               # 清非法字符 + 截断长度
```

`_safe_folder_name` 必做：
- 去掉 `\ / : * ? " < > |` 与换行制表符
- 合并连续空格、去掉首尾空格与 `.`（避免 Windows 目录末尾点号问题）
- 长度截断（建议 60 字符）+ 空结果兜底 `product`

### 4. 同名商品目录复用

同一商品（`product_id`）复用同名目录；不同商品撞名时追加 `-2`、`-3`，靠目录内 `.product_id` 标记文件识别归属，避免多个商品图片混装。

---

## 三、配置热读取范式（改配置即生效，绝不重启）

### 1. 两种落地方式

**方式 A：每次读盘（推荐用于小配置）**

```python
def _read_config():
    path = _config_file()
    if not os.path.isfile(path):
        return defaults
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return parse(f)          # 每次调用都重新解析
    except Exception as e:           # [HANDLED]
        log_print(f'[config] 读取失败: {type(e).__name__}: {e}')
        return defaults
```

**方式 B：文件签名 + 全局缓存（推荐用于大文件/高频访问）**

```python
_cache = None
_cache_sig = None

def _config_file_signature(path):
    try:
        st = os.stat(path)
        return (st.st_mtime_ns, st.st_size)
    except OSError:
        return None

def get_config():
    global _cache, _cache_sig
    path = _config_file()
    sig = _config_file_signature(path)
    if _cache is not None and sig == _cache_sig:
        return _cache
    data = parse_file(path)          # 签名变了才重新解析
    _cache, _cache_sig = data, sig
    return data
```

### 2. 本项目的配置清单（全部热读取）

| 配置文件 | 内容 | 读取方式 |
| --- | --- | --- |
| `config/folder_naming.txt` | 品类/命名关键词，分节 | 每次读盘 |
| `config/brands.txt` | 品牌表（`规范名\|别名1,别名2`），分节 | 文件签名 + 缓存 |
| `config/download_dir.txt` | 保存目录（`~` 脱敏） | 每次读盘 |
| `config/clean_allowed_roots.txt` | 清理白名单根目录 | 文件签名 + 缓存 |
| `config/config.json` | 目标相册 URL 等 | 每次读盘 / ConfigManager 签名对比 |
| `config/cookies.json` | 登录 Cookie | 每次读盘 |
| `config/input_stock_numbers.txt` | 待处理货号清单 | 每次读盘 |
| `file/*微购相册*.json` | 商品数据 | 每次 glob 取最新 mtime |

### 3. 配置格式约定（脱敏 + 可注释）

- 一行一条，`#` 后为注释
- 支持 `~` 展开；**写入时把家目录缩写成 `~`**，配置文件里不出现真实用户名
- 真实配置加入 `.gitignore`，只提交 `*.example.txt` 模板
- 分节配置用 `[颜色] [规格] [手机品牌] [非手机] [笔记本] [平板] [手表] [其他]`，未知分节忽略
- 品牌表分节用 `[手机] [笔记本] [平板] [手表] [其他]`，一行 `规范品牌名|别名1,别名2`，只写品牌名时品牌名即别名

```python
def _abbreviate_home(path):
    home = os.path.expanduser('~').rstrip(os.sep)
    norm = os.path.normpath(path)
    if norm == home:
        return '~'
    if home and os.path.commonpath([norm, home]) == home:
        return '~' + os.sep + os.path.relpath(norm, home)
    return path
```

---

## 四、下载范式（逐文件直落磁盘，不打包）

用户诉求：**临时下载、用完即删，不要 ZIP**。

### 1. 流程

1. 从商品数据取媒体 URL（图片/视频，Base64 解码后即为原站 URL）
2. 直接带 UA/Referer 请求原站 CDN（token 在 URL 里，不需要中间代理）
3. 逐个文件写入 `保存目录/商品文件夹/01.jpg`、`02.mp4` …
4. 返回每个文件的落盘路径与字节数

### 2. 关键约束

- **不打包**：不生成 zip/tar，每个文件独立落盘
- 文件序号 `01`、`02` … 按媒体顺序；后缀优先取 URL，其次 `Content-Type`，兜底 `.jpg`
- 单文件大小上限（如 200MB），先看 `Content-Length` 再 `read(limit+1)` 二次校验
- 单次批量文件数上限（如 200），防止一个商品拖垮服务
- 部分失败不整体失败：返回 `saved` / `failed` 两组，`failed` 带 `index` + 原因
- 落盘前 `os.makedirs(exist_ok=True)`，写临时探针文件验证目录可写

### 3. 返回结构

```json
{
  "success": true,
  "dir": "~/Downloads/微购/手机/华为/华为Mate 60 Pro 电池97%",
  "saved": 3,
  "failed": 0,
  "files": [{"index": 0, "filename": "01.jpg", "path": "...", "bytes": 586918}],
  "errors": []
}
```

---

## 五、攻防范式（Web 接口安全基线）

### 1. 服务端请求伪造（SSRF）

- 仅允许 `http/https`
- 拒绝私有网段 `10/8`、`172.16/12`、`192.168/16`、`127/8`、`169.254/16`、`::1`、`fe80::/10`、`fc00::/7`
- 拒绝云元数据域名（`metadata.google.internal`、`169.254.169.254`）
- 所有出网请求统一走 `safe_urlopen`，确保 `resp.close()` 在 `finally` 中执行
- 下载类接口的 URL 必须由服务端从可信数据源取，**不接受前端传任意 URL**

### 2. CSRF（写操作同源校验）

- 写方法（`POST/PUT/PATCH/DELETE`）校验 `Origin`（缺省回退 `Referer`）的 host 与请求 `Host` 一致
- 白名单豁免仅限静态资源与明确的安全接口
- 动态域名（隧道/Cloudflare）用「host 对比」而非固定白名单，避免误伤

### 3. 频率限制

- 按「IP + 接口分桶」计数，滑动窗口 60s，超限返回 `429` + `Retry-After`
- 高频轮询接口（隧道状态、任务输出）单独分桶，避免互相挤占配额
- 敏感接口（`/api/bootstrap` 等）使用独立 `RateLimiter`
- 定期清理过期桶，防止内存膨胀

### 4. 请求体与超时

- `Content-Length` 超过 10MB 直接 `413`，不读 body
- 单请求处理超时 120s，超时返回 `504`，避免线程被长任务占死
- 大请求体（>1MB）记录告警日志

### 5. 响应安全头

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY（/dist 静态资源用 SAMEORIGIN）
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=(), camera=(), payment=()
Content-Security-Policy: 按页面白名单下发（不要全站一刀切，否则 CDN 脚本失效）
```

### 6. 日志注入

日志里的路径、IP、用户输入必须过滤 `\r` `\n`（替换成 `\\r` `\\n`），防止伪造日志行；用户可控文本统一走 `sanitize_log_input`（截断 + 去控制字符）。

### 7. 路径穿越与目录白名单

- 清理/删除类接口的根目录走白名单（`clean_allowed_roots.txt` + 默认下载目录）
- 路径比较用 `realpath + normcase`（大小写不敏感文件系统再 `casefold`）
- 拒绝 `..`、符号链接逃逸到白名单外
- 写目录前先探针写入，验证可写

### 8. 敏感信息

- API Key 从 `config.json` 读取，缺省时生成随机值写回，不硬编码在仓库里
- 目录配置写入时家目录缩写 `~`，配置文件脱敏
- 日志不打印 Cookie / Token / 完整 URL 查询串

### 9. 输入校验

- 路径参数（`product_id` / `index`）限长度、限类型，非法直接 `400`
- JSON body 先判 `isinstance(dict)` 再取字段，非法 JSON 返回 `400`
- 命令执行类接口用 Pydantic 校验 + 危险命令黑名单

### 10. 异常与错误信息

- 全局捕获异常，对外只返回**友好中文提示**，不暴露堆栈/路径
- 统一 `try/except` 并标注 `# [HANDLED]`，避免裸 `except` 静默吞异常
- 前端渲染一律 `escapeHtml` / `escapeAttr`，防止 XSS

---

## 六、前端展示范式

- 商品详情弹窗顶部固定「保存位置」栏（显示完整「品类/品牌/商品名」路径）+ 「保存全部 (N)」按钮，每个缩略图右上角独立下载按钮
- 「品类」用彩色 badge 展示（手机蓝 / 笔记本灰 / 平板绿 / 手表橙 / 其他红）
- 「品牌」单独一列/一行展示，与「品类」并列，方便按品牌核对
- 商品搜索下拉必须有「按品牌」选项，输入品牌名（如 `华为`）或 `品类/品牌`（如 `手机/华为`）即可筛选
- 行级数据要把 `_brand`、`_category` 写到 `data-brand` / `data-category` 属性，前端搜索直接读属性，避免每次重新解析文案
- 售价单元格统一加 `class="price-cell"`，前端取价一律优先 `querySelector('.price-cell')`、再回退 `td:nth-child(4)`，避免加列后错位
- 弹窗内说明文案与后端规则保持一致（手机=型号+电池，其它=型号），避免用户误解
- 静态资源带版本号 `app.js?v=<时间戳>`，改完前端必须改版本号，否则浏览器缓存导致看不到改动

---

## 七、落地检查清单

- [ ] 目录结构是「保存目录/品类/品牌/商品文件夹名」，品牌单独成层
- [ ] 品牌从描述里摘出，找不到品牌落 `其他`，品类不属于四大类也落 `其他`
- [ ] 品类判定顺序是「手表→平板→笔记本→其他→手机→其他兜底」
- [ ] 手机带电池、其它品类不带电池、颜色/容量/成色全部剔除
- [ ] 同名序号只追加到最后一层（商品名），不污染品类/品牌目录
- [ ] 所有配置文件热读取（改完不重启即生效），品牌表改动立即生效
- [ ] 配置文件脱敏（`~` 缩写）、真实配置进 `.gitignore`
- [ ] 下载逐文件落盘、不打包、部分失败可提示
- [ ] SSRF / CSRF / 限流 / 请求体上限 / 安全头 / 日志注入 / 路径白名单全部到位
- [ ] 前端品牌列/详情行/按品牌搜索已展示，静态资源版本号已更新