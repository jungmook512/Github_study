

# def myabs(arg):
#     if(arg < 0):
#         result=arg * -1
#     else:
#         result=arg
#     return result

# print(myabs(10))
# print(myabs(-10))

# print("----------")
# def funca():
#     print("a 함수 호출")

# def funcb():
#     funca()     # 세번째 호출
#     print("b 함수 호출")

# def funcc():
#     funcb()     # 두번째 호출
#     print("c 함수 호출")

# funcc()         # 첫번째 호출

# def draw_stars(num):
#     print('*' * num)

# draw_stars(3)

# na = int(input("첫번째 값: "))
# nb = int(input("두번재 값: "))


sta = "python example"
lena = len(sta)
print(lena)

# stb = sta
def string_length(stb):
    count = 0
    for letter in stb:
        count += 1
        print(count)
    return count

lena = string_length(sta)
print("문자열 길이:", lena)
print("--------------")


def fdiv(pa, pb):
    if pb == 0:
        print("0으로는 나눌수 없다.")
    else:
        return pa/pb

na = float(input("첫번째 값: "))
nb = float(input("두번째 값: "))

nc = fdiv(na, nb)
print(na, "/", nb, "=", nc)