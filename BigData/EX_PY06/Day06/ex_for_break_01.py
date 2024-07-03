# ------------------------------------------------------------------
# 제어문 - 반복문 중단 break
# - 반복을 중단시키는 조건문과 함께 사용된
# ------------------------------------------------------------------
## [실습] 숫자 데이터의 합계가 30 이상이 되면 더 이상 합계를 하지 마세요.
## 숫자 데이터는 1~50 구성됨.
nums = list(range(1,51))

total = 0

for n in nums:
    if total>=30:
        break
    total = total + n

print(f"total => {total} 1 ~ {n-1}까지의 합")

# ------------------------------------------------------------------
## [실습] 4개 과목점수가 있습니다.
##        과목점수가 40 이하면 불합격입니다.
##        4개 과목 평균이 60점 이상이면 합격입니다.
# ------------------------------------------------------------------
score = list(map(int,(input("4개 과목 점수 입력해주세요. : ").split())))
total = 0
avg = 0


for s in score:
    if s <= 40:
        break
    else:
        ispass = True
    total = total + s
    avg = total/len(score)
if avg >= 60:
    print(f"평균 {avg}점으로 합격입니다.")



for s in score:
    if s < 40:
        print("과락")
        ispass = False
        break
    print("모든 과목이 40점 이상입니다.")
if ispass == False:
    print()


for i in enumerate():
    print(i)