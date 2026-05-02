

class Phone:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def showinfo(self):
        print('전화번호:' + self.number)
        print('색상:' + self.color)

class SmartPhone(Phone):
    def __init__(self, number, color, company):
        self.number = number
        self.color = color
        self.company = company

apple = SmartPhone("010-1234-5678", "검정", "애플")
print(apple.number)
print(apple.color)
print(apple.company)

phone = Phone("010-1234-5678", "검정")
phone.showinfo()

apple.showinfo()