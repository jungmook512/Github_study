
b = 0   # 전역변수 선언(초기화)
print("b값: ", b)
b = 1   # 재할당
print("b값: ", b)

def scope_test():
    a = 1       # 지역변수 선언
    print("함수 내 a 값: ", a)

a = 0       # 전역변수 선언
print("함수 밖 a 값:", a)
scope_test()

print("함수 호출 후 a 값:", a)