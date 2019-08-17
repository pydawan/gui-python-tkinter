# -*- coding: utf-8 -*-
"""."""
import tkinter as tk
from tkinter import font

from material_design_colors import red


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


class MyFrame(tk.Frame):
    FONT_ARIAL_16_BOLD_ITALIC = ('Arial', '16', 'bold italic')

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        BOLD = font.Font(weight='bold')
        ITALIC = font.Font(slant='italic')
        TIMES_12 = font.Font(family='Times New Roman', size=12)

        label_1 = tk.Label(
            master=self,
            text='Label 1',
            font=BOLD,
        )
        label_1.pack()

        label_2 = tk.Label(
            master=self,
            text='Label 2',
            font=ITALIC,
        )
        label_2.pack()

        label_3 = tk.Label(
            master=self,
            text='Label 3',
            fg=red['500'],
            font=TIMES_12,
        )
        label_3.pack()

        label_4 = tk.Label(
            master=self,
            text='Label 4',
            font=self.FONT_ARIAL_16_BOLD_ITALIC,
        )
        label_4.pack()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
