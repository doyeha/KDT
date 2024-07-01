# # ---------------------------------------------------------
# # PYTHON EXAM 반복문
# # 제출 : work_0610_이름.py   Day12
# # ---------------------------------------------------------
# [1] nums = [13, 21, 12, 14, 30, 18] 데이터에 대해 작성하세요.
# (1) nums의 모든 요소를 for반복문으로 출력
# (2) nums에서 짝수값만 for반복문으로 출력
# (3) nums에서 모든 요소 값의 합계와 평균 출력
print("[1]")
nums = [13, 21, 12, 14, 30, 18]
# (1)
print("n의 모든 요소 : ", end="")
for n in nums:
    print(n, end=" ")
print()
# (2) 
print("n의 짝수 요소 : ", end="")
for n in nums:
    if not n%2:
        print(n, end=" ")
print()
# (3)
sum = 0
for n in nums:
    sum = sum+n
print(f"nums 값의 모든 합 : {sum}")
print(f"nums 평균 값 : {sum/len(nums)}")
print("\n")

# [2] 데이터에서 모든 요소 길이 출력하세요.
# com = ["SK하이닉스", "삼성전자", "LG전자"]
# [출력] 
# SK하이닉스 - 6개
# 삼성전자 - 4개
# LG전자 - 4개
print("[2]")
com = ["SK하이닉스", "삼성전자", "LG전자"]
for c in com:
    print(f"{c} - {len(c)}개")
print("\n")

# [3] 1~50 범위의 데이터를 저장 후 요소들을 아래와 같이
#     출력하세요.
# [출력] 
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30
# 31 32 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48 49 50
print("[3]")
data = range(1,51)
line = int(len(data)/10) # 5
cnt = range(line)

for i in data: # 1~50 출력
    print(i, end=" ")
    if i/10 in cnt:
        print()
print("\n")


# T
print("[3]")
data = range(1,51)

for i in data: # 1~50 출력
    if i%10:
        print(i, end="\n")
    else:
        print(i)

    print(i, end=" ") if n%10 else print(i)    
print("\n")


# [4] 아래 그림과 같이 출력하는 코드 작성하세요.
# *
# **
# ***
# ****
# *****
# ******
print("[4]")
star = range(6)
i = 5
for s in star:
    print(f"{'*'*(len(star)-i)}")
    i = i-1
print("\n")

print("[4 - T]")
for i in range(1,7):
    print("*"*i)
for i in range(5,0,-1):
    print("*"*i)

print("\n")
# [5] 사용자로부터 원하는 단을 입력 받아서 해당 구구단을 출력하세요.
# [입력] 출력 단 : 3
# [출력] 가로로 출력
#  3 * 1 = 3    3 * 2 = 6    3 * 3 = 9    .....   3 * 9 = 27 
print("[5]")
gugu = input("좋아하는 단을 입력해주세요. : ")
if gugu.isnumeric():
   gugu = int(gugu)
   dan = range(1,10)
#    for g in dan:
#       print(gugu * g, end=" ")

   for g in dan:
      print(f"{gugu} * {g} = {gugu * g} ", end="  ")
print("\n")

# [6] [11, 22, 33, 44, 55] 데이터에 대한 16진수를 아래와 같이 출력
#     하세요.
# [출력]
# 11 => 0xb     22 => 0x16
# 33 => 0x21    44 => 0x2c
# 55 => 0x37
print("[6]")
data = [11, 22, 33, 44, 55]
c = 1
for i in data:
    print(f"{i} => {hex(i)}", end="\t") if c%2!=0 else print(f"{i} => {hex(i)}")
    c= c+1
        