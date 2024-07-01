# ------------------------------------------------------------
# 문자열 전용의 함수 즉, 메서드 살펴보기 (4)
# ------------------------------------------------------------
# 문자열 안에 문자 종류 검사 관련 메서드

# 문자열이 알파벳으로만 구성된 문자인지 검사 메서드
# 메서드명 : isalpha()
# 형식 : 변수명.isalpha()
# 결과 : true or false
# 

data = "abc"
print(data.isalpha())
data = "abc "
print(data.isalpha())
data = "abc!"
print(data.isalpha())
#한글
data = "오늘"
print(data.isalpha())  #True
data = "오늘!"
print(data.isalpha())   #False
   #isalpha()는 각 나라의 언어 모두 사용 가능, 굳이 영어가 아니어도 됨. 
#한글
data = "䖓"
print(data.isalpha())  #True
data = "आज"
print(data.isalpha())   #False

data = "abc"
print(data.isnumeric()) # << 숫자 체크.