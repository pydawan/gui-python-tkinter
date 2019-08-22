# -*- coding: utf-8 -*-
"""
Progressbar
===========

principais opções
-----------------

- `cursor`: (`str`) Cursor que é exibido quando o mouse passa sobre o
widget. [Clique aqui](../extras/cursor.md) para ver os cursores válidos.
- `length`: (`int` ou `float`) Tamanho (em pixels) do widget ao longo
do eixo (x ou y).
- `maximum`: Valor maximo do indicador. O valor padrão é 100.
- `mode`: (`str`) determina o tipo do progressbar, os valores válidos
são:
    - `mode='indeterminate'` Marcador vai e volta no eixo determinado.
    - `mode='determinate'` Marcador vai até o final do eixo e inicia
    novamente.
- **`orient`**: Especifica o eixo de posição do widget. O valor padrão
é horizontal, valores válidos são:
    - `orient=tk.HORIZONTAL`.
    - `orient=tk.VERTICAL`.
- **`style`**: Estilo que será aplicado ao widget.
- **`takefocus`**: Parâmetro determina se o widget deve receber foco.
O padrão é `False`.
- **`variable`**: Determina o tipo de variável que será recebida pelo
widget (`tk.DoubleVar()`, `tk.IntVar()` ou `tk.StringVar()`).

Métodos
-------

- `start([interval])`: Inicia o widget, pode ser passado um valor que
irá determinal a atualização automatica do valor. O valor padrão é de
`50ms` (milesegundos).
- `step([delta])`: Determina de quando em quanto o widget deve ser
incrementado. O valor padrão é `1.0`.
- `stop()`: Finaliza a execução do widget e retorna o valor para 0 (zero).
"""
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
        progressbar_1 = ttk.Progressbar(master=self)
        progressbar_1.pack(expand=True, fill=tk.X)
        progressbar_1.start()

        progressbar_2 = ttk.Progressbar(
            master=self,
            mode='indeterminate',
        )
        progressbar_2.pack(expand=True, fill=tk.X)
        progressbar_2.start()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
