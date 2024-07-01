# ------------------------------------------------------------
# 메서드(Method) : 특정 데이터 전용 함수의미
# - 형식 : 변수명.전용함수()
# 
# ------------------------------------------------------------d
data = 9.12
print(data.is_integer())

data = "Happy"
print(data.index("a"))

# 가독성을 높이기 위한 서식 설정 메서드
data.format()

year = 2020
month = 11
day = 6

msg = "오늘은 {}월 {}일 {}일입니다.".format(year, month, day)

print(msg)


year = 2024
month = 6
day = 31

# 글자의 가독성을 높이기 위한 서식 설정 메서드
# index-value 형식
d_day="프로젝트 D-Day  : {}년 {}월 {}일".format(year, month,day)      #012 순서 그대로라면 {0}{1}{2} 순서 입력해야하지만 생략도 가능.
d_day="프로젝트 D-Day  : {1}월 {2}일, {0}년".format(year, month,day)  # 순서 지정
print(d_day)

# name-value 형식
d_day="프로젝트 D-Day  : {y}년 {m}월 {d}일".format(y=year, m=month, d=day)

print(d_day)

