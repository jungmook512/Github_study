
# x = 10

# def example1():
#     x = 20
#     print(x)

# example1()
# print(x)

# x = 5
# def example2():
#     global x
#     x = 15
#     print(x)

# example2()
# print(x)

# numbers = [42, 17, 23, 56, 9, 34]

# def fmin(fu):
#     min = fu[0]
#     for sfu in fu:
#         if min > sfu:
#             min = sfu
#     return min

# print(fmin(numbers))

# class Student:
#     school = "High School"

#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

# s1 = Student("Alice", 1)

# print(Student.school)
# print(s1.school)
# print(s1.name)

# from math import factorial
# print(factorial(5))

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# dog1 = Dog()
# print(dog1.speak())

import tkinter as tk
from tkinter import messagebox

def on_buton_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

root = tk.Tk()
root.title("간단한 Tkinter 앱")
root.geometry("300x200")

btn = tk.Button(root, text = "클릭하세요", command = on_buton_click)
btn.pack(pady=20)

root.mainloop()