# ------------------------------------------------------------------
# Dict 전용 함수 즉, 메서드
# -> keys(), values(), items()
# 수정 불가 즉, 추가, 삭제, 변경 x
# ------------------------------------------------------------------
person = {"name":"홍길동", "age": 10}

# [메서드 - 값 읽어오는 메서드 get(key)]
# 키에 해당하는 values가 없으면 default값 반환 
# print(person["name"])
# # print(person["gender"]) #Key Error

# print(person.get("name", "몰라"))
# print(person.get("gender", "없음"))
# print(person.get("gender" if "gender" in person))


# [메서드 - 키와 값 추가 메서드]
person["gender"] = "남"
print(person)

# [메서드 - 수정 및 추가 업데이트 메서드 update((k=v)]
# 수정 / 업데이트
person["gender"] = "여"
print(person)
person.update(gender = "어린이")
print(person)

person.update({"phone" : "010", "birth" : "240101"})
print(person)


## **{"weight":100, "height":170} ==>
## weight=100, height:170
person.update({"weight" : 100, "height" :170})
print(person)

# save = {}
# msg = "Hello Good Luck"
# alpha = set(msg)
# print(alpha)
# for m in alpha:
#     print(m, msg.count(m))
#     save[m] = msg.count(m)

# print(save)









