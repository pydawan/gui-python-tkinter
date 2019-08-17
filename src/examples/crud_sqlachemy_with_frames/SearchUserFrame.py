# -*- coding: utf-8 -*-
"""."""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror, askokcancel, showinfo

from database.SQLAchemyConnectSQLite import Users


class SearchUserFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title(string='Buscar usuário')

        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.ent_search_value = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        btn_back_to_main_window_icon = tk.PhotoImage(file='assets/icons/button/arrow_back.png')
        btn_back_to_main_window = tk.Button(
            master=self,
            text='Voltar para a tela principal',
            image=btn_back_to_main_window_icon,
            compound=tk.LEFT,
            command=self.master.back_to_main_window,
        )
        btn_back_to_main_window.photo = btn_back_to_main_window_icon
        btn_back_to_main_window.pack(anchor=tk.W, pady=(0, 10))

        frame_search = tk.Frame(master=self)
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

        frame_treeview = tk.Frame(self)
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

        frame_buttons = tk.Frame(master=self)
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
        data = self.master.session.query(Users).filter(Users.name.ilike(f'%{name}%')).all()
        self.tree_view.delete(*self.tree_view.get_children())
        if data:
            for row in data:
                self.tree_view.insert(
                    parent='',
                    index=tk.END,
                    text=f'{row.user_id}',
                    values=(f'{row.name}', f'{row.age}', f'{row.gender}'),
                )
        else:
            showerror(
                parent=self.master,
                title='Não foi possível localizar',
                message=f'Usuário {name} não localizado',
            )

    def edit_record(self):
        index = self.tree_view.focus()
        if index:
            data = self.tree_view.item(index)
            self.master.change_to_update_user(data=data)
        else:
            showerror(
                parent=self.master,
                title='Nenhum item selecionado',
                message='Nenhum item selecionado',
            )

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
                self.master.session.query(Users).filter(Users.user_id == data['text']).delete()
                self.master.session.commit()
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
    from MainWindow import MainWindow

    app = MainWindow()
    SearchUser(master=app)
    app.mainloop()
