# -------------------------------------------------------
# 제어문 - 조건문 살펴보기
# -------------------------------------------------------
# [실습2] 단순 계산기 구현하기
# - 숫자 2개와 연산자 1개 입력받기
# - 단, input()은 1번만 사용
# -------------------------------------------------------
data = input("숫자 2개와 사칙연산자() 중 1개 입력 \n (ex. 10 30 *) : ").strip()
datas = data.split()
print(datas)

# 2개 문자열 숫자 ===> 정수 숫자 형변환
num1 = int(datas[0])
num2 = int(datas[1])
calc = str(datas[2])
if calc == '+':
    print(f"{num1}+{num2}는 {num1+num2}")
elif calc =="-":
    print(f"{num1}-{num2}는 {num1-num2}")
elif calc =="*":
    print(f"{num1}*{num2}는 {num1*num2}")
elif calc =="/":
    if num1 == 0 or num2 == 0:
        print("0으로 나눌 수 없습니다.")  
    else:
          print(f"{num1}/{num2}는 {num1/num2}")   
else:
    print("오류 발생!")