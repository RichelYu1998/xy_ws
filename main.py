import json
import time
import asyncio
import os
import re
import platform
import sys
import shutil
import subprocess
import threading
import uuid
import logging
import base64
import glob
import gzip
import traceback
import select
import argparse
import socket
import smtplib
import io
import urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Any, Callable, TypeVar, Union, Tuple

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    from playwright.async_api import async_playwright
except ImportError:
    async_playwright = None

try:
    import openpyxl
except ImportError:
    openpyxl = None

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置 Playwright CDN 加速（如 run.sh 已设置则使用其值）

if not hasattr(subprocess, 'CREATE_NO_WINDOW'):
    subprocess.CREATE_NO_WINDOW = 0x08000000 if platform.system() == 'Windows' else 0


class AppException(Exception):
    """统一异常类 - 所有业务异常都使用此类"""
    
    CATEGORY_FILE = 'FILE'
    CATEGORY_NETWORK = 'NETWORK'
    CATEGORY_AUTH = 'AUTH'
    CATEGORY_BROWSER = 'BROWSER'
    CATEGORY_PARSE = 'PARSE'
    CATEGORY_CONFIG = 'CONFIG'
    CATEGORY_EXCEL = 'EXCEL'
    CATEGORY_EMAIL = 'EMAIL'
    CATEGORY_PERMISSION = 'PERMISSION'
    CATEGORY_RESOURCE = 'RESOURCE'
    CATEGORY_VALIDATION = 'VALIDATION'
    CATEGORY_DATABASE = 'DATABASE'
    
    _CATEGORY_CODES = {
        CATEGORY_FILE: 'FILE_ERROR',
        CATEGORY_NETWORK: 'NETWORK_ERROR',
        CATEGORY_AUTH: 'AUTH_ERROR',
        CATEGORY_BROWSER: 'BROWSER_ERROR',
        CATEGORY_PARSE: 'PARSE_ERROR',
        CATEGORY_CONFIG: 'CONFIG_ERROR',
        CATEGORY_EXCEL: 'EXCEL_ERROR',
        CATEGORY_EMAIL: 'EMAIL_ERROR',
        CATEGORY_PERMISSION: 'PERMISSION_ERROR',
        CATEGORY_RESOURCE: 'RESOURCE_ERROR',
        CATEGORY_VALIDATION: 'VALIDATION_ERROR',
        CATEGORY_DATABASE: 'DATABASE_ERROR',
    }
    
    def __init__(self, message: str, category: str = None, code: str = None, details: Any = None):
        self.message = message
        self.category = category or 'APP'
        self.code = code or self._CATEGORY_CODES.get(self.category, 'APP_ERROR')
        self.details = details or {}
        super().__init__(self.message)
    
    @classmethod
    def file_error(cls, message: str, file_path: str = None, operation: str = None, **kwargs):
        """文件操作异常"""
        details = {'file_path': file_path, 'operation': operation}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_FILE, details=details)
    
    @classmethod
    def network_error(cls, message: str, url: str = None, status_code: int = None, **kwargs):
        """网络请求异常"""
        details = {'url': url, 'status_code': status_code}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_NETWORK, details=details)
    
    @classmethod
    def auth_error(cls, message: str, cookie_file: str = None, **kwargs):
        """认证异常"""
        details = {'cookie_file': cookie_file}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_AUTH, details=details)
    
    @classmethod
    def browser_error(cls, message: str, browser_error: str = None, **kwargs):
        """浏览器操作异常"""
        details = {'browser_error': browser_error}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_BROWSER, details=details)
    
    @classmethod
    def parse_error(cls, message: str, data_type: str = None, raw_data: Any = None, **kwargs):
        """数据解析异常"""
        details = {'data_type': data_type, 'raw_data': str(raw_data)[:200] if raw_data else None}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_PARSE, details=details)
    
    @classmethod
    def config_error(cls, message: str, config_key: str = None, **kwargs):
        """配置异常"""
        details = {'config_key': config_key}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_CONFIG, details=details)
    
    @classmethod
    def excel_error(cls, message: str, excel_file: str = None, sheet_name: str = None, **kwargs):
        """Excel操作异常"""
        details = {'excel_file': excel_file, 'sheet_name': sheet_name}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_EXCEL, details=details)
    
    @classmethod
    def email_error(cls, message: str, smtp_host: str = None, recipient: str = None, **kwargs):
        """邮件发送异常"""
        details = {'smtp_host': smtp_host, 'recipient': recipient}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_EMAIL, details=details)
    
    @classmethod
    def permission_error(cls, message: str, path: str = None, operation: str = None, **kwargs):
        """权限异常"""
        details = {'path': path, 'operation': operation}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_PERMISSION, details=details)
    
    @classmethod
    def resource_error(cls, message: str, resource_type: str = None, resource_id: str = None, **kwargs):
        """资源异常"""
        details = {'resource_type': resource_type, 'resource_id': resource_id}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_RESOURCE, details=details)
    
    @classmethod
    def validation_error(cls, message: str, field: str = None, **kwargs):
        """数据验证异常"""
        details = {'field': field}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_VALIDATION, details=details)
    
    @classmethod
    def database_error(cls, message: str, table: str = None, query: str = None, **kwargs):
        """数据库异常"""
        details = {'table': table, 'query': query}
        details.update(kwargs)
        return cls(message, category=cls.CATEGORY_DATABASE, details=details)
    
    def to_dict(self) -> dict:
        return {
            'error': self.__class__.__name__,
            'category': self.category,
            'code': self.code,
            'message': self.message,
            'details': self.details
        }


class ExceptionHandler:
    """统一异常处理器"""
    
    _instance = None
    _logger = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._setup_logger()
        self._error_counts = {}
        self._error_history = []
        self._max_history = 100
    
    def _setup_logger(self):
        """设置日志记录器"""
        if self._logger is None:
            self._logger = logging.getLogger('ExceptionHandler')
            self._logger.setLevel(logging.ERROR)
            if not self._logger.handlers:
                handler = logging.StreamHandler()
                handler.setFormatter(logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                ))
                self._logger.addHandler(handler)
    
    def handle(self, error: Exception, context: str = '', show_traceback: bool = True) -> str:
        """处理异常并返回错误信息"""
        error_type = type(error).__name__
        error_msg = str(error)
        
        self._error_counts[error_type] = self._error_counts.get(error_type, 0) + 1
        
        error_record = {
            'timestamp': datetime.now().isoformat(),
            'type': error_type,
            'message': error_msg,
            'context': context
        }
        self._error_history.append(error_record)
        if len(self._error_history) > self._max_history:
            self._error_history.pop(0)
        
        if isinstance(error, AppException):
            full_msg = f"[{error.code}] {error.message}"
        else:
            full_msg = f"[{error_type}] {error_msg}"
        
        if context:
            full_msg = f"{context}: {full_msg}"
        
        print(f'错误: {full_msg}')
        if show_traceback:
            traceback.print_exc()
        
        self._logger.error(full_msg, exc_info=show_traceback)
        
        return full_msg
    
    def try_execute(self, func: Callable, default: Any = None, context: str = '') -> Any:
        """统一异常处理包装器 - 用于需要捕获异常并返回默认值的场景"""
        try:
            return func()
        except Exception as e:
            self.handle(e, context)
            return default
    
    def try_execute_with_error(self, func: Callable, context: str = '') -> Tuple[Any, str]:
        """统一异常处理包装器 - 用于需要获取错误信息的场景"""
        try:
            return func(), None
        except Exception as e:
            error_msg = self.handle(e, context)
            return None, error_msg
    
    def get_error_counts(self) -> dict:
        """获取错误统计"""
        return self._error_counts.copy()
    
    def get_error_history(self, limit: int = 10) -> List[dict]:
        """获取错误历史"""
        return self._error_history[-limit:]


class ExceptionContext:
    """异常处理上下文管理器"""
    
    def __init__(self, context: str = '', default: Any = None, show_traceback: bool = True):
        self.context = context
        self.default = default
        self.show_traceback = show_traceback
        self.handler = ExceptionHandler()
        self.result = None
        self.error = None
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.error = self.handler.handle(exc_val, self.context, self.show_traceback)
            self.result = self.default
            return True
        return False
    
    def get_result(self) -> Tuple[Any, str]:
        """获取结果和错误信息"""
        return self.result, self.error


T = TypeVar('T')


def safe_call(func: Callable[..., T], *args, default: T = None, context: str = '', **kwargs) -> T:
    """安全调用函数，返回默认值"""
    handler = ExceptionHandler()
    return handler.try_execute(lambda: func(*args, **kwargs), default, context)


def safe_call_with_error(func: Callable[..., T], *args, context: str = '', **kwargs) -> Tuple[T, str]:
    """安全调用函数，返回(结果, 错误信息)"""
    handler = ExceptionHandler()
    return handler.try_execute_with_error(lambda: func(*args, **kwargs), context)


def handle_error(error: Exception, context: str = '') -> str:
    """处理已捕获的异常"""
    handler = ExceptionHandler()
    return handler.handle(error, context)


def safe_execute_func(func: Callable, default: Any = None, context: str = '') -> Any:
    """统一异常处理包装器 - 用于需要捕获异常并返回默认值的场景"""
    handler = ExceptionHandler()
    return handler.try_execute(func, default, context)


def safe_execute_with_error(func: Callable, context: str = '') -> Tuple[Any, str]:
    """统一异常处理包装器 - 用于需要获取错误信息的场景"""
    handler = ExceptionHandler()
    return handler.try_execute_with_error(func, context)


def handle_exception(e: Exception, context: str = '') -> str:
    """统一异常处理函数 - 用于已捕获异常的场景"""
    handler = ExceptionHandler()
    return handler.handle(e, context)


def exception_handler(context: str = '', default: Any = None, reraise: bool = False, custom_exc: type = None):
    """统一异常处理装饰器
    
    Args:
        context: 错误上下文描述
        default: 异常时返回的默认值
        reraise: 是否在异常时重新抛出统一的自定义异常
        custom_exc: 自定义异常类型（如果reraise=True）
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AppException:
                raise
            except Exception as e:
                handler = ExceptionHandler()
                handler.handle(e, context)
                if reraise and custom_exc:
                    raise custom_exc(str(e)) from e
                return default
        return wrapper
    return decorator


def file_operation_handler(operation: str):
    """文件操作异常处理装饰器"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PermissionError as e:
                raise AppException.permission_error(
                    f"文件操作{operation}失败（权限不足）",
                    path=str(args[0]) if args else kwargs.get('path'),
                    operation=operation
                ) from e
            except FileNotFoundError as e:
                raise AppException.file_error(
                    f"文件操作{operation}失败（文件不存在）",
                    file_path=str(args[0]) if args else kwargs.get('path'),
                    operation=operation
                ) from e
            except OSError as e:
                raise AppException.file_error(
                    f"文件操作{operation}失败（系统错误）: {e}",
                    file_path=str(args[0]) if args else kwargs.get('path'),
                    operation=operation
                ) from e
        return wrapper
    return decorator


def network_handler(url: str = None):
    """网络请求异常处理装饰器"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except urllib.error.HTTPError as e:
                raise AppException.network_error(
                    f"网络请求失败（HTTP {e.code}）",
                    url=url or str(args[0]) if args else None,
                    status_code=e.code
                ) from e
            except urllib.error.URLError as e:
                raise AppException.network_error(
                    f"网络请求失败（连接错误）: {e.reason}",
                    url=url or str(args[0]) if args else None
                ) from e
            except Exception as e:
                raise AppException.network_error(
                    f"网络请求失败: {e}",
                    url=url or str(args[0]) if args else None
                ) from e
        return wrapper
    return decorator


def json_handler(context: str = ''):
    """JSON解析异常处理装饰器"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except json.JSONDecodeError as e:
                raise AppException.parse_error(
                    f"JSON解析失败: {e}",
                    data_type='json',
                    raw_data=str(e)
                ) from e
        return wrapper
    return decorator


def excel_handler(operation: str = '操作'):
    """Excel操作异常处理装饰器"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PermissionError as e:
                if "sharing violation" in str(e).lower() or "另一个程序" in str(e) or "正在使用" in str(e):
                    raise AppException.excel_error(
                        f"Excel文件{operation}失败（共享违规）",
                        excel_file=str(args[0]) if args else kwargs.get('excel_file')
                    ) from e
                raise AppException.excel_error(
                    f"Excel文件{operation}失败（权限不足）",
                    excel_file=str(args[0]) if args else kwargs.get('excel_file')
                ) from e
            except Exception as e:
                raise AppException.excel_error(
                    f"Excel文件{operation}失败: {e}",
                    excel_file=str(args[0]) if args else kwargs.get('excel_file')
                ) from e
        return wrapper
    return decorator


from flask import Flask, request, jsonify, send_file, send_from_directory, Response

if pd is None:
    print("警告: pandas未安装，Excel对比功能将不可用")

if async_playwright is None:
    print("警告: playwright未安装，浏览器自动化功能将不可用")
    print("请运行: pip install playwright && playwright install chromium")

if openpyxl is None:
    print("警告: openpyxl未安装，Excel功能将不可用")

# 文件写入锁，防止多线程同时写入同一文件
file_write_lock = threading.Lock()

# Web日志文件路径
web_log_file = None

class TeeOutput:
    """同时输出到控制台和文件"""
    def __init__(self, original, log_file_path=None):
        self.original = original
        self.log_file_path = log_file_path
        self.file = None
        if log_file_path:
            safe_execute_func(
                lambda: setattr(self, 'file', open(log_file_path, 'a', encoding='utf-8')),
                context='TeeOutput初始化'
            )
    
    def write(self, text):
        self.original.write(text)
        if self.file:
            safe_execute_func(
                lambda: (self.file.write(text), self.file.flush()),
                context='TeeOutput写入'
            )
    
    def flush(self):
        self.original.flush()
        if self.file:
            safe_execute_func(
                lambda: self.file.flush(),
                context='TeeOutput刷新'
            )
    
    def close(self):
        if self.file:
            safe_execute_func(
                lambda: self.file.close(),
                context='TeeOutput关闭'
            )
    
    def isatty(self):
        return False

def setup_web_logging():
    """设置Web模式下的日志输出"""
    global web_log_file
    web_log_file = PathManager.get_web_output_file()
    safe_execute_func(
        lambda: open(web_log_file, 'w', encoding='utf-8').write("=" * 50 + "\nSzwego商品爬虫 - Web服务\n" + "=" * 50 + "\n"),
        context='setup_web_logging'
    )
    sys.stdout = TeeOutput(sys.stdout, web_log_file)
    sys.stderr = TeeOutput(sys.stderr, web_log_file)

def log_print(*args, **kwargs):
    """同时输出到控制台和 web_output.log"""
    global web_log_file
    msg = ' '.join(str(a) for a in args)
    print(msg, **kwargs)
    if web_log_file:
        safe_execute_func(
            lambda: open(web_log_file, 'a', encoding='utf-8').write(msg + '\n'),
            context='log_print'
        )

def format_size(size_bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def setup_logger(log_file: Optional[str] = None, log_level: int = logging.INFO, stream=None) -> logging.Logger:
    logger = logging.getLogger('FileCleaner')
    logger.setLevel(log_level)
    logger.handlers.clear()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler = logging.StreamHandler(stream)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    if log_file:
        safe_execute_func(
            lambda: logger.addHandler(logging.FileHandler(log_file, encoding='utf-8')),
            context='setup_logger'
        )
        for h in logger.handlers:
            if isinstance(h, logging.FileHandler):
                h.setLevel(log_level)
                h.setFormatter(formatter)
    return logger


IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.svg'}
VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.m4v'}
MEDIA_EXTENSIONS = IMAGE_EXTENSIONS | VIDEO_EXTENSIONS
EXCLUDE_EXTENSIONS = {'.log', '.sh', '.py', '.bat', '.json', '.md', '.txt', '.html', '.htm', '.sql', '.xml', '.yml', '.yaml', '.ini', '.cfg', '.conf'}
EXCLUDE_FOLDERS = {'file', 'config', '__pycache__', 'clean', '.venv', 'templates', '.git', '.idea', 'node_modules', '.vscode', 'static'}
EXCLUDE_FILE_NAMES = {'.DS_Store', 'Thumbs.db', '.gitkeep', '.gitignore'}  # 特殊文件名保护


def clean_old_files(
        directory: str,
        dry_run: bool = False,
        log_file: Optional[str] = None,
        log_level: int = logging.INFO,
        stream=None
) -> None:
    logger = setup_logger(log_file, log_level, stream)
    logger.info("=" * 60)
    logger.info("开始清理旧文件")
    logger.info(f"清理目录: {directory}")
    logger.info(f"保留规则: 最新的一组文件（'_'前完全一致的为一组）")
    logger.info(f"排序方式: 按文件下载到本地的毫秒时间")
    logger.info(f"测试模式: {'是' if dry_run else '否'}")
    logger.info("=" * 60)

    directory = Path(directory)

    if not directory.exists():
        logger.error(f"目录不存在: {directory}")
        return

    if not directory.is_dir():
        logger.error(f"路径不是目录: {directory}")
        return

    matched_files = []
    logger.info("扫描文件中...")
    for file in directory.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            if ext in MEDIA_EXTENSIONS:
                with ExceptionContext(f"clean_old_files扫描 {file.name}", default=None) as ctx:
                    file_stat = file.stat()
                    mtime = file_stat.st_mtime
                    download_time = datetime.fromtimestamp(mtime)

                    name_without_ext = file.stem
                    group_key = name_without_ext.split('_')[0] if '_' in name_without_ext else name_without_ext

                    matched_files.append({
                        'file': file,
                        'group_key': group_key,
                        'ext': ext,
                        'is_image': ext in IMAGE_EXTENSIONS,
                        'is_video': ext in VIDEO_EXTENSIONS,
                        'mtime': mtime,
                        'size': file_stat.st_size,
                        'download_time': download_time
                    })

    if not matched_files:
        logger.warning("没有找到图片或视频文件")
        return

    matched_files.sort(key=lambda x: x['mtime'], reverse=True)
    logger.info(f"按文件下载到本地的毫秒时间排序（从最新到最旧）")

    total_files = len(matched_files)
    image_count = sum(1 for f in matched_files if f['is_image'])
    video_count = sum(1 for f in matched_files if f['is_video'])
    total_size = sum(f['size'] for f in matched_files)

    logger.info(f"找到 {total_files} 个符合条件的文件")
    logger.info(f"  - 图片: {image_count} 个")
    logger.info(f"  - 视频: {video_count} 个")
    logger.info(f"  - 总大小: {format_size(total_size)}")

    groups = {}
    for file_info in matched_files:
        group_key = file_info['group_key']
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(file_info)

    def get_group_latest_mtime(group_key):
        group_files = groups[group_key]
        return max(f['mtime'] for f in group_files)

    sorted_group_keys = sorted(groups.keys(), key=get_group_latest_mtime, reverse=True)

    logger.info(f"共 {len(groups)} 组文件（按'_'前部分分组）")
    for i, group_key in enumerate(sorted_group_keys[:5], 1):
        group_files = groups[group_key]
        latest_file = max(group_files, key=lambda x: x['mtime'])
        group_time = latest_file['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        group_images = sum(1 for f in group_files if f['is_image'])
        group_videos = sum(1 for f in group_files if f['is_video'])
        logger.info(
            f"  组{i}: {group_key} - {len(group_files)}个文件 (图片:{group_images}, 视频:{group_videos}, 最新下载时间:{group_time})")

    if len(sorted_group_keys) > 5:
        logger.info(f"  ... 还有 {len(sorted_group_keys) - 5} 组")

    latest_group_key = sorted_group_keys[0]
    latest_group = groups[latest_group_key]
    latest_file = max(latest_group, key=lambda x: x['mtime'])
    latest_time_str = latest_file['download_time'].strftime('%Y-%m-%d %H:%M:%S')

    logger.info(f"\n将保留最新的一组文件（组名: {latest_group_key}, 最新下载时间: {latest_time_str}）")
    logger.info(f"  该组共 {len(latest_group)} 个文件")
    logger.info(f"  将删除其他 {len(sorted_group_keys) - 1} 组旧文件，共 {total_files - len(latest_group)} 个文件")

    logger.info("\n文件列表（从最新到最旧）：")
    for i, file_info in enumerate(matched_files[:10], 1):
        is_latest = file_info['group_key'] == latest_group_key
        status = "保留" if is_latest else "删除"
        file_type = "图片" if file_info['is_image'] else "视频"
        download_time_str = file_info['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        logger.info(
            f"{i:3d}. [{status}] {file_info['file'].name} ({file_type}, {format_size(file_info['size'])}, 下载时间: {download_time_str})")

    if len(matched_files) > 10:
        logger.info(f"... 还有 {len(matched_files) - 10} 个文件")

    files_to_delete = [f for f in matched_files if f['group_key'] != latest_group_key]

    if not files_to_delete:
        logger.info("没有需要删除的文件")
        logger.info("清理完成")
        return

    delete_size = sum(f['size'] for f in files_to_delete)
    logger.info(f"\n准备删除 {len(files_to_delete)} 个旧文件，释放空间: {format_size(delete_size)}")

    for file_info in files_to_delete:
        file_type = "图片" if file_info['is_image'] else "视频"
        download_time_str = file_info['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        logger.info(
            f"  - {file_info['file'].name} ({file_type}, {format_size(file_info['size'])}, 下载时间: {download_time_str})")

    if dry_run:
        logger.info("\n[测试模式] 未实际删除文件")
        logger.info("清理完成（测试模式）")
        return

    logger.info("\n开始删除文件...")
    deleted_count = 0
    failed_count = 0
    deleted_size = 0

    for file_info in files_to_delete:
        with ExceptionContext(f"删除文件 {file_info['file'].name}", default=False) as ctx:
            file_info['file'].unlink()
            deleted_count += 1
            deleted_size += file_info['size']
            logger.info(f"已删除: {file_info['file'].name} ({format_size(file_info['size'])})")
            if ctx.error:
                failed_count += 1

    logger.info("\n" + "=" * 60)
    logger.info("清理完成")
    logger.info(f"成功删除: {deleted_count} 个文件，释放空间: {format_size(deleted_size)}")
    if failed_count > 0:
        logger.warning(f"删除失败: {failed_count} 个文件")
    logger.info("=" * 60)


def clean_old_files_by_time(
        directory: str,
        minutes: int = 5,
        dry_run: bool = False,
        log_file: Optional[str] = None,
        log_level: int = logging.INFO,
        stream=None
) -> None:
    logger = setup_logger(log_file, log_level, stream)
    logger.info("=" * 60)
    logger.info("开始按时间清理旧文件")
    logger.info(f"清理目录: {directory}")
    logger.info(f"删除规则: 删除 {minutes} 分钟前下载到本地的所有文件")
    logger.info(f"测试模式: {'是' if dry_run else '否'}")
    logger.info("=" * 60)

    directory = Path(directory)

    if not directory.exists():
        logger.error(f"目录不存在: {directory}")
        return

    if not directory.is_dir():
        logger.error(f"路径不是目录: {directory}")
        return

    matched_files = []
    logger.info("扫描文件中...")

    current_time = datetime.now()
    cutoff_time = current_time.timestamp() - (minutes * 60)

    for file in directory.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            if ext in MEDIA_EXTENSIONS:
                with ExceptionContext(f"clean_old_files_by_time扫描 {file.name}", default=None) as ctx:
                    file_stat = file.stat()
                    mtime = file_stat.st_mtime
                    download_time = datetime.fromtimestamp(mtime)

                    matched_files.append({
                        'file': file,
                        'ext': ext,
                        'is_image': ext in IMAGE_EXTENSIONS,
                        'is_video': ext in VIDEO_EXTENSIONS,
                        'mtime': mtime,
                        'size': file_stat.st_size,
                        'download_time': download_time
                    })

    if not matched_files:
        logger.warning("没有找到图片或视频文件")
        return

    matched_files.sort(key=lambda x: x['mtime'], reverse=True)

    total_files = len(matched_files)
    image_count = sum(1 for f in matched_files if f['is_image'])
    video_count = sum(1 for f in matched_files if f['is_video'])
    total_size = sum(f['size'] for f in matched_files)

    logger.info(f"找到 {total_files} 个符合条件的文件")
    logger.info(f"  - 图片: {image_count} 个")
    logger.info(f"  - 视频: {video_count} 个")
    logger.info(f"  - 总大小: {format_size(total_size)}")

    cutoff_time_str = datetime.fromtimestamp(cutoff_time).strftime('%Y-%m-%d %H:%M:%S')
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

    logger.info(f"\n当前时间: {current_time_str}")
    logger.info(f"删除时间阈值: {cutoff_time_str} ( {minutes} 分钟前)")

    files_to_delete = [f for f in matched_files if f['mtime'] < cutoff_time]
    files_to_keep = [f for f in matched_files if f['mtime'] >= cutoff_time]

    logger.info(f"\n将保留 {len(files_to_keep)} 个文件（{minutes} 分钟内下载的）")
    logger.info(f"将删除 {len(files_to_delete)} 个文件（{minutes} 分钟前下载的）")

    if not files_to_delete:
        logger.info("没有需要删除的文件")
        logger.info("清理完成")
        return

    delete_size = sum(f['size'] for f in files_to_delete)
    logger.info(f"\n准备删除 {len(files_to_delete)} 个旧文件，释放空间: {format_size(delete_size)}")

    logger.info("\n将要删除的文件列表：")
    for i, file_info in enumerate(files_to_delete, 1):
        file_type = "图片" if file_info['is_image'] else "视频"
        download_time_str = file_info['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        time_diff = (current_time - file_info['download_time']).total_seconds() / 60
        logger.info(
            f"{i:3d}. {file_info['file'].name} ({file_type}, {format_size(file_info['size'])}, 下载时间: {download_time_str}, {time_diff:.1f}分钟前)")

    if dry_run:
        logger.info("\n[测试模式] 未实际删除文件")
        logger.info("清理完成（测试模式）")
        return

    logger.info("\n开始删除文件...")
    deleted_count = 0
    failed_count = 0
    deleted_size = 0

    for file_info in files_to_delete:
        with ExceptionContext(f"删除文件 {file_info['file'].name}", default=False) as ctx:
            file_info['file'].unlink()
            deleted_count += 1
            deleted_size += file_info['size']
            logger.info(f"已删除: {file_info['file'].name} ({format_size(file_info['size'])})")
            if ctx.error:
                failed_count += 1

    logger.info("\n" + "=" * 60)
    logger.info("清理完成")
    logger.info(f"成功删除: {deleted_count} 个文件，释放空间: {format_size(deleted_size)}")
    if failed_count > 0:
        logger.warning(f"删除失败: {failed_count} 个文件")
    logger.info("=" * 60)


def list_files(
        directory: str,
        log_file: Optional[str] = None,
        log_level: int = logging.INFO,
        stream=None
) -> None:
    logger = setup_logger(log_file, log_level, stream)
    logger.info("=" * 60)
    logger.info("扫描文件列表")
    logger.info(f"扫描目录: {directory}")
    logger.info(f"排序方式: 按文件下载到本地的毫秒时间")
    logger.info("扫描模式: 递归扫描所有子目录")
    logger.info("=" * 60)

    directory = Path(directory)

    if not directory.exists():
        logger.error(f"目录不存在: {directory}")
        return

    matched_files = []
    scanned_dirs = 0
    logger.info("扫描文件中...")
    
    for root, dirs, files in os.walk(directory):
        root_path = Path(root)
        scanned_dirs += 1
        
        for file in files:
            file_path = root_path / file
            ext = Path(file).suffix.lower()
            if ext in MEDIA_EXTENSIONS:
                with ExceptionContext(f"list_files扫描 {file_path}", default=None) as ctx:
                    file_stat = file_path.stat()
                    mtime = file_stat.st_mtime
                    download_time = datetime.fromtimestamp(mtime)

                    matched_files.append({
                        'file': file_path,
                        'relative_path': str(file_path.relative_to(directory)),
                        'ext': ext,
                        'is_image': ext in IMAGE_EXTENSIONS,
                        'is_video': ext in VIDEO_EXTENSIONS,
                        'mtime': mtime,
                        'size': file_stat.st_size,
                        'download_time': download_time
                    })

    if not matched_files:
        logger.warning("没有找到图片或视频文件")
        return

    matched_files.sort(key=lambda x: x['mtime'], reverse=True)

    total_files = len(matched_files)
    image_count = sum(1 for f in matched_files if f['is_image'])
    video_count = sum(1 for f in matched_files if f['is_video'])
    total_size = sum(f['size'] for f in matched_files)

    logger.info(f"扫描了 {scanned_dirs} 个目录")
    logger.info(f"找到 {total_files} 个符合条件的文件")
    logger.info(f"  - 图片: {image_count} 个")
    logger.info(f"  - 视频: {video_count} 个")
    logger.info(f"  - 总大小: {format_size(total_size)}")

    logger.info("\n文件列表：")
    for i, file_info in enumerate(matched_files, 1):
        file_type = "图片" if file_info['is_image'] else "视频"
        download_time_str = file_info['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        logger.info(
            f"{i:3d}. {file_info['relative_path']} ({file_type}, {format_size(file_info['size'])}, 下载时间: {download_time_str})")

    logger.info("\n扫描完成")


def clean_all_files(
        directory: str,
        dry_run: bool = False,
        log_file: Optional[str] = None,
        log_level: int = logging.INFO,
        stream=None
) -> None:
    logger = setup_logger(log_file, log_level, stream)
    logger.info("=" * 60)
    logger.info("开始删除所有文件和文件夹")
    logger.info(f"清理目录: {directory}")
    logger.info(f"删除规则: 删除所有文件和文件夹，除了 log, sh, py, bat 格式的文件")
    logger.info(f"测试模式: {'是' if dry_run else '否'}")
    logger.info("=" * 60)

    directory = Path(directory)

    if not directory.exists():
        logger.error(f"目录不存在: {directory}")
        return

    if not directory.is_dir():
        logger.error(f"路径不是目录: {directory}")
        return

    files_to_delete = []
    folders_to_delete = []
    logger.info("扫描文件和文件夹中...")

    for item in directory.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            if item.name in EXCLUDE_FILE_NAMES:
                logger.info(f"保留文件: {item.name}")
            elif ext not in EXCLUDE_EXTENSIONS:
                files_to_delete.append(item)
            else:
                logger.info(f"保留文件: {item.name}")
        elif item.is_dir():
            if item.name not in EXCLUDE_FOLDERS:
                folders_to_delete.append(item)
            else:
                logger.info(f"保留文件夹: {item.name}")

    total_files = len(files_to_delete)
    total_folders = len(folders_to_delete)
    total_size = sum(
        safe_call(lambda f=item: f.stat().st_size, default=0, context='clean_all_files获取文件大小')
        for item in files_to_delete
    )

    logger.info(f"找到 {total_files} 个文件和 {total_folders} 个文件夹")
    logger.info(f"  - 总大小: {format_size(total_size)}")

    if not files_to_delete and not folders_to_delete:
        logger.warning("没有需要删除的文件或文件夹")
        logger.info("清理完成")
        return

    logger.info(f"\n将删除 {total_files} 个文件和 {total_folders} 个文件夹")

    if files_to_delete:
        logger.info("\n将要删除的文件列表：")
        for i, item in enumerate(files_to_delete, 1):
            file_size = safe_call(lambda f=item: f.stat().st_size, default=0, context='clean_all_files显示文件')
            logger.info(f"{i:3d}. {item.name} ({format_size(file_size)})")

    if folders_to_delete:
        logger.info("\n将要删除的文件夹列表：")
        for i, folder in enumerate(folders_to_delete, 1):
            logger.info(f"{i:3d}. {folder.name}")

    if dry_run:
        logger.info("\n[测试模式] 未实际删除文件和文件夹")
        logger.info("清理完成（测试模式）")
        return

    logger.info("\n开始删除文件...")
    deleted_files_count = 0
    deleted_folders_count = 0
    deleted_size = 0
    failed_count = 0

    for file in files_to_delete:
        with ExceptionContext(f"删除文件 {file.name}", default=False) as ctx:
            file_size = file.stat().st_size
            file.unlink()
            deleted_files_count += 1
            deleted_size += file_size
            logger.info(f"已删除文件: {file.name} ({format_size(file_size)})")
            if ctx.error:
                failed_count += 1

    for folder in folders_to_delete:
        with ExceptionContext(f"删除文件夹 {folder.name}", default=False) as ctx:
            shutil.rmtree(folder)
            deleted_folders_count += 1
            logger.info(f"已删除文件夹: {folder.name}")
            if ctx.error:
                failed_count += 1

    logger.info("\n" + "=" * 60)
    logger.info("清理完成")
    logger.info(f"成功删除: {deleted_files_count} 个文件，{deleted_folders_count} 个文件夹，释放空间: {format_size(deleted_size)}")
    if failed_count > 0:
        logger.warning(f"删除失败: {failed_count} 个项目")
    logger.info("=" * 60)


def clean_png_files(
        directory: str,
        dry_run: bool = False,
        log_file: Optional[str] = None,
        log_level: int = logging.INFO,
        stream=None
) -> None:
    logger = setup_logger(log_file, log_level, stream)
    logger.info("=" * 60)
    logger.info("开始删除PNG文件")
    logger.info(f"清理目录: {directory}")
    logger.info(f"删除规则: 删除所有以.png结尾的文件，不保留任何文件")
    logger.info(f"测试模式: {'是' if dry_run else '否'}")
    logger.info("=" * 60)

    directory = Path(directory)

    if not directory.exists():
        logger.error(f"目录不存在: {directory}")
        return

    if not directory.is_dir():
        logger.error(f"路径不是目录: {directory}")
        return

    matched_files = []
    logger.info("扫描文件中...")

    for file in directory.iterdir():
        if file.is_file() and file.name.lower().endswith('.png'):
            file_stat = file.stat()
            mtime = file_stat.st_mtime
            download_time = datetime.fromtimestamp(mtime)

            matched_files.append({
                'file': file,
                'main_num': file.name,
                'sub_num': 0,
                'ext': '.png',
                'is_image': True,
                'is_video': False,
                'mtime': mtime,
                'size': file_stat.st_size,
                'download_time': download_time
            })

    if not matched_files:
        logger.warning("没有找到PNG文件")
        return

    matched_files.sort(key=lambda x: x['mtime'], reverse=True)

    total_files = len(matched_files)
    total_size = sum(f['size'] for f in matched_files)

    logger.info(f"找到 {total_files} 个PNG文件")
    logger.info(f"  - 总大小: {format_size(total_size)}")

    logger.info(f"\n将删除所有 {total_files} 个PNG文件，释放空间: {format_size(total_size)}")

    logger.info("\n文件列表：")
    for i, file_info in enumerate(matched_files, 1):
        download_time_str = file_info['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        logger.info(
            f"{i:3d}. {file_info['file'].name} ({format_size(file_info['size'])}, 下载时间: {download_time_str})")

    if dry_run:
        logger.info("\n[测试模式] 未实际删除文件")
        logger.info("清理完成（测试模式）")
        return

    logger.info("\n开始删除文件...")
    deleted_count = 0
    failed_count = 0
    deleted_size = 0

    for file_info in matched_files:
        with ExceptionContext(f"删除PNG文件 {file_info['file'].name}", default=False) as ctx:
            file_info['file'].unlink()
            deleted_count += 1
            deleted_size += file_info['size']
            logger.info(f"已删除: {file_info['file'].name} ({format_size(file_info['size'])})")
            if ctx.error:
                failed_count += 1

    logger.info("\n" + "=" * 60)
    logger.info("清理完成")
    logger.info(f"成功删除: {deleted_count} 个文件，释放空间: {format_size(deleted_size)}")
    if failed_count > 0:
        logger.warning(f"删除失败: {failed_count} 个文件")
    logger.info("=" * 60)


def clean_media_files(
        directory: str,
        dry_run: bool = False,
        log_file: Optional[str] = None,
        log_level: int = logging.INFO,
        stream=None
) -> None:
    logger = setup_logger(log_file, log_level, stream)
    logger.info("=" * 60)
    logger.info("开始删除媒体文件")
    logger.info(f"清理目录: {directory}")
    logger.info(f"删除规则: 删除所有以.png、.jpg、.gif和.mp4结尾的文件，不保留任何文件")
    logger.info(f"测试模式: {'是' if dry_run else '否'}")
    logger.info("=" * 60)

    valid_extensions = {'.png', '.jpg', '.gif', '.mp4'}

    directory = Path(directory)

    if not directory.exists():
        logger.error(f"目录不存在: {directory}")
        return

    if not directory.is_dir():
        logger.error(f"路径不是目录: {directory}")
        return

    matched_files = []
    logger.info("扫描文件中...")

    for file in directory.iterdir():
        if file.is_file():
            ext = file.name.lower().split('.')[-1] if '.' in file.name else ''
            ext_with_dot = f'.{ext}' if ext else ''

            if ext_with_dot in valid_extensions:
                file_stat = file.stat()
                mtime = file_stat.st_mtime
                download_time = datetime.fromtimestamp(mtime)

                matched_files.append({
                    'file': file,
                    'main_num': file.name,
                    'sub_num': 0,
                    'ext': ext_with_dot,
                    'is_image': ext_with_dot in {'.png', '.jpg', '.gif'},
                    'is_video': ext_with_dot == '.mp4',
                    'mtime': mtime,
                    'size': file_stat.st_size,
                    'download_time': download_time
                })

    if not matched_files:
        logger.warning("没有找到PNG、JPG、GIF或MP4文件")
        return

    matched_files.sort(key=lambda x: x['mtime'], reverse=True)

    total_files = len(matched_files)
    png_count = sum(1 for f in matched_files if f['ext'] == '.png')
    jpg_count = sum(1 for f in matched_files if f['ext'] == '.jpg')
    gif_count = sum(1 for f in matched_files if f['ext'] == '.gif')
    video_count = sum(1 for f in matched_files if f['is_video'])
    total_size = sum(f['size'] for f in matched_files)

    logger.info(f"找到 {total_files} 个媒体文件")
    logger.info(f"  - PNG图片: {png_count} 个")
    logger.info(f"  - JPG图片: {jpg_count} 个")
    logger.info(f"  - GIF图片: {gif_count} 个")
    logger.info(f"  - MP4视频: {video_count} 个")
    logger.info(f"  - 总大小: {format_size(total_size)}")

    logger.info(f"\n将删除所有 {total_files} 个媒体文件，释放空间: {format_size(total_size)}")

    logger.info("\n文件列表：")
    for i, file_info in enumerate(matched_files, 1):
        if file_info['ext'] == '.png':
            file_type = "PNG图片"
        elif file_info['ext'] == '.jpg':
            file_type = "JPG图片"
        elif file_info['ext'] == '.gif':
            file_type = "GIF图片"
        else:
            file_type = "MP4视频"
        download_time_str = file_info['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        logger.info(
            f"{i:3d}. {file_info['file'].name} ({file_type}, {format_size(file_info['size'])}, 下载时间: {download_time_str})")

    if dry_run:
        logger.info("\n[测试模式] 未实际删除文件")
        logger.info("清理完成（测试模式）")
        return

    logger.info("\n开始删除文件...")
    deleted_count = 0
    failed_count = 0
    deleted_size = 0

    for file_info in matched_files:
        with ExceptionContext(f"删除媒体文件 {file_info['file'].name}", default=False) as ctx:
            file_info['file'].unlink()
            deleted_count += 1
            deleted_size += file_info['size']
            if file_info['ext'] == '.png':
                file_type = "PNG图片"
            elif file_info['ext'] == '.jpg':
                file_type = "JPG图片"
            elif file_info['ext'] == '.gif':
                file_type = "GIF图片"
            else:
                file_type = "MP4视频"
            logger.info(f"已删除: {file_info['file'].name} ({file_type}, {format_size(file_info['size'])})")
            if ctx.error:
                failed_count += 1

    logger.info("\n" + "=" * 60)
    logger.info("清理完成")
    logger.info(f"成功删除: {deleted_count} 个文件，释放空间: {format_size(deleted_size)}")
    if failed_count > 0:
        logger.warning(f"删除失败: {failed_count} 个文件")
    logger.info("=" * 60)


def run_cleaner():
    """文件清理工具主函数"""
    print_separator()
    print('文件清理工具')
    print_separator()
    
    default_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"默认清理目录: {default_dir}")
    
    while True:
        print('\n请选择清理模式：')
        print('1. 按组清理（保留最新的一组文件）')
        print('2. 按时间清理（删除指定分钟前的文件）')
        print('3. 列出文件（不删除）')
        print('4. 删除所有文件和文件夹')
        print('5. 删除PNG文件')
        print('6. 删除媒体文件（PNG/JPG/GIF/MP4）')
        print('0. 返回主菜单')
        print_separator()
        
        try:
            choice = input('请输入选项 (0-6): ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n已退出清理工具')
            return
        
        if choice == '0':
            print('返回主菜单')
            return
        
        # 获取目录
        dir_input = input(f'请输入清理目录（回车使用默认目录 {default_dir}）: ').strip()
        directory = dir_input if dir_input else default_dir
        
        # 询问是否测试模式
        dry_run_input = input('是否启用测试模式（不实际删除文件）？(y/n): ').strip().lower()
        dry_run = dry_run_input in ['y', 'yes', '是']
        
        log_file = os.path.join(directory, 'clean_files.log')
        
        if choice == '1':
            clean_old_files(directory=directory, dry_run=dry_run, log_file=log_file)
        elif choice == '2':
            try:
                minutes = int(input('请输入分钟数（默认5分钟）: ').strip() or '5')
                clean_old_files_by_time(directory=directory, minutes=minutes, dry_run=dry_run, log_file=log_file)
            except ValueError:
                print('无效的分钟数，使用默认值5分钟')
                clean_old_files_by_time(directory=directory, minutes=5, dry_run=dry_run, log_file=log_file)
        elif choice == '3':
            list_files(directory=directory, log_file=log_file)
        elif choice == '4':
            clean_all_files(directory=directory, dry_run=dry_run, log_file=log_file)
        elif choice == '5':
            clean_png_files(directory=directory, dry_run=dry_run, log_file=log_file)
        elif choice == '6':
            clean_media_files(directory=directory, dry_run=dry_run, log_file=log_file)
        else:
            print('无效的选项')
        
        input('\n按回车键继续...')

def print_separator(char='=', length=60):
    """打印分隔线"""
    print(char * length)

def get_version_from_readme():
    """从 README.md 自动解析最新版本号"""
    readme_path = os.path.join(PROJECT_DIR, 'README.md')
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'###\s+v(\d+\.\d+\.\d+)', content)
        if match:
            return match.group(1)
    except Exception:
        pass
    return "0.0.0"

VERSION = get_version_from_readme()

# 统一环境检测类
class Environment:
    """统一环境检测和管理"""
    
    # 系统类型
    SYSTEM = platform.system()  # 'Windows', 'Darwin'(Mac), 'Linux'
    
    # 是否为Windows系统
    IS_WINDOWS = SYSTEM == 'Windows'
    
    # 是否为Mac系统
    IS_MAC = SYSTEM == 'Darwin'
    
    # 是否为Linux系统
    IS_LINUX = SYSTEM == 'Linux'
    
    @staticmethod
    def get_venv_python():
        """获取虚拟环境Python路径"""
        if Environment.IS_WINDOWS:
            return os.path.join(PROJECT_DIR, '.venv', 'Scripts', 'python.exe')
        else:
            return os.path.join(PROJECT_DIR, '.venv', 'bin', 'python')
    
    @staticmethod
    def get_chrome_path():
        """获取Chrome浏览器路径，支持Windows、Mac和Linux系统"""
        chrome_path = None
        
        if Environment.IS_WINDOWS:
            # Windows上使用Playwright内置浏览器，避免权限问题
            chrome_path = None
        elif Environment.IS_MAC:
            if os.path.exists('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'):
                chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        elif Environment.IS_LINUX:
            # 优先检测 /chrome-linux64 目录下的Chrome
            if os.path.exists('/chrome-linux64/chrome'):
                chrome_path = '/chrome-linux64/chrome'
            elif os.path.exists('/usr/bin/google-chrome'):
                chrome_path = '/usr/bin/google-chrome'
        
        return chrome_path
    
    @staticmethod
    def get_browser_args():
        """获取浏览器启动参数，根据系统类型返回不同的参数"""
        browser_args = ['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled']
        
        if Environment.IS_WINDOWS:
            browser_args.append('--disable-gpu')
        elif Environment.IS_LINUX:
            browser_args.extend(['--disable-gpu', '--disable-dev-shm-usage'])
        
        return browser_args
    
    @staticmethod
    def get_user_agent():
        """获取用户代理字符串，根据系统类型返回不同的UA"""
        if Environment.IS_WINDOWS:
            return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        elif Environment.IS_MAC:
            return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        elif Environment.IS_LINUX:
            return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        else:
            # 默认使用Windows UA
            return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    
    @staticmethod
    def get_system_info():
        """获取系统信息"""
        return {
            'system': Environment.SYSTEM,
            'is_windows': Environment.IS_WINDOWS,
            'is_mac': Environment.IS_MAC,
            'is_linux': Environment.IS_LINUX,
            'venv_python': Environment.get_venv_python(),
            'project_dir': PROJECT_DIR
        }
    
    @staticmethod
    def test_pip_mirror(mirror_url, timeout=3):
        """测试pip镜像源速度"""
        try:
            start_time = time.time()
            urllib.request.urlopen(mirror_url, timeout=timeout)
            elapsed_time = time.time() - start_time
            return elapsed_time
        except:
            return None
    
    @staticmethod
    def get_fastest_pip_mirror():
        """获取最快的pip镜像源"""
        mirrors = [
            ('https://mirrors.aliyun.com/pypi/simple/', 'mirrors.aliyun.com'),
            ('https://pypi.tuna.tsinghua.edu.cn/simple/', 'pypi.tuna.tsinghua.edu.cn'),
            ('https://mirrors.cloud.tencent.com/pypi/simple/', 'mirrors.cloud.tencent.com'),
            ('https://mirrors.ustc.edu.cn/pypi/simple/', 'mirrors.ustc.edu.cn'),
            ('https://pypi.douban.com/simple/', 'pypi.douban.com')
        ]
        
        fastest_mirror = mirrors[0]
        min_time = float('inf')
        
        for mirror_url, host in mirrors:
            elapsed = Environment.test_pip_mirror(mirror_url)
            if elapsed is not None and elapsed < min_time:
                min_time = elapsed
                fastest_mirror = (mirror_url, host)
        
        return fastest_mirror
    
    @staticmethod
    def kill_process_by_name(process_name):
        """跨系统终止进程"""
        try:
            if Environment.IS_WINDOWS:
                subprocess.run(f'taskkill /F /IM {process_name}', shell=True, capture_output=True, timeout=10)
            else:
                subprocess.run(f'pkill -f "{process_name}"', shell=True, capture_output=True, timeout=10)
        except:
            pass
    
    @staticmethod
    def check_process_running(process_name):
        """跨系统检查进程是否运行"""
        try:
            if Environment.IS_WINDOWS:
                result = subprocess.run(f'tasklist /FI "IMAGENAME eq {process_name}"', shell=True, capture_output=True, text=True, timeout=3)
                return process_name in result.stdout
            else:
                result = subprocess.run(f'pgrep -f "{process_name}"', shell=True, capture_output=True, text=True, timeout=3)
                return result.returncode == 0
        except:
            return False

# Windows上的emoji安全打印
def safe_print(*args, **kwargs):
    """安全打印，处理Windows上的emoji编码问题"""
    try:
        print(*args, **kwargs)
    except UnicodeEncodeError:
        # Windows上无法打印emoji，替换为ASCII字符
        safe_args = []
        for arg in args:
            if isinstance(arg, str):
                # 替换emoji为ASCII字符
                safe_arg = arg
                emoji_map = {
                    '🔍': '[检查]',
                    '❌': '[错误]',
                    '✓': '[OK]',
                    '⚠️': '[警告]',
                    '✗': '[失败]',
                    '📝': '[说明]',
                    '💡': '[提示]',
                    '🚀': '[启动]',
                    '🎯': '[目标]',
                    '📊': '[数据]',
                    '🔧': '[设置]',
                    '🎉': '[完成]'
                }
                for emoji, replacement in emoji_map.items():
                    safe_arg = safe_arg.replace(emoji, replacement)
                safe_args.append(safe_arg)
            else:
                safe_args.append(arg)
        print(*safe_args, **kwargs)

# 使用Environment类的VENV_PYTHON，自动创建虚拟环境
def get_python_executable():
    """获取Python可执行文件路径，优先使用虚拟环境，不存在则创建"""
    venv_python = Environment.get_venv_python()
    if os.path.exists(venv_python):
        return venv_python
    # 虚拟环境不存在，创建它
    print(f"虚拟环境不存在，正在创建...")
    try:
        subprocess.run(
            [sys.executable, '-m', 'venv', '.venv'],
            check=True,
            capture_output=True
        )
        print(f"虚拟环境创建成功: .venv")
        return venv_python
    except Exception as e:
        print(f"创建虚拟环境失败: {e}")
        # 创建失败，fallback到系统Python
        return 'python' if Environment.IS_WINDOWS else 'python3'

VENV_PYTHON = get_python_executable()

app = Flask(__name__, template_folder='.', static_folder=None)

def get_daily_profit_report_from_excel(excel_file):
    """从Excel的'每日利润'sheet的A列中查找以'截止'开头的报表文本
    
    Args:
        excel_file: Excel文件路径
        
    Returns:
        str: 报表文本，如果未找到则返回None
    """
    if openpyxl is None:
        return None
    try:
        wb = openpyxl.load_workbook(excel_file, data_only=True)
        sheet_name = '每日利润'
        if sheet_name not in wb.sheetnames:
            wb.close()
            return None
        ws = wb[sheet_name]
        report_text = None
        # 在A列中搜索以"截止"开头的单元格
        for row in ws.iter_rows(min_col=1, max_col=1, min_row=1, max_row=ws.max_row):
            for cell in row:
                if cell.value and isinstance(cell.value, str) and cell.value.strip().startswith('截止'):
                    report_text = cell.value.strip()
                    break
            if report_text:
                break
        wb.close()
        return report_text
    except Exception as e:
        print(f"读取每日利润报表失败: {e}")
        return None

@app.errorhandler(Exception)
def handle_api_exception(e):
    """Flask全局异常处理器 - 统一处理所有未捕获的异常"""
    error_msg = handle_exception(e, 'Flask API')
    return jsonify({'error': error_msg, 'success': False, 'code': getattr(e, 'code', 'UNKNOWN')}), 500

processes = {}
tasks = {}

def run_command_background(task_id, command):
    try:
        tasks[task_id]['status'] = 'running'
        
        # 设置环境变量，确保使用UTF-8编码
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        # Windows上使用不同的参数
        if Environment.IS_WINDOWS:
            # Windows需要使用shell=True来处理路径
            # 注意：使用 stdin=DEVNULL 避免 input() 调用导致 Input/output error
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # 合并stderr到stdout
                stdin=subprocess.DEVNULL,
                cwd=PROJECT_DIR,
                text=True,
                encoding='utf-8',
                errors='replace',
                bufsize=1,  # 行缓冲
                env=env  # 设置环境变量
            )
        else:
            # Mac/Linux使用更安全的参数
            # 注意：使用 stdin=DEVNULL 避免 input() 调用导致 Input/output error
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # 合并stderr到stdout
                stdin=subprocess.DEVNULL,
                cwd=PROJECT_DIR,
                text=True,
                bufsize=1,  # 行缓冲
                env=env  # 设置环境变量
            )
        
        processes[task_id] = process
        
        stdout_lines = []
        # 使用非阻塞读取
        while True:
            # 检查进程是否结束
            if process.poll() is not None:
                # 读取剩余输出
                remaining = process.stdout.read()
                if remaining:
                    stdout_lines.append(remaining)
                break
            
            # 读取可用输出
            try:
                if Environment.IS_WINDOWS:
                    # Windows不支持select，使用超时读取
                    time.sleep(0.1)
                    line = process.stdout.readline()
                    if line:
                        stdout_lines.append(line)
                else:
                    # Mac/Linux使用select
                    readable, _, _ = select.select([process.stdout], [], [], 0.1)
                    if readable:
                        line = process.stdout.readline()
                        if line:
                            stdout_lines.append(line)
            except Exception as e:
                handle_exception(e, 'run_command_background读取输出')
            
            # 更新输出
            tasks[task_id]['output'] = ''.join(stdout_lines)
        
        process.wait()
        tasks[task_id]['returncode'] = process.returncode
        tasks[task_id]['output'] = ''.join(stdout_lines)
        tasks[task_id]['status'] = 'completed'
    except Exception as e:
        handle_exception(e, 'run_command_background')
        tasks[task_id]['error'] = str(e)
        tasks[task_id]['status'] = 'error'


class PathManager:
    """路径管理类，统一处理跨系统路径问题"""
    
    @staticmethod
    def get_config_dir():
        """获取配置文件目录"""
        return os.path.join(PROJECT_DIR, 'config')
    
    @staticmethod
    def get_file_dir():
        """获取输出文件目录"""
        return os.path.join(PROJECT_DIR, 'file')
    
    @staticmethod
    def get_config_file():
        """获取配置文件路径"""
        return os.path.join(PathManager.get_config_dir(), 'config.json')
    
    @staticmethod
    def get_cookie_file():
        """获取Cookie文件路径"""
        return os.path.join(PathManager.get_config_dir(), 'cookies.json')
    
    @staticmethod
    def get_output_file():
        """获取输出文件路径"""
        return os.path.join(PathManager.get_file_dir(), 'output.json')
    
    @staticmethod
    def get_input_file():
        """获取输入文件路径"""
        return os.path.join(PathManager.get_config_dir(), 'input_stock_numbers.txt')
    
    @staticmethod
    def get_json_filename(date_str):
        """获取JSON文件名"""
        return f"{date_str}微购相册(小旭数码).json"
    
    @staticmethod
    def get_cache_filename(date_str):
        """获取缓存文件名"""
        return f"{date_str}微购相册(小旭数码)_cache.json"
    
    @staticmethod
    def get_json_file_path(date_str):
        """获取JSON文件完整路径"""
        return os.path.join(PathManager.get_file_dir(), PathManager.get_json_filename(date_str))
    
    @staticmethod
    def get_cache_file_path(date_str):
        """获取缓存文件完整路径"""
        return os.path.join(PathManager.get_file_dir(), PathManager.get_cache_filename(date_str))
    
    @staticmethod
    def get_diff_log_file(date_str):
        """获取差异日志文件路径"""
        return os.path.join(PathManager.get_file_dir(), f'diff_log_{date_str}.json')
    
    @staticmethod
    def get_duplicate_log_file():
        """获取重复日志文件路径"""
        return os.path.join(PathManager.get_file_dir(), 'duplicate_log.json')
    
    @staticmethod
    def get_tunnel_url_file():
        """获取隧道URL文件路径"""
        return os.path.join(PathManager.get_file_dir(), 'tunnel_url.txt')
    
    @staticmethod
    def get_web_output_file():
        """获取Web输出日志文件路径"""
        return os.path.join(PathManager.get_file_dir(), 'web_output.log')
    @staticmethod
    def get_public_url_from_web_log():
        """从 web_output.log 读取公网地址（统一入口）"""
        try:
            web_log_file = PathManager.get_web_output_file()
            if os.path.exists(web_log_file):
                with open(web_log_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                match = re.search(r'Public URL:\s*(https?://[^\s]+)', content)
                if match:
                    return match.group(1).rstrip('/')
                match = re.search(r'(https://[a-zA-Z0-9_-]+\.hostc\.dev)', content)
                if match:
                    return match.group(1).rstrip('/')
        except Exception as e:
            handle_exception(e, 'get_public_url_from_web_log')
        return None
    
    @staticmethod
    def sync_web_output_from_tunnel_url():
        """从 tunnel_url.txt 同步公网地址到 web_output.log（统一入口）"""
        try:
            tunnel_file = PathManager.get_tunnel_url_file()
            web_log_file = PathManager.get_web_output_file()
            if os.path.exists(tunnel_file):
                with open(tunnel_file, 'r', encoding='utf-8') as f:
                    tunnel_content = f.read()
                
                tunnel_match = re.search(r'Public URL:\s*(https://[^\s]+)', tunnel_content)
                if not tunnel_match:
                    # 如果 tunnel_url.txt 没有 Public URL，尝试直接匹配 hostc.dev URL
                    tunnel_match = re.search(r'(https://[a-zA-Z0-9_-]+\.hostc\.dev)', tunnel_content)
                if tunnel_match:
                    new_url = tunnel_match.group(1)
                    
                    try:
                        if os.path.exists(web_log_file):
                            with open(web_log_file, 'r', encoding='utf-8') as f:
                                lines = f.readlines()
                            
                            updated = False
                            for i, line in enumerate(lines):
                                if 'Public URL:' in line and 'hostc.dev' in line:
                                    lines[i] = f"  Public URL: {new_url}\n"
                                    updated = True
                            
                            if updated:
                                with open(web_log_file, 'w', encoding='utf-8') as f:
                                    f.writelines(lines)
                                return True
                    except Exception as e:
                        print(f"[Tunnel] 更新 web_output.log 失败: {e}")
                    
                    try:
                        header = """==================================================
Szwego商品爬虫 - Web服务
==================================================
访问地址: http://localhost:8888
局域网地址: http://192.168.31.36:8888
"""
                        with open(web_log_file, 'w', encoding='utf-8') as f:
                            f.write(header)
                            f.write(f"  Public URL: {new_url}\n")
                    except Exception as e2:
                        handle_exception(e2, 'sync_web_output_from_tunnel_url重建web_output')
                        return False
                    return True
        except Exception as e:
            handle_exception(e, 'sync_web_output_from_tunnel_url同步')
        return False
    
    @staticmethod
    def ensure_dirs_exist():
        """确保所有必要的目录存在"""
        dirs = [PathManager.get_config_dir(), PathManager.get_file_dir()]
        for dir_path in dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)


class EmailNotifier:
    """邮件通知类"""
    
    def __init__(self, config_manager=None):
        self.config_manager = config_manager or ConfigManager()
    
    def get_email_config(self):
        """获取邮件配置"""
        return {
            'enabled': self.config_manager.get('email_notification_enabled', False),
            'smtp_host': self.config_manager.get('email_smtp_host', 'smtp.qq.com'),
            'smtp_port': self.config_manager.get('email_smtp_port', 587),
            'smtp_user': self.config_manager.get('email_smtp_user', ''),
            'smtp_password': self.config_manager.get('email_smtp_password', ''),
            'from_name': self.config_manager.get('email_from_name', '公网IP监控'),
            'to_email': self.config_manager.get('email_to', '980187223@qq.com'),
        }
    
    def send_tunnel_notification(self, tunnel_url, event_type='new'):
        """发送隧道URL变化通知邮件"""
        config = self.get_email_config()
        
        if not config['enabled']:
            print(f"[Email] 邮件通知未启用，跳过发送")
            return False
        
        try:
            print(f"[Email] 开始发送邮件通知: {tunnel_url} (事件类型: {event_type})")
            print(f"[Email] SMTP服务器: {config['smtp_host']}:{config['smtp_port']}")
            print(f"[Email] 发送人: {config['smtp_user']}")
            print(f"[Email] 接收人: {config['to_email']}")
            
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{Header(config['from_name'], 'utf-8').encode()} <{config['smtp_user']}>"
            msg['To'] = config['to_email']
            msg['Subject'] = Header(f'【{"新" if event_type == "new" else "更新"}公网地址】{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 'utf-8')
            
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            body = f"""公网地址已{"生成" if event_type == "new" else "更新"}

时间: {current_time}
公网地址: {tunnel_url}

请妥善保管此地址。
"""
            
            html_body = f"""
<html>
<body>
<h2>{"新公网地址已生成" if event_type == "new" else "公网地址已更新"}</h2>
<table>
<tr><td><b>时间:</b></td><td>{current_time}</td></tr>
<tr><td><b>公网地址:</b></td><td><a href="{tunnel_url}">{tunnel_url}</a></td></tr>
</table>
<p>请妥善保管此地址。</p>
</body>
</html>
"""
            
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            msg.attach(MIMEText(html_body, 'html', 'utf-8'))
            
            print(f"[Email] 正在连接SMTP服务器...")
            timeout = 30
            if config['smtp_port'] == 465:
                server = smtplib.SMTP_SSL(config['smtp_host'], config['smtp_port'], timeout=timeout)
            else:
                server = smtplib.SMTP(config['smtp_host'], config['smtp_port'], timeout=timeout)
                server.starttls()
            
            print(f"[Email] 正在登录SMTP服务器...")
            server.login(config['smtp_user'], config['smtp_password'])
            
            print(f"[Email] 正在发送邮件...")
            server.sendmail(config['smtp_user'], config['to_email'], msg.as_string())
            server.quit()
            
            print(f"[Email] 已成功发送邮件通知到 {config['to_email']}")
            return True
        except smtplib.SMTPServerDisconnected as e:
            handle_exception(e, 'Email SMTP连接断开')
            raise AppException.email_error(
                f"SMTP连接断开: {e}。请检查网络连接或SMTP服务器配置",
                smtp_host=config['smtp_host'],
                recipient=config['to_email']
            )
        except smtplib.SMTPAuthenticationError as e:
            handle_exception(e, 'Email SMTP认证')
            raise AppException.email_error(
                f"SMTP认证失败: {e}。请检查邮箱账号和授权码",
                smtp_host=config['smtp_host'],
                recipient=config['to_email']
            )
        except smtplib.SMTPException as e:
            handle_exception(e, 'Email SMTP错误')
            raise AppException.email_error(
                f"SMTP错误: {e}",
                smtp_host=config['smtp_host'],
                recipient=config['to_email']
            )
        except Exception as e:
            handle_exception(e, 'Email发送失败')
            raise AppException.email_error(
                f"发送邮件失败: {e}",
                smtp_host=config['smtp_host'],
                recipient=config['to_email']
            )
    
    def save_email_config(self, smtp_host, smtp_port, smtp_user, smtp_password, from_name, to_email):
        """保存邮件配置"""
        self.config_manager.set('email_notification_enabled', True)
        self.config_manager.set('email_smtp_host', smtp_host)
        self.config_manager.set('email_smtp_port', smtp_port)
        self.config_manager.set('email_smtp_user', smtp_user)
        self.config_manager.set('email_smtp_password', smtp_password)
        self.config_manager.set('email_from_name', from_name)
        self.config_manager.set('email_to', to_email)
        return True


class ConfigManager:
    def __init__(self, config_path=None):
        self.config_path = config_path or PathManager.get_config_file()
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
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            handle_exception(e, 'ConfigManager JSON解析')
            raise AppException.config_error(
                f"配置文件格式错误: {e}",
                config_key=self.config_path
            )
        except Exception as e:
            handle_exception(e, 'ConfigManager加载配置')
            raise AppException.config_error(
                f"加载配置文件失败: {e}",
                config_key=self.config_path
            )

    def save_config(self):
        if self._config:
            try:
                with open(self.config_path, 'w', encoding='utf-8') as f:
                    json.dump(self._config, f, ensure_ascii=False, indent=2)
                return True
            except PermissionError as e:
                handle_exception(e, 'ConfigManager保存配置权限')
                raise AppException.permission_error(
                    f"保存配置文件失败（权限不足）: {e}",
                    path=self.config_path,
                    operation='write'
                )
            except Exception as e:
                handle_exception(e, 'ConfigManager保存配置')
                raise AppException.config_error(
                    f"保存配置文件失败: {e}",
                    config_key=self.config_path
                )
        return False

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        if self._config is not None:
            self._config[key] = value
            self.save_config()

    def get_cookie_file(self):
        return self.config.get('cookie_file', PathManager.get_cookie_file())

    def get_output_file(self):
        return self.config.get('output_file', PathManager.get_output_file())

    def get_excel_file(self):
        excel_files = self.config.get('excel_files', [])
        if excel_files:
            for path in excel_files:
                expanded_path = os.path.expanduser(path)
                if FileManager.file_exists(expanded_path):
                    return expanded_path
        return self.config.get('excel_file', '')

    def get_all_excel_files(self):
        excel_files = self.config.get('excel_files', [])
        existing_files = []
        if excel_files:
            for path in excel_files:
                expanded_path = os.path.expanduser(path)
                if FileManager.file_exists(expanded_path):
                    existing_files.append(expanded_path)
        return existing_files

    def get_target_url(self):
        return self.config.get('target_url', '')

    def get_user_agent(self):
        return self.config.get('user_agent', WegoScraper.get_user_agent())


class CookieValidator:
    """Cookie验证器 - 提供完整的cookie验证和友好提示"""
    
    @staticmethod
    def validate_and_prompt(cookie_file):
        """验证cookie并给出友好提示，返回: (is_valid, cookies_or_None)"""
        print_separator()
        print('🔍 验证Cookie状态...')
        print_separator()
        
        # 1. 检查文件是否存在
        if not os.path.exists(cookie_file):
            CookieValidator._show_prompt('Cookie文件不存在', cookie_file, 
                reasons=['首次使用程序，尚未获取Cookie', 'Cookie文件被误删除', '配置文件路径错误'],
                solutions=['返回主菜单选择"4. 更新Cookie"', '浏览器将自动打开并跳转到登录页面', '手动登录账号后关闭浏览器', 'Cookie将自动保存并可以正常使用'],
                tip='Cookie有效期为30天，建议定期更新')
            return False, None
        
        # 2. 检查文件是否可读
        try:
            with open(cookie_file, 'r', encoding='utf-8') as f:
                cookies = json.load(f)
        except json.JSONDecodeError:
            CookieValidator._show_prompt('Cookie文件格式错误', cookie_file,
                reasons=['文件被意外修改', '文件保存时出错', '文件传输过程中损坏'],
                solutions=['删除当前的Cookie文件', '运行"4. 更新Cookie"功能', '重新获取有效的Cookie'],
                tip='建议定期备份Cookie文件')
            return False, None
        except Exception as e:
            CookieValidator._show_prompt('Cookie文件读取失败', cookie_file,
                extra_info=f'❌ 错误信息: {str(e)}',
                reasons=['文件权限不足', '文件被其他程序占用', '磁盘空间不足'],
                solutions=['检查文件权限设置', '关闭可能占用文件的其他程序', '检查磁盘空间', '如果问题持续，请重新运行"更新Cookie"功能'])
            return False, None
        
        # 3. 检查cookie是否为空
        if not cookies:
            CookieValidator._show_prompt('Cookie为空', cookie_file,
                reasons=['Cookie文件被清空', '获取Cookie时出错', 'Cookie保存失败'],
                solutions=['运行"4. 更新Cookie"功能', '重新登录账号', '确认Cookie已正确保存'])
            return False, None
        
        print(f'✓ Cookie文件存在，共 {len(cookies)} 个Cookie')
        
        # 4. 检查是否存在token
        token_cookie = next((c for c in cookies if 'token' in c.get('name', '').lower()), None)
        if not token_cookie:
            CookieValidator._show_prompt('未找到Token Cookie', cookie_file,
                reasons=['未登录或登录已失效', 'Token Cookie被清除', 'Cookie保存不完整'],
                solutions=['运行"4. 更新Cookie"功能', '确保使用正确的账号登录', '登录成功后再关闭浏览器'],
                tip='Token是保持登录状态的关键Cookie')
            return False, None
        
        print(f'✓ 找到Token: {token_cookie["name"]}')
        
        # 5. 检查token是否过期
        expires = token_cookie.get('expires')
        if expires and expires < time.time():
            expired_time = datetime.fromtimestamp(expires).strftime('%Y-%m-%d %H:%M:%S')
            current_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            days_expired = int((time.time() - expires) / 86400)
            CookieValidator._show_prompt('Token已过期', '',
                extra_info=f'📅 过期时间: {expired_time}\n📅 当前时间: {current_time_str}\n⏱️  已过期: {days_expired}天',
                reasons=['无法获取商品数据', '登录状态失效', '需要重新登录'],
                solutions=['选择"4. 更新Cookie"功能', '使用您的账号重新登录', '更新完成后即可继续使用'],
                tip='建议在Cookie过期前一周进行更新',
                impact=True)
            return False, None
        
        expires_time = datetime.fromtimestamp(expires).strftime('%Y-%m-%d %H:%M:%S') if expires else '未知'
        print(f'✓ Token有效期至: {expires_time}')
        
        # 6. 检查token值是否有效
        token_value = token_cookie.get('value', '')
        if not token_value or len(token_value) < 10:
            CookieValidator._show_prompt('Token值无效', cookie_file,
                reasons=['Token值为空', 'Token值过短或格式错误', 'Token被意外修改'],
                solutions=['运行"4. 更新Cookie"功能', '重新登录账号', '确认Token已正确保存'],
                tip='正常的Token应该是一长串加密字符串')
            return False, None
        
        print(f'✓ Token值有效 (长度: {len(token_value)} 字符)')
        
        # 7. 检查cookie是否即将过期（7天内）
        if expires:
            days_until_expiry = int((expires - time.time()) / 86400)
            if days_until_expiry <= 7:
                CookieValidator._show_expiry_warning(days_until_expiry)
        
        print_separator()
        print('✅ Cookie验证通过！')
        print_separator()
        
        return True, cookies
    
    @staticmethod
    def _show_prompt(title, file_path, extra_info=None, reasons=None, solutions=None, tip=None, impact=False):
        """显示统一的友好提示"""
        print('\n' + '─'*60)
        print(f'⚠️  检测到{title}')
        print('─'*60)
        if file_path:
            print(f'📂 文件位置: {file_path}')
        if extra_info:
            print(extra_info)
        print()
        if reasons:
            print('📝 可能原因:' if not impact else '📝 影响范围:')
            for reason in reasons:
                print(f'   • {reason}')
            print()
        if solutions:
            print('✅ 解决方案:')
            for i, solution in enumerate(solutions, 1):
                print(f'   {i}. {solution}')
            print()
        if tip:
            print(f'💡 提示: {tip}')
        print('─'*60)
    
    @staticmethod
    def _show_expiry_warning(days_until_expiry):
        """显示即将过期的警告"""
        print('\n' + '─'*60)
        print('⏰  Cookie即将过期提醒')
        print('─'*60)
        print(f'⏱️  剩余有效期: {days_until_expiry}天')
        print()
        if days_until_expiry <= 3:
            print('🔴 状态: 即将过期（3天内）')
            print('⚠️  建议: 立即更新Cookie')
        else:
            print('🟡 状态: 即将过期（7天内）')
            print('💡 建议: 近期更新Cookie')
        print()
        print('✅ 操作: 返回主菜单选择"4. 更新Cookie"')
        print('─'*60)


class FileManager:
    @staticmethod
    def read_json(file_path):
        with ExceptionContext(f"FileManager.read_json({file_path})", default=None) as ctx:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)

    @staticmethod
    def write_json(file_path, data, indent=2):
        with ExceptionContext(f"FileManager.write_json({file_path})", default=False) as ctx:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
            return True

    @staticmethod
    def read_text(file_path):
        with ExceptionContext(f"FileManager.read_text({file_path})", default=None) as ctx:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()

    @staticmethod
    def write_text(file_path, content):
        with ExceptionContext(f"FileManager.write_text({file_path})", default=False) as ctx:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

    @staticmethod
    def file_exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def get_latest_json_file(directory=None, pattern='微购相册'):
        with ExceptionContext(f"FileManager.get_latest_json_file", default=None) as ctx:
            directory = directory or PathManager.get_file_dir()
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

    @staticmethod
    def get_today_json_files(directory=None, pattern='微购相册'):
        """
        获取用于对比的两个JSON文件
        优先级：
        1. 当天的缓存文件和最新文件
        2. 当天的最新文件和前一天的文件
        3. 最新的两个文件
        """
        with ExceptionContext("FileManager.get_today_json_files", default=(None, None)) as ctx:
            directory = directory or PathManager.get_file_dir()
            if not os.path.exists(directory):
                print(f'目录 {directory} 不存在')
                return None, None
            
            today = datetime.now().strftime('%Y%m%d')
            
            all_json_files = []
            for file in os.listdir(directory):
                if file.endswith('.json') and pattern in file and '_cache' not in file:
                    file_path = os.path.join(directory, file)
                    all_json_files.append((file_path, os.path.getmtime(file_path)))
            
            if len(all_json_files) < 1:
                print(f'未找到包含"{pattern}"的JSON文件')
                return None, None
            
            all_json_files.sort(key=lambda x: x[1], reverse=True)
            latest_file = all_json_files[0][0]
            
            cache_file = PathManager.get_cache_file_path(today)
            if os.path.exists(cache_file):
                print(f'找到当天缓存文件: {cache_file}')
                print(f'找到当天最新文件: {latest_file}')
                return latest_file, cache_file
            
            today_files = []
            for file in os.listdir(directory):
                if file.endswith('.json') and pattern in file and today in file and '_cache' not in file:
                    file_path = os.path.join(directory, file)
                    today_files.append((file_path, os.path.getmtime(file_path)))
            
            if len(today_files) >= 2:
                today_files.sort(key=lambda x: x[1], reverse=True)
                print(f'找到当天最新文件: {today_files[0][0]}')
                print(f'找到当天次新文件: {today_files[1][0]}')
                return today_files[0][0], today_files[1][0]
            
            if len(all_json_files) >= 2:
                print(f'当天只有一个文件，使用最新文件和次新文件对比')
                print(f'最新文件: {latest_file}')
                print(f'次新文件: {all_json_files[1][0]}')
                return latest_file, all_json_files[1][0]
            
            print(f'只找到一个文件: {latest_file}')
            return latest_file, None

    @staticmethod
    def list_files(directory=None, pattern=None):
        with ExceptionContext("FileManager.list_files", default=[]) as ctx:
            directory = directory or PathManager.get_file_dir()
            if not os.path.exists(directory):
                return []
            
            files = os.listdir(directory)
            if pattern:
                files = [f for f in files if pattern in f]
            return files

    @staticmethod
    def safe_read_excel(excel_file, max_retries=3, retry_delay=0.5):
        """
        安全读取Excel文件，处理Windows共享违规问题
        通过复制到临时文件再读取，确保原文件不被锁定
        
        Args:
            excel_file: Excel文件路径
            max_retries: 最大重试次数
            retry_delay: 重试间隔（秒）
            
        Returns:
            dict: {sheet_name: DataFrame} 或 None
        """
        if pd is None:
            return None
        
        temp_file = None
        with ExceptionContext(f"FileManager.safe_read_excel({excel_file})", default=None) as ctx:
            for attempt in range(max_retries):
                try:
                    temp_dir = os.path.join(PROJECT_DIR, 'temp')
                    os.makedirs(temp_dir, exist_ok=True)
                    temp_file = os.path.join(temp_dir, f'_temp_excel_{uuid.uuid4().hex}.xlsx')
                    shutil.copy2(excel_file, temp_file)
                    
                    with file_write_lock:
                        xls = pd.ExcelFile(temp_file, engine='openpyxl')
                        dfs = {}
                        for sheet in xls.sheet_names:
                            dfs[sheet] = xls.parse(sheet)
                        xls.close()
                    return dfs
                except PermissionError as e:
                    if "sharing violation" in str(e).lower() or "另一个程序" in str(e) or "正在使用" in str(e) or "Permission" in str(e):
                        if attempt < max_retries - 1:
                            print(f'Excel文件被占用，正在等待重试 ({attempt + 1}/{max_retries}): {excel_file}')
                            time.sleep(retry_delay)
                        else:
                            raise AppException.excel_error(f'Excel文件读取失败（共享违规）', excel_file=excel_file)
                    else:
                        raise
                except Exception as e:
                    raise AppException.parse_error(f'读取Excel文件失败', data_type='excel', raw_data=str(e))
        
        if temp_file and os.path.exists(temp_file):
            safe_execute_func(
                lambda: os.remove(temp_file),
                context='清理临时Excel文件'
            )
        
        return None


class WegoScraper:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = PathManager.get_config_file()
        self.config_manager = ConfigManager(config_path)

    @staticmethod
    def get_system_info():
        return Environment.get_system_info()
    
    @staticmethod
    def get_chrome_path():
        return Environment.get_chrome_path()
    
    @staticmethod
    def get_browser_args():
        return Environment.get_browser_args()
    
    @staticmethod
    def get_user_agent():
        return Environment.get_user_agent()

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
        
        for selector in popup_selectors[:close_limit]:
            safe_execute_func(
                lambda: self._close_popup_impl(page, selector, wait_time),
                context=f'close_popups({selector})'
            )
    
    async def _close_popup_impl(self, page, selector, wait_time):
        close_button = await page.query_selector(selector, timeout=1000)
        if close_button:
            await close_button.click(timeout=1000)
            print(f'关闭了弹窗: {selector}')
            await asyncio.sleep(wait_time)

    async def scroll_to_load_all(self, page):
        print('开始滚动加载所有商品...')
        
        config = self.config_manager.get('scroll_config', {})
        max_attempts = config.get('max_attempts', 30)
        same_height_limit = config.get('same_height_limit', 8)
        scroll_wait_time = config.get('scroll_wait_time', 0.8)
        popup_close_interval = config.get('popup_close_interval', 5)
        popup_close_limit = config.get('popup_close_limit', 3)
        popup_close_wait = config.get('popup_close_wait', 0.3)
        
        print(f'滚动配置: 最大尝试{max_attempts}次, 高度不变限制{same_height_limit}次, 初始等待时间{scroll_wait_time}秒')
        
        last_height = 0
        no_change_count = 0
        height_history = []
        dynamic_adjust = config.get('dynamic_adjust', True)
        
        for scroll_attempts in range(max_attempts):
            with ExceptionContext(f"scroll_to_load_all第{scroll_attempts + 1}次滚动", default=None) as ctx:
                start_time = time.time()
                
                current_height = await asyncio.wait_for(
                    page.evaluate('document.body.scrollHeight'),
                    timeout=5.0
                ) if scroll_attempts > 0 else 0
                
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
                
                scroll_distance = current_height * 0.3 if scroll_attempts < 10 else current_height
                safe_execute_func(
                    lambda: asyncio.wait_for(
                        page.evaluate(f'window.scrollBy(0, {scroll_distance})' if scroll_attempts < 10 else 'window.scrollTo(0, document.body.scrollHeight)'),
                        timeout=3.0
                    ),
                    context='scroll操作'
                )
                
                await asyncio.sleep(scroll_wait_time)
                
                progress_percent = min(100, int((scroll_attempts + 1) / max_attempts * 100))
                print(f'滚动 {scroll_attempts + 1}/{max_attempts} ({progress_percent}%) - 当前高度: {current_height} - 加载耗时: {load_time:.2f}秒')
                
                if dynamic_adjust and len(height_history) >= 5:
                    height_changes = [abs(height_history[i] - height_history[i-1]) for i in range(1, len(height_history))]
                    avg_change = sum(height_changes) / len(height_changes)
                    
                    if avg_change < 50 and scroll_wait_time < 2.0:
                        scroll_wait_time = min(2.0, scroll_wait_time + 0.1)
                        print(f'  ⚠️  页面加载较慢，增加等待时间至 {scroll_wait_time:.1f}秒')
                    elif avg_change > 300 and scroll_wait_time > 0.5:
                        scroll_wait_time = max(0.5, scroll_wait_time - 0.1)
                        print(f'  ✅ 页面加载较快，减少等待时间至 {scroll_wait_time:.1f}秒')
                
                if (scroll_attempts + 1) % popup_close_interval == 0:
                    await self.close_popups(page, popup_close_limit, popup_close_wait)
                
                if ctx.error:
                    break
        
        print('滚动完成')

    @staticmethod
    def extract_product_info(element_text, html_content):
        try:
            stock_match = re.search(r'货号[：:]\s*(\d+)', element_text)
            stock_number = stock_match.group(1) if stock_match else ''
            
            def extract_price(text):
                price_match = re.search(r'售价[：:]\s*¥?\s*([\d,]+)', text)
                if not price_match:
                    price_match = re.search(r'¥\s*([\d,]+)(?![0-9])', text)
                if price_match:
                    price_value = int(price_match.group(1).replace(',', ''))
                    if 100 <= price_value <= 50000:
                        return '¥' + price_match.group(1)
                return None
            
            price = extract_price(element_text)
            
            def extract_cost_price(text, html):
                # 只匹配真正包含"拿货价"关键字的数据
                # 移除价格范围限制，接受任何合理的拿货价
                
                # 模式1: 拿货价：¥1234 或 拿货价:1234
                cost_match = re.search(r'拿货价[：:]\s*¥?\s*([\d,]+)', text)
                if cost_match:
                    cost_value = int(cost_match.group(1).replace(',', ''))
                    if cost_value > 50:  # 拿货价至少要大于50元
                        return '¥' + cost_match.group(1)
                
                # 模式2: 带空格的情况 拿货价 ：1234
                cost_match2 = re.search(r'拿货价\s*[：:]\s*([\d,]+)', text)
                if cost_match2:
                    cost_value = int(cost_match2.group(1).replace(',', ''))
                    if cost_value > 50:
                        return '¥' + cost_match2.group(1)
                
                # 模式3: HTML内容中的拿货价
                if html:
                    html_cost_match = re.search(r'拿货价[：:]\s*¥?\s*([\d,]+)', html)
                    if html_cost_match:
                        cost_value = int(html_cost_match.group(1).replace(',', ''))
                        if cost_value > 50:
                            return '¥' + html_cost_match.group(1)
                    
                    # 模式4: HTML中带空格的情况
                    html_cost_match2 = re.search(r'拿货价\s*[：:]\s*([\d,]+)', html)
                    if html_cost_match2:
                        cost_value = int(html_cost_match2.group(1).replace(',', ''))
                        if cost_value > 50:
                            return '¥' + html_cost_match2.group(1)
                
                return None
            
            cost_price = extract_cost_price(element_text, html_content)
            
            employee_match = re.search(r'员工[：:]\s*(.+)', element_text)
            employee = employee_match.group(1).strip() if employee_match else None
            
            def extract_remark(text, emp_match):
                if emp_match:
                    emp_pos = text.find('员工')
                    price_match = re.search(r'售价[：:]', text)
                    if price_match:
                        price_pos = price_match.start()
                        between_text = text[price_pos:emp_pos]
                        if between_text and len(between_text.strip()) > 0:
                            between_text = between_text.replace('售价：', '').replace('售价:', '')
                            between_text = re.sub(r'¥\s*[\d,]+', '', between_text)
                            between_text = re.sub(r'\s+', ' ', between_text).strip()
                            if between_text and len(between_text) > 0:
                                return between_text
                
                remark_match = re.search(r'备注[：:]\s*(.+?)(?:\s*员工[：:]|$)', text, re.DOTALL)
                if remark_match:
                    return re.sub(r'\s+', ' ', remark_match.group(1).strip())
                return None
            
            remark = extract_remark(element_text, employee_match)
            
            cut_pos = min(
                len(element_text),
                *(pos for pos in [element_text.find('¥'), element_text.find('删除'), element_text.find('货号')] if pos > 0)
            )
            
            name_part = element_text[:cut_pos] if cut_pos < len(element_text) and cut_pos > 10 else element_text
            name = WegoScraper.clean_product_name(re.sub(r'\s+', ' ', name_part.strip()))
            
            if name:
                return {
                    '商品名称': name,
                    '售价': price if price else '',
                    '拿货价': cost_price if cost_price else '',
                    '货号': stock_number,
                    '备注': remark if remark else '',
                    '员工': employee if employee else '',
                    '图片': ''
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
                element_text = await asyncio.wait_for(element.text_content(), timeout=2.0)
                html_content = await asyncio.wait_for(element.inner_html(), timeout=2.0)
                
                # 尝试获取商品ID - 尝试多种属性
                element_id = None
                try:
                    element_id = await element.get_attribute('data-id')
                except:
                    pass
                if not element_id:
                    try:
                        href = await element.get_attribute('href')
                        if href:
                            href_match = re.search(r'/(\d+)(?:\?|$)', href)
                            if href_match:
                                element_id = href_match.group(1)
                    except:
                        pass
                if not element_id:
                    try:
                        element_id = await element.get_attribute('data-goods-id')
                    except:
                        pass

                if not element_text or not element_text.strip():
                    continue
                if '试试批量' in element_text or '暂无搭配' in element_text:
                    continue
                if re.match(r'^\d{2}月 \d{4}$', element_text.strip()):
                    continue
                if len(element_text.strip()) < 30:
                    continue

                elements_data.append((element_text, html_content, element_id))
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                print(f'收集元素 {i} 数据时出错: {e}')

        print(f'收集了 {len(elements_data)} 个有效商品数据')

        # 第一轮：提取商品基本信息
        products = []
        seen_products = set()
        products_need_api = []  # 需要通过API获取拿货价的商品

        with ThreadPoolExecutor(max_workers=15) as executor:
            futures = [executor.submit(self.extract_product_info, text, html) for text, html, _ in elements_data]

            for i, future in enumerate(futures):
                try:
                    result = future.result(timeout=2)
                    if result:
                        product_key = result['货号'] or result['商品名称']
                        if product_key not in seen_products:
                            seen_products.add(product_key)
                            
                            # 如果没有拿货价，记录下来后面用API获取
                            if not result.get('拿货价'):
                                products_need_api.append((result, elements_data[i][2]))  # result和element_id
                            else:
                                products.append(result)
                            
                            if len(products) + len(products_need_api) <= 10:
                                print(f'商品 {len(products) + len(products_need_api)}: {result["商品名称"][:50]}...')
                                print(f'  售价: {result["售价"]}')
                                print(f'  拿货价: {result["拿货价"]}')
                                print(f'  货号: {result["货号"]}')
                                print(f'  data-id: {elements_data[i][2]}\n')
                except Exception:
                    pass
        
        # 第二轮：通过API获取缺失拿货价的商品
        if products_need_api:
            print(f'\n通过API获取缺失的拿货价，需要处理 {len(products_need_api)} 个商品...')
            await self.fetch_cost_prices_via_api(page, products_need_api, products)
        
        return products
    
    async def fetch_cost_prices_via_api(self, page, products_need_api, products):
        """通过API获取缺失拿货价的商品详情"""
        print(f'开始通过API获取 {len(products_need_api)} 个商品的拿货价...')
        
        cookie_file = os.path.join(os.path.dirname(__file__), 'config', 'cookies.json')
        cookies = []
        if os.path.exists(cookie_file):
            try:
                with open(cookie_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                print(f'读取到 {len(cookies)} 个cookie')
            except Exception as e:
                handle_exception(e, 'fetch_cost_prices_via_api读取Cookie')
                return
        
        cookie_str = '; '.join([f'{c["name"]}={c["value"]}' for c in cookies])
        
        current_url = page.url        # 尝试从URL中提取albumId（可能在query参数或hash中）
        album_id_match = re.search(r'albumId=([^&/]+)|/shop_detail/([^/?#]+)', current_url)
        if album_id_match:
            album_id = album_id_match.group(1) or album_id_match.group(2)
        else:
            album_id = '_du7mJco53PgiClrX_onUY7Hs5F3Mez8q5_nMrFQ'
        print(f'Album ID: {album_id}')
        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            'x-wg-language': 'zh'
        }
        
        # 使用正确的API获取商品列表
        api_url = 'https://www.szwego.com/album/personal/all'
        
        all_goods_data = []
        
        # 获取所有商品（处理分页）
        page_timestamp = ''
        for page_num in range(20):
            params = {
                'albumId': album_id,
                'searchValue': '',
                'searchImg': '',
                'startDate': '',
                'endDate': '',
                'sourceId': ''
            }
            # 只有第一页不需要timestamp，后续需要
            if page_timestamp:
                params['timestamp'] = page_timestamp
            
            try:
                # 使用带cookies的请求
                # 在headers中添加Cookie
                headers_with_cookie = dict(headers)
                headers_with_cookie['Cookie'] = cookie_str
                response = await page.request.get(api_url, params=params, headers=headers_with_cookie)
                if response.status == 200:
                    text = await response.text()
                    try:
                        data = json.loads(text)
                        result = data.get('result', {})
                        items = result.get('items', [])
                        pagination = result.get('pagination', {})
                        
                        if items:
                            all_goods_data.extend(items)
                            print(f'  第{page_num+1}页: 获取 {len(items)} 个商品')
                            
                            # 调试：打印第一个商品的title和goodsNum
                            if page_num == 0 and items:
                                print(f'    调试: 第一个商品 title={items[0].get("title", "")[:30]}... goodsNum={items[0].get("goodsNum", "")}')
                            
                            # 检查是否还有更多 - 使用 isLoadMore 判断
                            is_load_more = pagination.get('isLoadMore', False)
                            page_timestamp = str(pagination.get('pageTimestamp', ''))
                            
                            if is_load_more and page_timestamp:
                                params['timestamp'] = page_timestamp
                            else:
                                break
                        else:
                            break
                    except Exception as e:
                        handle_exception(e, 'fetch_cost_prices_via_api解析响应')
                        break
                else:
                    print(f'  请求失败: {response.status}')
                    break
            except Exception as e:
                handle_exception(e, 'fetch_cost_prices_via_api请求')
                break
        
        print(f'共获取 {len(all_goods_data)} 个商品数据')
        
        # 调试：打印API获取到的goodsNum列表
        api_goods_nums = [item.get('goodsNum', '') for item in all_goods_data if item.get('goodsNum')]
        print(f'  调试: API goodsNums: {api_goods_nums[:10]}')
        
        # 调试：打印products_need_api中的货号和名称
        print(f'  调试: 需要API的商品数: {len(products_need_api)}')
        if products_need_api:
            sample = products_need_api[0][0]
            print(f'  调试: 第一个商品的货号={sample.get("货号", "")}, 名称={sample.get("商品名称", "")[:30]}...')
        
        # 构建商品映射
        goods_by_num = {}
        goods_by_title = {}
        for item in all_goods_data:
            goods_num = item.get('goodsNum', '')
            title = item.get('title', '')
            if goods_num:
                goods_by_num[goods_num] = item
            if title:
                goods_by_title[title] = item
        
        # 匹配并更新拿货价
        success_count = 0
        for product, element_id in products_need_api:
            goods_num = product.get('货号', '')
            title = product.get('商品名称', '')
            
            matched_item = None
            if goods_num and goods_num in goods_by_num:
                matched_item = goods_by_num[goods_num]
            elif title and title in goods_by_title:
                matched_item = goods_by_title[title]
            
            if matched_item:
                price_arr = matched_item.get('priceArr', [])
                cost_price = None
                for price_item in price_arr:
                    if price_item.get('priceType') == 1:
                        cost_price = price_item.get('value')
                        break
                
                if cost_price:
                    product['拿货价'] = f'¥{int(cost_price):,}'
                    success_count += 1
                    print(f'  ✓ 获取拿货价: {product["商品名称"][:30]}... -> {product["拿货价"]}')
                else:
                    print(f'  ⚠ 无拿货价: {product["商品名称"][:30]}...')
            else:
                print(f'  ⚠ 未匹配到: {product["商品名称"][:30]}...')
        
        print(f'API获取完成，成功获取 {success_count}/{len(products_need_api)} 个拿货价')

    async def get_data_with_playwright(self, page):
        try:
            target_url = self.config_manager.get_target_url()
            print(f'正在访问目标页面: {target_url}')
            print(f'当前系统: {self.get_system_info()}')
            
            # 页面导航重试机制
            max_retries = 3
            page_loaded = False
            
            for retry in range(max_retries):
                goto_start = time.time()
                try:
                    print(f'尝试加载页面 (第{retry + 1}/{max_retries}次)...')
                    await page.goto(target_url, timeout=30000, wait_until='domcontentloaded')
                    print('页面DOM已加载')
                    page_loaded = True
                    break
                except Exception as e:
                    print(f'页面导航出错: {e}')
                    if retry < max_retries - 1:
                        print(f'等待3秒后重试...')
                        await asyncio.sleep(3)
                    else:
                        print('所有重试都失败，尝试继续执行...')
                        await asyncio.sleep(2)
                print(f'页面导航耗时: {time.time() - goto_start:.2f}秒')
            
            if not page_loaded:
                print('警告: 页面可能未完全加载，继续执行...')
            
            await asyncio.sleep(2)
            
            # 直接通过API获取所有商品数据
            print('直接通过API获取所有商品数据...')
            products = await self.fetch_all_products_via_api(page)
            
            if products:
                print(f'通过API成功获取 {len(products)} 个商品')
                print(f'get_data_with_playwright 返回: {len(products)} 个商品')
                return products
            
            # 如果API失败，返回空列表
            print('API获取失败，返回空列表')
            return []
        except Exception as e:
            print(f'获取数据失败: {e}')
            traceback.print_exc()
            return []

    async def fetch_all_products_via_api(self, page):
        """通过API获取所有商品数据"""
        cookie_file = os.path.join(os.path.dirname(__file__), 'config', 'cookies.json')
        cookies = []
        if os.path.exists(cookie_file):
            try:
                with open(cookie_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                print(f'读取到 {len(cookies)} 个cookie')
            except Exception as e:
                print(f'读取cookie失败: {e}')
                return None
        
        current_url = page.url
        album_id_match = re.search(r'albumId=([^&/]+)|/shop_detail/([^/?#]+)', current_url)
        if album_id_match:
            album_id = album_id_match.group(1) or album_id_match.group(2)
        else:
            album_id = '_du7mJco53PgiClrX_onUY7Hs5F3Mez8q5_nMrFQ'
        print(f'Album ID: {album_id}')
        
        cookie_str = '; '.join([f'{c["name"]}={c["value"]}' for c in cookies])
        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            'x-wg-language': 'zh'
        }
        
        api_url = 'https://www.szwego.com/album/personal/all'
        
        all_goods_data = []
        page_timestamp = ''
        
        print('开始通过API获取所有商品...')
        for page_num in range(20):
            params = {
                'albumId': album_id,
                'searchValue': '',
                'searchImg': '',
                'startDate': '',
                'endDate': '',
                'sourceId': ''
            }
            if page_timestamp:
                params['timestamp'] = page_timestamp
            
            try:
                # 在headers中添加Cookie
                headers_with_cookie = dict(headers)
                headers_with_cookie['Cookie'] = cookie_str
                response = await page.request.get(api_url, params=params, headers=headers_with_cookie)
                
                if response.status == 200:
                    text = await response.text()
                    try:
                        data = json.loads(text)
                        result = data.get('result', {})
                        items = result.get('items', [])
                        pagination = result.get('pagination', {})
                        
                        if items:
                            all_goods_data.extend(items)
                            print(f'  第{page_num+1}页: 获取 {len(items)} 个商品')
                            
                            is_load_more = pagination.get('isLoadMore', False)
                            page_timestamp = str(pagination.get('pageTimestamp', ''))
                            
                            if is_load_more and page_timestamp:
                                params['timestamp'] = page_timestamp
                            else:
                                break
                        else:
                            break
                    except Exception as e:
                        print(f'  解析失败: {e}')
                        break
                else:
                    print(f'  请求失败: {response.status}')
                    break
            except Exception as e:
                print(f'  请求异常: {e}')
                break
        
        print(f'共获取 {len(all_goods_data)} 个商品数据')
        
        if not all_goods_data:
            return None
        
        products = []
        for item in all_goods_data:
            title = item.get('title', '')
            goods_num = item.get('goodsNum', '')
            
            price_arr = item.get('priceArr', [])
            sale_price = None
            cost_price = None
            for price_item in price_arr:
                if price_item.get('priceType') == 1:
                    cost_price = price_item.get('value')
                elif price_item.get('priceType') == 2:
                    sale_price = price_item.get('value')
            
            note_arr = item.get('noteArr', [])
            remark = note_arr[0].get('value', '') if note_arr else ''
            
            staff_info = item.get('staffInfo', {})
            staff_nick = staff_info.get('staffNick', '')
            
            media_b64_list = []
            imgs_src = item.get('imgsSrc', [])
            if imgs_src:
                for url in imgs_src:
                    media_b64_list.append(base64.b64encode(url.encode('utf-8')).decode('utf-8'))
            video_url = item.get('videoUrl', '')
            if video_url:
                media_b64_list.append(base64.b64encode(video_url.encode('utf-8')).decode('utf-8'))
            
            media_b64 = media_b64_list[0] if len(media_b64_list) == 1 else media_b64_list
            
            product = {
                '商品描述': title,
                '售价': f'¥{int(sale_price):,}' if sale_price else '',
                '拿货价': f'¥{int(cost_price):,}' if cost_price else '',
                '货号': goods_num,
                '备注': remark,
                '员工': staff_nick,
                '图片': media_b64
            }
            products.append(product)
        
        print(f'fetch_all_products_via_api 返回: {len(products)} 个商品')
        return products

    @staticmethod
    def parse_price(price_str):
        """解析价格字符串，返回整数价格或None"""
        if not price_str:
            return None        # 移除常见的价格符号
        price_clean = str(price_str).replace('¥', '').replace(',', '').replace('元', '').strip()
        # 使用正则提取数字部分
        match = re.search(r'(\d+)', price_clean)
        if match:
            return int(match.group(1))
        return None

    def filter_high_price_products(self, data, min_price=599):
        """筛选高价商品"""
        return [p for p in data if self.parse_price(p.get('售价', '')) and self.parse_price(p.get('售价', '')) >= min_price]

    def analyze_data_changes(self, data, previous_file):
        """分析数据变化"""
        if not previous_file:
            return ""
        
        try:
            old_data = FileManager.read_json(previous_file)
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
                handle_exception(e, 'analyze_data_changes对比分析')
                return f"对比分析失败: {str(e)}"

    def save_data(self, data, filename=None):
        today = datetime.now().strftime('%Y%m%d')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_filename = PathManager.get_json_file_path(today)
        cache_filename = PathManager.get_cache_file_path(today)
        
        # 如果当天的JSON文件已存在，先保存为缓存文件
        existing_summary = None
        if os.path.exists(new_filename):
            try:
                shutil.copy2(new_filename, cache_filename)
                print(f'已将旧数据保存为缓存文件: {cache_filename}')
                
                # 读取现有的"小计"字段
                existing_data = FileManager.read_json(new_filename)
                if existing_data and '小计' in existing_data:
                    existing_summary = existing_data['小计']
                    print(f'已保留 {len(existing_summary) if isinstance(existing_summary, list) else 1} 条对比记录')
            except Exception as e:
                print(f'创建缓存文件失败: {e}')
        
        total_count = len(data)
        high_price_products = self.filter_high_price_products(data)
        high_price_count = len(high_price_products)
        
        # 计算累计值
        total_sell_price = 0.0
        total_platform_fee = 0.0
        total_cost_price = 0.0  # 累计成本
        
        for product in data:
            sell_price = 0.0
            cost_price = 0.0
            
            if '售价' in product:
                try:
                    sell_price = float(str(product['售价']).replace('¥', '').replace(',', '').strip())
                    total_sell_price += sell_price
                except (ValueError, TypeError):
                    pass
            
            if '拿货价' in product:
                try:
                    cost_price_str = str(product['拿货价']).replace('¥', '').replace(',', '').strip()
                    if cost_price_str:  # 确保不是空字符串
                        cost_price = float(cost_price_str)
                        total_cost_price += cost_price
                except (ValueError, TypeError):
                    pass
            
            # 计算闲鱼平台手续费（售价 * 1.6%）
            if sell_price > 0:
                platform_fee = sell_price * 0.016
                total_platform_fee += platform_fee
        
        # 计算平均每个设备售出均价
        avg_sell_price = total_sell_price / total_count if total_count > 0 else 0.0
        
        # 计算预计毛利
        estimated_gross_profit = total_sell_price - total_cost_price
        
        # 计算毛利率
        gross_profit_margin = estimated_gross_profit / total_cost_price if total_cost_price > 0 else 0.0
        
        # 计算所有设备卖到闲鱼平台的毛利
        idle_fish_gross_profit = total_sell_price - total_platform_fee
        
        # 计算单个设备的平均回收价格（累计成本 / 商品数量）
        avg_cost_price = total_cost_price / total_count if total_count > 0 else 0.0
        
        existing_files = sorted(FileManager.list_files(PathManager.get_file_dir(), '微购相册'), reverse=True)
        
        previous_file = None
        for f in existing_files:
            if f != PathManager.get_json_filename(today):
                previous_file = os.path.join(PathManager.get_file_dir(), f)
                break
        
        change_summary = self.analyze_data_changes(data, previous_file)
        
        output_data = {
            "生成日期": today,
            "时间戳": current_time,
            "成功获取": f"{total_count} 个商品",
            "商品列表": data,
            "单个设备的平均回收价格": f"{avg_cost_price:,.2f}",
            "平均每个设备售出均价": f"{avg_sell_price:,.2f}",
            "累计成本": f"{total_cost_price:,.2f}",
            "预计毛利": f"{estimated_gross_profit:,.2f}",
            "毛利率": f"{gross_profit_margin:.2%}",
            "预计售出价格累计": f"{total_sell_price:,.2f}",
            "闲鱼平台手续费累计": f"{total_platform_fee:,.2f}",
            "所有设备卖到闲鱼平台的毛利": f"{idle_fish_gross_profit:,.2f}",
            "统计": f"共计获取到 {total_count} 个商品"
        }
        
        # 保留现有的"小计"字段（如果有）
        if existing_summary:
            output_data["小计"] = existing_summary
        
        # "小计"字段将由compare_json_files方法管理，用于存储多次对比的差异记录
        
        output_data["高价商品统计"] = {
            "筛选条件": "售价 >= 599",
            "数量": high_price_count,
            "商品列表": high_price_products
        }
        
        FileManager.write_json(new_filename, output_data)
        print(f'数据已保存到 {new_filename}')
        print(f'成功获取 {total_count} 个商品')
        print(f'售价 >= 599 的商品: {high_price_count} 个')
        print(f'预计售出价格累计: ¥{total_sell_price:,.2f}')
        print(f'平均每个设备售出均价: ¥{avg_sell_price:,.2f}')
        print(f'闲鱼平台手续费累计: ¥{total_platform_fee:,.2f}')
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
            
            browser_start = time.time()
            async with async_playwright() as p:
                print('正在启动浏览器...')
                
                system = self.get_system_info()
                browser_args = self.get_browser_args()
                chrome_path = self.get_chrome_path()
                
                print(f'检测到系统: {system}')
                if chrome_path:
                    print(f'使用系统Chrome: {chrome_path}')
                else:
                    print(f'使用Playwright内置Chromium')
                
                browser = await p.chromium.launch(headless=False, args=browser_args, executable_path=chrome_path)
                print(f'浏览器启动耗时: {time.time() - browser_start:.2f}秒')
                
                context_start = time.time()
                context = await browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent=self.get_user_agent()
                )
                print(f'上下文创建耗时: {time.time() - context_start:.2f}秒')
                
                cookie_start = time.time()
                cookie_file = self.config_manager.get_cookie_file()
                if FileManager.file_exists(cookie_file):
                    cookies = FileManager.read_json(cookie_file)
                    if cookies:
                        print(f'已加载 {len(cookies)} 个Cookie')
                        await context.add_cookies(cookies)
                print(f'Cookie加载耗时: {time.time() - cookie_start:.2f}秒')
                
                page_start = time.time()
                page = await context.new_page()
                print(f'页面创建耗时: {time.time() - page_start:.2f}秒')
                
                data_start = time.time()
                products = await self.get_data_with_playwright(page)
                print(f'数据获取耗时: {time.time() - data_start:.2f}秒')
                
                if products:
                    save_start = time.time()
                    self.save_data(products)
                    print(f'数据保存耗时: {time.time() - save_start:.2f}秒')
                    
                    compare_start = time.time()
                    print('\n开始自动对比当天JSON文件...')
                    comparator = StockNumberComparator()
                    comparator.compare_json_files()
                    print(f'对比耗时: {time.time() - compare_start:.2f}秒')
                
                save_cookie_start = time.time()
                cookies = await context.cookies()
                # 统一domain格式，将所有cookie的domain改为.szwego.com
                szwego_cookies = [cookie for cookie in cookies if 'szwego.com' in cookie['domain']]
                for cookie in szwego_cookies:
                    if cookie['domain'] == 'www.szwego.com':
                        cookie['domain'] = '.szwego.com'
                FileManager.write_json(cookie_file, szwego_cookies)
                print(f'Cookie已保存到 {cookie_file}')
                print(f'Cookie保存耗时: {time.time() - save_cookie_start:.2f}秒')
                
                close_start = time.time()
                await browser.close()
                print(f'浏览器关闭耗时: {time.time() - close_start:.2f}秒')
                
        except Exception as e:
            print(f'运行失败: {e}')
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
    def __init__(self, output_file=None, input_file=None, config_path=None):
        self.output_file = output_file or PathManager.get_output_file()
        self.input_file = input_file or PathManager.get_input_file()
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

    def load_excel_data(self, excel_file=None, remove_duplicates=True):
        if excel_file is None:
            excel_file = self.excel_file
        
        if not excel_file:
            return None
        
        temp_file = None
        try:
            if not FileManager.file_exists(excel_file):
                return None
            
            temp_dir = os.path.join(PROJECT_DIR, 'temp')
            os.makedirs(temp_dir, exist_ok=True)
            temp_file = os.path.join(temp_dir, f'_temp_excel_{uuid.uuid4().hex}.xlsx')
            shutil.copy2(excel_file, temp_file)
            
            print(f'正在读取Excel文件: {excel_file}')
            workbook = openpyxl.load_workbook(temp_file, read_only=True, data_only=True)
            
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
                    number_match = re.match(r'^([A-Za-z0-9]{3,10})$', cell_str)
                    if number_match:
                        stock_numbers.append(cell_str)
            
            stock_numbers = list(set(stock_numbers)) if remove_duplicates else stock_numbers
            print(f'从Excel文件的E列中读取到 {len(stock_numbers)} 个货号')
            workbook.close()
            return stock_numbers
        except Exception as e:
                handle_exception(e, 'load_excel_data读取Excel')
                return None
        finally:
            if temp_file and os.path.exists(temp_file):
                safe_execute_func(lambda: os.remove(temp_file), context='load_excel_data清理临时文件')

    def load_all_excel_data(self, remove_duplicates=True):
        all_stock_numbers = []
        excel_files = self.config_manager.get_all_excel_files()
        
        if not excel_files:
            print('未找到任何Excel文件')
            return None
        
        excel_files = list(dict.fromkeys(os.path.abspath(f) for f in excel_files))
        
        print(f'找到 {len(excel_files)} 个Excel文件')
        
        for excel_file in excel_files:
            temp_file = None
            try:
                if not FileManager.file_exists(excel_file):
                    continue
                
                temp_dir = os.path.join(PROJECT_DIR, 'temp')
                os.makedirs(temp_dir, exist_ok=True)
                temp_file = os.path.join(temp_dir, f'_temp_excel_{uuid.uuid4().hex}.xlsx')
                shutil.copy2(excel_file, temp_file)
                
                print(f'正在读取Excel文件: {excel_file}')
                workbook = openpyxl.load_workbook(temp_file, read_only=True, data_only=True)
                
                sheet = next((workbook[sheet_name] for sheet_name in workbook.sheetnames if '闲鱼' in sheet_name), None)
                
                if sheet is None:
                    print('未找到"闲鱼"工作表，使用第一个工作表')
                    sheet = workbook.active
                else:
                    print(f'使用工作表: {sheet.title}')
                
                file_stock_numbers = []
                for row in sheet.iter_rows(min_col=5, max_col=5, values_only=True):
                    cell_value = row[0]
                    if cell_value:
                        cell_str = str(cell_value).strip()
                        number_match = re.match(r'^([A-Za-z0-9]{3,10})$', cell_str)
                        if number_match:
                            file_stock_numbers.append(cell_str)
                
                print(f'从 {os.path.basename(excel_file)} 的E列中读取到 {len(file_stock_numbers)} 个货号')
                all_stock_numbers.extend(file_stock_numbers)
                workbook.close()
                
            except Exception as e:
                handle_exception(e, f'load_all_excel_data读取Excel {excel_file}')
                continue
            finally:
                if temp_file and os.path.exists(temp_file):
                    safe_execute_func(lambda: os.remove(temp_file), context='load_all_excel_data清理临时文件')
        
        if remove_duplicates:
            all_stock_numbers = list(set(all_stock_numbers))
        
        print(f'总共读取到 {len(all_stock_numbers)} 个货号（已去重）')
        return all_stock_numbers

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

    def save_duplicate_log(self, duplicates, log_file=None):
        try:
            log_file = log_file or PathManager.get_duplicate_log_file()
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
                handle_exception(e, 'save_duplicate_log保存重复日志')
                return False

    def compare_json_files(self):
        """
        对比当天最新的两个JSON文件，将差异写进最新的JSON文件中
        如果使用缓存文件，对比完成后会删除缓存文件
        """
        try:
            print_separator()
            print('当天JSON文件对比工具')
            print_separator()
            
            # 获取用于对比的两个JSON文件
            latest_json_file, second_latest_json_file = FileManager.get_today_json_files()
            if not latest_json_file:
                print('无法获取最新的JSON文件')
                return False
            
            if not second_latest_json_file:
                print('只找到一个JSON文件，无法进行对比')
                print(f'当前文件: {latest_json_file}')
                print('提示：运行爬虫后再次运行此功能即可进行对比')
                return True
            
            # 检查是否使用缓存文件
            is_cache_used = '_cache' in second_latest_json_file
            
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
            
            # 将差异信息追加到"小计"字段中
            if '小计' not in latest_json_data:
                latest_json_data['小计'] = []
            
            # 处理"小计"字段的不同格式
            if isinstance(latest_json_data['小计'], str):
                # 如果是字符串，先保存为字典
                old_summary = latest_json_data['小计']
                latest_json_data['小计'] = []
                # 尝试解析字符串中的信息（如果有）
                if old_summary and old_summary != "数据无变化":
                    # 创建一个基础记录
                    base_record = {
                        'timestamp': current_time,
                        'date': date_str,
                        'description': old_summary
                    }
                    latest_json_data['小计'].append(base_record)
            elif isinstance(latest_json_data['小计'], dict):
                # 如果是字典，转换为列表
                latest_json_data['小计'] = [latest_json_data['小计']]
            elif not isinstance(latest_json_data['小计'], list):
                # 其他类型，初始化为列表
                latest_json_data['小计'] = []
            
            # 追加新的差异记录
            latest_json_data['小计'].append(diff_data)
            
            # 按时间戳排序
            latest_json_data['小计'].sort(key=lambda x: x['timestamp'])
            
            FileManager.write_json(latest_json_file, latest_json_data)
            print(f'\n对比差异已追加到 {latest_json_file}')
            print(f'当前共有 {len(latest_json_data["小计"])} 条对比记录')
            
            # 打印对比结果
            print_separator()
            print('对比结果')
            print_separator()
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
            
            # 不删除缓存文件，保留用于后续对比
            # 缓存文件会在下一次运行爬虫时被覆盖
            if is_cache_used:
                print(f'注意：缓存文件 {second_latest_json_file} 已保留，用于后续对比')
                print(f'提示：下次运行爬虫时会自动更新缓存文件')
            
            return True
        except Exception as e:
            handle_exception(e, 'compare_json_files对比JSON文件')
            return False

    def compare_excel_with_json(self):
        try:
            print_separator()
            print('Excel与JSON数据对比工具')
            print_separator()
            
            latest_json_file = FileManager.get_latest_json_file()
            if not latest_json_file:
                print('无法获取最新的JSON文件')
                return False
            
            json_data = FileManager.read_json(latest_json_file)
            if not json_data:
                print('无法读取JSON文件')
                return False
            
            if isinstance(json_data, dict) and '商品列表' in json_data:
                products = json_data['商品列表']
            else:
                products = json_data if isinstance(json_data, list) else []
            
            json_stock_numbers = self.extract_stock_numbers(products)
            print(f'从JSON文件中读取到 {len(json_stock_numbers)} 个货号\n')
            
            high_price_stock_numbers = [
                p.get('货号', '') for p in products 
                if WegoScraper.parse_price(p.get('售价', '')) is not None
                and WegoScraper.parse_price(p.get('售价', '')) >= 599
            ]
            
            excel_stock_numbers = self.load_all_excel_data(remove_duplicates=False)
            if not excel_stock_numbers:
                print('无法从Excel文件读取货号')
                return False
            
            json_set, excel_set = set(json_stock_numbers), set(excel_stock_numbers)
            
            # 高价商品与已存在货号的对比
            high_price_set = set(high_price_stock_numbers)
            existing_set = json_set & excel_set  # 已存在的货号
            
            # 高价商品中已存在于Excel的货号
            high_price_existing = sorted(list(high_price_set & existing_set))
            # 高价商品中不在Excel的货号（多余的）
            high_price_extra = sorted(list(high_price_set - excel_set))
            
            # 保存对比结果
            result = self.compare_stock_numbers(json_stock_numbers, excel_stock_numbers, high_price_extra)
            result['high_price_existing'] = high_price_existing
            result['high_price_existing_count'] = len(high_price_existing)
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_str = datetime.now().strftime('%Y%m%d')
            
            data_change = "数据无变化" if result['missing_count'] == 0 and result['extra_in_json_count'] == 0 else f"数据有变化：缺失 {result['missing_count']} 个货号，多余 {result['extra_in_json_count']} 个货号"
            
            added_products = sorted([p.get('货号') for p in products if p.get('货号') and p.get('货号') not in excel_set]) if products else []
            
            removed_products = []
            prev_file = FileManager.get_latest_json_file('微购相册')
            if prev_file and prev_file != latest_json_file:
                old_data = FileManager.read_json(prev_file)
                if old_data and isinstance(old_data, dict):
                    removed_products = sorted([item.get('货号') for item in old_data.get('商品列表', []) if item.get('货号') and item.get('货号') not in json_set])
            
            duplicates = self.find_duplicate_stock_numbers(excel_stock_numbers)
            
            diff_data = {
                'timestamp': timestamp,
                'date': date_str,
                'json_file': os.path.basename(latest_json_file),
                'excel_file': os.path.basename(self.excel_file) if self.excel_file else 'None',
                'comparison': {
                    'missing_description': '微购相册比本地表格多出的序列号仅供参考',
                    'existing_description': '本地表格比微购相册上多的序列号，请仔细核对后删除多出的地方',
                    'extra_in_json_description': '微购相册比本地表格多出的序列号',
                    'high_price_extra_in_json': high_price_extra,
                    'high_price_extra_in_json_count': len(high_price_extra),
                    'high_price_extra_in_json_description': '只在JSON中存在但不在Excel中的售价>=599的货号',
                    **result
                },
                'result_message': self.get_result_message(result, duplicates),
                'data_change': data_change,
                'duplicates': duplicates,
                'duplicates_count': len(duplicates),
                '新增商品': added_products,
                '新增商品数量': len(added_products),
                '删除商品': removed_products,
                '删除商品数量': len(removed_products)
            }
            
            self._save_diff_log(date_str, diff_data)
            self._add_high_price_info_to_json(latest_json_file, json_data, high_price_extra)
            self._add_diff_to_json_summary(latest_json_file, json_data, diff_data)
            
            self.print_comparison_result(result, duplicates)
            return True
        except Exception as e:
            print(f'对比失败: {e}')
            traceback.print_exc()
            return False

    def _get_product_detail(self, item):
        return {
            "商品名称": item.get('商品名称', ''),
            "售价": item.get('售价', ''),
            "货号": item.get('货号', ''),
            "备注": item.get('备注', ''),
            "员工": item.get('员工', '')
        }
    
    def _save_diff_log(self, date_str, diff_data):
        diff_log_file = PathManager.get_diff_log_file(date_str)
        existing_data = FileManager.read_json(diff_log_file) if FileManager.file_exists(diff_log_file) else {'logs': []}
        
        if isinstance(existing_data, list):
            existing_data.append(diff_data)
        elif isinstance(existing_data, dict) and 'logs' in existing_data:
            existing_data['logs'].append(diff_data)
        else:
            existing_data = {'logs': [existing_data, diff_data]}
        
        FileManager.write_json(diff_log_file, existing_data)
        print(f'\n差异日志已保存到 {diff_log_file}')
    
    def _add_high_price_info_to_json(self, json_file_path, json_data, high_price_stock_numbers):
        if not json_data or not isinstance(json_data, dict):
            return
        
        products = json_data.get('商品列表', [])
        if not products:
            return
        
        high_price_count = 0
        for product in products:
            stock_num = product.get('货号', '')
            if stock_num in high_price_stock_numbers:
                product['备注'] = f'高价商品(≥599) - 只在JSON中存在但不在Excel中'
                high_price_count += 1
        
        if '统计信息' not in json_data:
            json_data['统计信息'] = {}
        
        json_data['统计信息']['高价商品数量'] = high_price_count
        json_data['统计信息']['高价商品货号'] = high_price_stock_numbers
        json_data['统计信息']['高价商品描述'] = '只在JSON中存在但不在Excel中的售价>=599的货号'
        
        FileManager.write_json(json_file_path, json_data)
        print(f'已为 {high_price_count} 个高价商品添加备注，并更新统计信息到 {json_file_path}')
    
    def _add_diff_to_json_summary(self, json_file_path, json_data, diff_data):
        if not json_data or not isinstance(json_data, dict):
            return
        
        if '小计' not in json_data:
            json_data['小计'] = []
        elif not isinstance(json_data['小计'], list):
            json_data['小计'] = [json_data['小计']] if json_data['小计'] else []
        
        excel_diff_record = {
            'timestamp': diff_data['timestamp'],
            'date': diff_data['date'],
            'json_file': diff_data['json_file'],
            'excel_file': diff_data['excel_file'],
            'comparison_type': 'Excel与JSON对比',
            'missing_count': diff_data['comparison']['missing_count'],
            'extra_in_json_count': diff_data['comparison']['extra_in_json_count'],
            'high_price_extra_in_json_count': diff_data['comparison']['high_price_extra_in_json_count'],
            'added_products_count': diff_data['新增商品数量'],
            'removed_products_count': diff_data['删除商品数量'],
            'data_change': diff_data['data_change'],
            'result_message': diff_data['result_message']
        }
        
        json_data['小计'].append(excel_diff_record)
        json_data['小计'].sort(key=lambda x: x['timestamp'])
        
        FileManager.write_json(json_file_path, json_data)
        print(f'Excel对比记录已追加到 {json_file_path} 的"小计"字段')

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
        
        # 显示高价商品(≥599)与已存在货号的对比结果
        print('\n=== 高价商品(≥599)与已存在货号对比 ===')
        print(f"高价商品总数: {len(result.get('high_price_stock_numbers', []))}")
        print(f"已存在于Excel的高价商品: {result.get('high_price_existing_count', 0)}")
        print(f"不在Excel的高价商品(多余): {result.get('high_price_count', 0)}")
        
        if result.get('high_price_existing'):
            print('\n高价商品中已存在于Excel的货号:')
            for i, num in enumerate(result['high_price_existing'], 1):
                print(f'  {num}', end=', ' if i % 5 != 0 else '\n')
            print()
        
        if result.get('high_price_stock_numbers'):
            print('\nJSON多余货号列表(高价商品):')
            for i, num in enumerate(result['high_price_stock_numbers'], 1):
                print(f'  {num}', end=', ' if i % 5 != 0 else '\n')
            print()
        else:
            print('\nJSON多余货号列表(高价商品): 无')
        
        if duplicates:
            print('\n重复的序列号:')
            for i, dup in enumerate(duplicates, 1):
                print(f'  {i}. 序列号: {dup["货号"]} (重复次数: {dup["count"]})')
        
        print('='*60)
        
        print('\n' + '='*60)
        print(StockNumberComparator.get_result_message(result, duplicates))
        print('='*60 + '\n')

    def run_comparison(self):
        print('='*60)
        print('货号对比工具 (TXT文件对比JSON)')
        print('='*60)
        
        data = self.load_json_data()
        json_stock_numbers = self.extract_stock_numbers(data)
        print(f'已从JSON加载 {len(json_stock_numbers)} 个货号\n')
        
        input_stock_numbers = None
        input_source = None
        
        if FileManager.file_exists(self.input_file):
            print(f'从文件 {self.input_file} 读取输入...')
            input_str = FileManager.read_text(self.input_file)
            if input_str:
                input_stock_numbers = self.parse_input_string(input_str)
                if input_stock_numbers:
                    input_source = 'TXT'
                    print(f'从TXT文件解析出 {len(input_stock_numbers)} 个货号\n')
        
        if not input_stock_numbers:
            print('未找到自动输入源，进入交互模式')
            print('功能说明：')
            print('  1. 直接输入货号字符串')
            print('  2. 输入 "load" 从本地文件读取')
            print('  3. 输入 "quit" 或 "exit" 退出程序')
            print('\n输入格式支持：')
            print('  - 逗号分隔: 12345, 67890, 11111')
            print('  - 空格分隔: 12345 67890 11111')
            print('  - 混合分隔: 12345, 67890 11111; 22222')
            print('='*60 + '\n')
            
            while True:
                try:
                    user_input = input('请输入货号字符串 (输入 "help" 查看帮助): ').strip()
                except (EOFError, KeyboardInterrupt):
                    print('\n程序已退出')
                    return
                
                if user_input.lower() in ['quit', 'exit', 'q', '退出']:
                    print('\n程序已退出')
                    return
                
                if user_input.lower() in ['help', 'h', '帮助']:
                    print('\n帮助信息：')
                    print('  load    - 从本地文件读取')
                    print('  quit    - 退出程序')
                    print('  help    - 显示此帮助信息')
                    print('\n输入格式：')
                    print('  - 直接输入货号字符串')
                    print('  - 支持多种分隔符')
                    print('  - 自动检测重复序列号')
                    print('='*60 + '\n')
                    continue
                
                if user_input.lower() in ['load', '读取']:
                    file_content = self.load_input_from_file()
                    if file_content:
                        input_stock_numbers = self.parse_input_string(file_content)
                        if input_stock_numbers:
                            input_source = 'TXT'
                            print(f'从TXT文件读取到 {len(input_stock_numbers)} 个货号\n')
                            break
                    else:
                        print('未找到TXT输入文件\n')
                
                if user_input:
                    input_stock_numbers = self.parse_input_string(user_input)
                    if input_stock_numbers:
                        input_source = '手动输入'
                        print(f'解析出 {len(input_stock_numbers)} 个货号\n')
                        break
        
        if input_stock_numbers:
            duplicates = self.find_duplicate_stock_numbers(input_stock_numbers)
            if duplicates:
                self.save_duplicate_log(duplicates)
            
            result = self.compare_stock_numbers(json_stock_numbers, input_stock_numbers)
            print(f'\n对比来源: {input_source}')
            self.print_comparison_result(result, duplicates)
        else:
            print('未找到有效的货号输入')


def main():
    while True:
        print_separator()
        print(f'Szwego商品爬虫和货号对比工具 - v{VERSION}')
        print_separator()
        
        config_file = PathManager.get_config_file()
        if not FileManager.file_exists(config_file):
            print(f'⚠️  警告: 配置文件不存在 ({config_file})')
            print(f'请先配置 {config_file} 文件')
            print_separator()
            input('按回车键退出...')
            return
        
        cookie_file = PathManager.get_cookie_file()
        is_valid, _ = CookieValidator.validate_and_prompt(cookie_file)
        
        if not is_valid:
            print('\n⚠️  Cookie状态异常，建议先更新Cookie')
            print_separator()
        
        print('请选择功能：')
        print('1. 运行爬虫（自动对比当天JSON文件）')
        print('2. 货号对比')
        print('3. Excel与JSON对比（自动保存差异日志）')
        print('4. 更新Cookie（自动更新）')
        print('5. 启动Web服务（可视化界面）')
        print('6. 文件清理工具')
        print('0. 退出')
        print_separator()
        
        try:
            choice = input('请输入选项 (0-6): ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n程序已退出')
            return
        
        def start_web():
            print('\n正在启动Web服务...')
            print('访问地址: http://localhost:8888')
            print('按 Ctrl+C 停止服务\n')
            
            os.system(f'"{VENV_PYTHON}" main.py --web')
        
        actions = {
            '1': lambda: run_scraper() or True,
            '2': lambda: StockNumberComparator().run_comparison() or True,
            '3': lambda: StockNumberComparator().compare_excel_with_json() or True,
            '4': lambda: update_cookie() or True,
            '5': lambda: start_web() or True,
            '6': lambda: run_cleaner() or True,
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
    """运行爬虫"""
    try:
        # 直接运行爬虫，使用现有的cookie
        print('准备启动爬虫，将使用现有Cookie...')
        
        scraper = WegoScraper()
        asyncio.run(scraper.run())
    except Exception as e:
        handle_exception(e, 'run_scraper运行爬虫')
        input('按回车键继续...')


def update_cookie():
    """自动更新Cookie功能"""
    print_separator()
    print('Cookie自动更新工具')
    print_separator()
    print('说明：')
    print('  - 自动打开浏览器并获取最新Cookie')
    print('  - 用户手动登录后关闭浏览器')
    print('  - 完成后自动保存到配置文件')
    print_separator()
    
    if async_playwright is None:
        print("错误: 请先安装playwright")
        print("运行: pip install playwright && playwright install chromium")
        return
    
    cookie_file = PathManager.get_cookie_file()
    if FileManager.file_exists(cookie_file):
        print(f'清空现有Cookie文件: {cookie_file}')
        FileManager.write_json(cookie_file, [])
        print('✓ Cookie文件已清空')
    
    async def get_cookie():
        async with async_playwright() as p:
            browser_args = WegoScraper.get_browser_args()
            chrome_path = WegoScraper.get_chrome_path()
            
            print(f'检测到系统: {Environment.SYSTEM}')
            if chrome_path:
                print(f'使用系统Chrome: {chrome_path}')
            else:
                print(f'使用Playwright内置Chromium')
            
            browser = await p.chromium.launch(
                headless=False, 
                args=browser_args, 
                executable_path=chrome_path
            )
            
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent=WegoScraper.get_user_agent()
            )
            
            existing_cookies = []
            cookie_file = PathManager.get_cookie_file()
            if FileManager.file_exists(cookie_file):
                existing_cookies = FileManager.read_json(cookie_file)
                if existing_cookies:
                    print(f'已加载 {len(existing_cookies)} 个现有Cookie')
                    await context.add_cookies(existing_cookies)
            
            page = await context.new_page()
            await page.goto('https://www.szwego.com', wait_until='networkidle')
            
            print('浏览器已打开，正在获取Cookie...')
            print('请稍候，系统会自动处理...')
            
            try:
                await page.wait_for_load_state('networkidle', timeout=10000)
                print('页面加载完成')
            except Exception as e:
                print(f'页面加载超时，继续获取Cookie: {e}')
            
            print_separator()
            print('浏览器已打开')
            print('请在浏览器中完成以下操作：')
            print('1. 如果需要登录，请完成登录')
            print('2. 登录后刷新一下页面')
            print('3. 程序会自动检测登录状态并关闭浏览器')
            print_separator()
            print('自动检测登录状态...')
            print_separator()
            
            start_time = time.time()
            timeout = 300
            login_detected = False
            
            while time.time() - start_time < timeout:
                try:
                    cookies = await context.cookies()
                    auth_cookies = [c for c in cookies if 'token' in c['name'].lower() or 'session' in c['name'].lower() or 'auth' in c['name'].lower()]
                    
                    if auth_cookies:
                        print('✓ 检测到登录成功，自动关闭浏览器...')
                        login_detected = True
                        break
                except:
                    pass
                
                await asyncio.sleep(5)
                elapsed = int(time.time() - start_time)
                print(f'等待登录中... ({elapsed}秒)')
            
            if not login_detected:
                print('⚠️ 登录超时，尝试获取当前Cookie')
            
            cookies = await context.cookies()
            szwego_cookies = [cookie for cookie in cookies if 'szwego.com' in cookie['domain']]
            
            for cookie in szwego_cookies:
                if cookie['domain'] == 'www.szwego.com':
                    cookie['domain'] = '.szwego.com'
            
            FileManager.write_json(cookie_file, szwego_cookies)
            
            print(f'✓ Cookie已保存到 {cookie_file}')
            print(f'✓ 共保存 {len(szwego_cookies)} 个Cookie')
            
            print_separator()
            print('Cookie有效期信息：')
            token_cookie = next((c for c in szwego_cookies if c['name'] == 'token'), None)
            if token_cookie and 'expires' in token_cookie and token_cookie['expires']:
                expiry_time = datetime.fromtimestamp(token_cookie['expires'])
                expiry_str = expiry_time.strftime('%Y-%m-%d')
                print(f'Token有效期: {expiry_str}')
            else:
                print('未找到Token Cookie')
            print_separator()
            
            config_file = PathManager.get_config_file()
            if FileManager.file_exists(config_file):
                config_data = FileManager.read_json(config_file)
                
                cookie_header = '; '.join([f'{c["name"]}={c["value"]}' for c in szwego_cookies])
                
                if 'headers' not in config_data:
                    config_data['headers'] = {}
                config_data['headers']['cookie'] = cookie_header
                config_data['cookies'] = szwego_cookies
                
                FileManager.write_json(config_file, config_data)
                print('✓ config.json中的Cookie已更新')
            
            await browser.close()
            print('✓ 浏览器已自动关闭')
            
            return True
    
    try:
        asyncio.run(get_cookie())
        print('\n✓ Cookie更新完成')
    except Exception as e:
        handle_exception(e, 'update_cookie更新Cookie')


def select_pip_mirror(venv_path: str):
    """pip镜像智能测速+写入配置"""
    MIRRORS = [
        ("阿里云", "https://mirrors.aliyun.com/pypi/simple/", "mirrors.aliyun.com"),
        ("清华", "https://pypi.tuna.tsinghua.edu.cn/simple/", "pypi.tuna.tsinghua.edu.cn"),
        ("腾讯云", "https://mirrors.cloud.tencent.com/pypi/simple/", "mirrors.cloud.tencent.com"),
        ("中科大", "https://mirrors.ustc.edu.cn/pypi/simple/", "mirrors.ustc.edu.cn"),
        ("豆瓣", "https://pypi.douban.com/simple/", "pypi.douban.com"),
    ]

    def test_mirror(name, url):
        try:
            start = time.time()
            urllib.request.urlopen(url, timeout=3)
            return round(time.time() - start, 3)
        except Exception:
            return None

    print("[*] 检测到未配置pip镜像源，正在测试镜像源速度...")
    os.makedirs(os.path.join(venv_path, "pip_config"), exist_ok=True)

    results = []
    for i, (name, url, host) in enumerate(MIRRORS, 1):
        print(f"[*] 测试镜像源 {i}/5: {name}...", end="", flush=True)
        elapsed = test_mirror(name, url)
        if elapsed is not None:
            print(f" {elapsed}秒")
            results.append((name, url, host, elapsed))
        else:
            print(" 失败")

    if results:
        results.sort(key=lambda x: x[3])
        fastest_name, fastest_mirror, fastest_host, fastest_time = results[0]
        print(f"[*] 最终选择最快镜像源: {fastest_name} ({fastest_time}秒)")
    else:
        fastest_name, fastest_mirror, fastest_host = "阿里云", "https://mirrors.aliyun.com/pypi/simple/", "mirrors.aliyun.com"
        print(f"[WARNING] 所有镜像源均失败，使用默认阿里云")

    conf_path = os.path.join(venv_path, "pip_config", "pip.conf" if platform.system() != "Windows" else "pip.ini")
    with open(conf_path, "w", encoding="utf-8") as f:
        if platform.system() != "Windows":
            f.write("[global]\n")
            f.write(f"index-url = {fastest_mirror}\n")
            f.write("[install]\n")
            f.write(f"trusted-host = {fastest_host}\n")
        else:
            f.write("[global]\r\n")
            f.write(f"index-url = {fastest_mirror}\r\n")
            f.write("[install]\r\n")
            f.write(f"trusted-host = {fastest_host}\r\n")
    print(f"[*] pip配置已写入: {conf_path}")


def install_playwright_cdn():
    """Playwright CDN智能测速+安装"""
    CDNS = [
        ("npmmirror", "https://npmmirror.com/mirrors/playwright/"),
        ("azureedge", "https://playwright.azureedge.net/builds/"),
        ("cdn", "https://cdn.playwright.dev/"),
    ]

    def test_cdn(name, url):
        try:
            start = time.time()
            urllib.request.urlopen(url, timeout=3)
            return round(time.time() - start, 3)
        except Exception:
            return None

    print("[*] 测试Playwright CDN速度...")
    results = []
    for name, url in CDNS:
        elapsed = test_cdn(name, url)
        if elapsed is not None:
            print(f"    {name}: {elapsed}秒")
            results.append((name, url, elapsed))
        else:
            print(f"    {name}: 失败")

    if results:
        results.sort(key=lambda x: x[2])
        fastest_name, fastest_url, fastest_time = results[0]
        print(f"[*] 最终选择最快Playwright CDN: {fastest_name} ({fastest_time}秒)")
        download_order = [(n, u) for n, u, _ in results if n != fastest_name]
        download_order.insert(0, (fastest_name, fastest_url))
    else:
        print("[WARNING] 所有CDN连通性测试失败，使用官方CDN下载")
        download_order = [("cdn", "https://cdn.playwright.dev/")]

    print("[*] 安装Playwright浏览器...")
    installed = False
    for name, url in download_order:
        print(f"    尝试从 {name} 下载...", flush=True)
        env = os.environ.copy()
        env["PLAYWRIGHT_DOWNLOAD_HOST"] = url
        result = subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            capture_output=True, text=True, env=env
        )
        if result.returncode == 0:
            print(f"[*] Playwright浏览器安装成功 (来源: {name})")
            installed = True
            break
        print(f"    {name} 下载失败，尝试下一个...")

    if not installed:
        print("[WARNING] Playwright浏览器安装失败，将在首次运行时自动安装")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Szwego商品爬虫')
    parser.add_argument('--web', action='store_true', help='启动Web服务模式')
    parser.add_argument('--port', type=int, default=8888, help='Web服务端口 (默认8888)')
    parser.add_argument('--setup', action='store_true', help='运行配置初始化向导')
    parser.add_argument('--username', '-u', help='登录用户名')
    parser.add_argument('--password', '-p', help='登录密码')
    parser.add_argument('--url', '-l', help='目标店铺URL')
    parser.add_argument('--excel', '-e', help='Excel文件路径')
    parser.add_argument('--task', type=int, choices=[1, 2, 3, 4, 6], help='直接执行指定任务后退出 (1:爬虫, 2:货号对比, 3:Excel对比, 4:更新Cookie, 6:文件清理)')
    parser.add_argument('--install-playwright', action='store_true', help='Playwright CDN智能测速+安装浏览器')
    parser.add_argument('--select-pip-mirror', action='store_true', help='pip镜像智能测速并写入配置')
    args = parser.parse_args()

    if args.select_pip_mirror:
        venv_path = os.environ.get('VIRTUAL_ENV') or os.path.join(PROJECT_DIR, '.venv')
        select_pip_mirror(venv_path)
        sys.exit(0)

    if args.install_playwright:
        install_playwright_cdn()
        sys.exit(0)

    if args.setup or (args.username and args.password and args.url):
        print("=" * 50)
        print("配置初始化向导")
        print("=" * 50)

        username = args.username
        password = args.password
        url = args.url
        excel = args.excel or ""

        if not username:
            username = input("请输入用户名: ")
        if not password:
            password = input("请输入密码: ")
        if not url:
            url = input("请输入目标URL: ")

        print("\n正在启动浏览器进行登录...")
        print("请在浏览器中登录您的账号")

        os.makedirs("config", exist_ok=True)

        async def get_cookie():
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                context = await browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
                )
                page = await context.new_page()
                await page.goto('https://www.szwego.com', wait_until='networkidle')

                print('\n请在浏览器中登录您的账号...')

                start_time = time.time()
                timeout = 300
                login_detected = False

                while time.time() - start_time < timeout:
                    try:
                        cookies = await context.cookies()
                        token_cookie = next((c for c in cookies if c['name'] == 'token'), None)
                        if token_cookie and token_cookie['value']:
                            print('\n✓ 检测到登录成功！正在获取Cookie...')
                            login_detected = True
                            break
                    except:
                        pass
                    await asyncio.sleep(3)
                    elapsed = int(time.time() - start_time)
                    print(f'等待登录中... ({elapsed}秒)', end='\r')

                if not login_detected:
                    print('\n⚠️ 登录超时，将尝试获取当前Cookie')

                cookies = await context.cookies()
                szwego_cookies = [cookie for cookie in cookies if 'szwego.com' in cookie.get('domain', '')]
                for cookie in szwego_cookies:
                    if cookie['domain'] == 'www.szwego.com':
                        cookie['domain'] = '.szwego.com'

                cookie_file = "config/cookies.json"
                with open(cookie_file, "w", encoding="utf-8") as f:
                    json.dump(szwego_cookies, f, ensure_ascii=False, indent=2)
                print(f'✓ Cookie已保存 ({len(szwego_cookies)}个)')

                await browser.close()
                return szwego_cookies

        if async_playwright is None:
            print("错误: 请先安装playwright")
            print("运行: pip install playwright && playwright install chromium")
            sys.exit(1)

        cookies = asyncio.run(get_cookie())

        cookie_header = '; '.join([f'{c["name"]}={c["value"]}' for c in cookies])

        config = {
            "login": {
                "username": username,
                "password": password,
                "login_type": "phone"
            },
            "target_url": url,
            "scroll_config": {
                "max_attempts": 30,
                "same_height_limit": 8,
                "scroll_wait_time": 0.8,
                "popup_close_interval": 5,
                "popup_close_limit": 3,
                "popup_close_wait": 0.3,
                "dynamic_adjust": True
            },
            "headers": {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "max-age=0",
                "connection": "keep-alive",
                "cookie": cookie_header,
                "host": "www.szwego.com",
                "sec-ch-ua": "\"Chromium\";v=\"146\", \"Not-A.Brand\";v=\"24\", \"Google Chrome\";v=\"146\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
            },
            "cookies": cookies,
            "output_file": "file/output.json",
            "cookie_file": "config/cookies.json",
            "excel_files": [excel] if excel else []
        }

        config_path = "config/config.json"
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

        print(f'\n✓ 配置文件创建成功！')
        print("\n========================================")
        print("   初始化完成！")
        print("========================================")
        print(f"\n配置信息：")
        print(f"  - 用户名: {username}")
        print(f"  - 目标URL: {url}")
        print(f"  - Cookie数量: {len(cookies)}")
        sys.exit(0)

    if args.task:
        print(f'执行任务 {args.task}...')
        try:
            if args.task == 1:
                run_scraper()
            elif args.task == 2:
                StockNumberComparator().run_comparison()
            elif args.task == 3:
                StockNumberComparator().compare_excel_with_json()
            elif args.task == 4:
                update_cookie()
            elif args.task == 6:
                run_cleaner()
            print('任务完成')
        except Exception as e:
            handle_exception(e, f'任务{args.task}执行')
        sys.exit(0)
    
    if args.web:
        @app.route('/')
        def index():
            current_version = get_version_from_readme()
            with open(os.path.join(PROJECT_DIR, 'index.html'), 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('版本: 3.0.9', f'版本: {current_version}')
            response = Response(content, mimetype='text/html')
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response

        @app.route('/dist/<path:filename>')
        def dist_files(filename):
            file_path = os.path.join(PROJECT_DIR, 'dist', filename)

            if not os.path.isfile(file_path):
                return "File not found", 404

            mimetype_map = {
                '.js': 'application/javascript',
                '.css': 'text/css',
                '.html': 'text/html',
                '.json': 'application/json',
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.svg': 'image/svg+xml',
                '.ico': 'image/x-icon',
                '.woff': 'font/woff',
                '.woff2': 'font/woff2',
            }
            ext = os.path.splitext(filename)[1].lower()
            mimetype = mimetype_map.get(ext, 'application/octet-stream')

            accept_encoding = request.headers.get('Accept-Encoding', '')
            gzip_enabled = 'gzip' in accept_encoding.lower()

            if gzip_enabled and ext in ['.js', '.css', '.html', '.json', '.svg']:
                with open(file_path, 'rb') as f:
                    content = f.read()

                gzip_content = gzip.compress(content, compresslevel=6)
                response = Response(gzip_content, mimetype=mimetype)
                response.headers['Content-Encoding'] = 'gzip'
                response.headers['Vary'] = 'Accept-Encoding'
                response.headers['Cache-Control'] = 'public, max-age=86400'
                return response
            else:
                response = send_file(file_path, mimetype=mimetype)
                response.headers['Cache-Control'] = 'public, max-age=86400'
                return response

        @app.route('/run', methods=['POST'])
        def run_command():
            data = request.get_json()
            command = data.get('command', '')
            if not command:
                return jsonify({'error': '命令不能为空'}), 400
            
            if command.startswith('python '):
                command = command.replace('python ', VENV_PYTHON + ' ', 1)
            if command.startswith('python3 '):
                command = command.replace('python3 ', VENV_PYTHON + ' ', 1)
            
            task_id = str(uuid.uuid4())[:8]
            tasks[task_id] = {'command': command, 'status': 'starting', 'output': '', 'returncode': None, 'error': None}
            thread = threading.Thread(target=run_command_background, args=(task_id, command))
            thread.start()
            return jsonify({'success': True, 'task_id': task_id, 'message': f'命令已启动 (系统: {Environment.SYSTEM})'})

        @app.route('/input', methods=['POST'])
        def send_input():
            data = request.get_json()
            task_id, user_input = data.get('task_id', ''), data.get('input', '')
            if task_id not in processes:
                return jsonify({'error': '没有正在运行的进程'}), 404
            try:
                process = processes[task_id]
                process.stdin.write(user_input + '\n')
                process.stdin.flush()
                return jsonify({'success': True, 'message': '输入已发送'})
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/kill', methods=['POST'])
        def kill_task():
            data = request.get_json()
            task_id = data.get('task_id', '')
            if task_id not in processes:
                return jsonify({'success': True, 'message': '进程已结束'})
            try:
                process = processes[task_id]
                try:
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        process.kill()
                except:
                    pass
                if task_id in tasks:
                    tasks[task_id]['status'] = 'killed'
                if task_id in processes:
                    del processes[task_id]
                return jsonify({'success': True, 'message': '进程已终止'})
            except:
                return jsonify({'success': True, 'message': '操作完成'})

        @app.route('/output/<task_id>', methods=['GET'])
        def get_output(task_id):
            if task_id not in tasks:
                return jsonify({'error': '任务不存在'}), 404
            task = tasks[task_id]
            return jsonify({'status': task['status'], 'output': task.get('output', ''), 'returncode': task.get('returncode'), 'error': task.get('error')})

        @app.route('/api/cookie', methods=['GET'])
        def get_cookie_status():
            cookie_file = os.path.join(PROJECT_DIR, 'config', 'cookies.json')
            if not os.path.exists(cookie_file):
                return jsonify({'error': 'Cookie文件不存在', 'valid': False, 'system': Environment.SYSTEM}), 404
            try:
                with open(cookie_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                
                if not cookies or len(cookies) == 0:
                    return jsonify({'error': 'Cookie文件为空', 'valid': False, 'system': Environment.SYSTEM}), 404
                
                # 查找token cookie
                token_cookie = None
                for c in cookies:
                    if c.get('name') == 'token':
                        token_cookie = c
                        break
                
                if not token_cookie:
                    return jsonify({'error': '未找到Token Cookie', 'valid': False, 'system': Environment.SYSTEM}), 404
                
                expires = token_cookie.get('expires')
                if not expires or not isinstance(expires, (int, float)) or expires <= 0:
                    return jsonify({'error': 'Token Cookie无效', 'valid': False, 'system': Environment.SYSTEM}), 404
                
                expires_time = datetime.fromtimestamp(expires)
                hours_remaining = (expires_time - datetime.now()).total_seconds() / 3600
                
                return jsonify({
                    'valid': True, 
                    'expires': expires_time.strftime('%Y-%m-%d'), 
                    'hours_remaining': round(hours_remaining, 1), 
                    'expired': hours_remaining <= 0, 
                    'system': Environment.SYSTEM,
                    'cookie_name': 'Token'
                })
            except Exception as e:
                return jsonify({'error': str(e), 'valid': False}), 500

        @app.route('/api/sku/compare', methods=['GET'])
        def compare_sku():
            try:
                json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
                if not json_files:
                    return jsonify({'error': '没有找到JSON文件'}), 404
                latest_json = max(json_files, key=os.path.getmtime)
                
                with open(latest_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                json_stock_numbers = sorted([p.get('货号', '') for p in products if p.get('货号')])
                
                input_file = os.path.join(PROJECT_DIR, 'config', 'input_stock_numbers.txt')
                txt_stock_numbers = []
                if os.path.exists(input_file):
                    with open(input_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        txt_stock_numbers = sorted(set(re.findall(r'\d+', content)))
                
                json_set = set(json_stock_numbers)
                txt_set = set(txt_stock_numbers)
                
                result = {
                    'json_file': os.path.basename(latest_json),
                    'json_count': len(json_set),
                    'txt_count': len(txt_set),
                    'json_skus': json_stock_numbers,
                    'txt_skus': txt_stock_numbers,
                    'missing_in_json': sorted(list(txt_set - json_set)),
                    'extra_in_json': sorted(list(json_set - txt_set)),
                    'common': sorted(list(txt_set & json_set)),
                    'missing_count': len(txt_set - json_set),
                    'extra_count': len(json_set - txt_set),
                    'common_count': len(txt_set & json_set)
                }
                return jsonify(result)
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/sku/compare/txt', methods=['GET', 'POST'])
        def compare_sku_txt():
            try:
                json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
                if not json_files:
                    return jsonify({'error': '没有找到JSON文件'}), 404
                latest_json = max(json_files, key=os.path.getmtime)
                
                with open(latest_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                json_stock_numbers = sorted([p.get('货号', '') for p in products if p.get('货号')])
                
                txt_stock_numbers_raw = []
                if request.method == 'POST':
                    req_data = request.get_json()
                    input_skus = req_data.get('skus', '')
                    txt_stock_numbers_raw = re.findall(r'\d+', input_skus)
                else:
                    input_file = os.path.join(PROJECT_DIR, 'config', 'input_stock_numbers.txt')
                    if os.path.exists(input_file):
                        with open(input_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            txt_stock_numbers_raw = re.findall(r'\d+', content)
                
                txt_stock_numbers = sorted(set(txt_stock_numbers_raw))
                duplicates = StockNumberComparator.find_duplicate_stock_numbers(txt_stock_numbers_raw)
                
                json_set = set(json_stock_numbers)
                txt_set = set(txt_stock_numbers)
                
                result = {
                    'type': 'txt',
                    'json_file': os.path.basename(latest_json),
                    'json_count': len(json_set),
                    'txt_count': len(txt_set),
                    'missing_in_json': sorted(list(txt_set - json_set)),
                    'extra_in_json': sorted(list(json_set - txt_set)),
                    'common': sorted(list(txt_set & json_set)),
                    'missing_count': len(txt_set - json_set),
                    'extra_count': len(json_set - txt_set),
                    'common_count': len(txt_set & json_set),
                    'duplicate_count': len(duplicates),
                    'duplicates': duplicates
                }
                return jsonify(result)
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/sku/compare/excel', methods=['GET'])
        def compare_sku_excel():
            try:
                if pd is None:
                    return jsonify({'error': 'pandas未安装，Excel对比功能不可用'}), 500
                
                today = datetime.now().strftime('%Y%m%d')
                diff_log_file = os.path.join(PROJECT_DIR, 'file', f'diff_log_{today}.json')
                
                json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
                json_files = [f for f in json_files if '_cache' not in f]
                if not json_files:
                    return jsonify({'error': '没有找到JSON文件'}), 404
                latest_json = max(json_files, key=os.path.getmtime)
                
                with open(latest_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                json_stock_numbers = sorted([p.get('货号', '') for p in products if p.get('货号')])
                
                excel_files_list = []
                config_file = os.path.join(PROJECT_DIR, 'config', 'config.json')
                if os.path.exists(config_file):
                    with open(config_file, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                    excel_files = config.get('excel_files', [])
                    for path in excel_files:
                        expanded_path = os.path.expanduser(path)
                        if os.path.exists(expanded_path):
                            excel_files_list.append(expanded_path)
                
                if not excel_files_list:
                    excel_files_list = [os.path.join(PROJECT_DIR, 'config', '本地商品表格.xlsx')]
                
                excel_files_list = list(dict.fromkeys(os.path.abspath(f) for f in excel_files_list))
                
                excel_stock_numbers = []
                daily_profit_report = None  # 存储每日利润报表A317内容
                
                for excel_file in excel_files_list:
                    if os.path.exists(excel_file):
                        try:
                            if daily_profit_report is None:
                                daily_profit_report = get_daily_profit_report_from_excel(excel_file)
                            
                            excel_dfs = FileManager.safe_read_excel(excel_file, max_retries=3, retry_delay=1.0)
                            if excel_dfs is None:
                                print(f'无法读取Excel文件: {excel_file}')
                                continue
                            
                            df = None
                            sheet_name = None
                            sku_column = None
                            
                            for sheet, temp_df in excel_dfs.items():
                                if '货号' in temp_df.columns:
                                    df = temp_df
                                    sheet_name = sheet
                                    sku_column = '货号'
                                    break
                                elif '序列号' in temp_df.columns:
                                    df = temp_df
                                    sheet_name = sheet
                                    sku_column = '序列号'
                                    break
                                elif '闲鱼' in sheet:
                                    if len(temp_df.columns) > 4:
                                        second_row = temp_df.iloc[1].tolist()
                                        if '序列号' in second_row:
                                            col_idx = second_row.index('序列号')
                                            temp_df.columns = second_row
                                            temp_df = temp_df.drop([0, 1]).reset_index(drop=True)
                                            df = temp_df
                                            sheet_name = sheet
                                            sku_column = '序列号'
                                            break
                            
                            if df is not None and sku_column is not None:
                                file_stock_numbers = [str(int(x)) if isinstance(x, float) and x == int(x) else str(x).strip() 
                                                             for x in df[sku_column].dropna() 
                                                             if str(x).strip() and str(x).strip() != 'nan' and str(x).strip() != '序列号']
                                excel_stock_numbers.extend(file_stock_numbers)
                        except PermissionError as e:
                            if "sharing violation" in str(e).lower() or "另一个程序" in str(e) or "正在使用" in str(e):
                                return jsonify({
                                    'error': f'Excel文件被其他程序占用，请关闭后再试',
                                    'detail': f'文件: {os.path.basename(excel_file)}',
                                    'path': excel_file
                                }), 423
                            raise
                        except Exception as e:
                            print(f'读取Excel文件失败: {excel_file} - {e}')
                            continue
                
                if not excel_stock_numbers:
                    return jsonify({'error': f'Excel文件中未找到"货号"或"序列号"列'}), 404
                
                json_set = set(json_stock_numbers)
                excel_set = set(excel_stock_numbers)
                
                json_sku_counts = {}
                for sku in json_stock_numbers:
                    json_sku_counts[sku] = json_sku_counts.get(sku, 0) + 1
                duplicate_skus_json = {sku: count for sku, count in json_sku_counts.items() if count > 1}
                
                excel_sku_counts = {}
                for sku in excel_stock_numbers:
                    excel_sku_counts[sku] = excel_sku_counts.get(sku, 0) + 1
                duplicate_skus = {sku: count for sku, count in excel_sku_counts.items() if count > 1}
                
                high_price_count = 0
                high_price_stock_numbers = []
                for p in products:
                    price = p.get('售价', '')
                    if price:
                        try:
                            price_val = float(price.replace('¥', '').replace(',', ''))
                            if price_val >= 599:
                                high_price_count += 1
                                sku = p.get('货号', '')
                                if sku:
                                    high_price_stock_numbers.append(str(sku))
                        except Exception as e:
                            handle_exception(e, '/api/compare解析商品价格')
                            pass
                
                # 高价商品与已存在货号的对比
                high_price_set = set(high_price_stock_numbers)
                high_price_existing = sorted(list(high_price_set & excel_set))
                high_price_extra_in_json = sorted(list(high_price_set - excel_set))
                
                # 判断今天是否运行过爬虫：从 JSON 的"小计"中查找今天的记录
                xiaoji_records = data.get('小计', []) if isinstance(data, dict) else []
                today_xiaoji = None
                for record in reversed(xiaoji_records):
                    if record.get('timestamp', '').startswith(today):
                        today_xiaoji = record
                        break
                
                # 从差异日志读取今天之前的数据（昨天 vs 今天）
                added_products_all = []
                removed_products = []
                added_high_price = []
                
                if os.path.exists(diff_log_file):
                    with open(diff_log_file, 'r', encoding='utf-8') as f:
                        diff_data = json.load(f)
                    if diff_data.get('logs'):
                        last_log = diff_data['logs'][-1]
                        added_products_all = last_log.get('added', [])
                        removed_products = last_log.get('removed', [])
                
                # 如果今天运行过爬虫（有小计记录），使用小计的数据
                if today_xiaoji:
                    added_products_all = today_xiaoji.get('added', [])
                    removed_products = today_xiaoji.get('removed', [])
                    # 高价新增从新增商品中筛选
                    for sku in added_products_all:
                        for p in products:
                            if str(p.get('货号', '')) == str(sku):
                                price = p.get('售价', '')
                                try:
                                    price_val = float(price.replace('¥', '').replace(',', '')) if price else 0
                                    if price_val >= 599:
                                        added_high_price.append(sku)
                                except:
                                    pass
                                break
                
                added_high_price = sorted(list(set(added_high_price)))
                
                result = {
                    'type': 'excel',
                    'json_file': os.path.basename(latest_json),
                    'excel_files': [os.path.basename(f) for f in excel_files_list],
                    'excel_files_count': len(excel_files_list),
                    'input_count': len(excel_set),
                    'extra_count': len(json_set - excel_set),
                    'json_count': len(json_set),
                    'common_count': len(excel_set & json_set),
                    'duplicate_count': len(duplicate_skus),
                    'duplicate_count_json': len(duplicate_skus_json),
                    'duplicate_count_excel': len(duplicate_skus),
                    'high_price_count': high_price_count,
                    'missing_in_json': sorted(list(excel_set - json_set)),
                    'extra_in_json': sorted(list(json_set - excel_set)),
                    'common': sorted(list(excel_set & json_set)),
                    'duplicates': duplicate_skus,
                    'duplicates_json': duplicate_skus_json,
                    'duplicates_excel': duplicate_skus,
                    'missing_count': len(excel_set - json_set),
                    'high_price_extra_in_json': high_price_extra_in_json,
                    'high_price_existing': high_price_existing,
                    'added_high_price': added_high_price,
                    'added_high_price_count': len(added_high_price),
                    'added_products': sorted(added_products_all)[:100],
                    'added_products_count': len(added_products_all),
                    'removed_products': removed_products[:100],
                    'removed_products_count': len(removed_products),
                    'daily_profit_report': daily_profit_report,
                    'report_text': daily_profit_report
                }
                return jsonify(result)
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/products', methods=['GET'])
        def get_all_products():
            json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
            if not json_files:
                return jsonify({'error': '没有找到JSON文件'}), 404
            latest_file = max(json_files, key=os.path.getmtime)
            try:
                with open(latest_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                
                for p in products:
                    media_result = []
                    img_data = p.get('图片', '')
                    if img_data:
                        try:
                            if isinstance(img_data, list):
                                for b64_str in img_data:
                                    try:
                                        media_result.append(base64.b64decode(b64_str).decode('utf-8'))
                                    except:
                                        media_result.append(b64_str)
                            else:
                                try:
                                    media_result = base64.b64decode(img_data).decode('utf-8')
                                except:
                                    media_result = img_data
                        except:
                            media_result = img_data
                    p['图片'] = media_result if media_result else img_data
                
                high_price_products = []
                total_price = 0
                total_fee = 0
                valid_price_count = 0
                
                def safe_print(*args, **kwargs):
                    try:
                        print(*args, **kwargs)
                    except (IOError, OSError):
                        pass
                
                safe_print(f'开始处理 {len(products)} 个商品...')
                
                for p in products:
                    try:
                        price_str = p.get('售价', '')
                        if not price_str or not price_str.strip():
                            continue
                        
                        price_clean = price_str.replace('¥', '').replace(',', '').strip()
                        price = float(price_clean)
                        
                        if price >= 599:
                            high_price_products.append(p)
                        
                        if price > 0:
                            total_price += price
                            fee = price * 0.016
                            total_fee += fee
                            valid_price_count += 1
                    except Exception as e:
                        safe_print(f'处理商品时出错: {e}, price_str: {p.get("售价", "")}')
                        pass
                
                safe_print(f'统计结果: valid_price_count={valid_price_count}, total_price={total_price}, high_price_count={len(high_price_products)}')
                
                avg_price = total_price / valid_price_count if valid_price_count > 0 else 0
                
                return jsonify({
                    'filename': os.path.basename(latest_file), 
                    'total': len(products), 
                    'products': products[:100], 
                    'highPriceProducts': high_price_products[:500], 
                    'highPriceCount': len(high_price_products),
                    'totalPrice': f'¥{total_price:,.2f}',
                    'avgPrice': f'¥{avg_price:,.2f}',
                    'fee': f'¥{total_fee:,.2f}',
                    'system': Environment.SYSTEM
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/daily-profit', methods=['GET'])
        def get_daily_profit():
            try:
                if pd is None or openpyxl is None:
                    return jsonify({'error': 'pandas或openpyxl未安装，每日利润报表功能不可用'}), 500
                
                group_by = request.args.get('group_by', 'day')
                start_date = request.args.get('start_date', None)
                end_date = request.args.get('end_date', None)
                
                excel_files_list = []
                config_file = os.path.join(PROJECT_DIR, 'config', 'config.json')
                if os.path.exists(config_file):
                    with open(config_file, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                    excel_files = config.get('excel_files', [])
                    for path in excel_files:
                        expanded_path = os.path.expanduser(path)
                        if os.path.exists(expanded_path):
                            excel_files_list.append(expanded_path)
                
                if not excel_files_list:
                    excel_files_list = [os.path.join(PROJECT_DIR, 'config', '本地商品表格.xlsx')]
                
                excel_files_list = list(dict.fromkeys(os.path.abspath(f) for f in excel_files_list))
                
                daily_profit_report = None
                table_data = []
                all_records = []
                
                for excel_file in excel_files_list:
                    if os.path.exists(excel_file):
                        try:
                            if daily_profit_report is None:
                                daily_profit_report = get_daily_profit_report_from_excel(excel_file)
                            
                            wb = openpyxl.load_workbook(excel_file, data_only=True)
                            sheet_name = '每日利润'
                            if sheet_name in wb.sheetnames:
                                ws = wb[sheet_name]
                            else:
                                ws = wb.active
                            
                            for row_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column, values_only=False)):
                                row_data = []
                                for cell in row:
                                    row_data.append(cell.value)
                                table_data.append(row_data)
                                
                                if row_idx > 0:
                                    try:
                                        amount = float(str(row_data[1] or 0).replace('¥', '').replace(',', '').strip()) if row_data[1] else 0
                                        cost = float(str(row_data[2] or 0).replace('¥', '').replace(',', '').strip()) if row_data[2] else 0
                                        profit = float(str(row_data[3] or 0).replace('¥', '').replace(',', '').strip()) if row_data[3] else 0
                                        date_val = row_data[4]
                                        remark = row_data[5] if len(row_data) > 5 else ''
                                        
                                        if isinstance(date_val, datetime):
                                            record_date = date_val
                                        elif isinstance(date_val, str):
                                            try:
                                                record_date = datetime.strptime(date_val.split()[0], '%Y-%m-%d')
                                            except:
                                                continue
                                        else:
                                            continue
                                        
                                        all_records.append({
                                            '项目': row_data[0],
                                            '金额': amount,
                                            '成本': cost,
                                            '纯利': profit,
                                            '日期': record_date,
                                            '备注': remark
                                        })
                                    except (ValueError, TypeError, IndexError):
                                        pass
                            
                            wb.close()
                            break
                        except Exception as e:
                            print(f'读取Excel文件失败: {excel_file} - {e}')
                            continue
                
                if not table_data:
                    return jsonify({'error': '未找到Excel数据'}), 404
                
                if start_date:
                    try:
                        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
                        all_records = [r for r in all_records if r['日期'] >= start_dt]
                    except:
                        pass
                
                if end_date:
                    try:
                        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
                        all_records = [r for r in all_records if r['日期'] <= end_dt]
                    except:
                        pass
                
                summary = {}
                for record in all_records:
                    date_key = record['日期']
                    
                    if group_by == 'month':
                        key = date_key.strftime('%Y-%m')
                    elif group_by == 'year':
                        key = date_key.strftime('%Y')
                    elif group_by == 'all':
                        key = '总计'
                    else:
                        key = date_key.strftime('%Y-%m-%d')
                    
                    if key not in summary:
                        summary[key] = {'金额': 0, '成本': 0, '纯利': 0, '数量': 0, '日期': key}
                    
                    summary[key]['金额'] += record['金额']
                    summary[key]['成本'] += record['成本']
                    summary[key]['纯利'] += record['纯利']
                    summary[key]['数量'] += 1
                
                summary_list = sorted(summary.values(), key=lambda x: x['日期'])
                
                result = {
                    'daily_profit_report': daily_profit_report,
                    'table_data': table_data,
                    'excel_file': os.path.basename(excel_files_list[0]) if excel_files_list else None,
                    'summary': summary_list,
                    'group_by': group_by,
                    'total_records': len(all_records),
                    'all_records': all_records
                }
                return jsonify(result)
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        def get_all_products():
            json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
            if not json_files:
                return jsonify({'error': '没有找到JSON文件'}), 404
            latest_file = max(json_files, key=os.path.getmtime)
            try:
                with open(latest_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                
                for p in products:
                    media_result = []
                    img_data = p.get('图片', '')
                    if img_data:
                        try:
                            if isinstance(img_data, list):
                                for b64_str in img_data:
                                    try:
                                        media_result.append(base64.b64decode(b64_str).decode('utf-8'))
                                    except:
                                        media_result.append(b64_str)
                            else:
                                try:
                                    media_result = base64.b64decode(img_data).decode('utf-8')
                                except:
                                    media_result = img_data
                        except:
                            media_result = img_data
                    p['图片'] = media_result if media_result else img_data
                
                high_price_products = []
                total_price = 0
                total_fee = 0
                valid_price_count = 0
                
                def safe_print(*args, **kwargs):
                    try:
                        print(*args, **kwargs)
                    except (IOError, OSError):
                        pass
                
                safe_print(f'开始处理 {len(products)} 个商品...')
                
                for p in products:
                    try:
                        price_str = p.get('售价', '')
                        if not price_str or not price_str.strip():
                            continue
                        
                        price_clean = price_str.replace('¥', '').replace(',', '').strip()
                        price = float(price_clean)
                        
                        if price >= 599:
                            high_price_products.append(p)
                        
                        # 计算总价和手续费
                        if price > 0:
                            total_price += price
                            # 计算闲鱼平台手续费（售价 * 1.6%）
                            fee = price * 0.016
                            total_fee += fee
                            valid_price_count += 1
                    except Exception as e:
                        safe_print(f'处理商品时出错: {e}, price_str: {p.get("售价", "")}')
                        pass
                
                safe_print(f'统计结果: valid_price_count={valid_price_count}, total_price={total_price}, high_price_count={len(high_price_products)}')
                
                # 计算平均价格
                avg_price = total_price / valid_price_count if valid_price_count > 0 else 0
                
                return jsonify({
                    'filename': os.path.basename(latest_file), 
                    'total': len(products), 
                    'products': products[:100], 
                    'highPriceProducts': high_price_products[:500], 
                    'highPriceCount': len(high_price_products),
                    'totalPrice': f'¥{total_price:,.2f}',
                    'avgPrice': f'¥{avg_price:,.2f}',
                    'fee': f'¥{total_fee:,.2f}',
                    'system': Environment.SYSTEM
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/product', methods=['GET'])
        def get_product():
            sku = request.args.get('sku', '').strip()
            if not sku:
                return jsonify({'error': '请提供货号'}), 400
            json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
            if not json_files:
                return jsonify({'found': False, 'error': '没有找到JSON文件'})
            latest_file = max(json_files, key=os.path.getmtime)
            try:
                with open(latest_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                for p in products:
                    if str(p.get('货号')) == str(sku):
                        # 解码Base64图片URL
                        images = p.get('图片', [])
                        if images:
                            if isinstance(images, list):
                                decoded_images = []
                                for img in images:
                                    try:
                                        decoded = base64.b64decode(img).decode('utf-8')
                                        decoded_images.append(decoded)
                                    except:
                                        decoded_images.append(img)
                                p['图片'] = decoded_images
                            elif isinstance(images, str):
                                try:
                                    decoded = base64.b64decode(images).decode('utf-8')
                                    p['图片'] = [decoded]
                                except:
                                    p['图片'] = [images]
                            else:
                                p['图片'] = []
                        else:
                            p['图片'] = []
                        return jsonify({'found': True, 'product': p})
                return jsonify({'found': False, 'error': '未找到该商品'})
            except Exception as e:
                return jsonify({'found': False, 'error': str(e)})
        
        @app.route('/api/product/search', methods=['GET'])
        def search_product():
            sku = request.args.get('sku', '').strip()
            if not sku:
                return jsonify({'error': '请提供货号'}), 400
            json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
            if not json_files:
                return jsonify({'error': '没有找到JSON文件'}), 404
            latest_file = max(json_files, key=os.path.getmtime)
            try:
                with open(latest_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                for p in products:
                    if p.get('货号') == sku:
                        media_result = []
                        new_image_url = p.get('图片', '')
                        if new_image_url:
                            try:
                                img_data = json.loads(new_image_url) if isinstance(new_image_url, str) else new_image_url
                            except:
                                img_data = new_image_url
                            if isinstance(img_data, list):
                                for b64_str in img_data:
                                    try:
                                        decoded_url = base64.b64decode(b64_str).decode('utf-8')
                                        if decoded_url.startswith('http'):
                                            media_result.append(decoded_url)
                                        else:
                                            media_result.append(b64_str)
                                    except:
                                        media_result.append(b64_str)
                            else:
                                try:
                                    decoded_url = base64.b64decode(img_data).decode('utf-8')
                                    if decoded_url.startswith('http'):
                                        media_result = [decoded_url]
                                    else:
                                        media_result = [img_data]
                                except:
                                    media_result = [img_data]
                        p['图片'] = media_result
                        return jsonify({'found': True, 'product': p, 'filename': os.path.basename(latest_file), 'saved': True})
                return jsonify({'found': False, 'error': f'未找到货号为 {sku} 的商品'})
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/product/by-description', methods=['GET'])
        def get_product_by_description():
            description = request.args.get('description', '').strip()
            if not description:
                return jsonify({'error': '请提供商品描述'}), 400
            json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
            if not json_files:
                return jsonify({'found': False, 'error': '没有找到JSON文件'})
            latest_file = max(json_files, key=os.path.getmtime)
            try:
                with open(latest_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                for p in products:
                    stored_desc = p.get('商品描述', '')
                    if stored_desc.replace(' ', '') == description.replace(' ', ''):
                        images = p.get('图片', [])
                        if images:
                            if isinstance(images, list):
                                decoded_images = []
                                for img in images:
                                    try:
                                        decoded = base64.b64decode(img).decode('utf-8')
                                        decoded_images.append(decoded)
                                    except:
                                        decoded_images.append(img)
                                p['图片'] = decoded_images
                            elif isinstance(images, str):
                                try:
                                    decoded = base64.b64decode(images).decode('utf-8')
                                    p['图片'] = [decoded]
                                except:
                                    p['图片'] = [images]
                            else:
                                p['图片'] = []
                        else:
                            p['图片'] = []
                        return jsonify({'found': True, 'product': p})
                return jsonify({'found': False, 'error': '未找到该商品'})
            except Exception as e:
                return jsonify({'found': False, 'error': str(e)})

        @app.route('/api/clean/list', methods=['POST'])
        def api_clean_list():
            try:
                data = request.get_json()
                directory = data.get('directory', '')
                
                if not directory or directory.strip() == '':
                    directory = PROJECT_DIR
                elif not os.path.isabs(directory):
                    directory = os.path.join(PROJECT_DIR, directory)
                
                if not os.path.exists(directory):
                    return jsonify({'success': False, 'error': f'目录不存在: {directory}'})
                
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                list_files(directory=directory, log_file=log_file, stream=log_stream)
                
                return jsonify({'success': True, 'output': log_stream.getvalue()})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/group', methods=['POST'])
        def api_clean_group():
            try:
                data = request.get_json()
                directory = data.get('directory', '')
                if not directory or directory.strip() == '':
                    directory = PROJECT_DIR
                elif not os.path.isabs(directory):
                    directory = os.path.join(PROJECT_DIR, directory)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                clean_old_files(directory=directory, dry_run=dry_run, log_file=log_file, stream=log_stream)
                
                return jsonify({'success': True, 'output': log_stream.getvalue()})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/time', methods=['POST'])
        def api_clean_time():
            try:
                data = request.get_json()
                directory = data.get('directory', '')
                if not directory or directory.strip() == '':
                    directory = PROJECT_DIR
                elif not os.path.isabs(directory):
                    directory = os.path.join(PROJECT_DIR, directory)
                minutes = data.get('minutes', 5)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                clean_old_files_by_time(directory=directory, minutes=minutes, dry_run=dry_run, log_file=log_file, stream=log_stream)
                
                return jsonify({'success': True, 'output': log_stream.getvalue()})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/all', methods=['POST'])
        def api_clean_all():
            try:
                data = request.get_json()
                directory = data.get('directory', '')
                if not directory or directory.strip() == '':
                    directory = PROJECT_DIR
                elif not os.path.isabs(directory):
                    directory = os.path.join(PROJECT_DIR, directory)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')

                log_stream = io.StringIO()
                clean_all_files(directory=directory, dry_run=dry_run, log_file=log_file, stream=log_stream)

                output = log_stream.getvalue()
                response_data = json.dumps({'success': True, 'output': output}, ensure_ascii=False)
                return Response(response_data, mimetype='application/json')
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/png', methods=['POST'])
        def api_clean_png():
            try:
                data = request.get_json()
                directory = data.get('directory', '')
                if not directory or directory.strip() == '':
                    directory = PROJECT_DIR
                elif not os.path.isabs(directory):
                    directory = os.path.join(PROJECT_DIR, directory)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                clean_png_files(directory=directory, dry_run=dry_run, log_file=log_file, stream=log_stream)
                
                output = log_stream.getvalue()
                response_data = json.dumps({'success': True, 'output': output}, ensure_ascii=False)
                return Response(response_data, mimetype='application/json')
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/media', methods=['POST'])
        def api_clean_media():
            try:
                data = request.get_json()
                directory = data.get('directory', '')
                if not directory or directory.strip() == '':
                    directory = PROJECT_DIR
                elif not os.path.isabs(directory):
                    directory = os.path.join(PROJECT_DIR, directory)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                clean_media_files(directory=directory, dry_run=dry_run, log_file=log_file, stream=log_stream)
                
                output = log_stream.getvalue()
                response_data = json.dumps({'success': True, 'output': output}, ensure_ascii=False)
                return Response(response_data, mimetype='application/json')
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/version', methods=['GET'])
        def get_version():
            return jsonify({'version': get_version_from_readme()})

        @app.route('/api/email/config', methods=['GET'])
        def get_email_config():
            notifier = EmailNotifier()
            config = notifier.get_email_config()
            if config['smtp_password']:
                config['smtp_password'] = '******'
            return jsonify({'success': True, 'config': config})

        @app.route('/api/email/config', methods=['POST'])
        def save_email_config():
            try:
                data = request.get_json()
                notifier = EmailNotifier()
                notifier.save_email_config(
                    smtp_host=data.get('smtp_host', 'smtp.qq.com'),
                    smtp_port=int(data.get('smtp_port', 587)),
                    smtp_user=data.get('smtp_user', ''),
                    smtp_password=data.get('smtp_password', ''),
                    from_name=data.get('from_name', '公网IP监控'),
                    to_email=data.get('to_email', '980187223@qq.com')
                )
                return jsonify({'success': True, 'message': '邮件配置已保存'})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/email/test', methods=['POST'])
        def test_email():
            try:
                data = request.get_json()
                test_notifier = EmailNotifier()
                test_notifier.save_email_config(
                    smtp_host=data.get('smtp_host', 'smtp.qq.com'),
                    smtp_port=int(data.get('smtp_port', 587)),
                    smtp_user=data.get('smtp_user', ''),
                    smtp_password=data.get('smtp_password', ''),
                    from_name=data.get('from_name', '公网IP监控'),
                    to_email=data.get('to_email', '980187223@qq.com')
                )
                success = test_notifier.send_tunnel_notification('https://test.example.com', 'test')
                if success:
                    return jsonify({'success': True, 'message': '测试邮件发送成功'})
                else:
                    return jsonify({'success': False, 'error': '请先启用邮件通知'})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/server/info', methods=['GET'])
        def get_server_info():
            port = args.port
            
            # 获取局域网 IP
            lan_ip = None
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                lan_ip = s.getsockname()[0]
                s.close()
            except:
                pass
            
            return jsonify({
                'success': True,
                'local_url': f'http://127.0.0.1:{port}',
                'lan_url': f'http://{lan_ip}:{port}' if lan_ip else None,
                'lan_ip': lan_ip,
                'port': port,
                'version': get_version_from_readme()
            })

        tunnel_process = None
        tunnel_url = None
        tunnel_auto_restart = True
        tunnel_restart_thread = None
        tunnel_last_error = None
        tunnel_restart_count = 0
        tunnel_restart_delay = 1
        tunnel_heartbeat_thread = None
        tunnel_last_heartbeat = 0
        tunnel_heartbeat_failed = False
        tunnel_need_restart = False
        tunnel_daemon_started = False
        tunnel_type = 'hostc'
        email_notifier = EmailNotifier()
        old_tunnel_url = None
        tunnel_consecutive_failures = 0
        tunnel_max_consecutive_failures = 5
        tunnel_backoff_delay = 5
        last_email_sent_time = 0
        email_cooldown = 60
        email_fail_count = 0
        email_max_fail_count = 3
        email_fail_cooldown = 300
        last_email_sent_url = None
        pending_email_url = None
        
        def send_tunnel_notification(new_url, event_type='new'):
            global last_email_sent_time, email_fail_count, last_email_sent_url, pending_email_url
            
            current_time = time.time()
            
            if email_fail_count >= email_max_fail_count:
                if current_time - last_email_sent_time < email_fail_cooldown:
                    print(f"[Email] 邮件发送失败次数过多 ({email_fail_count}次)，暂停发送 {email_fail_cooldown} 秒")
                    return
                else:
                    print(f"[Email] 邮件发送失败冷却期已过，重置失败计数")
                    email_fail_count = 0
            
            remaining_cooldown = email_cooldown - (current_time - last_email_sent_time)
            
            if current_time - last_email_sent_time < email_cooldown:
                if new_url != last_email_sent_url:
                    pending_email_url = new_url
                    print(f"[Email] 邮件发送冷却中，距离上次发送仅 {int(current_time - last_email_sent_time)} 秒，已记录待发送URL: {new_url}")
                else:
                    print(f"[Email] 邮件发送冷却中，距离上次发送仅 {int(current_time - last_email_sent_time)} 秒")
                return
            
            last_email_sent_url = new_url
            pending_email_url = None
            
            def send_with_retry():
                global last_email_sent_time, email_fail_count, last_email_sent_url
                try:
                    print(f"[Email] 准备发送邮件通知: {new_url} (事件类型: {event_type})")
                    success = email_notifier.send_tunnel_notification(new_url, event_type)
                    if success:
                        last_email_sent_time = time.time()
                        email_fail_count = 0
                        last_email_sent_url = new_url
                        print(f"[Email] 邮件发送成功")
                    else:
                        email_fail_count += 1
                        print(f"[Email] 邮件发送失败，当前失败次数: {email_fail_count}")
                except Exception as e:
                    email_fail_count += 1
                    print(f"[Email] 发送邮件异常: {e}，当前失败次数: {email_fail_count}")
            
            threading.Thread(target=send_with_retry, daemon=True).start()
        
        def check_and_send_pending_email():
            global pending_email_url, last_email_sent_time, email_fail_count, last_email_sent_url
            current_time = time.time()
            if pending_email_url and (current_time - last_email_sent_time) >= email_cooldown:
                url_to_send = pending_email_url
                pending_email_url = None
                last_email_sent_url = url_to_send
                print(f"[Email] 冷却期已过，发送待发邮件: {url_to_send}")
                def send_pending():
                    global last_email_sent_time, email_fail_count, last_email_sent_url
                    try:
                        success = email_notifier.send_tunnel_notification(url_to_send, 'pending')
                        if success:
                            last_email_sent_time = time.time()
                            email_fail_count = 0
                            last_email_sent_url = url_to_send
                            print(f"[Email] 待发邮件发送成功")
                        else:
                            email_fail_count += 1
                            pending_email_url = url_to_send
                    except Exception as e:
                        email_fail_count += 1
                        pending_email_url = url_to_send
                        print(f"[Email] 待发邮件发送异常: {e}")
                threading.Thread(target=send_pending, daemon=True).start()
        
        def verify_url(url, timeout=10):
            try:
                req = urllib.request.Request(url, method='HEAD')
                req.add_header('User-Agent', 'hostc-verify/1.0')
                urllib.request.urlopen(req, timeout=timeout)
                return True
            except Exception as e:
                return False
        
        def send_heartbeat():
            global tunnel_last_heartbeat, tunnel_heartbeat_failed
            web_url = PathManager.get_public_url_from_web_log()
            if not web_url:
                tunnel_heartbeat_failed = True
                return False
            try:
                req = urllib.request.Request(web_url, method='HEAD')
                req.add_header('User-Agent', 'hostc-heartbeat/1.0')
                urllib.request.urlopen(req, timeout=15)
                tunnel_last_heartbeat = time.time()
                tunnel_heartbeat_failed = False
                return True
            except Exception as e:
                tunnel_heartbeat_failed = True
                return False
        
        def heartbeat_loop():
            global tunnel_process, tunnel_auto_restart, tunnel_need_restart, tunnel_url, tunnel_consecutive_failures
            consecutive_failures = 0
            max_consecutive_failures = 10
            heartbeat_interval = 5  # 心跳间隔5秒
            last_log_time = 0
            while tunnel_auto_restart:
                # 从 web_output.log 获取 URL（唯一来源）
                web_url = PathManager.get_public_url_from_web_log()
                is_tunnel_running = False
                
                if web_url:
                    try:
                        if verify_url(web_url, timeout=5):
                            is_tunnel_running = True
                        else:
                            if time.time() - last_log_time > 60:
                                print(f"[Tunnel] URL验证失败: {web_url}")
                                last_log_time = time.time()
                            tunnel_need_restart = True
                    except Exception as e:
                        if time.time() - last_log_time > 60:
                            print(f"[Tunnel] URL验证异常: {e}")
                            last_log_time = time.time()
                        tunnel_need_restart = True
                
                if is_tunnel_running:
                    success = send_heartbeat()
                    if not success:
                        consecutive_failures += 1
                        if consecutive_failures >= max_consecutive_failures:
                            print(f"[Tunnel] 心跳连续失败 {consecutive_failures} 次，标记需要重启")
                            tunnel_need_restart = True
                            last_log_time = time.time()
                        elif consecutive_failures == 1 and time.time() - last_log_time > 60:
                            print(f"[Tunnel] 心跳检测异常: 网络连接不稳定 ({consecutive_failures}/{max_consecutive_failures})")
                            last_log_time = time.time()
                    else:
                        if consecutive_failures > 0:
                            print(f"[Tunnel] 心跳恢复，当前连续失败次数: {consecutive_failures}")
                            last_log_time = time.time()
                        consecutive_failures = 0
                        
                        check_and_send_pending_email()
                        
                        # 确保 tunnel_url.txt 和 web_output.log 一致
                        if web_url:
                            tunnel_url_file = PathManager.get_tunnel_url_file()
                            try:
                                with open(tunnel_url_file, 'w', encoding='utf-8') as tf:
                                    port_match = re.search(r'--port\s+(\d+)', ' '.join(sys.argv))
                                    local_port = port_match.group(1) if port_match else '8888'
                                    tf.write(f"Public URL: {web_url}\n")
                                    tf.write(f"Local URL: http://127.0.0.1:{local_port}/\n")
                                    tf.write(f"Tunnel: {web_url.split('//')[1].split('.')[0]}\n")
                            except Exception as e:
                                pass
                time.sleep(heartbeat_interval)
        
        def auto_start_tunnel(force_restart=False):
            global tunnel_process, tunnel_url, tunnel_auto_restart, tunnel_restart_thread, tunnel_restart_count, tunnel_last_error, tunnel_need_restart, tunnel_daemon_started, tunnel_type, old_tunnel_url

            # 检查是否有 hostc 进程在运行
            has_hostc_process = Environment.check_process_running('node.exe' if Environment.IS_WINDOWS else 'hostc')
            
            # 从 web_output.log 检查是否有有效 URL（统一入口）
            web_url = PathManager.get_public_url_from_web_log()
            
            # 如果有 hostc 进程在运行且 web_output.log 有有效 URL，复用现有隧道
            if has_hostc_process and web_url and not force_restart:
                if verify_url(web_url):
                    print(f"[Tunnel] 复用已有隧道: {web_url}")
                    sys.stdout.flush()
                    tunnel_url = web_url
                    old_tunnel_url = web_url
                    return {'success': True, 'url': tunnel_url, 'message': f'复用已有隧道，URL: {tunnel_url}'}
            
            try:
                port = args.port
                tunnel_url = None
                url_ready = False
                tunnel_last_error = None
                tunnel_auto_restart = True
                
                print("[Tunnel] 启动 hostc 隧道")
                sys.stdout.flush()
                tunnel_type = 'hostc'
                
                # 清理所有旧的 node.exe 进程
                Environment.kill_process_by_name('node.exe' if Environment.IS_WINDOWS else 'hostc')
                
                tunnel_process = subprocess.Popen(
                    f'npx hostc@latest {port} --local-host 127.0.0.1',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=0,
                    shell=True,
                    creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0) if Environment.IS_WINDOWS else 0
                )

                def read_output():
                    global tunnel_url, url_ready, old_tunnel_url, tunnel_consecutive_failures
                    if not tunnel_process or not tunnel_process.stdout:
                        return
                    
                    buffer = ''
                    while True:
                        if tunnel_process is None:
                            break
                        if tunnel_process.poll() is not None:
                            print(f"[Tunnel] hostc进程已退出")
                            sys.stdout.flush()
                            break
                        
                        try:
                            char = tunnel_process.stdout.read(1)
                            if char:
                                buffer += char
                                # 查找 URL
                                match = re.search(r'(https://[a-zA-Z0-9_-]+\.hostc\.dev)', buffer)
                                if match:
                                    file_url = match.group(1).rstrip('/')
                                    if file_url and file_url != tunnel_url:
                                        print(f"[Tunnel] 从 hostc 输出获取到URL: {file_url}")
                                        
                                        # 同时写入 web_output.log 和 tunnel_url.txt
                                        web_output_file = PathManager.get_web_output_file()
                                        tunnel_url_file = PathManager.get_tunnel_url_file()
                                        try:
                                            with open(web_output_file, 'w', encoding='utf-8') as wf:
                                                wf.write(f"Public URL: {file_url}\n")
                                            print(f"[Tunnel] 已写入 web_output.log")
                                        except Exception as e:
                                            print(f"[Tunnel] 写入 web_output.log 失败: {e}")
                                        
                                        try:
                                            with open(tunnel_url_file, 'w', encoding='utf-8') as tf:
                                                tf.write(f"Public URL: {file_url}\n")
                                                tf.write(f"Local URL: http://127.0.0.1:{port}/\n")
                                                tf.write(f"Tunnel: {file_url.split('//')[1].split('.')[0]}\n")
                                            print(f"[Tunnel] 已写入 tunnel_url.txt")
                                        except Exception as e:
                                            print(f"[Tunnel] 写入 tunnel_url.txt 失败: {e}")
                                        
                                        tunnel_url = file_url
                                        url_ready = True
                                        tunnel_consecutive_failures = 0
                                        old_tunnel_url = file_url
                                        send_tunnel_notification(tunnel_url, 'new')
                                        print(f"[Tunnel] URL已就绪")
                                        sys.stdout.flush()
                                        return
                                
                                # 保持 buffer 不超过 1000 字符
                                if len(buffer) > 1000:
                                    buffer = buffer[-500:]
                            else:
                                time.sleep(0.1)
                        except Exception as e:
                            time.sleep(0.1)

                read_thread = threading.Thread(target=read_output, daemon=True)
                read_thread.start()
                
                # 等待 read_output 线程完成（获取到 URL 或超时）
                read_thread.join(timeout=30)
                
                if tunnel_url:
                    print(f"[Tunnel] 隧道启动成功: {tunnel_url}")
                    return {'success': True, 'url': tunnel_url, 'message': f'隧道已启动，URL: {tunnel_url}'}
                else:
                    print(f"[Tunnel] 启动超时，未获取到URL")
                    return {'success': False, 'url': None, 'error': '启动超时，未获取到URL'}
            except Exception as e:
                return {'success': False, 'error': str(e)}
        
        def restart_tunnel():
            global tunnel_process, tunnel_url, tunnel_auto_restart, tunnel_last_error, tunnel_restart_count, tunnel_need_restart, old_tunnel_url, tunnel_consecutive_failures, tunnel_backoff_delay
            
            consecutive_restart_attempts = 0
            max_consecutive_restarts = 3
            restart_cooldown = 60
            restart_wait_start = None  # 重启等待开始时间
            
            while tunnel_auto_restart:
                # 从 web_output.log 获取公网地址（统一入口）
                web_url = PathManager.get_public_url_from_web_log()
                
                # 检查是否有 hostc 进程在运行
                has_hostc_process = Environment.check_process_running('node.exe' if Environment.IS_WINDOWS else 'hostc')
                
                # 检查 URL 是否可用
                is_url_valid = False
                if web_url:
                    try:
                        if verify_url(web_url):
                            is_url_valid = True
                    except:
                        pass
                
                # 状态判断
                if has_hostc_process and is_url_valid:
                    # 一切正常
                    restart_wait_start = None  # 重置等待状态
                    tunnel_need_restart = False
                    time.sleep(1)
                    continue
                
                # 需要等待或重启
                if restart_wait_start is None:
                    restart_wait_start = time.time()
                    elapsed = 0
                else:
                    elapsed = time.time() - restart_wait_start
                
                # 等待时间阈值：首次等待 30 秒，之后等待 60 秒
                wait_threshold = 30 if elapsed < 60 else 60
                
                if elapsed < wait_threshold:
                    # 等待期间，不打印日志避免刷屏
                    time.sleep(2)
                    continue
                
                # 超过等待时间，触发重启
                restart_wait_start = None
                tunnel_restart_count += 1
                print(f"[Tunnel] 检测到问题，尝试重启 (第{tunnel_restart_count}次)")
                print(f"[Tunnel] - hostc进程: {'运行中' if has_hostc_process else '未运行'}")
                print(f"[Tunnel] - 公网URL: {web_url if web_url else '无'}")
                print(f"[Tunnel] - URL有效: {'是' if is_url_valid else '否'}")
                sys.stdout.flush()
                
                # 清理所有 hostc/node 进程
                Environment.kill_process_by_name('node.exe' if Environment.IS_WINDOWS else 'hostc')
                
                # 重置状态
                if tunnel_process:
                    try:
                        tunnel_process.terminate()
                        tunnel_process.wait(timeout=2)
                    except:
                        try:
                            tunnel_process.kill()
                        except:
                            pass
                
                tunnel_process = None
                tunnel_url = None
                old_tunnel_url = None
                
                time.sleep(tunnel_restart_delay)
                
                if not tunnel_auto_restart:
                    break
                
                try:
                    result = auto_start_tunnel()
                    
                    if result['success']:
                        new_url = result.get('url')
                        if new_url:
                            # URL变化时发送通知，让用户知道新地址
                            if old_tunnel_url and old_tunnel_url != new_url:
                                print(f"[Tunnel] 隧道URL已变化: {old_tunnel_url} -> {new_url}")
                                sys.stdout.flush()
                                send_tunnel_notification(new_url, 'update')
                            
                            tunnel_last_error = None
                            tunnel_need_restart = False
                            tunnel_consecutive_failures = 0
                            consecutive_restart_attempts = 0
                            tunnel_restart_count = 0
                            print(f"[Tunnel] 隧道重启成功! URL: {tunnel_url}")
                            sys.stdout.flush()
                        else:
                            print(f"[Tunnel] 隧道启动成功但URL未就绪，继续等待...")
                            sys.stdout.flush()
                    else:
                        tunnel_last_error = result.get('error', '启动失败')
                        print(f"[Tunnel] 重启失败: {tunnel_last_error}")
                        sys.stdout.flush()
                        
                except Exception as e:
                    tunnel_last_error = str(e)
                    print(f"[Tunnel] 重启失败: {e}")
                    sys.stdout.flush()
        
        @app.route('/api/tunnel/start', methods=['POST'])
        def start_tunnel():
            global tunnel_process, tunnel_url, tunnel_auto_restart, tunnel_restart_thread, tunnel_restart_count, tunnel_last_error, tunnel_need_restart, tunnel_daemon_started, tunnel_type, tunnel_consecutive_failures

            tunnel_need_restart = False
            tunnel_consecutive_failures = 0
            
            if tunnel_process and tunnel_process.poll() is None:
                return jsonify({'success': True, 'url': tunnel_url, 'message': '隧道已在运行'})

            result = auto_start_tunnel()
            if result['success']:
                return jsonify(result)
            else:
                return jsonify({'success': False, 'error': result.get('error', '启动失败')})

        last_url_invalid_log_time = 0  # 上次打印URL不可用日志的时间
        
        @app.route('/api/tunnel/status', methods=['GET'])
        def tunnel_status():
            global tunnel_process, tunnel_url, tunnel_auto_restart, tunnel_restart_count, tunnel_last_error, tunnel_last_heartbeat, tunnel_daemon_started, tunnel_restart_thread, tunnel_heartbeat_thread, tunnel_need_restart, last_url_invalid_log_time
            
            heartbeat_str = datetime.fromtimestamp(tunnel_last_heartbeat).strftime('%Y-%m-%d %H:%M:%S') if tunnel_last_heartbeat > 0 else None
            
            tunnel_type = 'hostc'
            
            # 从 web_output.log 读取公网地址（唯一来源）
            web_url = PathManager.get_public_url_from_web_log()
            url_valid = False
            
            # 检测是否有 hostc 进程在运行
            process_running = Environment.check_process_running('node.exe' if Environment.IS_WINDOWS else 'hostc')
            
            # 验证 URL 是否可用
            if web_url:
                try:
                    if verify_url(web_url, timeout=5):
                        url_valid = True
                    else:
                        # URL不可用，触发自动重启
                        if time.time() - last_url_invalid_log_time > 60:
                            print(f"[Tunnel] 检测到URL不可用，触发自动重启: {web_url}")
                            last_url_invalid_log_time = time.time()
                        tunnel_need_restart = True
                except Exception as e:
                    print(f"[Tunnel] 验证URL失败: {e}")
                    tunnel_need_restart = True
            
            # 判断隧道是否在运行
            is_running = process_running and url_valid
            
            # 确保守护线程在运行
            if tunnel_restart_thread is None or not tunnel_restart_thread.is_alive():
                if not tunnel_daemon_started:
                    tunnel_daemon_started = True
                    print("[Tunnel] 启动自动重启守护进程")
                tunnel_restart_thread = threading.Thread(target=restart_tunnel, daemon=True)
                tunnel_restart_thread.start()
            if tunnel_heartbeat_thread is None or not tunnel_heartbeat_thread.is_alive():
                tunnel_heartbeat_thread = threading.Thread(target=heartbeat_loop, daemon=True)
                tunnel_heartbeat_thread.start()
                print("[Tunnel] 启动心跳守护进程")
            
            # 返回状态 - 统一使用 web_url
            return jsonify({
                'running': is_running,
                'url': web_url if url_valid else None,
                'url_valid': url_valid,
                'auto_restart': tunnel_auto_restart,
                'restart_count': tunnel_restart_count,
                'last_error': tunnel_last_error or ('URL无效，正在重启...' if tunnel_need_restart else None),
                'last_heartbeat': heartbeat_str,
                'tunnel_type': tunnel_type
            })

        # 初始化日志输出到 web_output.log
        setup_web_logging()
        
        # 启动前获取一次局域网 IP 用于显示
        lan_ip_startup = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            lan_ip_startup = s.getsockname()[0]
            s.close()
        except:
            pass
        
        print("=" * 50)
        print("Szwego商品爬虫 - Web服务")
        print("=" * 50)
        print(f"访问地址: http://localhost:{args.port}")
        print(f"局域网地址: http://{lan_ip_startup}:{args.port}" if lan_ip_startup else "")
        print("[Tunnel] 正在自动启动隧道...")
        
        tunnel_result = auto_start_tunnel()
        if tunnel_result['success']:
            print(f"[Tunnel] 隧道启动成功: {tunnel_result.get('url', '')}")
        else:
            print(f"[Tunnel] 隧道启动失败: {tunnel_result.get('error', '未知错误')}")
        
        print("按 Ctrl+C 停止服务")
        print("=" * 50)
        
        @app.route('/<path:invalid_path>')
        def handle_invalid_path(invalid_path):
            if request.path.startswith('/dist/'):
                return "File not found", 404
            return index()
        
        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(os.path.join(PROJECT_DIR, 'dist', 'favicon'), 'favicon.ico')
        
        app.run(host='0.0.0.0', port=args.port, debug=False)
    else:
        main()