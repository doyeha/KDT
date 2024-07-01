# ------------------------------------------------------------------ 
# 내장함수 print() 사용법
#  - 모니터 즉, 콘솔/터미널에 출력하는 함수
#  - 문법 : print(argument, argu2, argu3, argu4)
# ------------------------------------------------------------------ 
# 나이, 이름, 성별을 저장하기
age = 100
name = "마징가"
gender = "남자"

# 모니터에 출력하기
print(age)
print(name)
print(gender)   

# 한 줄에 3개 모두 출력하기
print(age, name, gender)

# 2개의 정수 덧셈 결과 출력하기
num1 = 2
num2 = 9
print( num1 + num2 )

print(num1, "+", num2, "=", num1+num2 )

# ==> 화면 출력 글자를 만들곡 그 글자 안에 특정 결과를 출력하는 형식
# ==> 글자 내부에 정수 결과 넣기 ' %d '  %변수명 또는 %수식
# ==> 글자 내부에 실수 결과 넣기 ' %f '  %변수명 또는 %수식
# ==> 글자 내부에 글자 결과 넣기 ' %s '  %변수명 또는 %수식

print('num1 + num2 = %d' %(num1+num2))

# 9 / 2 = 4.5
print('%d / %d = %f' %(num1 , num2, num1/num2)) # 순서대로 들어간다.
print('%s / %s = %s' %(num1 , num2, num1/num2))  #형변환, 정수를 문자열로 변형


# ==> F-string 방식
# ==> 형식 : f'     '
print(f"{num1} + {num2} = {num1+num2}")

print(num1, "+", num2, "=", num1+num2 )
print(f"{num1} + {num2} = {num1+num2}")