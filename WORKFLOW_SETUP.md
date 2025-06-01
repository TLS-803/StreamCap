# GitHub Actions 工作流设置完成

## 📋 已创建的工作流

### 1. 🔨 build.yml - 构建和打包工作流

**文件位置**: `.github/workflows/build.yml`

**功能特性**:
- ✅ 监控主要文件变更（app/**, main.py, pyproject.toml, requirements.txt, assets/**, config/**, locales/**）
- ✅ 支持 Windows 和 macOS 平台构建
- ✅ 使用 Flet 框架打包桌面应用
- ✅ 自动从 pyproject.toml 提取版本信息
- ✅ 创建压缩包（Windows: .zip, macOS: .tar.gz）
- ✅ 上传构建产物到 GitHub Artifacts
- ✅ 自动创建和推送版本标签

**触发条件**:
- 推送到 main/master 分支
- Pull Request 到 main/master 分支
- 指定文件路径变更时

### 2. 🚀 release.yml - 发布工作流

**文件位置**: `.github/workflows/release.yml`

**功能特性**:
- ✅ 检测新版本标签（v*格式）
- ✅ 重新构建应用确保版本一致性
- ✅ 从 pyproject.toml 提取项目信息
- ✅ 创建 GitHub Release
- ✅ 生成详细发布说明
- ✅ 上传安装包到 Release

**触发条件**:
- 推送版本标签（如 v1.0.1）

## 🔧 配置详情

### 构建配置
- **Python版本**: 3.11
- **Windows图标**: `assets/icon.ico` ✅
- **macOS图标**: `assets/icons/Appicon.icns` ✅
- **包含目录**: assets/, config/, locales/
- **缓存策略**: pip依赖缓存

### 版本管理
- **版本源**: pyproject.toml 中的 project.version
- **当前版本**: 1.0.1
- **标签格式**: v{version} (如 v1.0.1)

### 构建产物
- **Windows**: StreamCap-Windows-v{version}.zip
- **macOS**: StreamCap-macOS-v{version}.dmg

## 📝 使用指南

### 发布新版本的完整流程：

1. **更新代码和版本**
   ```bash
   # 1. 修改代码
   git add .
   git commit -m "feat: 添加新功能"
   
   # 2. 更新版本号（编辑 pyproject.toml）
   # 将 version = "1.0.1" 改为 version = "1.0.2"
   
   # 3. 提交版本更新
   git add pyproject.toml
   git commit -m "bump: version to 1.0.2"
   git push origin main
   ```

2. **创建发布标签**
   ```bash
   # 创建并推送标签
   git tag v1.0.2
   git push origin v1.0.2
   ```

3. **自动化流程**
   - `build.yml` 在推送到 main 时运行 → 构建应用 → 创建标签
   - `release.yml` 在推送标签时运行 → 重新构建 → 创建 Release

### 监控构建状态
- 访问 GitHub 仓库的 "Actions" 页面
- 查看工作流运行状态和日志
- 下载构建产物（Artifacts）

### 手动触发
- 可以在 GitHub Actions 页面手动重新运行失败的工作流

## ⚠️ 注意事项

1. **版本一致性**: 确保 pyproject.toml 中的版本与标签版本一致
2. **标签格式**: 必须使用 `v` 前缀（如 v1.0.1）
3. **图标文件**: 确保图标文件存在且路径正确
4. **权限设置**: 确保 GitHub Actions 有推送标签的权限

## 🔍 故障排除

### 常见问题：

1. **构建失败**
   - 检查 requirements.txt 中的依赖
   - 确保 Python 版本兼容性
   - 查看 Actions 日志获取详细错误信息

2. **标签创建失败**
   - 检查是否已存在相同版本的标签
   - 确保有推送权限

3. **Release 创建失败**
   - 检查 GITHUB_TOKEN 权限
   - 确保构建产物存在

### 调试步骤：
1. 查看 GitHub Actions 日志
2. 检查文件路径和权限
3. 验证 pyproject.toml 语法
4. 确认依赖安装成功

## 📊 工作流状态

| 工作流 | 状态 | 最后运行 | 描述 |
|--------|------|----------|------|
| build.yml | ✅ 已配置 | 待运行 | 构建和打包 |
| release.yml | ✅ 已配置 | 待运行 | 发布管理 |

---

**设置完成时间**: 2025-06-01  
**配置版本**: v1.0  
**支持平台**: Windows, macOS  
**构建工具**: Flet, GitHub Actions