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
from PyQt5.QtCore import Qt
import threading
from collections import deque 
import warnings
warnings.simplefilter("ignore", DeprecationWarning) # deprecated 오류메세지 ignore 목적

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


form_class = uic.loadUiType("./ui/setting.ui")[0]

class settingsView(QMainWindow, form_class) :
    def __init__(self, signal) :
        super().__init__()
        self.setupUi(self)
        # yj_ui 추가
        self.setWindowIcon(QIcon("./img/setting_img.png"))
        self.signal = signal

        # 디폴트 값
        self.helmet = True
        self.reck = True
        self.crush = True
        # print("세팅 초기 설정 :",self.helmet, self.reck, self.crush)

        # self.checkBox.stateChanged.connect(self.update_alarm_settings)      # 안전모
        # self.checkBox_2.stateChanged.connect(self.update_alarm_settings)    # 위험구역
        # self.checkBox_3.stateChanged.connect(self.update_alarm_settings)     # 충돌


    #알람 설정 '확인' 버튼
    def ok(self):
        self.helmet = self.checkBox.isChecked()
        self.reck = self.checkBox_2.isChecked()
        self.crush = self.checkBox_3.isChecked()
        self.signal.ram_setting_info_signal.emit(self.helmet, self.reck, self.crush)

    #알람 설정 '초기화' 버튼
    def reset(self):
        pass

    #파일 저장 경로 '폴더' 버튼
    def path(self):
        pass


# if __name__ == "__main__" :
#     app = QApplication(sys.argv) 
#     myWindow = settingsView() 
#     myWindow.show()
#     app.exec_()