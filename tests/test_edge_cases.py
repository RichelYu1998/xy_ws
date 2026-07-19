# -*- coding: utf-8 -*-
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
            data=b'{"command": "\x00echo test"}',
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
        
        print(f"\n突发流量结果: 成功={success_count}, 被限流={rate_limited_count}")
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
            print(f"\n大文件读取: {duration*1000:.2f}ms, 10000条记录")
            
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
            ('  \n\t  ', '空白字符'),
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
                    print(f"\n内存增长: {memory_growth_mb:.2f}MB (1000次操作)")
                    
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
