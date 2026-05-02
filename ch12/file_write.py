
# 파일객체명.write(data)

import locale
print(locale.getpreferredencoding())

f = open(r"ch12\file1.txt", "w", encoding="utf-8") 

# # f.write("hello")
# f.write("안녕!")    # CP949 인코딩 수행
                    # VScode 기본 인코딩 UTF-8
                    # => 깨짐(인코딩 설정 필요)


for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)


f.close()