# ------------------------------------------------------------------
# List / Dictionary / Set 자료형과 반복문, 조건부 표현식 결합
# - 메모리 사용량 감소 & 속도 빠름
# ------------------------------------------------------------------
keys = ['a','b','c','d']

x = {key : value for key, value in dict.fromkeys(keys).items() }
x = {key : value for key, value in [("age",12), ("name","흥")]}
# keys로 새로운 딕셔너리 만드는 

print(x)