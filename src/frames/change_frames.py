# -*- coding: utf-8 -*-
"""Alterando o frame da janela principal."""

import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Alternando entre frames')
        icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        # Registrando os frames.
        self.frames = {
            'frame1': MyFrame1,
            'frame2': MyFrame2,
            'frame3': MyFrame3,
        }

        # Frame que será iniciado junto com o aplicativo.
        self.current_frame = None

        self.create_widgets()

    def create_widgets(self):
        self.current_frame = self.frames['frame1'](master=self)

    def change_to_frame_1(self):
        self.winfo_children()[0].destroy()
        self.current_frame = self.frames['frame1'](master=self)

    def change_to_frame_2(self):
        self.winfo_children()[0].destroy()
        self.current_frame = self.frames['frame2'](master=self)

    def change_to_frame_3(self):
        self.winfo_children()[0].destroy()
        self.current_frame = self.frames['frame3'](master=self)


class MyFrame1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(master=self, text='Frame 1')
        label.pack(expand=True, fill=tk.BOTH)

        button = tk.Button(
            master=self,
            text='Ir para o frame 2',
            command=self.master.change_to_frame_2
        )
        button.pack(expand=False, fill=tk.X)


class MyFrame2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(master=self, text='Frame 2')
        label.pack(expand=True, fill=tk.BOTH)

        button_to_frame_1 = tk.Button(
            master=self,
            text='Ir para o frame 1',
            command=self.master.change_to_frame_1
        )
        button_to_frame_1.pack(expand=True, fill=tk.X, side=tk.LEFT)

        button_to_frame_3 = tk.Button(
            master=self,
            text='Ir para o frame 3',
            command=self.master.change_to_frame_3
        )
        button_to_frame_3.pack(expand=True, fill=tk.X, side=tk.RIGHT)


class MyFrame3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(master=self, text='Frame 3')
        label.pack(expand=True, fill=tk.BOTH)

        button_to_frame_2 = tk.Button(
            master=self,
            text='Ir para o frame 2',
            command=self.master.change_to_frame_2
        )
        button_to_frame_2.pack(expand=False, fill=tk.X)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
