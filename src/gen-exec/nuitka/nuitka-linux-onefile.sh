#!/usr/bin/env bash
python -m nuitka --standalone --follow-imports --plugin-enable=tk-inter MainWindow.py
