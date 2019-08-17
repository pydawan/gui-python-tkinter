# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


def _open_top_level_1():
    my_toplevel_1 = tk.Toplevel(master=root)
    my_toplevel_1.title = 'Top Level 1'

    icon_png = tk.PhotoImage(file='../assets/icons/circular-icon.png')
    my_toplevel_1.iconphoto(False, icon_png)

    width = round(number=root.winfo_screenwidth() / 2)
    height = round(number=root.winfo_screenheight() / 2)
    my_toplevel_1.geometry(newGeometry=f'{width}x{height}')
    my_toplevel_1.minsize(width=width, height=height)

    # grab_set() impede que se tenha acesso a janela principal e assim evita
    # que se criem outras janelas até que a janela em aberto seja fechada
    my_toplevel_1.grab_set()

    frame_1 = tk.Frame(master=my_toplevel_1)
    frame_1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    label = tk.Label(master=frame_1, text='Top Level 1')
    label.pack(expand=True, fill=tk.BOTH)


def _open_top_level_2():
    my_toplevel_2 = tk.Toplevel()
    my_toplevel_2.title(string='Top Level 2')
    icon_png = tk.PhotoImage(file='../assets/icons/paper-plane.png')
    my_toplevel_2.iconphoto(False, icon_png)

    width = round(number=root.winfo_screenwidth() / 2)
    height = round(number=root.winfo_screenheight() / 2)
    my_toplevel_2.geometry(newGeometry=f'{width}x{height}')
    my_toplevel_2.minsize(width=width, height=height)

    frame_2 = tk.Frame(master=my_toplevel_2)
    frame_2.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    label = tk.Label(master=frame_2, text='Top Level 2')
    label.pack(expand=True, fill=tk.BOTH)


def _open_top_level_3():
    my_toplevel_3 = tk.Toplevel()
    my_toplevel_3.title(string='Top Level 3')
    icon_png = tk.PhotoImage(file='../assets/icons/person.png')
    my_toplevel_3.iconphoto(False, icon_png)

    width = round(number=root.winfo_screenwidth() / 2)
    height = round(number=root.winfo_screenheight() / 2)
    my_toplevel_3.geometry(newGeometry=f'{width}x{height}')
    my_toplevel_3.minsize(width=width, height=height)

    frame_3 = tk.Frame(master=my_toplevel_3)
    frame_3.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    label = tk.Label(master=frame_3, text='Top Level 3')
    label.pack(expand=True, fill=tk.BOTH)


root = tk.Tk()
root.title(string='Multiplos TopLevel')

icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
root.iconphoto(False, icon_png)

width = round(number=root.winfo_screenwidth() / 2)
height = round(number=root.winfo_screenheight() / 2)
root.geometry(newGeometry=f'{width}x{height}')
root.minsize(width=width, height=height)

frame = tk.Frame(master=root)
frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

btn_toplevel_1 = tk.Button(
    master=frame,
    text='Top Level 1',
    command=_open_top_level_1,
)
btn_toplevel_1.pack(expand=True, fill=tk.X, side=tk.LEFT)

btn_toplevel_2 = tk.Button(
    master=frame,
    text='Top Level 2',
    command=_open_top_level_2,
)
btn_toplevel_2.pack(expand=True, fill=tk.X, side=tk.LEFT, padx=10)

btn_toplevel_2 = tk.Button(
    master=frame,
    text='Top Level 3',
    command=_open_top_level_3,
)
btn_toplevel_2.pack(expand=True, fill=tk.X, side=tk.LEFT)

root.mainloop()
