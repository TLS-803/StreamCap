# GitHub Actions 工作流说明

本项目包含以下GitHub Actions工作流：

## 🔨 build.yml - 构建工作流

**触发条件：**
- 推送到 `main` 或 `master` 分支
- 对以下文件/目录的更改：
  - `app/**` - 应用程序源代码
  - `main.py` - 主程序文件
  - `pyproject.toml` - 项目配置
  - `requirements.txt` - Python依赖
  - `assets/**` - 资源文件
  - `config/**` - 配置文件
  - `locales/**` - 本地化文件

**功能：**
- 为 Windows 和 macOS 构建应用程序
- 使用 Flet 打包桌面应用
- 创建压缩包（Windows: .zip, macOS: .tar.gz）
- 上传构建产物到 GitHub Artifacts
- 自动创建版本标签（基于 pyproject.toml 中的版本）

**输出：**
- `StreamCap-Windows-v{version}.zip`
- `StreamCap-macOS-v{version}.dmg`

## 🚀 release.yml - 发布工作流

**触发条件：**
- 推送版本标签（格式：`v*`，如 `v1.0.1`）

**功能：**
- 重新构建应用程序确保版本一致性
- 从 `pyproject.toml` 提取版本和项目信息
- 创建 GitHub Release
- 上传安装包到 Release
- 生成详细的发布说明

**发布内容：**
- Windows 安装包 (.zip)
- macOS 磁盘映像 (.dmg)
- 自动生成的发布说明
- 安装指南

## 🐳 docker-build.yml - Docker构建工作流

**触发条件：**
- 推送版本标签
- 手动触发

**功能：**
- 构建多平台 Docker 镜像（linux/amd64, linux/arm64）
- 推送到 Docker Hub

## 🧪 test.yml - 测试工作流

**触发条件：**
- Pull Request 到 main 分支

**功能：**
- 运行单元测试
- 验证代码质量

## 🔄 python-lint.yml - 代码检查工作流

**功能：**
- Python 代码风格检查
- 代码质量分析

## 📋 使用说明

### 发布新版本的步骤：

1. **更新版本号**
   ```bash
   # 编辑 pyproject.toml 文件，更新 version 字段
   vim pyproject.toml
   ```

2. **提交更改**
   ```bash
   git add pyproject.toml
   git commit -m "Bump version to x.x.x"
   git push origin main
   ```

3. **创建版本标签**
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

4. **自动化流程**
   - `build.yml` 会在推送到 main 分支时自动运行
   - `release.yml` 会在推送标签时自动运行
   - 构建完成后，新的 Release 会自动创建并包含安装包

### 手动触发构建：

可以通过 GitHub Actions 页面手动触发 `docker-build.yml` 工作流。

### 监控构建状态：

在 GitHub 仓库的 "Actions" 标签页可以查看所有工作流的运行状态和日志。

## 🔧 配置要求

确保仓库设置了以下 Secrets（如果使用 Docker 构建）：
- `DOCKER_HUB_USERNAME` - Docker Hub 用户名
- `DOCKER_HUB_TOKEN` - Docker Hub 访问令牌

## 📝 注意事项

- 版本标签必须以 `v` 开头（如 `v1.0.1`）
- 确保 `pyproject.toml` 中的版本号与标签版本一致
- 构建需要的图标文件：
  - Windows: `assets/icon.ico`
  - macOS: `assets/icons/Appicon.icns`
- 构建过程会包含 `assets/`, `config/`, `locales/` 目录