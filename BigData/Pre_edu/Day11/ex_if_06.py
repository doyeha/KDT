# -------------------------------------------------------
# 제어문 - 조건문 살펴보기
# - 형식
# if 조건식:
#    조건식이 True일때 실행되는 코드
# else:
#     조건식이 False일대 실행되는 코드
# -------------------------------------------------------
#
num = 7

if num%2:   #0은 False니까 그 자체로 논리연산 가능.
    print(f"{num}은 홀수")
else:
    print(f"{num}은 짝수")

## ==> 조건부표현식으로 변경
print(f"{num}은 홀수") if num%2 else print (f"{num}은 짝수")

print(f"{num}은 {'홀수' if num%2 else '짝수'}")

if num%2 ==0:
    print(f"{num}은 짝수")
else:
    print(f"{num}은 홀수")
print(f"{num}은 짝수") if num%2==0 else print (f"{num}은 홀수")