# ------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# - 형태 : {키1:값, 키2:값, 키3:값, ... 키n: 값}
# - 키는 중복x, 값은 중복o
# - 데이터 분석 시 파일 데이터 가져올 때 많이 사용
# ------------------------------------------------------------------
## [Dict 생성]
data = {}
print(f"data = > {len(data)}개, {type(data)}")

# 사람에 대한 정보 : 이름, 나이, 성별
data = {"name":"maginga", "age":100, "gender":"M"}
print(f"data = > {len(data)}개, {type(data)}")

# 강아지에 대한 정보 : 품종, 무게, 색상, 성별, 나이
dog = {"breed":"요키", "weight":"3kg", "color":"silver", "gender":"M", "age":14}
print(f"dog = > {len(dog)}개, {type(dog)}")

# 색상 출력
print(f"{dog['color']} {dog['color']}")

# 성별, 품종 출력
print(f"강아지 성별 : {dog['gender']}, 강아지 품종 : {dog['breed']}")

## [Dict 원소/요소 변경]
## - 변수명[키] = 새로운 값
dog["age"] = 6
print(dog)

# 몸무게 3kg = > 8kg
dog["weight"] = "8kg"
print(dog)

##- del 변수명[키] 또는 del(변수명[키])
del dog["gender"]
print(dog)

## 추가 : 변수명[새로운 키]=값
## 이름 추가
dog["name"] = "초코"
print(dog)
dog["name"] = 3
print(dog)