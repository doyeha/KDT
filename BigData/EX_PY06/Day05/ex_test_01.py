# ------------------------------------------------------------------
# [실습1] 글자를 입력받습니다.
#        입력받은 글자의 (a~z, A~Z) 코드값을 출력합니다.
# ------------------------------------------------------------------
x = input("글자 1개 입력 : ")
if len(x)>0:
    if len(x)==1:
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            print(ord(x))
    else:
        print("문자를 하나만 입력해주세요.")
else:
    print("다시 입력해주세요.")

# [Self] 문자를 입력받습니다. 입력받은 문자들의 (a~z, A~Z) 코드값을 출력합니다.
# ------------------------------------------------------------------
x = input("글자 1개 입력 : ")
x = list(x)
print(x, type(x))

for i in range(0,len(x)):
    print(ord(x[i]), end=" ")
print()



# ------------------------------------------------------------------
# [실습2] 점수를 입력 받은 후 학점을 출력합니다.
#        학점 : A+ A A- B+ B B- C+ C C- D+ D D- F
#           100~96 | 95 | 94~90
# ------------------------------------------------------------------
score = int(input("[학점 환산기] 점수를 입력해주세요. : "))

if score < 0 or score > 100:
    print("점수를 다시 입력해주세요.")
elif score >= 90:
    if score >= 96:
        print("A+", end=" ")
    elif score >= 95:
        print("A", end=" ")
    else:
        print("A-", end=" ")
elif score >= 80:
    if score >= 86:
        print("B+", end=" ")
    elif score >= 85:
        print("B", end=" ")
    else:
        print("B-", end=" ")
elif score >= 70:
    if score >= 76:
        print("C+", end=" ")
    elif score >= 75:
        print("C", end=" ")
    else:
        print("C-", end=" ")
elif score >= 60:
    if score >= 66:
        print("D+", end=" ")
    elif score >= 65:
        print("D", end=" ")
    else:
        print("D-", end=" ")
else:
    print("F")
