def add(num1, num2): return num1 + num2

def mis(num1, num2): return num1 - num2

def mul(num1, num2): return num1 * num2

def div(num1, num2):  return num1 / num2 if num2 else "0으로 나눌 수 없습니다."

def print_menu():
    print(f"{'*':*^18}")
    print(f"{'계 산 기':*^15}")
    print(f"{'*':*^18}")
    print(f"{'* 1. 덧    셈 *':*^16}")
    print(f"{'* 2. 뺄    셈 *':*^16}")
    print(f"{'* 3. 곱    셈 *':*^16}")
    print(f"{'* 4. 나 눗 셈 *':*^15}")
    print(f"{'* 5. 종    료 *':*^16}")
    print(f"{'*':*^18}")             

# ------------------------------------------------------------------
# 함수 기능 : 계산기 메뉴를 출력하는 함수
# 함수 이름 : print_menu
# 매개 변수 : 없음
# 함수 결과 : 없음
# ------------------------------------------------------------------
"""
계산기
| 1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈  5. """
print_menu()
# print(f"{'*':*^16}") # 가운데 정렬
# print(f"{'*':->16}") # 오른쪽 정렬
# print(f"{'*':-<16}") # 왼쪽 정렬


# ------------------------------------------------------------------
# 함수 기능 : 연산 수행 후 결과를 반환하는 함수
# 함수 이름 : calc
# 매개 변수 : 함수명, str 숫자 2개
# 함수 결과 : 
# ------------------------------------------------------------------
def calc(func, num1, num2, op):
    data = input("정수 2개 입력 (예 : 10 2) : ")
    if check_data(data,2):
        data = data.split()   
        print(f"결과 : {data[0]}{op}{data[1]} = {func(int(data[0]),int(data[1]))}")
    else:
        print(f"{data} : 올바른 데이터가 아닙니다.")

# ------------------------------------------------------------------
# 함수 기능 : 입력 받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수 이름 : check_data
# 매개 변수 : str 데이터, 데이터 갯수
# 함수 결과 : True False
# ------------------------------------------------------------------
# # 갯수 2개되는지, 
def check_data(data, l_data):
    data = data.split()
    if len(data) == l_data:
        check01 = True
    
    isOK = True
    for d in data:
        if not d.isdecimal():
            isOK = False
            break
        return isOK
    if check01 == True and isOK == True:
        result = True
    
#     return True

# def check_data(data,count):
#     # 입력된 str list로 split
#     data = data.split()
#     # 갯수 체크
#     if count == len(data):
#         # 0~9로 구성된 str인지 체크
#         if data[0].isdecimal() and data[1].isdecimal():
#             return True
#         else:
#             return False
#     else:
#         return False



## 계산기 프로그램 ------------------------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택 시 프로그램 종료
# => 반복 ------------> 무한반복 : while
# ------------------------------------------------------------------
while True:
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청 
    choice = input("메뉴 선택 :")
    if choice.isdecimal():
        choice = int(choice)
    
    else: print(" -!9tntwkaks dlqfurgktpwyu")


    # 종료 조건 처리
    if choice == 5:
        print("프로그램을 종료합니다.")
        break


    elif choice == 1:
        # check_data(da)
        print("덧셈")
        # inpu = 
        num1, num2 = map(int,inpu.split())
        if check_data(inpu,len(inpu)) == True:
            calc(add, num1,num2, "+")

    elif choice == 2:
        print("뺄셈")
        num1, num2 = map(int,input("정수 2개 (예시 : 10 2) : ").split())
        calc(mis, num1,num2, "-")

    elif choice == 3:
        print("곱셈")
        num1, num2 = map(int,input("정수 2개 (예시 : 10 2) : ").split())
        calc(mul, num1,num2, "*")

    elif choice == 4:
        print("나눗셈")
        num1, num2 = map(int,input("정수 2개 (예시 : 10 2) : ").split())
        calc(div, num1,num2, "/")
    else:
        print("선택된 메뉴가 존재하지 않습니다.")
    



#  =\ \\
# 발표

#  수요일 반재ㅏ포




