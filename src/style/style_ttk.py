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

        style = ttk.Style()
        style.configure('red.TLabel', foreground='red')
        style.configure('arial.16.bold.TLabel', font=('Helvetica', 16, 'bold'))
        style.configure('bg.blue.TLabel', background='blue')
        style.configure('padding.50.TLabel', padding=50)

        self.create_widgets()

    def create_widgets(self):
        label_1 = ttk.Label(
            master=self,
            text='Label 1',
            style='red.TLabel',
        )
        label_1.pack()

        label_2 = ttk.Label(
            master=self,
            text='Label 2',
            style='arial.16.bold.TLabel',
        )
        label_2.pack()

        label_3 = ttk.Label(
            master=self,
            text='Label 3',
            style='bg.blue.TLabel',
        )
        label_3.pack()

        label_4 = ttk.Label(
            master=self,
            text='Label 4',
            style='padding.50.TLabel',
        )
        label_4.pack()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
