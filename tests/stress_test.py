#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
压力测试脚本 - v3.8.71
用于验证线程安全性和性能基线

使用方法:
    python stress_test.py --target http://localhost:5000 --concurrent 100 --requests 1000
    
依赖安装:
    pip install requests asyncio aiohttp
"""

import argparse
import asyncio
import time
import json
import statistics
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import requests


class StressTestResult:
    """压力测试结果收集器"""
    
    def __init__(self):
        self.results = []
        self.errors = []
        self.start_time = None
        self.end_time = None
        
    def add_success(self, duration, status_code):
        self.results.append({
            'duration': duration,
            'status_code': status_code,
            'success': True
        })
    
    def add_error(self, error, duration=None):
        self.errors.append({
            'error': str(error),
            'duration': duration,
            'success': False
        })
    
    def get_statistics(self):
        """计算统计信息"""
        if not self.results:
            return {}
        
        durations = [r['duration'] for r in self.results]
        
        return {
            'total_requests': len(self.results) + len(self.errors),
            'successful_requests': len(self.results),
            'failed_requests': len(self.errors),
            'success_rate': f"{(len(self.results) / (len(self.results) + len(self.errors))) * 100:.2f}%",
            'avg_response_time_ms': round(statistics.mean(durations) * 1000, 2),
            'min_response_time_ms': round(min(durations) * 1000, 2),
            'max_response_time_ms': round(max(durations) * 1000, 2),
            'p50_response_time_ms': round(sorted(durations)[len(durations)//2] * 1000, 2),
            'p95_response_time_ms': round(sorted(durations)[int(len(durations)*0.95)] * 1000, 2),
            'p99_response_time_ms': round(sorted(durations)[int(len(durations)*0.99)] * 1000, 2),
            'total_time_seconds': round(self.end_time - self.start_time, 2),
            'requests_per_second': round(len(self.results) / (self.end_time - self.start_time), 2)
        }


def test_endpoint_single(url, method='GET', data=None, headers=None):
    """单次请求测试"""
    start = time.time()
    try:
        if method == 'POST':
            response = requests.post(url, json=data, headers=headers or {}, timeout=10)
        else:
            response = requests.get(url, headers=headers or {}, timeout=10)
        
        duration = time.time() - start
        return {'duration': duration, 'status_code': response.status_code}
        
    except Exception as e:
        duration = time.time() - start
        raise Exception(f"请求失败: {e}")


def run_concurrent_test(target_url, concurrent_users=50, total_requests=1000, 
                       endpoint='/api/run', method='POST', data=None):
    """并发测试主函数"""
    
    url = target_url.rstrip('/') + endpoint
    result = StressTestResult()
    
    print(f"\n{'='*60}")
    print(f"🚀 开始并发压力测试")
    print(f"{'='*60}")
    print(f"目标URL: {url}")
    print(f"并发用户数: {concurrent_users}")
    print(f"总请求数: {total_requests}")
    print(f"请求方法: {method}")
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    result.start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
        futures = []
        
        # 提交所有请求
        for i in range(total_requests):
            future = executor.submit(test_endpoint_single, url, method, data)
            futures.append(future)
        
        # 收集结果
        completed = 0
        for future in as_completed(futures):
            try:
                res = future.result()
                result.add_success(res['duration'], res['status_code'])
            except Exception as e:
                result.add_error(e)
            
            completed += 1
            if completed % 100 == 0:
                print(f"进度: {completed}/{total_requests} ({completed/total_requests*100:.1f}%)")
    
    result.end_time = time.time()
    
    # 输出结果
    stats = result.get_statistics()
    
    print(f"\n{'='*60}")
    print(f"📊 压力测试结果报告")
    print(f"{'='*60}")
    print(f"\n✅ 成功指标:")
    print(f"   总请求数: {stats.get('total_requests', 0)}")
    print(f"   成功请求: {stats.get('successful_requests', 0)}")
    print(f"   失败请求: {stats.get('failed_requests', 0)}")
    print(f"   成功率: {stats.get('success_rate', 'N/A')}")
    
    print(f"\n⏱️  性能指标:")
    print(f"   平均响应时间: {stats.get('avg_response_time_ms', 0):.2f}ms")
    print(f"   最小响应时间: {stats.get('min_response_time_ms', 0):.2f}ms")
    print(f"   最大响应时间: {stats.get('max_response_time_ms', 0):.2f}ms")
    print(f"   P50响应时间: {stats.get('p50_response_time_ms', 0):.2f}ms")
    print(f"   P95响应时间: {stats.get('p95_response_time_ms', 0):.2f}ms")
    print(f"   P99响应时间: {stats.get('p99_response_time_ms', 0):.2f}ms")
    
    print(f"\n📈 吞吐量:")
    print(f"   总耗时: {stats.get('total_time_seconds', 0):.2f}s")
    print(f"   QPS (每秒查询数): {stats.get('requests_per_second', 0):.2f}")
    
    if result.errors:
        print(f"\n❌ 错误样本 (前5个):")
        for i, error in enumerate(result.errors[:5], 1):
            print(f"   {i}. {error['error'][:100]}")
    
    print(f"\n结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # 保存详细结果到文件
    report_file = f'stress_test_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'config': {
                'url': url,
                'concurrent_users': concurrent_users,
                'total_requests': total_requests,
                'method': method
            },
            'statistics': stats,
            'errors': result.errors[:20]  # 只保存前20个错误
        }, f, indent=2, ensure_ascii=False)
    
    print(f"📄 详细报告已保存: {report_file}")
    
    return result


def main():
    parser = argparse.ArgumentParser(description='API压力测试工具')
    parser.add_argument('--target', '-t', required=True, help='目标基础URL (如: http://localhost:5000)')
    parser.add_argument('--concurrent', '-c', type=int, default=50, help='并发用户数 (默认: 50)')
    parser.add_argument('--requests', '-r', type=int, default=1000, help='总请求数 (默认: 1000)')
    parser.add_argument('--endpoint', '-e', default='/api/run', help='测试端点 (默认: /api/run)')
    parser.add_argument('--method', '-m', choices=['GET', 'POST'], default='POST', help='HTTP方法 (默认: POST)')
    parser.add_argument('--data', '-d', help='POST数据 (JSON格式)')
    
    args = parser.parse_args()
    
    # 解析POST数据
    post_data = None
    if args.data:
        try:
            post_data = json.loads(args.data)
        except json.JSONDecodeError:
            print(f"错误: 无效的JSON数据: {args.data}")
            return
    
    # 运行测试
    run_concurrent_test(
        target_url=args.target,
        concurrent_users=args.concurrent,
        total_requests=args.requests,
        endpoint=args.endpoint,
        method=args.method,
        data=post_data
    )


if __name__ == '__main__':
    main()
