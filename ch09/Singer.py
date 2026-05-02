
# 가수: 아이유, BTS
# 속성(데이터, 명사): 변수 => 이름
# 기능(동작, 동사): 함수 => 노래부르다

class Singer:
    # name = "아이유"
    job = "가수"
    def call_name(self, name):
        self.name = name
    def sing(self):
        print("이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요~")

print(Singer.job)
iu = Singer()   # 생성자 함수
# print(iu.name)  # 속성 확인
# iu.sing()       # 기능 확인
print(iu.job)
iu.call_name("아이유")
print(iu.name)
iu.sing()

print(Singer.job)
bts = Singer()
print(bts.job)
bts.call_name("BTS")
print(bts.name)