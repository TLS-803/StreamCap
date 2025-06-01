# GitHub Actions 工作流更改总结

## 📋 更改概述

本次更新创建了两个新的 GitHub Actions 工作流，用于自动化 StreamCap 项目的构建和发布流程。

## 🆕 新增文件

### 1. `.github/workflows/build.yml` - 构建工作流
**功能：**
- 自动构建 Windows 和 macOS 安装包
- 当主要文件更新时触发构建
- 自动创建版本标签

**触发条件：**
- 推送到 main/master 分支
- 修改以下文件时：
  - `*.py` (Python源码)
  - `pyproject.toml` (项目配置)
  - `requirements.txt` (依赖)
  - `assets/**` (资源文件)
  - `config/**` (配置文件)
  - `locales/**` (本地化文件)

**输出产物：**
- `StreamCap-Windows-v{version}.zip` - Windows 可执行文件
- `StreamCap-macOS-v{version}.dmg` - macOS 磁盘映像文件

### 2. `.github/workflows/release.yml` - 发布工作流
**功能：**
- 检测新的版本标签
- 自动创建 GitHub Release
- 从 pyproject.toml 提取版本信息
- 生成详细的发布说明

**触发条件：**
- 推送版本标签 (v*.*.*)

**发布内容：**
- Windows 安装包
- macOS 磁盘映像
- 自动生成的发布说明
- 安装指南

## 🔧 技术细节

### 构建配置
- **Python 版本**: 3.11
- **构建工具**: Flet
- **Windows 图标**: `assets/icon.ico`
- **macOS 图标**: `assets/icons/Appicon.icns`
- **DMG 背景**: `assets/images/dmg.jpg`

### 版本管理
- **版本源**: `pyproject.toml` 中的 `project.version`
- **当前版本**: 1.0.1
- **标签格式**: v{version} (如 v1.0.1)

### macOS DMG 特性
- 使用系统自带的 `hdiutil` 创建 DMG
- 包含 Applications 文件夹快捷方式
- 支持拖拽安装
- 自动压缩优化

## 📁 文档文件

### 3. `.github/workflows/README.md`
详细说明所有工作流的功能和配置

### 4. `WORKFLOW_SETUP.md`
完整的工作流设置指南和使用说明

## 🚀 使用流程

### 发布新版本：
1. 更新 `pyproject.toml` 中的版本号
2. 提交并推送到 main 分支
3. build.yml 自动构建并创建标签
4. release.yml 自动创建 Release

### 手动触发构建：
- 在 GitHub Actions 页面手动运行 build.yml

## ✅ 验证完成

- [x] YAML 语法验证通过
- [x] 版本提取功能测试通过
- [x] 文件路径验证完成
- [x] 图标文件存在确认
- [x] DMG 背景图片确认
- [x] 与现有工作流兼容性检查

## 🔄 与现有工作流的兼容性

新工作流与现有的以下工作流完全兼容：
- `docker-build.yml` - Docker 构建
- `python-lint.yml` - Python 代码检查
- `sync.yml` - 同步工作流
- `test.yml` - 测试工作流

## 📝 注意事项

1. **首次运行**：工作流需要在 GitHub 环境中首次运行以验证所有功能
2. **权限要求**：需要 GITHUB_TOKEN 权限来创建 Release 和上传文件
3. **依赖安装**：所有必需的依赖都会自动安装
4. **缓存优化**：使用 pip 缓存加速构建过程

## 🎯 下一步

工作流已准备就绪，可以：
1. 提交这些更改到仓库
2. 推送到 main 分支触发首次构建
3. 验证构建产物和发布流程