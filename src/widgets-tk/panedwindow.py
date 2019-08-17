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
        MyPanedWindow(master=self)


class MyPanedWindow(tk.PanedWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Aplicando cor para visualizar o painel.
        self['bg'] = 'red'
        self.orient = tk.HORIZONTAL
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        self.add(child=MyFrame1(master=self))
        self.add(child=MyFrame2(master=self))


class MyFrame1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'green'
        self.pack(expand=True, fill=tk.BOTH)

        self.create_widgets()

    def create_widgets(self):
        for n in range(1, 3):
            button = tk.Button(
                master=self,
                text=f'Botão {n} do frame 1',
            )
            button.pack(expand=False, fill=tk.X)


class MyFrame2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'blue'
        self.pack(expand=True, fill=tk.BOTH)

        self.create_widgets()

    def create_widgets(self):
        for n in range(1, 3):
            button = tk.Button(
                master=self,
                text=f'Botão {n} do frame 2',
            )
            button.pack(expand=False, fill=tk.X)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
