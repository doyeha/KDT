# -------------------------------------------------------
# 제어문 - 조건문 살펴보기
# - 다중조건문의 조건부표현식
# -------------------------------------------------------
# 양수, 음수, 0
num = 9
if num > 0:
    print("양수")
elif num<0:
    print("음수")
else:
    print("0")

print("양수") if num>0 else print("음수") if num<0 else print("0")

msg = "양수" if num>0 else "음수" if num<0 else "영"
print(msg)