# pinput.py

print("첫 번째 정수를 입력하세요: ")
ra = input()        # 20
print(type(ra))     #str
ra = int(ra)
print(type(ra))


# 5
rb = input("두 번째 정수를 입력하세요: ")
print(type(rb))
rb = int(rb)
print(type(rb))         

# 1.문자열 연결 연산자
# 2. 산술 연산자
rc = ra + rb
print(ra, "+", rb, "=", rc)

