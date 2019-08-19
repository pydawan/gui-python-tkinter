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
    combobox_values = (
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    )

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        self.combobox_value = tk.StringVar()
        combobox = ttk.Combobox(
            master=self,
            text='Texto que se deseja exibir no label',
            textvariable=self.combobox_value,
            values=self.combobox_values,
        )
        combobox.current(0)
        combobox.bind(sequence='<<ComboboxSelected>>', func=self.on_combobox_selected)
        combobox.pack(expand=True)

    def on_combobox_selected(self, event):
        print(f'Mês selecionado: {self.combobox_value.get()}')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
