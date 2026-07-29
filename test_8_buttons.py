import urllib.request
import json

base_url = "http://localhost:8888"

tests = [
    ("1.健康检查", f"{base_url}/health", "GET"),
    ("2.版本查询", f"{base_url}/api/version", "GET"),
    ("3.更新日志", f"{base_url}/api/changelog", "GET"),
    ("4.服务器信息", f"{base_url}/api/server/info", "GET"),
    ("5.隧道状态", f"{base_url}/api/tunnel/status", "GET"),
    ("6.URL源状态", f"{base_url}/api/url-source/status", "GET"),
    ("7.邮件配置", f"{base_url}/api/email/config", "GET"),
    ("8.文件清理列表", f"{base_url}/api/clean/list", "POST")
]

print("=" * 60)
print("🧪 测试8个主要功能按钮")
print("=" * 60)

passed = 0
failed = 0

for name, url, method in tests:
    try:
        if method == "GET":
            req = urllib.request.Request(url)
        else:
            req = urllib.request.Request(url, data=b"{}", method=method,
                                       headers={"Content-Type": "application/json"})
        
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            
            if name == "3.更新日志":
                print(f"✅ {name}: {len(data.get('changelog', []))}个版本")
            elif name == "4.服务器信息":
                print(f"✅ {name}: 端口{data.get('port')}")
            elif name == "5.隧道状态":
                url_val = data.get('url', 'N/A')
                print(f"✅ {name}: 运行={data.get('running')}, URL={str(url_val)[:30]}...")
            elif name == "6.URL源状态":
                print(f"✅ {name}: {data.get('status', 'OK')}")
            elif name == "7.邮件配置":
                enabled = data.get('config', {}).get('enabled')
                print(f"✅ {name}: 启用={enabled}")
            elif name == "8.文件清理列表":
                files_count = len(data.get('files_to_clean', []))
                print(f"✅ {name}: 可清理{files_count}个文件组")
            else:
                print(f"✅ {name}: 正常响应")
            
            passed += 1
            
    except Exception as e:
        print(f"❌ {name}: 失败 - {str(e)}")
        failed += 1

print("=" * 60)
print(f"📊 测试结果: ✅ {passed}个通过, ❌ {failed}个失败 (共{len(tests)}个)")
print("=" * 60)

if failed == 0:
    print("🎉 所有8个功能按钮都正常工作！")
else:
    print(f"⚠️ 有{failed}个功能需要检查")