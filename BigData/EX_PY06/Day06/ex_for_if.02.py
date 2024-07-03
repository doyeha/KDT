# ------------------------------------------------------------------
# [실습]
## 매사지 입력받기
## 알파벳 대문자인경우 소문소, 소문자인 경우 그문자를 출력

msg = str(input("문자열 입력 : "))


for i in msg:
    if 'a'<= i <= "z":
        print(i.upper(), end="")

    elif 'A' <= i <= "Z":
            print(i.lower(), end="")
print()
print(f"{msg}는 {type(msg)}")
print()


## 2
# print(chr(ord('A')+32))
# print(chr(ord('a')-32))



for i in msg:
    if 'a'<= i <= "z":
        print(chr(ord(i)-32), end="")

    elif 'A' <= i <= "Z":
            print(chr(ord(i)+32), end="")
print()
print(f"{msg}는 {type(msg)}")
print()