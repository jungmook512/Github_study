
# 선택 정렬2
ca = [21, 10, 11, 15, 13]

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