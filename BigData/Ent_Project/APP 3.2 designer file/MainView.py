from PyQt5.QtWidgets import *
from PyQt5 import uic
from setting import settingsView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QPixmap, QImage
import sys

# 영상 관련 import
import cv2
from time import sleep
import threading
from PyQt5 import QtWidgets, QtGui, QtCore


form_class = uic.loadUiType("MainView.ui")[0]

# 메인뷰 540 x 420 
class MainView(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # self.video_playing = False 
        # video_file = self.video_FileLoad()
        # self.video_file = 
        # 영상 띄우기
        self.video_frame = self.findChild(QtWidgets.QLabel, "video_frame")
        self.video_frame.setStyleSheet("background-color: black;")  # 영상 없음 검은 호ㅜㅏ면 해 
        # self.video_thread(video_file)

        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("NEMONEMO")

        


    # 세팅 가는 버튼 def
    def go_setting(self) :
        self.w = settingsView()
        self.w.show()

    # 로그 리스트 (미구현)
    def showlist(self):
        text = ["24-11-14_18:22:13_103", "24-11-14_18:24:13_103", "24-11-14_18:30:13_103", "24-11-14_18:40:13_103"]
        model = QStandardItemModel()
        for x in text:
            model.appendRow(QStandardItemModel(x))
        self.ui.listView.setModel(model)
    
    def load_video(self):
        # 파일을 선택하는 함수
        video_file = self.video_FileLoad()
        if video_file:  # 파일이 선택되었으면
            # self.video_playing = True
            self.video_thread(video_file) 


    # 영상 파일 넣는 버튼
    # 파일 불러오기 | https://newbie-developer.tistory.com/122 참고
    def video_FileLoad(self):        
        fname=QFileDialog.getOpenFileName(self)    # QFileDialog 자체가 파일 불러오기 기능. App2 디렉토리가 열린다.
        # print("fname : ", fname)    # 튜플 형식으로 나온다. (문서 위치, 나온 문서들의 형식 ex All Files)
        # print("fname[0]: ", fname[0])  # print("fname[1]: ",fname[1]) 
        print(fname[0])
        return fname[0]
    

    def Video_to_frame(self, video_file):
        video_check = None
        # print("video_file :", video_file)
        if video_file:
            cap = cv2.VideoCapture(video_file) #저장된 영상 가져오기 프레임별로 계속 가져오는 듯
            video_check = True
            ###cap으로 영상의 프레임을 가지고와서 전처리 후 화면에 띄움###
            ## 새로운 영상 오면 멈춰야함.
            while True:
                self.ret, self.frame = cap.read() #영상의 정보 저장
                if self.ret:
                    self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) #프레임에 색입히기
                    self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
                    self.pixmap = QPixmap(self.convertToQtFormat)
                    self.p = self.pixmap.scaled(2050, 1150, QtCore.Qt.IgnoreAspectRatio) #프레임 크기 조정 1920, 1080 후보 1
                    self.video_frame.setPixmap(self.p)
                    self.video_frame.update() #프레임 띄우기
                    sleep(0.01)  # 영상 1프레임당 0.01초로 이걸로 영상 재생속도 조절하면됨 0.02로하면 0.5배속인거임
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
            self.video_playing = False 
        
    def video_thread(self,video_file):
        # thread = threading.Thread(target=self.Video_to_frame(video_file))
        thread = threading.Thread(target=self.Video_to_frame, args=(video_file,))
        thread.daemon = True  # 프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    myWindow = MainView() 
    myWindow.show()
    # myWindow.video_thread(form_class)
    app.exec_()