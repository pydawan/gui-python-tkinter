# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Janela principal')
        icon_png = tk.PhotoImage(file='icons/icon.png')
        self.iconphoto(True, icon_png)

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

        self.entry_value = tk.StringVar()
        self.label_value = tk.StringVar(
            value='Clique no botão e o texto será alterado'
        )

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(
            master=self,
            textvariable=self.entry_value,
        )
        entry.pack(fill=tk.X)

        label = tk.Label(
            master=self,
            textvariable=self.label_value,

        )
        label.pack(expand=True, fill=tk.BOTH)

        button = tk.Button(
            master=self,
            text='Clique Aqui',
            command=self.on_button_clicked,
        )
        button.pack(fill=tk.X)

    def on_button_clicked(self):
        text = self.entry_value.get()
        if text:
            self.label_value.set(value=text)
        else:
            self.label_value.set(value='Digite algo no campo de texto!')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
