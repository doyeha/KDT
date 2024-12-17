from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
import sys
import time, datetime
import datetime as dt
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
class ThreadOfLogMaker(QThread):
    def __init__(self, signal, video_path):
        super().__init__()
        self.video_path = video_path
        self.signal = signal
        self.rec1,self.rec2, self.rec3  = None, None, None
        self.rect1_x1,self.rect1_y1,self.rect1_x2,self.rect1_y2 = None, None, None, None
        self.rect2_x1,self.rect2_y1,self.rect2_x2,self.rect2_y2 = None, None, None, None
        self.rect3_x1,self.rect3_y1,self.rect3_x2,self.rect3_y2 = None, None, None, None

        self.signal.rect_info_signal.connect(self.recxy_receiver)   # rect_info_signal로 drawing에서 그린 영역의 xy 좌표값 받아오기 . 받아와서 recxy_receiver 실행.
        
        self.cntTh=10           # 프레임 몇번 참아줄껀데?
        self.car_cnt=0
        self.helmet_cnt=0
        self.r1_cnt=0
        self.r2_cnt=0
        self.r3_cnt=0


    # connect되어있는 시그널에서 emit으로 값 전달 받으면 실행되고 있음.
    def recxy_receiver(self, rec, x1, y1, x2, y2):
        if rec == "rec1":              self.rec1 = rec
        elif rec == "rec2":            self.rec2 = rec
        elif rec == "rec3":            self.rec3 = rec
        if rec == "rec1":
            self.rect1_x1 = int(x1 / 2121 * 2050)
            self.rect1_y1 = int(y1 / 1201 * 1150)
            self.rect1_x2 = int(x2 / 2121 * 2050)
            self.rect1_y2 = int(y2 / 1201 * 1150)
        if rec == "rec2":
            self.rect2_x1 = int(x1 / 2121 * 2050)
            self.rect2_y1 = int(y1 / 1201 * 1150)
            self.rect2_x2 = int(x2 / 2121 * 2050)
            self.rect2_y2 = int(y2 / 1201 * 1150)

        if rec == "rec3":
            self.rect3_x1 = int(x1 / 2121 * 2050)
            self.rect3_y1 = int(y1 / 1201 * 1150)
            self.rect3_x2 = int(x2 / 2121 * 2050)
            self.rect3_y2 = int(y2 / 1201 * 1150)

    # 스레드 실행 시 자동으로 같이 실행되는 부분
    def run(self):
        self.signal.accident_signal.connect(self.accident_fun)


    def accident_fun(self,DF):                  # Thread에 연결할친구
        self.car_accident(DF)
        self.no_helmet(DF)
        self.rect_accident(DF)

    def make_log(self,rack,case,video_path):
        file_boundary = self.video_path.rindex("/")
        filename = self.video_path[file_boundary + 1 :]
        now=datetime.datetime.now().strftime('%Y_%m_%d')    # 오늘날짜 저장
        print('사고발생시간',now)
        if not os.path.exists('log/'):              # 로그폴더가 없으면 만들어줘
            os.mkdir('log/')
        with open(f'log/{now}.txt',mode='a+',encoding='utf-8') as f:
            new_line = f'{filename} {rack} case_{case} {now} {video_path}\n'
            f.write(new_line)
            # !!!!make 실행 후 파일이 만들어 졌으니 여기서 case 보내기 self.signal.시그널명.emit(case) 해주기 
        # 여기서 showlist 하지 말고 str 만들어서 Mainview에서 리스트 작성하도록 유도.
        # self.signal.loglist_signal.emit(new_line.replace("\n",""))
        clean_line = new_line.replace('\n', '')
        self.signal.loglist_signal.emit(f"{clean_line}|{case}")




    # 차 vs 사람 사고 경고
    def car_accident(self,DF,ratio=0.7):
        if len(DF):
            personDF=DF[(DF['class']==0)|(DF['class']==1)]  # 사람 관련 DF
            carDF=DF.drop(personDF.index)       # 차량 관련 DF
            w,a,s,d=0,0,0,0                     # 4방향 가중치 초기화
            accident=False                   # 사고여부 초기화
            if len(personDF)*len(carDF):        # 차와 사람이 둘다있을경우만 진행
                for c_idx in carDF.index:
                    c=carDF.loc[c_idx,'xyxyn']
                    if carDF.loc[c_idx,'class']==2:            # w 방향 가중치
                        w=ratio
                    elif carDF.loc[c_idx,'class']==3:           # a 방향 가중치
                        a=ratio
                    elif carDF.loc[c_idx,'class']==4:           # s 방향 가중치
                        s=ratio
                    elif carDF.loc[c_idx,'class']==3:           # d 방향 가중치
                        d=ratio
                    wid=c[2]-c[0]         # 차너비
                    hei=c[3]-c[1]         # 차높이
                    for p in personDF.xyxyn:
                        if ((c[0]-wid*a<=p[0]<=c[2]+wid*d) or (c[0]-wid*a<=p[2]<=c[2]+wid*d)) and ((c[1]-hei*w<=p[1]<=c[3]+hei*s) or (c[1]-hei*w<=p[3]<=c[3]+hei*s)) :
                            accident=True
                            break
            if accident:
                self.car_cnt=min(self.car_cnt+1,self.cntTh+10)
                if self.car_cnt==self.cntTh:
                    self.make_log(0,'car',f"test_{dt.datetime.now().strftime('%m%d_%H%M')}.mp4")
                    self.signal.aci_info_signal.emit(0, "car")
            else:
                self.car_cnt=max(self.car_cnt-1,0)


    def no_helmet(self,DF):
        if len(DF):
            if len(DF[DF['class']==1]):
                self.helmet_cnt=min(self.helmet_cnt+1,self.cntTh+10)
                if self.helmet_cnt==self.cntTh:
                    self.make_log(0,'helmet','no_video')
            else:
                self.helmet_cnt=max(self.helmet_cnt-1,0)


    def rect_accident(self,DF):
        # 1번 렉사고 모두x
        r1_accident=False
        if self.rect1_x2:
            x1=min(self.rect1_x1,self.rect1_x1+self.rect1_x2)/2050
            y1=min(self.rect1_y1,self.rect1_y1+self.rect1_y2)/1150
            x2=max(self.rect1_x1,self.rect1_x1+self.rect1_x2)/2050
            y2=max(self.rect1_y1,self.rect1_y1+self.rect1_y2)/1150
            if len(DF):
                for idx in DF.index:
                    c=DF.loc[idx,'xyxyn']
                    if ((x1<=c[0]<=x2) or (x1<c[2]<=x2)) and ((y1<=c[1]<=y2) or (y1<=c[3]<=y2)) :
                        r1_accident=True
                        break
            if r1_accident:
                self.r1_cnt=min(self.r1_cnt+1,self.cntTh+5)
                if self.r1_cnt==self.cntTh:
                    self.make_log(1,'rack',f"test_{dt.datetime.now().strftime('%m%d_%H%M')}.mp4")
                    self.signal.aci_info_signal.emit(1, "rack")
            else:
                self.r1_cnt=max(self.r1_cnt-1,0)
        # 2번렉사고 지게차만x
        r2_accident=False
        if self.rect2_x2:
            x1=min(self.rect2_x1,self.rect2_x1+self.rect2_x2)/2050
            y1=min(self.rect2_y1,self.rect2_y1+self.rect2_y2)/1150
            x2=max(self.rect2_x1,self.rect2_x1+self.rect2_x2)/2050
            y2=max(self.rect2_y1,self.rect2_y1+self.rect2_y2)/1150
            if len(DF):
                carDF=DF[~( (DF['class']==0) | (DF['class']==1))]
                if len(carDF):
                    for idx in carDF.index:
                        c=carDF.loc[idx,'xyxyn']
                        if ((x1<=c[0]<=x2) or (x1<c[2]<=x2)) and ((y1<=c[1]<=y2) or (y1<=c[3]<=y2)) :
                            r2_accident=True
                            break
            if r2_accident:
                self.r2_cnt=min(self.r2_cnt+1,self.cntTh+5)
                if self.r2_cnt==self.cntTh:
                    self.make_log(2,'rack',f"test_{dt.datetime.now().strftime('%m%d_%H%M')}.mp4")
                    self.signal.aci_info_signal.emit(2, "rack")
            else:
                self.r2_cnt=max(self.r2_cnt-1,0)
        # 3번렉사고 사람만 x
        r3_accident=False
        if self.rect3_x2:
            x1=min(self.rect3_x1,self.rect3_x1+self.rect3_x2)/2050
            y1=min(self.rect3_y1,self.rect3_y1+self.rect3_y2)/1150
            x2=max(self.rect3_x1,self.rect3_x1+self.rect3_x2)/2050
            y2=max(self.rect3_y1,self.rect3_y1+self.rect3_y2)/1150
            if len(DF):
                personDF=DF[(DF['class']==0) | (DF['class']==1)]
                if len(personDF):
                    for idx in personDF.index:
                        c=personDF.loc[idx,'xyxyn']
                        if ((x1<=c[0]<=x2) or (x1<c[2]<=x2)) and ((y1<=c[1]<=y2) or (y1<=c[3]<=y2)) :
                            r3_accident=True
                            break
            if r3_accident:
                self.r3_cnt=min(self.r3_cnt+1,self.cntTh+5)
                if self.r3_cnt==self.cntTh:
                    self.make_log(3,'rack',f"test_{dt.datetime.now().strftime('%m%d_%H%M')}.mp4")
                    self.signal.aci_info_signal.emit(3, "rack")
            else:
                self.r3_cnt=max(self.r3_cnt-1,0)