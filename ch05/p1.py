
clovers = ['클로버1','클로버2', '클로버3']

for clover in clovers:
    print(clover)

for clover1 in range(3):
    print(clovers[clover1])


count = 0
while count < 3:
    print(count)
    count = count + 1

print("-----------")
count = 1
while count < 4:
    count = count + 1
    print(count)

count = 0
while count <= 5:
    if count % 2 !=0:
        print(count)
    count = count + 1

price = 0
while price !=-1:
    price = int(input('가격을 입력하세요 (종료:-1):'))
    if price > 10000:
        print('너무 비싸요.')
    elif price > 5000:
        print('괜찮은 가격이네요.')
    elif price > 0:
        print('정말 싸요.')
    
# 1단 구구단 출력 프로그램

for x in range(1,10):
    print("1 *",x, "=", x)

for x in range(1,10):
    print("2 *", x, '=', 2*x)

