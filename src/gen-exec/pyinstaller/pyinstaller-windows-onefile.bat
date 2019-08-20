@echo off
pyinstaller --noconfirm --log-level=WARN ^
    --onefile ^
    --windowed ^
    --hidden-import="tkinter" ^
    --add-data="icons/icon.png;icons" ^
    --icon="icons/icon.ico" ^
    --name=MyApp ^
    MainWindow.py
