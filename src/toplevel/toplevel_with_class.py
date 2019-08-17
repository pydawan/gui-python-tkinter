# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Multiplos Toplevel')
        icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
        # False para que o ícone principal não seja exibido nas outras janelas.
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.create_widgets()

    def create_widgets(self):
        MainWindowFrame(master=self)


class MainWindowFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        btn_toplevel_1 = tk.Button(
            master=self,
            text='Top Level 1',
            command=self._open_top_level_1,
        )
        btn_toplevel_1.pack(expand=True, fill=tk.X, side=tk.LEFT)

        btn_toplevel_2 = tk.Button(
            master=self,
            text='Top Level 2',
            command=self._open_top_level_2,
        )
        btn_toplevel_2.pack(expand=True, fill=tk.X, side=tk.LEFT, padx=10)

        btn_toplevel_2 = tk.Button(
            master=self,
            text='Top Level 3',
            command=self._open_top_level_3,
        )
        btn_toplevel_2.pack(expand=True, fill=tk.X, side=tk.LEFT)

    def _open_top_level_1(self):
        MyTopLevel1(master=self.master)

    def _open_top_level_2(self):
        MyTopLevel2(master=self.master)

    def _open_top_level_3(self):
        MyTopLevel3(master=self.master)


class MyTopLevel1(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title(string='Top Level 1')
        icon_png = tk.PhotoImage(file='../assets/icons/circular-icon.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        # grab_set() impede que se tenha acesso a janela principal e assim evita
        # que se criem outras janelas até que a janela em aberto seja fechada
        self.grab_set()

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(master=self)
        frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        label = tk.Label(master=frame, text='Top Level 1')
        label.pack(expand=True, fill=tk.BOTH)


class MyTopLevel2(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title(string='Top Level 2')
        icon_png = tk.PhotoImage(file='../assets/icons/paper-plane.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(master=self)
        frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        label = tk.Label(master=frame, text='Top Level 2')
        label.pack(expand=True, fill=tk.BOTH)


class MyTopLevel3(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title(string='Top Level 3')
        icon_png = tk.PhotoImage(file='../assets/icons/person.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(master=self)
        frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        label = tk.Label(master=frame, text='Top Level 3')
        label.pack(expand=True, fill=tk.BOTH)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
