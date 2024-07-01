# -----------------------------------------------------------------------------
# 문자열 구성하는 문자 검사 메서드 => 변수명.isOOO()
# -----------------------------------------------------------------------------
# 문자열 내에 숫자 존재여부 체크 메서드들 3종류
# - 변수명.isnumeric() : 0~9까지의 숫자, 5¹, 5₁, ①, ➊, ⅒, Ⅳ, ⅳ, 百
# - 변수명.isdigit()    : 0~9까지의 숫자, 5¹, 5₁, ①, ➊ 
# - 변수명.isdecimal()  : 0~9까지의 숫자
#    ==> 실수, 음수, 나머지 : False
# - isdecimal() < isdigit() < isnumeric()
# -----------------------------------------------------------------------------
data = "123"
print(f"\n[{data}]-----------")
print(f"data.isnumeric() : {data.isnumeric()}")
print(f"data.isdigit() : {data.isdigit()}")
print(f"data.isdecimal() : {data.isdecimal()}")

data1 = "123."
print(f"\n[{data1}]-----------")
print(f"data.isnumeric() : {data1.isnumeric()}")
print(f"data.isdigit() : {data1.isdigit()}")
print(f"data.isdecimal() : {data1.isdecimal()}")

data2 = "-123"
print(f"\n[{data2}]-----------")
print(f"data.isnumeric() : {data2.isnumeric()}")
print(f"data.isdigit() : {data2.isdigit()}")
print(f"data.isdecimal() : {data2.isdecimal()}")

data3 = "5¹"
print(f"\n[{data3}]-----------")
print(f"data.isnumeric() : {data3.isnumeric()}")
print(f"data.isdigit() : {data3.isdigit()}")
print(f"data.isdecimal() : {data3.isdecimal()}")


data = "①"
print(f"\n[{data}]-----------")
print(f"data.isnumeric() : {data.isnumeric()}")
print(f"data.isdigit() : {data.isdigit()}")
print(f"data.isdecimal() : {data.isdecimal()}")

data = "Happy 2025"
print(f"\n[{data}]-----------")
print(f"data.isalpha() : {data.isalpha()}")
print(f"data.isalnum() : {data.isalnum()}")
print(f"data.isnumeric() : {data.isnumeric()}")

