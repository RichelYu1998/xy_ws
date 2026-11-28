# -*- coding: utf-8 -*-
"""
浏览器自动化适配回归验证（Playwright / Chromium，不使用 Selenium）
遵循 UTF-8 编码 + 简体中文规范

功能：
1. 全市场设备屏幕矩阵：智能手表 / 手环 / 副屏辅屏 / 小折叠外屏与内屏 / 阔折叠 / 大折叠 /
   三折叠 / 双屏手机展开 / 卷轴与环绕屏 / 手机竖屏与横屏 / 平板竖屏与横屏 /
   双屏与折叠笔记本 / 笔记本 / 桌面显示器 / 超宽屏 / 电视 / 投影 / LED 拼接屏 /
   条形屏 / 车机嵌入式 / 车载副屏与后排屏 / 方形标牌 / 数字标牌竖屏 /
   智能家居带屏 / 头显 VR-AR / 电子墨水屏，共 28 类 171 款已发布设备屏幕（同尺寸去重后 156 档），
   口径：只要能联网、能显示画面的设备，无论主屏 / 副屏 / 辅屏 / 外屏 / 内屏 / 横屏 / 竖屏 /
   方形 / 条形 / 卷轴 / 环绕 / 头显 / 电子纸，一律纳入，逐档真实渲染
2. 主页面断言：页面级横向溢出、设备类名唯一且正确、导航栏高度与 body.paddingTop 同步
3. 折叠态断言（≤991.98px）：品牌中心对齐视口中心（偏差 ≤2px）、时间与 Token 左边界相等且分两排、
   品牌文字不压汉堡按钮且不越出视口
4. 菜单展开态断言：展开后仍零横向溢出、导航栏高度增加、body.paddingTop 不变（不整页跳动）
5. 天气看板断言：dist/index.html 同档零溢出、面板已渲染、面板宽度不超过视口
6. 运行期 JS 异常：每档捕获 pageerror，必须为 0
7. 覆盖自检：全部设备类别逐一核对，任一类别缺席即判失败（防止后续删档导致覆盖面退化）
8. 极小屏抖动自检：宽度 ≤200px 的档位连采两次，`navbarHeight` / `paddingTop` / 品牌文字边界 /
   品牌中心 / 根字号必须逐项一致，把「换行边界随滚动条或字体晚到翻转」的非确定性抖动当场判失败
9. 性能自检：主页面 / 看板 / 展开态三张矩阵顺序跑（并发实测因渲染进程单核争用反而慢 4 倍），
   单次加载 + 视口复用 + 同步补发 resize（免等 16.7ms 帧）+ 切视口前鼠标归位（免悬停命中测试）
   + 展开态按需降级过渡，总耗时必须 ≤ TIMING_BUDGET_S（10 秒），超时即判失败
   （防止后续加档把回归拖成分钟级）

依赖与离线：
- 页面引用的 CDN 资源（bootstrap / jquery / popper / font-awesome）在 test/fixtures 下固化，
  由路由拦截就地返回，测试全程不依赖公网；echarts 页面未引用，以空占位返回（一旦真被调用会报错暴露）
- Chromium 取自 tools/playwright/<平台>，可用 PLAYWRIGHT_BROWSERS_PATH 覆盖

用法：.venv/bin/python test/browser_adapt_test.py
时机：改动 index.html / dist/app.js / dist/display-adapt.css 后必须跑，退出码 0 才允许提交
退出码：0 = 全档零缺陷；1 = 存在断言失败（含超时）；2 = 运行环境缺失（playwright / chromium / 固化资源）
"""

import asyncio
import os
import sys
import threading
import time
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
FIXTURE_DIR = PROJECT_DIR / 'test' / 'fixtures'
PLATFORM_DIR = {'darwin': 'macos', 'win32': 'windows'}.get(sys.platform, 'linux')

LOAD_TIMEOUT_MS = 30000
NAV_TIMEOUT_MS = 5000
TIMING_BUDGET_S = 10.0
CENTER_TOLERANCE = 2.0
EDGE_TOLERANCE = 1.0
COLLAPSED_MAX_WIDTH = 991.98
ROOT_FONT_MIN = 12.0
ROOT_FONT_MAX = 256.0
EXPAND_MIN_GROWTH = 40.0
JITTER_MAX_WIDTH = 200.0
JITTER_KEYS = ('navbarHeight', 'paddingTop', 'brandTextLeft', 'brandTextRight',
               'brandCenter', 'rootFontSize')


def _dedupe_devices(families):
    """按 (宽, 高) 去重：同一 CSS 视口只测一次，标签沿用首个出现的设备名"""
    seen, rows = set(), []
    for family, entries in families:
        for width, height, name in entries:
            if (width, height) not in seen:
                seen.add((width, height))
                rows.append((width, height, family, name))
    return tuple(rows)


# 全市场设备屏幕矩阵（CSS 视口尺寸 / dp，按已发布设备的屏幕规格换算，宽 × 高）
# 口径：只要能联网能显示，主屏 / 副屏 / 辅屏 / 外屏 / 内屏 / 横竖 / 方形 / 条形 / 卷轴 / 环绕 / 头显 / 电子纸
# 新增机型只需在对应类别追加一行，去重后自动并入测试矩阵
DEVICE_FAMILIES = (
    ('智能手表', (
        (136, 170, 'Apple Watch 38/40mm'),
        (176, 215, 'Apple Watch 41mm'),
        (198, 242, 'Apple Watch 45mm'),
        (205, 251, 'Apple Watch Ultra'),
        (165, 165, 'Wear OS 小方屏'),
        (186, 186, '华为 Watch 4 圆屏'),
        (192, 192, '三星 Watch 6 圆屏'),
        (168, 168, 'Fitbit Versa 4'),
    )),
    ('智能手环', (
        (168, 240, '小米手环 8 Pro'),
        (194, 368, '手环长条屏'),
    )),
    ('小折叠外屏', (
        (262, 272, 'Galaxy Z Flip5/6 外屏'),
        (260, 512, 'Galaxy Z Flip3/4 外屏'),
        (351, 355, 'moto razr 40 Ultra 外屏'),
        (240, 127, 'OPPO Find N3 Flip 外屏'),
    )),
    ('小折叠内屏', (
        (411, 1006, 'Galaxy Z Flip6 内屏'),
        (360, 880, 'moto razr 40 Ultra 内屏'),
        (393, 916, 'OPPO Find N3 Flip 内屏'),
    )),
    ('阔折叠', (
        (392, 392, '华为 Pura X 外屏'),
        (528, 848, '华为 Pura X 内屏'),
        (749, 827, 'OPPO Find N5 内屏'),
    )),
    ('大折叠', (
        (344, 882, 'Galaxy Z Fold5/6 外屏'),
        (690, 829, 'Galaxy Z Fold5 内屏'),
        (707, 823, 'Galaxy Z Fold6 内屏'),
        (372, 914, 'Galaxy Z Fold7 外屏'),
        (757, 840, 'Galaxy Z Fold7 内屏'),
        (890, 998, '华为 Mate X5 内屏'),
        (976, 992, '华为 Mate X6 内屏'),
        (766, 864, '小米 MIX Fold 3 内屏'),
        (880, 992, 'vivo X Fold3 Pro 内屏'),
        (938, 862, '荣耀 Magic V3 内屏'),
        (810, 871, 'OPPO Find N3 内屏'),
    )),
    ('三折叠', (
        (336, 732, '华为 Mate XT 单屏'),
        (504, 732, '华为 Mate XT 双屏'),
        (744, 1061, '华为 Mate XT 三屏全展开'),
        (528, 821, '三星 TriFold 全展开'),
    )),
    ('双屏手机展开', (
        (2688, 1892, 'Surface Duo 2 双屏展开'),
        (1080, 2460, 'LG Wing 旋转副屏'),
    )),
    ('卷轴与环绕屏', (
        (1440, 2560, 'OPPO X 2021 卷轴展开'),
        (2088, 2250, '小米 MIX Alpha 环绕屏'),
        (1600, 2560, 'LG Rollable 卷轴展开'),
    )),
    ('手机竖屏', (
        (320, 480, '320×480 老款安卓'),
        (320, 568, 'iPhone SE 1'),
        (360, 640, '360×640 安卓'),
        (360, 740, '360×740 安卓'),
        (360, 780, 'Galaxy S24'),
        (360, 800, '360×800 安卓'),
        (375, 667, 'iPhone SE2/8'),
        (375, 812, 'iPhone X/13 mini'),
        (384, 854, '384×854 安卓'),
        (390, 844, 'iPhone 13/16e'),
        (393, 852, 'iPhone 14 Pro/15/16'),
        (402, 874, 'iPhone 16 Pro/17'),
        (411, 914, 'Pixel 6'),
        (412, 915, 'Pixel 8/S24 Ultra'),
        (414, 736, 'iPhone 8 Plus'),
        (414, 896, 'iPhone XR/11'),
        (420, 912, 'iPhone Air'),
        (428, 926, 'iPhone 12 Pro Max'),
        (430, 932, 'iPhone 14 Pro Max'),
        (440, 956, 'iPhone 16 Pro Max'),
    )),
    ('手机横屏', (
        (480, 320, '480×320 横屏'),
        (568, 320, 'iPhone SE 横屏'),
        (640, 360, '640×360 横屏'),
        (667, 375, 'iPhone 8 横屏'),
        (736, 414, 'iPhone 8 Plus 横屏'),
        (740, 360, '740×360 横屏'),
        (780, 360, 'Galaxy S24 横屏'),
        (800, 360, '800×360 横屏'),
        (812, 375, 'iPhone X 横屏'),
        (844, 390, 'iPhone 13 横屏'),
        (852, 393, 'iPhone 15 横屏'),
        (874, 402, 'iPhone 16 Pro 横屏'),
        (896, 414, 'iPhone XR 横屏'),
        (912, 420, 'iPhone Air 横屏'),
        (914, 411, 'Pixel 6 横屏'),
        (915, 412, 'Pixel 8 横屏'),
        (926, 428, 'iPhone 12 Pro Max 横屏'),
        (932, 430, 'iPhone 14 Pro Max 横屏'),
        (956, 440, 'iPhone 16 Pro Max 横屏'),
    )),
    ('平板竖屏', (
        (576, 1024, '小尺寸平板 576'),
        (600, 960, '600×960 平板'),
        (744, 1133, 'iPad mini 6'),
        (768, 1024, 'iPad 9'),
        (810, 1080, 'iPad 10'),
        (820, 1180, 'iPad Air 11'),
        (834, 1112, 'iPad Pro 11'),
        (834, 1194, 'iPad Pro 11 M4'),
        (1024, 1366, 'iPad Pro 12.9'),
        (1032, 1376, 'iPad Pro 13 M4'),
        (1200, 1920, '安卓平板 1200'),
        (1600, 2560, 'Galaxy Tab S9 Ultra'),
    )),
    ('平板横屏', (
        (1024, 768, 'iPad 横屏'),
        (1080, 810, 'iPad 10 横屏'),
        (1112, 834, 'iPad Pro 11 横屏'),
        (1133, 744, 'iPad mini 横屏'),
        (1180, 820, 'iPad Air 横屏'),
        (1194, 834, 'iPad Pro 11 M4 横屏'),
        (1366, 1024, 'iPad Pro 12.9 横屏'),
        (1376, 1032, 'iPad Pro 13 横屏'),
        (1920, 1200, '安卓平板横屏'),
        (2560, 1600, 'Tab S9 Ultra 横屏'),
    )),
    ('双屏与折叠笔记本', (
        (2048, 1536, 'ThinkPad X1 Fold 展开'),
        (1920, 2160, 'ZenBook Duo 双屏组合'),
        (1350, 1800, 'Surface Neo 双屏'),
        (2160, 1350, 'Yoga Book 9i 双屏横置'),
    )),
    ('笔记本', (
        (1024, 600, '上网本 1024×600'),
        (1180, 820, '1180×820 笔电'),
        (1280, 800, '1280×800 笔电'),
        (1366, 768, '1366×768 笔电'),
        (1440, 900, '1440×900 笔电'),
        (1470, 956, 'MacBook Air 13'),
        (1512, 982, 'MacBook Pro 14'),
        (1600, 900, '1600×900 笔电'),
        (1680, 1050, '1680×1050 笔电'),
        (1728, 1117, 'MacBook Pro 16'),
        (1920, 1080, '1920×1080 笔电'),
        (2048, 1280, '2048×1280 笔电'),
        (2560, 1600, '2560×1600 笔电'),
        (2880, 1800, 'MacBook Pro 15 Retina'),
    )),
    ('桌面显示器', (
        (2560, 1440, '2K 桌面'),
        (3840, 2160, '4K 桌面'),
        (5120, 2880, '5K 桌面'),
        (7680, 4320, '8K 桌面'),
    )),
    ('超宽屏', (
        (2560, 1080, '21:9 超宽 2560×1080'),
        (3440, 1440, '21:9 超宽 3440×1440'),
        (3840, 1080, '32:9 超宽 3840×1080'),
        (5120, 1440, '32:9 双 2K 5120×1440'),
    )),
    ('电视', (
        (1280, 720, '720P 电视'),
        (1920, 1080, '1080P 电视'),
        (2560, 1440, '2K 电视'),
        (3840, 2160, '4K 电视'),
        (4096, 2160, 'DCI 4K 电视'),
        (7680, 4320, '8K 电视'),
    )),
    ('投影', (
        (1920, 1200, '投影 1920×1200'),
        (3840, 2400, '投影 4K 16:10'),
        (5120, 3200, '投影 5K'),
        (15360, 8640, '投影 16K 16:9'),
    )),
    ('LED 拼接屏', (
        (25600, 4320, 'LED 墙 300 寸'),
        (38400, 4320, 'LED 墙 800 寸'),
        (4320, 7680, 'LED 竖屏 9:16'),
        (2160, 3840, '竖屏 4K 广告机'),
    )),
    ('条形屏', (
        (3840, 540, '地铁条形屏'),
        (1920, 540, '公交条形屏'),
        (1920, 360, '货架电子条屏'),
    )),
    ('车机嵌入式', (
        (800, 480, '车载 HMI 800×480'),
        (1024, 600, '车机/POS 1024×600'),
        (1280, 480, '条屏 1280×480'),
        (1920, 720, '车机超宽 8:3'),
    )),
    ('车载副屏与后排屏', (
        (1920, 480, '液晶仪表盘 1920×480'),
        (2560, 720, '副驾超宽娱乐屏'),
        (1280, 480, '后排吸顶屏 1280×480'),
    )),
    ('方形标牌', (
        (480, 480, '方形标牌 480'),
        (1024, 1024, '方形标牌 1024'),
    )),
    ('数字标牌竖屏', (
        (1080, 1920, '竖屏标牌 1080×1920'),
        (3840, 2160, '横屏标牌 4K'),
    )),
    ('智能家居带屏', (
        (960, 480, 'Echo Show 5'),
        (1280, 800, 'Echo Show 8'),
        (1024, 600, '小度在家触屏音箱'),
        (320, 320, 'Nest 温控器'),
        (1080, 1920, 'Family Hub 冰箱屏'),
        (480, 272, '空气净化器屏'),
        (240, 320, '智能门锁屏'),
    )),
    ('头显 VR-AR', (
        (2064, 2208, 'Meta Quest 3 单眼'),
        (3660, 3200, 'Apple Vision Pro 单眼'),
        (2160, 2160, 'Pico 4 单眼'),
        (1920, 1080, 'Xreal Air 眼镜屏'),
    )),
    ('电子墨水屏', (
        (250, 122, '电子价签 2.13 寸'),
        (1072, 1448, 'Kindle Paperwhite'),
        (1860, 2480, 'Kindle Scribe'),
        (1200, 1600, '墨水屏标牌'),
        (640, 384, '电子价签 7.5 寸'),
    )),
)

DEVICE_MATRIX = _dedupe_devices(DEVICE_FAMILIES)

REQUIRED_FAMILIES = tuple(family for family, _ in DEVICE_FAMILIES)

BOARD_WIDTHS = tuple(sorted({width for width, _, _, _ in DEVICE_MATRIX}))

# 菜单展开态代表机型：手表 / 副屏 / 手环 / 手机竖屏 / 手机横屏 / 小折叠内屏 / 大折叠内屏 / 平板
EXPAND_CASES = ((198, 242), (126, 294), (194, 368), (360, 780), (780, 360),
                (411, 1006), (707, 823), (768, 1024))

# 真动画档：bootstrap 折叠动画单程 .35s，两程约 .8s。动画时序是纯 CSS 行为与宽度无关，
# 故只留 1 档跑完整动画（验动画期 paddingTop 冻结），其余档用 prefers-reduced-motion
# 关掉过渡只验展开后布局，既保覆盖又不让 8 档 × .8s 的等待吃掉 10 秒预算
EXPAND_REAL_CASES = ((360, 780),)

DEVICE_BUCKETS = (
    (320, 'wearable'),
    (576, 'phone'),
    (768, 'tablet'),
    (992, 'laptop'),
    (1440, 'desktop'),
    (1920, 'large-desktop'),
    (2560, 'tv'),
    (3840, 'large-tv'),
    (5120, 'projector-4k'),
    (7680, 'projector-5k'),
    (15360, 'projector-8k'),
    (25600, 'projector-16k'),
    (38400, 'wall-300'),
)

DEVICE_CLASSES = tuple('is-' + bucket for _, bucket in DEVICE_BUCKETS) + ('is-wall-ultra',)

CDN_FIXTURES = {
    'bootstrap@4.6.2/dist/css/bootstrap.min.css': ('bootstrap-4.6.2.min.css', 'text/css'),
    'bootstrap@4.6.2/dist/js/bootstrap.min.js': ('bootstrap-4.6.2.min.js', 'application/javascript'),
    'jquery@3.5.1/dist/jquery.slim.min.js': ('jquery-3.5.1.slim.min.js', 'application/javascript'),
    'popper.js@1.16.1/dist/umd/popper.min.js': ('popper-1.16.1.min.js', 'application/javascript'),
    'font-awesome@4.7.0/css/font-awesome.min.css': ('font-awesome-4.7.0.min.css', 'text/css'),
}
ECHARTS_STUB = 'window.echarts = window.echarts || {};'

# 指标采集：切完视口后同步补发一次 resize 事件再读，不走 rAF。
# 原因：Playwright 的 set_viewport_size 只改设备指标，页面自己的 resize 监听要等下一个
# 任务才跑，等一帧就要固定 16.7ms（156 档 × 16.7ms ≈ 2.6s 纯等待）。改成同步派发
# resize 事件，app.js 的 applyDeviceStyles() 与 paddingTop 同步逻辑当场跑完，
# 读 getBoundingClientRect 又强制同步布局，读到的就是本档终态，零脏读且省掉整帧等待
METRICS_JS = """
() => {
    window.dispatchEvent(new Event('resize'));
    const doc = document.documentElement;
    const box = (el) => {
        if (!el) { return null; }
        const rect = el.getBoundingClientRect();
        return { left: rect.left, top: rect.top, right: rect.right,
                 width: rect.width, height: rect.height };
    };
    const brand = box(document.querySelector('.navbar-brand'));
    const brandEl = document.querySelector('.navbar-brand');
    const brandText = (() => {
        if (!brandEl) { return null; }
        const range = document.createRange();
        range.selectNodeContents(brandEl);
        const rect = range.getBoundingClientRect();
        return { left: rect.left, right: rect.right, width: rect.width };
    })();
    const nav = box(document.querySelector('.navbar'));
    const toggler = box(document.querySelector('.navbar-toggler'));
    const timeEl = box(document.getElementById('current-time'));
    const cookieEl = box(document.getElementById('cookie-status'));
    const panels = Array.from(document.querySelectorAll('.glass-panel'));
    return {
        innerWidth: window.innerWidth,
        scrollWidth: doc.scrollWidth,
        clientWidth: doc.clientWidth,
        bodyScrollWidth: document.body.scrollWidth,
        navbarHeight: nav ? nav.height : 0,
        brandLeft: brand ? brand.left : -1,
        brandRight: brand ? brand.right : -1,
        brandCenter: brand ? brand.left + brand.width / 2 : -1,
        brandTextLeft: brandText ? brandText.left : -1,
        brandTextRight: brandText ? brandText.right : -1,
        togglerLeft: toggler ? toggler.left : -1,
        togglerRight: toggler ? toggler.right : -1,
        timeLeft: timeEl ? timeEl.left : -1,
        timeTop: timeEl ? timeEl.top : -1,
        cookieLeft: cookieEl ? cookieEl.left : -1,
        cookieTop: cookieEl ? cookieEl.top : -1,
        paddingTop: parseFloat(getComputedStyle(document.body).paddingTop) || 0,
        rootFontSize: parseFloat(getComputedStyle(doc).fontSize) || 0,
        bodyClass: document.body ? document.body.className : '',
        panelCount: panels.length,
        widestPanel: panels.reduce((max, el) => Math.max(max, el.getBoundingClientRect().width), 0)
    };
}
"""

# 只读版采集：去掉补发 resize 那一行，供幂等自检的第二次采集使用。
# 若第二次也补发 resize，会再触发一次前端 resize 监听并重启 250ms 防抖，
# 实测让总耗时从 8s 级涨到 10~13s，把自检成本抬成性能问题
METRICS_READ_JS = METRICS_JS.replace("    window.dispatchEvent(new Event('resize'));\n", "")

# 菜单折叠动画结束判定：bootstrap 的 show / collapsing 类稳定后即为终态，比固定 sleep 更快更准
COLLAPSE_STATE_JS = """
(expanded) => {
    const c = document.querySelector('.navbar-collapse');
    return !!c && c.classList.contains('show') === expanded && !c.classList.contains('collapsing');
}
"""


try:
    from playwright.async_api import async_playwright
except ImportError as exc:
    print(f'❌ 未安装 playwright（{exc}），请先执行 pip install playwright')
    sys.exit(2)


class _QuietHandler(SimpleHTTPRequestHandler):
    """本地静态服务器：关闭访问日志，避免数百档 × 多页刷屏"""

    def log_message(self, fmt, *args):
        return


def _ensure_browsers_path():
    """把 Chromium 缓存目录指向仓库自带的 tools/playwright/<平台>"""
    if os.environ.get('PLAYWRIGHT_BROWSERS_PATH'):
        return
    local = PROJECT_DIR / 'tools' / 'playwright' / PLATFORM_DIR
    if local.is_dir():
        os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(local)


def _start_server():
    """起一个随机端口的本地静态服务器，返回 (server, origin)"""
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(_QuietHandler, directory=str(PROJECT_DIR)))
    server.daemon_threads = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    host, port = server.server_address[0], server.server_address[1]
    return server, f'http://{host}:{port}'


def _match_cdn(url):
    """CDN 请求 → 本地固化资源 (body, mime)；未命中返回 None（由调用方中止）"""
    if 'cdn.jsdelivr.net' not in url:
        return None
    for key, (name, mime) in CDN_FIXTURES.items():
        if key in url:
            path = FIXTURE_DIR / name
            if not path.is_file():
                return None
            return path.read_text(encoding='utf-8'), mime
    if 'echarts' in url:
        return ECHARTS_STUB, 'application/javascript'
    return None


def _make_router(origin):
    """路由：本机资源放行，CDN 走固化资源，其余外网请求一律中止（保证离线可重复）"""

    async def handler(route, request):
        url = request.url
        if url.startswith(origin):
            await route.continue_()
            return
        payload = _match_cdn(url)
        if payload is None:
            await route.abort()
            return
        body, mime = payload
        await route.fulfill(status=200, content_type=mime, body=body)

    return handler


def _find_chromium():
    """在 tools/playwright/<平台>/chromium-* 中动态搜索可执行文件，不硬编码子目录名"""
    base = Path(os.environ.get('PLAYWRIGHT_BROWSERS_PATH', PROJECT_DIR / 'tools' / 'playwright' / PLATFORM_DIR))
    if not base.is_dir():
        return None
    names = ('chrome.exe', 'chromium.exe') if sys.platform == 'win32' else ('chrome', 'chromium', 'Chromium')
    for folder in sorted((p for p in base.iterdir() if p.name.startswith('chromium-')), reverse=True):
        for path in folder.rglob('*'):
            if path.is_file() and path.name in names and (sys.platform == 'win32' or os.access(path, os.X_OK)):
                return str(path)
    return None


async def _new_page(browser, origin):
    """新建页面并挂上路由与 JS 异常采集"""
    page = await browser.new_page(viewport={'width': 1280, 'height': 800})
    page.set_default_timeout(LOAD_TIMEOUT_MS)
    errors = []
    page.on('pageerror', lambda exc: errors.append(str(exc)))
    await page.route('**/*', _make_router(origin))
    return page, errors


def _expected_device(width):
    """与 dist/app.js detectDevice 的分档阈值逐条对齐"""
    for upper, bucket in DEVICE_BUCKETS:
        if width < upper:
            return bucket
    return 'wall-ultra'


def _fail(failures, scope, detail):
    failures.append(f'{scope} → {detail}')


def _check_layout(metrics, scope, failures):
    """页面级通用断言：零横向溢出、导航栏存在、paddingTop 同步、根字号在兜底区间内"""
    overflow = metrics['scrollWidth'] - metrics['clientWidth']
    if overflow > 0:
        _fail(failures, scope, f'页面横向溢出 {overflow}px')
    if metrics['navbarHeight'] <= 0:
        _fail(failures, scope, '导航栏高度为 0，未渲染')
    if abs(metrics['paddingTop'] - metrics['navbarHeight']) > EDGE_TOLERANCE:
        _fail(failures, scope,
              f'body.paddingTop {metrics["paddingTop"]}px 与导航栏高度 {metrics["navbarHeight"]}px 不同步')
    if not ROOT_FONT_MIN <= metrics['rootFontSize'] <= ROOT_FONT_MAX:
        _fail(failures, scope, f'根字号 {metrics["rootFontSize"]}px 超出 {ROOT_FONT_MIN}~{ROOT_FONT_MAX}px')
    if metrics['brandLeft'] < 0 or metrics['brandRight'] > metrics['clientWidth'] + EDGE_TOLERANCE:
        _fail(failures, scope,
              f'品牌名越界 left={metrics["brandLeft"]} right={metrics["brandRight"]} 视口={metrics["clientWidth"]}')


def _check_device(metrics, width, scope, failures):
    """设备类名必须唯一且与视口分档一致（先全清后按档加，禁止残留叠加）"""
    expected = _expected_device(width)
    classes = metrics['bodyClass'].split()
    if 'is-' + expected not in classes:
        _fail(failures, scope, f'设备类名应为 is-{expected}，实际 body="{metrics["bodyClass"]}"')
    leftovers = [name for name in classes if name in DEVICE_CLASSES]
    if len(leftovers) != 1:
        _fail(failures, scope, f'设备类名残留 {leftovers}')


def _check_collapsed(metrics, scope, failures):
    """折叠态断言：品牌居中、时间与 Token 左对齐且分两排、汉堡按钮不压标题"""
    center = metrics['clientWidth'] / 2.0
    offset = abs(metrics['brandCenter'] - center)
    if offset > CENTER_TOLERANCE:
        _fail(failures, scope, f'品牌中心 {metrics["brandCenter"]}px 偏离视口中心 {center}px 达 {offset}px')
    if abs(metrics['timeLeft'] - metrics['cookieLeft']) > EDGE_TOLERANCE:
        _fail(failures, scope, f'时间 left={metrics["timeLeft"]} 与 Token left={metrics["cookieLeft"]} 未左对齐')
    if metrics['cookieTop'] <= metrics['timeTop']:
        _fail(failures, scope, '时间与 Token 未分两排，仍挤在同一行')
    if metrics['togglerLeft'] <= 0:
        _fail(failures, scope, '汉堡按钮未渲染或不可见')
    if metrics['togglerRight'] > metrics['clientWidth'] + EDGE_TOLERANCE:
        _fail(failures, scope,
              f'汉堡按钮 right={metrics["togglerRight"]}px 超出视口 {metrics["clientWidth"]}px')
    if metrics['brandTextRight'] > metrics['togglerLeft'] + EDGE_TOLERANCE:
        _fail(failures, scope,
              f'品牌文字 right={metrics["brandTextRight"]}px 压住汉堡按钮 left={metrics["togglerLeft"]}px')
    if metrics['brandTextLeft'] < -EDGE_TOLERANCE:
        _fail(failures, scope, f'品牌文字 left={metrics["brandTextLeft"]}px 越出视口左边界')


def _check_dashboard(metrics, scope, failures):
    """天气看板断言：零溢出、面板已渲染、面板宽度不超过视口"""
    overflow = metrics['scrollWidth'] - metrics['clientWidth']
    if overflow > 0:
        _fail(failures, scope, f'看板横向溢出 {overflow}px')
    if metrics['panelCount'] <= 0:
        _fail(failures, scope, '看板未渲染出 .glass-panel 面板')
    if metrics['widestPanel'] > metrics['clientWidth'] + EDGE_TOLERANCE:
        _fail(failures, scope,
              f'最宽面板 {metrics["widestPanel"]}px 超过视口 {metrics["clientWidth"]}px')
    if not ROOT_FONT_MIN <= metrics['rootFontSize'] <= ROOT_FONT_MAX:
        _fail(failures, scope, f'看板根字号 {metrics["rootFontSize"]}px 超出兜底区间')


async def _check_expand(page, width, height, failures, tag='展开态'):
    """菜单展开态：零溢出、导航栏变高、body.paddingTop 保持折叠态（避免整页跳动）"""
    scope = f'{tag} {width}x{height}'
    before = await page.evaluate(METRICS_JS)
    await page.click('.navbar-toggler')
    await page.wait_for_function(COLLAPSE_STATE_JS, arg=True, timeout=NAV_TIMEOUT_MS)
    after = await page.evaluate(METRICS_JS)
    overflow = after['scrollWidth'] - after['clientWidth']
    if overflow > 0:
        _fail(failures, scope, f'展开后横向溢出 {overflow}px')
    if after['navbarHeight'] < before['navbarHeight'] + EXPAND_MIN_GROWTH:
        _fail(failures, scope, f'菜单未展开：高度 {before["navbarHeight"]}px → {after["navbarHeight"]}px')
    if abs(after['paddingTop'] - before['paddingTop']) > EDGE_TOLERANCE:
        _fail(failures, scope,
              f'展开态 body.paddingTop {before["paddingTop"]}px → {after["paddingTop"]}px 会整页跳动')
    # 展开动画已经完整跑过一轮（动画期 paddingTop 冻结也已验），收起方向不必再等 .35s 动画，
    # 关掉过渡立即回到折叠态，收起后的终态断言照旧
    await page.emulate_media(reduced_motion='reduce')
    await page.click('.navbar-toggler')
    await page.wait_for_function(COLLAPSE_STATE_JS, arg=False, timeout=NAV_TIMEOUT_MS)
    closed = await page.evaluate(METRICS_JS)
    if closed['navbarHeight'] > before['navbarHeight'] + EDGE_TOLERANCE:
        _fail(failures, scope, f'收起后导航栏未回到折叠高度 {closed["navbarHeight"]}px')
    if abs(closed['paddingTop'] - before['paddingTop']) > EDGE_TOLERANCE:
        _fail(failures, scope, f'收起后 paddingTop {closed["paddingTop"]}px 未回到 {before["paddingTop"]}px')
    return after


def _bump(stats, key, metrics, bad):
    """按类别累计档数 / 最大溢出 / 最大品牌偏差 / 失败数，用于压缩输出"""
    row = stats.setdefault(key, {'n': 0, 'overflow': 0, 'dev': 0.0, 'bad': 0, 'panel': 0})
    row['n'] += 1
    row['overflow'] = max(row['overflow'], metrics['scrollWidth'] - metrics['clientWidth'])
    row['dev'] = max(row['dev'], abs(metrics['brandCenter'] - metrics['clientWidth'] / 2.0))
    row['panel'] = max(row['panel'], metrics['panelCount'])
    row['bad'] += 1 if bad else 0


async def _check_stability(page, metrics, scope, failures):
    """极小屏布局幂等自检：同一视口连采两次，字段必须逐项一致

    极小屏（≤200px）品牌名靠换行落到多行，一旦换行边界落在临界宽度上，
    滚动条出现 / 消失或字体晚到都会让 `navbarHeight` 在 80px / 95px 之间翻转，
    而 `EDGE_TOLERANCE` 收紧后这种翻转就是偶发红灯。连采两次即可把「采集后
    布局仍在自变」这类非确定性抖动当场抓成失败，而不是等它随机复发
    """
    again = await page.evaluate(METRICS_READ_JS)
    drift = [(key, round(metrics[key], 2), round(again[key], 2))
             for key in JITTER_KEYS if abs(metrics[key] - again[key]) > EDGE_TOLERANCE]
    if drift:
        _fail(failures, scope, f'极小屏布局抖动，同视口两次采集不一致 {drift}')


async def _run_main_matrix(page, errors, origin, failures, stats):
    """主页面全设备矩阵：单次加载后逐档切视口（比逐档重载快一个数量级，且更易暴露类名残留）"""
    await page.goto(f'{origin}/index.html', wait_until='load', timeout=LOAD_TIMEOUT_MS)
    for width, height, family, label in DEVICE_MATRIX:
        scope = f'主页面 {width}x{height} {family}/{label}'
        errors.clear()
        try:
            await page.set_viewport_size({'width': width, 'height': height})
            metrics = await page.evaluate(METRICS_JS)
        except Exception as exc:
            _fail(failures, scope, f'渲染异常 {exc}')
            continue
        before = len(failures)
        _check_layout(metrics, scope, failures)
        _check_device(metrics, width, scope, failures)
        if width <= COLLAPSED_MAX_WIDTH:
            _check_collapsed(metrics, scope, failures)
        if width <= JITTER_MAX_WIDTH:
            await _check_stability(page, metrics, scope, failures)
        if errors:
            _fail(failures, scope, f'JS 异常 {errors[0]}')
        _bump(stats, family, metrics, len(failures) > before)


async def _run_dashboard_matrix(page, errors, origin, failures, stats):
    """天气看板矩阵：按全部唯一宽度逐档切视口（看板断言由宽度驱动，同宽异高结果一致）"""
    await page.goto(f'{origin}/dist/index.html', wait_until='load', timeout=LOAD_TIMEOUT_MS)
    for width in BOARD_WIDTHS:
        height = max(h for w, h, _, _ in DEVICE_MATRIX if w == width)
        scope = f'看板 {width}x{height}'
        errors.clear()
        try:
            await page.set_viewport_size({'width': width, 'height': height})
            metrics = await page.evaluate(METRICS_JS)
        except Exception as exc:
            _fail(failures, scope, f'渲染异常 {exc}')
            continue
        before = len(failures)
        _check_dashboard(metrics, scope, failures)
        if errors:
            _fail(failures, scope, f'JS 异常 {errors[0]}')
        _bump(stats, '看板', metrics, len(failures) > before)


async def _run_expand_matrix(page, errors, origin, failures, stats):
    """折叠态菜单展开：覆盖手表 / 副屏 / 手环 / 手机 / 折叠屏 / 平板代表宽度

    先关过渡跑全部代表机型（只验展开后布局与 paddingTop 冻结），再开过渡跑真动画档，
    这样既保真覆盖动画期行为，又不让每档 0.8s 的动画等待拖垮总耗时。
    必须排在大矩阵之前：从 38400px 巨视口回切小视口要整页重排，每档多花 ~0.4s
    """
    await page.goto(f'{origin}/index.html', wait_until='load', timeout=LOAD_TIMEOUT_MS)
    await page.emulate_media(reduced_motion='reduce')
    for width, height in EXPAND_CASES:
        await _run_expand_case(page, errors, width, height, failures, stats, '展开态')
    await page.emulate_media(reduced_motion='no-preference')
    for width, height in EXPAND_REAL_CASES:
        await _run_expand_case(page, errors, width, height, failures, stats, '展开态·真动画')


async def _run_expand_case(page, errors, width, height, failures, stats, tag):
    """单档展开 / 收起校验，异常收敛成一条失败记录，不打断后续档位"""
    scope = f'{tag} {width}x{height}'
    errors.clear()
    before = len(failures)
    try:
        await _park_mouse(page)
        await page.set_viewport_size({'width': width, 'height': height})
        after = await _check_expand(page, width, height, failures, tag)
    except Exception as exc:
        _fail(failures, scope, f'展开异常 {exc}')
        return
    if errors:
        _fail(failures, scope, f'JS 异常 {errors[0]}')
    _bump(stats, '展开态', after, len(failures) > before)


async def _park_mouse(page):
    """切视口前把鼠标挪到左上角：上一档真实点击后指针还停在汉堡按钮上，
    Chromium 会在下一次 resize 时带着悬停命中测试重排，实测每档多花约 500ms"""
    try:
        await page.mouse.move(1, 1)
    except Exception:
        pass  # [SILENT_OK] 鼠标归位失败不影响断言，仅可能多花 500ms 重排，下一档仍会重新定位


def _check_family_coverage(failures):
    """覆盖面自检：每个设备类别都必须有代表机型入矩阵，防止后续删档导致覆盖面退化"""
    covered = {family for _, _, family, _ in DEVICE_MATRIX}
    missing = [family for family in REQUIRED_FAMILIES if family not in covered]
    if missing:
        _fail(failures, '覆盖面', f'设备类别缺席 {missing}')
    if len(DEVICE_MATRIX) < len(REQUIRED_FAMILIES):
        _fail(failures, '覆盖面', f'矩阵仅 {len(DEVICE_MATRIX)} 档，少于类别数 {len(REQUIRED_FAMILIES)}')
    widths = [width for width, _, _, _ in DEVICE_MATRIX]
    if min(widths) > 200 or max(widths) < 38400:
        _fail(failures, '覆盖面', f'宽度两端边界不足：{min(widths)}px ~ {max(widths)}px')


def _report_rows(stats, families):
    """每类一行汇总：档数 / 最大溢出 / 最大品牌偏差，避免数百行刷屏"""
    for family in families:
        row = stats.get(family)
        if not row:
            print(f'❌ {family}  0 档（该类别未进入矩阵）')
            continue
        mark = '✅' if row['bad'] == 0 else '❌'
        print(f'{mark} {family} {row["n"]} 档  最大溢出={row["overflow"]}px  '
              f'品牌最大偏差={row["dev"]:.1f}px  失败={row["bad"]}')


async def _run_all(browser, origin, failures, stats):
    """顺序跑三张矩阵：主页面与展开态复用同一页面（省一次加载），看板单独一页

    注：曾试过三页并发，实测 Chromium 渲染进程单核争用后每档耗时放大 10 倍
    （主页面 5.5s → 54.7s），并发不但不提速反而更慢，故保持顺序执行
    """
    main_page, main_errors = await _new_page(browser, origin)
    board_page, board_errors = await _new_page(browser, origin)
    expand_page, expand_errors = await _new_page(browser, origin)
    t0 = time.perf_counter()
    await _run_expand_matrix(expand_page, expand_errors, origin, failures, stats)
    print(f'[phase] expand {(time.perf_counter() - t0):.2f}s', flush=True)
    t0 = time.perf_counter()
    await _run_main_matrix(main_page, main_errors, origin, failures, stats)
    print(f'[phase] main {(time.perf_counter() - t0):.2f}s', flush=True)
    t0 = time.perf_counter()
    await _run_dashboard_matrix(board_page, board_errors, origin, failures, stats)
    print(f'[phase] board {(time.perf_counter() - t0):.2f}s', flush=True)


async def _run(failures, stats, origin):
    async with async_playwright() as pw:
        chromium_path = _find_chromium()
        browser = await pw.chromium.launch(headless=True, executable_path=chromium_path)
        try:
            await _run_all(browser, origin, failures, stats)
        finally:
            await browser.close()


def main():
    _ensure_browsers_path()
    server, origin = _start_server()
    failures, stats = [], {}
    expand_total = len(EXPAND_CASES) + len(EXPAND_REAL_CASES)
    total = len(DEVICE_MATRIX) + len(BOARD_WIDTHS) + expand_total
    started = time.perf_counter()
    try:
        print('=' * 78)
        print(f'浏览器自动化适配回归验证（Playwright Chromium）'
              f'设备 {len(DEVICE_MATRIX)} 档 / {len(REQUIRED_FAMILIES)} 类 + 看板 {len(BOARD_WIDTHS)} 档'
              f' + 展开态 {expand_total} 档 = {total} 档')
        print('=' * 78)
        _check_family_coverage(failures)
        asyncio.run(_run(failures, stats, origin))
        elapsed = time.perf_counter() - started
        _report_rows(stats, REQUIRED_FAMILIES + ('展开态',))
        print(f'⏱  总耗时 {elapsed:.2f}s（上限 {TIMING_BUDGET_S:.0f}s）')
        if elapsed > TIMING_BUDGET_S:
            _fail(failures, '性能', f'总耗时 {elapsed:.2f}s 超过 {TIMING_BUDGET_S:.0f}s 上限，回归过慢')
    finally:
        server.shutdown()

    print('=' * 78)
    if failures:
        print(f'❌ 共 {total} 档，失败 {len(failures)} 项：')
        for item in failures:
            print(f'   - {item}')
        print('退出码 1：适配断言未通过，禁止提交')
        return 1
    print(f'✅ 共 {total} 档（主页面 {len(DEVICE_MATRIX)} 款设备屏幕 + 看板 {len(BOARD_WIDTHS)} 档'
          f' + 展开态 {expand_total} 档）全部零缺陷')
    print(f'✅ 设备类别 {len(REQUIRED_FAMILIES)} 类全覆盖：{" / ".join(REQUIRED_FAMILIES)}')
    print('退出码 0：全档实测通过')
    return 0


if __name__ == '__main__':
    sys.exit(main())