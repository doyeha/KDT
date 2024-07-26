import pygame
import random
from PIL import Image
import time
# from load_image_def import loadImageFromPath

""" 기본 설정"""
pygame.init()
running = True
# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame GIF Example')
clock = pygame.time.Clock()         # 프레임 속도 제어를 위한 Clock 객체를 생성합니다.

clock.tick(60)      #프레임 레이트 설정하기
WHITE = (255, 255, 255) # 색상 정의

# image_bg = pygame.image.load('./image/stadium.png')
myFont = pygame.font.SysFont("malgungothic", 50) #(글자체, 글자크기) None=기본글자체


# 애니메이션 관련 설정
# def loadImage()
# current_frame = 0
# frame_duration = 50   # 각 프레임의 지속 시간 (밀리초 단위)
# last_update = pygame.time.get_ticks()
# screen = pygame.display.set_mode((800, 600))

def loadImageFromPath(imgPath):
    if str(imgPath).lower().endswith('.gif'):
        gif = Image.open(imgPath)
        frames = []
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = gif.convert('RGBA')
            mode = frame_image.mode
            size = frame_image.size
            data = frame_image.tobytes()
            frames.append(pygame.image.fromstring(data, size, mode))
        screen.blit(frames, (100, 100))
    else:
        None

# # GIF 파일 불러오기
# gif = Image.open('C:\Git\KDT\BigData\Project\solo_image\Dice.gif')
# frames = []
# for frame in range(gif.n_frames):
#     gif.seek(frame)
#     frame_image = gif.convert('RGBA')
#     mode = frame_image.mode
#     size = frame_image.size
#     data = frame_image.tobytes()
#     frames.append(pygame.image.fromstring(data, size, mode))

# Dice = random.randint(1,6)


pygame.display.update()     #화면 업데이트하기


# 게임 진행
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get(): # 게임 실행 도중 이벤트 인식
        if event.type == pygame.QUIT: # 게임 1차 실행 도중 x버튼 누르면
            running = False            # 종료.
        elif event.type == pygame.MOUSEBUTTONDOWN:   # 1차 실행에서 버튼 클릭 시
            loadImageFromPath('C:\Git\KDT\BigData\Project\solo_image\Dice.gif')
            # screen.blit(myText, (100,100)) #(글자변수, 위치(「 기준 가로,세로))
            print("1차 클릭 인식")
            for event in pygame.event.get(): 
                Dice=random.randint(1,6)   # 클릭 시 주사위 1~6 굴림.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("클릭 인식")
                    screen.fill(WHITE)
                    myText = myFont.render(f"{Dice}번이 나왔습니다.", True, (255,255,255)) #(Text,anti-alias, color)
                    
    # 시간 업데이트
    now = pygame.time.get_ticks()
    # 프레임 업데이트
    # if now - last_update > frame_duration:
    #     current_frame = (current_frame + 1) % len(frames)
    #     last_update = now
    # 화면 채우기
    screen.fill(WHITE)
    # 현재 프레임 그리기
    # screen.blit(frames[current_frame], (100, 100))
    # 화면 업데이트
    pygame.display.flip()
    # 프레임 속도 제어
    clock.tick(60)

# 종료
pygame.quit()