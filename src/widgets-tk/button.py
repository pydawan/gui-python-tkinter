# -*- coding: utf-8 -*-
"""
Button
======

principais opções
-----------------

- **`activebackground`**: Cor de fundo (Background) quando o botão é
clicado.
- **`activeforeground`**: Cor do texto quando o botão é clicado.

----

- **`anchor`**: Posição do texto dentro do botão (widget). Os
Valores válidos para `anchor` são:
    - `tk.N`, `tk.NE`, `tk.E`, `tk.SE`, `tk.S`, `tk.SW`, `tk.W`,
    `tk.NW`, `tk.CENTER`.

----

- **`bd`** ou **`borderwidth`**: Espessura da borda. O valor padrão é
de `2 pixels`.
- **`bg`** ou **`background`**: Cor de fundo do botão em seu estado
`Normal` (não clicado).
- **`bitmap`**:	Imagem que será exibida no lugar do texto. Os valores
válidos são:
    - `'error'`, `'gray75'`, `'gray50'`, `'gray25'`, `'gray12'`,
    `'hourglass'`, `'info'`, `'questhead'`, `'question'`, `'warning'`.
- **`command`**: **Método** ou **Função** que é chamada quando o botão
é clicado.
- **`cursor`**: Curso que é exibido quando o mouse está sobre o botão.
- **`default`**: Estado inicial do botão, o padrão é `tk.NORMAL`.
Outros valores válidos são `tk.DISABLED` e `tk.ACTIVE`.
- **`disabledforeground`**: Cor da fonte quando o botão está
configurado com `state=tk.DISABLED`.
- **`fg`** ou **`foreground`**: Cor da fonte do botão.

----

- **`font`**: Fonte que será utilizada pelo texto do botão.
    - **Ex**: `font='Times 24 bold italic'` ou
    `font=('Times', '24', 'bold italic')`.
    - Também existe a possibilidade de se criar uma variável com a
    configuração da fonte:

Os parâmetros válidos para `Font()` são:

+---------------+-------------------------------------------------------+
| Propriedade   | Descrição                                             |
+===============+=======================================================|
| family        | Nome da fonte.                                        |
+---------------+-------------------------------------------------------+
| size          | Tamanho da fonte.                                     |
+---------------+-------------------------------------------------------+
| weight        | 'bold' para negrito, 'normal' para sem formatação.    |
+---------------+-------------------------------------------------------+
| slant         | 'italic' para itálico, 'roman' para sem formatação.   |
+---------------+-------------------------------------------------------+
| underline     | 1 para sublinhado, 0 for normal.                      |
+---------------+-------------------------------------------------------+
| overstrike    | 1 para tachado, 0 para normal.                        |
+---------------+-------------------------------------------------------+

----

- **`height`**:	Altura do botão em **linhas se houver um texto** e em
**pixels caso o botão possua uma imagem**.
- **`highlightbackground`**: Cor da borda quando o botão está sem foco
(utilize `Tab` para dar foco ao botão).
- **`highlightcolor`**: Cor da borda quando o botão ganha foco
(utilize `Tab` para dar foco ao botão).
- **`highlightthickness`**: Espessura da borda quando o botão ganha
foco (utilize `Tab` para dar foco ao botão).

----

- **`image`**: Define imagem que será exibida no botão, a imagem irá
sobrepor o texto.
    - Caso queira a imagem sendo exibida juntamente com o texto utilize
    a propriedade `compound`.
    - Os valores válidos para `compound` são:
        - `tk.LEFT`, `tk.TOP`, `tk.RIGHT`, `tk.BOTTOM`, `tk.CENTER`
        (Caso a imagem tenha o centro vazado).

----

- **`justify`**: Alinhamento do texto dentro do botão, esté parametro é
utilizado quando o texto do botão possui várias linhas. Os valores
válidos são:
    - `tk.LEFT`, `tk.CENTER` e `tk.RIGHT`.
- **`overrelief`**: Estilo que é exibido quando o mouse passa sobre o
botão, o valor padrão é `tk.RAISED`. Outros valores válidos são:
    - `tk.FLAT`, `tk.RAISED`, `tk.SUNKEN`, `tk.GROOVE` e `tk.RIDGE`.
- **`padx`**: Espaço adicionar entre o texto e a borda do botão (eixo X).
- **`pady`**: Espaço adicionar entre o texto e a borda do botão (eixo Y).
- **`relief`**: Estilo do botão, o valor padrão é `tk.RAISED`. Outros
valores válidos são:
    - `tk.FLAT`, `tk.RAISED`, `tk.SUNKEN`, `tk.GROOVE` e `tk.RIDGE`.
- **`repeatdelay`**: O `command` é disparado após um intervalo de tempo
(em milisegundos). O mouse deve pressionar o botão de forma continua
(Clicar e segurar). Veja também `repeatinterval`.
- **`repeatinterval`**: Intervalo de tempo (em milisegundos) que o
`command` deve ser repetido. Ex: `repeatdelay=1000` e
`repeatinterval=2000`. Ao clicar e segurar o clique do botão o
`command` será executado automaticamente após 1 segundo e o comando
será executado novamente após 2 segundo.
- **`state`**: Define o estado inicial do botão, o padrão é
`tk.NORMAL`. Para desabilitar o botão utilize `tk.DISABLED`.
- **`takefocus`**: Habilitar ou desabilitar o foco, quando pressionamos
`Tab` o botão ganha foco, caso não queira que o botão tenha foco defina
esta propriedade para `0` (zero). O valor padrão é `1`.
- **`text`**: Texto que é exibido no botão.
- **`textvariable`**: Uma instancia de `StringVar()` que é associada
com o texto do botão.
- **`underline`**: Caracter do texto que deve ser sublinhado, o valor
padrão é `-1` e o primeiro caracter tem indice igual a `0` (zero).
- **`width`**: Largura do botão em **letras se houver um texto** e em
**pixels caso o botão possua uma imagem**.
- **`wraplength`**: Valor determina a quebra de linha, o valor padrão é
em pixels. Também podem ser utilizados os valores:
    - **`c`**: Centimetros.
    - **`i`**: Polegadas.
    - **`m`**: Milimetros.
    - **`p`**: Pontos de impressão (1/72″).
    - **Ex**: `'10c'`, `'10i'`, `'10m'`, `'10p'`.
"""
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
        MyFrame(master=self)


class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        button = tk.Button(
            master=self,
            text='Botão',
            command=self._on_button_clicked,
        )
        button.pack(fill=tk.X)

        button_icon = tk.PhotoImage(file='../assets/icons/flag-16x16.png')
        button_with_icon = tk.Button(
            master=self,
            text='Botão com ícone',
            image=button_icon,
            compound=tk.RIGHT,
            command=self._on_button_clicked,
        )
        button_with_icon.photo = button_icon
        button_with_icon.pack(fill=tk.X)

    def _on_button_clicked(self):
        print('Botão pressionado!')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
