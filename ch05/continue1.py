
count= 0
while count < 3:
    count += 1
    if count == 2:
        continue
    print(count)
print("반복문이 종료되었습니다.")

print('--------------')

users = ["admin", "guest", "", "user1", None]

for user in users:
    if not user:
        continue
    print(user)

# ""(빈 값) / None => 건너뜀
# 유효한 데이터만 처리
print('--------------')

count= 0
while count < 3:
    count += 1
    if count == 2:
        break
    print(count)

users = ['kim', 'lee', 'park']

for user in users:
    if user == 'lee':
        print("발견!")
        break

# 찾으면 탐색 중지 -> 성능 절약

while True:
    cmd = input("프롬프트> ")
    if cmd == "python3":
        print("파이썬 프로그램 실행")
    elif cmd == "exit":
        print("터미널 종료")
        break
    