# ------------------------------------------------------------------ 
# 내장함수 print() 내장함수
# - print 함수의 매개변수 알아보기
# - 매개변수(parameter) : 함수 코드 실행 시에 필요한 데이터를 명시해 놓은 것 (서식,형식,갯수의 틀 개념(?))

# - sep 매개변수 : 구분자 의미, 여러 개의 데이터를 보기 좋게 출력되도록 구분해주는 변수
# - end 매개변수 : 출력 데이터의 마지막 부분에 줄바꿈 문자를 추가해놓은 변수


# ------------------------------------------------------------------ 
print()
 # 기본세팅 
 # sep : str  |  None : " "
 # end : str  |  None : "\n"

# 여러 개의 데이터 전달 시 구분 문자를 변경하기
# 010-1111-2222
print("010","1111","2222")   

# 20살
age = 20
print(age, "살")            # 출력결과 : 20 살    →  20 이랑 살이 떨어져서 나온다.
print(age, "살", sep="")    #'' empty 문자  # 출력결과 : 20살

# 화면 출력 후에 문자 설정하기 =? [기본] 줄바꿈 '\n'
print(1)              #1\n
print(2 , end=" ")    #2_
print(3)              #3\n

# 출력 결과는 아래와 같고 print함수는 4개 사용
# 1234567
# abcdefg      ABCDEFG
# 1234567

print("1234567")
print("abcdefg", end="       ")
print("ABCDEFG")
print("1234567")




