from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
import sys
from time import sleep
import threading
import cv2
import numpy as np
import datetime as dt
from PyQt5.QtCore import (QThread,pyqtSignal)  # 영상 처리 멀티스레드 // 메인스레드 - 영상용 스레드 신호 연결 목적
from PyQt5 import QtWidgets, QtGui, QtCore
import os, datetime  # 영상 정보 띄우기 목적, datetime
from PyQt5.QtCore import Qt
from collections import deque 
import warnings
warnings.simplefilter("ignore", DeprecationWarning) # deprecated 오류메세지 ignore 목적


class frame_saver(QThread):
    def __init__(self, singal):
        super().__init__()
        self.signal = singal
        self.background_queue = deque(maxlen=300)
        self.after_queue = deque(maxlen=300)
        self.dupl_queu = deque(maxlen=300)
        self.lock = threading.Lock()
        self.video_saver = video_saver(self.signal, self.lock, self.background_queue, self.after_queue)
        self.running = False
        
        self.acci_cnt = 1
        self.fps = 0
        self.current_time = 0
        self.length = 0
        self.playing_frame = None

        self.rect, self.accident= None, None
        self.savering = False


    def accident_receiver(self, rect, accident):
        self.rect = rect
        print("로그비디오에서 로그 발생 인식 rect: ", self.rect, "self.accident :", self.accident) 
        self.accident = accident
        if self.acci_cnt <= 3:
            self.acci_cnt += 1
        self.running = True
        if ((self.accident =="car") or (self.accident =="reck")) and not self.savering:
            # self.saver()
            self.video_saver.start()


    def pixmap_to_numpy(self, pixmap):
        qimage = pixmap.toImage()
        qimage = qimage.convertToFormat(QImage.Format.Format_RGB888)  # RGB888 포맷 변환

        width = qimage.width()         # 실제 이미지 너비
        height = qimage.height()       # 실제 이미지 높이
        bytes_per_line = qimage.bytesPerLine()  # 한 줄당 총 바이트 수

        # 데이터 포인터를 가져와 numpy 배열로 변환
        ptr = qimage.bits()
        ptr.setsize(qimage.byteCount())  # 전체 바이트 수를 설정

        # reshape 시 bytes_per_line을 활용하여 배열 생성
        arr = np.array(ptr, dtype=np.uint8).reshape((height, bytes_per_line))

        # 마지막으로 필요 없는 패딩을 잘라내어 실제 이미지 데이터만 사용
        arr = arr[:, :width * 3].reshape((height, width, 3))
        
        return arr


    def numpy_to_pixmap(self, array):
        height, width, channel = array.shape
        bytes_per_line = 3 * width
        qimage = QImage(array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(qimage)
    
    
    def on_pixmap_received(self, pixmap):
        # Step 1: QPixmap → NumPy 배열
        frame = self.pixmap_to_numpy(pixmap)

        # Step 2: NumPy 배열 리사이즈 (예: 640x360으로 축소)
        resized_frame = cv2.resize(frame, (640, 360), interpolation=cv2.INTER_LINEAR)

        # Step 3: NumPy 배열 → QPixmap
        resized_pixmap = self.numpy_to_pixmap(resized_frame)
        self.background_queue.append(resized_pixmap)
        # print("백그라운드 저장", len(self.background_queue))

    def save_pixmap(self, pixmap):
        frame = self.pixmap_to_numpy(pixmap)
        # Step 2: NumPy 배열 리사이즈 (예: 640x360으로 축소)
        resized_frame = cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_LINEAR)
        # Step 3: NumPy 배열 → QPixmap
        # resized_pixmap = self.numpy_to_pixmap(resized_frame)
        return resized_frame

    ###########################################################


    def run(self):
        self.signal.pixmap_signal.connect(self.on_pixmap_received)  # 얘는 무한으로 계속 저장해야하는디.
        self.signal.pixmap_signal.connect(self.after_queue_go)
        self.signal.aci_info_signal.connect(self.accident_receiver)   # 렉 번호랑 사고 정보 받아온. int str 

                          
    # 로그 발생 시, 로그 발생 후의 pixmap을 저장해야함.
    def after_queue_go(self, pixmap):
        if self.running and (len(self.after_queue)<=300):
            self.after_queue.append(pixmap)


    


class video_saver(QThread):
    def __init__(self, signal, lock, background_queue, after_queue):
        super().__init__()
        self.signal = signal
        self.lock = lock
        self.background_queue = background_queue
        self.after_queue = after_queue
        self.save_time = 0

    def run(self): # 시그널이 올때마다 acci_cnt가 실시간 변동되어야함.
        save_directory = './log_video/'
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        filename = os.path.join(save_directory, f"test_{dt.datetime.now().strftime('%m%d_%H%M%S')}.mp4")
        self.savering = True
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        bad_try = 0
        fps = 30
        out = cv2.VideoWriter(filename, self.fourcc, fps, (1920, 1080))

        while self.save_time <= 300 or (self.save_time <= len(self.background_queue)):
            print("saver 이전 10초 작동중", self.save_time,"/",300)
            if self.background_queue:
                # print("저장저장저장")
                pic = self.background_queue.popleft()
                pic = self.save_pixmap(pic)
                out.write(pic)
                self.save_time += 1
            else:
                if bad_try == 30:
                    break
                bad_try += 1
                print(bad_try)
        # 이후 10초 
        self.save_time = 0
        bad_try = 0
        while self.save_time <= 300 or (self.save_time <= len(self.after_queue)):
            print("saver 이후 10초 작동중", self.save_time,"/",300)
            if self.after_queue:
                # print("저장저장저장")
                pic = self.after_queue.popleft()
                pic = self.save_pixmap(pic)
                out.write(pic)
                self.save_time += 1
            else:
                if bad_try == 30:
                    break
                bad_try += 1
                print(bad_try)
        out.release()

            
    def pixmap_to_numpy(self, pixmap):
        qimage = pixmap.toImage()
        qimage = qimage.convertToFormat(QImage.Format.Format_RGB888)  # RGB888 포맷 변환

        width = qimage.width()         # 실제 이미지 너비
        height = qimage.height()       # 실제 이미지 높이
        bytes_per_line = qimage.bytesPerLine()  # 한 줄당 총 바이트 수

        # 데이터 포인터를 가져와 numpy 배열로 변환
        ptr = qimage.bits()
        ptr.setsize(qimage.byteCount())  # 전체 바이트 수를 설정

        # reshape 시 bytes_per_line을 활용하여 배열 생성
        # bytes_per_line 이게 뭔가 새꺄 .... 
        arr = np.array(ptr, dtype=np.uint8).reshape((height, bytes_per_line))

        # 마지막으로 필요 없는 패딩을 잘라내어 실제 이미지 데이터만 사용
        arr = arr[:, :width * 3].reshape((height, width, 3))
        return arr


    def numpy_to_pixmap(self, array):
        height, width, channel = array.shape
        bytes_per_line = 3 * width
        qimage = QImage(array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(qimage)
    
    
    def on_pixmap_received(self, pixmap):
        # Step 1: QPixmap → NumPy 배열
        frame = self.pixmap_to_numpy(pixmap)
        # Step 2: NumPy 배열 리사이즈 (예: 640x360으로 축소)
        resized_frame = cv2.resize(frame, (640, 360), interpolation=cv2.INTER_LINEAR)
        resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        # Step 3: NumPy 배열 → QPixmap
        resized_pixmap = self.numpy_to_pixmap(resized_frame)
        self.background_queue.append(resized_pixmap)
        print("백그라운드 저장", len(self.background_queue))

    def save_pixmap(self, pixmap):
        frame = self.pixmap_to_numpy(pixmap)
        # Step 2: NumPy 배열 리사이즈 (예: 640x360으로 축소)
        
        resized_frame = cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_LINEAR)
        resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        # Step 3: NumPy 배열 → QPixmap
        # resized_pixmap = self.numpy_to_pixmap(resized_frame)
        return resized_frame