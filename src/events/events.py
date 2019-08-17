# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


def _event_mouse_button_1(event):
    text = f'Botão {event.num} pressionado sobre o label.'
    label['text'] = text


def _event_mouse_in_out(event):
    text = f'Mouse ENTROU na área do frame: x={event.x} e y={event.x}.'
    if event.type.name == 'Leave':
        text = f'Mouse SAIU na área do frame: x={event.x} e y={event.x}.'
    label['text'] = text


def _on_key_pressed(event):
    text = f'Tecla {repr(event.char)} pressionada.'
    label['text'] = text


root = tk.Tk()
root.title(string='Janela principal')

icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
root.iconphoto(False, icon_png)

width = round(number=root.winfo_screenwidth() / 2)
height = round(number=root.winfo_screenheight() / 2)
root.geometry(newGeometry=f'{width}x{height}')
root.minsize(width=width, height=height)
# Evento é disparado quando alguma tecla é pressionada.
# Execto teclas especiais.
root.bind(sequence="<Key>", func=_on_key_pressed)

# Frame.
frame = tk.Frame(master=root, bg='red')
# Evento disparado quando o mouse ENTRA na área do label.
frame.bind(sequence='<Enter>', func=_event_mouse_in_out)
# Evento disparado quando o mouse SAI na área do label.
frame.bind(sequence='<Leave>', func=_event_mouse_in_out)
frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

label = tk.Label(master=frame, text='Este texto será alterado!')
# Evento disparado quando o botão esquerdo no mouse é pressionado sobre o label.
label.bind(sequence='<Button-1>', func=_event_mouse_button_1)
label.pack()

root.mainloop()
