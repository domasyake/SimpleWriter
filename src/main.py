import tkinter as tk
import tkinter.ttk as ttk
from widgetmanage import *
from widgetcreators import *
from configload import *
from xlswrite import *

if __name__ == '__main__':
    root = tk.Tk()
    root.title('DataWriter')
    root.geometry("1080x720")

    elements_frame = tk.Frame(root, bd=2, relief="ridge")
    elements_frame.pack(fill="x")
    button_frame = tk.Frame(root, bd=2, relief="ridge")
    button_frame.pack(fill="x")

    config_loader = ConfigLoader()
    widget_creator = WidgetCreatorRoot(elements_frame)
    widget_manager = WidgetManager()
    widget_manager.set_elements(widget_creator.create_elements(config_loader.data))
    xls_writer = XlsWriter(widget_creator.get_all_label_name())

    # event on submit
    def button1_clicked():
        print(widget_manager.get_elements_parameter())
        xls_writer.add_raw(widget_manager.get_elements_parameter())
        widget_manager.clear_elements()
        widget_manager.set_elements(widget_creator.re_create(config_loader.data))

    button1 = ttk.Button(
        button_frame,
        text='Submit',
        command=button1_clicked,
        width=15)
    button1.bind("<Return>", (lambda event: button1_clicked()))
    button1.pack(side="left")

    root.mainloop()
