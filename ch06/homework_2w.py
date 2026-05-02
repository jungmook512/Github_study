

# a = 3.14
# b = True
# c = "False"
# print(type(a))
# print(type(b))
# print(type(c))


# num1 = input("첫번째 숫자를 입력해주세요:")
# num2 = input("두번째 숫자를 입력해주세요:")
# a = float(num1)
# b = float(num2)

# def math(a, b):
#     if b == 0:
#         print(a + b)
#         print(a - b)
#         print(a * b)
#         print("0으로는 나눌 수 없습니다")
#     else:
#         print(a + b)
#         print(a - b)
#         print(a * b)
#         print(a / b)

# math(a, b)

# water = 700
# if water >= 1000:
#     print("충분")
# elif water < 1000 and water >= 500:
#     print("적절")
# else:
#     print("부족")

# a = input("점수를 입력하시오:")
# score = int(a)

# if score >= 90:
#     print("A 학점")
# elif score >= 80 :
#     print("B 학점")
# elif score >= 70 :
#     print("C 학점")
# else:
#     print("F 학점")


# Numbers = [1, 2, 3, 4, 5]

# for n in Numbers:
#     print(n)

# fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']

# for fruit in fruits:
#     print(fruit)
#     if "사과" in fruit:
#         print("사과를 찾았습니다!")

# def solution(a, b):
# 	sum = a + b
# 	sub = a - b
# 	multi = a * b
# 	return sum, sub, multi
#     print(sum)
# 	print(sub)
# 	print(multi)

# solution(1, 2)

# # 프로그램 실행 예시
# num1 = 10
# num2 = 5

# # 함수 호출 및 결과 반환 (튜플 언패킹)
# s, d, m = solution(num1, num2)

# print(f"두 수의 합: {s}")
# print(f"두 수의 차: {d}")
# print(f"두 수의 곱: {m}")

# num1 = input("첫번째 숫자를 입력해주세요:")
# num2 = input("두번째 숫자를 입력해주세요:")
# a = int(num1)
# b = int(num2)

# def solution(a, b):
#     sum = a + b      # 합
#     sub = a - b      # 차
#     multi = a * b    # 곱
#     return sum, sub, multi

# result = solution(a, b)

# print("두 수의 합:", result[0])
# print("두 수의 차:", result[1])
# print("두 수의 곱:", result[2])

# def get_sum(n):
#     total = 0
#     # 1부터 n까지 반복 (range의 두 번째 인자는 포함되지 않으므로 n + 1)
#     for i in range(1, n + 1):
#         total = total + i
#     return total

# # 프로그램 실행 예시
# number = 10
# result = get_sum(number)

# print("1부터", number, "까지의 합은:", result)

num1 = input("1부터 n까지 수의 합을 구하고자 하는 n값을 입력하시오:")
n = int(num1)

def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = sum(n)
print(result)