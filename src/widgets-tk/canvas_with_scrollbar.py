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
    indigo = {'500': '#3F51B5'}
    blue = {'50': '#E3F2FD'}
    yellow = {'500': '#FFEB3B'}
    orange = {'500': '#FF9800'}

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # Criando scrollbar para o eixo x.
        scrollbar_x = tk.Scrollbar(master=self, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Criando scrollbar para o exixo y.
        scrollbar_y = tk.Scrollbar(master=self, orient=tk.VERTICAL)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Criando o canvas.
        canvas = tk.Canvas(
            master=self,
            bg=self.indigo['500'],
            # Pontos de origem e tamanho da área do canvas.
            scrollregion=(0, 0, 1920, 1080),
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set,
        )

        # Desenhando um retângulo.
        canvas.bbox(
            canvas.create_rectangle(10, 10, 1366, 768, fill=self.blue['50'])
        )

        # Desenhando uma linha.
        canvas.create_line((1920 / 2), 0, (1920 / 2), 1080, fill=self.yellow['500'])

        # Desenhando outra linha.
        canvas.create_line(0, (1080 / 2), 1920, (1080 / 2), fill=self.orange['500'])
        canvas.pack(expand=True, fill=tk.BOTH)

        canvas.create_oval(20, 20, 256, 128, fill=self.indigo['500'])
        canvas.pack()

        # Configurando o canvas no scroll.
        scrollbar_x['command'] = canvas.xview
        scrollbar_y['command'] = canvas.yview


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
