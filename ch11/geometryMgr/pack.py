
# 수업 다시보기 필요

from tkinter import Tk
from tkinter import Button

otk = Tk()
otk.geometry("300x200")

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.pack(side="left")
obtn2.pack(side="right")
obtn3.pack(side="bottom")

otk.mainloop()
