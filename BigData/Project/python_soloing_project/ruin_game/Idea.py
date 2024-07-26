"""
# 끝말잇기 게임
 사전 검색 or 크롤링해서 자체 사전 제작?


# 


# 정보 취합 및 통계내주는 프로그램
# 저장형식
# 캐릭터
#  API 정보 받아오기    - 직업 (42중 1개 고정), 투력(int), 
#  외부사이트 활용      - 환산투력(int)
#  통계 및 취합 데이터  - 점수(직업 별 & 투력 대비 연관)

딕셔너리로 키 : 값 
 닉네임 : 고유난수 (영어 소문자 대문자 & 숫자 섞어서 고유 번호 부여)
 랜덤으로 숫자 뽑아서 20자리 발행, 일부 난수 20 이하 랜덤 뽑아서 해당 수 만큼 일부 숫자 영문으로 변경.
 나온 값 다른 고유난수와 비교하여 존재하는지 확인.
   ex) 12345678900000000000 나오면 rand() if 9?
       aefasdfgw00000000000 이런식으로.
       한번 더 꼬아서 이 중에 대문자로도 변경.
       아니면 20개 중 대문자 7개 rand 변경, 소문자 7개 rand 변경.

    새로운 요소 입력으로 해서 저장 필요.

"""
import random
# char = input("닉네임을 입력해주세요.")
# for i in range(1,7):
#     rand_num = random.randint

# 1~6 랜덤 
Dice = random.randint(1,6)

print(Dice)





# 글자체(text font) 지정하기
myFont = pygame.font.SysFont(None, 50) #(글자체, 글자크기) None=기본글자체
myText = myFont.render("Hello World " + str(x_pos), True, (0,0,255)) #(Text,anti-alias, color)