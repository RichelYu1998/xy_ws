import json
import os

# 创建生产环境配置
production_config = {
    "version": "3.8.71",
    "environment": "production",
    "rate_limiting": {
        "api_endpoints": {"max_requests_per_minute": 200, "window_seconds": 60, "enabled": True},
        "upload_endpoints": {"max_requests_per_minute": 10, "window_seconds": 60, "enabled": True}
    },
    "caching": {
        "json_files": {"ttl_seconds": 30, "max_cache_size_mb": 100, "enabled": True,
                      "monitoring": {"log_cache_hits": True, "log_cache_misses": True}}
    },
    "logging": {"level": "INFO", "file": "logs/app.log"},
    "health_check": {"cpu_warning_threshold_percent": 80, "memory_warning_threshold_percent": 80},
    "monitoring": {"prometheus_enabled": True, "metrics_endpoint": "/metrics"}
}

with open(r'D:\ws\xy_ws\config\production.json', 'w', encoding='utf-8') as f:
    json.dump(production_config, f, indent=2, ensure_ascii=False)

# 创建Staging配置
staging_config = production_config.copy()
staging_config['environment'] = 'staging'
staging_config['rate_limiting']['api_endpoints']['max_requests_per_minute'] = 1000
staging_config['logging']['level'] = 'DEBUG'

with open(r'D:\ws\xy_ws\config\staging.json', 'w', encoding='utf-8') as f:
    json.dump(staging_config, f, indent=2, ensure_ascii=False)

print("✅ 配置文件创建完成")
print("   - config/production.json")
print("   - config/staging.json")
