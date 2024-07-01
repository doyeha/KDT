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

