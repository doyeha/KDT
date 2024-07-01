# -------------------------------------------------------
# [실습] 1~50 사이의 숫자 데이터를 생성
# 숫자 데이터에서 3의 배수만 저장하는 리스트를 생성

ran = range(1,51)
num = []

num2 = [r for r in ran if not r%3]
print(num2)

# 3의 배수면 세제곱 하고 아니면 그냥 두고 
num3 = [r**3 if not r%3 else r for r in ran]
print(num3)


# T
nums=range(1,51)
three = []
for n in nums:
    if not n%3:
        three.append(n)

three2 = [n for n in nums if not n%3]
print(three)
print(three2)