# -*- coding: utf-8 -*-
"""."""

import random
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Plotar Gráfico')
        icon_png = tk.PhotoImage(file='assets/icons/icon.png')
        self.iconphoto(True, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.create_widgets()

    def create_widgets(self):
        MainWindowFrame(master=self)


class MainWindowFrame(tk.Frame):
    FONT_ARIAL_16_BOLD_ITALIC = ('Arial', '16', 'bold italic')

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        frame_title = tk.Frame(master=self)
        frame_title.pack(side=tk.TOP)
        label_title = tk.Label(
            master=frame_title,
            text='Plotar gráfico',
            font=self.FONT_ARIAL_16_BOLD_ITALIC,
        )
        label_title.pack()

        frame_graph = tk.Frame(master=self)
        frame_graph.pack(expand=True, fill=tk.BOTH)

        # Contêiner para os elementos do plot (top level).
        figure = Figure(figsize=(2, 1))
        figure.subplots_adjust(left=0.08, bottom=0.18, right=0.98, top=0.97)

        # subplot(nrows, ncols, index).
        self.axes = figure.add_subplot(1, 1, 1)

        # FigureCanvasTkAgg é um widget do matplotlib que se integra com o Tkinter.
        self.canvas = FigureCanvasTkAgg(
            master=frame_graph,
            figure=figure,
        )
        self.canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

        frame_button = tk.Frame(master=self)
        frame_button.pack()
        btn_plot_graph = tk.Button(
            master=frame_button,
            text='Criar gráfico',
            command=self.plot_graph,
        )
        btn_plot_graph.pack(pady=(5, 0))

        # Para que permite a interação com o gráfico.
        toolbar = NavigationToolbar2Tk(window=self.master, canvas=self.canvas)
        toolbar.update()

    def plot_graph(self):
        # Limpando o gráfico existente.
        self.axes.cla()

        # Texto dos eixos
        self.axes.set_xlabel(xlabel='Eixo X')
        self.axes.set_ylabel(ylabel='Eixo Y')

        # Definindo o limite inferior e superior dos eixos.
        self.axes.set_ylim(bottom=-0.5, top=10.5)
        self.axes.set_xlim(left=-0.5, right=10.5)

        # Este grid() é a grade do gráfico e não o grid() do Tkinter.
        self.axes.grid()

        # Valores valores do eixo y gerados de forma aleatória.
        valores_y = [random.randint(0, 10) for _ in range(11)]

        # Plotando/Criando o gráfico.
        # Os valores do eixo x é um range de 0 a 10).
        self.axes.plot(range(11), valores_y, marker='o', color='orange')

        # Desenhando o gráfico na tela.
        self.canvas.draw()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
