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

Sobre ToDo

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
- style ttk: ToDo

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
- Menubutton: Tornou-se obsoleto a partir da versão 8.0.
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

ToDo

## Exemplos

Lembre-se de verificar e instalar as dependências do arquivo `Pipfile` ([Pipenv](https://github.com/pypa/pipenv)).

- [CRUD com SQLite](src/examples/crud_sqlite) (Não possui dependências).
- [CRUD com SQLite e SQLAchemy](src/examples/crud_sqlachemy).
- [CRUD com SQLite, SQLAchemy e utilizando frames](src/examples/crud_sqlachemy_with_frames).
- [Plotando gráfico](src/examples/plot_graph).
