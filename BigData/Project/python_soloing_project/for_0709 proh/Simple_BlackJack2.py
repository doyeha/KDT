import random as rand
import time

# 카드 덱, 키로 뽑아져있는지 구분.
# 딜러 카드 나중에 보이기 진행.
card_deck = {
1:"01", 2:"01", 3:"01", 4:"01", 5:"01", 6:"01",   # 인덱스 0~5 // 
7:"02", 8:"02", 9:"02", 10:"02", 11:"02",         # 인덱스 6~10
12:"03", 13:"03", 14:"03", 15:"03",               # 인덱스 11~14
16:"04", 17:"04", 18:"04",                        # 인덱스 16~17
19:"05", 20:"05", 21:"05",                        # 인덱스 18~20
22:"06", 23:"06",                                 # 인덱스 21 22
24:"07", 25:"07",                                 # 인덱스 23 24
26:"08", 27:"09", 28:"10", 29:"10", 30:"11"       # 인덱스 25 26 27 28 29 
}

""" [ 투명한 확률 공개 -☆ ]
01 : 20.0% (6개)
02 : 16.6% (5개)
03 : 13.3% (4개)
04 : 10.0% (3개)
05 : 10.0% (3개)
06 : 06.6% (2개)
07 : 06.6% (2개)
08 : 03.3% (1개)
09 : 03.3% (1개)
10 : 06.6% (2개)
11 : 03.3% (1개)
"""

def check_card(card): # 카드 뽑았는지 확인.
    if card not in dealer_card and card not in player_card: # 현재 카드 자체가 1개의 딕셔너리 쌍이니까. 그대로 넣는다.
        return True
    else:
        return False

def pick_card():    # 카드 랜덤 뽑기. 튜플 키로 카드번호 반환.
    ran = rand.randint(1,30)
    card = card_deck[ran]
    return {ran : card}  # 리스트 index 0은 키 / 1은 카드번호

def get_first_card():       # 처음 카드 2개 뽑기
    dealer_card.clear()
    player_card.clear()
    while len(dealer_card)<=1:
        card = pick_card()
        # print(f"1번 카드 {card}")
        if check_card(card) == True:
            dealer_card.append(card)

    while len(player_card)<=1:
        card = pick_card()
        # print(f"1번 카드 {card}")
        if check_card(card) == True:
            player_card.append(card)

def play_get_card():    # pick_card & check_card 활용, 플레이어가 카드 1장 추가하는 것.
    i = 0
    while i < 1:
        card = pick_card()
        # print(f"1번 카드 {card}")
        if check_card(card) == True:
            player_card.append(card)
            i += 1
    else:
        i = 0

def dealer_ger_card() :
    i = 0
    while i < 1:
        if (play_sum(player_card) - deal_sum(dealer_card)) >= 4 : # 플레이어가 딜러의 합산보다 4 이상 높으면 70프로 확률로 카드 뽑기
            do = rand.randint(1,10)
            if do in [1,2,3,4,5,6,7]: 
                card = pick_card()
                if check_card(card) == True:
                    dealer_card.append(card)
        if (play_sum(player_card) - deal_sum(dealer_card)) > 0 : # 플레이어가 딜러의 합산보다 3 ~ 0 ? 20프로 확률로 카드 뽑기
            do = rand.randint(1,10)
            if do in [1,2]: 
                card = pick_card()
                if check_card(card) == True:
                    dealer_card.append(card)
        else:
            i = 1   # while문 막는 용도 // 플레이어와 딜러 간의 숫자 합 차이가 4이상 or 0~3에 따라 딜러가 카드를 더 뽑는가에 대한 확률 조정

def play_sum(player_card):  # 플레이어 접수 합산
    play_sum = 0
    for i in player_card:   
         for i in i.values():
             i = int(i)
             play_sum += i
    return play_sum

def deal_sum(dealer_card):  # 딜러 점수 합산
    deal_sum = 0
    for i in dealer_card:   
         for i in i.values():
             i = int(i)
             deal_sum += i
    return deal_sum

def show_card(deal):         # 카드 딜러:  당신 : 카드 형으로 출력 완.
    # 딜러 - - - - - - - - - - - - - - - - - - - - - - - - - -  
    # 첫줄
    if deal == False:   #  보이는 상황
       line2 = ""
       dealer_sum = []
       ds = 0
       for i in dealer_card:
                for v in i.values():                 # line2 먼저 제작 해
                    line = (f"│ {v} │ ")     # │ 04 │ │ 04 │ │ 04 │ │ 04 │
                    line2 = line2 + line

                for v in i.values():
                    i = int(v)
                    dealer_sum.append(i)   # 딜러들 값으로 이루어진 리스트 
                    


       for show in range(0,len(dealer_card)-1): #추가 연출
            sh = len(dealer_card)-2
            if show == sh: print("\n\n\n\n")  # 화면 정리용

            print("            ┌────┐ ┌────┐ ", end="")
            print("┌────┐ "*show)
                #둘 ㅉ재ㅜㄹ
            print(f"딜러 {sum(dealer_sum[:2+show]):^2}점 :", end=" ")    
            print(line2[:13+7*show])  # 7씩 증가
            print("            └────┘ └────┘ ", end="")
            print("└────┘ "*show)
            if show == sh:
                pass
            else:
                print(f"당신의 점수는 {play_sum(player_card)}, 딜러가 카드를 뽑는 중입니다.", end="")
                print("."*show if not len(dealer_card) == show else "")
            if show == sh:
                time.sleep(0.5)
            else:
                time.sleep(1.5)



    else:   # 안보이는 상황
        for i in range(len(dealer_card)):   
            if i == 0: print(f"            ┌────┐", end="")
            else: print(f" ┌────┐", end=" ")
        # 둘째줄
        print(f"\n딜러 ??점 :", end= " ")
        for i in dealer_card:   
            for i in i.values():
                print(f"│ ╬╬ │", end=" ")
        # 셋째 줄
        print()
        for i in range(len(dealer_card)):
            if i == 0: print(f"            └────┘", end="")
            else: print(f" └────┘", end=" ")
        print()
        


    ## 플레이어 - - - - - - - - - - - - - - - - - - - - - - - - - -        
    # 첫줄
    for i in range(len(player_card)):   
        if i == 0:
            print(f"            ┌────┐", end="")
        else:
            print(f" ┌────┐", end="")
    print(f"\n당신 {play_sum(player_card):>2}점 :", end= " ")
    for i in player_card:   # 둘째줄
        for i in i.values():
            print(f"│ {i} │", end=" ")
    print()
    for i in range(len(player_card)):
        if i == 0:
            print(f"            └────┘", end="")
        else:
            print(f" └────┘", end="")
    print()
        
explains = """
이 게임은 카드를 뽑아 그 수의 합이 21을 넘지 않되 21에 가장 근접하는 사람이 이기는 게임입니다.
딜러와 당신에게 각각 2장의 카드가 주어지고, 당신의 선택에 따라 카드를 한 장씩 더 받을 수 있습니다.
힛을 달성한다면 게임 머니를 더 많이 획득하실 수 있습니다.

딜러의 카드는 당신이 더 이상 카드를 받지 않겠다고 했을 때, 마지막에 공개됩니다.

카드를 새로이 받다가 21이 넘는 순간 당신의 패배이니 조심하시기를!

그럼, 게임을 시작하시겠습니까?
"""

def over_check():  #  버스트 확인 및 상태에 따라 다른 값 return
    if play_sum(player_card) >= 22:     # 플레이어 21 초과
        return "플 21 초과" 
    elif play_sum(player_card) == 21:     # 플레이어 21 달성 
        return "플 힛"  
    elif deal_sum(dealer_card) >= 22:   # 딜러 21 초과
        return "딜 21 초과"
    elif play_sum(dealer_card) == 21: # 딜러 21 달성
        return "딜 힛"
    else:
        return 0
    
    # if deal_sum(dealer_card) < 21 and play_sum(player_card) < 21:
    #     return 0


game_money = 1000   # 초기 게임자금
game_cost = 500     # 게임 참여금
win = 0             # 연승 횟수
lose = 0            # 연패 횟수
## main 시작-------------------------------------------
while game_money >= 500:
    game_cost = game_cost*(win+1)   # 500 1000 2000 4000
    deal = True # 딜러 카드 보이는지 유무 변수/ True면 안보임.
    dobak = False   # 패배 후 재도전 시 True
    check = 0   # 딜러, 플레이어 카드 21 초과 체크
    dealer_card = []    # 딜러 현재 카드 덱
    player_card = []    # 플레이어 현재 카드 덱

    ## [플레이어의 이전 플레이 기록에 따라 다른 문구 출력]
    # 완전 쌩 처음.
    if lose == 0 and win == 0:  
        print(f"KD 도박장에 오신 것을 환영합니다. 저희의 대표게임은 K_Jack입니다. \n★Welcome★ 선물로 게임머니 1000을 드렸습니다.\n K_Jack 시작하시겠습니까?\n 현재 게임 머니 : {game_money} \n 한 게임 당 게임 머니 500이 소모됩니다.\n시작하시려면 y를, 게임 설명을 원하신다면 e를 입력해주세요. : ", end=" ")      
    # 연승 중
    elif lose <= 0 and win > 0: 
        print(f"\n\n이기고 오셨군요? 축하드립니다. \n언제나 초심자의 행운이란 것이 있는 법이지요.\n연승 시 참여 및 상금이 2배씩 증가합니다. 현재 {win}연승 중, {500+500*win} 머니가 소모됩니다.\n현재 게임 머니 : {game_money} \n더 큰 머니를 걸고, 도전 해보시겠습니까? (y/n)")
    # 패배.
    elif lose > 0: 
        print(f" 이전 게임이 잘 풀리지 않으셨나보군요. 현재 게임 머니 {game_money}를 소유중이십니다.\n정말 다시 도전하십니까?")
        dobak = True    # line226 사용.


    ## [게임 시작 Yes or No And 설명 듣기 선택]
    get_input = input()
    # 게임 시작 선택
    if get_input in ["예", "Yes", "Y", "네", "y", "ㅛ"]:
        game_money -= game_cost   # 연승에 따라 게임 참여금액 증가
        print("너무 중독되지 않으시기를, 행운을 빕니다." if dobak==True else "")    # 연패중이라면 중독 우려 대사 출력
        print(f"\n\n게임을 시작합니다! \n게임 머니 : {game_money}")                # 게임 시작 알림
    # 설명 선택
    elif get_input in ["e", "E", "ㄷ"]:   
        print(explains, end=" : ")
        # 설명 끝, 다시 시작 여부 질문
        new_input = input()
        if new_input in ["예", "Yes", "Y", "네", "y"]:
            game_money -= game_cost # 참여금 + 상금 // 연승 참여금 
            print(f"게임 머니 : {game_money}")
    # 게임 시작 X
    else:   
        print("취향이 아니신가 보군요. 다음에는 더 재미있는 게임으로 찾아뵙겠습니다.")
        break


    # !!!!!!!!!!!!!!!! 본 게임 시작!!!!!!!!!!!!!!!
    # 첫 카드 2개 뽑고 - 딜러 카드는 안보여주는 상태에서 카드 상태 출력 - 첫 카드에서 버스트 발생 유무 체크.
    get_first_card()
    show_card(deal)
    over_check()    # 체크 후 check 반환
    if check == 0:  # check 가 0이면 플레이어와 딜러, 둘 다 21 이하라는 뜻.
        pass
    # 첫 카드뽑기에서 22 이상 나올 수 없으므로 21 언더 or 힛만 취급.
    elif check == "플 힛":
        print(f"플레이어 힛, 승리! 시작이 좋군요. 오늘은 북적거리는 하루가 될 것 같습니다.")
        game_money += game_cost*5
        win += 1
        lose = 0
    elif check == "딜 힛":
        deal = False
        show_card(deal)
        print(f"첫 턴에 딜러의 점수가 21? 시작부터 운이 좋지 않으시군요. 유감입니다.")
        lose += 1
    else:
        print(f"오류 발생.")
        break


    
    regame = True
    ## 처음 2개의 카드 뽑은 후, 힛, 버스트 체크 완료 // 플레이어의 카드 추가 뽑기 선택
    while check == 0:   ## 카드 뽑기 진행 도중 힛, 버스트 발생 시 check값 변동. while 중단.
        more_card = input("카드를 더 받으시겠습니까? (y/n) : ")

        print("\n\n\n\n\n") # 화면 정리용
        # 카드를 더 받겠다. -> 플레이어의 카드에만 변동 있음.
        if more_card in ["Y", "y", "네", "예"]:
            play_get_card()
            show_card(deal) # 아직 딜러 카드 숨기기 True
            check = over_check()# 체크 후 check 반환
            # 플레이어 숫자 21 이하
            if check == 0:
                pass
            elif check == "플 21 초과":
                if play_sum(player_card) > 17:
                    print(f"이전 숫자도 충분히 높았는데... 선택이 아쉽군요. 패배입니다.")
                else:
                    print(f"패배... 숫자가 애매하긴 했지요. 저 같아도 카드를 한 장 더 뽑기는 했을 겁니다.")
                lose += 1
            elif check == "플 힛":
                print(f"축하드립니다 이기셨군요. 하하, 긴장하지 않으면 큰일나겠군요. 힛으로 승리 시 게임 금액을 4배를 더 받을 수 있지요.")
                if win > 0:
                    print(f"...이런 연승중이셨지요? 오늘은... 이만 영업을 종료해야할지도 모르겠습니다.")
                game_money += game_cost*4
                # 1연승이면 1000원 주고 0원 상태에서 힛,  1000원 3배 3000, 연승 시 2000, 2배로 돌려줌.
                win += 1
                lose = 0
            else:
                print(f"오류 발생.")
                break
            # 플레이어 숫자 21 초과
            if not check == 0:  # 딜러와 플레이어 중 한 사람이라도 21을 달성했거나 22를 초과했으므로 게임 끝. continue로 while 시작점 복귀
                if game_money <= 0:
                    print("저희가 제공해드린 기본 머니를 다 사용하셨군요. 소유하신 것이라도 처분해 새로운 머니를 마련해보시겠습니까?\n진심이시라면 이곳을 나가 10분 거리에 중고물품 판매장이 있습니다.\n오, 도박장 근처에 기생하는 곳인 만큼 값을 후하게 주지는 않으니 기대 마시기를.")
                    break   # 카드 21 이하면 추가 카드 뽑기 while문 break
                else:
                    print(f"현재 게임머니 : {game_money}, 크다면 큰 금액이기는 하지요. 더 불려보시겠습니까?", end=" ")
                    new_game_question = input()
                    if not new_game_question in ["y", "Y"]:
                        print("즐거운 시간이었기를")
                        regame = False  # 다시 게임 안함. 2번째 while문이 아닌 첫 while 스탑용 bool 변수
                        break
                    else:
                        print("\n\n\n\n\n\n\n\n") # 화면 정리용
                        continue
            # 플레이어 카드 21이면 그대로 계속 Pass       
                  
        # 카드 더 안받겟다고 하면 딜러 카드 받고 공개.
        elif more_card in ["n"]:
                dealer_ger_card()
                deal = False    # 이제 카드 보여줄거니까 False로 변경
                show_card(deal) # 딜러 카드 다 받음.
                check = over_check()# 체크 후 check 반환
                # 플레이어 카드는 체크 완료
                if check == 0:
                    break
                    # 적은 수에서 멈추면 계속 카드 뽑겟냐고 묻는다. check == 0은 둘다 21 미만의 안전ㅅ ㅜ의미.
                elif check == "딜 21 초과":
                    print(f"딜러의 욕심이 과했군요. 당신의 승리입니다.")
                    game_money += game_cost*2
                    win += 1
                    lose = 0
                    print("다시 돌아올 행운을 위해, 게임을 더 하시는 것은 어떻습니까? (y/n)", end=" ")
                    new_game_question = input()
                    if not new_game_question in ["y", "Y"]:
                        print("즐거운 시간이었기를")
                        break # game = False
                    else:
                        print("\n\n\n")
                        continue
                elif check == "딜 힛":
                    print(f"딜러의 점수가 21. 게임의 룰은 잘 기억하시죠? 졌습니다")
                    lose += 1
                    # 졌음. 게임 머니 있을 시 새로운 게임 할지말지 선택
                    if game_money <= 0:
                        print("게임머니가 없으시군요. 추가적으로 머니를 구매하실 생각이 아니시라면 그만 나가주십시오. 손님으로서의 예우는 여기까지입니다. 그럼, 다음에 뵙겠습니다.")
                        break
                    else:
                        print(f"한 판 더 어떠신가요? 혹시 모르죠, 이번에는 당신이 힛이 나올지. (y/n) \n현재 게임머니 : {game_money}", end=" ")
                        new_game_question = input()
                        if not new_game_question in ["y", "Y"]:
                            print("즐거운 시간이었기를")
                            break
                else:
                    print(f"오류 발생.")
                    break

                


                

    if regame == False: # 카드 받다가 게임 종료 후 1차 while까지 종료 시키는 용
        break
    
    # 플레이어와 딜러, 둘다 21 이하 일 시 둘 중에 수가 더 큰 사람의 승리.
    if play_sum(player_card) > deal_sum(dealer_card) and check == 0:
        game_money += game_cost*2     
        print(f"Player 승리!")
        print(f"종종 초기 금액의 10배를 가져가시는 분이 계시죠. 그런 승리자가 되어보시겠습니까? : {game_money}", end=" ")
        new_game_question = input() # 플레이어 승리 후 연승 게임 도전 선택지
        if new_game_question in ["y", "Y"]:
            print("\n\n\n")         # 화면 정리용\
            continue
        else:
            print("즐거웠습니다. 다음에 또 뵐 수 있으면 좋겠군요.")
            break 
    
    # 딜러 승리
    elif play_sum(player_card) < deal_sum(dealer_card) and check == 0:
        print(f"Dealer 승리! \n게임 머니를 잃었습니다. 현재 게임 머니 : {game_money}")
        win = 0
        lose += 1
        if game_money <= 0:
            print("저희가 제공해드린 기본 머니를 다 사용하셨군요. 소유하신 것이라도 처분해 새로운 머니를 마련해보시겠습니까?\n음, 농담이었는데 말이죠. 너무 진지하게 받아들이지 마십시오.\n... 도박 중독 치료센터의 전화번호는 1336입니다. 외우시죠.")
            break
        else:
            print(f"새로운 게임을 시작하시겠습니까?  현재 게임머니 : {game_money}", end=" ")
            new_game_question = input()
            if not new_game_question in ["y", "Y"]:
                print("의욕을 잃으신겁니까? 아쉽군요. 다음을 기약하겠습니다.")
                break
    # 동점
    elif play_sum(player_card) == deal_sum(dealer_card) and check == 0:
        game_money += game_cost
        print(f"동점!")
        print(f"본전이라니, 흔치 않은 경우이지요. 다시 승부를 겨뤄보시겠습니까? 현재 게임머니 : {game_money}", end=" ")
        new_game_question = input()
        if not new_game_question in ["y", "Y"]:
            print("오, 우린 꽤 잘 맞는다고 생각했는데 말이죠. 저만 기대했다니 무척 아쉽습니다.")
            break
        else:
            print("\n\n\n")
            continue

    
    



            





    



"""
        ┌───┐
딜러 :   │   │
        └───┘
"""


"""
딕셔너리변수[키값] : 해당 키 값에 해당하는 value값 조회
(에러O)딕셔너리변수.get(키값) : 해당 키 값에 해당하는 value값 조회
(에러X)딕셔너리변수[키값] = vlaue값 : 변수 내 키+value값 추가
출처: https://secuinfo.tistory.com/entry/Python-basic-주요-딕셔너리-메소드 [Song's Lab:티스토리]
"""




# 요소 추가 insert(인덱스, 데이터) // append(데이터)