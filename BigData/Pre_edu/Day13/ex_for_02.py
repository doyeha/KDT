# ------------------------------------------------------- 
# 제어문 - for 반복문과 list
# - 리스트 컨프리헨션 문법 : 메모리 적게 사용, 성능 빠름
# -------------------------------------------------------
# 리스트 1번에서 새로운 리스트 2번 생성 
num1 = [1,2,3,4,5]

# 원소 중 짝수 값이 원소는 제곱을 하고 나머지 값은 그대로 가지고 가는 새로운 리스트 생성 
num2=[]

# 리스트에 원소 추가 ==> 리스트 전용 함수 즉, 메서드
# append() 메서드
num2.append(10)
print(num2)

num2.append(11)
num2.append(12)
num2.append(13)
print(num2)


#clear() 메서드 : 메서드 안에 모든 원소 제거 후 빈 리스트로 만듬
num2.clear()
print(num2)

## num1의 원소를 num2에 넣기
num2.append(num1[0])
num2.append(num1[1])
num2.append(num1[2])
num2.append(num1[3])
num2.append(num1[4])

for n in num1:
    num2.append(n)

for n in num1:
    if n%2:
        num2.append(n)
    else:
        num2.append(n**2)
print()