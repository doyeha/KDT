import pygame
import random
import math
import time
import datetime
"""
https://wondangcom.tistory.com/2597
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
        
    image_giftest0
    image_giftest1
    image_giftest2
    


    #화면 업데이트하기
    pygame.display.update()