

# 함수 기능 : ca 리스트 원소의 총합 계산
def fk(cb):
    total = 0   # 지역변수

    for sb in range(0, 3, 1):
        total += cb[sb]

    cb[2] = total
    return cb   # list

ca = [10, 20, 30]
print(ca)

cd = fk(ca)
print(ca)
print(cd)
print(type(cd))
