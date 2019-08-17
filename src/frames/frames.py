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

frame_1 = tk.Frame(master=root, bg='red')
frame_1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

label_1 = tk.Label(master=frame_1, text='Frame 1', bg='red')
label_1.pack(expand=True, fill=tk.BOTH)

frame_2 = tk.Frame(master=root, bg='blue')
frame_2.pack(expand=True, fill=tk.BOTH, padx=10, pady=(0, 10))

label_2 = tk.Label(master=frame_2, text='Frame 2', bg='Blue')
label_2.pack(expand=True, fill=tk.BOTH)

root.mainloop()
