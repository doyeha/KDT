import pygame
import random
import math
import time
import datetime
import sys
"""
https://wondangcom.tistory.com/2597
"""

pygame.init()       # 모듈 초기화
screen = pygame.display.set_mode((1280,720))        # 화면 생성, 크기
pygame.display.set_caption("pygame test")           # 게임 창 제목
background = pygame.display.set_mode((1280,720))    # 배경 크기
screen.fill((0,0,0))                                 #배경색상 설정하기
clock = pygame.time.Clock()         # 프레임 속도 제어를 위한 Clock 객체를 생성합니다.


clock.tick(60)      #프레임 레이트 설정하기




pygame.display.update()     #화면 업데이트하기

#이미지 경로
# pygame.image.load('')
image_posX = 500
image_posY = 100

image_textbox = pygame.image.load('C:\\Git\\KDT\\BigData\\Project\\solo_image\\Textbox.png')

image_giftest = [pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0000.jpg'),
                 pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0001.jpg'),
                 pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0002.jpg'),
                 pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0002.jpg')]

clock = pygame.time.Clock()

# image_bg = pygame.image.load('./image/stadium.png')
myFont = pygame.font.SysFont("malgungothic", 50) #(글자체, 글자크기) None=기본글자체

# 이미지 정리
def clear_screen():
    screen.fill((0, 0, 0))



# 게임 루프
running = True
current_image = 0
frame_rate = 1 / 0.3  # 초당 프레임 수 (1초 간격)
last_frame_time = time.time()






while True:
    #이벤트 확인하기 
    for event in pygame.event.get():
        #닫기 버튼을 눌렀는지
        if event.type == pygame.QUIT:
            #게임 끝내기
            pygame.quit()
            sys.exit()


    #화면 업데이트하기
    pygame.display.update()

    current_time = time.time()
    if current_time - last_frame_time >= 1 / frame_rate:
        clear_screen()  # 화면 지우기
        screen.blit(image_giftest[current_image], (500, 200))  # 이미지 출력
        pygame.display.flip()  # 화면 업데이트

        # 다음 이미지로 넘어가기
        current_image = (current_image + 1) % len(image_giftest)
        last_frame_time = current_time



    background.blit(image_textbox, (0,0))
    myText = myFont.render("테스트 테스트.", True, (255,255,255)) #(Text,anti-alias, color)
    background.blit(myText, (100,10)) #(글자변수, 위치(「 기준 가로,세로))
# 3초 뒤 다음 텍스트 넘어가기

    #프레임 레이트 설정하기




"""
1. 주사위 클래스 (1~4 or 1~6)
2. 대사 박스, 출력 클래스
3. @Override 대사 - 선택지 박스 (2~3개 해야함.)


"""



""" 3

선택지 주사위. 1~6 사망 원인 랜덤
if 주사위 1. 범죄자 
 도망쳐! 잡히면 사망
 선택지 1 2 3 
    1. 넌센스 퀴즈풀어야함 
    2. 유령엔딩 
    3. 스스로 지옥문 평생 노역  (지옥문 사진, Bad Ending 01)

주사위 2~3. 우연한 사고 (약간의 측은, 일반 엔딩)
  코코 : 저런 사고로 죽으셧군요. 축하드립니다! 당신은 저희 환생써비스(베타.. 소곤)에 응모하실 자격이 충분하시군요.
   어쩌고 저쩌고 암튼 환생 ㄱ!
    선택 1.
        싫다. -> 코코 설득 -> 다시 선택지 -> 응 그래도 보낼거야! -> ??? -> 선택권이 없어 랜덤으로 환생 (Normal Ending)
    선택 2.
        좋아. -> 희망 세계라도 있으신가요.
        
         1. 무협
            주사위
            1~2. 엄청 쎈 놈
            3~4. 평범한 상인
            5~6. 거지
        선택지 2. 로맨스
            주사위
            1~2. 성공적인 주인공
            3~4. 조연
            5~6. 이름 없는 엑스트라로 그저 그렇게 살아갑니다...
        선택지 3. 아포칼립스
            주사위
            1. 좀비가 되었습니다.
            2. 전쟁중 
            3. 살아남은 영웅
            4. 멸망 후 혼자 남은 생존자
            5. 아포칼립스를 일으킨 원인, 모두의 적대감을 얻습니다.
            6. 인류의 마지막 희망.


주사위 4. 과로사 (대사 조금 더 따뜻)


주사위 ~6. 억울한 죽음 (대사 조금 더 따뜻)
 




"""
 
"""



https://wondangcom.tistory.com/2597?pidx=1
pygame.QUIT 윈도우 x버튼, 창닫기 버튼

pygame.ACTIVEEVENT
 gain 0 마우스 화면 들어옴
 gain 1 마우 화면 밖

 state 1 창이 활성화
 satae 2 창 비활성화
 state 6 비활성화된 다시 활성화

 pygame.KEYDOWN 키가 눌렸을때.
 pygame.KEYUP 키가 올라갔을때

 pygame.MOUSEMOTION 마우스 움직임
 pygame.MOUSEBUTTONUP 뗄때
 pygame.MOUSEBUTTONDOWN 눌렀을때



"""