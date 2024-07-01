# ------------------------------------------------------------
# 데이터 타입 즉, 자료형
# - 컴퓨터에서 메모리 낭ㅇ비 없이 데이터를 저장하기 위한 방법으로 데이터 종류에 따라서 사용 데이터 칸수를 정한 것이다.
# - 프로그래밍 언어마다 조금씩 차이가 있다.
# - 종류 
#   * 수치 데이터 : 정수(Integer as a 'int'),  실수(floating point as a 'float'),  복소수(complex) 
#   * 글자 데이터 : 문자열 string as a 'str'
#   * 논리 데이터 : 논리형 boolean as a 'bool'
#   * 바이트 데이터 : 데이터를 2진수로 저장하는 데이터 타입 : bytes
# 
# ------------------------   Tips! cls = clear 줄임말   ------------------------

# 데이터 종류별 타입 확인 -> 내장함수 type() 사용
# 숫자 100의 타입 출력하기
print(type(100))
#숫자 100.0 타입 출력하기
print(type(100.0))
#숫자 100을 '100' 타입을 출력하기.
print(type('100'))
print(type('A'), type("A"))

#스페이스바의 타입을 출력하기
print(type(" "))
   #스페이스바도 문자열로 인식한다. 그래서 무조건 '' 또는 "" 내부에 스페이스 바를 해야한다.
   # 키보드에서 입력되는 것은 모두 '',"" 감싸기.
# 빈 문자열로 empty string '', "" 사이에 아무것도 없는 경우.
print(type('')) #empty str

# 참, 거짓 또는 맞다, 틀리다 데이터를 저장 -> 논리형 데이터 타입
print(type(True))
# print(type(true)) 소문자 t, true는 논리형 아님.