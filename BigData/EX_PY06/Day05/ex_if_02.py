# ------------------------------------------------------------------ 
# ==> 1줄로 조건식을 축약 : 조건부 표현식
# 
# ------------------------------------------------------------------ 
# [실습] 입력된 임의의 숫자가  5의 배수인지 결과를 출력하세요.
# 단, 2와 5를 제외한 나머지는 고려하지 않습니다.
x = int(input())
print(f"{x}는 5의 배수입니다") if x%5==0 else print("탈락.")

## [실습] 문자열을 입력받아서 문자열의 원소 개수를 저장
## - 단, 원소 개수가 0이면 None 저장
## (1) 입력받기 input()
## (2) 원소/요소 개수 파악 len()
## (3) 원소/요소 저장. 단, 0인 경우 None 저장

st = str(input("문자열 입력 : "))
s = len(st)
if s==0:
    st = None
    print(st)
else:
    print(f"문자열의 요소/개수는 {s}개")


## [실습] 연산자(4칙 연산자 : + - * /)와 숫자 2개 입력받기
## - 입력된 연산자에 따라 계산 결과 저장
## - 예) + 10 3

op = input().split()
dus = op[0]
num1 = int(op[1])
num2 = int(op[2])

print(num1+num2) if dus =="+" else None
print(num1-num2) if dus =="-" else None
print(num1*num2) if dus =="*" else None
print(num1/num2) if dus =="/" else None





print(num1+dus+num2)