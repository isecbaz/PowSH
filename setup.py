import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["subprocess", "telebot", "winreg"],
    "include_files": [],
    "excludes": [],
    "optimize": 2,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # برای اجرای برنامه به صورت GUI بدون کنسول مورد نیاز است.

executables = [
    Executable("main.py", base=base, icon="icon.ico")
]

setup(
    name="secbaz",
    version="0.1",
    description="Telegram bot for managing PowerShell commands.",
    options={"build_exe": build_exe_options},
    executables=executables,
)
