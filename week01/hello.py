# 环境自检：确认 Python 和路径都对
import platform
import sys
from pathlib import Path

print("Python 版本：", sys.version.split()[0])
print("解释器路径：", sys.executable)
print("操作系统：", platform.system(), platform.release())
print("当前目录：", Path.cwd())
print("脚本位置：", Path(__file__).resolve())

# 判断是否踩了 Windows 的“应用商店 Python 别名”坑
if "WindowsApps" in sys.executable:
    print("\n[警告] 你用的是应用商店的占位 Python，建议重装官方版并勾选 Add to PATH")
else:
    print("\n环境正常，可以开始写代码了")
