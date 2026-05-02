
def persona(width, height):
    print("함수 기본값 없음")
    print("width=", width, end=" ")
    print("height=", height)

def persona():
    print("매개변수 없는 함수")

def personb(width=4, height=3):
    print("함수 기본값 있음")
    print("width=", width, end=" ")
    print("height=", height)


# 함수가 재 정의 되면 기존 함수보다 재정의 함수의 우선순위가 높음
# persona(10, 20) # 인수가 없어야 동작
persona()       # 정상 동작
personb()         # 인수가 없는데 정상 실행
personb(50, 60)     # 기본값보다 인수 우선순위 높음

