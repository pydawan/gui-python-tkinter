# -*- coding: utf-8 -*-
"""
Event Handlers
==============

**Event Handlers** (manipuladores de eventos), a partir do momento que
o aplicativo é iniciado com o método `mainloop()` os eventos são
criados e monitorados.

No Tkinter as 2 formas principais de se conectar aos eventos
(**event bindings**) são:

- `command`: Ele está ligado a interação direta com um widget, um
exemplo é quando clicamos em um botão e o mesmo realiza uma ação.
- `bind()`: Ele está comumente ligado a eventos do mouse e teclado,
um exemplo é se conectar a um evento que dispara uma ação quando o
mouse entra ou sai da área de um widget.

A esta **ação** que é disparada damos o nome de **callback**.

**OBS**:

    Argumentos **podem** ser passados a um **callback**, nestes casos
    **DEVEM** ser utilizadas funções anonimas (`lambda`).

Bind
----

**Principais eventos**:

- `<Button-1>`: Evento é disparado quando o botão **esquerdo** do mouse
é pressionado.
- `<Button-2>`: Evento é disparado quando o Botão **central** (scroll)
do mouse é - pressionado.
- `<Button-3>`: Evento é disparado quando o Botão **direito** do mouse
é pressionado.

- `<B1-Motion>`: Evento é disparado quando o mouse é arrastado com o
botão **esquerdo** pressionado.
- `<B2-Motion>`: Evento é disparado quando o mouse é arrastado com o
botão **central** pressionado.
- `<B3-Motion>`: Evento é disparado quando o mouse é arrastado com o
botão **direito** pressionado.

- `<ButtonRelease-1>`: Evento é disparado quando o botão **esquerdo**
do mouse é solto.
- `<ButtonRelease-2>`: Evento é disparado quando o botão **central**
do mouse é solto.
- `<ButtonRelease-3>`: Evento é disparado quando o botão **direito**
do mouse é solto.

- `<Double-Button-1>`: Evento é disparado quando o botão **esquerdo**
do mouse é pressionado 2 vezes.
- `<Double-Button-2>`: Evento é disparado quando o botão **esquerdo**
do mouse é pressionado 2 vezes.
- `<Double-Button-3>`: Evento é disparado quando o botão **esquerdo**
do mouse é pressionado 2 vezes.

- `<Enter>`: Evento é disparado quando o mouse entra na área do widget.
- `<Leave>`: Evento é disparado quando o mouse sai da área do widget.

- `<FocusIn>`: Evento disparado quando o wiget ganha foco.
- `<FocusOut>`: Evento disparado quando o widget perde o foco.

- `<Return>`: Evento disparado quando o usuário pressiona a tecla
`Enter`. Outras teclas do teclado podem ser mapeadas para isso:
- `<BackSpace>`: Evento disparado quando a `barra de espaço` é
pressionada.
- `<Shift_L>`: Evento disparado quando a tecla `Shift` esquerdo é
pressionada.
- `<Control-slash>`: Evento disparado quando a tecla `Ctrl + /` é
pressionada.
- `<KP_0>`: Evento disparado quando o numero 1 do teclado numérico
é pressionado (**verificar**).
- `<F1>`: Evento disparado quando a tecla `F1` é pressionada.
- Etc.

**OBS**:

    Para que alguns eventos de teclado funcionem de forma adequada o
    widget deve estar em foco.

Quando o `bind()` é utilizado o **método** ou **função** recebe um
parâmetro `event`, para acessar os valores contidos nele utilize:

- `widget`: Widget que gerou o evento.
- `x`, `y`: Posição atual do mouse.
- `x_root`, `y_root`: Posição atual do mouse com base no canto superior
esquerdo da tela (em pixels).
- `char`: String com o código do carácter que foi pressionado
(apenas para eventos de teclado).
- `keysym`: Simbolo da tecla que foi pressionada
(apenas para eventos de teclado).
- `keycode`: Código da tecla que foi pressionada
(apenas para eventos de teclado).
- `num`: Botão do mouse que foi clicado (apenas eventos do mouse).
- `width`, `height`: Tamanho do widget em pixels
(apenas para eventos de configuração).
- `type`: Tipo do evento.

**OBS**:

    Foi utilizado o nome `event` para o argumento, no entanto este
    argumento pode ter um nome qualquer.
"""
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

        label_info = tk.Label(
            master=self,
            bg='red',
            text=(
                'Mova o cursor do mouse para dentro e fora do frame vermelho.\n'
                'Pressione o botão esquerdo do mouse sobre o label que está '
                'exibindo as informações.\n'
                'Pressione qualquer tecla do teclado.'
            ),
        )
        label_info.pack(expand=True)

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
