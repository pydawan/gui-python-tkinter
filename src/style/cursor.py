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
            text='Botão',
            cursor='target',
            command=self._on_button_clicked,
        )
        button.pack(fill=tk.X)

        button_icon = tk.PhotoImage(file='../assets/icons/flag-16x16.png')
        button_with_icon = tk.Button(
            master=self,
            text='Botão com ícone',
            image=button_icon,
            compound=tk.RIGHT,
            cursor='plus',
            command=self._on_button_clicked,
        )
        button_with_icon.photo = button_icon
        button_with_icon.pack(fill=tk.X)

    def _on_button_clicked(self):
        print('Botão pressionado!')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
