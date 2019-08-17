# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Olá Mundo')
        icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        # Protocolo é disparado quando a janela principal é fechada.
        self.protocol("WM_DELETE_WINDOW", self._on_mainwindow_closed)
        self.protocol("WM_TAKE_FOCUS", print('focus'))
        self.protocol("WM_SAVE_YOURSELF", print('save'))

        self.create_widgets()

    def create_widgets(self):
        MyFrame(master=self)

    def _on_mainwindow_closed(self):
        print('A janela principal foi fechada.')
        # Finalizando a janela principal.
        self.quit()


class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            master=self,
            text='Callback será executado quando a janela principal for fechada!'
        )
        self.label.pack(expand=True, fill=tk.BOTH)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
