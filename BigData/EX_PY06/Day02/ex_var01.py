# ------------------------------------------------------------------ 
# 변수와 메모리 관계
#  - 파이썬에서 사용하는 변수 => 참조형변수
#  - 메모리 힙 영역에서 저장된 데이터의 주소 저장
#  -> 주소 확인 내장함수 : id()
# ------------------------------------------------------------------ 
# 나이를 저장하기
age = 27
number = 27

# 데이터가 존재하는 주소 확인
print(id(age))
print(id(27))
  # 실제로는 다르겠지만, age라는 객체에 27이라는 값을 넣었기에 2개의 메모리 주소는 동일하다.



id(100,300,age)


chr = 45*300000
random = 26*10
rad = 10**random

print(chr, random, rad)