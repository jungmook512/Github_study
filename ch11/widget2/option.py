
from tkinter import Tk
from tkinter import StringVar
from tkinter import OptionMenu

# 1. 위젯 생성
otk = Tk()
otk.geometry("700x600")

options_list = ['Option1', 'Option2', 'Option3']

selected_option = StringVar()

selected_option.set(options_list[0])
# sel_option = selected_option.get()
# print(sel_option)

def get_menu(value):
    sel_option = selected_option.get()
    print(sel_option)

option_menu = OptionMenu(otk, selected_option, *options_list, command=get_menu)
# *options_list == options_list[0], options_list[1], options_list[2]

option_menu.pack()

otk.mainloop()