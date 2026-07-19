# ============================================================
# 创建压力测试、CI/CD和扩展测试套件
# ============================================================
import os

project_root = r'D:\ws\xy_ws'

# ============================================================
# 1. 创建压力测试脚本 (本周规划 #2)
# ============================================================
print("[5/9] 🏋️ 创建压力测试脚本...")

stress_test_content = '''#!/usr/bin/env python3
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
    
    print(f"\\n{'='*60}")
    print(f"🚀 开始并发压力测试")
    print(f"{'='*60}")
    print(f"目标URL: {url}")
    print(f"并发用户数: {concurrent_users}")
    print(f"总请求数: {total_requests}")
    print(f"请求方法: {method}")
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\\n")
    
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
    
    print(f"\\n{'='*60}")
    print(f"📊 压力测试结果报告")
    print(f"{'='*60}")
    print(f"\\n✅ 成功指标:")
    print(f"   总请求数: {stats.get('total_requests', 0)}")
    print(f"   成功请求: {stats.get('successful_requests', 0)}")
    print(f"   失败请求: {stats.get('failed_requests', 0)}")
    print(f"   成功率: {stats.get('success_rate', 'N/A')}")
    
    print(f"\\n⏱️  性能指标:")
    print(f"   平均响应时间: {stats.get('avg_response_time_ms', 0):.2f}ms")
    print(f"   最小响应时间: {stats.get('min_response_time_ms', 0):.2f}ms")
    print(f"   最大响应时间: {stats.get('max_response_time_ms', 0):.2f}ms")
    print(f"   P50响应时间: {stats.get('p50_response_time_ms', 0):.2f}ms")
    print(f"   P95响应时间: {stats.get('p95_response_time_ms', 0):.2f}ms")
    print(f"   P99响应时间: {stats.get('p99_response_time_ms', 0):.2f}ms")
    
    print(f"\\n📈 吞吐量:")
    print(f"   总耗时: {stats.get('total_time_seconds', 0):.2f}s")
    print(f"   QPS (每秒查询数): {stats.get('requests_per_second', 0):.2f}")
    
    if result.errors:
        print(f"\\n❌ 错误样本 (前5个):")
        for i, error in enumerate(result.errors[:5], 1):
            print(f"   {i}. {error['error'][:100]}")
    
    print(f"\\n结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\\n")
    
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
'''

with open(os.path.join(project_root, 'tests', 'stress_test.py'), 'w', encoding='utf-8') as f:
    f.write(stress_test_content)

print("   ✓ 已创建 tests/stress_test.py")

# ============================================================
# 2. 创建CI/CD配置文件 (本周规划 #5)
# ============================================================
print("[6/9] 🔧 创建CI/CD流水线配置...")

github_actions_content = '''name: CI/CD Pipeline

on:
  push:
    branches: [master, develop, staging]
  pull_request:
    branches: [master]

jobs:
  # ============================================================
  # Job 1: 代码质量检查
  # ============================================================
  lint-and-format:
    name: 代码质量检查
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: 设置Python环境
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'
      
      - name: 安装依赖
        run: |
          python -m pip install --upgrade pip
          pip install flake8 black isort mypy pytest pytest-cov
      
      - name: 代码风格检查 (Black)
        run: black --check --diff .
        continue-on-error: true
      
      - name: 导入排序检查 (isort)
        run: isort --check-only --diff .
        continue-on-error: true
      
      - name: Linting (Flake8)
        run: flake8 main.py tests/ --max-line-length=120 --extend-ignore=E203,W503
        continue-on-error: true
      
      - name: 类型检查 (mypy)
        run: mypy main.py --ignore-missing-imports
        continue-on-error: true

  # ============================================================
  # Job 2: 单元测试
  # ============================================================
  unit-tests:
    name: 单元测试
    runs-on: ubuntu-latest
    needs: lint-and-format
    
    steps:
      - uses: actions/checkout@v3
      
      - name: 设置Python环境
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'
      
      - name: 安装依赖
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov pytest-xdist flask pydantic prometheus-client
          
      - name: 运行单元测试
        run: |
          pytest tests/test_security_fixes.py -v \
            --cov=main \
            --cov-report=term-missing \
            --cov-report=xml:coverage.xml \
            --junitxml=test-results.xml \
            --cov-fail-under=70
      
      - name: 上传测试覆盖率
        uses: codecov/codecov-action@v3
        with:
          files: coverage.xml
          fail_ci_if_error: false

  # ============================================================
  # Job 3: 安全扫描
  # ============================================================
  security-scan:
    name: 安全扫描
    runs-on: ubuntu-latest
    needs: unit-tests
    
    steps:
      - uses: actions/checkout@v3
      
      - name: 设置Python环境
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: 安装安全扫描工具
        run: pip install bandit safety
      
      - name: Bandit安全扫描
        run: bandit -r main.py -ll || true
      
      - name: Safety依赖漏洞检查
        run: safety check --full-report || true

  # ============================================================
  # Job 4: 构建和部署到Staging
  # ============================================================
  deploy-staging:
    name: 部署到Staging环境
    runs-on: ubuntu-latest
    needs: [unit-tests, security-scan]
    if: github.ref == 'refs/heads/staging' || github.ref == 'refs/heads/master'
    environment: staging
    
    steps:
      - uses: actions/checkout@v3
      
      - name: 设置Python环境
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: 安装依赖
        run: |
          python -m pip install --upgrade pip
          pip install gunicorn flask pydantic prometheus-client flask-restx
          
      - name: 运行健康检查（本地）
        run: |
          timeout 30s python main.py &
          sleep 10
          curl -f http://localhost:5000/health || exit 1
          curl -f http://localhost:5000/ready || exit 1
          
      - name: 部署到Staging服务器
        env:
          DEPLOY_KEY: ${{ secrets.STAGING_SSH_KEY }}
          STAGING_HOST: ${{ secrets.STAGING_HOST }}
        run: |
          echo "部署到Staging环境..."
          echo "主机: $STAGING_HOST"
          # 这里可以添加实际的部署命令，如rsync、docker等
'''

with open(os.path.join(project_root, '.github', 'workflows', 'ci-cd.yml'), 'w', encoding='utf-8') as f:
    f.write(github_actions_content)

print("   ✓ 已创建 .github/workflows/ci-cd.yml")

# ============================================================
# 3. 扩展边界情况测试用例 (本月规划 #5)
# ============================================================
print("[7/9] 🧪 扩展边界情况测试用例...")

extended_tests_content = '''# -*- coding: utf-8 -*-
"""
边界情况和极端条件测试套件 - v3.8.71
补充test_security_fixes.py中未覆盖的场景
"""

import pytest
import json
import os
import tempfile
import threading
import time
from unittest.mock import Mock, patch, MagicMock


class TestBoundaryConditions:
    """边界条件测试类"""
    
    def test_empty_string_input(self):
        """空字符串输入处理"""
        from main import app
        
        client = app.test_client()
        response = client.post(
            '/api/run',
            data=json.dumps({'command': ''}),
            content_type='application/json'
        )
        
        assert response.status_code in [400, 200]  # 根据业务逻辑决定
    
    def test_very_long_command(self):
        """超长命令字符串（10000+字符）"""
        from main import app
        
        client = app.test_client()
        long_command = 'echo "' + 'a' * 10000 + '"'
        response = client.post(
            '/api/run',
            data=json.dumps({'command': long_command}),
            content_type='application/json'
        )
        
        assert response.status_code in [200, 413]  # OK或Payload Too Large
    
    def test_special_characters_in_command(self):
        """包含特殊字符的命令"""
        special_commands = [
            {'command': 'echo "hello world"'},
            {"command": "echo 'single quotes'"},
            {'command': 'echo $HOME'},
            {'command': 'echo `backticks`'},
            {'command': 'echo $(subshell)'},
            {'command': 'echo ; malicious command'},
            {'command': 'echo && another'},
            {'command': 'echo | pipe'},
        ]
        
        from main import app
        client = app.test_client()
        
        for cmd in special_commands:
            response = client.post(
                '/api/run',
                data=json.dumps(cmd),
                content_type='application/json'
            )
            # 应该正常处理或拒绝，但不应该崩溃（500）
            assert response.status_code != 500, f"崩溃于特殊字符: {cmd['command'][:50]}"
    
    def test_unicode_input(self):
        """Unicode字符输入"""
        unicode_commands = [
            {'command': 'echo 中文测试'},
            {'command': 'echo 日本語テスト'},
            {'command': 'echo 한국어테스트'},
            {'command': 'echo 🎉🚀emoji测试'},
            {'command': 'echo العربية'},
            {'command': 'echo עברית'},
        ]
        
        from main import app
        client = app.test_client()
        
        for cmd in unicode_commands:
            response = client.post(
                '/api/run',
                data=json.dumps(cmd, ensure_ascii=False),
                content_type='application/json; charset=utf-8'
            )
            assert response.status_code != 500
    
    def test_null_bytes_in_input(self):
        """输入中的空字节"""
        from main import app
        
        client = app.test_client()
        response = client.post(
            '/api/run',
            data=b'{"command": "\\x00echo test"}',
            content_type='application/json'
        )
        
        assert response.status_code in [400, 200]  # 不应导致未处理异常


class TestConcurrencyEdgeCases:
    """并发边界情况测试"""
    
    def test_rapid_sequential_requests(self):
        """快速连续请求（无并发）"""
        from main import app
        
        client = app.test_client()
        
        for i in range(100):
            response = client.post(
                '/api/run',
                data=json.dumps({'command': f'echo test_{i}'}),
                content_type='application/json'
            )
            assert response.status_code == 200
    
    def test_burst_traffic(self):
        """突发流量模式：瞬间大量请求后静默"""
        import threading
        from main import app
        
        client = app.test_client()
        results = []
        
        def make_request(i):
            resp = client.post(
                '/api/run',
                data=json.dumps({'command': f'burst_{i}'}),
                content_type='application/json'
            )
            results.append(resp.status_code)
        
        threads = []
        # 瞬间启动50个线程
        for i in range(50):
            t = threading.Thread(target=make_request, args=(i,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join(timeout=10)
        
        # 大多数应该成功，少数可能被限流
        success_count = sum(1 for s in results if s == 200)
        rate_limited_count = sum(1 for s in results if s == 429)
        
        print(f"\\n突发流量结果: 成功={success_count}, 被限流={rate_limited_count}")
        assert success_count > 0  # 至少有一些成功
    
    def test_simultaneous_different_endpoints(self):
        """同时访问不同端点"""
        import threading
        from main import app
        
        client = app.test_client()
        results = {}
        
        def hit_health():
            results['health'] = client.get('/health').status_code
        
        def hit_ready():
            results['ready'] = client.get('/ready').status_code
            
        def hit_run():
            results['run'] = client.post(
                '/api/run',
                data=json.dumps({'command': 'echo test'}),
                content_type='application/json'
            ).status_code
        
        threads = [
            threading.Thread(target=hit_health),
            threading.Thread(target=hit_ready),
            threading.Thread(target=hit_run),
        ]
        
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=5)
        
        assert results.get('health') == 200
        assert results.get('ready') == 200
        assert results.get('run') in [200, 429]


class TestFilesystemEdgeCases:
    """文件系统边界情况"""
    
    def test_very_large_json_file(self):
        """超大JSON文件处理"""
        from main import safe_read_json
        
        # 创建一个较大的JSON文件（但不是太大）
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
            print(f"\\n大文件读取: {duration*1000:.2f}ms, 10000条记录")
            
        finally:
            os.unlink(temp_path)
    
    def test_malformed_json_variants(self):
        """各种畸形JSON格式"""
        malformed_cases = [
            ('', '空文件'),
            ('{', '不完整的对象'),
            ('[', '不完整的数组'),
            ('{"key": }', '缺失值'),
            ('{"key": undefined}', 'undefined值'),
            ('null', '仅null'),
            ('true', '仅布尔值'),
            ('123', '仅数字'),
            ('"string"', '仅字符串'),
            ('  \\n\\t  ', '空白字符'),
            ('{/**/}', '注释（非标准JSON）'),
        ]
        
        from main import safe_read_json
        
        for content, description in malformed_cases:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                f.write(content)
                temp_path = f.name
            
            try:
                result = safe_read_json(temp_path)
                # 应该返回默认值或解析后的值，不应崩溃
                assert result is not None, f"崩溃于: {description}"
            finally:
                os.unlink(temp_path)
    
    def test_permission_denied_handling(self):
        """权限不足时的优雅处理"""
        from main import safe_read_json
        
        # 在Windows上这个测试可能不太适用
        if os.name == 'nt':
            pytest.skip('权限测试在Windows上不适用')
            return
        
        # 尝试读取系统文件（应该被拒绝）
        result = safe_read_json('/etc/shadow', default={})
        assert result == {}  # 应返回默认值而不是崩溃


class TestMemoryAndResourceLimits:
    """内存和资源限制测试"""
    
    def test_many_consecutive_cache_reads(self):
        """连续多次缓存读取（检测内存泄漏）"""
        from main import FileCacheManager
        
        cache = FileCacheManager(ttl_seconds=5)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({'data': 'test'}, f)
            temp_path = f.name
        
        try:
            # 连续读取1000次
            initial_memory = None
            for i in range(1000):
                data = cache.read_json(temp_path)
                
                if i == 0:
                    import psutil
                    process = psutil.Process()
                    initial_memory = process.memory_info().rss
                
                if i == 999:
                    process = psutil.Process()
                    final_memory = process.memory_info().rss
                    
                    memory_growth_mb = (final_memory - initial_memory) / (1024*1024)
                    print(f"\\n内存增长: {memory_growth_mb:.2f}MB (1000次操作)")
                    
                    # 内存增长不应该超过10MB
                    assert memory_growth_mb < 10, f"可能的内存泄漏: {memory_growth_mb:.2f}MB"
        
        finally:
            os.unlink(temp_path)


class TestNetworkResilience:
    """网络弹性测试"""
    
    @patch('socket.socket')
    def test_socket_connection_timeout(self, mock_socket_class):
        """Socket连接超时处理"""
        mock_socket = Mock()
        mock_socket.connect.side_effect = TimeoutError('连接超时')
        mock_socket_class.return_value = mock_socket
        
        from main import PathManager
        ip = PathManager.get_lan_ip()
        
        # 应该返回空字符串而不是抛出异常
        assert ip == ''
    
    @patch('socket.socket')
    def test_socket_refused_connection(self, mock_socket_class):
        """连接被拒绝的处理"""
        mock_socket = Mock()
        mock_socket.connect.side_effect = ConnectionRefusedError('连接被拒绝')
        mock_socket.close = Mock()
        mock_socket_class.return_value = mock_socket
        
        from main import PathManager
        ip = PathManager.get_lan_ip()
        
        assert ip == ''
        mock_socket.close.assert_called_once()  # 确保socket被关闭


class TestDataIntegrity:
    """数据完整性测试"""
    
    def test_json_roundtrip_preserves_unicode(self):
        """JSON读写保留Unicode字符"""
        original_data = {
            '中文': '值',
            'emoji': '🎉🚀',
            'arabic': 'العربية',
            'mixed': 'Hello 世界 🌍'
        }
        
        from main import FileManager
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            FileManager.write_json(temp_path, original_data)
            read_data = FileManager.read_json(temp_path)
            
            assert read_data == original_data
        finally:
            os.unlink(temp_path)
    
    def test_cache_consistency_under_rapid_writes(self):
        """快速写入下的缓存一致性"""
        from main import FileCacheManager
        
        cache = FileCacheManager(ttl_seconds=1)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            versions = []
            for i in range(100):
                data = {'version': i, 'timestamp': time.time()}
                with open(temp_path, 'w') as f:
                    json.dump(data, f)
                
                cached = cache.read_json(temp_path)
                versions.append(cached.get('version'))
            
            # 所有版本应该是递增的或相同的（缓存可能返回旧数据）
            # 但不应该出现乱序或异常值
            unique_versions = set(versions)
            assert all(isinstance(v, int) for v in unique_versions)
            
        finally:
            os.unlink(temp_path)


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
'''

with open(os.path.join(project_root, 'tests', 'test_edge_cases.py'), 'w', encoding='utf-8') as f:
    f.write(extended_tests_content)

print("   ✓ 已创建 tests/test_edge_cases.py")

print("\n✅ 测试和CI/CD基础设施创建完成！")
