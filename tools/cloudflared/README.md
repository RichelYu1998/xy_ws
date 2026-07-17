# cloudflared 二进制文件

本目录包含 cloudflared 隧道工具的二进制文件，按操作系统分类存储。

## 版本信息
- 版本: 2026.7.2
- 发布日期: 2026-07-15

## 文件夹结构

```
cloudflared/
├── windows/
│   └── cloudflared.exe          # Windows amd64
├── linux/
│   └── cloudflared              # Linux amd64
├── macos/
│   ├── cloudflared-amd64        # macOS Intel (x86_64)
│   └── cloudflared-arm64        # macOS Apple Silicon (ARM64)
├── download_cloudflared.ps1     # 下载脚本
└── README.md                    # 本文件
```

## 文件列表

| 平台 | 架构 | 文件路径 | 大小 |
|------|------|----------|------|
| Windows | amd64 | `windows/cloudflared.exe` | ~52 MB |
| Linux | amd64 | `linux/cloudflared` | ~50 MB |
| macOS | amd64 (Intel) | `macos/cloudflared-amd64` | ~50 MB |
| macOS | arm64 (Apple Silicon) | `macos/cloudflared-arm64` | ~50 MB |

## 使用说明

### Windows
```powershell
.\windows\cloudflared.exe tunnel --url http://localhost:8888
```

### Linux
```bash
chmod +x linux/cloudflared
./linux/cloudflared tunnel --url http://localhost:8888
```

### macOS
```bash
# Apple Silicon (M1/M2/M3)
chmod +x macos/cloudflared-arm64
./macos/cloudflared-arm64 tunnel --url http://localhost:8888

# Intel Mac
chmod +x macos/cloudflared-amd64
./macos/cloudflared-amd64 tunnel --url http://localhost:8888
```

## 下载方式

### 方法 1: 运行下载脚本
```powershell
# Windows PowerShell
.\download_cloudflared.ps1
```

### 方法 2: 手动下载
访问: https://github.com/cloudflare/cloudflared/releases/tag/2026.7.2

下载以下文件到对应目录:
- `windows/cloudflared.exe` (重命名为 cloudflared.exe)
- `linux/cloudflared` (重命名为 cloudflared)
- `macos/cloudflared-amd64` (重命名为 cloudflared-amd64)
- `macos/cloudflared-arm64` (重命名为 cloudflared-arm64)

### 方法 3: 使用 curl
```bash
# Linux
curl -L https://github.com/cloudflare/cloudflared/releases/download/2026.7.2/cloudflared-linux-amd64 -o linux/cloudflared

# macOS Intel
curl -L https://github.com/cloudflare/cloudflared/releases/download/2026.7.2/cloudflared-darwin-amd64.tgz | tar xz -C macos && mv macos/cloudflared macos/cloudflared-amd64

# macOS Apple Silicon
curl -L https://github.com/cloudflare/cloudflared/releases/download/2026.7.2/cloudflared-darwin-arm64.tgz | tar xz -C macos && mv macos/cloudflared macos/cloudflared-arm64
```

## 官方文档
https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/