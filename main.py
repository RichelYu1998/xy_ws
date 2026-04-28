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
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

from flask import Flask, request, jsonify, send_file, Response


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
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
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
                file_stat = file.stat()
                mtime = file_stat.st_mtime
                download_time = datetime.fromtimestamp(mtime)

                name_without_ext = file.stem
                if '_' in name_without_ext:
                    group_key = name_without_ext.split('_')[0]
                else:
                    group_key = name_without_ext

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
        try:
            file_info['file'].unlink()
            deleted_count += 1
            deleted_size += file_info['size']
            logger.info(f"已删除: {file_info['file'].name} ({format_size(file_info['size'])})")
        except PermissionError:
            logger.error(f"删除失败（权限不足）: {file_info['file'].name}")
            failed_count += 1
        except FileNotFoundError:
            logger.warning(f"文件不存在（可能已被删除）: {file_info['file'].name}")
            failed_count += 1
        except Exception as e:
            logger.error(f"删除失败 {file_info['file'].name}: {e}")
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
        try:
            file_info['file'].unlink()
            deleted_count += 1
            deleted_size += file_info['size']
            logger.info(f"已删除: {file_info['file'].name} ({format_size(file_info['size'])})")
        except PermissionError:
            logger.error(f"删除失败（权限不足）: {file_info['file'].name}")
            failed_count += 1
        except FileNotFoundError:
            logger.warning(f"文件不存在（可能已被删除）: {file_info['file'].name}")
            failed_count += 1
        except Exception as e:
            logger.error(f"删除失败 {file_info['file'].name}: {e}")
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
    logger.info("=" * 60)

    directory = Path(directory)

    if not directory.exists():
        logger.error(f"目录不存在: {directory}")
        return

    matched_files = []
    logger.info("扫描文件中...")
    for file in directory.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            if ext in MEDIA_EXTENSIONS:
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

    logger.info("\n文件列表：")
    for i, file_info in enumerate(matched_files, 1):
        file_type = "图片" if file_info['is_image'] else "视频"
        download_time_str = file_info['download_time'].strftime('%Y-%m-%d %H:%M:%S')
        logger.info(
            f"{i:3d}. {file_info['file'].name} ({file_type}, {format_size(file_info['size'])}, 下载时间: {download_time_str})")

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
    total_size = sum(file.stat().st_size for file in files_to_delete)

    logger.info(f"找到 {total_files} 个文件和 {total_folders} 个文件夹")
    logger.info(f"  - 总大小: {format_size(total_size)}")

    if not files_to_delete and not folders_to_delete:
        logger.warning("没有需要删除的文件或文件夹")
        logger.info("清理完成")
        return

    logger.info(f"\n将删除 {total_files} 个文件和 {total_folders} 个文件夹")

    if files_to_delete:
        logger.info("\n将要删除的文件列表：")
        for i, file in enumerate(files_to_delete, 1):
            file_size = file.stat().st_size
            logger.info(f"{i:3d}. {file.name} ({format_size(file_size)})")

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
        try:
            file_size = file.stat().st_size
            file.unlink()
            deleted_files_count += 1
            deleted_size += file_size
            logger.info(f"已删除文件: {file.name} ({format_size(file_size)})")
        except PermissionError:
            logger.error(f"删除文件失败（权限不足）: {file.name}")
            failed_count += 1
        except FileNotFoundError:
            logger.warning(f"文件不存在（可能已被删除）: {file.name}")
            failed_count += 1
        except Exception as e:
            logger.error(f"删除文件失败 {file.name}: {e}")
            failed_count += 1

    for folder in folders_to_delete:
        try:
            shutil.rmtree(folder)
            deleted_folders_count += 1
            logger.info(f"已删除文件夹: {folder.name}")
        except PermissionError:
            logger.error(f"删除文件夹失败（权限不足）: {folder.name}")
            failed_count += 1
        except FileNotFoundError:
            logger.warning(f"文件夹不存在（可能已被删除）: {folder.name}")
            failed_count += 1
        except Exception as e:
            logger.error(f"删除文件夹失败 {folder.name}: {e}")
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
        try:
            file_info['file'].unlink()
            deleted_count += 1
            deleted_size += file_info['size']
            logger.info(f"已删除: {file_info['file'].name} ({format_size(file_info['size'])})")
        except PermissionError:
            logger.error(f"删除失败（权限不足）: {file_info['file'].name}")
            failed_count += 1
        except FileNotFoundError:
            logger.warning(f"文件不存在（可能已被删除）: {file_info['file'].name}")
            failed_count += 1
        except Exception as e:
            logger.error(f"删除失败 {file_info['file'].name}: {e}")
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
        try:
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
        except PermissionError:
            logger.error(f"删除失败（权限不足）: {file_info['file'].name}")
            failed_count += 1
        except FileNotFoundError:
            logger.warning(f"文件不存在（可能已被删除）: {file_info['file'].name}")
            failed_count += 1
        except Exception as e:
            logger.error(f"删除失败 {file_info['file'].name}: {e}")
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

VERSION = "2.5.21"

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_PYTHON = os.path.join(PROJECT_DIR, '.venv', 'bin', 'python')

app = Flask(__name__)

processes = {}
tasks = {}

def run_command_background(task_id, command):
    try:
        tasks[task_id]['status'] = 'running'
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            cwd=PROJECT_DIR,
            text=True
        )
        processes[task_id] = process
        
        stdout_lines = []
        for line in iter(process.stdout.readline, ''):
            if line:
                stdout_lines.append(line)
                tasks[task_id]['output'] = ''.join(stdout_lines)
        
        process.wait()
        tasks[task_id]['returncode'] = process.returncode
        tasks[task_id]['status'] = 'completed'
    except Exception as e:
        tasks[task_id]['error'] = str(e)
        tasks[task_id]['status'] = 'error'


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


class PathManager:
    """路径管理类，统一处理跨系统路径问题"""
    
    @staticmethod
    def get_config_dir():
        """获取配置文件目录"""
        return 'config'
    
    @staticmethod
    def get_file_dir():
        """获取输出文件目录"""
        return 'file'
    
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
    def ensure_dirs_exist():
        """确保所有必要的目录存在"""
        dirs = [PathManager.get_config_dir(), PathManager.get_file_dir()]
        for dir_path in dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)


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
    def get_latest_json_file(directory=None, pattern='微购相册'):
        try:
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
        except Exception as e:
            print(f'获取最新JSON文件失败: {e}')
            return None

    @staticmethod
    def get_today_json_files(directory=None, pattern='微购相册'):
        """
        获取用于对比的两个JSON文件
        优先级：
        1. 当天的缓存文件和最新文件
        2. 当天的最新文件和前一天的文件
        3. 最新的两个文件
        """
        try:
            directory = directory or PathManager.get_file_dir()
            if not os.path.exists(directory):
                print(f'目录 {directory} 不存在')
                return None, None
            
            today = datetime.now().strftime('%Y%m%d')
            
            # 获取所有符合条件的JSON文件
            all_json_files = []
            for file in os.listdir(directory):
                if file.endswith('.json') and pattern in file and '_cache' not in file:
                    file_path = os.path.join(directory, file)
                    all_json_files.append((file_path, os.path.getmtime(file_path)))
            
            if len(all_json_files) < 1:
                print(f'未找到包含"{pattern}"的JSON文件')
                return None, None
            
            # 按修改时间排序（最新的在前）
            all_json_files.sort(key=lambda x: x[1], reverse=True)
            latest_file = all_json_files[0][0]
            
            # 检查是否存在当天的缓存文件
            cache_file = PathManager.get_cache_file_path(today)
            if os.path.exists(cache_file):
                print(f'找到当天缓存文件: {cache_file}')
                print(f'找到当天最新文件: {latest_file}')
                return latest_file, cache_file
            
            # 如果没有缓存文件，检查当天是否有多个文件
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
            
            # 如果当天只有一个文件，尝试找前一天的文件
            if len(all_json_files) >= 2:
                print(f'当天只有一个文件，使用最新文件和次新文件对比')
                print(f'最新文件: {latest_file}')
                print(f'次新文件: {all_json_files[1][0]}')
                return latest_file, all_json_files[1][0]
            
            print(f'只找到一个文件: {latest_file}')
            return latest_file, None
            
        except Exception as e:
            print(f'获取JSON文件失败: {e}')
            return None, None

    @staticmethod
    def list_files(directory=None, pattern=None):
        try:
            directory = directory or PathManager.get_file_dir()
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
    def get_chrome_path():
        """获取Chrome浏览器路径，支持Windows、Mac和Linux系统"""
        system = platform.system()
        chrome_path = None
        
        if system == 'Windows':
            if os.path.exists(r'C:\Program Files\Google\Chrome\Application\chrome.exe'):
                chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        elif system == 'Darwin':  # Mac系统返回的是'Darwin'，不是'Mac'
            if os.path.exists('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'):
                chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        elif system == 'Linux':
            # 优先检测 /chrome-linux64 目录下的Chrome
            if os.path.exists('/chrome-linux64/chrome'):
                chrome_path = '/chrome-linux64/chrome'
            elif os.path.exists('/usr/bin/google-chrome'):
                chrome_path = '/usr/bin/google-chrome'
        
        return chrome_path
    
    @staticmethod
    def get_browser_args():
        """获取浏览器启动参数，根据系统类型返回不同的参数"""
        system = platform.system()
        browser_args = ['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled']
        
        if system == 'Windows':
            browser_args.append('--disable-gpu')
        elif system == 'Linux':
            browser_args.extend(['--disable-gpu', '--disable-dev-shm-usage'])
        
        return browser_args
    
    @staticmethod
    def get_user_agent():
        """获取用户代理字符串，根据系统类型返回不同的UA"""
        system = platform.system()
        
        if system == 'Windows':
            return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        elif system == 'Darwin':
            return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        elif system == 'Linux':
            return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        else:
            return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

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
            try:
                close_button = await page.query_selector(selector, timeout=1000)
                if close_button:
                    await close_button.click(timeout=1000)
                    print(f'关闭了弹窗: {selector}')
                    await asyncio.sleep(wait_time)
            except Exception:
                pass

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
            try:
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
                try:
                    await asyncio.wait_for(
                        page.evaluate(f'window.scrollBy(0, {scroll_distance})' if scroll_attempts < 10 else 'window.scrollTo(0, document.body.scrollHeight)'),
                        timeout=3.0
                    )
                except asyncio.TimeoutError:
                    print('滚动操作超时，尝试继续...')
                
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
            except Exception as e:
                print(f'滚动时出错: {e}')
                import traceback
                traceback.print_exc()
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
        
        import os
        cookie_file = os.path.join(os.path.dirname(__file__), 'config', 'cookies.json')
        cookies = []
        if os.path.exists(cookie_file):
            try:
                with open(cookie_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                print(f'读取到 {len(cookies)} 个cookie')
            except Exception as e:
                print(f'读取cookie失败: {e}')
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
                        print(f'  解析失败: {e}')
                        break
                else:
                    print(f'  请求失败: {response.status}')
                    break
            except Exception as e:
                print(f'  请求异常: {e}')
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
            import traceback
            traceback.print_exc()
            return []

    async def fetch_all_products_via_api(self, page):
        """通过API获取所有商品数据"""
        import os
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
            
            import base64
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
                import shutil
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
                FileManager.write_json(cookie_file, cookies)
                print(f'Cookie已保存到 {cookie_file}')
                print(f'Cookie保存耗时: {time.time() - save_cookie_start:.2f}秒')
                
                close_start = time.time()
                await browser.close()
                print(f'浏览器关闭耗时: {time.time() - close_start:.2f}秒')
                
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
                    number_match = re.match(r'^([A-Za-z0-9]{3,10})$', cell_str)
                    if number_match:
                        stock_numbers.append(cell_str)
            
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
            print(f'保存重复日志失败: {e}')
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
            print(f'对比失败: {e}')
            import traceback
            traceback.print_exc()
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
            
            excel_stock_numbers = self.load_excel_data()
            if not excel_stock_numbers:
                print('无法从Excel文件读取货号')
                return False
            
            json_set, excel_set = set(json_stock_numbers), set(excel_stock_numbers)
            high_price_extra_in_json = [n for n in high_price_stock_numbers if n in json_set - excel_set]
            
            result = self.compare_stock_numbers(json_stock_numbers, excel_stock_numbers, high_price_extra_in_json)
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_str = datetime.now().strftime('%Y%m%d')
            
            data_change = "数据无变化" if result['missing_count'] == 0 and result['extra_in_json_count'] == 0 else f"数据有变化：缺失 {result['missing_count']} 个货号，多余 {result['extra_in_json_count']} 个货号"
            
            added_products = [self._get_product_detail(p) for p in products if p.get('货号') and p.get('货号') not in excel_set] if products else []
            
            removed_products = []
            prev_file = FileManager.get_latest_json_file('微购相册')
            if prev_file and prev_file != latest_json_file:
                old_data = FileManager.read_json(prev_file)
                if old_data and isinstance(old_data, dict):
                    removed_products = [self._get_product_detail(item) for item in old_data.get('商品列表', []) if item.get('货号') and item.get('货号') not in json_set]
            
            diff_data = {
                'timestamp': timestamp,
                'date': date_str,
                'json_file': os.path.basename(latest_json_file),
                'excel_file': os.path.basename(self.excel_file) if self.excel_file else 'None',
                'comparison': {
                    'missing_description': '微购相册比本地表格多出的序列号仅供参考',
                    'existing_description': '本地表格比微购相册上多的序列号，请仔细核对后删除多出的地方',
                    'extra_in_json_description': '微购相册比本地表格多出的序列号',
                    'high_price_extra_in_json': high_price_extra_in_json,
                    'high_price_extra_in_json_count': len(high_price_extra_in_json),
                    'high_price_extra_in_json_description': '只在JSON中存在但不在Excel中的售价>=599的货号',
                    **result
                },
                'result_message': self.get_result_message(result, []),
                'data_change': data_change,
                '新增商品': added_products,
                '新增商品数量': len(added_products),
                '删除商品': removed_products,
                '删除商品数量': len(removed_products)
            }
            
            self._save_diff_log(date_str, diff_data)
            self._add_high_price_info_to_json(latest_json_file, json_data, high_price_extra_in_json)
            self._add_diff_to_json_summary(latest_json_file, json_data, diff_data)
            
            self.print_comparison_result(result, [])
            return True
        except Exception as e:
            print(f'对比失败: {e}')
            import traceback
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
        
        if not FileManager.file_exists('config/config.json'):
            print('⚠️  警告: 配置文件不存在 (config/config.json)')
            print('请先配置 config/config.json 文件')
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
            import platform
            import os
            
            venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.venv', 'bin', 'python')
            if platform.system() == 'Windows':
                venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.venv', 'Scripts', 'python.exe')
            
            print('\n正在启动Web服务...')
            print('访问地址: http://localhost:8888')
            print('按 Ctrl+C 停止服务\n')
            
            os.system(f'"{venv_python}" main.py --web')
        
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
        cookie_file = PathManager.get_cookie_file()
        is_valid, cookies = CookieValidator.validate_and_prompt(cookie_file)
        
        if not is_valid:
            print('\n❌ Cookie验证失败，无法运行爬虫')
            print('请先运行"更新Cookie"功能')
            input('按回车键继续...')
            return
        
        scraper = WegoScraper()
        asyncio.run(scraper.run())
    except Exception as e:
        print(f'运行爬虫时出错: {e}')
        import traceback
        traceback.print_exc()
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
    
    try:
        from playwright.async_api import async_playwright
        import asyncio
        
        async def get_cookie():
            async with async_playwright() as p:
                browser_args = WegoScraper.get_browser_args()
                chrome_path = WegoScraper.get_chrome_path()
                
                print(f'检测到系统: {platform.system()}')
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
                
                # 加载现有Cookie
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
                
                # 等待页面加载完成
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
                
                # 自动检测登录状态
                start_time = time.time()
                timeout = 300  # 5分钟超时
                login_detected = False
                
                while time.time() - start_time < timeout:
                    # 检查是否已登录
                    try:
                        # 检查Cookie中是否有认证信息
                        cookies = await context.cookies()
                        auth_cookies = [c for c in cookies if 'token' in c['name'].lower() or 'session' in c['name'].lower() or 'auth' in c['name'].lower()]
                        
                        if auth_cookies:
                            print('✓ 检测到登录成功，自动关闭浏览器...')
                            login_detected = True
                            break
                    except:
                        pass
                    
                    # 如果未检测到登录状态，继续等待
                    await asyncio.sleep(5)
                    elapsed = int(time.time() - start_time)
                    print(f'等待登录中... ({elapsed}秒)')
                
                if not login_detected:
                    print('⚠️ 登录超时，尝试获取当前Cookie')
                
                # 获取Cookie
                cookies = await context.cookies()
                szwego_cookies = [cookie for cookie in cookies if 'szwego.com' in cookie['domain']]
                
                FileManager.write_json(cookie_file, szwego_cookies)
                
                print(f'✓ Cookie已保存到 {cookie_file}')
                print(f'✓ 共保存 {len(szwego_cookies)} 个Cookie')
                
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
        
        asyncio.run(get_cookie())
        print('\n✓ Cookie更新完成')
        
    except Exception as e:
        print(f'✗ Cookie更新失败: {e}')
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Szwego商品爬虫')
    parser.add_argument('--web', action='store_true', help='启动Web服务模式')
    parser.add_argument('--port', type=int, default=8888, help='Web服务端口 (默认8888)')
    args = parser.parse_args()
    
    if args.web:
        @app.route('/')
        def index():
            with open('index.html', 'r', encoding='utf-8') as f:
                content = f.read()
            response = Response(content, mimetype='text/html')
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response

        @app.route('/run', methods=['POST'])
        def run_command():
            data = request.get_json()
            command = data.get('command', '')
            if not command:
                return jsonify({'error': '命令不能为空'}), 400
            
            system = platform.system()
            if command.startswith('python '):
                if system == 'Windows':
                    command = command.replace('python ', VENV_PYTHON + ' ', 1)
                else:
                    command = command.replace('python ', VENV_PYTHON + ' ', 1)
            if command.startswith('python3 '):
                command = command.replace('python3 ', VENV_PYTHON + ' ', 1)
            
            task_id = str(uuid.uuid4())[:8]
            tasks[task_id] = {'command': command, 'status': 'starting', 'output': '', 'returncode': None, 'error': None}
            thread = threading.Thread(target=run_command_background, args=(task_id, command))
            thread.start()
            return jsonify({'success': True, 'task_id': task_id, 'message': f'命令已启动 (系统: {system})'})

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
            import glob
            cookie_file = os.path.join(PROJECT_DIR, 'config', 'cookies.json')
            system = platform.system()
            if not os.path.exists(cookie_file):
                return jsonify({'error': 'Cookie文件不存在', 'valid': False, 'system': system}), 404
            try:
                with open(cookie_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                token_cookie = next((c for c in cookies if c.get('name') == 'token'), None)
                if not token_cookie:
                    return jsonify({'error': '未找到token', 'valid': False, 'system': system}), 404
                expires = token_cookie.get('expires')
                if not expires:
                    return jsonify({'error': 'token无过期时间', 'valid': False, 'system': system}), 404
                import datetime
                expires_time = datetime.datetime.fromtimestamp(expires)
                hours_remaining = (expires_time - datetime.datetime.now()).total_seconds() / 3600
                return jsonify({'valid': True, 'expires': expires_time.strftime('%Y-%m-%d %H:%M:%S'), 'hours_remaining': round(hours_remaining, 1), 'expired': hours_remaining <= 0, 'system': system})
            except Exception as e:
                return jsonify({'error': str(e), 'valid': False}), 500

        @app.route('/api/sku/compare', methods=['GET'])
        def compare_sku():
            import glob
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
                        import re
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

        @app.route('/api/sku/compare/txt', methods=['GET'])
        def compare_sku_txt():
            import glob
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
                        import re
                        txt_stock_numbers = sorted(set(re.findall(r'\d+', content)))
                
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
                    'common_count': len(txt_set & json_set)
                }
                return jsonify(result)
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/sku/compare/excel', methods=['GET'])
        def compare_sku_excel():
            import glob
            try:
                json_files = glob.glob(os.path.join(PROJECT_DIR, 'file', '*微购相册*.json'))
                if not json_files:
                    return jsonify({'error': '没有找到JSON文件'}), 404
                latest_json = max(json_files, key=os.path.getmtime)
                
                with open(latest_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                products = data.get('商品列表', []) if isinstance(data, dict) else data
                json_stock_numbers = sorted([p.get('货号', '') for p in products if p.get('货号')])
                
                excel_file = None
                config_file = os.path.join(PROJECT_DIR, 'config', 'config.json')
                if os.path.exists(config_file):
                    with open(config_file, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                    excel_files = config.get('excel_files', [])
                    for path in excel_files:
                        expanded_path = os.path.expanduser(path)
                        if os.path.exists(expanded_path):
                            excel_file = expanded_path
                            break
                
                if excel_file is None:
                    excel_file = os.path.join(PROJECT_DIR, 'config', '本地商品表格.xlsx')
                
                excel_stock_numbers = []
                if os.path.exists(excel_file):
                    import pandas as pd
                    xls = pd.ExcelFile(excel_file)
                    
                    df = None
                    sheet_name = None
                    sku_column = None
                    
                    for sheet in xls.sheet_names:
                        temp_df = xls.parse(sheet)
                        
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
                        excel_stock_numbers = sorted([str(int(x)) if isinstance(x, float) and x == int(x) else str(x).strip() 
                                                     for x in df[sku_column].dropna() 
                                                     if str(x).strip() and str(x).strip() != 'nan' and str(x).strip() != '序列号'])
                    else:
                        return jsonify({'error': f'Excel文件中未找到"货号"或"序列号"列'}), 404
                else:
                    return jsonify({'error': f'Excel文件不存在: {excel_file}'}), 404
                
                json_set = set(json_stock_numbers)
                excel_set = set(excel_stock_numbers)
                
                json_sku_counts = {}
                for sku in json_stock_numbers:
                    json_sku_counts[sku] = json_sku_counts.get(sku, 0) + 1
                duplicate_skus = {sku: count for sku, count in json_sku_counts.items() if count > 1}
                
                high_price_count = 0
                for p in products:
                    price = p.get('售价', '')
                    if price:
                        try:
                            price_val = float(price.replace('¥', '').replace(',', ''))
                            if price_val >= 599:
                                high_price_count += 1
                        except:
                            pass
                
                result = {
                    'type': 'excel',
                    'json_file': os.path.basename(latest_json),
                    'input_count': len(excel_set),
                    'extra_count': len(json_set - excel_set),
                    'json_count': len(json_set),
                    'common_count': len(excel_set & json_set),
                    'duplicate_count': len(duplicate_skus),
                    'high_price_count': high_price_count,
                    'missing_in_json': sorted(list(excel_set - json_set)),
                    'extra_in_json': sorted(list(json_set - excel_set)),
                    'common': sorted(list(excel_set & json_set)),
                    'duplicates': duplicate_skus,
                    'missing_count': len(excel_set - json_set)
                }
                return jsonify(result)
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/products', methods=['GET'])
        def get_all_products():
            import glob
            import base64
            system = platform.system()
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
                for p in products:
                    try:
                        price = float(p.get('售价', '¥0').replace('¥', '').replace(',', ''))
                        if price >= 599:
                            high_price_products.append(p)
                    except:
                        pass
                return jsonify({'filename': os.path.basename(latest_file), 'total': len(products), 'products': products[:100], 'highPriceProducts': high_price_products[:500], 'highPriceCount': len(high_price_products), 'system': system})
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/product/search', methods=['GET'])
        def search_product():
            sku = request.args.get('sku', '').strip()
            if not sku:
                return jsonify({'error': '请提供货号'}), 400
            import glob
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
                        import base64
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
                                        media_result.append(base64.b64decode(b64_str).decode('utf-8'))
                                    except:
                                        media_result.append(b64_str)
                            else:
                                try:
                                    media_result = base64.b64decode(img_data).decode('utf-8')
                                except:
                                    media_result = img_data
                        p['图片'] = media_result
                        return jsonify({'found': True, 'product': p, 'filename': os.path.basename(latest_file), 'saved': True})
                return jsonify({'found': False, 'error': f'未找到货号为 {sku} 的商品'})
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @app.route('/api/clean/list', methods=['POST'])
        def api_clean_list():
            try:
                import io
                data = request.get_json()
                directory = data.get('directory', PROJECT_DIR)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                list_files(directory=directory, log_file=log_file, stream=log_stream)
                
                return jsonify({'success': True, 'output': log_stream.getvalue()})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/group', methods=['POST'])
        def api_clean_group():
            try:
                import io
                data = request.get_json()
                directory = data.get('directory', PROJECT_DIR)
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
                import io
                data = request.get_json()
                directory = data.get('directory', PROJECT_DIR)
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
                import io
                data = request.get_json()
                directory = data.get('directory', PROJECT_DIR)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                clean_all_files(directory=directory, dry_run=dry_run, log_file=log_file, stream=log_stream)
                
                return jsonify({'success': True, 'output': log_stream.getvalue()})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/png', methods=['POST'])
        def api_clean_png():
            try:
                import io
                data = request.get_json()
                directory = data.get('directory', PROJECT_DIR)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                clean_png_files(directory=directory, dry_run=dry_run, log_file=log_file, stream=log_stream)
                
                return jsonify({'success': True, 'output': log_stream.getvalue()})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        @app.route('/api/clean/media', methods=['POST'])
        def api_clean_media():
            try:
                import io
                data = request.get_json()
                directory = data.get('directory', PROJECT_DIR)
                dry_run = data.get('dry_run', False)
                log_file = os.path.join(directory, 'clean_files.log')
                
                log_stream = io.StringIO()
                clean_media_files(directory=directory, dry_run=dry_run, log_file=log_file, stream=log_stream)
                
                return jsonify({'success': True, 'output': log_stream.getvalue()})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        print("=" * 50)
        print("Szwego商品爬虫 - Web服务")
        print("=" * 50)
        print(f"访问地址: http://localhost:{args.port}")
        print("按 Ctrl+C 停止服务")
        print("=" * 50)
        app.run(host='0.0.0.0', port=args.port, debug=True)
    else:
        main()