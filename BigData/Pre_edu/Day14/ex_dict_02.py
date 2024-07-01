# -------------------------------------------------------
# 딕셔너리 자료형 전용 함수 즉, 메서드
# -------------------------------------------------------
jumsu = {"국어":100, "수학":90, "체육":70}

# 모든 원소/요소를 출력하세요.
# 키 추출 메서드 => keys()
keys = jumsu.keys()
print(keys)

for k in keys:
    print(k, jumsu[k])


# 값 추출 메서드 => values()
values = jumsu.values()
for v in values:
    print(v)



# 키와 값 묶음으로 추출하는 메서드 => items()
# (키, 값) 튜플
items = jumsu.items()
print(items)

for i in items:
    print(i)
