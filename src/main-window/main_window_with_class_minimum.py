# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.create_widgets()

    def create_widgets(self):
        pass


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
