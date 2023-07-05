import sys
import os

from cx_Freeze import setup, Executable

file =['assets','database']

exe = Executable(script = "app.py", base = "Win32GUI")

setup(
    name = "Sistema de reservacion de JDE",
    version = "1.0",
    description = "Sistema de reservacion para el hotel JDE",
    author = "David Basantes",
    options ={'build_exe': {'include_files': file}},
    executables=[exe]
)