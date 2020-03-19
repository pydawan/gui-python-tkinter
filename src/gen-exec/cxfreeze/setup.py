# -*- coding: utf-8 -*-
"""Gerando executáveis com Cx_Freeze!"""

import sys
import tkinter as tk
from os import environ
from pathlib import Path

from cx_Freeze import setup, Executable

root = tk.Tk()
lib_tcl_path = Path(root.tk.exprstring('$tcl_library'))
lib_tk_path = Path(root.tk.exprstring('$tk_library'))
environ['TCL_LIBRARY'] = str(lib_tcl_path)
environ['TK_LIBRARY'] = str(lib_tk_path)

build_exe_options = {
    'excludes': ['wx', 'email', 'pydoc_data', 'curses'],
    'include_files': ['icons'],
    'packages': ['tkinter'],
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
if sys.platform == 'win64':
    base = 'Win64GUI'

setup(
    name='MyApp',
    author='Renato Cruz (natorsc@gmail.com)',
    version='0.0.1',
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
