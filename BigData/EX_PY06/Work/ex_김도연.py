# 240627 101p 까지.
# 논리연산 bool 타입은 x

# 저장방식
# 1, 1개 명령어 실행 모드
#2  명령어 파일에 저장. py (스크립트 모드)

# 35p
print("Hello, world!")

# 49p
print("Hello, world!")
print("Python Programming")

print("Hello, world!")
print("Hello, world!")

# 50p
print("Hello"); print("test")

# 52p
a=10
if a == 10:
    print('10입니다.')


# 62p
ap = input("현재 AP 수치는?")
ap = int(ap)
cal = (ap * 0.6) + 225
print(f"현재 AP는 {ap}이므로, 왜곡 스킬의 피해량은 {int(cal)}입니다.")

# 65
x,y,z = 10,20,30
a = b = c = 12
print( x, y, z, a,b,c )

#68
a=input("입력")
print(a, type(a))



a = input("합 구하기, 첫 번쨰 숫자")
b = input("합 구하기, 두 번쨰 숫자")
print(f"{a}+{b} = {a+b}")

a = int(input("합 구하기, 첫 번쨰 숫자"))
b = int(input("합 구하기, 두 번쨰 숫자"))
print(f"{a}+{b} = {a+b}")


#71 split
a, b, c = input("3개의 숫자를 입력 : ").split()
print(a,b,c)

a = int(a)  #얘는 한꺼번에 3개 불가능.
print(f"{type(a)} {type(b)} {type(c)}")

# 72, map(목표형, input(절))) 
a,b = map(int, input("숫자 2개 입력").split())
print(f"type(a) : {type(a)}, type(b) : {type(b)}")

a,b = map(float, input("숫자 2개 입력").split())
print(f"{a} : {type(a)}, {b} : {type(b)}")


# 75p 정수 세 개 입력받고 합산.
a,b,c = map(int, input("세 개 정수 입력. ex. 14 3 4 : ").split())
print(a+b+c)

a = 50
b = 100
c = None
print(a)
print(b)
print(c)

rnr = int(input())
dud = int(input())
tn = int(input())
rhk = int(input())
print(int((rnr+dud+tn+rhk)/4))


#77
print(1, 2, 3, sep=", ")
print(1,2,3, sep="  |")
print(2000,500, sep="x")

#79
print(1,2,3, sep="\n")
print(1, end="")
print(3, end = " - ")

#80
year = 2000
month = 10
day = 27
hour = 11
minute = 3
second = 59

print(year, month, day, sep="/")
print(hour,minute,second, sep=":")

#81
y,m,d,h,m,s = map(int,input("년 월 일 시 분 초를 입력해주세요. ex) 2000 01 01 11 24 45").split())
print(y,m,d, sep="-", end="T")
print(h,m,s, sep=":")


#91
a = not True and True
b = True or False
c = True or False or True
d = True and False or True
print(a,b,c) 

#95
rnr = int(input())
dud = int(input())
tn = int(input())
rhk = int(input())
print(rnr>=90 and dud > 80 and tn > 85 and rhk >=80)

#96
hel = "hello"
print(hel)

#99
print("Hello \nworld")
print("Hello \\ world")
print('isn\'t')

a = """과
제
중
99
페
이
지"""
print(a)

#100
s = "Python is a programming language that lets you work quickly \n and \n intergrate systems more effectively"
d = """Python is a programming language that lets you work quickly
and 
intergrate systems more effectively"""
print(s)
print(d)