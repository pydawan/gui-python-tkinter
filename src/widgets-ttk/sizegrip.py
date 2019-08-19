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
        # Área para ajustar o tamanho da janela no canto inferior direito.
        sizegrip = ttk.Sizegrip(master=self)
        sizegrip.pack(side=tk.BOTTOM, anchor=tk.E)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
