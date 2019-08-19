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
        MyNotebook(master=self)


class MyNotebook(ttk.Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('bg.red.TFrame', background='red')
        style.configure('bg.blue.TFrame', background='blue')

        frame_1 = ttk.Frame(master=self)
        frame_1['style'] = 'bg.red.TFrame'
        frame_1.pack(expand=True, fill=tk.BOTH)
        self.add(child=frame_1, text='Tab 1 (Frame 1)')

        label_frame_1 = ttk.Label(master=frame_1, text='Frame 1', background='red')
        label_frame_1.pack(expand=True)

        frame_2 = ttk.Frame(master=self)
        frame_2['style'] = 'bg.blue.TFrame'
        frame_2.pack(expand=True, fill=tk.BOTH)
        self.add(child=frame_2, text='Tab 2 (Frame 2)')

        label_frame_2 = ttk.Label(master=frame_2, text='Frame 2', background='blue')
        label_frame_2.pack(expand=True)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
