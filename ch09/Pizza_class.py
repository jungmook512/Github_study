

# class 클래스명:
#     # 1. 멤버변수
#     멤버변수명 = 속성값
#     # 2. 멤버함수(메서드)
#     def 함수명(self, 매개변수):
#         self.멤버변수 = 속성값
#         return 반환값

# 객체변수명 = 클래스명()
# 객체변수명.메서드(인수)
# 객체변수명.멤버변수

# #빈 클래스
# class 클래스명:
#     pass

# 클래스 정의
class Pizzaclass:
    def order(self):
        print("주문하다.")
        self.kind = 10





#객체 생성
na = Pizzaclass()

na.order()  # 객체.메서드()
print(na.kind)  #객체.멤버변수