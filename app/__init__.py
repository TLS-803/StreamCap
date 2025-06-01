import os
import sys

from .installation_manager import InstallationManager

# 获取正确的执行目录，兼容打包后的应用
if getattr(sys, 'frozen', False):
    # 如果是打包后的应用，使用_MEIPASS目录
    if hasattr(sys, '_MEIPASS'):
        execute_dir = sys._MEIPASS
    else:
        execute_dir = os.path.dirname(sys.executable)
else:
    # 如果是开发环境
    execute_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

__all__ = ["InstallationManager", "execute_dir"]
