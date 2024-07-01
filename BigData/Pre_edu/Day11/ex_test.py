# -------------------------------------------------------
# [나이를 계산해주세요~]
# - 주민등록번호 입력 받아서 나이 계산
# -------------------------------------------------------
jumin = input("주민번호를 입력해주세요. (ex. 123456-1234567) : ")
year = 2024
age = 0
## 01 / 00 / 9n일때
ju_year = jumin[0:2]
ju_list = jumin.split("-")
gender = ju_list[1][0]

if gender in ['1', '2']:
    age = year - (1900+int(ju_year))
    print(f"{age}살 입니다.")
elif gender in ['3', '4']:
    age = year - (2000+int(ju_year))
    print(f"{age}살입니다.")
else:
    print("주민번호를 다시 확인해주세요.")


# # 강의 답
jumin = input("주민번호를 입력해주세요. (ex. 123456-1234567) : ")
# # 년도 앞자리 찾기
if jumin[7] in ['1', '2']:
    year = "19"+jumin[:2]
else:
    year = "20"+jumin[:2]
print(f"year -> {year}")

# #나이 계산하기
age = 2024 - int(year)
print(f"당신은 {age}이군요")


# -------------------------------------------------------
# 다이아몬드를 출력해주세요.
#   *
#  ***
# *****
#  ***
#   *
# -------------------------------------------------------
print("{:^5}".format("*"))
print("{:^5}".format("*"*3))
print("{:^5}".format("*"*5))
print("{:^5}".format("*"*3))
print("{:^5}".format("*"))

# # 강의 답
pattern = "*"
print(f"{pattern*1:^5}")
print(f"{pattern*3:^5}")
print(f"{pattern*5:^5}")
print(f"{pattern*3:^5}")
print(f"{pattern*1:^5}")