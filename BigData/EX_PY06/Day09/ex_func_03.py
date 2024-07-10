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
    num1, num2 = int(num1), int(num2)
    print(f"결과 : {num1}{op}{num2} = {func(num1,num2)}")




## 계산기 프로그램 ------------------------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택 시 프로그램 종료
# => 반복 ------------> 무한반복 : while
# ------------------------------------------------------------------
while True:
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청
    choice = int(input("메뉴 선택 :"))
    if choice.isdecimal():
        choice = int(choice)
    
    else: print(" -!9tntwkaks dlqfurgktpwyu")


    # 종료 조건 처리
    if choice == 5:
        print("프로그램을 종료합니다.")


        break


    elif choice == 1:
        print("덧셈")
        num1, num2 = map(int,input("정수 2개 (예시 : 10 2) : ").split())
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
    



 =\ \\
발표

#  수요일 반재ㅏ포




