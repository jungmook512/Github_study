
from tkinter import Tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Label

# PNG 파일 형식 활용 가능
# - 라이브러리 다운로드 수행 후 설치
# - PIL(pillow)
# - pip install pillow
# - pip list
from PIL import Image

# jpg => png 파일 형식 변환
image = Image.open("C:/rokey/py_work/ch11/widget2/angry_apple.png")
image.save("C:/rokey/py_work/ch11/widget2/angry_apple.png", format="PNG")
print('이미지가 PNG로 변환되었습니다.')



# 1. 위젯 생성
otk = Tk()
otk.geometry("700x600")

# img1 = PhotoImage(file = "C:/rokey/py_work/ch11/widget2/angry_apple.png")
img1 = PhotoImage(file = "./ch11/widget2/angry_apple.png")
img_label = Label(otk, image=img1)
img_label.place(x=-20, y=-10)




obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.place(x=10 , y=60)
obtn2.place(x=140 , y=60)
obtn3.place(x=80 , y=10)



otk.mainloop()