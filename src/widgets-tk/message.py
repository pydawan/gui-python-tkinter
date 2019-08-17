# -*- coding: utf-8 -*-
"""``tk.Message()`` é uma variação do ``tk.Label()`` que permite a
exibição de texto em múltiplas linhas e a quebra de linha é automática.
"""
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
        MyFrame(master=self)


class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        message = tk.Message(
            master=self,
            text='Se o texto for grande a quebra de linha é automática!',
            width=100,
        )
        message.pack(expand=True, fill=tk.BOTH)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
