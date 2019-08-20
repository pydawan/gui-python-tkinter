#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
    --onefile \
    --windowed \
    --hidden-import="tkinter" \
    --add-data="icons/icon.png:icons" \
    --name=MyApp \
    MainWindow.py
