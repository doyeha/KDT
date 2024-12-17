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

        # 알람 설정 상태를 저장하기 위한 딕셔너리
        self.alarm_settings = {
            'helmet': self.checkBox.isChecked(),
            'car': self.checkBox_2.isChecked(),
            'rack': self.checkBox_3.isChecked()
        }

        # 체크박스 상태 변경 시 신호 연결
        self.checkBox.stateChanged.connect(self.update_alarm_settings)
        self.checkBox_2.stateChanged.connect(self.update_alarm_settings)
        self.checkBox_3.stateChanged.connect(self.update_alarm_settings)

    def update_alarm_settings(self):
        # 체크박스 상태 업데이트
        self.alarm_settings['helmet'] = self.checkBox.isChecked()
        self.alarm_settings['car'] = self.checkBox_2.isChecked()
        self.alarm_settings['rack'] = self.checkBox_3.isChecked()

        # 알람 설정 상태 변경 시 신호 발생
        self.signals.update_alarm_settings_signal.emit(self.alarm_settings)

    # 알람 설정 '확인' 버튼
    def ok(self):
        print("설정 확인 버튼 클릭됨")
        QMessageBox.information(self,'DONE','설정 완료')
        # 알람 설정을 신호로 전파
        # for alarm, is_active in self.alarm_settings.items():
        #     if is_active:
        #         print(f'{alarm} 알람 활성화 시도')
        #         self.signals.alram_signal.emit(alarm)

    # 알람 설정 '초기화' 버튼
    def reset(self):
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.alarm_settings = {'helmet': True, 'car': True, 'rack': True}
        self.update_alarm_settings()  # 초기화 후 상태 업데이트

    # 파일 저장 경로 '폴더' 버튼
    def path(self):
        pass