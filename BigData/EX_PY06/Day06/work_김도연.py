# ------------------------------------------------------------------ 
# 0703, Day06
# 17장 ~ 20장 
# ------------------------------------------------------------------
import random
## 198P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
cnt = int(input("정수 입력 : "))
i = 0
while i < cnt:
    print("Hello, World!", i)
    i = i + 1

Dice = [1,2,3,4,5,6]

i = 0
while i < 4:
    i = random.choice(Dice)
    print("주사위 굴리기! 4 이상을 뽑아주세요~", i)
    print("실패!") if i < 4 else print("오, 성공!")

## 201P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
""" 퀴즈 17.4
1. 다음 중 while 반복문에 대한 설명으로 잘못된 것을 모두 고르세요.
 a. while 반복문에는 조건식 또는 값을 지정하면 된다.
 b. while 반복문은 조건식의 결과가 True이면 반복을 끝낸다.
 c. while 반복문은 반복 횟수가 정해져 있을 때만 사용할 수 있다.
 d. while 반복문의 다음 줄은 반드시 들여쓰기를 해야한다.
 e. while 반복문의 조건식에 True를 지정하면 무한 루프가 된다.
    My Answer : b c 

2. 다음 while 반복문을 실행 했을 때 출력 결과를 고르세요.
 [ i = 10
    while i < 19:
        print(i, end=" ")
        i += 2            ]
 a. 10 11 12 13 14 15 16 17 18 19
 b. 10 11 12 13 14 15 16 17 18
 c. 10 12 14 16 18 19
 d. 10 12 14 16 18
 e. 10 12 14 16
    My Answer :  d


3. while 반복문으로 "Hello World!"를 10번 출력한다고 했을 때 잘못된 부분을 고르세요.
 a. i = 0
 b.
 c. while i > 20:
 d.     print("Hello World!")
 e.     i = i + 2
    My Answer :  c

4. 다음 while 반복문 중 무한 루프를 모두 고르세요.
 a. while "":
 b. while 1.1:
 c. while None:
 d. while False:
 e. while not 0:
    My Answer :  b e

"""
## 202P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 17.5 연습문제, 주어진 두 변수를 이용해 2 5, 4 4, 8 3, 16 2, 32 1이 각 줄에 출력되도록 만든다.
i = 2
j = 5

while i < 33 or j > 0:
    print(i, j)
    i = i*2
    j = j-1

# 17.6 심사문제. 교통카드 잔액 출력
# 정수 입력, 1회당 1350원. 사용할때마다 잔액 출력 / 최초 금액은 미출력. 잔액은 음수 x , 부족하면 break
print("17.6 심사문제 -  버스 잔액 출력")
money = int(input())
while money >= 1350:
    money = money-1350
    print(money)


## 204P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break

for i in range(100):
    print(i)
    if i == 10:
        break

## 205P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
for i in range(30):
    if i & 2 == 0:
        continue # 원래 print(i)도 해야하는데 컨티뉴 때문에 바로 for로 돌아간다. 투 비 컨티뉴 다음 반복에 계속
    print(i)

i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

## 209P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
cnt = int(input("반복 횟수, 정수로 입력 : "))

for i in range(cnt):
    if i % 2 == 0:
        print(i)

## 210P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
""" 18. 4 퀴즈
1. 다음 중 break와 continue에 대한 설명으로 올바른 것을 모두 고르세요.
 a. break는 if 조건문을 끝낸다.
 b. break while문을 끝낸다.
 c. break는 for range 반복문에 사용할 수 없다.
 d. continue는 코드를 실행하지 않고 건너뛰며 루프를 중단하지 않는다.
 e. continue는 코드를 실행하지 않고 건너면 뒤 루프를 중단한다.
    My Answer : b d

2. 다음 코드로 1부터 10까지 출력하면서 3의 배수는 제외하려고 할 때 밑줄 부분에 들어가야 할 코드를 고르세요.
 for i in range(1, 11):
 ___________________
    ________________
 print(1)

 a. if 1 % 3  == 0:
        break
 b. if 1 % 3 == 0:
        continue
 c. if 1 % 3 != 0:
        break
 d. if 1 % 3 != 0:
        continue
 e. if i % 3 == 1:
        print(1)
    My Answer : b

3. 다음 코드로 30부터 10까지 출력할 때 밑줄 부분에 들어가야 할 코드를 고르세요.
 i = 30

 while True:
    print(1)
    ______________
        ________
    i -= 1

 a. if i != 10:
        break
 b. if i != 10:
        continue
 c. if i ==10:
        break
 d. if i == 10:
        continue
 e. if i <= 30:
        continue
    My Answer : c
"""
## 211P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 18.5 연습문제 | 0~73 중에 3으로 끝나는 숫자만 출력
i = 0
while True:
    if i%10!=3:
        i += 1  # 여기도 안넣으면 무한 루프 while - continue
        continue
    if i > 73:
        break
    print(i, end=" ")
    i += 1

## 212P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 18.6 심사문제 | 정수 2개 입력, 1~200 하나 10 ~ 200 하나. 첫번째가 두번째 숫자보다 작아야함. 두 정수 사이에 3으로 끝나지 "않는" 숫자 출력
one, two = map(int, input().split()) 

while True:
    if one > two:
        break
    if one%10 != 3:
        print(one, end=" ")
    one += 1

## 213P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
for i in range(5):
    for j in range(5):
        print("J:", j, sep="", end=" ")

    print("i", i, "\\n", sep="")

## 214P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
for i in range(5): # 세로
    for j in range(5): # 가로
        print("*",end="")
    print()

for i in range(5): # 세로
    for j in range(5): # 가로
        if j <= i:
            print("*",end="")
    print()

for i in range(5): # 세로
    for j in range(5): # 가로
        if j == i:
            print("*",end="")
        else:
            print(" ", end=" ")
    print()

## 217P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
""" 19.5 퀴즈
1. 다음 코드에 대한 설명으로 잘못된 것을 모두 고르세요. 
 | for i in range(5):          |
 |    for j in range(5):       |
 |        print("*", end="")   |
 |    print()                  |
 └ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ┘
 a. 정사각형 모양 별 출력
 b. 반복문 안에 반복문이 들어있는 중첩 루프다.
 c. i가 있는 반복문은 가로 방향을 처리한다.
 d. j가 있는 반복문은 가로 방향을 처리한다.
 e. print()처럼 아무것도 지정하지 않으면 print()는 줄바꿈을 하지 않는다.
    My Answer : c e

2. 다음과 같은 모양으로 별을 출력할 때 밑줄 부분에 들어가야할 조건식을 고르세요.
 | for i in range(5):              |  실행 결과
 |    for j in range(5):           |    *
 |        if _____:                |    **
 |           print("*", end=" ")   |    ***
 |    print()                      |    ****
 └ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ┘    *****
 a. i <= j
 b. i < j
 c. j <= i
 d. j < i
 e. j == i
    My Answer : c


"""

## 218P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 19.5 연습 문제 | 역 삼각형 모양 별 출력
for i in range(5):
    for j in range(5):
        if j >= i:              # line3 " , ,***" 3,1 3,2 | 3,3 출력 j가 i보다 크거나 같을때 별 출력 // 나머지는 공백
            print("*", end="")
        else:
            print(" ", end="")
    print()

## 219P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 19.6 심사문제 | 입력 정수의 높이만큼의 산을 별로 출력.
hei = int(input())
h = 0 # 반복 제어 변수
s = 0 # 별 조절 변수
while h<hei:
    for i in range(1,hei+1): # 세로 |hei = 5, 1~5반복 (층 정리)
        for j in range(1,(hei*2)): # 가로 | hei에 비례해 가로 생성.

            ## 층에 따라 앞 부분 공백 출력
            if j < int(hei-i+1): #5층이라면, 1층에는 공백 4개 후 별 1개 // 총5층-1층+1 = 5번째 자리. 별이 들어와야함. 그 전까지 공백.
                print(" ", end="")
                continue
            elif j == int((hei-i+1)): # 별 들어올 자리부터 입력.
                print("*"*(i+s),end="") # 층에 따른 별 갯수 조절
                continue
        print() # 가로 출력 후 엔터      
        s = s + 1 
        h += 1


## 220P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# FizzBuzz 1~100 출력 중 3의 배수는 Fizz // 5의 배수는 Buzz // 공배수는 FizzBuzz
for i in range(1,101):
    if i%3 != 0 and i%5!=0:
        print(i, end=" ")
    elif i%3 == 0 and i%5==0:
        print("FizzBuzz")

    elif i%3 == 0:
        print("Fizz", end=" ")
    elif i%5 == 0:
        print("Buzz")
    

## 224P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
"""20.6 퀴즈
1. 다음 중 변수 i가 6의 배수인지 확인하는 방법으로 올바른 것을 고르세요.
 a. i / 6 == 0
 b. i & 6 == 0
 c. i : 6 == 0
 d. i % 6 == 0
 e. i // 6 == 0
    My Answer : d

2. 다음 중 변수 i가 5와 10의 공배수인지 확인하는 방법으로 올바른 것을 모두 고르세요.
 a. i // 5 == 0 or i // 10 == 0 
 b. i ¦ 5 == 0 and i ¦ 10 == 0 
 c. i % 5 == 0 or i % 10 == 0 
 d. i % 5 == 0 and i % 10 == 0 
 e. i % 10 == 0 
    My Answer : c  e
"""

## 225P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 20.7 연습문제 | 1~100 출력 중 2는 Fizz // 11의 배수는 Buzz 2와 11의 공배수는 FIZZBUZZ
for i in range(1,101):
    if i%2 != 0 and i%11!=0:
        print(i, end=" ")
    elif i%2 == 0 and i%11==0:
        print("FizzBuzz")

    elif i%2 == 0:
        print("Fizz", end=" ")
    elif i%11 == 0:
        print("Buzz")

## 226P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 20.8 심사문제 | 5와 7의 배수 공배수 처리
# 정수 2개 입력, 1~1000 , 10 ~1000 범위 2개. 1번째는 무조건 2번째보다 작고. 두 값 사이 수를 출력하면서 이전처럼 fizzbuzz 출력
one, two = map(int, input().split()) 
# 출력 형식 신경x
while True:
    if one > two:
        print("더 작은 숫자를 먼저 적어주세요.")
        break
    print("Fizz"*(one % 5 == 0) + "Buzz"*(one % 7 ==0) or one)
    # if one % 5 == 0 and one % 7 == 0:
    #     print("FizzBuzz")    
    one += 1
    if one == two:
        break

# 5개씩 끊어서 보기
i = 1
while one < two:    
    if one % 5 == 0 and one % 7 ==0:
        print("FizzBuzz", end=" ")
        print("\n") if i % 5 == 0 else None

    elif one % 5 == 0:
        print("Fizz", end=" ")
        print("\n") if i % 5 == 0 else None
    elif one % 7 == 0:
        print("Buzz", end=" ")
        print("\n") if i % 5 == 0 else None
    else:
        print(f"{one}", end=" ")
        print("\n") if i % 5 == 0 else None

    i = i + 1
    one += 1
