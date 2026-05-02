
def funca(pa, pb):
    temp = pa           # 지역변수
    pa = pb
    pb = temp
    return pa, pb

na = 10         #전역변수
nb = 11

print("na 값은", na, end=" ")
print("nb 값은", nb)

na, nb = funca(na, nb)

print("na 값은", na, end=" ")
print("nb 값은", nb)