# 24,29,30장
# ------------------------------------------------------------------
# 24장
# 287P - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# replace
msg = "Helo Python."
msg = msg.replace("l","ll") #복사본 제공. 따로 저장 필수
print(msg)

# translate
table = str.maketrans("aeiou", "12345") # =>  aeiou 12345, 각 인덱스와 대치되는 것을 table이라는 표에 저장해 변경하도록 지정.
print("apple".translate(table))         # => 문자열.번역할게!(이 표로) 형식.
print(msg.translate(table))

# split
fruit = "apple pear grape pineapple orange"
fruit = fruit.split()
print(fruit)

fruit = "apple,pear,grape,pineapple,orange"
fruit = fruit.split(",")
print(fruit)

# join
fruit = "apple pear grape pineapple orange"
print(" ".join(fruit))
# 출력결과 : a p p l e   p e a r   g r a p e   p i n e a p p l e   o r a n g e

fruit = ["apple", "pear", "grape", "pineapple", "orange"]
print("-".join(fruit))
# 출력결과 : apple-pear-grape-pineapple-orange


# 289P - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
msg = "python"
msg = msg.upper()
print(msg)

msg = msg.lower()
print(msg)

msg = " s  g r "
print(msg.lstrip()) # 출력결과 : "s  g r "
print(msg.rstrip()) # 출력결과 : " s  g r"
print(msg.strip())  # 출력결과 : "s  g r"

# 290P 특정 문자열 삭제 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
msg = ", test,"
msg = msg.lstrip(", ")
print(msg) # 출력 결과 : test,

msg = "te,st,"
msg = msg.lstrip(", ")
print(msg)  # 출력 결과 : te,st,

msg = ", test,"
msg = msg.rstrip(",")
print(msg) # 출력 결과 : , test

msg = ", test,"
msg = msg.strip(",")
print(msg) # 출력 결과 : test
 

# 291P 문자열 정렬- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
msg = "Hello World!"
print(msg.ljust(20), len(msg.ljust(20)))    # => "Hello World!       "로 만들어버림.
print(msg.ljust(5), len(msg.ljust(5)))      # => 단, 이미 msg의 길이가 12 이므로 5로 줄여도 msg에 손상은 없다.

print(msg.rjust(20), len(msg.rjust(20)))    # => "        Hello World!"

print(msg.center(20))                       # => "    Hello World!    "

print(msg.upper().center(10))               # 줄줄이 연결 가능. 메서드 체이닝이라고 한다.


# 292P - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("32".zfill(4))    # 4자리 중 문자열을 넣고 남는 공간만큼 앞쪽에 0으로 채워넣는다.


msg = "K-Digital-training"
print(msg.find("k"))    # => 없으면 -1을 반환한다. 대소문자 구분함.
print(msg.find("Digital"))  # 찾을 문자열의 첫 인덱스를 반환. = 2
print(msg.rfind("i"))       # 오른쪽에서부터 찾으니 15

"""
index : 찾는 문자열이 없으면 에러 발생  
find : 찾는 문자열이 없으면 -1 반환

"""

print(msg.count("i")) # 찾는 문자열이 몇개나 들어있는지 반환


# 문자 서식지정
name = "아무개"
age = 18
score = 91
score2 = 80
print("나는 %s이고 %d살." %(name, age)) # %f가 되면 age는 18.0000로 출력
print("평균 점수는 %f" %((score+score2)/2)) # 계산식도 가능

print("%3s" %age) # %s 사이에 3을 넣으면 총 3자리 중 age 값을 넣고 앞쪽에 공백으로 3자리를 채운다.
print("%-5s" %name + "check") # 음수값을 넣으면 오른쪽에 공백 준다.

# 포매팅
print("Hello {}".format("World"))       # {}에 넣을 자리를 만들고 포맷에 넣을 정보를 둔다.
print("{}년 {}월 {}일 ".format(2024, 7,7))
print("{2}년 {1}월 {0}일 ".format(2024, 7,7))       # {}가 여러개 있을 경우 자동으로 0 1 2 순서가 메겨진다. 포맷 속 정보도 그에 따라 자연스럽게 입장 . 따로 지정도 가능.

print("{0} {0} {0}".format(name))   # 그냥 {} {} {} 하면 포맷 속 자료는 하나이므로 0 1 2와 매칭되지 않아 오류. 모두 0으로 지정해줘야 오류 발생 x

print("{y}/{m}/{d}".format(y=2024, m = 7, d = 1))       # 변수로 지정 가능.

print("{}/{}/{:^3}".format(2024,7,8))       # 서식 지정. :^(중앙정렬)3(총3칸)

print("{:^10.3f}".format(1))        # 소수점 : 중앙정렬 총 10칸인데 그 중 float 소수점 자리 3개!

print("{:-^10}".format("2단"))      # 인덱스:빈칸은-로,중앙정렬 총 10칸

# 24.3 퀴즈 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
1. 다음 중 문자열 메서드에 대한 설명으로 잘못된 것을 모두 고르세요.
 a. count는 문자열의 전체 문자 개수를 구한다.
 b. find는 문자열에서 왼쪽부터 문자열을 찾아서 인덱스를 반환한다.
 c. replace는 문자열 안의 문자열을 다른 문자열로 바꾼다.
 d. split은 문자열을 공백 또는 기준 문자열을 기준으로 분리한다.
 e. index는 문자열의 오른쪽에서부터 문자열을 찾아서 인덱스를 반환한다.
    My Answer : a e

    
2. 다음 코드를 실행했을 때 출력 결과를 고르세요.
print('Python'.lower().replace('on', 'ON').ljust(10))
 a. '    Python'
 b. 'python    '
 c. 'PythON    '
 d. 'pythON    '
 e. '    PYTHON'
    My Answer : d


3. 다음 중 문자열 'Hello, Python 3.6'을 만드는 방법으로 올바른 것을 모두 고르세요.
 a. 'Hello, %d 3.6' % 'Python'
 b. '%s, %s 3.6' % ('Hello', 'Python')
 c. ' {0}, Python {1}'.format('Hello')
 d. ' {hello}, {language} 3.6'.format(hello='Hello', language='Python')
 e. '%s%s%s' % ('Hello,', 'Python', '3.6')    
    My Answer : b d

    
4. 다음 중 문자열 '   1675.3000'을 만드는 방법으로 올바른 것을 모두 고르세요. 이 문자열의 길이는 12이고 소수점 이하 자릿수는 4자리입니다.
    또한, 오른쪽으로 정렬되어 있고 남은 공간은 공백으로 채워져 있습니다.
 a '{0:>12.2f}'.format(1675.3)
 b '{0:>12}'.format(1675.3)
 c '{0:>12.4f}'.format(1675.3)
 d '{: >12.4f}'.format(1675.3)
 e '{:0>12.4f}'.format(1675.3)
    My Answer : c d

"""

## 24.4 연습문제 - 출력 결과 python.exe가 되도록, 
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename = path[path.rfind("\\")+1:]
print(filename)
 

# 24.5 심사문제 - 특정 단어 개수 세기, the의 개수를 출력하는 프로그램. them, therem their은 제외.
msg = input().split()
cnt = 0
for m in msg: # the 찾기 반복
    one = False
    two = False
    s = ""
    if m.isalpha(): # 기호 섞여있는지 확인
        # 기호가 없다면?
        if m.find("the") == 0 :
            one = True
        if len(m) == len("the"):
            two = True
    else:
        for i in range(0,len(m)):
            te = m[i]
            gh = m[i].isalpha()     # 기호 색출
            if gh == False:         # 기호가 있으면?
                te="" # 기호 삭제
            s = s + te
        if s.find("the") == 0 :
            one = True
        if len(s) == len("the"):
            two = True

    if one == True and two == True:
        cnt += 1
print(cnt)

# 24.6 심사문제 : 높은 가격 순으로 출력하기 | 가격 여러개 ; 구분으로 한 줄 입력. 입력된 가격을 높은 가격순으로 정렬. 더불어 길이는 9로 맞추고 오른쪽 정렬 및 천단위로 , 넣기
cash = list(map(int,input().split(";")))
cash.sort(reverse=True)
print(cash) # 정렬 완

for cas in cash:
    cas = str(cas)
    if len(cas) < 4: # 3자리면 패스.
        print("".join(cas).rjust(9))

    elif len(cas) < 7: # 4~6자리면 , 하나 입력 해야함.
        one = str(cas[:-3])
        two = "," +str(cas[-3:]) # 3 자리씩 분할.
        cas = (one, two)
        print("".join(cas).rjust(9))

    elif len(cas) < 10: # 4~6자리면 , 하나 입력 해야함.
        one = str(cas[:-6])
        two = "," +str(cas[-6:-3]) # 3 자리씩 분할.
        thr = "," +str(cas[-3:])
        cas = (one,two,thr)
        print("".join(cas).rjust(9))

    else:
        print("범위 밖의 숫자 입니다.")


# 2트
for cas in cash:
    print("{:>9,}".format(cas))


## 29장 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def say():
    print("Hello")
say()

def add(num1, num2):
    print(num1+num2)
add(1,5)

def add_sub(a,b):
    print(a+b, a - b, a // b , a % b)

add_sub(5,1)


def mul(a,b):   # mul이라는 함수 1차 생성
    c = a * b
    return c

def add(a,b):
    c = a+b
    print(c)
    d = mul(a,b)    # mul 끌어다 쓰기. 함수 속 함수 
    print(d)

mul(5,9)
add(1,6)
# 출력 결과 7 6 => add에 a+b와 mul 함수 각각 print 기능 넣어놔서 다 작동


# 29.6 퀴즈
"""
1. 다음 중 매개변수가 없는 hello 함수를 호출하는 방법으로 올바른 것을 고르세요.
 a. def hello
 b. hello
 c. hello()
 d. hello[]
 e. def hello:
    My Answer : c


2. 두 수를 받은 뒤 곱한 결과를 반환하는 함수를 만들려고 합니다. 올바른 코드를 고르세요.
 a. def mul():
        a * b
 b. def mul(a, b):
        a * b
 c. mul(a, b):
        return a * b
 d. def mul(a, b):
        return a * b
 e. mul(a, b):
        return a * b   
    My Answer : d


3. 다음 중 값을 세 개 반환하는 함수를 만들려고 합니다. 올바른 코드를 모두 고르세요.

 a. def three():
        return 1, 2, 3
 b. def three():
        return 1
        return 2
        return 3
 c. def three():
        return (1, 2, 3)
 d. def three():
        return [1, 2, 3]
 e. def three():
        return 1, return 2, return 3
    My Answer : a c d

"""

## 연습문제 : 몫과 나머지를 구하는 함수 만들기
x = 10
y = 3

def get_quotient_remainder(a, b):
    return a//b, a%b
                                                             
quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
# 몫: 3, 나머지: 1

## 심사문제 : 숫자 2개 입력, 덧셈 뺄셈 곱셈 나눗셈 결과 출력. 나눗셈은 실수로 .

a,b = map(int,input().split())
def calc(a,b):
    return f"덧셈 : {a+b}, 뺄셈 : {a-b}, 곱셈 : {a*b}, 나눗셈 : {a/b:>2.1f}"

print(calc(a,b))


## 30장
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
print_numbers(10,20,30)


x = [10,20,30]
print_numbers(*x)
# 원래 def에 변수 3개가 지정되어있기 때문에 리스트 x가 담고 있는 argu도 3개여야 오류가 안뜬다.

print("가변인수")
def print_number(*args):    # 처음부터 보따리 크게 열고 안정해둠.
    for arg in args:
        print(arg, end=" ")
print_number(*x)
print()

def personal(name, age, address):
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    print(f"주소 : {address}")

personal("이름", 20, "대구대구대구")

def d_personal(name="정해진 이름", age=10, address="주소"): # 미입력 시 디폴트 값 출력하도록 설정.
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    print(f"주소 : {address}")

d_personal()


## 딕셔너리 키워드 인수
def personal_dict(name, age, address):
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    print(f"주소 : {address}")

dicdict = {"name" : "김이름", "age" : 20, "address" : "대구대구대구"}

personal_dict(**dicdict)    # ==> def에 지정되어있는 가변인수의 변수명과 딕셔너리 키값이 같아야함.



def personal_info(name, age, address = "비공개"):
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    print(f"주소 : {address}")

personal_info("이름이", 20)
# 초기값이 정해진 함수는 뒤에 몰아넣기.

## 30.5 퀴즈
"""
1. 함수를 def print_numbers(a, b, c):처럼 만들었을 때 이 함수를 호출하는 방법으로 잘못된 것을 고르세요.
 a. print_numbers(1, 3, 5)
 b. print_numbers(a=1, b=2, c=3)
 c. a = [5, 0, 2]
        print_numbers(*a)
 d. a = [3, 7, 9]
        print_numbers(**a)
 e. print_numbers(*[9, 1, 2])
    My Answer : d


2. 다음 중 print_numbers(*[10, 20, 30])으로 호출할 수 있는 함수로 올바른 것을 모두 고르세요.
 a. def print_numbers(args):
 b. def print_numbers(a, b, c):
 c. def print_numbers(*args):
 d. def print_numbers(**kwargs):
 e. def print_numbers():
    My Answer : b c

    
3. 다음 중 personal_info(**{'name': '홍길동', 'age': 30})으로 호출할 수 있는 함수로 올바른 것을 모두 고르세요.
 a. def personal_info(**kwargs):
 b. def personal_info(*args):
 c. def personal_info(name='미공개', age=0):
 d. def personal_info(name, address):
 e. def personal_info(kwargs):
    My Answer : a c


"""

## 30.6 연습문제
korean, english, mathematics, science = 100, 86, 81, 91
 
def get_max_score(*args):
    return max(args)
                                             
max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)
 
max_score = get_max_score(english, science)
print('높은 점수:', max_score)

# 출력 결과 : 높은 점수: 100   |   높은 점수: 91


##30.7 심사문제 | 가장 낮은 점수, 높은 점수, 평균 점수
korean, english, mathematics, science = map(int, input().split())

def min_score(*args):
    return min(args)
    
def max_score(*args):
    return max(args)

def average(*args):
    return sum(args)/len(args)

min = min_score(korean, english, mathematics, science)
max = max_score(korean, english, mathematics, science)
avg = average(korean, english, mathematics, science)


print("낮은 점수 : {0:.2f}, 높은 점수 : {1:.2f}, 평균 점수 : {2:.2f}".format(min, max, avg))