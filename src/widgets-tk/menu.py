# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


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
        MyMenu(master=self)


class MyMenu(tk.Menu):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        menu_file = tk.Menu(master=self, tearoff=0)
        menu_file.add_command(label='New', command=None)
        menu_file.add_command(label='Open', command=None)
        menu_file.add_command(label='Save', command=None)
        menu_file.add_command(label='Quit', command=self._quit_app)
        self.add_cascade(label='File', menu=menu_file)

        menu_help = tk.Menu(master=self, tearoff=0)
        menu_help.add_command(label='About', command=None)
        self.add_cascade(label='Help', menu=menu_help)

        self.master.config(menu=self)

    def _quit_app(self):
        self.master.quit()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
