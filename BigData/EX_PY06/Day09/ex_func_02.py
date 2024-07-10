def add(num1, num2):
    result = num1 + num2
    print(result)

def mis(num1, num2):
    result = num1 - num2
    print(result)

def mul(num1, num2):
    result = num1 * num2
    print(result)

def div(num1, num2):
    if num2 == 0:
        result = "0으로 나눌 수 없습니다."
    else:
        result = num1 / num2
    print(result)


## 계산기 프로그램 ------------------------------------------------------------------
# - 사용자가 종료를 원할 때 종료 => 'x' or 'X' 입력 시
# - 연산 방식과 숫자 데이터 입력 받기


while True:
    # 입력받기
    req = input("연산(+,-,*,/) 방식과 숫자 정수 2개를 입력 (예시 : + 10 2) : ")
    # 종료 조건 검사
    if req == "x" or req == "X":
        print("계산기를 종료합니다.")
        break
    # 입력에 연산방식과 데이터 추출
    op, num1, num2 = req.split() # [+ 10 2]
    num1, num2 = int(num1,num2)
    if op == "+":
        print(f"{num1} + {num2} = {add(num1,num2)}")
    elif op == "-":
        print(f"{num1} - {num2} = {mis(num1,num2)}")
    elif op == "*":
        print(f"{num1} - {num2} = {mul(num1,num2)}")
    elif op == "/":
        print(f"{num1} - {num2} = {div(num1,num2)}")
    else:
        print(f"{op}는 지원되지 않는 연산입니다.")
    
