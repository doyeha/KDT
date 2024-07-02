"""
https://hello-bryan.tistory.com/187
"""
import pygame
import cv2
import numpy as np
import sys
    
def loadImageFromPath(imgPath):
    try:
        # gif 처리
        if str(imgPath).lower().endswith('.gif'):
            gif = cv2.VideoCapture(imgPath)
            ret, frame = gif.read()  # ret=True if it finds a frame else False.
            if ret:
                return frame
            else:
                return cv2.imread(imgPath)
    except Exception as e:
        print(e)
        return None
    

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

while True:
    #이벤트 확인하기 
    for event in pygame.event.get():
        #닫기 버튼을 눌렀는지

        if event.type == pygame.QUIT:
            #게임 끝내기
            pygame.quit()
            sys.exit()
    gif = cv2.VideoCapture("C:\Git\KDT\BigData\Project\solo_image\gif_test.gif")
    ret, frame = gif.read()  # ret=True if it finds a frame else False.
    while ret:
	# something to do 'frame'
    # ...
    # 다음 frame 읽음
        ret, frame = gif.read()


    #화면 업데이트하기
    pygame.display.update()
"""
import pygame
import os
from PIL import Image
from IPython.display import Image as Img
from IPython.display import display

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

def generate_gif(path):
    img_list = os.listdir(path)
    img_list = [path + '/' + x for x in img_list]
    images = [pygame.image.load(x) for x in img_list]
    
    im = images[0]
    im.save('out.gif', save_all=True, append_images=images[1:],loop=0xff, duration=500)
    # loop 반복 횟수
    # duration 프레임 전환 속도 (500 = 0.5초)
    return Img(url='out.gif')


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
    generate_gif("C:\Git\KDT\BigData\Project\solo_image\gif_test.gif")

image_giftest = [pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0000.jpg'),
                 pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0001.jpg'),
                 pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0002.jpg'),
                 pygame.image.load('C:\Git\KDT\BigData\Project\solo_image\iloveimg-converted\gif_test-0002.jpg')]


                 """