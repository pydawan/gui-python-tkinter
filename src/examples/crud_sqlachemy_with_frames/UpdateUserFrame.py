# -*- coding: utf-8 -*-
"""."""
import tkinter as tk
from tkinter.messagebox import showerror, showinfo

from database.SQLAchemyConnectSQLite import Users
from style.material_design_colors import red


class UpdateUserFrame(tk.Frame):
    def __init__(self, master=None, data=None):
        super().__init__(master)
        self.master = master
        self.master.title(string='Adicionar Usuário')
        self.user_data = data

        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.user_id_value = tk.StringVar(value=self.user_data['text'])
        self.ent_name_value = tk.StringVar(value=self.user_data['values'][0])
        self.ent_age_value = tk.StringVar(value=self.user_data['values'][1])
        self.ent_gender_value = tk.StringVar(value=self.user_data['values'][2])

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

        lbl_name = tk.Label(
            master=self,
            text='Nome (Campo obrigatório):',
        )
        lbl_name.pack(anchor=tk.W)
        ent_name = tk.Entry(
            master=self,
            bg=red['100'],
            textvariable=self.ent_name_value,
            validate='key',
            validatecommand=(self.master.vcmd_empty_field, '%P', '%W'),
        )
        ent_name.pack(fill=tk.X, pady=(0, 15))

        lbl_age = tk.Label(
            master=self,
            text='Idade (Valores de 18 até 120):',
        )
        lbl_age.pack(anchor=tk.W)
        ent_age = tk.Entry(
            master=self,
            textvariable=self.ent_age_value,
            validate='key',
            validatecommand=(self.master.vcmd_age, '%P', '%W'),
        )
        ent_age.pack(fill=tk.X, pady=(0, 15))

        lbl_gender = tk.Label(
            master=self,
            text='Genero (Campo obrigatório):',
        )
        lbl_gender.pack(anchor=tk.W)
        ent_gender = tk.Entry(
            master=self,
            bg=red['100'],
            textvariable=self.ent_gender_value,
            validate='key',
            validatecommand=(self.master.vcmd_empty_field, '%P', '%W'),
        )
        ent_gender.pack(fill=tk.X, pady=(0, 15))

        btn_add_record = tk.Button(
            master=self,
            text='Atualizar registro',
            command=self.update_data,
        )
        btn_add_record.pack()

    def update_data(self):
        user_id = self.user_id_value.get()
        name = self.ent_name_value.get()
        age = int(self.ent_age_value.get())
        gender = self.ent_gender_value.get()
        if name and gender and self.master.check_age(age=age):
            new_data = {
                'name': name,
                'age': age,
                'gender': gender,
            }
            self.master.session.query(Users).filter(Users.user_id == user_id).update(new_data)
            self.master.session.commit()
            showinfo(
                parent=self.master,
                title='Usuário atualizado com sucesso',
                message='Usuário atualizado com sucesso',
            )
        else:
            showerror(
                parent=self.master,
                title='Formulário possui campos incorretos',
                message='Formulário possui campos incorretos!',
            )


if __name__ == '__main__':
    from MainWindow import MainWindow

    app = MainWindow()
    data = app.session.query(Users).filter(Users.user_id == 1).first()
    if data:
        user = {
            'text': data.user_id,
            'values': [data.name, data.age, data.gender],
        }
        UpdateUser(master=app, data=user)
        app.mainloop()
    print('Não foi possível localizar ou banco vazio!')
