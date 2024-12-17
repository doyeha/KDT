import time, datetime
import cv2
from time import sleep
from PyQt5.QtCore import (QThread, pyqtSignal)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSound
import sys
from setting import settingsView
from PyQt5.QtCore import QTimer

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


class Alram(QThread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal
        self.signal.update_alarm_settings_signal.connect(self.update_alarm_settings)
        self.signal.alram_signal.connect(self.show_popup)

        # 초기 알람 상태
        self.alarm_settings = {
            'helmet': True,
            'car': True,
            'rack': True
        }
        
        self.current_dialog = None  # 현재 다이얼로그를 추적하기 위한 변수
        self.should_stop = False

    def update_alarm_settings(self, alarm_settings):
        self.alarm_settings = alarm_settings
        print(f"업데이트 된 알람 설정: {self.alarm_settings}")

    def show_popup(self, case):
        if self.current_dialog:  # 다이얼로그가 이미 열려 있으면
            print("다이얼로그가 이미 열려 있습니다.")
            return  # 새로운 경고창을 띄우지 않음

        print(f"받은 케이스: {case}")
        print(f"헬멧 알람 상태: {self.alarm_settings.get('helmet', '알람 설정 없음')}")

        # 알람 비활성화 상태 확인
        if case in self.alarm_settings and not self.alarm_settings[case]:
            print("알람 비활성화 활동 x")
            return  # 알람이 비활성화된 경우 아무 작업도 하지 않음

    # 알람이 활성화된 경우 다이얼로그 표시
        self.show_alarm_dialog(case)

    def show_alarm_dialog(self, case):
        """알람 다이얼로그 생성 및 표시"""
        if self.current_dialog:
            self.current_dialog.close()  # 이전 다이얼로그가 열려있으면 닫기

        self.current_dialog = QDialog()
        self.current_dialog.setWindowTitle("Warning")
        self.current_dialog.resize(400, 200)

        layout = QVBoxLayout()
        message_label = QLabel()

        # 다이얼로그 내용 설정
        if case == 'helmet':
            message_label.setText("헬멧 알람 발생!")
            image_path = os.path.join(os.path.dirname(__file__), 'img', 'helmet.png')  # 이미지 경로
            pixmap = QPixmap(image_path)
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)

        elif case == 'car':
            message_label.setText("사고 발생 경고!")
            message_label.setStyleSheet("color: orange; font-size: 24px;")

        elif case == 'rack':
            message_label.setText("위험 경고! 즉시 확인하세요!")
            message_label.setStyleSheet("color: red; font-size: 24px;")

        layout.addWidget(message_label)

        # 확인 버튼 추가
        ok_button = QPushButton("확인")
        ok_button.clicked.connect(self.current_dialog.accept)
        layout.addWidget(ok_button)

        self.current_dialog.setLayout(layout)
        if case == "helmet":
            try:
                QTimer.singleShot(2000, lambda: self.close_dialog())
            except:
                pass
        self.current_dialog.exec_()  # 다이얼로그 실행
        

        self.current_dialog = None  # 다이얼로그가 닫힌 후 변수 초기화
    
    def run(self):
        """스레드가 수행할 작업을 정의합니다."""
        while not self.should_stop:
            # 여기에 스레드가 수행할 작업을 추가
            time.sleep(0.1)  # CPU 사용량 감소를 위해 대기

    def stop(self):
        """스레드를 안전하게 종료하는 메서드"""
        self.should_stop = True
        self.wait() 

    def close_dialog(self):
        # if self.current_dialog:
        #     self.current_dialog.close()
        try:
            self.current_dialog.close()
        except:
            pass