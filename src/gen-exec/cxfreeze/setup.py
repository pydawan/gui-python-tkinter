# -*- coding: utf-8 -*-
"""."""
import os
import sys
import tkinter as tk
from pathlib import Path

from cx_Freeze import Executable, setup

root = tk.Tk()

tcl_lib_path = Path(root.tk.exprstring('$tcl_library'))
tk_lib_path = Path(root.tk.exprstring('$tk_library'))

os.environ['TCL_LIBRARY'] = str(tcl_lib_path)
os.environ['TK_LIBRARY'] = str(tk_lib_path)

base = None

build_exe_options = {
    'packages': ['tkinter'],
    'include_files': ['icons'],
}

# Windows.
if sys.platform == 'win32':
    base = 'Win32GUI'

    build_exe_options = {
        'packages': ['tkinter'],
        'include_files': [
            # Ajustar para o local onde o Python está instalado no Windows!
            os.path.join('C:\\Python37\\DLLs', 'tcl86t.dll'),
            os.path.join('C:\\Python37\\DLLs', 'tk86t.dll'),
            'icons',
        ]
    }

setup(
    name='MyApp',
    version='0.1',
    description='Criando executáveis com Cx_Freeze!',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            'MainWindow.py',
            base=base,
            icon='icons/icon.ico',
        ),
    ],
)
