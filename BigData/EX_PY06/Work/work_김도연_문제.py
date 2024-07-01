# ------------------------------------------------------------------ 
# 0628(금) 주말 과제, 문제은행 80문제까지.
# 문제 은행 링크 : https://wikidocs.net/7021
# ------------------------------------------------------------------ 
#001. 화면에 Hello World 문자열 출력
print("001번")
print("Hello World")

#002. 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("\n002번")
print("Mary\'s cosmetics")

#003 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
#신씨가 소리질렀다. "도둑이야".
print("\n003번")
print("신씨가 소리질렀다. \"도둑이야\".")

#004 화면에 C:\Windows를 출력하세요.
print("\n004번")
print("C:\\Windows")

#005 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("\n005번")
print("안녕하세요.\n만나서\t\t반갑습니다.")
"""
\t : 탭 기능. 문자열 사이에 탭, "     " 공백  
\n : 엔터 기능.
"""

#006 print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print("\n006번")
print ("오늘은", "일요일")
""" 출력 결과 : 오늘은 일요일   -> +는 띄워쓰기 없이 2개의 문자열 출력, ,는 띄워쓰기 후 2번째 문자열 출력. """

#007print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print("\n007번")
print("naver;kakao;sk;samsung")


#008 print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
print("\n8번")
print("naver/kakao/sk/samsung")


#009 다음 코드를 수정하여 줄바꿈이 없이 출력하세요.
# (힌트: end='') print 함수는 두 번 사용합니다.
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("\n9번")
print("first", end=" "); print("second")


#010 5/3의 결과를 화면에 출력하세요.
print("\n10번")
print(5/3)


#011 삼성전자라는 변수로 50,000원을 바인딩해보세요.
# 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
print("\n11번")
samsung = 50_000
print(f"삼성전자 10주의 총 평가금액 : {samsung*10}")


#012 다음 표는 삼성전자의 일부 투자정보입니다.
# 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
#    항목	    값
#  시가총액	   298조
#   현재가	  50,000원
#    PER	  15.79
print("12번")
시가총액 = "298조"
현재가 = "50,000원"
PER = 15.79


#013 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
#  두 변수를 이용하여 아래와 같이 출력해보세요.
#  실행 예:
#  hello! python
print("13번")
s = "hello"
t = "python"
print(f"{s}! {t}")


#014 아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3 
print("14번")
print(f"2 + 2 * 3 = {2 + 2 * 3}")


#015 type() 함수는 데이터 타입을 판별합니다.
# 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# a = 128
# print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
a = "132"
print("\n15번")
print(f"a = {type(a)}")


#016 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
print("\n16번")
print(f"num_str : {type(num_str)}")
num_str = int (num_str)
print(f"num_str : {type(num_str)}")


#017 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
print("\n17번")
print(f"num : {type(num)}")
num = str (num)
print(f"num : {type(num)}")


#018 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
print("\n18번")
s = "15.79"
print(f"15.79 : {type(s)}")
s = float(s)
print(f"{s} : {type(s)}")


#019 year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다.
# 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
print("\n19번")
year = "2020"
year = int(year)
print(year, year-1, year-2)


# 020 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
print("\n20번")
air_m = 48584
eza = 36
print(f"에어컨 월 {air_m}원 {eza}개월, 총 {air_m * eza}원! 와 개비싸")


# 021 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
#실행 예 : p t
print("\n21번")
print(letters[0], letters[2])


# 022 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
# 실행 예: 2210
print("\n22번")
print(license_plate[-4:])


# 023 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
# 실행 예 : 홀홀홀
print("\n23번")
print(string[::2])

# 024 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
# 실행 예:
# NOHTYP
print("\n24번")
for i in range(1,len(string)+1) :
    print(string[-1*i], end="")
print("\n24번-1")
print(string[::-1])
print("\n24번-2")
print(string[5], end="")
print(string[4], end="")
print(string[3], end="")
print(string[2], end="")
print(string[1], end="")
print(string[0], end="")


# 025 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
# 실행 예 : 010 1111 2222
print("\n25번")
print(phone_number.replace("-"," "))


# 026 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예
# 01011112222
print("\n26번")
print(phone_number.replace("-",""))


# 027 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
# 실행 예: kr
print("\n27번")
print(url[-2:])


# 028 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang)
print("\n28번")
""" 출력 결과 : 오류 발생, 문자열과 튜플은 수정 및 부분 삭제 불가능. """


# 029 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A
print("\n29번")
print(string.replace("a","A"))


# 030 아래 코드의 실행 결과를 예상해보세요.
# string = 'abcd'
# string.replace('b', 'B')
# print(string)
print("\n30번")
""" 출력 결과 : abcd, replace한 string을 따로 저장안해줌. abcd 그대로이다. """


# 031 아래 코드의 실행 결과를 예상해보세요.
# a = "3"
# b = "4"
# print(a + b)
print("\n31번")
""" 출력 결과 : 34  -> 문자열이므로 그냥 옆에 갖다붙임"""


# 032 아래 코드의 실행 결과를 예상해보세요.
# print("Hi" * 3)
print("\n32번")
""" 출력 결과 : HiHiHi """


# 033 화면에 '-'를 80개 출력하세요.
print("\n33번")
print("-"*80)


# 034 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
t1 = 'python'
t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예 : python java python java python java python java
print("\n34번")
t = t1+" "+t2+" "
print(t*4)


# 035 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때,
# % formatting을 사용해서 다음과 같이 출력해보세요. 
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
print("\n35번")
print("이름 : %s 나이 : %d" %(name1, age1))
print("이름 : %s 나이 : %d" %(name2, age2))


# 036 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("\n36번") 
print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))


# 037 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print("\n37번")
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")


# 038 삼성전자의 상장주식수가 다음과 같습니다.
# 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(",","")
상장주식수 = int(상장주식수)
print("\n38번")
print(상장주식수, type(상장주식수))


# 039 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"
print("\n39번")
print(분기[:7])


# 040 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print("\n40번")
data = data.replace(" ","")
print(data)


# 041 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print("\n41번")
print(ticker.upper())

# 042 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print("\n42번")
print(ticker.lower())


# 043 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
print("\n43번")
print("hello".capitalize())


# 044 파일 이름이 문자열로 저장되어 있을 때
# endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print("\n44번")
print(file_name.endswith("xlsx"))

# 045 파일 이름이 문자열로 저장되어 있을 때
# endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print("\n45번")
print(file_name.endswith("xlsx" or "xls"))


# 046 파일 이름이 문자열로 저장되어 있을 때
# startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
print("\n46번")
print(file_name.startswith("2020"))


# 047 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print("\n47번")
a= a.split(" ")
print(a)


# 048 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
print("\n48번")
print(ticker.split("-"))


# 049 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print("\n49번")
print(date.split("-"))


# 050 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print("\n50번")
print(data.replace(" ",""), end="")
print(data.strip(), end="")
print("공백확인용")

# 051 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다.
# 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
print("\n51번")
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)


# 052 051의 movie_rank 리스트에 "배트맨"을 추가하라.
print("\n52번 ")
movie_rank.append("배트맨")
print(movie_rank)


# 053 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
print("\n53번")
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)


# 054 movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
print("\n54번")
del movie_rank[3]
print(movie_rank)


# 055 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
print("\n55번")
del movie_rank[2:]
print(movie_rank)


# 056 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
# 실행 예 : langs = ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
print("\n56번")
lang = lang1 + lang2
print(lang)


# 057 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예:
# max:  7
# min:  1
print("\n57번")
print(f"max : {max(nums)}")
print(f"min : {min(nums)}")


# 058 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15
print("\n58번")
print(sum(nums))


# 059 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print("\n59번")
print(len(cook))


# 060 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
# 실행 예:
# 3.0
print("\n60번")
print(sum(nums)/len(nums))


# 061 price 변수에는 날짜와 종가 정보가 저장돼 있다.
# 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
print("\n61번")
print(price[1:])


# 062 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]
print("\n62번")
print(nums[::2])


# 063 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]
print("\n63번")
print(nums[1::2])


# 064 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]
print("\n64번")
print(nums[::-1])


# 065 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
print("\n65번")
print(interest[::2])


# 066 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print("\n66번")
print(" ".join(interest), print(type(interest)))


# 067 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print("\n67번")
print("/".join(interest),type(interest))


# 068 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print("\n68번")
print("\n".join(interest))


# 069 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']
print("\n69번")
string = string.split("/")
print(string)


# 070 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
print("\n70번")
data.sort()
print(data)


# 071 my_variable 이름의 비어있는 튜플을 만들라.
print("\n71번")
my_variable = ()
print(f"my_variable : {type(my_variable)}")


# 072 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다.
# 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
print("\n72번")
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank, type(movie_rank))


# 073 숫자 1 이 저장된 튜플을 생성하라.
print("\n73번")
tup = 1,
print("tup : ", tup, type(tup))


# 074 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
print("\n74번")
""" 튜플은 수정 및 추가가 불가능하다. 지원하지 않음. """


# 075 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print("\n75번")
""" 튜플 """


# 076 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
print("\n76번")
del t
t = ('A', 'b', 'c')
print(t)


# 077 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print("\n77번")
interest = list(interest)
print(f"interest : {interest}, {type(interest)}")


# 078 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print("\n78번")
interest = tuple(interest)
print(f"interest : {interest}, {type(interest)}")


# 079 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
print("\n79번")
""" 출력결과 : 'apple', 'banana', 'cake' """

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# (2, 4, 6, 8 ... 98)
print("\n80번")
ran = range(2,100,2)
ran = tuple(ran)
print(ran, type(ran))