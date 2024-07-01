# -----------------------------------------------------------------------------
# 문자열 관련 내장함수
# 
# -----------------------------------------------------------------------------
# 사람이 사용하는 문자 ====> 컴퓨터 언어 즉, 기계어 변환 함수
# 함수명 : ord(문자 1개만)
# 결과값 : 코드값 10진수 

print(f"A 코드값 : {ord('A')}, {bin(ord('A'))}")
print(f"B 코드값 : {ord('B')}, {bin(ord('B'))}")
print(f"a 코드값 : {ord('a')}, {bin(ord('a'))}")
print(f"b 코드값 : {ord('b')}, {bin(ord('b'))}")

print(f"A<a : {'A'<'a'}")



# -----------------------------------------------------------------------------
# 컴퓨터 언어 즉, 기계어 ===> 사람이 사용하는 문자 변환 함수
# 함수명 : chr(정수 코드값)
# 결과값 : 문자 1개
# -----------------------------------------------------------------------------
print(f"chr(65) : {chr(65)}")
print(f"chr(33) : {chr(33)}")


#[실습] 'Hello'를 코드값으로 변환하세요.
print(f"'H': {ord("H")}")
print(f"'H': {ord("e")}")
print(f"'H': {ord("l")}")
print(f"'H': {ord("l")}")
print(f"'H': {ord("o")}")

msg = 'Hello'
ord("H")
j = len(msg)