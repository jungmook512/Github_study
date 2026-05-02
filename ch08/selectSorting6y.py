
# 선택 정렬2
# fselsort 함수로 정의 및 호출

# def fselsort(매개변수):
#     코드블록
#     return 반환값

# fselsort(인수)

def fselsort(ca):
    for sa in range(0,4,1):
        mina = ca[sa]
        minix = sa
        
        for sb in range(sa+1,5,1):
            if mina > ca[sb]:
                mina = ca[sb]
                minix = sb
            
        temp = ca[sa]
        ca[sa] = ca[minix]
        ca[minix] = temp
        print(ca)
    return ca


ca = [21, 10, 11, 15, 13]
print(fselsort(ca))
ca = [31, 40, 19, 57, 17]
print(fselsort(ca))