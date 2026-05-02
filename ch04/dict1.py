
# 딕셔너리 생성
# 변수명 = {키1:값1, 키2:값2, 키3:값3}

my_dict1 = {}
print(my_dict1)
print(type(my_dict1))

my_dict2 = {0:1, 1:-2, 2:3.14}
print(my_dict2)

my_dict3 = {'이름':'엘리스', '나이':10,'시력':[1.0, 1.2]}
print(my_dict3)

print(my_dict3['이름'])
print(my_dict3['나이'])
print(my_dict3['시력'])

print(my_dict3.get('이름'))

my_dict3['성별'] = '여성'

print(my_dict3)

my_dict3['나이'] = 11
print(my_dict3)

print('-------------')
clover = {'나이':27, '직업':'병사'}
print(clover)
# 값 추가하기
clover['번호'] = 9
print(clover)

# 값 변경하기
clover['번호'] = 8
print(clover)

mook = {'이름':'조정묵', '나이':27, '성별':'남', '취미':'게임'}

print(mook)
print(type(mook))

mook['전화번호'] = '010-6573-2707'
mook['주소'] = '경북 안동시 용상동 977-5'

print(mook['주소'])
print(mook.get('취미'))

mook['나이'] = 28

print('---------------')

print(mook.items())

print(mook.values())

print(mook.keys())
