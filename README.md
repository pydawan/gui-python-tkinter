# Interfaces gráficas com Python e Tkinter

Repositório em construção!

Os códigos contidos neste repositório são apenas para referencia (cookbook) e estudo.

Informações importantes sobre os widgets devo adicionar via docstring com o tempo.

Entre em contato caso encontre algum erro ou se preferir abra uma issue :relaxed:.

## Instalação

### Fedora

```bash
sudo dnf install python3-tkinter
```

### Ubuntu

```bash
sudo apt install python3-tk
```

### macOS

O instalador do [site oficial](https://www.python.org/) do Python já instala o Tkinter.

### Windows

O instalador do [site oficial](https://www.python.org/) do Python já instala o Tkinter.

## Tkinter

Tkinter é a biblioteca padrão para construção de interfaces gráficas com Python, a mesma acompanha a [distribuição oficial de Python](https://www.python.org/).http://pyinstaller.readthedocs.io/en/v3.3.1/

Tkinter é baseado no toolkit [Tcl/Tk](http://www.tcl.tk/), da linguagem Tcl.

Para verificar os parâmetros que um determinado widget pode utilizar:

```python
print(tk.Button().keys())
```

Para configurar os widgets o Tkinter fornece pelo menos 4 formas:

```python
        button = tk.Button(
            master=self,
            text='Botão',
        )
        button.pack()
```
```python
        button = tk.Button(master=self)
        button['text'] = 'Botão'
        button.pack()
```
```python
        button = tk.Button(master=self)
        button.config(text='Botão')
        button.pack()
```
```python
        button = tk.Button(master=self)
        button.configure(text='Botão')
        button.pack()
```
> **OBS**: Lembre-se de substituir `self` por uma instância de `tk.Tk()`.

As 4 formas presentadas a cima levam ao mesmo resultado, ficando a cargo de cada equipe definir qual será o padrão para o projeto.

### Command

- [command](src/command/command.py).
- [command utilizando classe](src/command/command_with_class.py).

### Event

- [event](src/events/events.py).
- [event utilizando classe](src/events/events_with_class.py).

### Protocol

- [protocol utilizando classe](src/protocols/protocols_with_class.py).

### Style 

- [style tk](src/style/style_tk.py).
- [style ttk](src/style/style_ttk.py).
- [Cursores](src/style/cursor.py).
- [Tabela com o nome dos cursores](#tipos-de-cursor).

### Widgets

- [Button](src/widgets-tk/button.py).
- [Canvas](src/widgets-tk/canvas_with_scrollbar.py).
- [Checkbutton](src/widgets-tk/checkbutton.py).
- [Entry](src/widgets-tk/entry.py).
- [Frame](src/frames/frames.py).
- [Frame utilizando classe](src/frames/frames_with_class.py).
- [Alternar entre Frames](src/frames/change_frames.py).
- [Label](src/widgets-tk/label.py).
- [LabelFrame](src/widgets-tk/labelframe.py).
- [Listbox](src/widgets-tk/listbox_with_scrollbar.py).
- [Menu](src/widgets-tk/menu.py).
- [Menubutton](src/widgets-tk/menubutton.py) (obsoleto a partir da versão 8.0?).
- [Message](src/widgets-tk/message.py).
- [PanedWindow](src/widgets-tk/panedwindow.py).
- [Radiobutton](src/widgets-tk/radiobutton.py).
- [Scale](src/widgets-tk/scale.py).
- [Scrollbar](src/widgets-tk/scrollbar_x_y_axis.py).
- [Spinbox](src/widgets-tk/spinbox.py).
- [Text](src/widgets-tk/text.py).
- [MessageBox](src/widgets-tk/messagebox.py).
- [Toplevel](src/toplevel/toplevel.py).
- [Toplevel utilizando classe](src/toplevel/toplevel_with_class.py).

### Widgets ttk

- [Button](src/widgets-ttk/button.py).
- [Checkbutton](src/widgets-ttk/checkbutton.py).
- [Combobox](src/widgets-ttk/combobox.py).
- [Entry](src/widgets-ttk/entry.py).
- [Frame](src/widgets-ttk/frame.py).
- [Label](src/widgets-ttk/label.py).
- [LabelFrame](src/widgets-ttk/labelframe.py).
- [Menubutton](src/widgets-ttk/menubutton.py).
- [Notebook](src/widgets-ttk/notebook.py).
- [PanedWindow](src/widgets-ttk/panedwindow.py).
- [Progressbar](src/widgets-ttk/progressbar.py).
- [Progressbar com thread](src/widgets-ttk/progressbar_with_thread.py).
- [Radiobutton](src/widgets-ttk/radiobutton.py).
- [Scale](src/widgets-ttk/scale.py).
- [Scrollbar](src/widgets-ttk/scrollbar_x_y_axis.py).
- [Separator](src/widgets-ttk/separator.py).
- [Sizegrip](src/widgets-ttk/sizegrip.py).
- [Spinbox](src/widgets-ttk/spinbox.py).
- [Treeview](src/widgets-ttk/treeview.py).

### Tipos de cursor

| Cursor                                        | Nome                  | Cursor                                        | Nome              |
| --------------------------------------------- | --------------------- | --------------------------------------------- |------------------ |
| ![Cursor 1.png](src/assets/cursors/1.png)	    | X_cursor              | ![Cursor 40.png](src/assets/cursors/40.png)	| lr_angle          |
| ![Cursor 2.png](src/assets/cursors/2.png)	    | arrow	                | ![Cursor 41.png](src/assets/cursors/41.png)	| man               |
| ![Cursor 3.png](src/assets/cursors/3.png)	    | based_arrow_down 	    | ![Cursor 42.png](src/assets/cursors/42.png)	| middlebutton      |
| ![Cursor 4.png](src/assets/cursors/4.png)	    | based_arrow_up	    | ![Cursor 43.png](src/assets/cursors/43.png)	| mouse             |
| ![Cursor 5.png](src/assets/cursors/5.png)	    | boat	                | ![Cursor 44.png](src/assets/cursors/44.png)	| pencil            |
| ![Cursor 6.png](src/assets/cursors/6.png)	    | bogosity	            | ![Cursor 45.png](src/assets/cursors/45.png)	| pirate            |
| ![Cursor 7.png](src/assets/cursors/7.png)	    | bottom_left_corner    | ![Cursor 46.png](src/assets/cursors/46.png)	| plus              |
| ![Cursor 8.png](src/assets/cursors/8.png)	    | bottom_right_corner   | ![Cursor 47.png](src/assets/cursors/47.png)	| question_arrow    |
| ![Cursor 9.png](src/assets/cursors/9.png)	    | bottom_side           | ![Cursor 48.png](src/assets/cursors/48.png)	| right_ptr         |
| ![Cursor 10.png](src/assets/cursors/10.png)   | bottom_tee            | ![Cursor 49.png](src/assets/cursors/49.png)	| right_side        |
| ![Cursor 11.png](src/assets/cursors/11.png)	| box_spiral            | ![Cursor 50.png](src/assets/cursors/50.png)	| right_tee         |
| ![Cursor 12.png](src/assets/cursors/12.png)	| center_ptr            | ![Cursor 51.png](src/assets/cursors/51.png)	| rightbutton       |
| ![Cursor 13.png](src/assets/cursors/13.png)	| circle                | ![Cursor 52.png](src/assets/cursors/52.png)	| rtl_logo          |
| ![Cursor 14.png](src/assets/cursors/14.png)	| clock                 | ![Cursor 53.png](src/assets/cursors/53.png)	| sailboat          |
| ![Cursor 15.png](src/assets/cursors/15.png)	| coffee_mug            | ![Cursor 54.png](src/assets/cursors/54.png)	| sb_down_arrow     |
| ![Cursor 16.png](src/assets/cursors/16.png)	| cross                 | ![Cursor 55.png](src/assets/cursors/55.png)	| sb_h_double_arrow |
| ![Cursor 17.png](src/assets/cursors/17.png)	| cross_reverse         | ![Cursor 56.png](src/assets/cursors/56.png)	| sb_left_arrow     |
| ![Cursor 18.png](src/assets/cursors/18.png)	| crosshair             | ![Cursor 57.png](src/assets/cursors/57.png)	| sb_right_arrow    |
| ![Cursor 19.png](src/assets/cursors/19.png)	| diamond_cross         | ![Cursor 58.png](src/assets/cursors/58.png)	| sb_up_arrow       |
| ![Cursor 20.png](src/assets/cursors/20.png)	| dot                   | ![Cursor 59.png](src/assets/cursors/59.png)	| sb_v_double_arrow |
| ![Cursor 21.png](src/assets/cursors/21.png)	| dotbox                | ![Cursor 60.png](src/assets/cursors/60.png)	| shuttle           |
| ![Cursor 22.png](src/assets/cursors/22.png)	| double_arrow          | ![Cursor 61.png](src/assets/cursors/61.png)	| sizing            |
| ![Cursor 23.png](src/assets/cursors/23.png)	| draft_large           | ![Cursor 62.png](src/assets/cursors/62.png)	| spider            |
| ![Cursor 24.png](src/assets/cursors/24.png)	| draft_small           | ![Cursor 63.png](src/assets/cursors/63.png)	| spraycan          |
| ![Cursor 25.png](src/assets/cursors/25.png)	| draped_box            | ![Cursor 64.png](src/assets/cursors/64.png)	| star              |
| ![Cursor 26.png](src/assets/cursors/26.png)	| exchange              | ![Cursor 65.png](src/assets/cursors/65.png)	| target            |
| ![Cursor 27.png](src/assets/cursors/27.png)	| fleur                 | ![Cursor 66.png](src/assets/cursors/66.png)	| tcross            |
| ![Cursor 28.png](src/assets/cursors/28.png)	| gobbler               | ![Cursor 67.png](src/assets/cursors/67.png)	| top_left_arrow    |
| ![Cursor 29.png](src/assets/cursors/29.png)	| gumby                 | ![Cursor 68.png](src/assets/cursors/68.png)	| top_left_corner   |
| ![Cursor 30.png](src/assets/cursors/30.png)	| hand1                 | ![Cursor 69.png](src/assets/cursors/69.png)	| top_right_corner  |
| ![Cursor 31.png](src/assets/cursors/31.png)	| hand2                 | ![Cursor 70.png](src/assets/cursors/70.png)	| top_side          |
| ![Cursor 32.png](src/assets/cursors/32.png)	| heart                 | ![Cursor 71.png](src/assets/cursors/71.png)	| top_tee           |
| ![Cursor 33.png](src/assets/cursors/33.png)	| icon                  | ![Cursor 72.png](src/assets/cursors/72.png)	| trek              |
| ![Cursor 34.png](src/assets/cursors/34.png)	| iron_cross            | ![Cursor 73.png](src/assets/cursors/73.png)	| ul_angle          |
| ![Cursor 35.png](src/assets/cursors/35.png)	| left_ptr              | ![Cursor 74.png](src/assets/cursors/74.png)	| umbrella          |
| ![Cursor 36.png](src/assets/cursors/36.png)	| left_side             | ![Cursor 75.png](src/assets/cursors/75.png)	| ur_angle          |
| ![Cursor 37.png](src/assets/cursors/37.png)	| left_tee              | ![Cursor 76.png](src/assets/cursors/76.png)	| watch             |
| ![Cursor 38.png](src/assets/cursors/38.png)	| leftbutton            | ![Cursor 77.png](src/assets/cursors/77.png)	| xterm             |
| ![Cursor 39.png](src/assets/cursors/39.png)	| ll_angle              |                                               |                   |

#### Windows

cursores nativos do sistema:

- arrow
- center_ptr
- crosshair
- fleur
- ibeam
- icon
- sb_h_double_arrow
- sb_v_double_arrow
- watch
- xterm

Cursores adicionais:

- no
- starting
- size
- size_ne_sw
- size_ns
- size_nw_se
- size_we
- uparrow
- wait

> O cursor `no` pode ser utilizado para remover o cursor.

#### Mac OS X

cursores nativos do sistema:

- arrow
- cross
- crosshair
- ibeam
- plus
- watch
- xterm

Cursores adicionais:

- copyarrow
- aliasarrow
- contextualmenuarrow
- text
- cross-hair
- closedhand
- openhand
- pointinghand
- resizeleft
- resizeright
- resizeleftright
- resizeup
- resizedown
- resizeupdown
- none
- notallowed
- poof
- countinguphand
- countingdownhand
- countingupanddownhand
- spinning

## Exemplos

Lembre-se de verificar e instalar as dependências do arquivo `Pipfile` ([Pipenv](https://github.com/pypa/pipenv)).

- [CRUD com SQLite](src/examples/crud_sqlite) (Não possui dependências).
- [CRUD com SQLite e SQLAchemy](src/examples/crud_sqlachemy).
- [CRUD com SQLite, SQLAchemy e utilizando frames](src/examples/crud_sqlachemy_with_frames).
- [Plotando gráfico](src/examples/plot_graph).
