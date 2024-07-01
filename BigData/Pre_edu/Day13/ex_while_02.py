# -------------------------------------------------------
# 제어문 - while 반복문
# -------------------------------------------------------
# [실습] 정수를 입력받아서 정수의 누적 합계가 30이상 되면 입력을 중단하세요.

sum = 0
while True:
    data = input("정수를 입력해주세요. : ")
    data = int(data)
    sum = sum + data
    if sum >=30: break
print(f"------End. 도합 {sum} ------")

# -------------------------------------------------------
# [실습] Up-Down 게임 구현
# -------------------------------------------------------
target = 21
while True:
    num = int(input("점수 입력 : "))
    if num == target:
        print("성공!")
        break  
    elif num > target:
        print(f"Down!")
    elif num < target:
        print("Up!")