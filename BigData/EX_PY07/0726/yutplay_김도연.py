## 윷놀이 게임
# 4개의 윷가락을 교대로 던져 20점 이상의 점수가 먼저 나오는 사람의 승리
# 윷가락을 던져 나온 점수가 윷 4점 / 모 5점 일 시 한번 더 던진다.


# 윷가락 4개를 동시에 던지는데, 앞면이 나올 시 1점, 뒷면이 나올 시 0점으로 [1 2 3 4] 총 4개의 윷이 들어가있는
# 배열에서 앞면의 개수로 점수를 파악한다. 이때 전부 뒷면일 시 윷, 4점 // 전부 앞면일 시 5점이다.
import time
import random as rand
"""
형태 sticks=[0,0,0,0]
"""

def throw_yut(player):
    while True:
        sticks = []
        for i in range(4):
            sticks.append(rand.randint(0,1))
        # 윳 던짐! 이제 점수 카운팅

        if sticks.count(1)==1:
            yut = "도"
            score = 1
        elif sticks.count(1)==2:
            yut = "개"
            score = 2
        elif sticks.count(1)==3:
            yut = "걸"
            score = 3
        elif sticks.count(1)==0:
            yut = "윷"
            score = 4
        elif sticks.count(1)==4:
            yut = "모"
            score = 5
        else:
            yut = "오류 발생"
        
        if player == A:
            global A_total_score
            A_total_score += score
            A_side = f"{A} {sticks} : {yut} ({score}점) / (총"+"{:>2}점)---->".format(A_total_score)
            print( "{0:<80}".format(A_side) )
            time.sleep(1)
            if A_total_score >= 20:
                break
            elif score not in [4,5]:
                break
        elif player == B:
            global B_total_score
            B_total_score += score
            B_side = f"<----{B} {sticks} : {yut} ({score}점) / (총"+"{:>2}점)".format(B_total_score)
            print("{0:>80}".format(B_side))
            time.sleep(1)
            if B_total_score >= 20:
                break
            if score not in [4,5]:
                break
    return sticks


# 기능 검증 
def throw_only(player):
    while True:
        sticks = []
        for i in range(4):
            sticks.append(rand.randint(1,1))
        # 윳 던짐! 이제 점수 카운팅

        if sticks.count(1)==0:
            yut = "윷"
            score = 4
        elif sticks.count(1)==4:
            yut = "모"
            score = 5
        else:
            yut = "오류 발생"
        
        if player == A:
            global A_total_score
            A_total_score += score
            A_side = f"{A} {sticks} : {yut} ({score}점) / (총"+"{:>2}점)---->".format(A_total_score)
            print( "{0:<80}".format(A_side) )
            time.sleep(1)
            if A_total_score >= 20:
                break
            elif score not in [4,5]:
                break
        elif player == B:
            global B_total_score
            B_total_score += score
            B_side = f"<----{B} {sticks} : {yut} ({score}점) / (총"+"{:>2}점)".format(B_total_score)
            print("{0:>80}".format(B_side))
            time.sleep(1)
            if B_total_score >= 20:
                break
            if score not in [4,5]:
                break
    return sticks

while True:
    A_total_score = 0
    B_total_score = 0
    print("게임을 시작합니다!")
    A = input("첫 번째 플레이어의 이름을 입력해주세요. : ")
    B = input("두 번째 플레이어의 이름을 입력해주세요. : ")
    first = rand.randint(0,1)
    if A =='검증' or B == '검증':
        throw_only('검증')
        print('최악의 상황 검증모드 끝')
        break
    elif first==1:
        print(f"먼저 시작할 플레이어는 {A}입니다.")
        while True:
            throw_yut(A)
            if A_total_score >= 20:
                break
            throw_yut(B)
            if B_total_score >= 20:
                break

        if A_total_score >= 20:
            print(f"{A}의 승리입니다. 게임이 종료됩니다.")
            break
        elif B_total_score >= 20:
            print(f"{B}의 승리입니다. 게임이 종료됩니다.")
            break
        

    else:
        print(f"먼저 시작할 플레이어는 {B}입니다.")
        while True:
            throw_yut(B)
            if B_total_score >= 20:
                break

            throw_yut(A)
            if A_total_score >= 20:
                break


        if A_total_score >= 20:
            print(f"{A}의 승리입니다. 게임이 종료됩니다.")
            break
        elif B_total_score >= 20:
            print(f"{B}의 승리입니다. 게임이 종료됩니다.")
            break

    
    
    # 누군가가 20점이 달성하면 종료.
    # 각 플레이어 이름 입력 후 