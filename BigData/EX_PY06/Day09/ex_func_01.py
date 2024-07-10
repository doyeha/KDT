# ------------------------------------------------------------------
# 함수(function) 이해 및 활용
# ------------------------------------------------------------------
# 함수 기능 : 3개의 정수를 덧셈한 후 결과를 반환하는 함수
# 함수 이름 : add3()
# 매개 변수 : num1, num2, num3
# 함수 결과 : 정수 result
# ------------------------------------------------------------------
def add3(num1, num2, num3):
    result = num1 + num2 + num3
    return result



# ------------------------------------------------------------------
# 함수 기능 : 3개의 정수를 곱셈한 후 결과를 반환하는 함수
# 함수 이름 : multi3()
# 매개 변수 : num1, num2, num3
# 함수 결과 : 정수 result
# ------------------------------------------------------------------
def multi3(num1, num2, num3):
    result = num1 * num2 * num3
    return result
print(multi3(2,6,8))

# ------------------------------------------------------------------
# 함수 기능 : 2개의 정수를 나눗셈한 후 결과를 출력하는 함수
# 함수 이름 : div3()
# 매개 변수 : num1, num2
# 함수 결과 : 실수 result
# ------------------------------------------------------------------
def div(num1, num2):
    if num2 == 0:
        result = "0으로 나눌 수 없습니다."
    else:
        result = num1 / num2
    print(result)
    # return print(result) => None

def div1(num1, num2):
    if not num2:
        result = None
    else:
        result = num1 / num2

    print(f"{num1}/{num2}={result}")

# 함수 사용하기
values = add3(1,2,3)


div(1,0)
div1(1,0)

## 나눗셈 하기 
values1 = div(3,4)
print(values1)

# return .. 차이, values는 return result받았으니 값이 들어가지만 div1은 없어서 None이 된다.


# ------------------------------------------------------------------
# 함수 (Function) 이해 및 활용
# 함수 기반 계산기 프로그램
# - 4칙 연산 기능별 함수 생성 => 덧셈, 뺄셈, 곱셈, 나눗셈
# - 2개 정수만 계산
# ------------------------------------------------------------------
def get_add(num1, num2):
    result = num1 + num2
    print(result)

def get_minus(num1, num2):
    result = num1 - num2
    print(result)

def get_multi(num1, num2):
    result = num1 * num2
    print(result)

def get_div(num1, num2):
    if num2 == 0:
        result = "0으로 나눌 수 없습니다."
    else:
        result = num1 / num2
    print(result)



def get_calc(num1,stri,num2):
    if stri == "+":
        result = num1 + num2
    elif stri == "-":
        result = num1 - num2
    elif stri == "/":
        result = num1 / num2
    elif stri == "*":
        result = num1 * num2
    return result


print(get_calc(1,"+",4))



    


