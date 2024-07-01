# ---------------------------------------
# [실습] 기능 구현하기.
# - 조건1 : 계산할 숫자와 연산자를 한 번에 입력 받기
#           (예 : 10 5 +) 또는 (예 : 10, 5, *)
# 
# --------------------------------------- 

print()

msg = input("계산할 숫자를 입력해주세요.")
calc = msg.split()

if calc[2]=="*":
    print(f"{calc[0]} {calc[2]} {calc[1]} = {(int(calc[0]))*(int(calc[1]))}")
if calc[2]=="/":
    print(f"{calc[0]} {calc[2]} {calc[1]} = {(int(calc[0]))/(int(calc[1]))}")
if calc[2]=="+":
    print(f"{calc[0]} {calc[2]} {calc[1]} = {(int(calc[0]))+(int(calc[1]))}")
if calc[2]=="-":
    print(f"{calc[0]} {calc[2]} {calc[1]} = {(int(calc[0]))-(int(calc[1]))}")


a = input()
print(f"{a}, {ord(a)}")
  