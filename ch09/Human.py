
class Human:
    eyes = 2
    nose = 2
    mouth = 1
    def __init__(self, age, name):
        # 인스턴스 변수
        self.name = name
        self.age = age
    # 기능: 자기소개하다.
    def introduce(self):
        print(str(self.age)+"살", end=" ")
        print((self.name) +"입니다.")

    def eat(self, food):
        self.food = food
        print(str(food) + "을/를 먹다")
    
    def sleep(self):
        print("자다")
    
    def talk(self, blah):
        self.blah = blah
        print(str(blah) + "라고 말한다")


jo = Human(27, "조정묵")
jo.introduce()

lee = Human(45, "이승우")
lee.introduce()

print("눈 개수:", Human.eyes)
print("입 개수:", Human.mouth)
print("코 개수:", Human.nose)

jo.eat("피자")
jo.talk("이따가 짐 챙기고 설거지 해야해")


# 문자열 "10"을 na 변수명으로 할당
# 문자열 => 정수 자료형 변경
na = "10"
na = int("10")