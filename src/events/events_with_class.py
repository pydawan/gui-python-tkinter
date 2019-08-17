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

        # Evento é disparado quando alguma tecla é pressionada.
        # Execto teclas especiais.
        self.bind(sequence="<Key>", func=self._on_key_pressed)

        self.create_widgets()

    def create_widgets(self):
        self.frame = MyFrame(master=self)

    def _on_key_pressed(self, event):
        text = f'Tecla {repr(event.char)} pressionada.'
        self.frame.label['text'] = text


class MyFrame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'red'
        # Evento disparado quando o mouse ENTRA na área do label.
        self.bind(sequence='<Enter>', func=self._event_mouse_in_out)
        # Evento disparado quando o mouse SAI na área do label.
        self.bind(sequence='<Leave>', func=self._event_mouse_in_out)
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # self.label_text.set(value='Este texto será alterado!')

        self.label = tk.Label(
            master=self,
            text='Este texto será alterado!',
        )
        # Evento disparado quando o botão esquerdo no mouse é pressionado sobre o label.
        self.label.bind(sequence='<Button-1>', func=self._event_mouse_button_1)
        self.label.pack()

    def _event_mouse_button_1(self, event):
        text = f'Botão {event.num} pressionado sobre o label.'
        self.label['text'] = text

    def _event_mouse_in_out(self, event):
        text = f'Mouse ENTROU na área do frame: x={event.x} e y={event.x}.'
        if event.type.name == 'Leave':
            text = f'Mouse SAIU na área do frame: x={event.x} e y={event.x}.'
        self.label['text'] = text


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
