# ---------------------------------------
# 제어문 - 조건문
# - 조건에 따라서 실행 코드를 다르게 해주는 문법
# ---------------------------------------
# [실습] 숫자가 양수인지, 음수인지, 0인지 출력하는 코드 작성
# 

number = input("숫자 입력 : ").strip
#str => int로 변환하기 위해서 0~9로 구성된 문자열인지 검사

if number[0]=='-':
    print(f"{number} : {number[1:].isdecimal()}")
else:
    print(f"{number} : {number.isdecimal()}")

if number>0:
    print(f"{number}는 양수입니다.")
elif number<0:
    print(f"{number}는 음수입니다.")
else:
    print(f"{number}는 0 입니다.")
# 통 블럭 = 좌 컨 + ?

#str => int로 변환하기 위해서 0~9로 구성된 문자열인지 검사
