# ------------------------------------------------------------------
#   입력 & 출력 실습
# ------------------------------------------------------------------
# [실습1] 데이터 저장 및 변수 생성
# - 생년월일
# - 띠 (용,범...)
# - 혈액형
# 0000년 00월 00일 000띠입니다. 혈액형은 ____ 입니다.
# ------------------------------------------------------------------

# birth = input("생년월일을 입력해주세요.")
# ch_zodiac = input("띠를 입력해주세요.")
# blood = input("혈액형을 입력해주세요.")
# print(f"오! {birth}생이시고 {ch_zodiac}에 {blood}형이시군요. 반가워요!")
# print(f"{birth} {ch_zodiac}입니다. 혈액형은 누구에게나 헌혈이 가능한... {blood}입니다.")


b_year = 2000
b_month = 4
b_day = 11
c_zodi = "용"
blood = "O형"
print(f"{b_year}년 {b_month}월 {b_day}일 생이고 {c_zodi}띠 입니다. 혈액형은 누구에게나 헌혈이 가능한... {blood}입니다.")


# [실습2] 입력 받은 데이터 저장 단, 파일로 저장
# 좋아하는 계절
# 좋아하는 나라
# 여행가고 싶은 나라
# ------------------------------------------------------------------
season = input("좋아하는 계절은? ")
country = input("좋아하는 나라는? ")
trip = input("여행가고 싶은 나라는? ")

FILENAME = "sel.txt"
f = open(FILENAME, mode="w")
f.write("좋아하는 계절은 {season}이다. 좋아하는 나라는 {country}이고, 여행가고 싶은 나라는 {trip}이다.")
print("좋아하는 계절은",season,"이다. 좋아하는 나라는 ",country,"여행가고 싶은 나라는 ",trip,"이다.", file=f)
f.close()


FILENAME = "info.txt"
f = open(FILENAME, mode="w", encoding="utf-8")  #encoding="utf-8 한글 깨질 경우에 추가.
f.write(season)
f.write("\n")       # 줄바꿈 문자
f.write(country)
f.write("\n")       # 줄바꿈 문자
f.write(trip)
f.close()

# print는 자동으로 줄 바꿈이 있음.
print(f"좋아하는 계절 : {season}", file=f)
print(f"좋아하는 나라 : {country}", file=f)
print(f"여행가고 싶은 나라 : {trip}", file=f, end="")