# -------------------------------------------------------
# [실습] 구구단을 아래와 같이 출력하세요
# 예) 2단
# 2 * 1 = 2
# 2 * 2 = 4


# 예) 6단
# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# 6 * 6 = 36


dan = input("좋아하는 단을 입력해주세요. : ")
print(f"{dan}단")
dan = int(dan)
for g in range(1,10):
    if not g > dan:
        print(f"{dan} * {g} = {dan * g}")
    else:
        break


