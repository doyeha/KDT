import pygame
from PIL import Image

""" 기본 설정"""
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame GIF Example')

WHITE = (255, 255, 255) # 색상 정의

""" 단순 부르기 """

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
frame_duration = 50  # 각 프레임의 지속 시간 (밀리초 단위)
last_update = pygame.time.get_ticks()

""" 클릭 이벤트 """
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 시 위치 변경
            x, y = event.pos
##==================================================================

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 시간 업데이트
    now = pygame.time.get_ticks()
    # 프레임 업데이트
    if now - last_update > frame_duration:
        current_frame = (current_frame + 1) % len(frames)
        last_update = now
    # 화면 채우기
    screen.fill(WHITE)
    # 현재 프레임 그리기
    screen.blit(frames[current_frame], (100, 100))
    # 화면 업데이트
    pygame.display.flip()
    # 프레임 속도 제어
    clock.tick(60)

# 종료
pygame.quit()