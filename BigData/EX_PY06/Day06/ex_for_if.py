# ------------------------------------------------------------------
# 제어문 - 반복문과 조건문 혼합
# ------------------------------------------------------------------
## [실습]
## 숫자 1~50까지의 데이터, 해당 데이터에서 3의 배수는 제곱. 나머지는 합계 출력

num = range(1,51)
sum = 0
for i in num:
    if i%3 ==0:
        i = i*i
    sum = sum + i
print(f"합계는 {sum}")


## [실습]
## 메시지에서 알파벳과 숫자를 구분해서 처리한다.
## 알파벳은 ☆ / 숫자는 ♡

msg = "Good 2020"
for i in msg:
    if i.isalpha():
        print("☆", end="")
    elif i.isnumeric():
        print("♡", end="")

msg = "Good 2020"
for i in msg:
    if ('a'< i <'z') and ('A'< i <'Z') :
        print("☆", end="")

    elif i.isnumeric():
        print("♡", end="")
    
    else:
        print(" ")