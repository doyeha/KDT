import pygame
import random
from PIL import Image

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame GIF Example with Click Event')

# GIF 파일 불러오기
gif = Image.open('C:\Git\KDT\BigData\Project\solo_image\Dice.gif')
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
BLACK = (0, 0, 0)

# 폰트 설정
myFont = pygame.font.SysFont('Arial', 36)

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 클릭 시 주사위 1~6 굴림
            Dice = random.randint(1, 6)
            print("클릭 인식")
            screen.fill(WHITE)
            myText = myFont.render(f"{Dice}번이 나왔습니다.", True, BLACK)  # (Text, anti-alias, color)
            screen.blit(myText, (100, 100))  # (글자변수, 위치(「 기준 가로, 세로))

    # 시간 업데이트
    now = pygame.time.get_ticks()

    # 프레임 업데이트
    if now - last_update > frame_duration:
        current_frame = (current_frame + 1) % len(frames)
        last_update = now

    # 현재 프레임 그리기 (초기 상태에서만 그림)
    if pygame.mouse.get_pressed()[0] == 0:
        screen.fill(WHITE)
        screen.blit(frames[current_frame], (x, y))

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    clock.tick(60)

# 종료
pygame.quit()