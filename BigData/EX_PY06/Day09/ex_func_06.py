# ------------------------------------------------------------------
# 람다표현식 또는 람다함수
# - 1줄 함수, 익명 함수
# - 형식 : lambda 매개변수 : 실행코드
# ------------------------------------------------------------------
names = {1:"Kim", 2:"Adam", 3:"Zoo"}
# print(names.items())

# 정렬하기 => 내장함수 sorted() --> list 반환 ㄱㄷ
# 기본이 키로 정렬
result = sorted(names)
print("오름차순 정렬 ", result)


# value로 정렬 => names.items() -> (1,Kim), (2,Adam), (3,Zoo)
result = sorted(names.items(), key=lambda x : x[1]) 
# names의 items 키,값 식으로 나오게 할건데, 기존에 기준(key)가 딕셔너리의 key였으면? 이제는 item 묶음의 2번째것을 기준으로 한다.?

print("오름차순 정렬 ", result)



# test = ["ace", "Acb", "base", "Fruit"]
# result = sorted(test, key = lambda lower(test))


result = sorted("This is a test string from Andrew".split())
print(result)

result = sorted("This is a test string from Andrew".split(), key=str.lower)
print(result)

# map()와 lambda ---------------------------
data = [11,22,33,44]

# - 각 원소 값에 곱하기 2를 해서 다시 리스트에 저장
# 방법 1
def multi2(value):    return value * 2
data2 = list(map(multi2, data))
# 방법 2
data3 = list(map(lambda a : a*2, data))

print(data2, data3)


