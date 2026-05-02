
# 1. 중첩은 얼마든지 가능하다.
# 2. 중첩은 어디든지 가능하다.
# 3. 중첩이 복잡하면 블록다이어그램(순서도)을 그려라.

tscore = 700
tscore = 800

if tscore >= 900:
    print("당신의 토익 점수는", tscore, "상위권 점수입니다.")
elif tscore >= 700:
    print("당신의 토익 점수는", tscore, "중위권 점수입니다.")
    if tscore >= 800:
        print(tscore, "중상위권")
    else:
        print(tscore, "중하위권")
else:
    print("당신의 토익 점수는", tscore, "하위권 점수입니다.")

# 중위권 => 중상위권 / 중하위권

