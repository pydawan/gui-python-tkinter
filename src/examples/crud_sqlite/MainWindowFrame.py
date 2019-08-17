# -*- coding: utf-8 -*-
"""."""
import tkinter as tk

from AddUser import AddUser
from SearchUser import SearchUser


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
        AddUser(master=self.master)

    def open_seach_users(self):
        SearchUser(master=self.master)


if __name__ == '__main__':
    from MainWindow import MainWindow

    app = MainWindow()
    MainWindowFrame(master=app)
    app.mainloop()
