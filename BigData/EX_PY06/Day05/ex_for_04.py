# ------------------------------------------------------------------ 
# 제어문 - 반복문
# ------------------------------------------------------------------ 
# [실습] 2단~9단까지 모두 출력하세요.
# ------------------------------------------------------------------

for dan in range(2,10):
    print(f"{dan}단")
    for i in range(1,10):
        print(f"{dan} * {i} = {dan*i}")
    print()