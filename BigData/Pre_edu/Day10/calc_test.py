
print("계산기")
first = input("(사용 예시 : 10 * 4 )\n")
f_datas = first.split()

int(f_datas[0])

c_list = []




i = 1
calc = 0  # 현재 계산값.



while i > 0:   # i = 0이면 계산이 끝나도록.
  c_list[i-1] = input("계산기 시작 : ").strip() #입력값 받기

  if c_list[i-1].isdecimal():
    calc = int(calc+ int(c_list[i-1]))
    print(calc)
    i = i+1
  elif c_list[i-1]=="":
    print(calc)
    i=0
   # 연산자 
  else:
    if c_list[i-1]=="+":
        calc = calc+c_list[i-1]
    elif c_list[i-1]=="-":
        calc = calc-c_list[i-1]
    elif c_list[i-1]=="*":
        calc = calc*c_list[i-1]
    elif c_list[i-1]=="/":
        calc = calc/c_list[i-1]
    else:
        print("오류 발생!")  
        i = i+1

# 4 * 7, * 7, * 58 *

