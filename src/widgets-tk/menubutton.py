# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


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
        menu_frame = tk.Frame(master=self)
        menu_frame.pack(expand=False, fill=tk.X, side=tk.TOP)

        menu_button_label = tk.Menubutton(master=menu_frame, text='Label')
        menu_label = tk.Menu(master=menu_button_label, tearoff=False)
        for text in range(1, 4):
            menu_label.add_command(
                label=f'Label {text}',
                command=None,
            )
        menu_button_label['menu'] = menu_label
        menu_button_label.pack(side=tk.LEFT)

        menu_button_chekbox = tk.Menubutton(master=menu_frame, text='Checkbox')
        menu_chekbox = tk.Menu(master=menu_button_chekbox, tearoff=False)
        for text in range(1, 4):
            menu_chekbox.add_checkbutton(
                label=f'Checkbox {text}',
                command=None,
            )
        menu_button_chekbox['menu'] = menu_chekbox
        menu_button_chekbox.pack(side=tk.LEFT)

        menu_button_radiobutton = tk.Menubutton(master=menu_frame, text='Radiobutton')
        menu_radiobutton = tk.Menu(master=menu_button_radiobutton, tearoff=False)
        for text in range(1, 4):
            menu_radiobutton.add_radiobutton(
                label=f'Radiobutton {text}',
                command=None,
            )
        menu_button_radiobutton['menu'] = menu_radiobutton
        menu_button_radiobutton.pack(side=tk.LEFT)

        MyFrame(master=self)


class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self['bg'] = 'blue'
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        pass


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
