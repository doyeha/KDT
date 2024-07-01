# -----------------------------------------------------------------------------
# 문자열 내에 일부 문자열 변경해주는 메서드 => replace()
# -----------------------------------------------------------------------------
# 형식 : 변수명.replace(변경할 문자열, 새로운 문자열, 갯수)

data = "pithon "*5
print(f"data => {data}")
# "i" => "y"로 변경
data1 = data.replace("i","y")
print(f"data1 => {data1}")


# "i" => "y"로 변경
data = "pithon indexing"
data1 = data.replace("i","y")
print(f"data1 => {data1}") ##python yndexyng으로 나옴. 모든 i를 바꾸기 때문,

# "i" => "y"로 변경
data = "pithon indexing"
data1 = data.replace("i","y",1) # 하나만 바꾸라고 해서 
print(f"data1 => {data1}")

data1 = data.replace("ithon", "ython")
print(f"data1 => {data1}")

#[실습] 전화번호 010-2222-3333에서 "-"를 "*"로 변경하세요.
phone = "010-2222-3333"
phone1 = phone.replace("-", "*")
print(f" - 대체 폰 : {phone1}")

#[실습] 전화번호 010-2222-3333에서 "-"를 제거하세요.
phone = "010-2222-3333"
phone1 = phone.replace("-", "")
print(f" - 제거 : {phone1}")

#[실습] 주민번호 231224-4123456 일때, 뒷자리의 첫번째 문자만 그대로 두고 나머지는 *로 변경하세요.
jumin = "231224-4123456"
jumin1 = jumin.replace(jumin[-6:],"*"*len(jumin[-6:]))
print(f" 주민 뒷번호 6자리 변경 : {jumin1}")

# 방법2
jumin = "231224-4111111"
hy_idx = jumin.index("-")
jumin_1 = jumin[:hy_idx]                     #주민번호 앞부분 -
jumin_2 = jumin[hy_idx+1:].replace("1","*")  #주민번호 - 뒷부분
print(jumin_1+"-"+jumin_2)

