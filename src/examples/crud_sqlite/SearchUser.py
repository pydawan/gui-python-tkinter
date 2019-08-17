# -*- coding: utf-8 -*-
"""."""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror, askokcancel, showinfo

from UpdateUser import UpdateUser


class SearchUser(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title(string='Buscar usuário')
        icon_png = tk.PhotoImage(file='assets/icons/person.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.grab_set()

        self.ent_search_value = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(master=self)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        frame_search = tk.Frame(master=main_frame)
        frame_search.pack(fill=tk.X, side=tk.TOP)
        lbl_search = tk.Label(master=frame_search, text='Buscar por nome:')
        lbl_search.pack(expand=False, anchor=tk.W)
        ent_search = tk.Entry(
            master=frame_search,
            textvariable=self.ent_search_value,
        )
        ent_search.pack(expand=True, fill=tk.X, side=tk.LEFT, padx=(0, 15))
        btn_search = tk.Button(
            master=frame_search,
            text='Buscar',
            command=self.search_by_name,
        )
        btn_search.pack(side=tk.RIGHT)

        frame_treeview = tk.Frame(main_frame)
        frame_treeview.pack(expand=True, fill=tk.BOTH, pady=15)
        self.tree_view = ttk.Treeview(
            master=frame_treeview,
            columns=('nome', 'idade', 'genero'),

        )
        self.tree_view.heading(column='#0', text='ID do banco')
        self.tree_view.heading(column='nome', text='Nome')
        self.tree_view.heading(column='idade', text='Idade')
        self.tree_view.heading(column='genero', text='Gênero')
        self.tree_view.pack(expand=True, fill=tk.BOTH)

        frame_buttons = tk.Frame(master=main_frame)
        frame_buttons.pack(fill=tk.X, side=tk.BOTTOM)
        btn_edit = tk.Button(
            master=frame_buttons,
            text='Editar registro',
            command=self.edit_record,
        )
        btn_edit.pack(expand=True, side=tk.LEFT)
        btn_remove = tk.Button(
            master=frame_buttons,
            text='Remover registro',
            command=self.remove_record,
        )
        btn_remove.pack(expand=True, side=tk.RIGHT)

    def search_by_name(self):
        name = self.ent_search_value.get()
        data = self.master.database.find_by_name(name=name)
        self.tree_view.delete(*self.tree_view.get_children())
        if data:
            for row in data:
                self.tree_view.insert(
                    parent='',
                    index=tk.END,
                    text=f'{row[0]}',
                    values=(f'{row[1]}', f'{row[2]}', f'{row[3]}'),
                )
        else:
            showerror(
                parent=self,
                title='Não foi possível localizar',
                message=f'Usuário {name} não localizado',
            )

    def edit_record(self):
        index = self.tree_view.focus()
        if index:
            data = self.tree_view.item(index)
            UpdateUser(master=self.master, data=data)
            self.destroy()
            # self.tree_view.delete(*self.tree_view.get_children())
        else:
            showerror(
                parent=self,
                title='Nenhum item selecionado',
                message='Nenhum item selecionado',
            )

    def remove_record(self):
        index = self.tree_view.focus()
        if index:
            data = self.tree_view.item(index)
            response = askokcancel(
                parent=self,
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
                self.master.database.remove_row(rowid=data['text'])
                self.tree_view.delete(index)
                showinfo(
                    parent=self,
                    title='Registro removido com sucesso do banco',
                    message='Registro removido com sucesso do banco'
                )
            else:
                showinfo(
                    parent=self,
                    title='Operação cancelada',
                    message='Operação cancelada'
                )
        else:
            showerror(
                parent=self,
                title='Nenhum item selecionado',
                message='Nenhum item selecionado',
            )


if __name__ == '__main__':
    from MainWindow import MainWindow

    app = MainWindow()
    SearchUser(master=app)
    app.mainloop()
