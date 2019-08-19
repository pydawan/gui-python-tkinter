# -*- coding: utf-8 -*-
"""."""
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, showerror


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
        self.tree_view = ttk.Treeview(
            master=self,
            columns=('nome', 'idade', 'genero'),
        )
        self.tree_view.heading(column='#0', text='ID do banco')
        self.tree_view.heading(column='nome', text='Nome')
        self.tree_view.heading(column='idade', text='Idade')
        self.tree_view.heading(column='genero', text='Gênero')
        self.tree_view.pack(expand=True, fill=tk.BOTH, pady=(0, 10))

        gender_list = ['Masculino', 'Feminino']
        for row in range(1, 11):
            self.tree_view.insert(
                parent='',
                index=tk.END,
                text=f'{row}',
                values=(f'Nome {row}', f'{17 + row}', random.choice(gender_list)),
            )

        btn_remove = ttk.Button(
            master=self,
            text='Remover registro',
            command=self.remove_record,
        )
        btn_remove.pack()

    def remove_record(self):
        index = self.tree_view.focus()
        if index:
            data = self.tree_view.item(index)
            response = askokcancel(
                parent=self.master,
                title="Confirmar exclusão",
                message=(
                    'Deseja remover o registro:\n'
                    f'ID:{data["text"]}:\n'
                    f'Nome: {data["values"][0]}\n'
                    f'Idade: {data["values"][1]}\n'
                    f'Gênero: {data["values"][2]}\n'
                )
            )
            if response:
                self.tree_view.delete(index)
                showinfo(
                    parent=self.master,
                    title='Registro removido com sucesso do banco',
                    message='Registro removido com sucesso do banco'
                )
            else:
                showinfo(
                    parent=self.master,
                    title='Operação cancelada',
                    message='Operação cancelada'
                )
        else:
            showerror(
                parent=self.master,
                title='Nenhum item selecionado',
                message='Nenhum item selecionado',
            )


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
