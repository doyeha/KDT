much = int(input('몇칸으로 만들래...? 굳이 만들어야할까 ...? 이걸 왜? 뭐 땜에 ?'))
MG = [[0]*much]*much
# MG =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

"""
0 <= col <= 4 
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24  0 <= row <= 4
30 31 32 33 34
40 41 42 43 44
"""

# row -1 / col + 1 
col=0
row=0
# much-1 / much+1
def exist_check(row,col):
    if MG[row][col] != 0:
        row += 2
        col -= 1
    else:
        row = row
        col = col
    return row, col

        # col -=1

def over_check(row,col):
    if (col<0 or col>(much+1)) & (row<0 or row>(much+1)):
        row += 2
        col -=1
    elif (col<0 or col>(much+1)):
        row = row
        col = 0
    elif (row<0 or row>(much+1)):
        col = col
        row = much+1
    che = 1
    return row, col, che



# MG[0][2] = 1 # 고정 시작점.
for i in range(1,(much*much+1)):
    che = 0
    col+=1
    row-=1
    if i == 1:
        col=2
        row=0
        MG[row][col] = i
    # else:
    #     # exist_check(row,col)
    #     row =exist_check(row,col)[0]
    #     col =exist_check(row,col)[1]
    #     che = exist_check(row,col)[2]
    #     if che != 1:
    #         row = over_check(row,col)[0]
    #         col = over_check(row,col)[1]

    else:
        row, col, che = over_check(row,col)

        # exist_check(row,col)
        # if che != 1:
        row,col = exist_check(row,col)

            # che = exist_check(row,col)[2]
            
            

        # exist_check(row,col)
        MG[row][col] = i

for i in range(much):
    print(MG[i])

