import json
import time
import asyncio
import os
import re
import platform
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


VERSION = "2.0.1"


try:
    from playwright.async_api import async_playwright
except ImportError:
    print("请安装playwright: pip install playwright")
    print("然后运行: playwright install chromium")
    sys.exit(1)