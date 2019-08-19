# -*- coding: utf-8 -*-
"""."""
import threading
import time
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Janela principal')
        icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.create_widgets()

    def create_widgets(self):
        MyFrame(master=self)


class MyFrame(ttk.Frame):
    running = False

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        self.progressbar_value = tk.DoubleVar(value=0)
        self.progressbar = ttk.Progressbar(
            master=self,
            variable=self.progressbar_value,
            maximum=100.1,
        )
        self.progressbar.pack(expand=True, fill=tk.X)

        self.btn_start_progressbar = ttk.Button(
            master=self,
            text='Iniciar barra de progresso',
            command=self.enable_thread,
        )
        self.btn_start_progressbar.pack(fill=tk.X)

        self.btn_stop_progressbar = ttk.Button(
            master=self,
            text='Parar barra de progresso',
            command=self.stop_progressbar,
        )
        self.btn_stop_progressbar.pack(fill=tk.X)

        self.btn_reset_progressbar = ttk.Button(
            master=self,
            text='Reiniciar barra de progresso',
            command=self.reset_progressbar,
        )
        self.btn_reset_progressbar.pack(fill=tk.X)

    def start_progressbar(self):
        self.running = True
        while self.progressbar_value.get() != 100.0 and self.running is True:
            print(self.progressbar_value.get())
            self.progressbar.step(amount=10)
            time.sleep(1)
        self.progressbar.stop()
        self.btn_start_progressbar['state'] = tk.ACTIVE

    def stop_progressbar(self):
        self.running = False
        self.btn_start_progressbar['state'] = tk.ACTIVE

    def reset_progressbar(self):
        self.progressbar_value.set(value=0)

    def enable_thread(self):
        threading.Thread(target=self.start_progressbar, daemon=True).start()
        self.btn_start_progressbar['state'] = tk.DISABLED


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
