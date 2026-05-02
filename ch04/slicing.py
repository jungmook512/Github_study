
week = ['월', '화', '수,', '목', '금', '토', '일']

print(week)
print(week[2:5])
print(type(week[2:5]))
print(week)

print(week[5:7])

print(week[0:4])

print("음수 인덱싱 ----------------")
print(week[-1])
print(week[-2])
print(week[-3])

print('음수 슬라이싱-----------------')
print(week[-3:-1])
# 리스트명[시작인덱스:끝인덱스-1]

print(week[-5:5])

print('인덱스 번호 생략하는 경우--------')
# 1. 시작 인덱스 생략
print(week[:5])

# 2. 끝 인덱스 생략
print(week[-3:])        # week [-3:마지막인덱스+1]

# 3. 모든 인덱스 생략 => 전체 데이터 대상
print(week[:])          # week[0:마지막인덱스+1]

