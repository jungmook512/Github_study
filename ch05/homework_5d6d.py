
# 과일 = ["사과","귤", "수박"]

# for x in 과일:
#     print(x)

# 가격리스트 = [100, 200, 300]

# for 변수 in 가격리스트:
#     int(변수)
#     print(변수 + 10)

# 리스트 = ['dog', 'cat', 'parrot']
# # 동물 이름과 글자수를 다음과 같이 출력하라.
# # dog 3
# # cat 3
# # parrot 6
# for x in 리스트:
#     print(x, len(x))

# 리스트 = [3, -20, -3, 44]

# for x in 리스트:
#     if x < 0:
#         print(x)

# for w in range(2002, 2051, 4):
#     print(w)

# x = 1
# t = 0

# while 0 < x <= 100:
#     t += x
#     x += 1


# print(t)

# 홀수 = []
# 짝수 = []

# for 홀짝 in range(1, 31):
#     if 홀짝 % 2 == 0:
#         print(홀짝, ":", '짝수') 
#     else:
#         print(홀짝, ":", '홀수')
        

# for 홀짝 in range(1, 31):
#     if 홀짝 % 2 == 0:
#         짝수.append(홀짝) 
#     else:
#         홀수.append(홀짝) 
# print(홀수)
# print(짝수)

def greet(name = 'Guest'):
    print('Hello,', name, '!')
greet('Alice')
greet()

