import tkinter as tk
import tkinter.ttk as ttk


class WidgetCreatorControl:
    def __init__(self, frame):
        self.__my_frame = frame
        # List to put in except SimpleField
        self.__my_creators = [PullDownCreator(frame)]
        self.__simple_creator = SimpleBoxCreator(frame)
        self.__element_names = list()

    def get_all_label_name(self):
        return self.__element_names

    def create_elements(self, data):
        elements = []
        for i in range(len(data)):
            name = data[i]
            creator_temp_list = list(filter(lambda x: x.check_my_pattern(name), self.__my_creators))
            # If it does not match the special field pattern, create SimpleBox
            if len(creator_temp_list) == 0:
                creator = self.__simple_creator
            else:
                creator = creator_temp_list[0]
            label_name = creator.get_name(name)
            self.create_label(label_name, i)
            elements.append(creator.create_widget(name, i))
            self.__element_names.append(label_name)
        return elements

    def re_create(self, data):
        elements = []
        for i in range(len(data)):
            name = data[i]
            creator_temp_list = list(filter(lambda x: x.check_my_pattern(name), self.__my_creators))
            if len(creator_temp_list) == 0:
                creator = self.__simple_creator
            else:
                creator = creator_temp_list[0]
            elements.append(creator.create_widget(name, i))
        return elements

    def create_label(self, name, line):
        la = tk.Label(self.__my_frame, text=name, font=("", 15))
        la.grid(row=line, column=1, sticky=tk.W)


class PullDownCreator:
    def __init__(self, frame):
        self.__my_frame = frame

    def check_my_pattern(self, str):
        return str.count("[") == 1 and str.count("]") == 1

    def get_name(self, str):
        start_index = str.find("[")
        if start_index == -1:
            return str
        return str[0:start_index]

    def create_widget(self, names, line):
        start_index = names.find("[")
        element_part = names[start_index + 1:-1]
        element_part = element_part.split("-")
        combo = ttk.Combobox(self.__my_frame, state='readonly', font=("", 15))
        combo["values"] = element_part
        combo.current(0)
        combo.grid(row=line, column=2, sticky=tk.W)
        return combo


class SimpleBoxCreator:
    def __init__(self, frame):
        self.__my_frame = frame

    def check_my_pattern(self, str):
        return True

    def get_name(self, str):
        return str

    def create_widget(self, element, line):
        en = tk.Entry(self.__my_frame, width=50, font=("", 15))
        en.grid(row=line, column=2, sticky=tk.W)
        return en
