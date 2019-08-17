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
    # Cores material design.
    # Arquivo material_design_colors.py está na pasta style.
    blue = {'50': '#E3F2FD'}
    red = {'50': '#FFEBEE'}

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # Registrando o validador.
        vcmd_empty_field = self.master.register(self.validate_empty_field)

        # Variável que irá receber o valor do entry.
        # Assim não é preciso acessar diretamente o widget.
        self.entry_value = tk.StringVar()
        entry = tk.Entry(
            master=self,
            bg=self.red['50'],
            textvariable=self.entry_value,
            validate='key',
            validatecommand=(vcmd_empty_field, '%P', '%W'),
        )
        entry.pack(expand=True)

    def validate_empty_field(self, p, w):
        """Validar se o Entry está vazio.

        :param p: (str) Valor que está sendo digitado no Entry.
        :param w: (str) Nome do widget que está sendo validado.
        :return: (bool) True para que a validação seja constante.
        """
        widget = self.nametowidget(w)
        if len(p) > 0:
            widget['bg'] = self.blue['50']
        else:
            widget['bg'] = self.red['50']
        return True


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
