# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Olá Mundo')
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

        self.text_entry = tk.StringVar()
        entry = tk.Entry(
            master=self,
            textvariable=self.text_entry,
        )
        entry.pack(fill=tk.X)

        self.text_label = tk.StringVar(value='Este texto será alterado!')
        label = tk.Label(
            master=self,
            textvariable=self.text_label,
        )
        label.pack(expand=True, fill=tk.BOTH)

        button = tk.Button(
            master=self,
            text='Clique Aqui',
            command=self._on_button_clicked,
        )
        button.pack(fill=tk.X)

    def _on_button_clicked(self):
        text = self.text_entry.get()
        if text:
            self.text_label.set(value=text)
        else:
            self.text_label.set(value='Digite algo no campo acima!')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
