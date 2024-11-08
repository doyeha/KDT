# ------------------------------------------------------------
# 키보드로 입력받아서 연산 수행하기
# - input() 내장함수
# - 연산자 사용
# ------------------------------------------------------------
#[1] 연산 수행할 데이터 입력받기.
no1 = input("산술 연산을 위한 숫자 1 입력 : ")
no2 = input("산술 연산을 위한 숫자 1 입력 : ")


# 데이터 확인
print(f'{no1} 타입 : {type(no1)}')
print(f'{no2} 타입 : {type(no2)}')

#str ==> int 자료형 변환 : 형변환, 타입캐스팅, 캐스팅
# 컴은 입력값을 무조건 str로 받는다. 그래서 연산을 하기 위해서는 int로 형변환을 해줘야한다.
# int ('0~9')
no1 = int(no1)
no2 = int(no2)

#[2] 산술 연산 수행 후 출력
# 덧셈 => 출력
print(f'{no1} + {no2} = {no1 + no2}')
print(f'{no1} - {no2} = {no1 - no2}')
print(f'{no1} * {no2} = {no1 * no2}')
print(f'{no1} / {no2} = {no1 / no2}')