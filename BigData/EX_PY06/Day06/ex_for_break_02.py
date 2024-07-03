# ------------------------------------------------------------------
# 제어문 - 반복문과 break
# - 중첩 반복문일 경우의 break는 가장 가까이 있는 반복문과 종료
# ------------------------------------------------------------------
## [실습] 단의 숫자만큼만 구구단을 출력하세요.

## [중첩 반복문] 내부 반복문 종료 시 외부반복문종료
## - 내부 반복문 종료 여부를 변수 저장
## - 외부 반복문에서는 내부 반복문이 종료되면 함께 종료 

# dan = int(input("2~9 정수 입력, 정수의 구구단을, 정수만큼 출력 : "))

# 

t = 0
print("1번")
for dan in range(2,10): # 단 반복
    print(f"\n{dan}단")
    for i in range(1,dan+1): # 곱셈 수 반복 (2단은 2번만, 5단은 5번만)
        print(f"{dan} * {i} = {dan*i :<2}", end="\t") # 2*2=1 \t | f-string이랑 서식 지정 같이 쓰는 법 
        if i == dan:
            print()

print("\n2번")
isBreak = False
for d in range(2,10):
    print(f"\n[{d}단]", end="   ")
    for n in range(1,10):
        print(f"{d} * {n} = {d*n :<2}", end="\t")
        if n == d:
            isBreak = True
            break
    # print("outer for")
    if isBreak: break



