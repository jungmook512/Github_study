
# num = 1 > (2 and 3) + 3

num = 2 * (3 - 5)
print(num)

num2 = 1 > (2 and 3) + 3
print(num2)      #False

print(2 and 3)
print(0 and 3)
# 앞 값이 True => 뒤 값 반환
# 앞 값이 False => 앞 값 반환

print("--------------")
print(9>4 and 3>2)
# True and True
# True

print(9<4 and 3>2)
# False and True
# False

print(9<4 or 3<2)
# False or False
# False

print(9<4 or 3>2)
# False or True
# True

print("------------")
# 문제1
print(9 < 4 or 3 < 2 and 4 > 2)
# False or (False and True)
# False or False
# False

# 논리 연산자 우선순위
# not(단항 연산자) > and > or

# 문제2
print((3 - 5) + 3 < 1 and 3 - 5 > 1)
# -2+3 < 1 and 3-5 > 1
# 1 < 1 and -2 > 1
# False and False
# False

# 연산자 우선순위
# 괄호 > 산술 > 비교 > 논리 > 대입

# 산술 연산자 내 우선순위
# ** > +x, -x(단항 연산자) > * / // % > + -
