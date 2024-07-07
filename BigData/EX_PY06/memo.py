




# ------------------------------------------------------------------
# Dict 자료형 살펴보기
# - Dict 자료형 전용의 함수 즉, 메서드(Method) 사용
# - 사용법 : 변수명.메서드명()
# ------------------------------------------------------------------
## [Dict에서 키만 추출하는 메서드 keys()]

p1 = {"name":"홍길동", "age" : 20, "job":"학생"}

result = p1.keys()
print(f"키 추출 : {result}, {type(result)}")
# keys 메서드로 나온 결과물은 dict_keys라는 타입이기 때문에 keys[0]하면 오류가 발생한다.

result2 = list(p1.keys())
print(f"키 추출 : {result2[0]}, {type(result2)}")


## [Dict에서 값만 추출하는 메서드 values()]
result = p1.values()
print(f"값 추출 : {result}, {type(result)}")

## [Dict에서 키,값 만 추출하는 메서드 items()]
result = p1.items()
print(f"키와 값 묶음 추출 : {result}, {type(result)}")
# dict_items라는 클래스로 출력, dict_items([('name', '홍길동'), ('age', 20), ('job', '학생')]) 

result = list(result)
print(f"키와 값 묶음 추출 : {result[0]}, {type(result[0])}")

# ------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 연산자와 내장함수
# ------------------------------------------------------------------
person = {"name":"홍길동", "age" : 20, "job":"학생"}
dog = {"age":5, "kind":"허스키","weight":"3kg", "color":"검정", "gender":"남성"}
jumsu = {"국어":90, "수학":178, "체육":100}

## [연산자]
# 산술 연산X
# person + dog

# 멤버연산자 in, not in
#       key
print("name" in dog)
print("name" in person)


#       values : dict 타입에서는 key만 멤버 연산자로 확인한다.
print("허스키" in dog)
print(20 in person)

# Value 추출
print("허스키"  in dog.values())
print(20  in person.values())


## [내장함수]
## 원소/요소 개수 확인 : len()
print(f"dog의 요소 개수 : {len(dog)}")
print(f"person의 요소 개수 : {len(person)}")

## 원소/요소 정렬 : sorted()
#  - 키만 정렬
print(f"dog 오름차순 정렬 : {sorted(dog)}")              # 반환값 list, 키만 추출
print(f"person 내림차순 정렬 : {sorted(person, reverse=True)}") 

# print(f"dog 오름차순 정렬 : {sorted(person.values(), reverse=True)}") 
print(f"jumsu 값 오름차순 정렬 : {sorted(jumsu.values())}")
print(f"jumsu 키 오름차순 정렬 : {sorted(jumsu)}")

print(f"jumsu 값 오름차순 정렬 : {sorted(jumsu.items())}") # items 키 기준 정렬

print(f"jumsu 값 오름차순 정렬 : {sorted(jumsu.items(), key = lambda x:x[1])}") 
# 기존에 튜플 0을 기준으로 정렬하던 것을 기준점을 인덱스 1번을 기준으로 삼겠다는 의미.


## 동일한 타입에서만 정렬 가능함.
n1 = [1,4,9,-2]
n2 = ["a","Z","f"]
n3 = [1, "A", -4 , 9, "F"] # int & str 로 이루어짐. 서로 다른 타입이기 때문에 정렬 불가능.
# print(sorted(n3))

