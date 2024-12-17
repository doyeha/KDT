from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import sys
import time, datetime
import cv2
from time import sleep
from PyQt5.QtCore import (QThread,pyqtSignal)  # 영상 처리 멀티스레드 // 메인스레드 - 영상용 스레드 신호 연결 목적
from PyQt5 import QtWidgets, QtGui, QtCore
import os, datetime  # 영상 정보 띄우기 목적, datetime
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import *
import threading
from collections import deque 
import warnings
warnings.simplefilter("ignore", DeprecationWarning) # deprecated 오류메세지 ignore 목적
from PyQt5.QtWidgets import QMessageBox,QListWidgetItem
import pandas as pd
import subprocess

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


# self python.file import
from setting import settingsView
from drawing import Drawing, ThreadOfDrawing
from signal_collection import collectionOfSignals
from ThreadOfVideo import ThreadOfVideo
from log_maker import ThreadOfLogMaker
from log_alram import Alram
from LogVideo import frame_saver

## AR 모델 ##
from ultralytics import YOLO
#model ver 7
model=YOLO('best.pt')
## AR 모델 ##


form_class = uic.loadUiType("./ui/MainView.ui")[0]
# 메인뷰 540 x 420
class MainView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("프로그램 시작")

        # 팝업창 연결
        self.signal = collectionOfSignals()
        self.setting = settingsView(self.signal)
        self.alram = Alram(self.signal)
        # self.logmaker = ThreadOfLogMaker()
        
        self.video_file = "./img/base_pic.png"
        # 영상 띄우기
        self.video_frame = self.findChild(QtWidgets.QLabel, "video_frame")
        self.video_frame.setStyleSheet("background-color: black;")  # 영상 없음 검은 호ㅜㅏ면 해
        self.video_thread = None

        self.length = None  # 초기값 설정
        self.fps = None  # 초기값 설정

        # drawing 부분
        self.rec1,self.rec2, self.rec3  = None, None, None
        self.rect1_x1,self.rect1_y1,self.rect1_x2,self.rect1_y2 = 0, 0, 0, 0
        self.rect2_x1,self.rect2_y1,self.rect2_x2,self.rect2_y2 = 0, 0, 0, 0
        self.rect3_x1,self.rect3_y1,self.rect3_x2,self.rect3_y2 = 0, 0, 0, 0

        self.date=self.findChild(QtWidgets.QDateTimeEdit, "dateTimeEdit")
        self.case=self.findChild(QtWidgets.QComboBox, "comboBox")
        self.search_date=0
        self.search_case=0


        # 리스트뷰 띄우는 부분.
        self.showlist("")
        # self.signal.loglist_signal.connect(self.showlist)

        # 로그 메이커에서 clean_line | rack 받아옴.
        self.signal.loglist_signal.connect(self.update_log_list)


        # yj_ui 추가
        self.setWindowTitle("NEMONEMO")
        self.setWindowIcon(QIcon("./img/logo.png"))
        self.signal.rect_info_signal.connect(self.drawing_info_update)

        #yj_단축키 추가
        self.spacebar_shortcut = QShortcut(QKeySequence(Qt.Key_Space), self)
        self.spacebar_shortcut.activated.connect(self.video_pause)

        # 왼쪽 화살표 단축키 설정
        self.left_shortcut = QShortcut(QKeySequence(Qt.Key_Left), self)
        self.left_shortcut.activated.connect(self.move_before_10s)

        # 오른쪽 화살표 단축키 설정
        self.right_shortcut = QShortcut(QKeySequence(Qt.Key_Right), self)
        self.right_shortcut.activated.connect(self.move_after_10s)


        #QDateTimeEdit 오늘 날짜로 설정
        self.date = self.findChild(QtWidgets.QDateTimeEdit, "dateTimeEdit")
        current_datetime = QDateTime.currentDateTime()  
        self.date.setDateTime(current_datetime)

        self.Log_list.itemDoubleClicked.connect(self.logvideo_opener)


    def logvideo_opener(self):
        # 현재 아이템의 텍스트에서 파일 경로를 추출
        self.file_path = self.Log_list.currentItem().text()
        print(self.file_path)
        
        # 'videofile'가 포함되어 있는지 확인
        if "videofile" in self.file_path:
            # 'videofile' 기준으로 경로를 분리
            self.file_path = self.file_path.split("videofile")[1].replace(" ", "")
        else:
            # 'videofile'가 없으면 경고 메시지 출력
            print("Error: 'videofile' not found in the path.")
            return  # 함수 종료
        
        # 현재 스크립트의 디렉토리 경로 가져오기
        current_dir = os.path.dirname(os.path.realpath(__file__))
        
        # 전체 경로 계산 (현재 디렉토리 + 파일 경로)
        file_path = os.path.join(current_dir,'log_video', self.file_path)
        
        # 파일 경로 출력 (디버깅용)
        print(f"로그 영상 경로: {file_path}")
        
        # 영상 실행
        subprocess.run(["start", "", file_path], shell=True)


    def update_log_list(self, combined_message):
        # print("combined_message : ",combined_message)
        message, case = combined_message.rsplit('|', 1)  # 문자열을 나누어 message와 rack 추출
        # showlist 호출
        self.showlist(message)
        # 팝업 알림 표시
        # 영상이 재생될 때 알람 쓰레드도 같이 활성화.
        # 이때 신호주면 되겠네.
        self.signal.alram_signal.emit(case)


            

    # 연결 위젯 : directory_button  | 속성 : QPushButton
    # 기능 : 선택된 영상을 재생시키는 함수
    # 설명 : video_FileLoad()와 연동해 버튼 클릭 시 파일을 가져오고 영상 재생을 위한 쓰레드를 활성화시킨다.
    # 비고 : 다수 시그널 연결, 많은 메서드가 실행되는 구간.
    def load_video(self):
        # 이미 영상이 재생중이라면, 우선 재생중인 비디오를 일시정지한다.
        self.video_file = self.video_FileLoad()  # 파일을 선택하는 함수
        if self.video_file:
            self.video_playing = True
            # 영상 처리를 위한 쓰레드 생성
            if self.video_thread:
                self.video_thread.stop()   # 이미
                self.alram.stop()
                self.saver.wait()
            print(self.video_file)
            self.video_thread = ThreadOfVideo(self.signal, self.video_file, self.video_frame)
            self.alram = Alram(self.signal)
            self.saver = frame_saver(self.signal)
            # 시그널이 이렇게 많아지면 조금 복잡? 비효율적이지 않나. (질문 1)
            self.signal.pixmap_signal.connect(self.update_frame)  # 영상 cv정보(pixmap)를 받아오는 시그널, QPix... 쟤는 메인 쓰레드에서 처리되어야한다.
            self.signal.video_playing_signal.connect(self.playing_label_change)  # VideoOfThread에서 length (int) 받아옴
            self.signal.info_signal.connect(self.video_totaltime_label)  # VideoOfThread에서 length (int), fps (float) 받아옴
            self.signal.info_signal.connect(self.print_video_info)  
            self.signal.silder_signal.connect(self.silder_change)  # VideoOfThread에서 length (int), fps (float), current_time (int) 받아옴
            self.video_thread.start()
            self.alram.start()
            self.saver.start()

            #### 새로 영상 로드하면 랙 영역 좌표값 초기화 ####
            self.reset_drawing_info()
            # self.signal.rect_info_signal.connect(self.drawing_info_update)
            #############################################

    def closeEvent(self, event):
        quit_msg = "프로그램을 종료하시겠습니까?"
        reply = QMessageBox.question(self, 'Exit', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.video_thread.stop()
            event.accept()
        else:
            event.ignore()

    # 연결 위젯 : setting_button    | 속성 : QPushButton
    # 기능 : 버튼 클릭 이벤트를 통해 세팅창으로 이동하는 함수
    # 설명 : setting.py와 연동하여 settingsView를 새로운 창으로 띄운다.
    def go_setting(self):
        self.setting.show()

    def go_logVideo(self):
        pass

    ### rec영역 작성 파트 ###
    def go_drawing(self):
        if self.video_file:
            self.drawing_view = Drawing(self.signal, self.video_file)
            # 여기서 쓰레드 실행하게 하는 식으로 가자 ...ㅇㄴㄻㄴㅇㄻㅇㄴㄹ
            self.drawing_thread = ThreadOfDrawing(self.signal, self.video_file)
            self.drawing_thread.start()
            self.drawing_view.show()
            self.set_drawing_recxy_label()

    def reset_drawing_info(self):
            self.rec1,self.rec2, self.rec3  = None, None, None
            self.rect1_x1,self.rect1_y1,self.rect1_x2,self.rect1_y2 = 0, 0, 0, 0
            self.rect2_x1,self.rect2_y1,self.rect2_x2,self.rect2_y2 = 0, 0, 0, 0
            self.rect3_x1,self.rect3_y1,self.rect3_x2,self.rect3_y2 = 0, 0, 0, 0
            self.label = self.rec_film
            self.canvas = QPixmap(2050, 1150)  # 캔버스 크기 설정
            self.canvas.fill(Qt.transparent) 
            self.label.setPixmap(self.canvas)

    def drawing_info_update(self, rec, x1, y1, x2, y2):
        if rec == "rec1":              self.rec1 = rec
        elif rec == "rec2":            self.rec2 = rec
        elif rec == "rec3":            self.rec3 = rec
        
        self.label = self.rec_film  # ui에 지정되어있는 QLabel
        self.canvas = QPixmap(2050, 1150)  # 캔버스 크기 설정
        self.canvas.fill(Qt.transparent)  # 캔버스를 투명으로 초기화
        self.qp = QPainter(self.canvas)
        self.qp.begin(self)

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

        self.set_drawing_recxy_label()

        # 텍스트 크기 설정
        font = self.qp.font()
        font.setPointSize(20)  
        self.qp.setFont(font)

        def draw_rect_text(x,y,w,h, text):
            b_x = 5 # 텍스트 위치 x 보정값
            b_y = 35    # 텍스트 위치 y 보정값
            if w < 0 and h < 0:         self.qp.drawText(x + w + b_x, y + h + b_y, text)  # 좌상단에서 약간의 패딩 추가
            elif w < 0:                 self.qp.drawText(x + w+ b_x, y + b_y, text)  # 좌상단에서 약간의 패딩 추가
            elif h < 0:                 self.qp.drawText(x + b_x, y + h + b_y, text)  # 좌상단에서 약간의 패딩 추가
            else:                       self.qp.drawText(x + b_x, y + b_y, text)

        self.qp.setPen(QPen(Qt.red, 3))
        self.qp.drawRect(self.rect1_x1, self.rect1_y1, self.rect1_x2, self.rect1_y2)
        draw_rect_text(self.rect1_x1, self.rect1_y1, self.rect1_x2, self.rect1_y2, "rec1")
        
        self.qp.setPen(QPen(Qt.yellow, 3))
        self.qp.drawRect(self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2)
        draw_rect_text(self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2, "rec2")


        self.qp.setPen(QPen(Qt.blue, 3))
        self.qp.drawRect(self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2)
        draw_rect_text(self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2, "rec3")

        self.qp.end()
        self.label.setPixmap(self.canvas)


    def set_drawing_recxy_label(self):
        font = "굴림"
        font_size = 10
        self.drawing_view.rect1_info.setText(f"rec 영역 크기 {self.rect1_x1, self.rect1_y1, self.rect1_x2, self.rect1_y2}\n좌표")
        self.drawing_view.rect1_info.setFont(QtGui.QFont(font,font_size))
        self.drawing_view.rect2_info.setText(f"rec 영역 크기 {self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2}\n좌표")
        self.drawing_view.rect2_info.setFont(QtGui.QFont(font,font_size))
        self.drawing_view.rect3_info.setText(f"rec 영역 크기 {self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2}\n좌표")
        self.drawing_view.rect3_info.setFont(QtGui.QFont(font,font_size))
    ########################


    # 연결 위젯 : Log_list    | 속성 : QListWidget
    # 기능 : 로그 리스트를 제공하는 위젯에 정보를 전달하는 함수
    # 설명 : ListView가 아닌 Widget를 이용해 정보를 제공한다. 오토 스크롤 기능이 있다.
    def showlist(self,s):
        self.Log_list.clear()
        # log 폴더 접근
        logfile_list=os.listdir('log')
            # 일단 마지막파일 보여주는걸로! 나중에 오늘날짜로 수정하기
        

        # 30일 지난 로그파일 삭제
        for log_file in logfile_list:
            log_date=log_file.rstrip('.txt')
            log_dt=pd.to_datetime(log_date.replace('_','-'))
            log_range=pd.Timedelta('30 days')           # 일단 30일로 잡앗으나 옵션받을거면 받아보고..
            if datetime.datetime.now()-log_dt > log_range:
                os.remove('log/log_file')               # range넘은파일 삭제
                break




        if logfile_list:        # log 파일이 있다면
            if self.search_date:        # 설정된 날짜가 있다면.
                mon=str(self.search_date.month())
                if len(mon)==1:
                    mon='0'+mon
                day=str(self.search_date.day())
                if len(day)==1:
                    day='0'+day
                show_file=f'{self.search_date.year()}_{mon}_{day}.txt'
            else:           # 설정된 날짜가 없다면 최신파일
                show_file=logfile_list[-1] 

            if show_file in logfile_list:           # 보여줄파일이있다면
                # 리스트로 불러와서 한줄씩 보여줌
                with open('log/'+show_file,encoding='utf-8') as f :
                    logs=f.readlines()
                    log_list2=[i.strip('\n').split(' ') for i in logs]
                    log_df=pd.DataFrame(log_list2,columns=['movie','rack','case','date','videofile'])
            else: log_df=pd.DataFrame() # 보여줄 파일이 없다면 빈DF

        else:          # log 폴더가 없다면 빈DF
            log_df=pd.DataFrame()
        # case 검색
        if len(log_df)>0:
            if self.search_case=='case helmet':
                log_df=log_df[log_df['case']=='case_helmet']
            elif self.search_case=='case car':
                log_df=log_df[log_df['case']=='case_car']
            elif self.search_case=='case rack':
                log_df=log_df[log_df['case']=='case_rack']

            for i in log_df.index:
                self.Log_list.addItem(f"{log_df.loc[i]}")

        # 로그검색
    def log_search(self):
        self.search_date=self.date.date()
        self.search_case=self.case.currentText()
        self.showlist("")

    # 연결 위젯 : playing_silder    | 속성 : QSlider
    # 기능 : 슬라이더 재생바의 위치를 조정한다.
    # 설명 : length와 fps로 영상의 재생길이를 계산하고, 현재 영상의 프레임 번호를 이용해 현 시점을 계산한다. 그 위치로 slider의 바 위치 값을 변동한다.
    # 비고 : silder_signal에서 아래 args 3개를 받아온다.
    def silder_change(self, length, fps, current_time):
        self.signal.log_fps_signal.emit(length, fps, current_time)
        # .setValue(Value) 0~99 해서 100으로 나눈 다음에 27초면? 100에서 27초 나누고 100/27 만큼 움직이기.
        self.total_time = length / fps
        silder_position = (100 / self.total_time) * current_time
        self.playing_silder.setValue(silder_position)

    # 기능 : 영상 쓰레드에서 메인 쓰레드로 Pixmap값을 전달하는 함수
    def update_frame(self, pixmap):
        self.video_frame.setPixmap(pixmap)

    # 기능 : 파일 디렉토리 창을 띄워 영상을 선택할 수 있게 하는 함수
    # 설명 : load_video이 실행될 때 실행되며, 선택된 영상의 path값을 반환한다.
    def video_FileLoad(self):
        # fname = QFileDialog.getOpenFileName(self)  # QFileDialog 자체가 파일 불러오기 기능. App2 디렉토리가 열린다.
        # print("fname : ", fname)    # 튜플 형식으로 나온다. (문서 위치, 나온 문서들의 형식 ex All Files)
        # print(fname[0])

        ############# yj #################
        # 사용자의 Downloads 폴더 경로
        downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

        print(downloads_dir)

        fname = QFileDialog.getOpenFileName(self,"파일 업로드", downloads_dir,'MP4(*.mp4);;All Files(*)')

        if fname[0]:
            print("파일 선택 경로")
            print(fname[0])
        else:
            QMessageBox.critical(self,'Warning', '파일을 선택해주세요')
            print("파일 안 골랐슴")
        ############# yj #################

        return fname[0]

    # 연결 위젯 : 아직 없으나 연결될 가능성이 없지는 않다.
    # 기능 : 영상 쓰레드를 종료시키는 함수
    # 설명 : VideoOfThread의 stop 함수를 활용한다.
    # def video_stop(self):
    #     if self.video_playing:  # 실행중이라면 스탑
    #         self.video_thread.stop()

    # 연결 위젯 : video_pause_button    | 속성 : QPushButton
    # 기능 : 영상을 일시정지시키는 함수
    # 설명 : 일시정지 버튼 클릭 시 영상이 일시정지된다. VideoOfThread의 toggle_pause 함수를 활용한다.
    def video_pause(self):
        if self.video_thread:
            self.video_thread.toggle_pause()
            

    # 연결 위젯 :     | 속성 :
    # 기능 : 영상을 뒤로 되감는 함수
    # 설명 : 버튼 클릭 시 영상이 10초 이전으로 다시 재생된다.
    def move_before_10s(self):
        if self.video_thread:
            self.video_thread.move_video(-10)  # 여기서 클래스 쪽에 def가 실행되도록 함.

    def move_after_10s(self):
        if self.video_thread:
            self.video_thread.move_video(10)

    # 연결 위젯 : current_time_label  | 속성 : QLabel
    # 설명 : 영상의 실시간 재생시간을 제공하는 함수
    # 기능 : 현재 cv의 frame위치를 활용해 13:52과 같은 형식으로 영상의 실시간 위치 정보를 제공한다.
    # 비고 : video_playing_signal 이용해 ThreadOfVideo에서 length와 fps를 받아온다.
    def playing_label_change(self, current_time):
        if self.video_thread:
            if type(current_time) == float:
                current_time = int(current_time)
            if type(current_time) == int:
                current_time = str(datetime.timedelta(seconds=current_time))
            else:
                current_time = str(current_time)
            self.current_time_label.setText(current_time)

    # 연결 위젯 : video_total_label | 속성 : QLabel
    # 설명 : 영상의 총 길이정보를 제공하는 함수
    # 기능 : 영상의 총 길이를 계산하여 02:23과 같은 형식으로 영상의 총 길이를 제공한다.
    # 비고 : info_signal 이용해 ThreadOfVideo에서 length와 fps를 받아온다.
    def video_totaltime_label(self, length, fps):
        if self.video_thread:
            time = length / fps
            if type(time) == float:
                time = int(time)
            if type(time) == int:
                time = str(datetime.timedelta(seconds=time))
            else:
                time = str(time)
            self.video_total_label.setText(time)

    # 연결 위젯 : video_info_label | 속성 : QLabel
    # 설명 : 선택되어 재생중인 영상의 파일 정보를 불러오는 함수
    # 기능 : 경로, 파일명, 파일 최종 수정 날짜, 영상 길이 제공한다.
    # 비고 : silder_signal을 이용해 ThreadOfVideo에서 length와 fps를 받아온다.
    def print_video_info(self, length, fps):
        if self.video_file:
            path = self.video_file
            access_time = os.stat(path).st_mtime
            access_time = datetime.datetime.fromtimestamp(access_time)
            # print(video_file[:video_file.rindex("\\")])
            file_boundary = self.video_file.rindex("/")
            directory_position = self.video_file[:file_boundary]
            filename = self.video_file[file_boundary + 1 :]

            video_time = int(length / fps)
            # video_time = time.strftime(str(video_time), "%H:%M:%S")
            video_time = time.strftime("%H:%M:%S", time.gmtime(video_time))
            if video_time[:2] == "00":
                video_time = video_time[video_time.index(":") + 1 :]
            video_info = f"경로 : {directory_position} \n파일명 : {filename}\n영상 날짜 : {access_time}\n영상 길이 : {video_time}"
            self.video_info_label.setText(video_info)
    

    ########


# 콜백 func
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainView()
    myWindow.showMaximized()
    app.exec_()