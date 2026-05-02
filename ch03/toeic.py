
tscore = 900


if 990 >= tscore >= 900:
    print("당신의 토익 점수는", tscore, "상위권 점수입니다.")
elif tscore >= 600:
    print("당신의 토익 점수는", tscore, "중상위권 점수입니다.")
elif tscore >= 300:
    print("당신의 토익 점수는", tscore, "중위권 점수입니다.")
else:
    print("당신의 토익 점수는", tscore, "하위권 점수입니다.")
print("-----------------------")

print("번역하고자 하는 요일을 입력하세요")

yoil = input(":")
print(yoil)

if yoil == "월요일":
    print(yoil + "은", "Monday입니다")
elif yoil == "화요일":
    print(yoil + "은", "Tuesday입니다")
elif yoil == "수요일":
    print(yoil + "은", "Wednsday입니다")
elif yoil == "목요일":
    print(yoil + "은", "Thursday입니다")
elif yoil == "금요일":
    print(yoil + "은", "Friday입니다")
elif yoil == "토요일":
    print(yoil + "은", "Saturday입니다")
elif yoil == "일요일":
    print(yoil + "은", "Sunday입니다")
else:
    print("입력하신 요일이 정확하지 않습니다")

print("즐거운 영어공부 되세요 !")