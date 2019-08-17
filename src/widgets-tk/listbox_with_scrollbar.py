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
        # Criando scrollbar para o exixo y.
        scrollbar_y = tk.Scrollbar(master=self, orient=tk.VERTICAL)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Criando um listbox.
        self.listbox = tk.Listbox(
            master=self,
            bd=0,
            yscrollcommand=scrollbar_y.set,
        )
        self.listbox.bind('<<ListboxSelect>>', self._on_line_selected)
        self.listbox.pack(expand=True, fill=tk.BOTH)

        # Configurando os valores de y para listbox.
        scrollbar_y['command'] = self.listbox.yview

        # Inserindo dados no listbox.
        for n in range(1, 100):
            text = f'Linha {n}'
            self.listbox.insert(tk.END, text)

    def _on_line_selected(self, event):
        row = self.listbox.get(self.listbox.curselection())
        print(f'{row} selecionada')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
