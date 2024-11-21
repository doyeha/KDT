import random as rand
KDT_member = ["박란영", "조혜리", "전민규", "안효준", "김경태", "김태헌", "구성윤", "황은혁", "김경환", "곽경민", "김재성", "도영훈", "한세진", "이민하", "장재웅", "이현종", "박형준", "손지원", "황지원", "김환선", "김민석", "이동건", "김영주", "안윤호", "김미소", "김아란", "김도연", "권도운", "김이현", "김현주","이송은","박지훈"]
Team_log = {
"박란영":[], "조혜리":[], "전민규":[], "안효준":[], "김경태":[],  
"김태헌":[], "구성윤":[], "황은혁":[], "김경환":[], "곽경민":[], "김재성":[], "도영훈":[],
"한세진":[], "이민하":[], "장재웅":[], "이현종":[], "박형준":[], "손지원":[], "황지원":[],
"김환선":[], "김민석":[], "이동건":[], "김영주":[], "안윤호":[], "김미소":[], "김아란":[],
"김도연":[], "권도운":[], "김이현":[], "김현주":[], "이송은":[], "박지훈":[]
}


Team1 = []    # 각 조 리스트
Team2 = []    
Team3 = []
Team4 = []
Team5 = []
Team6 = []
Team7 = []
Team8 = []

AllTeam = [Team1, Team2, Team3,Team4,Team5,Team6,Team7,Team8]

# 멤버 리스트에서 랜덤 뽑고 그 사람의 팀 로그를 수정한다.


def picked_member():    # 각 팀에 4명씩 뽑아서 각 팀에 넣음. 리스트 형식으로 넣고, 그걸 다시 리스트에 묶어두엇다.
     for i in AllTeam:
        while len(i)<4:
            picked_member = rand.choice(KDT_member)
            
            # print(f"1번 카드 {card}")
            if check_Team(picked_member) == True:
                    i.append(picked_member)
              # 이름 리스트에 랜덤 뽑기.

def check_Team(picked_member): # 이미 뽑힌 조원인지 확인
    if picked_member not in AllTeam: # 1~8조를 묶은 "팀" 자체에 있는지 확인
        return True
    else:
        return False
    
def Team_log_in(picked_member):
     if picked_member in Team1:
          Team_log[picked_member].update([1])
          
     


# if check_Team(picked_member()):
#     Teamed_list = Team_log[picked_member]   # 뽑힌 사람의 팀 이력
#     print(Teamed_list)
    
# picked_member()
# for i in AllTeam:
#      for t in i:
#         print(f"{i}의 {t}", end=" ")
#         print()

    
