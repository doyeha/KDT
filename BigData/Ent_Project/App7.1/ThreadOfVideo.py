from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
import sys
import time, datetime

# 영상 관련 import
import cv2
from time import sleep
from PyQt5.QtCore import (
    QThread,
    pyqtSignal,
)  # 영상 처리 멀티스레드 // 메인스레드 - 영상용 스레드 신호 연결 목적
from PyQt5 import QtWidgets, QtGui, QtCore
import os, datetime  # 영상 정보 띄우기 목적, datetime
import threading
from collections import deque

from log_maker import ThreadOfLogMaker

## AR 모델 ##
from ultralytics import YOLO
#model ver 7
model=YOLO('best.pt')
## AR 모델 ##

# 디자인 qrc파일
# sys.path.append(r'C:\dlrj_rlaudwn\kdt\KDT-2\13.NEMO\APP\App6\resources')

# 현재 스크립트 파일의 경로
current_dir = os.path.dirname(os.path.realpath(__file__))
#print(current_dir)

# 현재 디렉토리에서 'resources' 폴더로 이동하는 상대 경로
resources_path = os.path.join(current_dir, 'resources')
#print(resources_path)

# 절대 경로로 변환
resources_path = os.path.abspath(resources_path)
#print(resources_path)

# sys.path에 추가
sys.path.append(resources_path)

from resources import *

form_class = uic.loadUiType("./ui/MainView.ui")[0]

# 여기에는 스레드 멈추고 일시정지하고 그러는 기능 밖에 없어. 두 클래스간 공유하느 ㄴ파라미터도 없다.
class ThreadOfVideo(QThread, form_class):
    # preview_pixmap_signal = pyqtSignal(QPixmap)

    def __init__(self, signal, video_file, video_frame):
        super().__init__()
        self.signal = signal
        # video_file, video_frame
        self.video_file = video_file
        self.video_frame = video_frame
        self.frame = None
        self.running = True  # 루프 상태 제어
        self.pause = False  # 일시정지 상태
        self.length, self.fps, self.current_time, self.current_time, self.now_frame, self.move_control = None, None, None, None, None, None
        self.frame_queue = deque(maxlen=5)  
        # 모델 예측값 쓰레드
        self.model_thread = threading.Thread(target=self.model_predict, daemon=True)
        self.predicted_frame = None
        # 로그 생성 쓰레드
        # self.logmaker_threade = threading.Thread(target=self.accident_fun, daemon=True)
        self.logmaker = ThreadOfLogMaker(self.signal, self.video_file)
        self.frame_number   = 1.0
        self.delay=0


    # 여기서 signal로 메인 스레드로 그냥 신호만 주는 식으로 영상 처리하는.... 고.
    # 설명 : 메인쓰레드에서 영상 재생을 시작하면 영상 쓰레드가 호출되며 실행되는 함수
    # 기능 : cv기반으로 영상을 처리. model_thread 쓰레드를 통해 Yolo모델과 공유 변수를 함께 쓰며 frame 처리중.
    #       run에서 frame read -> model에서 frame -> predicted_frame으로 반환 -> run에서 그 predicted_frame으로 setPixmap -> 띄웠으면 predicted_frame None으로 초기화
    def run(self):
        if self.video_file:
            cap = cv2.VideoCapture(self.video_file)  # 저장된 영상 가져오기 프레임별로 계속 가져오는 듯
            self.length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.fps = cap.get(cv2.CAP_PROP_FPS)
            self.signal.info_signal.emit(self.length, self.fps)  # info_signal을 통해 메인쓰레드로 변수 전송
            self.model_thread.start()   # Yolo 모델
            self.logmaker.start()   # 로그메이커 쓰레드

            while self.running:
                self.ret, self.frame = cap.read()  # 알아서 0번부터 끝까지 착실히 넘어가면서 수행
                self.frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
                # 이전, 이후 이벤트 발생
                if self.move_control == "after":
                    self.now_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                    self.ret = cap.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame + self.fps * 10)
                    self.move_control = None
                    continue
                elif self.move_control == "before":
                    self.now_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                    self.ret = cap.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame - self.fps * 10)
                    self.move_control = None
                    continue
                else:
                    pass

                # 일시 정지 이벤트 발생
                if self.pause:
                    time.sleep(1)
                    continue
                
                if self.ret:
                    if self.predicted_frame is not None:
                        self.rgbImage = cv2.cvtColor(self.predicted_frame, cv2.COLOR_BGR2RGB)  # 프레임에 색 입히기
                        self.convertToQtFormat = QImage(self.rgbImage.data,self.rgbImage.shape[1],self.rgbImage.shape[0],QImage.Format_RGB888,)
                        self.pixmap = QPixmap(self.convertToQtFormat)  # 이 부분이 메인스레드에서 처리되어야하는 QPixmap이 있어서 2개 다 잡아먹고 있는거다?
                        self.p = self.pixmap.scaled(2050, 1150, QtCore.Qt.IgnoreAspectRatio)  # 프레임 크기 조정 1920, 1080 후보 1
                        self.current_time = cap.get(cv2.CAP_PROP_POS_MSEC) * 0.001  # 밀리초 단위 현재 위치
                        self.frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)


                        print(f"self.fps : {self.fps}, self.frame_number : {self.frame_number}")
                        self.signal.video_playing_signal.emit(self.current_time)  # video_playing_signal을 통해 메인쓰레드로 변수 전송               
                        self.signal.silder_signal.emit(self.length, self.fps, self.current_time)
                        

                        self.signal.pixmap_signal.emit(self.p)
                        self.video_frame.update()  # 프레임 띄우기
                        time.sleep(1/self.fps)
                    else:
                        self.ret = cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_number-1)
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
            self.running = False

    def stop(self):
        self.running = False
        self.wait()

    # 메인쓰레드에서 stop하면 불러지는 함수
    def toggle_pause(self):
        self.pause = not self.pause

    def move_video(self, time):
        if time > 0:
            self.move_control = "after"
        else:
            self.move_control = "before"
        return self.move_control

    def model_predict(self):
            ## AR 모델 ##
            while self.running:
                # 일시 정지 이벤트 발생
                if self.pause:
                    time.sleep(1)
                    continue
                if self.frame is not None:
                    result = model.predict(source=self.frame)
                    for r in result:
                        self.frame = r.plot()
                        DF=r.to_df()
                        DF['xyxyn']=r.boxes.xyxyn.tolist()
                        self.signal.accident_signal.emit(DF)
                        break
        
                    ## AR 모델 ##
                    self.predicted_frame = self.frame
                    time.sleep(1/self.fps)
                    


#


        # self.logvideo = ThreadOflogVideo(self.signal, self.video_file)  # 여따가 파일 이름, 시그널 넣기
        # self.logvideo.start()
        # self.logvideo.log_frame_signal.emit(self.length, self.fps, self.current)   # frame 번호 전달 하기.

