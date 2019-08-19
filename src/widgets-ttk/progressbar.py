# -*- coding: utf-8 -*-
"""."""
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
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        progressbar_1 = ttk.Progressbar(master=self)
        progressbar_1.pack(expand=True, fill=tk.X)
        progressbar_1.start()

        progressbar_2 = ttk.Progressbar(
            master=self,
            mode='indeterminate',
        )
        progressbar_2.pack(expand=True, fill=tk.X)
        progressbar_2.start()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
