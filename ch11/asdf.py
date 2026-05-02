
import tkinter
from tkinter import Label
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import Button

otk = tkinter.Tk()
otk.geometry("300x300") # 출력 결과가 잘리지 않도록 높이를 조금 키웠습니다.
otk.title('조각 피자 주문 프로그램')

pizza = {0:'치즈 피자 (3200원)', 1:'콤비네이션 피자 (3500원)', 2:'불고기 피자 (3600원)'}
check_value = {}

olabel1 = Label(otk, text='피자')
olabel1.pack()

def order():
    # 1. 텍스트 초기화
    selected_text = "주문내역:\n"
    total_price = 0
    
    # 2. 체크된 항목 확인 및 가격 합산
    if check_value[0].get():
        selected_text = selected_text + "- " + pizza[0] + "\n"
        total_price = total_price + 3200
    if check_value[1].get():
        selected_text = selected_text + "- " + pizza[1] + "\n"
        total_price = total_price + 3500
    if check_value[2].get():
        selected_text = selected_text + "- " + pizza[2] + "\n"
        total_price = total_price + 3600
    
    # 3. 라벨에 결과 표시 (문자열 더하기 사용)
    olabel2["text"] = selected_text + "\n총 가격: " + str(total_price) + "원"

# 체크박스 변수 생성 및 배치
for i in range(len(pizza)):
    check_value[i] = BooleanVar()
    ocheckbutton = Checkbutton(otk, text=pizza[i], variable=check_value[i])
    ocheckbutton.pack(anchor='w')

# 주문 버튼
otkb = Button(otk, text='주문', command=order)
otkb.pack()

# 결과가 표시될 라벨
olabel2 = Label(otk, text="")
olabel2.pack()

otk.mainloop()