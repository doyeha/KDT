# -------------------------------------------------------
# 제어문에서 사용되는 키워드
# - 목적 : 코드 실행 흐름을 변경
# 조건문과 함께 사용되는 키워드
# - break : 반복문(for, while)을 즉시 중단 시키는 기능 
# - coutinue : 반복문(for, while)의 코드 일부를 실행 x
# - pass : 아무일도 일어나지 않음 (의미 없음!) 문법적인 제약상 사용
# -------------------------------------------------------
# [실습] 1~50까지의 숫자의 합계를 계산 후 출력합니다.
#        단, 합계가 27 이상이 되면 더 이상 합계를 하지 마세요.
total = 0
for num in range(1,51):
    total = total + num
    if total >= 27:
        break   

num = 1
while num <= 51:
    total = total+num
    num = num + 1
    if total >=27:
        break

# [실습] 1~50까지의 숫자중에서 짝수만 출력하세요.
for n in range(1,51):
    if not n%2: 
        print(n)

for n in range(1,51):
    if n%2:
        continue #홀수면 29line으로, 짝수면 32 line
    print(n) # 짝수일 때만 해당 코드를 실행하게 만듬.   


# [실습] 아직 정확한 기능을 정하지 못한 경우, 또는 약간의 시간이 필요한 경우
# #      사용하는 키워드 => pass
print("START")
for _ in range(100000000):
    pass
print("End")
