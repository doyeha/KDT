# ------------------------------------------------------- 
# 실습 - for 반복문과 range
# ------------------------------------------------------- 
# [1] 좋아하는 단의 구구단 출력하기
gugu = input("좋아하는 단을 입력해주세요. : ")
if gugu.isnumeric():
   gugu = int(gugu)
   dan = range(1,10)
   for g in dan:
      print(gugu * g, end=" ")

   for g in dan:
      print(f"{gugu} * {g} = {gugu * g} ")
print()


#[2] 문자열의 원소에서 대문자는 소문자로, 소문자는 대문자로 출력해주세요.
# 예) Happy ==> hAPPY
msg = "Happy"
for m in msg:
    if m.isupper():
      print(m.lower(), end="")
    elif m.islower():
       print(m.upper(), end="")
print()

# [3] range를 사용해서 문자열의 요소 출력하기. ????
msg = "Happy hAPPY"
ran = range(len(msg))
for r in ran:
   print(msg[r], end=" ")
print()

# T
msg = "Happy"
for idx in range(len(msg)):
   print(f"{idx} => {msg[idx]}")