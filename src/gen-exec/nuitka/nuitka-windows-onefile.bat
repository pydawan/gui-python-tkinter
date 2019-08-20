@echo off
python -m nuitka --standalone --follow-imports --plugin-enable=tk-inter MainWindow.py
