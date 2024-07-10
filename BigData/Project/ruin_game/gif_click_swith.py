import pygame
from PIL import Image

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame GIF Example with Click Event')

# GIF 파일 불러오기
gif = Image.open('C:\Git\KDT\BigData\Project\ruin_game\solo_image\Dice.gif')
frames = []
for frame in range(gif.n_frames):
    gif.seek(frame)
    frame_image = gif.convert('RGBA')
    mode = frame_image.mode
    size = frame_image.size
    data = frame_image.tobytes()
    frames.append(pygame.image.fromstring(data, size, mode))

# 애니메이션 관련 설정
current_frame = 0
frame_duration = 100  # 각 프레임의 지속 시간 (밀리초 단위)
last_update = pygame.time.get_ticks()

# 초기 위치 설정
x, y = 100, 100

# 색상 정의
WHITE = (255, 255, 255)

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 시 위치 변경, 화면 내 제한x 상태.
            x, y = event.pos 

    # 시간 업데이트
    now = pygame.time.get_ticks()

    # 프레임 업데이트
    if now - last_update > frame_duration:
        current_frame = (current_frame + 1) % len(frames)
        last_update = now

    # 화면 채우기
    screen.fill(WHITE)

    # 현재 프레임 그리기
    screen.blit(frames[current_frame], (x, y))

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    clock.tick(60)

# 종료
pygame.quit()


"""
import pygame
import random
import math
import time
import datetime
import sys
"""
#https://wondangcom.tistory.com/2597
"""

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("pygame test")

#프레임 매니저 초기화하기
clock = pygame.time.Clock()

#프레임 레이트 설정하기
clock.tick(60)

#배경색상, 크기 설정하기
screen.fill((0,0,0))
background = pygame.display.set_mode((1280,720))

#화면 업데이트하기
pygame.display.update()

#이미지 경로
# pygame.image.load('')
image_giftest0 = pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0000.jpg')
image_giftest1 = pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0001.jpg')
image_giftest2 = pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0002.jpg')
image_giftest3 = pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0002.jpg')

clock = pygame.time.Clock()

# image_bg = pygame.image.load('./image/stadium.png')
myFont = pygame.font.SysFont("malgungothic", 50) #(글자체, 글자크기) None=기본글자체

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
    background.blit(image_giftest0,(500,100))
    
    image_giftest0
    image_giftest1
    image_giftest2
"""