
b = 0   # 전역변수 선언(초기화)
print("b값: ", b)
b = 1   # 재할당
print("b값: ", b)

def scope_test():
    global a    # 지역 => 전역
    a = 1       # 전역변수 재할당
    # c = 0     # 지역 변수 선언
    print("함수 내 a 값: ", a)

a = 0       # 전역변수 선언
print("함수 밖 a 값:", a)
scope_test()

print("함수 호출 후 a 값:", a)

# 실무 관점
# : global 가능하면 안 쓰는게 좋음
# 이유
# : 디버깅 어려움,
# 사이드 이펙트(함수의 결과 외에 "외부 상태를 변경하는 것")
# 함수의 재사용성이 떨어짐

count = 0
def increment():
    global count
    count += 1

def increment(count):
    return count + 1


increment()
increment()
print(count)    # 2

print("-------------")
count = 100
increment()
print(count)
# 의도치 않게 기존 값이 바뀜

print("-------------")
def process():
    increment()     # 내부에서 count 값을 변경
# process() 함수만 봐서는 count 가 바뀌는 것을 알 수가 없다.

