# -------------------------------------------------------   
# 제어문 -  for 반복문
# - 용도 : 순서(Sequence)가 있는 데이터에서 원소/요소
#          차례대로 읽을 때 사용 (예 : str, list)
# - 형식 : for 요소 담을 변수명 in 시퀀스객체:
#              코드
# -------------------------------------------------------
msg = "Good Luck!"

#요소 / 원소 하나씩 읽기 // 아래 방식은 매우 비효율 !!!!
# print(msg[0])
# print(msg[1])
# print(msg[2])
# print(msg[3])
# print(msg[4])
# print(msg[5])
# print(msg[6])
# print(msg[7])
# print(msg[8])
# print(msg[9])

# ==> 요소/원소 순서대로 읽어주는 제어문 즉, 반복문
#  m=msg[0], m=msg[1],m=msg[2],  --- m=msg[9] 
for m in msg:   # msg에 담겨있는 것을 m에 넣는 것.
    print(m)
    #msg가 소유중인 요소 수 만큼 반복.

for m in msg:
    print(f"{m} - {ord(m)}")



# 문자열 msg를 2진수 코드값으로 변환해서 출력하기.
print(msg)
for i in msg:
    print(bin(ord(i)), end=" - ")

for m in msg:
    print(bin(ord(m)) [2:], end=" ")


#문자열을 모두 대문자로 변경하기 ==> upper() 사용x
# a = 97, A = 65 -32 => 65 
# b = 98, B = 66 -32 => 66
#1
msg = "good luck"
for m in msg:
    print(chr(ord(m) - 32))
#2
msg = "good luck"
for m in msg:
    if m >= 'a' and m <= 'z':
        print( chr (ord(m))-32, end=" ")
    else:
        print(m, end="")

# 숫자 문자열 원소/요소 다루기
numbers = "123456789"
total = 0
for num in numbers:
    # print(f"total = {total} : num => {num}") #이전 확인용
    total = total + int(num)
    print(f"total = {total} : num => {num}")



