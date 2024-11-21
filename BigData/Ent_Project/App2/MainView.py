from PyQt5.QtWidgets import *
from PyQt5 import uic
from setting import settingsView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QPixmap, QImage
import sys
import time

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

        self.first_file = None
        self.second_file = None
        self.stop_btn_press = False

        # 리스트뷰 띄우는 부분.
        self.showlist()




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


    # 오류오류 1번째껏만 실행이 됨.
    # def file_check(self, video_file):
    #     if self.first_file is None:
    #         self.first_file = video_file
    #         return True
        
    #     if video_file == self.first_file:
    #         return True
    #     else:
    #         self.first_file=None
    #         return False
        
    def video_stop(self):
        if self.stop_btn_press:
            self.stop_btn_press = False
        else:
            self.stop_btn_press = True
        print("버튼 눌리기는 함???", self.stop_btn_press)
        return self.stop_btn_press
        

    def Video_to_frame(self, video_file):
        if video_file:
            cap = cv2.VideoCapture(video_file) #저장된 영상 가져오기 프레임별로 계속 가져오는 듯
            ###cap으로 영상의 프레임을 가지고와서 전처리 후 화면에 띄움###
            ## 새로운 영상 오면 멈춰야함.
            # 내가? 영상을 재생중이야. 그럼 while문에서 졸라 열심히 돌리고 있는거겠지?
            #  근데, 내가 새로운 영상을 선택했어. 그럼뭐해. while문 멈춰야지!
            sc = 0
            while True: # 여기서 무한리필집으로 주고 있는데 어케 멈추노 아 배고파
                # filename = video_file

                # check_point =  self.file_check(video_file)    # 실
                # if check_point:                               # 패    
                #     pass
                # else:
                #     break                                     # 함
                # While문 하나 더 넣어서 이전에 넣은 파일명이 맞는지 확인하고 아니면 그것만 할까 ?
                self.ret, self.frame = cap.read() #영상의 정보 저장
                # while self.stop_btn_press:
                #     time.sleep(1)
                sc += 1
                if sc % 50 == 0: 
                    print(self.stop_btn_press)
                if self.ret:
                    self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) #프레임에 색입히기
                    self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
                    self.pixmap = QPixmap(self.convertToQtFormat)   # 이 부분이 메인스레드에서 처리되어야하는 QPixmap이 있어서 2개 다 잡아먹고
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
        video_thread = threading.Thread(target=self.Video_to_frame, args=(video_file,))   # PyQT5는 단일 스레드 이기 때문에 다른 스레드에서 처리하도록 지정.
        video_thread.daemon = True  # 프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)    # args = Video_to_frame에 전달할 매개변수를 지정
        video_thread.start()

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    myWindow = MainView() 
    myWindow.show()
    # myWindow.video_thread(form_class)
    app.exec_()