

import tkinter
from tkinter import Label
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import Button
from tkinter import StringVar

otk = tkinter.Tk()

otk.geometry("300x300")
pizza = {0:'치즈 피자 (3200원)', 1:'콤비네이션 피자 (3500원)', 2:'불고기 피자 (3600원)'}
check_value = {}
otk.title('조각 피자 주문 프로그램')
olabel1 = Label(otk, text = '피자')
olabel1.pack()


def order():
    selected_text = "주문내역:\n"
    total_price = 0
    
    if check_value[0].get():
        selected_text = selected_text + "- " + pizza[0] + "\n"
        total_price = total_price + 3200
    if check_value[1].get():
        selected_text = selected_text + "- " + pizza[1] + "\n"
        total_price = total_price + 3500
    if check_value[2].get():
        selected_text = selected_text + "- " + pizza[2] + "\n"
        total_price = total_price + 3600

    olabel2["text"] = selected_text + "\n총 가격: " + str(total_price) + "원"



for i in range(len(pizza)):
    check_value[i] = BooleanVar()

for i in range(len(pizza)):
    ocheckbutton = Checkbutton(otk, text = pizza[i], variable = check_value[i])
    ocheckbutton.pack(anchor = 'w')

otkb = tkinter.Button(text='주문', command=order)
otkb.pack()

olabel2 = Label(otk, text="", )
olabel2.pack()


otk.mainloop()