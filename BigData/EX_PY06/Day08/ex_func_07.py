# ------------------------------------------------------------------
# 사용자 정의 함수
# ------------------------------------------------------------------
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# - 매개변수 : 정수 2개, num1, num2
# - 함수결과 : 연산 결과 반환
# ------------------------------------------------------------------
"""
def minus(num1, num2):
    return print(num1 - num2)

def plus(num1, num2):
    return print(num1 + num2)

def multi(num1, num2):
    return print(num1 * num2)

def divide(num1, num2):
    return print(num1/num2 if num2 else None)

minus(10,2)
plus(10,2)
multi(10,2)
divide(10,2)
divide(10,0)


# 함수 사용하기 즉, 호출
# [실습] 사용자로부터 연산자, 숫자1, 숫자2를 입력받아서 연산 결과를 출력해주세요.


def calc( op="0", num1=0, num2=0):
    op, num1, num2 = input("연산자 숫자1 숫자2 : ").split(" ")
    if op not in ['+','-','/','%']:
        result = f"{op}는 잘못된 연산자 입니다."
    else:
        if num1.isdecimal() and num2.isdecimal():
            num1,num2 = int(num1), int(num2)
            if op=="+":
                result = num1+num2
            elif op=="-":
                result = num1-num2
            elif op=="/":
                result = num1/num2 if num2 else "0으로 나눌 수 없습니다."
            elif op=="*":
                result = num1*num2
        else:
            result="잘못된 숫자입니다."
    
    return print(result)

calc()
"""

# ------------------------------------------------------------------
# 함수 기능 : 입력데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 갯수 data, count, sep=" "
# 함수 결과 : 유효 여부 True / False
# ------------------------------------------------------------------
def check_data(data, count, sep=" "):
    # 데이터 여부
    if len(data):
        # 데이터 분리 후 갯수 체크
        data2 = data.split(sep)
        return True if count == len(data2) else False
        

    else:
        return False
    

print(check_data("+ 10 3",3))
print(check_data("+ 10 ",3))
print(check_data("+,10,3",3,','))

## 29 ~30 31장은 안함
