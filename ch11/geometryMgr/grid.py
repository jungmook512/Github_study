
# 수업 다시보기 필요

from tkinter import Tk
from tkinter import Button

otk = Tk()
otk.geometry("300x200")

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.grid(row=2, column=0)
obtn2.grid(row=2, column=1)
obtn3.grid(row=0, column=6)

otk.mainloop()
