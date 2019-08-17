# -*- coding: utf-8 -*-
"""."""
import tkinter as tk

from AddUserFrame import AddUserFrame
from MainWindowFrame import MainWindowFrame
from SearchUserFrame import SearchUserFrame
from UpdateUserFrame import UpdateUserFrame
from database import SQLAchemyConnectSQLite as sqla
from style.material_design_colors import red, blue


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='CRUD com SQLite')
        icon_png = tk.PhotoImage(file='assets/icons/icon.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.protocol("WM_DELETE_WINDOW", self.on_window_closed)

        self.vcmd_empty_field = self.register(self.validate_empty_field)
        self.vcmd_age = self.register(self.validate_age)

        # Acessando o banco.
        engine = sqla.engine

        # Criando todas as tabelas.
        sqla.Base.metadata.create_all(engine)

        # Criando uma sessão (add, commit, query, etc).
        self.session = sqla.Session()

        # Registrando os frames.
        self.frames = {
            'MainWindowFrame': MainWindowFrame,
            'AddUserFrame': AddUserFrame,
            'SearchUserFrame': SearchUserFrame,
            'UpdateUserFrame': UpdateUserFrame,
        }
        self.current_frame = None

        self.create_widgets()

    def create_widgets(self):
        self.current_frame = self.frames['MainWindowFrame'](master=self)

    def on_window_closed(self):
        """Método é executado quando a janela principal é fechada."""
        self.session.close()
        print('Conexão com o banco fechada')
        self.quit()

    def back_to_main_window(self):
        self.winfo_children()[0].destroy()
        self.current_frame = self.frames['MainWindowFrame'](master=self)

    def change_to_add_user(self):
        self.winfo_children()[0].destroy()
        self.current_frame = self.frames['AddUserFrame'](master=self)

    def change_to_search_user(self):
        self.winfo_children()[0].destroy()
        self.current_frame = self.frames['SearchUserFrame'](master=self)

    def change_to_update_user(self, data):
        self.winfo_children()[0].destroy()
        self.current_frame = self.frames['UpdateUserFrame'](master=self, data=data)

    def validate_empty_field(self, p, w):
        widget = self.nametowidget(w)
        if len(p) > 0:
            widget['bg'] = blue['100']
        else:
            widget['bg'] = red['100']
        return True

    def validate_age(self, p, w):
        widget = self.nametowidget(w)
        if p.isdigit() and self.check_age(age=p):
            widget['bg'] = blue['100']
        else:
            widget['bg'] = red['100']
        return True

    @staticmethod
    def check_age(age):
        if 18 <= int(age) <= 120:
            return True
        return False


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
