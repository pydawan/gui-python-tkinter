# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


class MainWindowFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        btn_add_record = tk.Button(
            master=self,
            text='Cadastrar novo usuário',
            command=self.open_add_user,
        )
        btn_add_record.pack(fill=tk.X)

        btn_search_record = tk.Button(
            master=self,
            text='Consultar registros',
            command=self.open_seach_users,
        )
        btn_search_record.pack(fill=tk.X)

    def open_add_user(self):
        self.master.change_to_add_user()

    def open_seach_users(self):
        self.master.change_to_search_user()


if __name__ == '__main__':
    pass
