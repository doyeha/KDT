# ------------------------------------------------------------------
# set 자료형 살펴보기
# - 여러가지 종류의 여러 개 데이터를 저장
# - 단! 중복 안됨!!
# - 컬렉션 타입의 데이터 저장 시 Tuple 가능
# - 형태 : {데이터1, 데이터2, 데이터3, ..., 데이터n}
# ------------------------------------------------------------------
## [Set 생성]
data = []
data = ()
data = {}
data  = set()

print(f"data의 타입 {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}")

# 여러 개 데이터 저장한 set // 중복 데이터는 포함x
data = {10, 30, 20, -9, 10, 30, 30, 10, 10}

print(f"data의 타입 {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}")
""" 출력 결과 원소/요소 개수 4개 """


data = {1,2,3,(1,2,3)}
print(f"data의 타입 {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}")

data = {1,2,3,(1,)[0]}
print(f"data의 타입 {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}")

# set() 내장함수
data = {1,2,3} # ===> set([1,2,3])
data = set()
data = set({1,2,3})
data = set([1,2,1,2,3])
data = set("Good")

print(data)

data = set({"name": "홍길동", "age":12})
print(data)

data = list("Good")
print(data)



# 다양한 타입 ===> set 변환
data = {1,2,3} # ===> set([1,2,3])
data = set()
data = set({1,2,3})
data = set([1,2,1,2,3])
data = set({"name":"홍길동", "age":12, "name":"배트맨"})
data = set((1,2,1,2,1))

print({"name":"홍길동", "age":12, "name":"배트맨"})
print(data)

