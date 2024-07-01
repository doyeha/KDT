# # 1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
# . 출력하는 코드 구현하세요
# [입력] msg = [‘Good’, ‘child’, ‘Zoo’, ‘apple’, ‘Flower’, ‘ zero’]
# 함수호출
# [출력] 정렬 결과 : ['zero', 'child', 'apple', 'Zoo', 'Good', 'Flower']
# 가장 높은 문자열 : zero,가장 낮은 문자열 : Flower 
msg = (input("언어로 구성된 리스트를 입력해주세요."))
msg = msg[1:-1]
print(msg)

# msg = msg.split(",")
# print(msg)

# msg2 = msg.sort()
# print(f"정렬 결과 : {msg2}")
# print(f"가장 높은 문자열 : {msg2[0]}, 가장 낮은 문자열 : {msg2[-1]}")