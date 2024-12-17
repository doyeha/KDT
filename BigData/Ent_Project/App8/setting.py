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

# import resources.resources_rc


form_class = uic.loadUiType("./ui/setting.ui")[0]

class settingsView(QMainWindow, form_class):
    def __init__(self, signals):
        super().__init__()
        self.setupUi(self)

        # 설정 아이콘
        self.setWindowIcon(QIcon("./img/setting_img.png"))
        self.signals = signals

        # 초기 알람 상태
        self.alarm_settings = {
            'helmet': True,
            'car': True,
            'rack': True
        }

        # 체크박스 상태 변경 시 신호 연결
        self.helmet_alram.stateChanged.connect(self.update_alarm_settings)
        self.rack_alram.stateChanged.connect(self.update_alarm_settings)
        self.car_alram.stateChanged.connect(self.update_alarm_settings)

    def update_alarm_settings(self):
        self.alarm_settings['helmet'] = self.helmet_alram.isChecked()
        self.alarm_settings['car'] = self.rack_alram.isChecked()
        self.alarm_settings['rack'] = self.car_alram.isChecked()

        print(f"Current alarm settings (before emit): {self.alarm_settings}")
        self.signals.update_alarm_settings_signal.emit(self.alarm_settings)

    
    def ok(self):
        # print("설정 확인 버튼 클릭됨")
        # QMessageBox.information(self,'DONE','설정 완료')
        # for alarm, is_active in self.alarm_settings.items():
        #     if is_active:
        #         # print(f'{alarm} 알람 활성화 시도')
        #         self.signals.alram_signal.emit(alarm)


        self.savemode = self.logvideo_combox.currentText()
        if self.savemode == "효율 저장 (저화질 압축으로 인한 영상 화질 저하 발생)":
            self.savemode = "효율 저장"

        elif self.savemode == "고화질 (1920x1080)":
            self.savemode = "고화질"

        elif self.savemode == "일반화질 (1280x720)":
            self.savemode = "일반화질"
        else:
            pass
        print(self.savemode)

        # 디폴트는 효율 저장
        self.signals.back_p_signal.emit(self.savemode)

    # 알람 설정 '초기화' 버튼
    def Alram_setting_reset(self):
        self.helmet_alram.setChecked(True)
        self.rack_alram.setChecked(True)
        self.car_alram.setChecked(True)
        # self.alarm_settings = {'helmet': True, 'car': True, 'rack': True}
        # self.update_alarm_settings()  # 초기화 후 상태 업데이트

    

    ## 영상 저장 설정
