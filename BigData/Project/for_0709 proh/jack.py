import random as rand
# 카드 덱, 튜플, 키로 뽑아져있는지 구분.
# 딜러 카드 안보이는 부분까지는 구현 완료.

card_deck = {
1:"01", 2:"01", 3:"01", 4:"01", 5:"01", 6:"01",   # 인덱스 0~5
7:"02", 8:"02", 9:"02", 10:"02", 11:"02",      # 인덱스 6~10
12:"03", 13:"03", 14:"03", 15:"03",         # 인덱스 11~14
16:"04", 17:"04", 18:"04",            # 인덱스 16~17
19:"05", 20:"05", 21:"05",            # 인덱스 18~20
22:"06", 23:"06",               # 인덱스 21 22
24:"07", 25:"07",               # 인덱스 23 24
26:"08", 27:"09", 28:"10", 29:"11", 30:"11"    # 인덱스 25 26 27 28 29 
}

"""
# card_deck = {
# 1:"01", 2:"01", 3:"01", 4:"01", 5:"01", 6:"01",   # 인덱스 0~5
# 7:"02", 8:"02", 9:"02", 10:"02", 11:"02",      # 인덱스 6~10
# 12:"03", 13:"03", 14:"03", 15:3,         # 인덱스 11~14
# 16:4, 17:4, 18:4,            # 인덱스 16~17
# 19:5, 20:5, 21:5,            # 인덱스 18~20
# 22:6, 23:6,               # 인덱스 21 22
# 24:7, 25:7,               # 인덱스 23 24
# 26:8, 27:9, 28:10, 29:11, 30:11    # 인덱스 25 26 27 28 29 
# }
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

def dealer_ger_card() : # 플레이어가 카드 받기를 종료한 후, 딜러 또한 카드를 차례차례 받는 것.
    return 0

def play_sum(player_card):
    play_sum = 0
    for i in player_card:   
         for i in i.values():
             i = int(i)
             play_sum += i
    return play_sum

def deal_sum(dealer_card):
    deal_sum = 0
    for i in dealer_card:   
         for i in i.values():
             i = int(i)
             deal_sum += i
    return deal_sum

def show_card():         # 카드 딜러: 당신 : 카드 형으로 출력 완.
    # 딜러 - - - - - - - - - - - - - - - - - - - - - - - - - -  
    # 첫줄
    for i in range(len(dealer_card)):   
        if i == 0: print(f"            ┌────┐", end="")
        else: print(f" ┌────┐", end=" ")
    # 둘째줄
    print(f"\n딜러 {play_sum(dealer_card):>2}점 :", end= " ")
    for i in dealer_card:   
        for i in i.values():
            print(f"│ {i} │", end=" ")
    # 셋째 줄
    print()
    for i in range(len(dealer_card)):
        if i == 0: print(f"            └────┘", end="")
        else: print(f" └────┘", end="   ")


    ## 플레이어 - - - - - - - - - - - - - - - - - - - - - - - - - -    
    print()
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
    # print(dealer_card)  #난.. 값만 보여주고 싶어 ...
    # print(player_card.values())

    # 값

explains = """
이 게임은 카드를 뽑아 그 수의 합이 21을 넘지 않되 21에 가장 근접하는 사람이 이기는 게임입니다.
딜러와 당신에게 각각 2장의 카드가 주어지고, 당신의 선택에 따라 카드를 한 장씩 더 받을 수 있습니다.
딜러의 카드는 당신이 더 이상 카드를 받겠다고 했을 때, 마지막에 공개됩니다.

카드를 새로이 받다가 21이 넘는 순간 당신의 패배이니 조심하시기를!

그럼, 게임을 시작하시겠습니까?
"""

def over_check():  # 합산으로 21 넘는 지 체크, 플레이어가 넘으면 1 / 딜러가 넘으면 2 / 0은 깔끔
    if play_sum(player_card) > 22:     
        # print(f"플레이어 버스트! 패배 하셨습니다.")
        if play_sum(player_card) == 21:
            return 3
        return 1      
    if deal_sum(dealer_card) > 22:
        # print(f"딜러 버스트! 승리하셧습니다.")
        if play_sum(dealer_card) == 21:
            return 4
        return 2
    
    if deal_sum(dealer_card) < 21 and play_sum(player_card) < 21:
        return 0 


game_money = 1000
## main
while True:
    check = 0
    dealer_card = []    # 딜러 현재 카드 덱
    player_card = []    # 플레이어 현재 카드 덱
    print(f"현재 게임 머니 : {game_money}")
    print("시작하시겠습니까? 한 게임 당 게임 머니 500이 소모됩니다.")
    get_input = input("시작하시려면 y를, 게임 설명을 원하신다면 e를 입력해주세요. : ")
    
    if get_input in ["예", "Yes", "Y", "네", "y"]:
        game_money -= 500
        print(f"게임 머니 : {game_money}")
    elif get_input in ["e", "E"]:
        print(explains, end=" : ")
        new_input = input()
        if new_input in ["예", "Yes", "Y", "네", "y"]:
            game_money -= 500
            print(f"게임 머니 : {game_money}")
    else:   # 첫 화면 게임 x 선택지
        print("다음에 뵙겠습니다.")
        break
        
    get_first_card()
    show_card()
    over_check()    # 체크 후 check 반환

    if check == 0:  # func 하기엔 continue 걸림.
        pass
    elif check == 1:
        print(f"플레이어 버스트! 패배 하셨습니다.")
        game_money -= 500
        continue
    elif check == 2:
        print(f"딜러 버스트! 승리하셧습니다.")
        game_money += 500
        continue
    else:
        print(f"오류 발생.")
        break
  
    while check == 0: # 카드 더 받는가. 근데, over체크에서 아무도 over안해야함.
        more_card = input("카드를 더 받으시겠습니까?")
        if more_card in ["Y", "y", "네", "예"]:
            play_get_card()
            show_card()
            check = over_check()# 체크 후 check 반환
            if check == 0:  # func 하기엔 continue 걸림.
                pass
            elif check == 1:
                print(f"플레이어 버스트! 패배 하셨습니다.")
                game_money -= 500
                continue
            elif check == 2:
                print(f"딜러 버스트! 승리하셧습니다.")
                game_money += 500
                continue
            elif check == 3:
                print(f"Wow 21! 플레이어 승리!")
                game_money += 500
                continue
            elif check == 4:
                print(f"딜러의 점수가 21? 아쉽게도 당신은 패배했습니다.")
                game_money += 500
                continue
            else:
                print(f"오류 발생.")
                break
        elif more_card in ["n"]:
                break # game = False
            
    if play_sum(player_card) > deal_sum(dealer_card) and check == 0:
        game_money += 1000        
        print(f"Play 승리! 게임머니 : {game_money}")
        print("더 즐기시겠습니까?")
        new_game_question = input()
        if new_game_question in ["y", "Y"]:
            continue
        else:
            print("즐거운 시간이었기를")
            break # game = False
    else:
        print(f"Dealer 승리! 게임머니 : {game_money}")
        print("더 즐기시겠습니까?")
        new_game_question = input()
        if not new_game_question in ["y", "Y"]:
            print("즐거운 시간이었기를")
            break # game = False
            
        else:
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