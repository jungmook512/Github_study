
# (조건식에 사용된)변수 초기화
# while 조건(식):
#     코드블록
#     (while문을 빠져나올 수 있는)증감식

# while False:
#     print('Ctrl+C를 누르세요.')

a = 10
b = 5
a = a - b
print(a)

a = 10
b = 5
a -= b
print(a)

print("--------------")
num = 0
while num < 3:
    print('안녕거북이', num)
    num += 1        # 복합대입 연산자 사용

print("--------------")
stra = "파이썬"
strb = "프로그래밍"
stra = stra + strb
print(stra)

stra = "파이썬"
strb = "프로그래밍"
stra += strb
print(stra)