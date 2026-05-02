
import os
print(os.getcwd())

path = r"C:\rokey\py_work\ch12\계좌1.txt"
mode = "w"
# f = open(path, mode, encoding="utf-8")

# f.write("김삿갓 597-89-000089\n")
# f.write("이수근 343-64-000064\n")
# f.write("박혁거세 136-97-000097")


# f.close()

with open(path, mode, encoding="utf-8") as file:
    file.write("김삿갓 597-89-000089\n")
    file.write("이수근 343-64-000064\n")
    file.write("박혁거세 136-97-000097\n")


accountlist = []
mode = "r"
with open(path, mode, encoding="utf-8") as f:
    lines = f.readlines()   # 리스트

    for line in lines:
    #     lineList = line.split()
    #     accountlist.append(lineList[1])
    # print(accountlist)
        print(line[-14:])
        accountlist.append(line[-14:].strip())
    print(accountlist)
# 문자열 일부 내용 가져오기(슬라이싱 또는 split함수 사용)