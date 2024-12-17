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
        self.signal.alram_signal.connect(self.show_popup)
        self.signal.update_alarm_settings_signal.connect(self.update_alarm_settings)  # 알람 설정 상태 업데이트
        
        self.current_dialog = None
        self.should_stop = False
        
        # 초기 알람 상태
        self.alarm_settings = {
            'helmet': True,
            'car': True,
            'rack': True
        }

    # 알람 상태 설정
    def update_alarm_settings(self, alarm_settings):
        print(f'before:{self.alarm_settings}')
        self.alarm_settings = alarm_settings
        print(f"Updated alarm settings: {self.alarm_settings}")

    def show_popup(self, case):
        print(f"Received case: {case}")

        # 알람 비활성화 상태 확인
        if case in self.alarm_settings and not self.alarm_settings[case]:
            print(f"알람 비활성화 활동 x")
            return  # 알람이 비활성화된 경우 아무 작업도 하지 않음

        # None일 경우 다이얼로그를 닫고 종료
        if case is None:
            if self.current_dialog:
                self.current_dialog.close()
                self.current_dialog = None
            return

        # 현재 다이얼로그가 열려 있으면 닫기
        if self.current_dialog:
            self.current_dialog.close()

        self.current_dialog = QDialog()
        self.current_dialog.setWindowTitle("Warning")
        self.current_dialog.resize(500, 300)

        layout = QVBoxLayout()
        message_label = QLabel()
        image_label = QLabel()

        current_dir = os.path.dirname(os.path.realpath(__file__))
        sound_file_path = os.path.join(current_dir, 'bbibbi.wav')
        sound_file_path = os.path.abspath(sound_file_path)

        if case == 'helmet':
            image_path = os.path.join(current_dir, 'img', 'helmet.png')
            pixmap = QPixmap(image_path)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(image_label)

        elif case == 'car':
            message_label.setText("사고 발생 경고!")
            message_label.setStyleSheet("color: orange; font-size: 60px;")
            QSound.play(sound_file_path)

        elif case == 'rack':
            message_label.setText("위험 경고! 즉시 확인하세요!")
            message_label.setStyleSheet("color: red; font-size: 60px;")
            QSound.play(sound_file_path)

        # 메시지를 중앙에 배치
        if case in ['car', 'rack']:
            h_layout = QHBoxLayout()
            h_layout.addWidget(message_label, alignment=Qt.AlignCenter)
            layout.addLayout(h_layout)

        # OK 버튼 추가
        ok_button = QPushButton("확인")
        ok_button.clicked.connect(self.current_dialog.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)

        self.current_dialog.setLayout(layout)
        
        self.current_dialog.exec_()

    def close_dialog(self):
        """다이얼로그를 닫고 알람을 비활성화합니다."""
        if self.current_dialog:
            self.current_dialog.close()
            self.current_dialog = None

    def run(self):
        """스레드가 수행할 작업을 정의합니다."""
        while not self.should_stop:
            # 여기에 스레드가 수행할 작업을 추가
            time.sleep(0.1)  # CPU 사용량 감소를 위해 대기

    def stop(self):
        """스레드를 안전하게 종료하는 메서드"""
        self.should_stop = True
        self.wait()  # 스레드가 종료될 때까지 대기
