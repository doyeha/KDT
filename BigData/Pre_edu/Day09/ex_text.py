# [실습1] 'Good Luck 2025'에서 문자열 내 공백을 '*"로 변경하세요.
msg ='Good Luck 2025'
msg1 = msg.replace(" ", " * ")
print(msg1)

# [실습2] 아래 문자열에서 숫자만 뽑아서 합계를 출력하세요.
# 123 456 789 ==> 1368
# 1
msg = "123,456,789"
print(int(msg[:msg.index(",")]) + int(msg[msg.index(",")+1:msg.rindex(",")])+int(msg[msg.rindex(",")+1:]))

# 2
comma = msg.index(",")
rcomma = msg.rindex(",")
print("msg 숫자의 합 :", int(msg[:comma]) + int(msg[comma+1:rcomma])+int(msg[rcomma+1:]))

# 3 
d_1 = msg[:comma]
d_2 = msg[comma+1:rcomma]
d_3 = msg[rcomma+1:]
print(" ")