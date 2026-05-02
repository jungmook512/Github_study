
class Human:
    # 1. 멤버변수
    eyes = 2    # 클래스 변수
    nose = 1
    mouth = 1
    # 2. 멤버함수(매서드)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("이름:", self.name)
        print("나이:", self.age)
    def eat(self):
        print('먹다')        
    def sleep(self):
        print('자다')
    def talk(self):
        print('말하다')


class Student(Human):
    # 1. 맴버 변수(속성)
    # 2. 맴버 함수(매서드)(기능/동작)
    def __init__(self, name, age, studentNum):
        self.name = name
        self.age = age
        self.studentNum = studentNum
    def introduce(self):
        print("이름:", self.name)
        print("나이:", self.age)
        print("학번:", self.studentNum)    
    
    def study(self):
        print("공부하다")


print("눈 개수:", Human.eyes)   # 클래스 변수 접근
lee = Human("이수근", 49)   # 객체 생성 및 초기 데이터 설정
print(lee.name)     # 인스턴스 변수 접근
lee.introduce()     # 매서드 접근
lee.eat()       # AttributeError
lee.study()     


print("---------------")
print("눈 개수:", Student.eyes)
print("코 개수:", Student.nose)
kim = Student("김수로", 56, 20260423)
print(kim.name)
kim.introduce()     # 자식 클래스 멤버 우선순위 높음
kim.study()
kim.eat()
kim.sleep()

print(kim.studentNum)