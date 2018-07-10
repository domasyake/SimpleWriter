class StringProcessor:
    def split_combobox_name(str):
        start_index = str.find("[")
        if start_index == -1:
            return str
        return str[0:start_index]

    def split_combobox_elements(str):
        start_index = str.find("[")
        element_part = str[start_index + 1:-1]
        element_part = element_part.split("-")
        return element_part

    def check_combobox(str):
        return str.count("[") == 1 and str.count("]") == 1
