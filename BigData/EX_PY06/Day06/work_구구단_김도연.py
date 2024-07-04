# ------------------------------------------------------------------
# 01. 구구단 전체 출력 => 중첩 for => for 1개로
print("과제 1번. 구구단 전체 출력")
# 몫, 나머지 연산자로.

for i in range(20,100):
    dan = i//10 # 몫 2~10 
    g = i%10 # 나머지,0
    if g==0:
        print(f'{str(dan)+"단" :=^10}')
    else:
        print(f'{dan} * {g} = {dan*g :0>2}')

for i in range(20,100):
    dan = i//10 # 몫 2~10 
    g = i%10 # 나머지,0
    if g==0:
        print(f'{str(dan)+"단" :=^10}')
    else:
        print(f'{dan} * {g} = {dan*g :0>2}')

# for dan in range(2,10):
#     for i in range(1,10):
#         print(f"{dan} * {i} = {dan * i:0>2}", end= "  ")
#     print()

# ------------------------------------------------------------------
# 02. 구구단 전체 출력=> 가로로 출력
""" 예시
2*1 3*2 4 5
2*2 3*2
:

6*1 7*1 8 9
"""
# ------------------------------------------------------------------
print("과제 2번")
print("1번 방법")
g = 0
for i in range(1,3): # 뭉텡이 2개 생성
    for d in range(1,10):
        for dan in range(2+g,6+g):
            print(f"{dan} * {d} = {dan * d:0>2}", end= "\t")
        print()
    g = g+4
    print()


print("2번 - 몇 분단으로 나눌건지?")
# 총 8개. 
tot = 8
bun = int(input("몇개씩 보시겠습니까? 1, 2, 4, 8만 입력해주세요."))
sat = int(tot/bun) # 8개, 기준 2단이면 4 / 4단이면 2 나와야함
# i 상승 시 분단 나눠진 것 만큼 그 수가 올라서 dan이 바뀌어야한다.

lop = 0
for i in range(1,bun+1): # 분단 2개할 예정.
    for d in range(1,10): # 1~9 곱셈 반복
        for dan in range(2+lop,2+sat+lop):      #2 시작에다가 2분단이면 4번 / 4분ㄷ나이면 2번만 반복 
            print(f"{dan} * {d} = {dan * d:0>2}", end= "\t")
        print()
    lop = lop + sat
    print()


"""
17 18  ~ 20장까지 ?
"""