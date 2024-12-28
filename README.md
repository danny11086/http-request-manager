# HTTP Request Manager

一个跨平台的HTTP请求管理工具，支持多种请求方式，提供友好的用户界面和响应数据管理功能。

## 功能特点

- 支持多种HTTP请求方法（GET、POST、PUT、DELETE、OPTIONS）
- 自定义请求头和参数设置
- JSON数据自动格式化
- 保存响应为Postman兼容的HAR文件
- 美观的分栏式用户界面

## 安装

### 从源码安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/[your-username]/http-request-manager.git
   cd http-request-manager
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

### 使用打包版本

- Windows: 下载并运行 `http-request-manager.exe`
- MacOS: 下载并安装 `http-request-manager.app`
- Linux: 下载并运行 `http-request-manager.AppImage`

## 开发环境设置

1. 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

2. 安装开发依赖：
   ```bash
   pip install -r requirements-dev.txt
   ```

## 打包说明

### Windows打包
```bash
pyinstaller --name http-request-manager --windowed --icon=assets/icon.ico app/main.py
```

### MacOS打包
```bash
pyinstaller --name "HTTP Request Manager" --windowed --icon=assets/icon.icns app/main.py
```

### Linux打包
```bash
pyinstaller --name http-request-manager --windowed app/main.py
```

## 使用说明

1. 选择请求方法（GET、POST等）
2. 输入请求名称和URL
3. 添加请求参数（JSON格式）
4. 添加请求头（可选）
5. 点击"Send Request"发送请求
6. 在右侧面板查看响应结果
7. 点击"Save as HAR"保存响应

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

[MIT License](LICENSE) 