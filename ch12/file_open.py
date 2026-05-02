# file_open.py

import os

# 작업 디렉터리 확인
print(os.getcwd())

# "\n" : 줄바꿈(new line)
# r : raw(날것의, 원형의)

# 파일 열기
# f = open(r"C:\rokey\py_work\ch12\file1.txt")    # 절대경로
f = open(r"ch12\file1.txt", "w")     # 상대경로(작업디렉터리 기준)
# f.메서드명()      # 파일객체 멤버함수
# f.변수명          # 파일객체 멤버변수

# 파일 닫기
f.close()