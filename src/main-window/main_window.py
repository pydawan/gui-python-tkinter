# -*- coding: utf-8 -*-
"""."""
import tkinter as tk

root = tk.Tk()
root.title(string='Janela principal')

icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
root.iconphoto(False, icon_png)

width = round(number=root.winfo_screenwidth() / 2)
height = round(number=root.winfo_screenheight() / 2)
root.geometry(newGeometry=f'{width}x{height}')
root.minsize(width=width, height=height)

root.mainloop()
