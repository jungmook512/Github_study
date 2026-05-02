
def persona(width=10, height=21):
    print("함수 기본값 없음")
    print("width=", width, end=" ")
    print("height=", height)

def personb(width=4, height=3):
    print("함수 기본값 있음")
    print("width=", width, end=" ")
    print("height=", height)

# 1. 모든 매개변수에 기본값 설정 가능
# 2. 인수 전달시 앞에서부터 설정 가능
# 3. 기본값이 있더라도 인수 설정 가능(인수 우선 처리)
# 4. 부분 매개변수에 기본값 설정시 뒤에서부터 설정할 것


persona(10, 20)     # 기본값 없이  
personb()           # 
personb()  

# 위치 인수 : 순서대로 전달하는 인수
persona(10)         # 인수 1개만 주어진 경우
# 키워드 인수 : 이름을 지정해서 전달하는 인수
persona(height=30)







print("-----------")

#  person_lee 사람 함수 생성
# 함수 내 전달되는 데이터 : 몸무게, 키, 나이
# 기능/동작사항 : 3가지 데이터를 확인(출력)
# 반환값 : 없음


def person_lee(weight=90, height=177, age=27):
    print("weight=", weight, end=" ")
    print("height=", height, end=" ")
    print("age=", age)

person_lee(55, 168, 21)
# 1. 모든 매개변수에 기본값 설정 가능
person_lee()

# 2. 인수 전달시 앞에서부터 설정 가능
person_lee(80, 180)

# 3. 기본값이 있더라도 인수 설정 가능(인수 우선 처리)
person_lee(75, 182, 34)

# 4. 부분 매개변수에 기본값 설정시 뒤에서부터 설정할 것
def person_lee(weight, height, age=27):
    print("weight=", weight, end=" ")
    print("height=", height, end=" ")
    print("age=", age)

person_lee(10,20)