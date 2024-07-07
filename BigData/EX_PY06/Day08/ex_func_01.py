# ------------------------------------------------------------------
# 사용자 정의 함수
# ------------------------------------------------------------------
# 함수 기능 : 2개 정수를 덧셈한 후 결과를 반환/리턴하는 함수
# 함수 이름 : add
# 매개 변수 : 2개, num1, num2 (어떤 변수가 들어올 지 알아야한다.)
# 함수 결과 : 덧셈 계산 값 result
# ------------------------------------------------------------------

def add(num1, num2):
    result = num1 + num2
    return result

def padd(num1,num2):
    result = num1+num2
    return print(result)

print(add(1,5))
padd(1,8)




def inp_add():
    num1, num2 = map(int,input().split())
    result = num1+num2
    return print(result)

inp_add()


# 함수 사용하기 즉, 함수 호출
# 함수명 (데이터 ... )
value = add(10,20)
print(value)

# 함수의 매게변수 개수와 다른 데이터 전달 X ERROR
value = add(10,40,50)







