# ------------------------------------------------------------------
# 모듈 : 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은 것
#         여러 개의 모듈 파일들 존재
# 모듈 사용법 : import 모듈파일명    <---- 확장자 제외
# ------------------------------------------------------------------
import random as rd

# 임의의 숫자를 생성 추출하기 
rd.random()

for i in range(10):
    print(rd.random()*10)

# randint(a,b)
for cnt in range(10):
    print(rd.randint(0,1))


## [실습] 로또 프로그램을 만들어주세요.
## - 1~45범위 중복되지 않는 6개 추출

lotto = []
while len(set(lotto)) < 6 :
    for i in range(6-len(set(lotto))):
            lotto.append(rd.randint(1,45))
lotto = set(lotto)
lotto = sorted(list(lotto))
print(lotto)

# T's way
lotto=[0,0,0,0,0,0]
idx = 0
while True:
    num = rd.randint(1,45)
    if num not in lotto:
        lotto[idx]= num
        idx = idx +1
    if idx == 6:
        break

    """
    22장부터 메소드 사용 
    """
    
    

