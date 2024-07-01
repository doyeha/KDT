# ---------------------------------------
# List 자료형 살펴보기
# - 여러 종류의 데이터를 저장하는 자료형
# - 형식 : [데1, 데2, ..., 데N]
# - 특징 : 리스트 안에 포함된 데이터 하나하나를 원소 / 요소
#          원소 / 요소 식별하기 위해서 인덱싱, 슬라이싱 
#          원소 / 요소 단위로 수정 가능함!
# ---------------------------------------
# 리스트 인스턴스 생성 
# 
datas = []
print(f"타입 : {type(datas)}")
print(f"요소수 : {len(datas)}개")

datas = [1,2,3]
print(f"\n\n 타입 : {type(datas)}")
print(f"요소수 : {len(datas)}개")



datas = ["A",False, 10.98, 1]
print(f"\n\n 타입 : {type(datas)}")
print(f"요소수 : {len(datas)}개")

## 리스트 원소 / 요소 읽기
## => 인덱싱 방식
print(f"datas[0] => {datas[0]}")
print(f"datas[-1] => {datas[-1]}")

## =>슬라이싱방식[시작 인덱싱 : 끝인덱싱 +1]
print(f"datas[0:1] => {datas[0:1]}")
print(f"datas[0:2] => {datas[0:2]}")

## 짝수 인덱스 요소만 추출
print(f"datas[::2] => {datas[::2]}")

