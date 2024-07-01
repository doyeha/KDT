# ------------------------------------------------------------
# 문자열 전용의 함수 즉, 메서드 살펴보기 (1)
# ------------------------------------------------------------
phone = "010-1111-2222"

# 문자열에서 특정 문자열의 인덱스 찾기 메서드 ① - index()
# 형식 : 변수명.index("문자열")
# 결과 : 해당 문자열의 시작 인덱스, 없는 경우 Error 발생
#       음수 인덱스는 미지원하고, 왼쪽 즉, 문자열 처음부터 찾아서 제일 먼저 발견되는 요소의 인덱스를 반환한다.
# [실습] 1의 인덱스를 찾기
print(f'1의 인덱스 : {phone.index("1")}')
print(f'-의 인덱스 : {phone.index("-")}')
print(f'1-2의 인덱스 : {phone.index("1-2")}')
# print(f'3의 인덱스 : {phone.index("3")}') # 없는 것 출력 희망, not found 오류 발생.

# 문자열에서 특정 문자열의 인덱스 찾기 메서드 ② - find()
# 형식 : 변수명.find("문자열")
# 결과 : 해당 무낮열의 시작 인덱스, 없는 경우 -1 반환
#        음수 인덱스는 미지원!
#        왼쪽 즉, 문자열 처음부터 찾아서 제일 먼저 발견되는 요소의 인덱스를 반환한다.

#[실습] 1의 인덱스를 찾기
print("1의 인덱스 : ", phone.find("1"))
print("-2의 인덱스 : ", phone.find("-2"))
print("3의 인덱스 : ", phone.find("3"))

# 문자열에서 특정 문자열의 인덱스 찾기 메서드 ③ - rindex(), rfind()
# 형식 : 변수명.rindex("문자열"), 변수명.rfind("문자열")
# 결과 : 문자열 끝에서 찾기 시작 즉, 오른쪽에서 왼쪽으로 들어가면서 찾는다.
#       하지만 0을 포함한 양수 인덱스를 반환
print("phone.rindex('1') : ", phone.rindex('1'))
print("phone.index('1') : ", phone.index('1'))
print("phone.rfind('2') : ", phone.rfind('2'))
print("phone.find('2') : ", phone.find('2'))

#[실습] 전화번호를 "-"제외한 3개로 나누기
# '-' 기준
#phone1 = phone[:phone.find("-")]
#phone2 = phone[phone.find("-")+1 : phone.rfind("-")]
#phone3 = phone[phone.rfind("-")+1:]
#print(phone1, phone2, phone3)
hy1 = phone.find("-")
hy2 = phone.rfind("-")
phone1 = phone[:hy1]
phone2 = phone[hy1+1 : hy2]
phone3 = phone[hy2+1:]

# '숫자' 기준
zero1 = phone.find("0")
zero2 = phone.rfind("0")

one1 = phone.find("1")
one2 = phone.rfind("1")

two1 = phone.find("2")
two2 = phone.rfind("2")

phone1 = phone[zero1:zero2+1]
phone2 = phone[one1:one2+1]
phone3 = phone[two1:]
print(phone1, phone2, phone3)

# 실행 시 >>> 되면 exit() 해서 나가기.