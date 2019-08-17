# -*- coding: utf-8 -*-
"""O tkinter posui 3 tipos messagebox:

- ``showerror()``.
- ``showwarning()``.
- ``showinfo()``.
"""
import tkinter as tk
from tkinter.messagebox import showinfo


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
        button = tk.Button(
            master=self,
            text='Abrir Tkinter messagebox',
            command=self._on_button_clicked,
        )
        button.pack(expand=True)

    def _on_button_clicked(self):
        showinfo(
            parent=self.master,
            title='Titulo da messagebox',
            message='Mensagem que será exibida na messagebox',
        )


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
