# ------------------------------------------------------------
# 멤버 연산자 in, not in
# - 형식 : 왼 in 오른쪽
#          왼쪽에 있는 문자열이 오른쪽 문자열 내에 존재 여부
# - 결과 : True, False
# ex) 1 in 123 : True     or      1 not in 123456 : False
# ------------------------------------------------------------
msg = "오늘은 금요일 좋은 날"

print(f"'금' in '{msg}' : {'금' in msg}")
print(f"'금' not in '{msg}' : {'금' not in msg}")

#[실습] '1234567890' 안에 '789'존재 여부
print(f'{"789" in "0123456789"}')
data = "0123456789"
print(f"'789' in '{data}' : {'789' in '0123456789'}")
print(f"'789' in '{data}' : {str(789) in '0123456789'}")