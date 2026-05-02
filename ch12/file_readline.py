
# 파일객체명.readline()

# f = open(r"ch12\file1.txt", "r")    # 인코딩 확인 필요
f = open(r"ch12\file1.txt", "r", encoding="utf-8")

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

# 특정 줄만 읽어서 출력
for i, line in enumerate(f, start=1):
    if i == 3:
        print(i, line)


f.close()