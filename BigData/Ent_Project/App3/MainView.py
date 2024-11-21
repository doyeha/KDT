from PyQt5.QtWidgets import *
from PyQt5 import uic
from setting import settingsView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QPixmap, QImage
import sys
import time, datetime

# 영상 관련 import
import cv2
from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal    # 영상 처리 멀티스레드 // 메인스레드 - 영상용 스레드 신호 연결 목적
import threading
from PyQt5 import QtWidgets, QtGui, QtCore

form_class = uic.loadUiType("MainView.ui")[0]
 
# 메인뷰 540 x 420 
class MainView(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 영상 띄우기
        self.video_frame = self.findChild(QtWidgets.QLabel, "video_frame")
        self.video_frame.setStyleSheet("background-color: black;")  # 영상 없음 검은 호ㅜㅏ면 해 
        # self.video_thread(video_file)

        self.video_thread = None

        # 리스트뷰 띄우는 부분.
        self.showlist()

        # jy_ui 추가
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("NEMONEMO")



    # 세팅 가는 버튼 def
    def go_setting(self) :
        self.w = settingsView()
        self.w.show()

    # 로그 리스트 (됐!ㅆ싸빌!!!!)
    def showlist(self):
        # # QListwidget으로 변형 후
        # 리스트로 일단 구현. 해당 리스트에서 추가된 것들 보여주는 용.
        text = ["24-11-14_18:22:13_103", "24-11-14_18:24:13_103", "24-11-14_18:30:13_103", "24-11-14_18:40:13_103"]
        for i in text:
            self.Log_list.addItem(f"{i}")

    # 파일 선택해서 재생
    def load_video(self):
        if self.video_thread:
            # self.video_pause()   # 앞에 이미 실행중이라면 완전 스탑
            self.video_thread.stop()
        # 파일을 선택하는 함수
        video_file = self.video_FileLoad()
        if video_file:  # 파일이 선택되었으면
            self.video_playing = True
            self.video_thread = ThreadOfVideo(video_file, self.video_frame)
            self.video_thread.pixmap_signal.connect(self.update_frame)
            self.video_thread.start()
            self.change_label()

    def update_frame(self, pixmap):
        self.video_frame.setPixmap(pixmap)

    # 영상 파일 넣는 버튼
    # 파일 불러오기 | https://newbie-developer.tistory.com/122 참고
    def video_FileLoad(self):        
        fname=QFileDialog.getOpenFileName(self)    # QFileDialog 자체가 파일 불러오기 기능. App2 디렉토리가 열린다.
        # print("fname : ", fname)    # 튜플 형식으로 나온다. (문서 위치, 나온 문서들의 형식 ex All Files)
        print(fname[0])
        return fname[0]
    
    # 완전 스탑
    def video_stop(self):   
        if self.video_playing:  # 실행중이라면 스탑
            self.video_thread.stop()

    # 일시정지
    def video_pause(self):
        if self.video_thread:
            self.video_thread.toggle_pause()
        
 
    def change_label(self):
        if self.video_thread:
            self.length = self.video_thread.video_info()
            if type(self.length) == int:
                self.length = str(datetime.timedelta(seconds=self.length))
            else:
                self.length = str(self.length)
            self.video_total_label.setText(self.length)






# 여기에는 스레드 멈추고 일시정지하고 그러는 기능 밖에 없어. 두 클래스간 공유하느 ㄴ파라미터도 없다.
class ThreadOfVideo(QThread, form_class):
    pixmap_signal = pyqtSignal(QPixmap) # 메인 스레드 쓰지말고 시그널만 줘 .... 
    def __init__(self, video_file, video_frame):
        super().__init__()
        # self.setupUi(self)
        self.video_file = video_file
        self.running = True  # 루프 상태 제어
        self.pause = False   # 일시정지 상태
        self.video_frame = video_frame
        self.length = 0
        self.fps = 0
        

    # 여기서 signal로 메인 스레드로 그냥 신호만 주는 식으로 영상 처리하는.... 고.
    def run(self):
        if self.video_file:
            cap = cv2.VideoCapture(self.video_file) #저장된 영상 가져오기 프레임별로 계속 가져오는 듯
            self.length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.fps = cap.get(cv2.CAP_PROP_FPS)
            print(f"영상 길이 : {self.length}    |   width&hegith {width}&{height}     |   fps : {self.fps}")
            while self.running: # 여기서 무한리필집으로 주고 있는데 어케 멈추노 아 배고파
                self.ret, self.frame = cap.read() #영상의 정보 저장
                if self.pause:
                    time.sleep(1)
                    continue

                if self.ret:
                    self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) #프레임에 색 입히기
                    self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
                    self.pixmap = QPixmap(self.convertToQtFormat)   # 이 부분이 메인스레드에서 처리되어야하는 QPixmap이 있어서 2개 다 잡아먹고 있는거다?
                    self.p = self.pixmap.scaled(2050, 1150, QtCore.Qt.IgnoreAspectRatio) #프레임 크기 조정 1920, 1080 후보 1
                    self.video_frame.setPixmap(self.p)  # NoneType 오류가 계속 떠요
                    self.video_frame.update() #프레임 띄우기
                    sleep(0.01)  # 영상 1프레임당 0.01초로 이걸로 영상 재생속도 조절하면됨 0.02로하면 0.5배속인거임
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
            self.running = False

    def video_info(self):
        if self.running:
            try:
                runtime = self.length/self.fps
            except:
                runtime = 0
        else:
            runtime = "오류 있음"
        return runtime
    

            

    def stop(self):
        self.running = False
        self.wait()

    def toggle_pause(self):
        self.pause = not self.pause

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    myWindow = MainView() 
    myWindow.show()
    # myWindow.video_thread(form_class)
    app.exec_()