# ------------------------------------------------------- 
# 제어문 -  for 반복문
# - 용도 : 순서(Sequence)가 있는 데이터에서 원소/요소
#          차례대로 읽을 때 사용 (예 : str, list)
# - 형식 : for 요소 담을 변수명 in 시퀀스객체:
# ------------------------------------------------------- 
#[실습] 아래 문자열에서 대문자만 코드로 변경하고 나머지 문자는 그대로 출력하세요.
data = "Happy New Year!!"

for d in data:
    if d >= 'A' and 'Z' >= d:
        print(ord(d), end="")
    else:
        print(d, end="")


# T
cnt=0   
for d in data:
    if d>='A' and d <= 'Z':
        print(ord(d), end=" ") #if cnt != len(data)-1 else "\n")
    else:
        print(d, end="") #if cnt != len(data)-1 else "\n")
print()        

# T2 메서드 사용
for d in data:
    if d.isupper():
        print(ord(d), end="")
    else:
        print(ord(d), end="")
print()

for d in data:
    if cnt!=len(data)-1:
        print(d, end="")
    else:
        print(d, end="\n")
    cnt=cnt+1

# ???
cnt = 0
for d in data:
    print(d, cnt, end=" " if cnt != len(data)-1 else "\n")
    cnt = cnt + 1
print("-------------------------")


