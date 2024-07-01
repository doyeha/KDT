# ------------------------------------------------------------------ 
# Work_02_김도연.py
# Day03 (0628)
# 102 ~ 142p
# ------------------------------------------------------------------ 
# 102P 리스트
li_01 = ['a', 1, 'd', True] #여러 자료형 저장 가능
li_02 = [] # 빈 리스트 생성도 가능

lira = list(range(1,11))  # range를 이용해 1~10까지의 정수로 이루어진 list 생성.

a = range(0,3,1) 
# (시작, 끝+1, 간격) 순으로 생성, (디폴트값 - 시작 : 0 , 간격 : 1)
# 슬라이싱과 마찬가지로 값 생략해도 디폴트값으로 자동 실행된다.
# ex. range(,100) => 0부터 99까지 1의 간격으로 range 생성


t = (1,"한글","정수", 100, True)    # 리스트와 마찬가지로 여러 자료형 저장 가능.
t = (1,)                           # 값 하나도 만들 수 있기는 하지만 튜플이라는 형식을 지정하기 위해서는 ','를 반드시 넣어줘야한다.
#                                  # 그렇지 않으면 그냥 ()는 의미없는 연산자로 보고 단순 문자열 또는 정수로 취급.


# 106p range로 튜플만들기
tuple_range = tuple(range(1,11))
print(tuple_range)   
""" -> 결과 : (1,2,3,4,5,6,7,8,9,10) """

# 107p] 튜플 → 리스트, 리스트 → 튜플 형변환
 # 튜 → 리
tu = (1,2,3,4)
tu = list(tu)
print(type(tu), tu) 

li = ('a','b','c','d')
li = tuple(li)
print(type(li), li)

""" 리스트와 튜블의 차이점!!!!! 리스트는 수정 및 삭제 가능 /// 튜플은 불가능. """

"""
108p] 퀴즈
01. 다음 중 리스트를 만드는 방법으로 올바른 것을 모두 고르세요.
 a. a = []
 b. a = ()
 c. a = [10,20,30]
 d. a = list(range(10,31,10))
 e. a = 10,20,30
  my 답 : a.c.d

02. 다음 중 튜플을 만드는 방법으로 올바른 것을 모두 고르시오.
 a. a = [10,20,30]
 b. a = 10, 20, 30, False, "Hello"
 c. a = (False, "Python")
 d. a = []
 e. a = tuple([10,20,30])
  my 답 : b.c.e

 03. 다음 중 튜플 (-10, -7, -4, -1, 2, 5, 8)을 만드는 방법으로 올바른 것을 고르세요.
 a. a = range(=10, 10, 3)
 b. a = list(range(-10,10,3))
 c. a = tuple(-10, 10, 3)
 d. a = tuple(range(-10, 10, 3))
 e. a = -10, 10, 3
  my 답 : d

"""

# 109P] 연습문제 : range로 리스트만들기
# 리스트 [5,3,1,-1,-3,-5,-7,-9] 출력 // range 사용하여 리스트 생성
a = list(range(5,-10,-2))
print(a)

# 110p] 심사문제 : 정수 입력 받음. range 시작10 / 끝 -10 / 입력 정수 만큼 숫자가 증가하는 튜플 제작 및 출력 
i = int(input())
i_tuple = tuple(range(-10,11,i))
print(i_tuple)



# 112p] 시퀀스객체 - 값 in
a = [1,2,33,4,5,45,6,7,778]
print(i in a); print(50 in a); print(1 in a)
print(i in (1,2,3,4,5,6))


# 113p] 시퀀스 객체 연결
# 01. + 덧셈.
a = (1,2,3)
b = ("a","b","c")
print(a+b)
""" 출력 결과 : (1,2,3,'a''b','c') """ 
 # str + str처럼 연결이 된다.
 # 단!!!! range는 + 연산자로 연결할 수 없다.

# 02. * 곱셈
print(a*3, type(a*3))
""" 출력 결과 : (1,2,3,1,2,3,1,2,3) <class 'tuple'> """
 # 튜플을 곱하기 햇는데 그대로 클래스 튜플 형식이 유지되고 튜플이 곱한만큼 반복된다.


# 115p] 시퀀스 객체의 요소 개수 구하기.
print("\n구분선 - 115페이지, 시퀀스 객체 개수 구하기")
print("len(a)",len(a), end="\t") ; print("len('카페인급구')",len("카페인급구"), end="\t")
print("len(tu)",len(tu), end="\t"); print("len(range(3,40,4))",len(range(3,40,4)), end="\t")
# 각각 리스트, 리스트, 튜플, range

"""
 시퀀스 객체에서는 str list tuple range가 있다
 ☆ 그럼 다른 형식에서는 len 을 쓸수없나?
"""


# 118p] 인덱스 사용하기
"""
            a = ("A",   "B",    "C",    "D") 라는 튜플이 있다면.
인덱스 순서        0      1       2       3
                 -4     -3      -2      -1      ** 양수는 0부터 시작하고, 음수는 오른쪽에서부터 -1로 시작.
"""

a = [11,22,33,44,55]
print(a[0], a[1], a[-1])

nt = (11,22,33,44,55)
print(nt[1], nt[4], nt[3])  

""" 만약 없는 인덱스 사용(범위 벗어날) 시 Error 발생! 추가 희망 시 메서드 사용 필요. 단, 리스트에만 해당한다. 튜플은 수정 불가능 """

print(a[1:])   #슬라이싱 사용 시 맨 마지막 요소는 -1을 입력해도 [-1]요소가 제외되기 때문에 -1을 생략해 마지막까지 나오도록 해주면 된다.




# 123p] 요소 값 할당 (수정하기)
""" 튜플, range, 문자열은 진행하면 Error 발생 !!!! """
a = [0,0,0,0,0]
print(f"\n123페이지 값 할당 !]\n{a}")
a[0] = 1
a[2] = "집"
a[-1] = True
print(f"{a}")
#124p] 요소 값 삭제하기.
""" del 명령어 """
del a[-1]
print(f"a[-1] 삭제 시 ? : {a}")
 # del a[-1] or del(a[-1]) 둘 중에 한 형식 사용 하면 된다. 메서드가 아니라 "명령어"

# 123p] 슬라이스 사용하기. 이미 앞부분 햇으니 설명 생략.
a = [11,22,33,44,55,66,77]
print(a[:50])   
""" 출력 결과 : [11,22,33,44] """
 # ==> 슬라이스는 범위 벗어나 사용해도 지정한 범위 내에 존재하는 것만 출력
print(a[1:50:3])
""" 출력 결과 : [22,55] """
# ==> range와 마찬가지로 간격 지정 가능

# datas = [1,2,3,4,5,6]
# datas[::1]=[100]   # ==> datas[::2]이라면, 연속된것이 아닌 상태에서 100으로 변경하겟다고 하는거라 에러 발생.
# print(datas)




# 131p] len 응용하기
a = [11,22,33,44,55,66]
print(a[3:len(a)+1])
""" 출력 결과 : [44,55,66] """
 # 슬라이싱 안에서 정수가 아닌 len을 활용해 인덱스 지정 가능.
b = (1,2,3,4,5,6,7,8,9,10)
print(b[1:len(b)-2])
c = range(1,101,2)
print(list(c[:len(c):int(len(c)/i)]))


# 135p] 슬라이스에 요소 할당하기.
a = [10,20,30,50,60,80]
a[1:5] = ["a", "b"]
print(a)
""" 출력 결과 : [10,'a', 'b', 80] """
 # 1:5 잡으면서 총 4개의 요소를 슬라이스로 묶고 리스트의 요소가 2개인 것으로 치환, 개수 안맞아도 괜찮음.

a = [10,80]
a[1:] = ["a", "b", "c", 1,2,3]
print(a)
""" 출력 결과 : [10,'a', 'b', 'c', 1, 2, 3] """
 # 1:5 잡으면서 총 4개의 요소를 슬라이스로 묶고 리스트의 요소가 2개인 것으로 치환, 개수 안맞아도 괜찮음.

# 138p] del 슬라이스 삭제하기.
a = [10,20,30,40,50,1,2,3,4,5,6,6,1,2,3,5]
print(f"\n138페이지\n{a}")
del a[::4]
print(a)


"""
139p] 퀴즈
1. 다음 중 시퀀스 자료형에 대한 설명으로 잘못된 것을 모두 고르시오.
 a. in 연산자는 시퀀스 객체 안에 특정 값이 없는 지 확인한다.
 b. range는 * 연산자로 반복할 수 없다.
 c. 문자열 str은 시퀀스 자료형이다.
 d. + 연산자로 두 시퀀스 객체를 연결하면 첫 번째 객체 안에 두번째 객체가 들어간다.
 e. len 함수는 시퀀스 객체에 들어잇는 요소 개수를 구한다.
  my 답 : a d 

2. 리스트 a = [10, 20, 30, 40, 50, 60]에서 인덱스 요소를 가져왔을 때 값이 올바르지 않을 것을 모두 고르세요.
 a. a[0]은 10
 b. a[1]은 10
 c. a[3]은 40
 d. a[-1]은 50
 e. a[-1]은 60
 my 답 : b d 
 
3. 튜플 a = (11,22,33,44,55,66,77,88,99)에서 (11,55,99)을 가져오는 방법으로 올바른 것을 모두 고르세요.
  a. a[0:9]
  b. a[0:9:3]
  c. a[::4]
  d. a[0:6:2]
  e. a[0:len(a):4]
   my 답 : c e

4. 다음 중 시퀀스 자료형의 슬라이스에 대한 설명으로 잘못된 것을 모두 고르세요.
 a. 시퀀스 객체에 슬라이스로 범위를 지정하여 요소에 값을 할당하면 새 객체가 생성된다.
 b. 문자열은 슬라이스를 사용하여 일부를 가져올 수 있다.
 c. 튜플은 슬라이스를 사용하여 일부를 가져올 수 없다.
 d. range 객체는 슬라이스로 범위를 지정하여 요소를 할당할 수 없다.
 e. 시퀀스 객체에 인덱스 증가폭을 지정하여 요소를 할당할 때는 슬라이스 범위의 요소 개수와 할당할 요소 개수가 정확히 일치해야 한다.
  my 답 : a c  
 
   """


# 140p] 연습문제 : 최근 3년간 인구 출력
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 1019538, 10143645, 10103233, 10022181, 993066, 9857426, 9838892]
print(year[-3:])
print(population[-3:])


# 141p] 11.7 연습문제 : 인덱스가 홀수인 요소 출력하기.
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

# 141p] 11.8 심사문제 : 리스트의 마지막 부분 삭제하기.
x = input().split()
del x[-5:]
x = tuple(x)
print(x)

# 142p] 11.9 심사문제
# 입력 각 2줄 받고, 첫번째는 홀수 / 두번째는 짝수 인덱스 연겨래서 출력하는 프로그램 
i1 = input()
i2 = input()

print(i1[0::2]+i2[1::2])
