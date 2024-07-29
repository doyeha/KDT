## 윷놀이 게임
# 4개의 윷가락을 교대로 던져 20점 이상의 점수가 먼저 나오는 사람의 승리
# 윷가락을 던져 나온 점수가 윷 4점 / 모 5점 일 시 한번 더 던진다.


# 윷가락 4개를 동시에 던지는데, 앞면이 나올 시 1점, 뒷면이 나올 시 0점으로 [1 2 3 4] 총 4개의 윷이 들어가있는
# 배열에서 앞면의 개수로 점수를 파악한다. 이때 전부 뒷면일 시 윷, 4점 // 전부 앞면일 시 5점이다.

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

        if sticks.count(1):
            yut = "도"
            score = 1
        elif sticks.count(2):
            yut = "개"
            score = 2
        elif sticks.count(3):
            yut = "걸"
            score = 3
        elif sticks.count(0):
            yut = "윷"
            score = 0
        elif sticks.count(4):
            yut = "모"
            score = 4
        else:
            yut = "오류 발생"
        
        if player == A:
            A_total_score += score
        elif player == B:
            B_total_score += score
        
        if player == A:
            A_side = f"{A} {sticks} : {yut} ({score}점)/{A_total_score}---->"
            print( "{0:<30}".format(A_side) )
        elif player == B:
            B_side = f"<----{B} {sticks} : {yut} ({score}점)/{B_total_score}"
            print("{0:>30}".format(B_side))
        return sticks
        
    # a = throw_yut()
    # print(a.count(1))

    while True:
        A_total_score = 0
        B_total_score = 0
        print("게임을 시작합니다!")
        A = input("첫 번째 플레이어의 이름을 입력해주세요. : ")
        B = input("첫 번째 플레이어의 이름을 입력해주세요. : ")
        first = rand.randint(0,1)
        if first==1:
            print(f"먼저 시작할 플레이어는 {A}입니다.")
            while True:
                throw_yut(A)
                # 점수 넘었는지 체크
                if A_total_score >= 20 or B_total_score >= 20:
                    break
                # 윷, 모 나왔을 시 재가동
                if throw_yut(A) in [4,5]:
                    throw_yut(A)
                    if A_total_score >= 20 or B_total_score >= 20:
                        break
                    else:
                        continue
                else:
                    continue
                
                b = throw_yut(B)




        else:
            print(f"먼저 시작할 플레이어는 {B}입니다.")

        
        
        # 누군가가 20점이 달성하면 종료.
        # 각 플레이어 이름 입력 후 