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
        MyPanedWindow(master=self)


class MyPanedWindow(ttk.PanedWindow):
    def __init__(self, master=None):
        super().__init__(master, orient=tk.HORIZONTAL)
        self.master = master
        # Aplicando cor para visualizar o painel.
        style = ttk.Style()
        style.configure('bg.red.TFrame', background='red')
        self['style'] = 'bg.red.TFrame'
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        self.add(child=MyFrame1(master=self))
        self.add(child=MyFrame2(master=self))


class MyFrame1(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        style = ttk.Style()
        style.configure('bg.green.TFrame', background='green')
        self['style'] = 'bg.green.TFrame'
        self.pack(expand=True, fill=tk.BOTH)

        self.create_widgets()

    def create_widgets(self):
        for n in range(1, 3):
            button = ttk.Button(
                master=self,
                text=f'Botão {n} do frame 1',
            )
            button.pack(expand=False, fill=tk.X)


class MyFrame2(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        style = ttk.Style()
        style.configure('bg.blue.TFrame', background='blue')
        self['style'] = 'bg.blue.TFrame'
        self.pack(expand=True, fill=tk.BOTH)

        self.create_widgets()

    def create_widgets(self):
        for n in range(1, 3):
            button = ttk.Button(
                master=self,
                text=f'Botão {n} do frame 2',
            )
            button.pack(expand=False, fill=tk.X)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
