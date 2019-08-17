# -*- coding: utf-8 -*-
"""Utilizando o parâmetro ``command`` para disparar um callback
(método ou função).
"""
import tkinter as tk


def _on_button_clicked():
    text = text_entry.get()
    if text:
        text_label.set(value=text)
    else:
        text_label.set('Digite algo no campo acima!')


root = tk.Tk()
root.title(string='Janela principal')

icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
root.iconphoto(False, icon_png)

width = round(number=root.winfo_screenwidth() / 2)
height = round(number=root.winfo_screenheight() / 2)
root.geometry(newGeometry=f'{width}x{height}')
root.minsize(width=width, height=height)

# Frame.
frame = tk.Frame(master=root)
frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

text_entry = tk.StringVar()
entry = tk.Entry(master=frame, textvariable=text_entry)
entry.pack(fill=tk.X)

text_label = tk.StringVar()
text_label.set(value='Este texto será alterado!')
label = tk.Label(master=frame, text='Este texto será alterado!', textvariable=text_label)
label.pack(expand=True, fill=tk.BOTH)

button = tk.Button(master=frame, text='Clique Aqui', command=_on_button_clicked)
button.pack(fill=tk.X)

root.mainloop()
