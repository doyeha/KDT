## 219P - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - -
# 19.6 심사문제 | 입력 정수의 높이만큼의 산을 별로 출력.
hei = int(input())
h = 0 # 반복 제어 변수
s = 0 # 별 조절 변수
while h<hei:
    for i in range(1,hei+1): # 세로 |hei = 5, 1~5반복 (층 정리)
        for j in range(1,(hei*2)): # 가로 | hei에 비례해 가로 생성.

            ## 층에 따라 앞 부분 공백 출력
            if j < int(hei-i+1): #5층이라면, 1층에는 공백 4개 후 별 1개 // 총5층-1층+1 = 5번째 자리. 별이 들어와야함. 그 전까지 공백.
                print(" ", end="")
                continue
            elif j == int((hei-i+1)): # 별 들어올 자리부터 입력.
                print("*"*(i+s),end="") # 층에 따른 별 갯수 조절
                continue
        print() # 가로 출력 후 엔터      
        s = s + 1 
        h += 1


layer = int(input())
h = 0 # 반복 제어 변수
s = 0 # 별 조절 변수
while h<layer:
    for i in range(1,layer+1): # 반복 - 층
        for j in range(1,(hei*2)): # 가로 | layer 에 비례해 가로 생성.
            ## 층에 따라 앞 부분 공백 출력
            if j <= int(layer-i): #5 공백 공식 i-1 
                print(" ", end="")
            else: # 별 들어올 자리부터 입력.
                print("*"*(i+s),end="") # 층에 따른 별 갯수 조절
                break
        print() # 가로 출력 후 엔터      
        s = s + 1 
        h += 1

"""         -> 공백                          별
    *       -> 4 : x-1(층 넘어가는 h로.) | 1  j
   ***      -> 3 : x-2                  | 3  j+2
  *****     -> 0 : x-3                  | 5 
 *******    -> 1                        | 7 
*********   -> -                        | 9  

맨 아래 층 => y = (Xx2)-1
""" 