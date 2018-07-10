class WidgedManager:
    def __init__(self):
        self.__elements=[]

    def set_elemetnts(self, elements):
        self.__elements = elements

    def get_elements_parameter(self):
        return [item.get() for item in self.__elements]

    def clear_elements(self):
        for item in self.__elements:
            item.destroy()
        del self.__elements[:]