"""
one, two = map(int, input().split()) 

while True:
    if one > two:
        print("더 작은 숫자를 먼저 적어주세요.")
        break
    print("Fizz"*(one % 5 == 0) + "Buzz"*(one % 7 ==0) or one)
    # if one % 5 == 0 and one % 7 == 0:
    #     print("FizzBuzz")    
    one += 1
    if one == two:
        break
"""
one, two = map(int, input().split()) 
i = 1
while one < two:    
    if one % 5 == 0 and one % 7 ==0:
        print("FizzBuzz", end=" ")
        print("\n") if i % 5 == 0 else None

    elif one % 5 == 0:
        print("Fizz", end=" ")
        print("\n") if i % 5 == 0 else None
    elif one % 7 == 0:
        print("Buzz", end=" ")
        print("\n") if i % 5 == 0 else None
    else:
        print(f"{one}", end=" ")
        print("\n") if i % 5 == 0 else None

    i = i + 1
    one += 1



    # print("Fizz"*(one % 5 == 0) + "Buzz"*(one % 7 ==0) or one)
    # # if one % 5 == 0 and one % 7 == 0:
    # #     print("FizzBuzz")    
    # one += 1
    # if one == two:
    #     break