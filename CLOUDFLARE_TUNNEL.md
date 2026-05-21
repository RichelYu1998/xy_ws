# Cloudflare Tunnel 配置指南

## 什么是 Cloudflare Tunnel？

Cloudflare Tunnel 是一个免费的隧道服务，提供：
- ✅ 固定的公网域名（如 `yourname.pages.dev`）
- ✅ 自动 HTTPS
- ✅ 全球 CDN 加速
- ✅ 无需手动重启，永久在线

## 配置步骤

### 1. 在本地安装 cloudflared

在你的**本地电脑**（不是服务器）上安装 cloudflared：

#### Windows:
```bash
# 使用 Chocolatey
choco install cloudflared

# 或手动下载
# 访问 https://github.com/cloudflare/cloudflared/releases
# 下载最新版本的 cloudflared-windows-amd64.exe
# 重命名为 cloudflared.exe 并放到 PATH 目录
```

#### Linux/Mac:
```bash
# 使用 Homebrew (Mac)
brew install cloudflared

# 或使用包管理器
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/
```

### 2. 登录 Cloudflare

在**本地电脑**上运行：

```bash
cloudflared tunnel login
```

这会打开浏览器，让你选择要使用的域名并授权。

### 3. 创建隧道

在**本地电脑**上运行：

```bash
# 创建一个新隧道
cloudflared tunnel create my-tunnel

# 输出示例：
# Created tunnel my-tunnel with id: 12345678-1234-1234-1234-123456789012
# Account ID: 98765432-9876-9876-9876-987654321098
```

请记录下输出的 **Tunnel ID** 和 **Account ID**。

### 4. 获取凭证文件

在**本地电脑**上运行：

```bash
# 下载凭证文件到本地
cloudflared tunnel token 12345678-1234-1234-1234-123456789012 > 12345678-1234-1234-1234-123456789012.json
```

这会生成一个 JSON 凭证文件。

### 5. 上传凭证文件到服务器

将生成的凭证文件上传到服务器的 `file/` 目录，文件名必须为：`<tunnel-id>.json`

例如：
```
file/12345678-1234-1234-1234-123456789012.json
```

### 6. 配置 Web 应用

有两种方式配置：

#### 方式 1: 通过 Web 界面配置（推荐）

1. 启动 Web 应用：`python main.py`
2. 打开浏览器访问 `http://localhost:8888`
3. 点击"隧道共享"按钮
4. 点击"配置 Cloudflare"按钮
5. 上传凭证文件（或手动上传到 `file/` 目录）
6. 在配置面板中填写：
   - **Tunnel ID**: `12345678-1234-1234-1234-123456789012`
   - **Tunnel Name**: `my-tunnel`
   - **Account ID**: `98765432-9876-9876-9876-987654321098`
7. 点击"保存配置"

#### 方式 2: 手动创建配置文件

创建文件 `file/cloudflare_tunnel.txt`，内容如下：
```
Tunnel ID: 12345678-1234-1234-1234-123456789012
Tunnel Name: my-tunnel
Account ID: 98765432-9876-9876-9876-987654321098
```

### 6. 启动隧道

在 Web 界面点击"隧道共享"按钮，系统会自动：
- 检测到 Cloudflare Tunnel 配置
- 启动 Cloudflare Tunnel
- 显示固定的公网地址

## 优势对比

| 特性 | hostc | Cloudflare Tunnel |
|------|-------|------------------|
| 固定域名 | ❌ 随机变化 | ✅ 固定域名 |
| 免费 | ✅ | ✅ |
| 自动 HTTPS | ✅ | ✅ |
| 全球 CDN | ❌ | ✅ |
| 速度 | 一般 | 快 |
| 配置复杂度 | 简单 | 中等 |

## 常见问题

### Q: Cloudflare Tunnel 启动失败？
A: 检查以下几点：
1. 确认 `cloudflared` 已正确安装
2. 确认凭证文件已下载到 `file/` 目录
3. 确认 Tunnel ID 和 Account ID 正确

### Q: 如何切换回 hostc？
A: 删除 `file/cloudflare_tunnel.txt` 文件，系统会自动使用 hostc。

### Q: 如何获取固定域名？
A: Cloudflare Tunnel 默认提供固定域名，格式为 `*.trycloudflare.com`。
如果需要自定义域名，需要在 Cloudflare Dashboard 中配置。

### Q: 隧道会自动重启吗？
A: 会！Cloudflare Tunnel 会自动保持连接，无需手动干预。

## 技术支持

如遇到问题，请检查：
1. `cloudflared` 是否在 PATH 中
2. 凭证文件路径是否正确
3. 网络连接是否正常

## 相关链接

- [Cloudflare Tunnel 官方文档](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [cloudflared GitHub](https://github.com/cloudflare/cloudflared)