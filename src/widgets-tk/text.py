# -*- coding: utf-8 -*-
"""."""
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
        frame_text_area = tk.Frame(master=self)
        frame_text_area.pack(expand=True, fill=tk.BOTH)

        # Criando scrollbar para o eixo x.
        scrollbar_x = tk.Scrollbar(master=self, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Criando scrollbar para o eixo y.
        scrollbar_y = tk.Scrollbar(master=self, orient=tk.VERTICAL)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(
            master=self,
            height=15,
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set,
        )
        self.text_area.insert(
            index=tk.INSERT,
            chars='Para aplicar negrito utilize Ctrl + b ou o botão negrito',
        )
        self.text_area.tag_config(tagName='bold', font='Helvetica 11 bold')
        self.text_area.bind_all('<Control-b>', self._apply_bold_bind)
        self.text_area.pack(fill=tk.X)

        button_bold = tk.Button(
            master=self,
            text='Negrito',
            command=self._apply_bold,
        )
        button_bold.pack(side=tk.LEFT)

    def _apply_bold(self):
        try:
            self.text_area.selection_get()
        except Exception as e:
            print('[X] Nenhum texto selecionado [X]')
            print(e)
        else:
            word = self.text_area.selection_get()
            first_char = self.text_area.index(tk.SEL_FIRST)
            last_char = self.text_area.index(tk.SEL_LAST)
            if 'bold' in self.text_area.tag_names(first_char):
                self.text_area.tag_remove('bold', first_char, last_char)
            else:
                self.text_area.tag_add('bold', first_char, last_char)

    def _apply_bold_bind(self, event):
        try:
            self.text_area.selection_get()
        except Exception as e:
            print('[X] Nenhum texto selecionado [X]')
            print(e)
        else:
            word = self.text_area.selection_get()
            first_char = self.text_area.index(tk.SEL_FIRST)
            last_char = self.text_area.index(tk.SEL_LAST)
            if 'bold' in self.text_area.tag_names(first_char):
                self.text_area.tag_remove('bold', first_char, last_char)
            else:
                self.text_area.tag_add('bold', first_char, last_char)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
