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
        self.spinbox_1_value = tk.IntVar()
        spinbox_1 = ttk.Spinbox(
            master=self,
            from_=0,
            to=10,
            textvariable=self.spinbox_1_value
        )
        spinbox_1.pack(expand=True)

        self.spinbox_2_value = tk.IntVar()
        spinbox_2 = ttk.Spinbox(
            master=self,
            values=(1, 2, 3, 4, 5, 6, 7, 8, 10),
            textvariable=self.spinbox_2_value,
        )
        spinbox_2.pack(expand=True)

        button = ttk.Button(
            master=self,
            text='Capturar valor do Spinbox',
            command=self._get_spinbox_value,
        )
        button.pack(expand=True)

    def _get_spinbox_value(self):
        print(self.spinbox_1_value.get())
        print(self.spinbox_2_value.get())


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
