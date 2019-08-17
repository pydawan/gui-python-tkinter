# -*- coding: utf-8 -*-
"""."""
import tkinter as tk
from tkinter.messagebox import showerror, showinfo

from database.SQLAchemyConnectSQLite import Users
from style.material_design_colors import red


class AddUser(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title(string='Adicionar Usuário')
        icon_png = tk.PhotoImage(file='assets/icons/person.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.grab_set()

        self.ent_name_value = tk.StringVar()
        self.ent_age_value = tk.StringVar(value=0)
        self.ent_gender_value = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(master=self)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        lbl_name = tk.Label(
            master=main_frame,
            text='Nome (Campo obrigatório):',
        )
        lbl_name.pack(anchor=tk.W)
        ent_name = tk.Entry(
            master=main_frame,
            bg=red['100'],
            textvariable=self.ent_name_value,
            validate='key',
            validatecommand=(self.master.vcmd_empty_field, '%P', '%W'),
        )
        ent_name.pack(fill=tk.X, pady=(0, 15))

        lbl_age = tk.Label(
            master=main_frame,
            text='Idade (Valores de 18 até 120):',
        )
        lbl_age.pack(anchor=tk.W)
        ent_age = tk.Entry(
            master=main_frame,
            bg=red['100'],
            textvariable=self.ent_age_value,
            validate='key',
            validatecommand=(self.master.vcmd_age, '%P', '%W'),
        )
        ent_age.pack(fill=tk.X, pady=(0, 15))

        lbl_gender = tk.Label(
            master=main_frame,
            text='Gênero (Campo obrigatório):',
        )
        lbl_gender.pack(anchor=tk.W)
        ent_gender = tk.Entry(
            master=main_frame,
            bg=red['100'],
            textvariable=self.ent_gender_value,
            validate='key',
            validatecommand=(self.master.vcmd_empty_field, '%P', '%W'),
        )
        ent_gender.pack(fill=tk.X, pady=(0, 15))

        btn_add_record = tk.Button(
            master=main_frame,
            text='Adicionar registro',
            command=self.save_data,
        )
        btn_add_record.pack()

    def save_data(self):
        name = self.ent_name_value.get()
        age = int(self.ent_age_value.get())
        gender = self.ent_gender_value.get()
        if name and gender and self.master.check_age(age=age):
            user = Users()
            user.name = name
            user.age = age
            user.gender = gender
            self.master.session.add(user)
            self.master.session.commit()
            showinfo(
                parent=self,
                title='Usuário inserido com sucesso',
                message='Usuário inserido com sucesso',
            )
            self.destroy()
        else:
            showerror(
                parent=self,
                title='Formulário possui campos incorretos',
                message='Formulário possui campos incorretos!',
            )


if __name__ == '__main__':
    from MainWindow import MainWindow

    app = MainWindow()
    AddUser(master=app)
    app.mainloop()
