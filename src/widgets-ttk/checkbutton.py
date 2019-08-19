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
    group_checkbutton = []
    texts = ['Check Button 1', 'Check Button 2', 'Check Button 3']

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        for text in self.texts:
            int_var = tk.IntVar()
            checkbutton = ttk.Checkbutton(
                master=self,
                text=text,
                variable=int_var,
                command=self._on_checked,
            )
            checkbutton.pack(expand=True)
            self.group_checkbutton.append(int_var)

    def _on_checked(self):
        for index, value in enumerate(self.group_checkbutton):
            if value.get() == 1:
                print(self.texts[index])
        print('---')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
