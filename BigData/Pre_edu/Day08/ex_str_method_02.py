# ------------------------------------------------------------
# 문자열 전용의 함수 즉, 메서드 살펴보기 (2)
# ------------------------------------------------------------
# 문자열 안에서 특정 문자열이 몇 개 존재하는 지 알려주는 메서드
# 메서드명 : count()
# 형식 : 변수명.count("문자열")
# 결과 : 존재하는 개수 즉, 숫자
# 
phone = "010-1111-2222"
print("0의 개수 : ", phone.count("0"))
print("1의 개수 : ", phone.count("1"))

msg = "HAPpy New Year!"
print("A의 개수 : ", msg.count("A"))
print("p의 개수 : ", msg.count("p"))
print("e의 개수 : ", msg.count("e"))
print("z의 개수 : ", msg.count("z"))
print("ea의 개수 : ", msg.count("ea"))

# 문자열에서 좌우 공백 제거 메서드
# 메서드명 : strip()
# 형식 : 변수명.strip("문자열")
# 결과 : 좌,우 즉, 시작 부분과 끝부분 공백 제거한 문자열
msg = "  Happy New Year !! "
msg1 = msg.strip()
print("len(msg) : ", len(msg))
print(msg.strip())
print("len(msg) : ", len(msg1))


# 문자열에서 오른쪽 즉, 끝부분 공백 제거 메서드 // 왼쪽 즉, 시작부분 공백 제거 메서드
# 메서드명 : rstrip()//  lstrip()
# 형식 : 변수명.rstrip("문자열") // 변수명.lstrip("문자열")
# 결과 : 오른쪽 즉, 끝부분 공백 제거한 문자열 // 왼쪽 즉, 끝부분 공백 제거한 문자열
msg = "  Happy New Year !!    "
msg1 = msg.rstrip()
print("len(msg1) : ", len(msg1))
msg2 = msg.lstrip()
print("len(msg2) : ", len(msg2))

# [실습] 숫자를 입력 받은 후 해당 숫자의 거듭제곱을 출력하세요.
num = input("숫자 입력 :")
# 좌우공백 제거
num = num.strip()
# 공백 제거 후 입력된 문자 개수 확인
if len(num)>0:
    # str => int 형변환
    num = int(num)
    #제곱 결과 출력
    print(num**2)






