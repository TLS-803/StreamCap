#!/usr/bin/env python3
"""
macOS应用程序启动器
确保应用程序在macOS上作为GUI应用程序正确启动
"""
import sys
import os

def main():
    # 确保在macOS上正确设置GUI环境
    if sys.platform == "darwin":
        # 设置macOS GUI应用程序环境
        os.environ['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))
        
        # 导入并启动主应用程序
        try:
            from main import main as app_main
            app_main()
        except ImportError:
            # 如果在打包环境中，尝试直接导入
            import main
            main.main()
    else:
        # 非macOS系统，直接启动
        from main import main as app_main
        app_main()

if __name__ == "__main__":
    main()