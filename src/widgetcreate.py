import tkinter as tk
import tkinter.ttk as ttk
from stringutil import StringProcessor as sp


class WidgetCreater:
    def __init__(self, frame):
        self.__myrame = frame

    def create_elements(self, names):
        elements = []
        for i in range(len(names)):
            if sp.check_combobox(names[i]):
                self.create_label(sp.split_combobox_name(names[i]), i)
                elements.append(self.create_combobox(sp.split_combobox_elements(names[i]), i))
            else:
                self.create_label(names[i], i)
                elements.append(self.create_simple_box(i))
        return elements

    def re_create(self, names):
        elements = []
        for i in range(len(names)):
            if sp.check_combobox(names[i]):
                elements.append(self.create_combobox(sp.split_combobox_elements(names[i]), i))
            else:
                elements.append(self.create_simple_box(i))
        return elements

    def create_label(self, name, line):
        la = tk.Label(self.__myrame, text=name, font=("", 15))
        la.grid(row=line, column=1, sticky=tk.W)

    def create_simple_box(self, line):
        en = tk.Entry(self.__myrame, width=50, font=("", 15))
        en.grid(row=line, column=2, sticky=tk.W)
        return en

    def create_combobox(self, names, line):
        combo = ttk.Combobox(self.__myrame, state='readonly', font=("", 15))
        combo["values"] = names
        combo.current(0)
        combo.grid(row=line, column=2, sticky=tk.W)
        return combo
