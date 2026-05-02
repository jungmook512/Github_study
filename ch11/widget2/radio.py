
from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Radiobutton
from tkinter import IntVar


otk = Tk()
otk.geometry("300x200")

radio_value = IntVar()      # 정수형 변수 생성 객체
radio_value.set(-1)      # 정수값 설정
# val = radio_value.get()       # 정수값 접근
# print(val)



lunch = {0:"A런치", 1:"B런치", 2:"C런치", 3:"D런치"}
# radio_value => 어떤 버튼이 선택되어 있는지 저장할 변수
# variable => 클릭된 버튼의 정보를 저장할 변수명 설정
# value => radio_value에 저장될 데이터를 지정하는 인수

orb1 = Radiobutton(otk, text=lunch[0], variable=radio_value, value=0)
orb2 = Radiobutton(otk, text=lunch[1], variable=radio_value, value=1)
orb3 = Radiobutton(otk, text=lunch[2], variable=radio_value, value=2)
orb4 = Radiobutton(otk, text=lunch[3], variable=radio_value, value=3)
# 기능 : 선택된 라디오버튼의 값을 변수로 가져와 출력
def buy():
    print("다음 메뉴를 주문합니다.")
    val = radio_value.get()
    print(lunch[val])

obtn1 = Button(otk, text="주문", command=buy)



orb1.pack()
orb2.pack()
orb3.pack()
orb4.pack()
obtn1.pack()

otk.mainloop()

# class IntVar:
#     def __init__(self):
#         self.int_val = 0

#     def set(self, int_val):
#         self.int_val = int_val
    
#     def get(self):
#         return self.int_val

