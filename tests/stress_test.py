#!/usr/bin/env python3
"""
Szwego商品爬虫 - API压力测试工具

用法:
    python stress_test.py --target http://localhost:5000 --concurrent 100 --requests 1000
    python stress_test.py --target http://localhost:5000 --concurrent 50 --duration 30
"""

import argparse
import json
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def make_request(url, method='GET', data=None, timeout=10):
    start = time.time()
    try:
        headers = {'Content-Type': 'application/json'}
        req = Request(url, data=data.encode('utf-8') if data else None, headers=headers, method=method)
        resp = urlopen(req, timeout=timeout)
        status = resp.getcode()
        body = resp.read().decode('utf-8', errors='replace')
        elapsed = time.time() - start
        return {'status': status, 'time': elapsed, 'error': None, 'size': len(body)}
    except HTTPError as e:
        elapsed = time.time() - start
        return {'status': e.code, 'time': elapsed, 'error': str(e), 'size': 0}
    except (URLError, OSError) as e:
        elapsed = time.time() - start
        return {'status': 0, 'time': elapsed, 'error': str(e), 'size': 0}
    except Exception as e:
        elapsed = time.time() - start
        return {'status': 0, 'time': elapsed, 'error': str(e), 'size': 0}


def run_stress_test(target, concurrent, total_requests, endpoints):
    results = []
    request_count = 0
    lock = __import__('threading').Lock()

    def worker(ep):
        nonlocal request_count
        with lock:
            if request_count >= total_requests:
                return None
            request_count += 1
        url = f"{target.rstrip('/')}{ep['path']}"
        return make_request(url, method=ep.get('method', 'GET'), data=ep.get('data'))

    default_endpoints = [
        {'path': '/', 'method': 'GET'},
        {'path': '/api/version', 'method': 'GET'},
        {'path': '/health', 'method': 'GET'},
        {'path': '/ready', 'method': 'GET'},
    ]
    if not endpoints:
        endpoints = default_endpoints

    print(f"{'='*60}")
    print(f"压力测试 - 目标: {target}")
    print(f"并发数: {concurrent} | 总请求数: {total_requests}")
    print(f"端点: {[e['path'] for e in endpoints]}")
    print(f"{'='*60}")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=concurrent) as executor:
        futures = []
        for i in range(total_requests):
            ep = endpoints[i % len(endpoints)]
            futures.append(executor.submit(worker, ep))

        completed = 0
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)
                completed += 1
                if completed % 100 == 0:
                    print(f"  已完成: {completed}/{total_requests}")

    total_time = time.time() - start_time

    if not results:
        print("没有成功完成的请求！")
        return

    success = [r for r in results if 200 <= r['status'] < 400]
    failed = [r for r in results if r['status'] >= 400 or r['status'] == 0]
    times = [r['time'] for r in results]
    sorted_times = sorted(times)

    print(f"\n{'='*60}")
    print(f"测试结果")
    print(f"{'='*60}")
    print(f"总请求数: {len(results)}")
    print(f"成功请求: {len(success)}")
    print(f"失败请求: {len(failed)}")
    print(f"成功率: {len(success)/len(results)*100:.2f}%")
    print(f"总耗时: {total_time:.2f}s")
    print(f"QPS: {len(results)/total_time:.2f}")
    print(f"\n响应时间统计:")
    print(f"  最小: {min(times)*1000:.2f}ms")
    print(f"  最大: {max(times)*1000:.2f}ms")
    print(f"  平均: {statistics.mean(times)*1000:.2f}ms")
    print(f"  中位数(P50): {statistics.median(times)*1000:.2f}ms")
    if len(sorted_times) >= 20:
        p95_idx = int(len(sorted_times) * 0.95)
        p99_idx = int(len(sorted_times) * 0.99)
        print(f"  P95: {sorted_times[p95_idx]*1000:.2f}ms")
        print(f"  P99: {sorted_times[p99_idx]*1000:.2f}ms")

    status_counts = {}
    for r in results:
        s = r['status']
        status_counts[s] = status_counts.get(s, 0) + 1
    print(f"\n状态码分布:")
    for s in sorted(status_counts.keys()):
        label = '成功' if 200 <= s < 400 else '失败'
        print(f"  {s}: {status_counts[s]} ({label})")

    if failed:
        error_types = {}
        for r in failed:
            err = r.get('error', 'Unknown')[:80]
            error_types[err] = error_types.get(err, 0) + 1
        print(f"\n错误类型:")
        for err, count in sorted(error_types.items(), key=lambda x: -x[1]):
            print(f"  [{count}x] {err}")

    report = {
        'total_requests': len(results),
        'success': len(success),
        'failed': len(failed),
        'success_rate': f"{len(success)/len(results)*100:.2f}%",
        'total_time': f"{total_time:.2f}s",
        'qps': f"{len(results)/total_time:.2f}",
        'avg_latency_ms': f"{statistics.mean(times)*1000:.2f}",
        'p50_ms': f"{statistics.median(times)*1000:.2f}",
    }
    report_path = 'tests/stress_test_report.json'
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n报告已保存到: {report_path}")
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(description='Szwego API压力测试工具')
    parser.add_argument('--target', default='http://localhost:5000', help='目标地址')
    parser.add_argument('--concurrent', type=int, default=100, help='并发数')
    parser.add_argument('--requests', type=int, default=1000, help='总请求数')
    parser.add_argument('--duration', type=int, default=0, help='持续时间(秒)，优先于--requests')
    args = parser.parse_args()

    total = args.requests
    if args.duration > 0:
        total = args.concurrent * args.duration

    run_stress_test(args.target, args.concurrent, total, [])


if __name__ == '__main__':
    main()
