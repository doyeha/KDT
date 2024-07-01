# -------------------------------------------------------
# 제어문 - 조건문 살펴보기
# -------------------------------------------------------
# [실습 1] 점수에 대한 학점을 출력하는 코드 작성
# - 학점 : A ~ F
# - A학점 : 90점 이상, B학점 : 80점 이상, C학점 : 70점 이상, D학점 : 60점 이상, F학점 : 이외 나머지.
jumsu = 89

if jumsu >= 90:
    print(f"{jumsu}는 A학점, 최고점이에요!")
elif jumsu >= 80:
    print(f"{jumsu}는 B학점, 달디단 BAM양갱")
elif jumsu >= 70:
    print(f"{jumsu}는 C학점, 괜찮아요. F는 아니잖아요?")
elif jumsu >= 60:
    print(f"{jumsu}는 D학점, 이런 재수강 해야겠는데요?")
else:
    print(f"{jumsu}는, 이건... ㅅㄱㅇ.\n\n")


# ----------------재미용---------------------------------------
sub = input("총 몇과목인가요?")
score = []
i=0
while i < int(sub):
    score[i] = input("각 과목의 점수를 입력해주세요.")
    grade = score[i] + score[i-1]
jumsu1 = grade/int(sub)

if jumsu1 >= 90:
    print(f"{jumsu1}는 A학점, 최고점이에요!")
elif jumsu1 >= 80:
    print(f"{jumsu1}는 B학점, 달디단 BAM양갱")
elif jumsu1 >= 70:
    print(f"{jumsu1}는 C학점, 괜찮아요. F는 아니잖아요?")
elif jumsu1 >= 60:
    print(f"{jumsu1}는 D학점, 이런 재수강 해야겠는데요?")
else:
    print(f"{jumsu1}는, 이건... ㅅㄱㅇ.\n\n")

