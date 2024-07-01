age = int(input())
cash = 9000

if 7 <= age <= 12:
    cost = 650; print(cash - cost)
elif 13 <= age <= 18:
    cost = 1050; print(cash - cost)
elif 19 <= age:
    cost = 1250; print(cash - cost)
else:
    print("사용 불가능")
