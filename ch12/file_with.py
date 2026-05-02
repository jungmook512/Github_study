
# 자동 닫기 처리 (close)
# with open(파일경로, 모드, 인코딩) as 파일객체:
#     코드블록

path = r"ch12\file2.txt"
mode = "w"

with open(path, mode, encoding="utf-8") as f:
    f.write("No pain, no gain.\n")
    f.write("노력 없이는 얻는 것도 없다.")

