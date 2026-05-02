

# 클래스: 가방
# 객체: 숄더백, 백팩, 핸드백, 에코백, 클러치백, 크로스백
# 속성: 재질, 색, 무게, 브랜드, 수납개수, 가격
# 기능: 넣다, 꺼내다, 꾸미다, 보호하다, ...

class Bag:
    # 클래스 멤버변수
    call_name = "가방"

    # 멤버함수(메서드)
    # def info(self):
    def __init__(self, kind, color):
        # print("초기화 수행")
        # 인스턴스 멤버변수
        self.kind = kind
        self.color = color
        self.data = []

    def add(self, x):    # 넣다
        self.data.append(x)

    def addtwice(self, x):   # 두번 넣다
        self.add(x)
        self.add(x)

shoulder = Bag("숄더백", "검정")        # 인스턴스 객체 생성
print(shoulder.kind)
print(shoulder.color)
print(shoulder.call_name)
# shoulder.info()
shoulder.add("휴대폰")
shoulder.addtwice("돈")
print(shoulder.data)



handbag = Bag("핸드백", "녹색")
print(handbag.kind)
print(handbag.color)
# handbag.info()
handbag.add("지갑")
handbag.addtwice("책")
print(handbag.data)
