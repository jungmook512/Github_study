
# print(3 == 5)

# print ((3 == 3) and (4 != 3))

# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")



# if True :
#       if False:
#           print("1")
#           print("2")
#       else:
#           print("3")
# else :
#       print("4")
# print("5")

# num1 = input("숫자를 입력해주세요:")
# num2 = int(num1)
# if num2 % 2 == 0:
#     print("그 숫자는 짝수입니다.")
# else:
#     print("그 숫자는 홀수입니다.")


# num1 = input("숫자를 입력해주세요:")
# num2 = int(num1)
# if num2 + 20 < 255:
#     print(num2 + 20)
# else:
#     print(255)



# num1 = input("숫자를 입력해주세요:")
# num2 = int(num1)
# if 255 > num2 - 20 > 0:
#     print(num2 - 20)
# elif num2 - 20 > 255:
#     print(255)
# else:
#     print(0)

# time = input("현재시간: ")

# if time.endswith("00"):
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

score = input("score:")
sc = int(score)
if 100 >=sc > 80:
    print("grade is A")
elif 80 >=sc > 60:
    print("grade is B")
elif 60 >= sc > 40:
    print("grade is C")
elif 40 >= sc > 20:
    print("grade is D")
elif 20>= sc >= 0:
    print("grade is E")
else:
    print("입력된 점수가 정확하지 않습니다. (0이상 100이하 숫자를 입력하세요)")