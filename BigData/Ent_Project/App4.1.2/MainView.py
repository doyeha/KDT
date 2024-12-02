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

# 디자인 qrc파일
import resources_rc

# deprecated 오류메세지 ignore 목적
import warnings



from setting import settingsView
from drawing import Drawing

# 그림 이슈
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
# from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt

# form_class = uic.loadUiType("MainView_ver2.ui")[0]
form_class = uic.loadUiType("MainView.ui")[0]


## AR 모델 ##
from ultralytics import YOLO

model = YOLO(
    r"C:\Git\KDT\BigData\Ent_Project\App4.1.1\best.pt"
)
## AR 모델 ##


warnings.simplefilter("ignore", DeprecationWarning)


# 메인뷰 540 x 420
class MainView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("프로그램 시작")

        # 팝업창 연결
        self.drawing = Drawing()
        self.setting = settingsView()

        # 영상 띄우기
        self.video_frame = self.findChild(QtWidgets.QLabel, "video_frame")
        self.video_frame.setStyleSheet("background-color: black;")  # 영상 없음 검은 호ㅜㅏ면 해
        # self.video_thread(video_file)
        # self.video_thread.info_signal.connect(self.update_frame)  # fps 랑 length 보내온거 받기.
        self.video_thread = None

        self.length = None  # 초기값 설정
        self.fps = None  # 초기값 설정

        # drawing 부분
        self.rec1,self.rec2, self.rec3  = None, None, None
        self.rect1_x1,self.rect1_y1,self.rect1_x2,self.rect1_y2 = 0, 0, 0, 0
        self.rect2_x1,self.rect2_y1,self.rect2_x2,self.rect2_y2 = 0, 0, 0, 0
        self.rect3_x1,self.rect3_y1,self.rect3_x2,self.rect3_y2 = 0, 0, 0, 0

    
        # 리스트뷰 띄우는 부분.
        self.showlist()

        # jy_ui 추가
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("NEMONEMO")

        self.drawing.rect_info_signal.connect(self.drawing_info_update)

    # 연결 위젯 : setting_button    | 속성 : QPushButton
    # 기능 : 버튼 클릭 이벤트를 통해 세팅창으로 이동하는 함수
    # 설명 : setting.py와 연동하여 settingsView를 새로운 창으로 띄운다.
    def go_setting(self):
        self.setting.show()


    ### rec영역 작성 파트 ###
    def go_drawing(self):
        self.drawing.show()

    
    # 
    def go_(self):
        self.drawing.show()
        

    # def drawing_info_update(self, rec, x1, y1, x2, y2):
    #     if rec == "rec1":
    #         self.rec1 = rec
    #     elif rec == "rec2":
    #         self.rec2 = rec
    #     elif rec == "rec3":
    #         self.rec3 = rec
    #     self.label = self.rec_film  # ui에 지정되어있는 QLabel
    #     self.canvas = QPixmap(2050, 1150)  # 캔버스 크기 설정
    #     self.canvas.fill(Qt.transparent)  # 캔버스를 흰색으로 초기화
    #     self.qp = QPainter(self.canvas)
    #     self.qp.begin(self)
    #     if self.rec1 is not None:
    #         self.rect1_x1 = x1
    #         self.rect1_y1 = y1
    #         self.rect1_x2 = x2
    #         self.rect1_y2 = y2
    #         self.drawing.rect1_info.setText(f"rec 영역 크기 {self.rect1_x1, self.rect1_y1, self.rect1_x2, self.rect1_y2}\n좌표")
    #         self.drawing.rect1_info.setFont(QtGui.QFont("굴림",5))
    #         self.qp.setPen(QPen(Qt.red, 3))
    #         self.qp.drawRect(self.rect1_x1+561, self.rect1_y1+431, self.rect1_x2, self.rect1_y2)

    #     if self.rec2 is not None:
    #         self.rect2_x1 = x1
    #         self.rect2_y1 = y1
    #         self.rect2_x2 = x2
    #         self.rect2_y2 = y2
    #         self.drawing.rect2_info.setText(f"rec 영역 크기 {self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2}\n좌표")
    #         self.drawing.rect2_info.setFont(QtGui.QFont("굴림",5))
    #         self.qp.setPen(QPen(Qt.yellow, 3))
    #         self.qp.drawRect(self.rect2_x1+561, self.rect2_y1+431, self.rect2_x2, self.rect2_y2)

    #     if self.rec3 is not None:
    #         self.rect3_x1 = x1
    #         self.rect3_y1 = y1
    #         self.rect3_x2 = x2
    #         self.rect3_y2 = y2
    #         self.drawing.rect3_info.setText(f"rec 영역 크기 {self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2}\n좌표")
    #         self.drawing.rect3_info.setFont(QtGui.QFont("굴림",5))
    #         self.qp.setPen(QPen(Qt.blue, 3))
    #         self.qp.drawRect(self.rect3_x1+561, self.rect3_y1+431, self.rect3_x2, self.rect3_y2)

    #     self.qp.end()
    #     self.label.setPixmap(self.canvas)
    #     print("rec1",self.rect1_x1,self.rect1_y1,self.rect1_x2,self.rect1_y2)
    #     print("rec2",self.rect2_x1,self.rect2_y1,self.rect2_x2,self.rect2_y2)
    #     print("rec3",self.rect3_x1,self.rect3_y1,self.rect3_x2,self.rect3_y2)

    def drawing_info_update(self, rec, x1, y1, x2, y2):
        if rec == "rec1":
            self.rec1 = rec
        elif rec == "rec2":
            self.rec2 = rec
        elif rec == "rec3":
            self.rec3 = rec
        
        self.label = self.rec_film  # ui에 지정되어있는 QLabel
        self.canvas = QPixmap(2050, 1150)  # 캔버스 크기 설정
        self.canvas.fill(Qt.transparent)  # 캔버스를 흰색으로 초기화
        self.qp = QPainter(self.canvas)
        self.qp.begin(self)

        if rec == "rec1":
            self.rect1_x1 = x1
            self.rect1_y1 = y1
            self.rect1_x2 = x2
            self.rect1_y2 = y2
        if rec == "rec2":
            self.rect2_x1 = x1
            self.rect2_y1 = y1
            self.rect2_x2 = x2
            self.rect2_y2 = y2
        if rec == "rec3":
            self.rect3_x1 = x1
            self.rect3_y1 = y1
            self.rect3_x2 = x2
            self.rect3_y2 = y2


        self.drawing.rect1_info.setText(f"rec 영역 크기 {self.rect1_x1, self.rect1_y1, self.rect1_x2, self.rect1_y2}\n좌표")
        self.drawing.rect1_info.setFont(QtGui.QFont("굴림",5))
        self.drawing.rect2_info.setText(f"rec 영역 크기 {self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2}\n좌표")
        self.drawing.rect2_info.setFont(QtGui.QFont("굴림",5))
        self.drawing.rect3_info.setText(f"rec 영역 크기 {self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2}\n좌표")
        self.drawing.rect3_info.setFont(QtGui.QFont("굴림",5))

        self.qp.setPen(QPen(Qt.red, 3))
        self.qp.drawRect(self.rect1_x1+561, self.rect1_y1+431, self.rect1_x2, self.rect1_y2)
        self.qp.setPen(QPen(Qt.yellow, 3))
        self.qp.drawRect(self.rect2_x1+561, self.rect2_y1+431, self.rect2_x2, self.rect2_y2)
        self.qp.setPen(QPen(Qt.blue, 3))
        self.qp.drawRect(self.rect3_x1+561, self.rect3_y1+431, self.rect3_x2, self.rect3_y2)

        self.qp.end()
        self.label.setPixmap(self.canvas)
        print("rec1",self.rect1_x1,self.rect1_y1,self.rect1_x2,self.rect1_y2)
        print("rec2",self.rect2_x1,self.rect2_y1,self.rect2_x2,self.rect2_y2)
        print("rec3",self.rect3_x1,self.rect3_y1,self.rect3_x2,self.rect3_y2)
    ########################


    # def paintEvent(self, event):
        
    #     # qp.setGeometry((20,130), 561, 431)
    #     qp.begin(self)
    #     self.draw_rect(qp)
    #     qp.end()
    # # Drawing

    # def draw_rect(self, qp):
    #     # rect1
    #     if self.rect1_x1 != None:
    #         print("그리기 실행은 되셧어")
    #         # qp.setBrush(QColor(180, 100, 160))
    #         qp.setPen(QPen(QColor(60, 60, 60), 3))
    #         qp.drawRect(self.rect1_x1+561, self.rect1_y1+431, self.rect1_x2, self.rect1_y2)

    #     if self.rect2_x1 != None:
    #         qp.setBrush(QColor(40, 150, 20))
    #         qp.setPen(QPen(Qt.blue, 2))
    #         qp.drawRect(self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2)


    #     if self.rect3_x1 != None:
    #         qp.setBrush(Qt.yellow)
    #         qp.setPen(QPen(Qt.red, 5))
    #         qp.drawRect(self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2)

        # if self.rect1_x1 != None:
        #     rect1 = QGraphicsRectItem()
        #     rect1.setRect(self.rect1_x1, self.rect1_y1, self.rect1_x2, self.rect1_y2)
        #     # rect1.setBrush(Qt.yellow)
        #     rect1.setPen(QPen(Qt.red, 5))
        #     scene1 = QGraphicsScene()
        #     scene1.addItem(rect1)
        #     view = self.rect_rec
            
        #     view.setScene(scene1)
        #     view.show()

        # if self.rect2_x1 != None:
        #     rect2 = QGraphicsRectItem()
        #     rect2.setRect(self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2)
        #     # rect2.setBrush(Qt.red)
        #     rect2.setPen(QPen(Qt.red, 5))
        #     scene2 = QGraphicsScene()
        #     scene2.addItem(rect2)
        #     view = self.rect_rec
            
        #     view.setScene(scene2)
        #     view.show()

        # if self.rect3_x1 != None:
        #     rect3 = QGraphicsRectItem()
        #     rect3.setRect(self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2)
        #     # rect3.setBrush(Qt.blue)
        #     rect3.setPen(QPen(Qt.red, 5))
        #     scene3 = QGraphicsScene()
        #     scene3.addItem(rect3)
        #     view = self.rect_rec
            
        #     view.setScene(scene3)
        #     view.show()
    # self.rect_rec


    def open_setting(self):
        pass
    # 검색

    # 연결 위젯 : Log_list    | 속성 : QListWidget
    # 기능 : 로그 리스트를 제공하는 위젯에 정보를 전달하는 함수
    # 설명 : ListView가 아닌 Widget를 이용해 정보를 제공한다. 오토 스크롤 기능이 있다.
    def showlist(self):
        # 리스트로 일단 구현. 해당 리스트에서 추가된 것들 보여주는 용.
        text = [
            "로그 형식","원본영상이름 랙번호 case번호 발생시간 새영상저장위치", "발생시간: systime", "랙번호(지게차-사람 순)", "0번 oo",
            "1번 xx","2번 ox","3번 xo",
            "ex1) 20231129095500 rec1 case1 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec3 case2 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec1 case2 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec0 case2 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec1 case3 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec1 case2 11.21-10:00:57 ..\logvideo\20231129095500.avi?"
            "ex1) 20231129095500 rec2 case2 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec1 case3 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec3 case2 11.21-10:00:57 ..\logvideo\20231129095500.avi?",
            "ex1) 20231129095500 rec2 case2 11.21-10:00:57 ..\logvideo\20231129095500.avi?"
        ]
        for i in text:
            self.Log_list.addItem(f"{i}")

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
                self.video_stop()   # 이미 
            self.video_thread = ThreadOfVideo(self.video_file, self.video_frame)
            # 시그널이 이렇게 많아지면 조금 복잡? 비효율적이지 않나. (질문 1)
            self.video_thread.pixmap_signal.connect(self.update_frame)  # 영상 cv정보(pixmap)를 받아오는 시그널, QPix... 쟤는 메인 쓰레드에서 처리되어야한다.
            self.video_thread.video_playing_signal.connect(self.playing_label_change)  # VideoOfThread에서 length (int) 받아옴
            self.video_thread.info_signal.connect(self.video_totaltime_label)  # VideoOfThread에서 length (int), fps (float) 받아옴
            self.video_thread.info_signal.connect(self.print_video_info)
            self.video_thread.silder_signal.connect(self.silder_change)  # VideoOfThread에서 length (int), fps (float), current_time (int) 받아옴

            self.video_thread.start()

    # 연결 위젯 : playing_silder    | 속성 : QSlider
    # 기능 : 슬라이더 재생바의 위치를 조정한다.
    # 설명 : length와 fps로 영상의 재생길이를 계산하고, 현재 영상의 프레임 번호를 이용해 현 시점을 계산한다. 그 위치로 slider의 바 위치 값을 변동한다.
    # 비고 : silder_signal에서 아래 args 3개를 받아온다.
    def silder_change(self, length, fps, current_time):
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
    def video_stop(self):
        if self.video_playing:  # 실행중이라면 스탑
            self.video_thread.stop()

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
                time = int(current_time)
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


# 여기에는 스레드 멈추고 일시정지하고 그러는 기능 밖에 없어. 두 클래스간 공유하느 ㄴ파라미터도 없다.
class ThreadOfVideo(QThread, form_class):
    # 쓰레드 간의 시그널 모음
    pixmap_signal = pyqtSignal(QPixmap)  # 메인 스레드 쓰지말고 시그널만 줘 ....
    info_signal = pyqtSignal(int, float)  # 영상 정보용 시그널 / length, fps
    video_playing_signal = pyqtSignal(int)  # 현재 영상 프레임 번호 전송
    silder_signal = pyqtSignal(int, float, int)  # length, fps, 현재 프레임 번호 전송

    def __init__(self, video_file, video_frame):
        super().__init__()
        self.video_file = video_file
        self.running = True  # 루프 상태 제어
        self.pause = False  # 일시정지 상태
        self.video_frame = video_frame
        self.length = None
        self.fps = None
        self.current_time = None
        self.now_frame = None
        self.move_control = None

    # 여기서 signal로 메인 스레드로 그냥 신호만 주는 식으로 영상 처리하는.... 고.
    # 설명 : 메인쓰레드에서 영상 재생을 시작하면 영상 쓰레드가 호출되며 실행되는 함수
    # 기능 : cv기반으로 영상을 처리한다. 추후 Yolo와 연동해야한다 ....
    def run(self):
        if self.video_file:
            cap = cv2.VideoCapture(self.video_file)  # 저장된 영상 가져오기 프레임별로 계속 가져오는 듯
            self.length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.fps = cap.get(cv2.CAP_PROP_FPS)
            # print(f"영상 길이 : {self.length}    |   width&hegith {width}&{height}     |   fps : {self.fps}")
            self.info_signal.emit(self.length, self.fps)  # info_signal을 통해 메인쓰레드로 변수 전송
            while self.running:
                self.ret, self.frame = (cap.read())  # 알아서 0번부터 끝까지 착실히 넘어가면서 수행
                # cap.set(cv2.CAP_PROP_POS_FRAMES, )   N번부터 실행


                ## AR 모델 ##
                result = model.predict(self.frame)
                for r in result:
                    self.frame = r.plot()
                ## AR 모델 ##
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

                if self.pause:
                    time.sleep(1)
                    continue
                if self.ret:
                    self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  # 프레임에 색 입히기
                    self.convertToQtFormat = QImage(self.rgbImage.data,self.rgbImage.shape[1],self.rgbImage.shape[0],QImage.Format_RGB888,)
                    self.pixmap = QPixmap(self.convertToQtFormat)  # 이 부분이 메인스레드에서 처리되어야하는 QPixmap이 있어서 2개 다 잡아먹고 있는거다?
                    self.p = self.pixmap.scaled(2050, 1150, QtCore.Qt.IgnoreAspectRatio)  # 프레임 크기 조정 1920, 1080 후보 1
                    # frame_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                    self.current_time = cap.get(cv2.CAP_PROP_POS_MSEC) * 0.001  # 밀리초 단위 현재 위치
                    self.video_playing_signal.emit(self.current_time)  # video_playing_signal을 통해 메인쓰레드로 변수 전송
                    self.silder_signal.emit(self.length, self.fps, self.current_time)

                    # self.video_frame.setPixmap(self.p)  # NoneType 오류가 계속 떠요
                    # 위 코드에서 아래 코드로 바꾸니까 강제 종료 되던 것이 해결이 .. 되었음.
                    self.pixmap_signal.emit(self.p)
                    self.video_frame.update()  # 프레임 띄우기
                    sleep(0.01)  # 영상 1프레임당 0.01초로 이걸로 영상 재생속도 조절하면됨 0.02로하면 0.5배속인거임
                    # delay = int(self.fps/1000)
                    # # cv2.waitKey(delay)  # fps에 맞게 프레임 지연이라는데 이게 sleep이랑 같은 역할을 하나?
                    # sleep(delay)
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


# 콜백 func
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainView()
    myWindow.show()
    app.exec_()
