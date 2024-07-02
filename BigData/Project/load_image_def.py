import pygame
import random
from PIL import Image
import time


# def loadImageFromPath(imgPath):
#     try:
#         # gif 처리
#         if str(imgPath).lower().endswith('.gif'):
#             gif = cv2.VideoCapture(imgPath)
#             ret, frame = gif.read()  # ret=True if it finds a frame else False.
#             if ret:
#                 return frame
#             else:
#                 return cv2.imread(imgPath)
#     except Exception as e:
#         print(e)
#         return None

current_frame = 0
frame_duration = 50   # 각 프레임의 지속 시간 (밀리초 단위)
last_update = pygame.time.get_ticks()
screen = pygame.display.set_mode((800, 600))

def loadImageFromPath(imgPath):
    try:
        # gif 처리
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
            screen.blit(frames[current_frame], (100, 100))
    except Exception as e:
        print(e)
        return None