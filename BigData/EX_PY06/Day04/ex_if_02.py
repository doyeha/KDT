# ------------------------------------------------------------------
# [실습] 숫자를 입력받아서 음이 아닌 정수와 음수 구분하기.
## - 출력 : 숫자 -5는 음수입니다.
# ------------------------------------------------------------------

a = int(input("정수를 입력해주세요. : "))

if(a<0):
    print(f"숫자 {a}는 음수입니다.")
elif(a>=0):
    print(f"숫자 {a}는 양수입니다.")
else:
    print("잘못 입력하셨습니다.")



# ------------------------------------------------------------------
# [실습] 점수를 입력받아서 합격과 불합격 출력
# - 합격 : 60점 이상
# ------------------------------------------------------------------
score = int(input("당신의 점수를 입력하세요. : "))
if score < 60:
    print("유감스럽게도 불합격입니다.")
elif score >= 60:
    print("축하드립니다. 합격입니다!")
else:
    print("잘못입력하셨습니다. ")

# ------------------------------------------------------------------
# [실습] 점수를 입력 받아서 학점 출력
# - ABCDF
# ------------------------------------------------------------------
g_score = int(input("[학점 환산기] 점수를 입력해주세요 : "))
grade = ""
if g_score >= 90:
    grade = "A"
elif g_score >= 80:
    grade = "B"
elif g_score >= 70:
    grade = "C"
elif g_score >= 60:
    grade = "D"
elif g_score < 60:
    grade = "F"
print(f"당신의 학점은 {grade}학점 입니다.")

