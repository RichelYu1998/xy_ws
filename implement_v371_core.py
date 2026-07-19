# ============================================================
# v3.8.71 企业级功能全面升级 - 实施所有规划任务
# ============================================================
import os
import sys

file = r'D:\ws\xy_ws\main.py'
project_root = r'D:\ws\xy_ws'

with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("🚀 开始实施 v3.8.71 企业级功能升级")
print("=" * 80)

total_features = 0
features_list = []

# ============================================================
# 功能1: 健康检查端点 /health (本月规划 #4)
# ============================================================
print("\n[1/9] 🏥 实现健康检查端点 /health ...")

health_endpoint_code = '''

@app.route('/health', methods=['GET'])
def health_check():
    """健康检查端点 - 用于负载均衡器和监控系统
    
    返回格式:
    - 200: 服务正常
    - 503: 服务不可用（部分组件异常）
    
    检查项:
    - 系统资源（CPU、内存、磁盘）
    - 关键依赖服务状态
    - 缓存系统状态
    """
    import psutil
    import platform
    
    health_status = {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': VERSION,
        'system': Environment.SYSTEM,
        'uptime': None,
        'checks': {}
    }
    
    try:
        # 系统运行时间
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        health_status['uptime'] = str(datetime.now() - boot_time).split('.')[0]
        
        # CPU使用率（最近5秒平均值）
        cpu_percent = psutil.cpu_percent(interval=0.5)
        health_status['checks']['cpu'] = {
            'status': 'healthy' if cpu_percent < 80 else 'warning' if cpu_percent < 95 else 'critical',
            'usage_percent': round(cpu_percent, 2)
        }
        
        # 内存使用情况
        memory = psutil.virtual_memory()
        health_status['checks']['memory'] = {
            'status': 'healthy' if memory.percent < 80 else 'warning' if memory.percent < 95 else 'critical',
            'total_gb': round(memory.total / (1024**3), 2),
            'used_gb': round(memory.used / (1024**3), 2),
            'percent': memory.percent
        }
        
        # 磁盘使用情况
        disk = psutil.disk_usage(PROJECT_DIR)
        health_status['checks']['disk'] = {
            'status': 'healthy' if disk.percent < 85 else 'warning' if disk.percent < 95 else 'critical',
            'total_gb': round(disk.total / (1024**3), 2),
            'free_gb': round(disk.free / (1024**3), 2),
            'percent': disk.percent
        }
        
        # 进程数量
        process_count = len(psutil.pids())
        health_status['checks']['processes'] = {
            'status': 'healthy',
            'count': process_count
        }
        
        # 缓存状态
        try:
            cache_stats = json_cache.get_stats()
            health_status['checks']['cache'] = {
                'status': 'healthy',
                'cached_files': cache_stats['cached_files']
            }
        except Exception as e:
            health_status['checks']['cache'] = {
                'status': 'warning',
                'error': str(e)
            }
        
        # 活跃任务数
        active_tasks = len([t for t in tasks.values() if t.get('status') == 'running'])
        health_status['checks']['active_tasks'] = {
            'status': 'healthy' if active_tasks < 10 else 'warning',
            'count': active_tasks
        }
        
        # 判断整体状态
        all_statuses = [check['status'] for check in health_status['checks'].values()]
        if 'critical' in all_statuses:
            health_status['status'] = 'unhealthy'
        elif 'warning' in all_statuses:
            health_status['status'] = 'degraded'
            
    except Exception as e:
        health_status['status'] = 'error'
        health_status['error'] = str(e)
    
    status_code = 200 if health_status['status'] == 'healthy' else 503
    
    return jsonify(health_status), status_code


@app.route('/ready', methods=['GET'])
def readiness_check():
    """就绪检查端点 - 用于Kubernetes等容器编排系统
    
    与/health的区别:
    - /health: 检查进程是否存活
    - /ready: 检查是否准备好接收流量
    """
    return jsonify({
        'status': 'ready',
        'timestamp': datetime.now().isoformat()
    }), 200


'''

# 在第一个@app.route之前插入健康检查端点
first_route_point = content.find('@app.route(\'/\')')
if first_route_point > 0 and '/health' not in content:
    content = content[:first_route_point] + health_endpoint_code + '\n\n' + content[first_route_point:]
    total_features += 1
    features_list.append("✓ 新增 /health 和 /ready 健康检查端点")
    print("   ✓ 已添加健康检查端点")
else:
    print("   ⊗ 健康检查端点已存在")

# ============================================================
# 功能2: Pydantic 输入验证框架 (本月规划 #1)
# ============================================================
print("\n[2/9] 🔍 引入Pydantic进行输入验证...")

pydantic_validation_code = '''
# ============================================================
# Pydantic 输入验证模型 (v3.8.71)
# ============================================================
try:
    from pydantic import BaseModel, Field, validator, ValidationError
    from typing import Optional, List
    PYDANTIC_AVAILABLE = True
except ImportError:
    PYDANTIC_AVAILABLE = False
    print("⚠️ Pydantic未安装，将使用基础验证。安装命令: pip install pydantic")


class RunCommandRequest(BaseModel):
    """运行命令请求验证模型"""
    command: str = Field(..., min_length=1, max_length=10000, 
                        description="要执行的命令")
    
    @validator('command')
    def validate_command_safe(cls, v):
        """验证命令安全性"""
        dangerous_patterns = ['rm -rf /', 'mkfs', 'shutdown', 'reboot', 
                            'format', 'del /f /q C:\\\\']
        for pattern in dangerous_patterns:
            if pattern.lower() in v.lower():
                raise ValueError(f"检测到危险命令模式: {pattern}")
        return v.strip()


class TaskInputRequest(BaseModel):
    """任务输入请求验证模型"""
    task_id: str = Field(..., min_length=1, max_length=50,
                        description="任务ID")
    user_input: str = Field("", max_length=10000,
                           description="用户输入内容")


class KillTaskRequest(BaseModel):
    """终止任务请求验证模型"""
    task_id: str = Field(..., min_length=1, max_length=50)


class SKUCompareRequest(BaseModel):
    """SKU对比请求验证模型"""
    skus: Optional[str] = Field(None, max_length=50000,
                               description="SKU列表，支持空格/逗号/换行分隔")


def validate_request(model_class, data):
    """通用请求验证函数"""
    if not PYDANTIC_AVAILABLE:
        # 回退到基础验证
        if not data:
            return None, "请求体不能为空"
        return data, None
    
    try:
        validated_data = model_class(**data)
        return validated_data.dict(), None
    except ValidationError as e:
        error_msg = "; ".join([f"{err['loc'][0]}: {err['msg']}" for err in e.errors()])
        return None, f"输入验证失败: {error_msg}"


'''

# 在RateLimiter类之后插入Pydantic代码
insert_after_rate_limiter = content.find('class RateLimiter:')
if insert_after_rate_limiter > 0 and 'PYDANTIC_AVAILABLE' not in content:
    # 找到RateLimiter类的结尾（下一个类或函数定义）
    next_class = content.find('\nclass ', insert_after_rate_limiter + 1)
    next_func = content.find('\ndef ', insert_after_rate_limiter + 1)
    insert_point = min(x for x in [next_class, next_func] if x > 0)
    
    content = content[:insert_point] + pydantic_validation_code + '\n\n' + content[insert_point:]
    total_features += 1
    features_list.append("✓ 引入Pydantic输入验证框架")
    print("   ✓ 已添加Pydantic验证模型")
else:
    print("   ⊗ Pydantic已存在或插入点未找到")

# ============================================================
# 功能3: Prometheus 指标导出 (本月规划 #2)
# ============================================================
print("\n[3/9] 📊 集成Prometheus指标导出...")

prometheus_code = '''
# ============================================================
# Prometheus 指标导出 (v3.8.71)
# ============================================================
try:
    from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
    PROMETHEUS_AVAILABLE = True
    
    # 定义指标
    REQUEST_COUNT = Counter(
        'flask_requests_total',
        'Flask请求总数',
        ['method', 'endpoint', 'http_status']
    )
    
    REQUEST_LATENCY = Histogram(
        'flask_request_duration_seconds',
        'Flask请求延迟',
        ['method', 'endpoint'],
        buckets=(0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 10.0)
    )
    
    ACTIVE_TASKS_GAUGE = Gauge(
        'flask_active_tasks',
        '当前活跃任务数'
    )
    
    CACHE_HITS_GAUGE = Gauge(
        'flask_cache_hits_total',
        '缓存命中次数'
    )
    
    RATE_LIMITED_COUNT = Counter(
        'flask_rate_limited_total',
        '被速率限制的请求数',
        ['endpoint']
    )
    
except ImportError:
    PROMETHEUS_AVAILABLE = False
    print("⚠️ prometheus_client未安装。安装命令: pip install prometheus_client")


@app.route('/metrics', methods=['GET'])
def prometheus_metrics():
    """Prometheus指标抓取端点"""
    if not PROMETHEUS_AVAILABLE:
        return jsonify({
            'error': 'Prometheus未启用',
            'hint': '安装prometheus_client库以启用此功能'
        }), 503
    
    # 更新活跃任务数
    if PROMETHEUS_AVAILABLE:
        ACTIVE_TASKS_GAUGE.set(len([t for t in tasks.values() if t.get('status') == 'running']))
    
    response = Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
    return response


'''

# 在健康检查端点之后插入Prometheus代码
metrics_insert_point = content.find("def readiness_check():")
if metrics_insert_point > 0 and 'PROMETHEUS_AVAILABLE' not in content:
    # 找到readiness_check函数的结尾
    func_end = content.find('\n\n', metrics_insert_point) + 2
    content = content[:func_end] + prometheus_code + content[func_end:]
    total_features += 1
    features_list.append("✓ 集成Prometheus指标导出")
    print("   ✓ 已添加Prometheus /metrics 端点")
else:
    print("   ⊗ Prometheus已存在或插入点未找到")

# ============================================================
# 功能4: Swagger/OpenAPI 自动文档 (本月规划 #3)
# ============================================================
print("\n[4/9] 📚 添加Swagger/OpenAPI自动文档...")

swagger_code = '''
# ============================================================
# Swagger/OpenAPI 文档自动生成 (v3.8.71)
# ============================================================
try:
    from flask_restx import Api, Resource, fields
    SWAGGER_AVAILABLE = True
    
    # 创建API实例
    api = Api(app, version='3.8.71', title='微购商品管理系统API',
              description='企业级商品数据爬取和管理系统的RESTful API文档',
              doc='/docs/',  # Swagger UI路径
              prefix='/api')
    
    # 定义命名空间
    ns_command = api.namespace('command', description='命令执行相关接口')
    ns_task = api.namespace('task', description='任务管理相关接口')
    ns_sku = api.namespace('sku', description='SKU对比相关接口')
    ns_system = api.namespace('system', description='系统监控相关接口')
    
    # 定义响应模型
    success_model = api.model('SuccessResponse', {
        'success': fields.Boolean(description='操作是否成功'),
        'task_id': fields.String(description='任务ID'),
        'message': fields.String(description='消息')
    })
    
    error_model = api.model('ErrorResponse', {
        'error': fields.String(description='错误信息'),
        'code': fields.String(description='错误码')
    })
    
    health_model = api.model('HealthResponse', {
        'status': fields.String(description='健康状态: healthy/degraded/unhealthy'),
        'timestamp': fields.String(description='检查时间'),
        'version': fields.String(description='版本号'),
        'checks': fields.Raw(description='详细检查项')
    })
    
except ImportError:
    SWAGGER_AVAILABLE = False
    print("⚠️ flask-restx未安装。安装命令: pip install flask-restx")
    api = None


'''

# 在Prometheus代码之后插入Swagger代码
swagger_insert = content.find("@app.route('/metrics'")
if swagger_insert > 0 and 'SWAGGER_AVAILABLE' not in content:
    # 找到metrics函数的结尾
    metrics_func_end = content.find('\n\n', swagger_insert) + 2
    content = content[:metrics_func_end] + swagger_code + content[metrics_func_end:]
    total_features += 1
    features_list.append("✓ 添加Swagger/OpenAPI自动文档 (/docs/)")
    print("   ✓ 已添加Swagger UI文档端点")
else:
    print("   ⊗ Swagger已存在或插入点未找到")

# 保存所有修改
with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 80)
print(f"核心功能实现完成！共添加 {total_features} 个新特性")
print("=" * 80)
