# ------------------------------------------------------------------
# 문자열 str 데이터 다루기
#  - 문자요소 연산 : 산술, 비교, 멤버연산 
# ------------------------------------------------------------------
## [1] 산술 연산 
data1 = "Happy"
data2 = "Year"

# 덧셈(+)연산 :  str + str => str 연결
print(f"{data1} + {data2} => {data1+data2}")
# print(f"{data1} + {10} => {data1 + 10}") # str + int 형 합산 불가능 오류 발생!
print(f"{data1} + {10} => {data1 + str(10)}")

# 뺄셈(-)연산 : str - str : 미지원
# print(f"{data1} - {10} => {data1 - str(10)}")


# 곱셈(*)연산 : str * str : 미지원    |   str * int : int만큼 str 반복
# print(f"{data1} * {data2} => {data1 * data2}") 
print(f"{data1} * {10} => {data1 * 10}")


## [2] 멤버 연산 ---------------------------
## 요소/원소 in 문자열 : True or False
## 요소/원소 not in 문자열 : True or False
print(f"h in {data1} : { 'h' in data1}")
print(f"h not in {data1} : {'h' not in data1}")

# 원소/요소를 가진 데이터 타입에서 사용 가능!
# print( 3 in 123 ) # Error
# print(len(123))   #Error