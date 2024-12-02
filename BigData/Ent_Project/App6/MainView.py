from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
import sys
import time, datetime
import cv2
from time import sleep
from PyQt5.QtCore import (QThread,pyqtSignal)  # 영상 처리 멀티스레드 // 메인스레드 - 영상용 스레드 신호 연결 목적
from PyQt5 import QtWidgets, QtGui, QtCore
import os, datetime  # 영상 정보 띄우기 목적, datetime
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
import threading
from collections import deque 
import warnings
warnings.simplefilter("ignore", DeprecationWarning) # deprecated 오류메세지 ignore 목적


# 디자인 qrc파일
sys.path.append(r'C:\Git\KDT\BigData\Ent_Project\App6\resources') 
from resources import *


# self python.file import
from setting import settingsView
from drawing import Drawing, ThreadOfDrawing
from signal_collection import collectionOfSignals
from ThreadOfVideo import ThreadOfVideo
from log_maker import ThreadOfLogMaker


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
        self.setting = settingsView()
        self.signal = collectionOfSignals()
        # self.logmaker = ThreadOfLogMaker()
        
        self.video_file = ".img/base_pic.png"
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


        # 리스트뷰 띄우는 부분.
        self.showlist("")
        self.signal.loglist_signal.connect(self.showlist)

        # jy_ui 추가
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("NEMONEMO")

        self.signal.rect_info_signal.connect(self.drawing_info_update)
        
    
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
            print(self.video_file)
            self.video_thread = ThreadOfVideo(self.signal, self.video_file, self.video_frame)
            # 시그널이 이렇게 많아지면 조금 복잡? 비효율적이지 않나. (질문 1)
            self.video_thread.pixmap_signal.connect(self.update_frame)  # 영상 cv정보(pixmap)를 받아오는 시그널, QPix... 쟤는 메인 쓰레드에서 처리되어야한다.
            self.signal.video_playing_signal.connect(self.playing_label_change)  # VideoOfThread에서 length (int) 받아옴
            self.signal.info_signal.connect(self.video_totaltime_label)  # VideoOfThread에서 length (int), fps (float) 받아옴
            self.signal.info_signal.connect(self.print_video_info)  
            self.signal.silder_signal.connect(self.silder_change)  # VideoOfThread에서 length (int), fps (float), current_time (int) 받아옴
            self.video_thread.start()

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


    def open_setting(self):
        pass
    # 검색

    # 연결 위젯 : Log_list    | 속성 : QListWidget
    # 기능 : 로그 리스트를 제공하는 위젯에 정보를 전달하는 함수
    # 설명 : ListView가 아닌 Widget를 이용해 정보를 제공한다. 오토 스크롤 기능이 있다.
    def showlist(self, str):
        if not os.path.exists('log/'):              # 로그폴더가 없으면 만들어줘
            os.mkdir('log/')
        text = []
        file_path = "log\\"
        all_file = os.listdir(file_path)
        for f in all_file:
            with open(file_path+f, mode='r') as f:
                lines = f.readlines()
                text.extend(lines)

        self.Log_list.clear()
        list_idx=1
        for i in text:
            i = i.replace("\n","")
            self.Log_list.addItem(f"{list_idx}. {i}")
            list_idx+=1

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
        fname = QFileDialog.getOpenFileName(self)  # QFileDialog 자체가 파일 불러오기 기능. App2 디렉토리가 열린다.
        # print("fname : ", fname)    # 튜플 형식으로 나온다. (문서 위치, 나온 문서들의 형식 ex All Files)
        # print(fname[0])
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

# class ThreadOflogVideo(QThread, form_class):
#     logvideo_signal = pyqtSignal(QPixmap)
#     log_frame_signal = pyqtSignal(int, float, int)  # length, fps, 현재 프레임 번호 전송
#     # 로그 비디오를 비디오를 남길건데?
#     # 얘는 로그가 만들어지면 그 로그의 정보값을 받아서 그 영상의 시간에 가서 일부를 저장하는 것이에요~~~~
#     # 그럼? 로그가 남겨질 당시의 영상 프레임도 받아오야게쌍르미ㅏㅡㅏㅣㄹㅇ느ㅏㅣㅇㅁㄴㅀㅅ가ㅣㅢㅇ휴
#     def __init__(self, signal, video_file):
#         super().__init__()
#         self.video_file = video_file
#         self.signal = signal
#         self.fps = 0
#         self.current_time = 0
#         self.length = 0
#         self.playing_frame = None

#     def fps_receiver(self, length, fps,current_time):
#         self.length = length
#         self.fps = fps
#         self.current_time = current_time
#         print("fps_receiver 실행 완.")
#         print(self.length,self.fps, self.current_time)

#     def run(self):
#         cap = cv2.VideoCapture(self.video_file)  # 저장된 영상 가져오기 프레임별로 계속 가져오는 듯
#         self.w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # 프레임 넓이
#         self.h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이
#         if self.current_time == 0:
#             self.signal.log_fps_signal.connect(self.fps_receiver)   # 슬라이드바 상태 따라서 메인뷰에서 fps값 갱신받기

#         # length, fps, current_time 받아서 
#         # 길이가 총 길이 / length/fps 하면 총 시간 

#         # 처음에 시작 프레임 번호 받고 거따가 -10 해서 20만큼 흘러갈 동안만 while문 반복.
#         # self.current_time 에서 -length/fps*10 그리고  +10 되는 구간에서 스탑.
#         print("현재 시간으으응륾아ㅣㅡㅇㄴ르ㅏㅇ랑ㄹㄹㄹ라아아악",self.current_time)
#         self.playtime = 20*self.fps + self.current_time*self.fps
#         # self.running = True
#         # 현재 프레임 번호는 ... length/fps (총 시간)   120초
#         # current_time  (현재 시간) 60초 << 시간*fps 하면 현재 프레임 번호구나!
#         self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         out = cv2.VideoWriter('결과물 테스트.mp4', self.fourcc, self.fps, (self.w, self.h))
        
#         cap.set(cv2.CAP_PROP_POS_FRAMES, self.fps*self.current_time)               # , b 값으로 프레임 번호를 바꿈.

#         while True:
#             self.ret, self.frame = cap.read()
#             if not self.ret:
#                 break
#             # self.ret, self.frame = cap.read()
#             self.playing_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
#             if self.playing_frame ==  self.playtime:
#                 break
#             out.write(self.frame)
#         out.release()
#         cap.release()


        # self.fps

        # self.log_frame_signal.connect() # 로고 프레임 번호 받아오기

        # self.logvideo_signal.connect()
        
        # self.length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # self.fps = cap.get(cv2.CAP_PROP_FPS)
        # self.signal.info_signal.emit(self.length, self.fps)

        # self.current_time = cap.get(cv2.CAP_PROP_POS_MSEC) * 0.001  # 밀리초 단위 현재 위치
        # self.signal.video_playing_signal.emit(self.current_time)  # video_playing_signal을 통해 메인쓰레드로 변수 전송
        # self.signal.silder_signal.emit(self.length, self.fps, self.current_time)

            # self.video_frame.setPixmap(self.p)  # NoneType 오류가 계속 떠요
            # 위 코드에서 아래 코드로 바꾸니까 강제 종료 되던 것이 해결이 .. 되었음.
        # self.pixmap_signal.emit(self.p)

        # cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=None) 
        # • filename : 비디오 파일 이름 (e.g. 'video.mp4')
        # • fourcc : fourcc (e.g. cv2.VideoWriter_fourcc(*'DIVX'))
        # • fps : 초당 프레임 수 (e.g. 30)
        # • frameSize : 프레임 크기. (width, height) 튜플.
        # • isColor : 컬러 영상이면 True, 그렇지않으면 False. 기본값은 True입니다.
        # • retval : cv2.VideoWriter 객체




# 콜백 func
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainView()
    myWindow.show()
    app.exec_()
