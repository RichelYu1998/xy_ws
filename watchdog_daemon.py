#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
watchdog_daemon.py - 外部守护进程（防闪退增强版）
独立于主进程运行，监控主进程状态，崩溃时自动重启。
用法: python watchdog_daemon.py -- python main.py --web --port 8888
"""
import os
import sys
import time
import signal
import subprocess
import logging
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('watchdog')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(PROJECT_DIR, 'file')
os.makedirs(LOG_DIR, exist_ok=True)
CRASH_LOG = os.path.join(LOG_DIR, 'crash_history.log')


class WatchdogDaemon:
    def __init__(self, command):
        self.command = command
        self.process = None
        self.restart_count = 0
        self.max_restarts = 50
        self.max_memory_mb = 2000
        self.restart_cooldown = 10
        self.start_time = time.time()

    def _log_crash(self, reason):
        try:
            with open(CRASH_LOG, 'a', encoding='utf-8') as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {reason}\n")
        except Exception:
            pass

    def _is_over_memory(self):
        if not psutil or not self.process:
            return False
        try:
            proc = psutil.Process(self.process.pid)
            mem_mb = proc.memory_info().rss / (1024 * 1024)
            if mem_mb > self.max_memory_mb:
                logger.warning(f"内存超限: {mem_mb:.0f}MB > {self.max_memory_mb}MB")
                return True
        except (psutil.NoSuchProcess, Exception):
            pass
        return False

    def _kill_process(self):
        if not self.process:
            return
        try:
            if psutil:
                proc = psutil.Process(self.process.pid)
                children = proc.children(recursive=True)
                for child in children:
                    try:
                        child.terminate()
                    except Exception:
                        pass
                try:
                    proc.terminate()
                except Exception:
                    pass
                gone, alive = psutil.wait_procs(children + [proc], timeout=5)
                for p in alive:
                    try:
                        p.kill()
                    except Exception:
                        pass
            else:
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    self.process.kill()
        except Exception as e:
            logger.debug(f"终止进程异常: {e}")

    def _start_process(self):
        try:
            env = os.environ.copy()
            if sys.platform == 'win32':
                self.process = subprocess.Popen(
                    self.command,
                    env=env,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                )
            else:
                self.process = subprocess.Popen(
                    self.command,
                    env=env,
                    preexec_fn=os.setsid
                )
            logger.info(f"进程已启动 (PID: {self.process.pid})")
            return True
        except Exception as e:
            logger.error(f"启动失败: {e}")
            return False

    def run(self):
        logger.info("=" * 50)
        logger.info("守护进程启动")
        logger.info(f"命令: {' '.join(self.command)}")
        logger.info(f"最大重启次数: {self.max_restarts}")
        logger.info(f"内存限制: {self.max_memory_mb}MB")
        logger.info("=" * 50)

        def signal_handler(signum, frame):
            logger.info("收到停止信号，正在关闭...")
            self._kill_process()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        while self.restart_count < self.max_restarts:
            if not self._start_process():
                logger.error("启动失败，等待后重试...")
                time.sleep(self.restart_cooldown)
                self.restart_count += 1
                continue

            while True:
                try:
                    retcode = self.process.poll()
                except Exception:
                    retcode = -1

                if retcode is not None:
                    break

                if self._is_over_memory():
                    logger.warning("内存超限，正在重启...")
                    self._log_crash(f"内存超限(>{self.max_memory_mb}MB)，进程被重启")
                    self._kill_process()
                    time.sleep(2)
                    break

                time.sleep(2)

            if retcode == 0:
                logger.info("进程正常退出")
                break

            self.restart_count += 1
            logger.warning(f"进程异常退出(码:{retcode})，第{self.restart_count}次重启...")
            self._log_crash(f"进程异常退出(码:{retcode})，第{self.restart_count}次重启")

            if self.restart_count >= self.max_restarts:
                logger.error(f"已达最大重启次数({self.max_restarts})，停止")
                break

            time.sleep(self.restart_cooldown)

        uptime = time.time() - self.start_time
        logger.info(f"守护进程结束，运行时间: {uptime:.0f}s，重启次数: {self.restart_count}")


def main():
    if len(sys.argv) < 3 or sys.argv[1] != '--':
        print("用法: python watchdog_daemon.py -- <command> [args...]")
        print("示例: python watchdog_daemon.py -- python main.py --web --port 8888")
        sys.exit(1)

    command = sys.argv[2:]
    daemon = WatchdogDaemon(command)
    daemon.run()


if __name__ == '__main__':
    main()