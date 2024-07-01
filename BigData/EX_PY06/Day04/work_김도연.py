# ------------------------------------------------------------------ 
# Work_03_김도연.py
# Day04 (0701)
# 132 ~ 184p  | 12장 ~ 15장
# ------------------------------------------------------------------ 
## 143P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
lux = {"health": 490, "mana": 334, "melee": 550, "armor": 18.72}
print(lux)

# 144P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
lux = {"health": 490,"health": 650, "mana": 334, "melee": 550, "armor": 18.72}
print(lux)
""" 출력 결과 :{'health': 650, 'mana': 334, 'melee': 550, 'armor': 18.72} => 중복 키, 후에 저장된 것만 저장. """

x = {100 : "hundred", False:0, 3.5 : [3.5, 3.5]}
print(x)
 # 딕셔너리 내 값에는 타입 제한x, 단, 키에 리스트와 딕셔너리를 사용할 수 없다.

# 빈 딕셔너리
dic = {}
dic = dict()

# 딕셔너리 생성
dic0 = dict (key1 = 1, key2=2, key3=3) 
    # => 이때 key1,2,3은 자연스럽게 문자열로 저장된다. 따옴표에 넣으면 에러 발생.
dic1 = dict([("key1",1), ("key2",2),("key3",3)])
    # => (키,값)으로 이루어진 리스트를 딕셔너리로.
dic2 = dict( zip(["key1","key2","key3"],[1,2,3]) )
    # => 두 리스트를 묶는 Zip을 이용해 딕셔너리를  만드는 방법.
dic3 = dict({"key1":1,"key2":2,"key3":3})
    # => 딕셔너리 식으로 나열 후 dict로 감쌈.

print(f"{dic0} \n {dic1} \n {dic2} \n {dic3}")

## 146P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
lux = {"health": 490, "mana": 334, "melee": 550, "armor": 18.72}
print(lux["health"])  # => health 400
lux["health"] = 1000
print(lux["health"])    # => health 1000 (수정 가능.)

print("health" in lux)  # => 멤버 연산자 in으로 키 확인은 가능.
print(1000 in lux)      # 값은 확인 불가능\


## 146P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
print(len(lux)) # => 출력 결과 4개. 키:값 한쌍, 1개로 침.

## 12.3 퀴즈
"""
1. 다음 중 딕셔너리를 만드는 방법으로 올바르지 않은 것을 고르세요.
    a. x = {'a':10, 'b':20}
    b. x = {'a'=10, 'b'=20}
    c. x = dict()
    d. x = dict(a=10, b=20)
    e. x = dict({'a':10, 'b':20})
        My Answer : b

2. 딕셔너리 x = {10 : "Hello", "world" : 30}에서 키 10의 값을 출력하는 방법으로 올바른 것을 고르세요.
    a. print(x.Hello)
    b. print(x("Hello))
    c. print(x[Hello])
    d. print(x["Hello])
    e. print(x[10])
         My Answer : e
           
3. 다음 코드를 실행했을 때 출력 결과로 올바른 것을 고르세요.
    fruits = {"apple":1500, "pear":3000, "grape":1400}
    fruits["orange"] = 2000
    print(fruits["apple], fruits["orange])

    a. 1200 2000
    b. 1500 0
    c. 1500 1200
    d. 1200 1500
    e. 1200 3000
        My Answer : c

4. 다음 중 print(len({10:0, 20:1, 30:2, 40:2, 50:4, 60:7}))의 출력 결과로 올바른 것을 고르세요.
    a. 12
    b. 0
    c.{10:0, 20:1, 30:2. 40:3, 50:4, 60:7}
    d. 6
    e. 7
        My Answer : d
"""

# 12.4 연습문제 :딕셔너리에 게임 캐릭터 능력치 저장하기. 체력과 이동속도 출력하기.
camile = {
    "health" : 575.5,
    "health_regen" : 1.7,
    "mana" : 338.8,
    "mana_regen" : 1.63,
    "melee" : 125,
    "attack_damage" : 60,
    "attack_speed" : 0.625,
    "amor" : 26,
    "magic_resistance" : 32.1,
    "movement_speed" : 340,
}

print(camile["health"], camile["movement_speed"])
## 150P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 12.5 심사문제. 문자열 1줄, 숫자 1줄 입력. 첫번째는 키, 두번째는 값으로 딕셔너리 생성 후 출력
# 입력 health health_regen mana mana_regen // 575.5 1.7 338.8 1.63
f_keys = input().split()
s_values = input().split()

camile_dic = dict(zip(f_keys,s_values))
print(camile_dic, type(camile_dic))


## 157P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
x = 10
if x == 10:
    print(f"x: {x}")
else:
    print(f"{x}는 10이 아니야!")

x = 10
if x == 10:
    print(f"x: {x}")
else:
    pass


## 161P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
x = 15

if x >=10:
    print(f"10 이상입니다.")
    if x >= 20:
        print("20 이상입니다.")
else:
    print("10 이하입니다.")


## 163P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
x = int(input())

if x == 10:
    print(f"{x}입니다.")
elif x == 20:
    print(f"{x}입니다")
else:
    print("우리가 원하는 숫자가 아니야")


""" 13.5 퀴즈
1. 다음 중 if 조건문의 사용 방법으로 올바른 것을 고르시오.
 a. if (x == 10)
        print("10입니다.")
 b. if x == 10
        print("10입니다.")
 c. if x == 10:
        print("10입니다.")
 d. if x == 10:
    print("10입니다.")
 e. if x = 10:
        print("10입니다.")
    My Answer : c

2. 다음은 코드에서 잘못된 부분을 모두 고르세요.
 a. x = -20
 b. 
 c. if x < 0
 d      print("0 미만입니다.")
 e.
 f.     if x == -10:
 g.         print("-10 입니다.")
 h. 
 i.     if x == -20:
 j.     print("-20입니다")
    My Answer : c j

3. 다음 중 잘못된 if 조건문을 고르세요 (a와 b는 변수)
 a. if a = b:
 b. if a > b:
 c. if a is b:
 d. if not a:
 e. if a != 10:
    My Answer : a
"""


## 164P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 13.6 연습문제 : if 조건문 사용하기.
# x 의 값이 10이 아닐 때, ok 출력하기.
x = 5
if x != 10:
    print("OK")

## 165P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 13.7 심사문제 : 온라인 할인 쿠폰 시스템. CASH1234는 1234원 할인.
# 예시 입력 : 27000 \n Cash3000 => 출력 : 24000
print("13.7번 심사 문제")
cash = int(input())
discount = input()
discount = int(discount[-4:])
print(f"{cash-discount}")

## 166P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
x = 5
if x == 10:
    print("10")
else:
    print(f"{x}")


## 170P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
if True:
    print("참")
else:
    print("거짓")

if False:
    print("참")
else:
    print("거짓")

if None:
    print("참")
else:
    print("거짓")   # 값이 없으니 0

if "참?":           # 0이 아닌 1 이상의 값은 모두 참으로 인식.
    print("참")
else:
    print("거짓")

if 0:               # 컴퓨터에게 0은 거짓, 1은 참. 그래서 정수 0은 거짓으로 판별
    print("참")
else:
    print("거짓")

if 1:               
    print("참")
else:
    print("거짓")



# 14.4 
x,y = 10,20

if x == 10 and y == 20:
    print("모두 참")
else:
    print("ㅠ")

x,y = 10, 10
if x == 10 or y == 20:
    print(f"x: {x}, y : {y}. x=10 or y = 10 ?" "참")
else:
    print(f"x: {x}, y : {y}. x=10 or y = 10 ?" "거짓")


## 173P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
""" 14.5 퀴즈
1. 다음 중 if 조건문에 대한 설명으로 올바른 것을 고르세요.
 a. if의 코드는 조건식이 만족하지 않을 때 실행된다.
 b. else의 코드는 조건문이 참일 때 실행된다.
 c. else는 단독으로 사용할 수 없다.
 d. else에서 실행되는 코드는 다음 줄에서 들여쓰기를 하지 않아야 한다.
 e. if는 항상 else가 있어야 한다.
    My Answer : c


2. 다음 if, else 조건문에서 잘못된 부분을 모두 고르세요.
 a. if x >= 10:
 b. print('x에 들어있는 값은')
 c.     print('10 이상입니다.')
 d. else
 e.     print('x에 들어있는 값은.')
 f.     print('10 미만입니다.')
    My Answer : b d


3. 다음 코드의 출력 결과를 입력하세요.
 if not "":
    print(True)
 else:
    print(False)
    My Answer : True

4. 다음 중 if에서 조건식을 여러 개 지정하는 방법으로 올바른 것을 모두 고르세요(x와 y는 변수).
 a. if x == 10 & y == 20:
 b. if x == 10 or y == 20:
 c. if x== 10 not y == 20:
 d. if x 10 : y= 20:
 e. if x and y:
    My Answer : b e 

5. 다음 소스 코드를 실행했을 때 출력 결과로 올바른 것을 고르세요.
 x = 5
 if x % 2 ==0:
    print("짝수')
 else:
    print(홀수)

 a. 홀수
 b. 투수
 c. 2
 d. 4
 e. 아무것도 출력되지 않는다.
    My Answer : a
"""


## 174P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 14.6 연습문제 : 합격 여부 판단 || 필기 80점 이상 합격 
written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print("합격")
else:
    print("불합격")

# 14.7 심사문제 : 국영수과 점수 입력, 평균 80이상 합격|| 0~100 밖이면 잘못된 점수
# 입력 : 89 72 93 82 : 합격
# 입력 : 89 72 93 104 : 잘못된 점수
# 풀이 1번
score = list(map(int,input().split()))
print(score,type(score))

if 100 >= int(score[0]) >= 0:
    if 100 >= int(score[1]) >= 0:
            if 100 >= int(score[2]) >= 0:
                    if 100 >= int(score[3]) >= 0:
                        avg = sum(score)/len(score)
                        if avg >= 80:
                            print("합격")
                        else:
                            print("불합격")
                    
            else:
                print("잘못된 점수입니다.")
    else:
        print("잘못된 점수입니다.")
else:
    print("잘못된 점수입니다.")


# 풀이 2번
score = list(map(int,input().split()))

avg = sum(score)/len(score)
if avg < 80:
     print("불합격")
else:
    if 0 <= score[0] and score[1] and score[2] and score[3] <=100:
         print("합격")
    else:
         print("잘못된 점수입니다.")


## 176P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
x = input("아무 정수 숫자")
if x > 10:
    print(f"{x}는 10보다 크다.")
elif x > 20:
    print(f"{x}는 20보다 크다")
else:
    print("수가 너무 작아.")


button = int(input("자판음료 1~4번 입력, 랜덤 선택"))

if button == 1:
    print("콜라 당첨!")
elif button == 2:
    print("사이다 당첨!")
elif button == 3:
    print("환타 당첨!")
elif button == 4:
    print("탄산수 당첨!")
else:
    print("1~4 범위 밖.")


## 179P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
""" 15.2 퀴즈
1. 다음 중 if 조건문에 대한 설명으로 잘못된 것을 모두 고르세요.
 a. elif는 여러번 사용할 수 있다.
 b. else는 elif 앞에 올 수 없다.
 c. elif는 조건식을 지정할 수 없다.
 d. elif는 단독으로 사용할 수 있다.
 e. elif는 항상 else가 있어야 한다.
    My Answer : d e

2. 다음 if 조건문을 실행햇을 때 출력되는 결과를 고르시오.
 x = 10

 if x == 4:
    print("A")
 elif x == 3:
    print("B")
 elif x == 2:
    print("C")
 elif x == 1:
    print("D")
 else:
 print("E")
    My Answer : e
"""


## 180P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 연습문제 : if elif else 모두사용하기 | x가 11~20 / 21~30 / 아무것도 해당되지 않음. 범위 출력
x = int(input())
if 11 <= x  <= 20:
    print("11~20")
elif 21 <= x  <= 30:
    print("21~30")
else:
    print("해당되지 않음.")

# 심사문제 : 교통카드 시스템 만들기
# 잔액 9000, 7세 이상만 입력되며, 7~12는 650 / 13~18은 1050 / 19~ 1250 사용하는 식으로 / 남은 금액 출력
age = int(input())
cash = 9000

if 7 <= age <= 12:
    cost = 650; print(cash - cost)
elif 13 <= age <= 18:
    cost = 1050; print(cash - cost)
elif 19 <= age:
    cost = 1250; print(cash - cost)
else:
    print("사용 불가능")
