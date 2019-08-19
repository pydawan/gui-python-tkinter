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
    # Cores material design.
    # Arquivo material_design_colors.py está na pasta style.
    blue = {'500': '#2196F3'}
    red = {'500': '#F44336'}

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Registrando o validador.
        self.vcmd_empty_field = self.master.register(self.validate_empty_field)

        style = ttk.Style()
        style.configure('bg.blue.TEntry', foreground=self.blue['500'])
        style.configure('bg.red.TEntry', foreground=self.red['500'])

        self.entry_value = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):

        entry = ttk.Entry(
            master=self,
            style='bg.red.TEntry',
            textvariable=self.entry_value,
            validate='key',
            validatecommand=(self.vcmd_empty_field, '%P', '%W'),
        )
        entry.pack(expand=True)

    def validate_empty_field(self, p, w):
        """Validar se o Entry está vazio.

        :param p: (str) Valor que está sendo digitado no Entry.
        :param w: (str) Nome do widget que está sendo validado.
        :return: (bool) True para que a validação seja constante.
        """
        widget = self.nametowidget(w)
        if len(p) > 3:
            widget['style'] = 'bg.blue.TEntry'
        else:
            widget['style'] = 'bg.red.TEntry'
        return True


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
