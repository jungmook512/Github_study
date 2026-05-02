
# range(정수)
# range(시작 정수, 끝정수)
# range(시작 정수, 끝정수, 증감정수)
# 증감정수 몇씩 뛸것인지 step

nums = range(11)
print(nums)         # range(0, 10)
print(type(nums))   #
print(type(list(nums))) #
print(list(nums)) 

print("--------------")
print(range(11))    # range(0, 10)
print(list(range(11)))

print("-------------")
print(range(2, 12, 2))
print(list(range(2, 12, 2)))

print("-------------")
for num in range(3):    # [0,1,2]
    print('안녕 거북이', num)

for num in range(1,5):    
    print('안녕 거북이', num)

for num in range(1,5,2):    
    print('안녕 거북이', num)
