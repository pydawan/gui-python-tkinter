@echo off
python -m nuitka --follow-imports --plugin-enable=tk-inter MainWindow.py
