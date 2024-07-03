# ------------------------------------------------------------------
# 제어문 - while 반복문
# ------------------------------------------------------------------
## [실습] 3단 출력하기. 단, while문 사용

dan = 3
data = 1
while data < 10:
    print(f"{dan} * {data} = {data * dan :0>2}")
    data = data + 1


## [실습] 1 ~ 30범위의 수 중에서 홀수만 출력
##         단, while 사용
print("My way")
data = list(range(1,31))
i = 0
while i < 30:
    print(data[i], end=" ")
    i = i+1
print()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
i = 0
while i < 30:
    print(data[i], end=" ")
    i = i+2
print()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("3th")
num = 1
while num < 31:
    if num%2:
        print(num, end=" ")
    num = num+1
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("T's way")
num = 1
while num < 31:
    print(num, end=" ")
    num = num+2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
