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
        self.scale_value = tk.DoubleVar()
        scale = ttk.Scale(
            master=self,
            variable=self.scale_value,
        )
        scale.pack(expand=True)

        button = ttk.Button(
            master=self,
            text='Capturar valor do Scale',
            command=self._get_scale_value,
        )
        button.pack(expand=True)

        self.label_value = tk.StringVar(value='Valor do Scale = 0.0')
        label = ttk.Label(
            master=self,
            textvariable=self.label_value,
        )
        label.pack(expand=True)

    def _get_scale_value(self):
        scale_value = self.scale_value.get()
        text = f'Valor do Scale = {scale_value:.2f}'
        self.label_value.set(value=text)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
