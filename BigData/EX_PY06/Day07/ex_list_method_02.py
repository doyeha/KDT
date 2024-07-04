# ------------------------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# ------------------------------------------------------------------
import random as rad
# [메서드 - 요소 추가 메서드 append(데이터)]
datas = [1,3,5]

# 새로운 데이터 100 추가
datas.append(100)
print(f"datas의 개수 : {len(datas)}, {datas}")


# [메서드 - 요소 추가 메서드 insert(인덱스, 데이터)]
datas.insert(0,300)
print(f"datas 개수 : {len(datas)},{datas}")

datas.insert(-1,200)
print(f"datas 개수 : {len(datas)},{datas}")


# [실습] 임의의 숫자 숫자 10개 저장하는 리스트 생성
lis = []
for i in range(10):
    lis.append(rad.randint(1,1000))

print(sorted(lis))

# - random 모듈
# - 빈리스트 생성
# - for 반복문
nums = []
for cnt in range(10):
    nums.append(rad.randint(1,50))


# [메서드 : 요소 삭제 메서드 remove(데이터)]
# datas 개수:7, [300, 1, 3, 4, 5, 6, 7]
for cnt in range(datas.count(300)):
    datas.remove(300)
    print(f"datas 개수 : {len(datas)},{datas}")
