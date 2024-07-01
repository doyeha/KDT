# -------------------------------------------------------
# list 전용 함수 즉, 메서드 살펴보기
# -------------------------------------------------------
datas = []

#원소/요소 추가 메서드 - (1) append(데이터)
datas.append("A")
datas.append("B")
print(f"datas = > {datas}, {len(datas)}개")

#원소/요소 추가 메서드 - (2) insert(인덱스, 데이터)
datas.insert(0, 100)
print(f"datas = > {datas}, {len(datas)}개")
datas.insert(-1, 100) # 맨 마지막이 아니라 걔를 뒤로 밀어내는 거기 때문에 -2 자리에 들어간다.
print(f"datas = > {datas}, {len(datas)}개")

# 원소/요소 삭제 메서드 - remove(데이터)

if 100 in datas:
    datas.remove(100) # 제일 처음 발견되는 데이터 삭제
    print(f"datas = > {datas}, {len(datas)}개")
else: pass

# 원소/요소 모두 삭제 메서드 - clear() 빈 리스트가 됨.
datas.clear()
print(f"datas = > {datas}, {len(datas)}개")

# 원소/요소 정렬 메서드 - sort()
datas = [9, -3, 1, 7, 2, -5]
datas.sort()   # 기본은 오름차순
print(datas)

datas = [9, -3, 1, 7, 2, -5]
datas.sort(reverse=True) #큰값 >>> 작은 값 나열 즉, 내림차순
print(datas)


datas = ["abc", "abd", "aba"]
datas.sort()
print(datas)

# 원소/요소 역순으로 출력 메서드 -> reverse()
# 제일 뒤에 있던 데이터 ==> 0번 위치로, 0번 위치에 있던 데이터 ===> 제일 마지막으로
datas = [9, -3, 1, 7, 2, -5]
print("전", datas)
datas.reverse()
print("후", datas)

# 원소/요소에 인덱스 찾아주는 메서드 -> index(데이터) : 없으면 에러 발생
idx = datas.index(9)
print(f"datas.index(9) => {idx}")

if 0 in datas:
    idx = datas.index(0)
    print(f"datas.index(0) => {idx}")


# 원소/요소를 리슽에서 꺼내주는 메서드 - pop() : 제일 마지막 원소 / 요소 꺼냄
print("전", datas)
value = datas.pop()
print("후", datas)
value = datas.pop()
print("후", datas)

# 원소/요소를 리슽에서 꺼내주는 메서드 - pop(인덱스) : 원소 / 요소 꺼냄
value = datas.pop(1)
print("후", datas)





## 내장함수 => sorted()
## 원본 데이터는 그대로 두고 정렬된 복사본 반환
datas2 = sorted(datas)
 #저장 xxxx / sort는 저장을 함 .
print(datas, datas2)
