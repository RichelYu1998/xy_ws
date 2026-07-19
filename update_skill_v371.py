# 更新skill.md - 添加v3.8.71企业级功能规范
skill_path = r'D:\ws\xy_ws\skill.md'

with open(skill_path, 'r', encoding='utf-8') as f:
    skill = f.read()

new_skill_content = '''

## 2.15 企业级运维标准（v3.8.71 新增）

### 2.15.1 健康检查端点规范

#### 端点定义
```python
# /health - 完整健康状态检查
GET /health

响应格式:
{
    "status": "healthy | degraded | unhealthy",
    "timestamp": "2026-07-19T14:30:00",
    "version": "3.8.71",
    "checks": {
        "cpu": {"status": "healthy", "usage_percent": 45.2},
        "memory": {"status": "healthy", "percent": 62.5},
        "disk": {"status": "warning", "percent": 88.3}
    }
}

HTTP状态码:
- 200: healthy 或 degraded
- 503: unhealthy
```

#### 使用场景
```python
# 负载均衡器健康检查
# Kubernetes liveness/readiness probes
# 监控系统定时探测
```

### 2.15.2 Prometheus指标集成

#### 必需指标
```python
from prometheus_client import Counter, Histogram, Gauge

# 请求计数器
REQUEST_COUNT = Counter(
    'flask_requests_total',
    '请求总数',
    ['method', 'endpoint', 'http_status']
)

# 延迟直方图
REQUEST_LATENCY = Histogram(
    'flask_request_duration_seconds',
    '请求延迟',
    buckets=(0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 10.0)
)

# 活跃任务数
ACTIVE_TASKS_GAUGE = Gauge('flask_active_tasks', '活跃任务数')
```

### 2.15.3 Pydantic验证模型示例

```python
from pydantic import BaseModel, Field, validator

class RunCommandRequest(BaseModel):
    """命令执行请求"""
    command: str = Field(..., min_length=1, max_length=10000)
    
    @validator('command')
    def validate_command_safe(cls, v):
        dangerous = ['rm -rf /', 'mkfs', 'shutdown']
        for pattern in dangerous:
            if pattern.lower() in v.lower():
                raise ValueError(f"危险命令: {pattern}")
        return v.strip()

# 使用方式
data, error = validate_request(RunCommandRequest, request_data)
if error:
    return jsonify({'error': error}), 400
```

### 2.15.4 环境配置管理

#### 配置文件结构
```json
// config/production.json
{
    "environment": "production",
    "rate_limiting": {
        "api_endpoints": {
            "max_requests_per_minute": 200,
            "window_seconds": 60,
            "enabled": true
        }
    },
    "caching": {
        "json_files": {
            "ttl_seconds": 30,
            "monitoring": {
                "log_cache_hits": true,
                "report_interval_seconds": 300
            }
        }
    },
    "monitoring": {
        "prometheus_enabled": true,
        "metrics_endpoint": "/metrics"
    }
}
```

#### 部署流程
```bash
# Staging环境部署（包含测试）
./deploy.sh staging

# Production环境部署（跳过测试）
./deploy.sh production

# 回滚到上一版本
./deploy.sh rollback
```

### 2.15.5 性能测试基准

#### 压力测试命令
```bash
# 基础测试：100并发，1000请求
python tests/stress_test.py --target http://localhost:5000 --concurrent 100 --requests 1000

# 高负载测试：500并发，10000请求
python tests/stress_test.py --target http://localhost:5000 --concurrent 500 --requests 10000

# 测试特定端点
python tests/stress_test.py --target http://localhost:5000 --endpoint /health --method GET --requests 1000
```

#### 性能目标
| 指标 | Staging | Production |
|------|---------|------------|
| 平均响应时间 | <200ms | <100ms |
| P99延迟 | <1000ms | <500ms |
| 成功率 | >95% | >99% |
| QPS支持 | >100 | >500 |

---

'''

# 在文件末尾添加新内容
if '2.15 企业级运维标准' not in skill:
    skill += new_skill_content
    
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(skill)
    
    print('✅ skill.md已更新')
    print('   - 新增第2.15章：企业级运维标准')
    print('   - 包含健康检查、Prometheus、Pydantic等规范')
else:
    print('⊗ 已存在')
