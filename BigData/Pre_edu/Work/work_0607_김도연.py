# # ---------------------------------------------------------
# # PYTHON EXAM 조건문과 리스트
# # 제출 :  work_0607_이름.py   #Day11
# # ---------------------------------------------------------
# 1. 실수를 입력 받은 후 소수점 이하 자리 반올림하여 정수로 출력해주세요.
# [ 입력 ]  실수 (소수점이하 1자리까지) : 12.4
# [ 출력 ]  정수 12
# [ 입력 ]  실수 (소수점이하 1자리까지) : 12.5
# [ 출력 ]  정수 13
print("[1번]")
data = input("실수 (소수점이하 1자리까지) : ")
data = float(data)
print("%d" %(data))
data = input("실수 (소수점이하 1자리까지) : ")
data = float(data)
print("%d" %(data))
print("")


# 2. 데이터를 입력 받아 데이터에 따른 패턴 문자를 설정합니다.
# - 알파벳 => ★
# - 숫  자 => ♠
# [ 입력 ] 알파벳 또는 숫자 입력 : 1
# [ 출력 ]
#   ♠♠   ♠♠ 
#  ♠♠♠♠ ♠♠♠♠
# ♠♠♠♠♠♠♠♠♠♠♠
#  ♠♠♠♠♠♠♠♠♠
#   ♠♠♠♠♠♠♠
#     ♠♠♠
#      ♠
print("[2번]")
data = input("알파벳 또는 숫자 입력  : ")
if data.isalpha():
    data = "★"
    print("{:>4}".format(data*2), "{:>5}".format(data*2))
    print("{:>5}".format(data*4), "{:>5}".format(data*4))
    print("{:^11}".format(data*11))
    print("{:^11}".format(data*9))
    print("{:^11}".format(data*7))
    print("{:^11}".format(data*3))
    print("{:^11}".format(data*1))

elif data.isnumeric():
    data = "♠"
    print("{:>4}".format(data*2), "{:>5}".format(data*2))
    print("{:>5}".format(data*4), "{:>5}".format(data*4))
    print("{:^11}".format(data*11))
    print("{:^11}".format(data*9))
    print("{:^11}".format(data*7))
    print("{:^11}".format(data*3))
    print("{:^11}".format(data*1))
else:
    print("오류 발생!")

print()

# 3. 나이를 입력 받은 후 연령대를 출력하는 코드 작성하세요.
# ------------------------------------------------------------
# - 영유아 ( 0세 ~  5세)
# - 아동   ( 6세 ~ 12세)
# - 청소년 (13세 ~ 18세)
# - 청년   (19세 ~ 29세)
# - 중년   (30세 ~ 49세)
# - 장년   (50세 ~ 64세)
# - 노년   (65세 ~ )
# ------------------------------------------------------------
# [ 입력 ]  나이 :  31
# [ 출력 ]  당신은 '중년층'입니다.
print("[3번]")
age = input("나이를 입력해주세요 : ")
if age.isnumeric():
    if int(age)<6:
        print("당신은 '영유아'입니다.")
    elif int(age)<13:
        print("당신은 '아동'입니다.")
    elif int(age)<30:
        print("당신은 '청년'입니다.")
    elif int(age)<50:
        print("당신은 '중년'입니다.")
    elif int(age)<65:
        print("당신은 '장년층'입니다.")
    else:
        print("당신은 '노년층'입니다.")
else:
    print("잘못 입력하셨습니다.")
print("\n")
# 4. 금액과 통화명을 입력 받은 후 원화로 환전한 금액을 출력하세요.
# ------------------
# 통화명|  환율
# ------------------
# 달러	|  1167
# 엔	|  1.096
# 유로	|  1268
# 위안	|   171
# ------------------
# [ 입력 ]  금액 및 통화명 :  100 달러
# [ 출력 ]  환전      금액 :  116700.00 원
print("[4번]")
money = input("금액 및 통화명 (ex.100 달러, 10 엔) : ")
money = (money.strip()).split()   # [100, 달러]
print(money)
if len(money) <2:
    print("예시와 같이 입력해주세요.") # 스페이스바 미입력 시 오류 발생 방지
elif money[0].isnumeric:
    cash = money[0]
    cash = int(cash)
    won = money[1]
    if won.isalpha():
        if won == "달러":
            print(f"환전 금액 : {cash*1167}원")
        elif won == "엔":
            print(f"환전 금액 : {cash*1.096}원")
        elif won == "유로":
            print(f"환전 금액 : {cash*1268}원")
        elif won == "위안":
            print(f"환전 금액 : {cash*171}원")
    else:
        ("잘못 입력하셨습니다.")


# 5. 전화번호를 입력 받고 통신사 정보를 출력하세요.
# ---------------
# 번호	통신사
# ---------------
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# --------------

# [ 입력 ]  전화번호 :  016-222-1234
# [ 출력 ]  통 신 사 :  KT
print("[5번]")
phone = input("전화번호를 입력해주세요. (ex.010-1234-1234) : ")
phone = (phone.strip()).split("-")
tong = phone[0]
if len(tong) > 3:
    print("잘못 입력하셨습니다.")
elif tong.isnumeric():
    if tong == "011":
        print(f" 통신사 : SKT")
    elif tong == "016":
        print(f" 통신사 : KT")
    elif tong == "019":
        print(f" 통신사 : KT")
    elif tong == "010":
        print(f"알수없음.")
else:
    print("잘못 입력하셨습니다.")
print()

# 6 .우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타냅니다.
#    예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작합니다.
# --------------------------------------------------------------------------------
# -	    0	      1	     2	     3	    4	   5	   6	  7	      8	     9
# --------------------------------------------------------------------------------
# 01  강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# ---------------------------------------------------------------------------------
# 5자리 우편번호를 입력받고 구를 판별하여 주세요.
# [ 입력 ]  우편번호 :    01500
# [ 출력 ]  지    역 :   도봉구
print("[6번]")
adr = input("우편번호 5자리를 입력해주세요 : ")
gu = int(adr[2])
if gu == 0 or gu == 1 or gu == 2:
    print(f"지  역: 강북구")
elif gu == 3 or gu == 4 or gu == 5:
    print(f"지  역: 도봉구")
elif gu == 6 or gu == 7 or  gu == 8 or gu == 9:
    print(f"지  역: 노원구")
else:
    ("우편번호를 다시 확인해주세요.")

print("[6번]")
adr = input("우편번호 5자리를 입력해주세요 : ")
gu = int(adr[2])
if gu in [1,2,3]:
    print(f"지  역: 강북구")
elif gu in [4,5,6]:
    print(f"지  역: 도봉구")
elif gu in [6, 7, 8, 9]:
    print(f"지  역: 노원구")
else:
    ("우편번호를 다시 확인해주세요.")

# 7. 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 
#    1, 3은 남자, 2, 4는 여자를 의미합니다.
#    사용자로부터 13자리의 주민등록번호를 입력 받은 후 
#    성별 (남자, 여자)를 출력하는 프로그램을 작성하세요.
# [ 입력 ]  주민 번호 :  990103-1079700
# [ 출력 ]  성     별 :  남자
#           나    이 :   25세
print("[5번]")
jumin = input("주민번호를 입력해주세요 ex)990103-1079700 :")
jumin = jumin.split("-")
year = jumin[0][:2] # 99
gender = jumin[1][:1] # 1

if gender == "1":
    age="19" + year
    age = 2024 - int(age)
    gender = "남성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
elif gender == "2":
    age="19"+str(year)
    age = 2024 - int(age)
    gender = "여성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
elif gender == "3":
    age="20"+str(year)
    age = 2024 - int(age)
    gender = "남성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
elif gender == "4":
    age="20"+str(year)
    age = 2024 - int(age)
    gender = "여성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
else:
    ("주민번호를 다시 입력해주세요.")
print()


# 8. 데이터 10, 5, 21, 9, 100, 5, 9를 하나의 변수에 저장 후 출력해 주세요.
data = [10, 5, 21, 9, 100, 5, 9]
print(data)

# 9. 개인정보 이름, 주민번호, 전화번호를 하나의 변수에 저장 후 출력해 주세요.
human = ["이름", "123456-1234567", "010-1234-4567"]
print(human)
# 10. 8번에서 저장한 데이터의 원소들의 값을 모두 더한 합계를 출력해 주세요.
sum = data[0] + data[1] + data[2] + data[3] +data[4] + data[5] + data[6]
print(sum)