# # 1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
# . 출력하는 코드 구현하세요
# [입력] msg = [‘Good’, ‘child’, ‘Zoo’, ‘apple’, ‘Flower’, ‘ zero’]
# 함수호출
# [출력] 정렬 결과 : ['zero', 'child', 'apple', 'Zoo', 'Good', 'Flower']
# 가장 높은 문자열 : zero,가장 낮은 문자열 : Flower 
# msg = (input("언어로 구성된 리스트를 입력해주세요."))
# msg = msg.split(",")
# print(msg)
# msg2 = msg.sort()
# print(f"정렬 결과 : {msg2}")
# print(f"가장 높은 문자열 : {msg2[0]}, 가장 낮은 문자열 : {msg2[-1]}")


# 2. 입력 받은 데이터 중에서 숫자만 모두 저장하여 합계 최대값 최소값을 출력하는 코드를 구현하세요
# [입 력] : 데이터 입력 : 하늘 Apple 2021 9 False 23 7 None 끝
# [ 출 력 ] 합계 : 2060     최댓값 : 2021   최솟값 : 7 
# ----------------------------------------------------------------------------------------------
# [입 력 ] 데이터 입력 : 홍길동 A False True True None Good Luck 가나다라
# [출 력] 합계 : 0       최댓값 : 0      최솟값 : 0  
print("[2번]")
msg = input("데이터 입력 : ")
msg = msg.split()
total = 0
max = 0
min = 0
print(msg)

for i in msg:
    if i.isnumeric():
        min = 999
        i = int(i)
        total = total + i
        if max < i:
            max = i
        elif min > i:
            min = i
        
print(f"합계 : {total}, 최대: {max}, 최소 : {min}")
print()

# 3. 아래 조건을 만족하는 코드를 작성하세요 (완)
# - ‘q’, ‘Q’ 입력 전까지 동작
# - 대문자 Q 제외한 나머지 알파벳 입력 시 ♠ 출력
# - 소문자 q  제외한 나머지 알파벳 입력 시 ♤ 출력
# - 0 ~ 9  숫자 입력 시 숫자만큼의 ◎ 출력
print("[3번]")
while True:
    data = input("알파벳을 입력해주세요.")
    if data.islower():
        if data == 'q':
            break
        else:
            print("♤")
    elif data.isupper():
        if data == 'Q':
            break
        else:
            print("♠")
    elif data.isnumeric():
        data = int(data)
        print("◎"*data)
    else:
        ("잘못 입력하셨습니다.")
        

# 4. . 아래 조건을 만족하는 코드를 작성하세요 (완)
print("[4번]")
data = range(1,101)
for r in data:
    if not r%3 or not r%7 or not r%8:
        print(r, end=" ")
print()
# 5. 문자열을 입력하면 코드값을 아래와 같이 출력해주는 함수를 구현해 주세요.
print("[5번]")
data = input("문자열을 입력해주세요. : ")
print(f"{data}의 인코딩 : ", end="")
for r in data:
    r = hex(ord(r))
    print(r, end="")
print()

print(f"{data} 인코딩 : ", end="")
for r in data:
    r = bin(ord(r))
    print(r, end="")

print()

# 6. 아래와 같이 출력된 함수를 구현해 주세요.
print("[6번]")
dan = input("출력을 희망하는 구구단의 단을 입력해주세요.")
dan = int(dan)
print(f"-------------- {dan}단 -----------------")
cnt = 1
for i in range(1,10):
    print(f"{dan}*{i} = {dan * i}", end="   ")
    if not cnt%3: print() 
    cnt = cnt +1

# 7. 숫자와 콤마로만 이루어진 문자열 가 주어지면 이때 에 포함되어있는 자연수 data , data
# 의 합과 가장 작은 수 가장 큰 수 , 를 출력하는 함수를 구현하세요.
print("[7번]")
data2 = input("숫자와 콤마(,)로만 구성된 문자열을 입력해주세요. (ex. 1213,456,7) : ")
data = data2.split(",")
total = 0
max = 0 
min = 0
for d in data:
    if d.isnumeric():
        min = 999

        d = int(d)
        total = total + d
        if max < d:
            max = d
        elif min > d:
            min = d
    else:
        print("다시 입력해주세요.")
        break
print(f"{data2}의 합 : {total}, 가장 큰 수 {max}, 가장 작은 수 {min}")


# 8. 업 다운 게임 기능 - 의 함수를 구현하세요.
rand = 55 #랜덤 안배움
while True:
    data = input("1 ~ 100 까지의 숫자를 입력해주세요.")
    data = int(data)
    if rand == data:
        print(f"{data}? 정답!!")
        break
    elif rand > data:
        print(f"힌트 {data}보다 큰 수")
        continue
    elif rand < data:
        print(f"힌트 {data}보다 작은 수")
print()
# 9. 월 을 입력 받아 해당 월 의 영어와 계절을 출력하는 코드를 작성하세요 (Month) (Month) .
print("[9번]")
month = int(input("좋아하는 월 입력 : "))
if month <1 or month >12:
    print("존재하지 않는 월입니다.")
else:
    if month==1:
        print("january Winter")
    if month==2:
        print("february Winter")
    if month==3:
        print("March Spring")
    if month==4:
        print("April Spring")
    if month==5:
        print("May Spring")
    if month==6:
        print("June Summer")
    if month==7:
        print("July Summer")
    if month==8:
        print("August Summer")
    if month==9:
        print("September Summer")
    if month==10:
        print("October Fall")
    if month==11:
        print("November Winter")
    if month==12:
        print("december Winter")
print()
        

# 10. 팩토리얼 을 반복문으로 구현해 주세요 (Factorial) while .
# . 팩토리얼 수를 입력 받아서 팩토리얼 결과를 아래와 같이 출력하세요
print("[10번]")
fac = (input("팩토리얼 수 입력 : ")).strip()
if fac.isnumeric():
    fac = int(fac)
    if fac < 1:
        print(f"{fac}! => {fac}")
    else:
        print(f"{fac}! => ", end="")
        fac = int(fac)
        total = 1
        i=0
        while fac-i > 0:
            total = total * fac
            if fac ==1:
                print(f"{fac}", end="") 
            else:
                print(f"{fac} * ", end="") 
            fac = fac - 1
        print(f" = {total}")
else:
    print("숫자만 입력해주세요.")