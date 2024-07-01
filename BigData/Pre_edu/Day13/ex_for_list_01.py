# ------------------------------------------------------- 
# 제어문 - for 반복문과 list
# - 리스트 컨프리헨션 문법 : 메모리 적게 사용, 성능 빠름
# -------------------------------------------------------
num1 = [1, 2, 3, 4, 5]

# [새로운 리스트 생성] 짝수값만 새로운 리스트에 담기
num2=[]
for n in num1:
    if not n%2:
        num2.append(n)
num3 = [ n for n in num1 if not n%2 ]
# 1. for n in num1
# 2. if not n%2
# 3. n

print(f"num2 ==> {num2}")
print(f"num3 => {num3}")



# [새로운 리스트 생성] 홀수 값은 그대로, 짝수값은 제곱해서 추가하기
num4 = []
for n in num1:
    if not n%2:
        num4.append(n)
    else:
        num4.append(n**2)

num5 = [ n**2 if not n%2 else n for n in num1 ]
# 1. for n in num1
# 2. if not n%2 else n