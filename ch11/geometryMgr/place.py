
# 수업 다시보기 필요

from tkinter import Tk
from tkinter import Button

otk = Tk()
otk.geometry("300x200")

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)

otk.mainloop()

# 배치 매니저 주의사항!
# pack()과 grid() 혼합 사용 불가
# grid()와 place() 혼합 사용 불가
