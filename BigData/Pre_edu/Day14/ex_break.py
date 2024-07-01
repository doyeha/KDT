# -------------------------------------------------------
# 제어문에서 사용되는 키워드 - break
# -------------------------------------------------------
# [중첩 반복문]
for n in range(1,50):
    for d in range(10,100):
        print(n, d)
        if d==15:
            break

is_stop = False
for n in range(1,50):
    if is_stop:
        break
    for d in range(10, 100):
        print(n,d)
        if d==15:
            is_stop = True
            break