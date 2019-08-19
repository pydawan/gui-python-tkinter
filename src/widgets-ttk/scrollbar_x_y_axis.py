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
        # Criando scrollbar para o eixo x.
        scrollbar_x = ttk.Scrollbar(master=self, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Criando scrollbar para o eixo y.
        scrollbar_y = ttk.Scrollbar(master=self, orient=tk.VERTICAL)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Criando uma área de texto.
        text_area = tk.Text(
            master=self,
            wrap=tk.NONE,
            bd=0,
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set,
        )
        text_area.pack(expand=True, fill=tk.BOTH)

        # Configurando os valores dos eixo para o scrollbar.
        scrollbar_x['command'] = text_area.xview
        scrollbar_y['command'] = text_area.yview

        # Inserindo dados na área de texto.
        for n in range(1, 100):
            text = f'Linha {n} ' * 20 + '\n'
            text_area.insert(index=tk.END, chars=text)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
