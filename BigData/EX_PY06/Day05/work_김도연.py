# ------------------------------------------------------------------ 
# 0702, Day05
# 16장 
# ------------------------------------------------------------------
## 187P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
for i in range(1,10):
    print(f"Hello, name...World-{i}?")

lis = []
m = 0
for i in range(0,10):
    lis.append(i)

print(lis)

## 188P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
for i in range(1,20,3):
    print(f"{i}번")

for i in range(100,0,-1):
    print(f"{i}", end=" ")
print()


## 191P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
a = [10,20,30,40,50]
for i in a:
    print(a, end="!")
print()


## 192P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
for letter in reversed("Python"):
    print(letter, end=" ")
print()

"""
16.4 퀴즈
1. 다음 중 for로 10번 반복하는 방법으로 올바른 것을 모두 고르세요.
 a. for i in range(10): 10
 b. for i in range(5,16): 11
 c. for i in range(10, 0): x
 d. for i in range(20, 40, 2): d
 e. for i in range(1,10,1):
    My Answer : a d

2. 다음 중 20부터 10까지 출력하는 방법으로 올바른 것을 모두 고르세요.
 a. for i in range(20,10):
    print(i)
 b. for i in range(20,10,1):
    print(i)
 c. for i in range(20,9,-1):
    print(i)
 d. for i in reversed(range(10,21)):
    print(i)
 e. for i in reversed(range(10,20)):
    print(i)
    My Answer : c d

3. 다음 소스 코드에서 잘못된 부분을 모두 고르세요.
 a. count = input()
 b. 
 c. for i in range(count)
 d.     print("i의 값은',end=" ")
 e.     print(i)
    My Answer : a c 


4. 다음 for 반복문을 실행했을 때의 출력 결과를 고르세요.
 [for i in reversed("Python"):
    print(i, end=".")]
 a. Python
 b. P y t h o n
 c. n o h t y p
 d. n.o.h.t.y.P
 e. nothyp
    My Answer : d
"""


## 193P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 16.5 연습문제 
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(f"{i*10}", end=" ")
print()
# 16.6 심사 문제
# 표준 정수 입력, 구구단 출력  > 숫자 * 숫자 = 숫자 < 형식
gugu = int(input())

for i in range(1,10):
    print(gugu,"*", i, "= {:02}".format(gugu*i))
