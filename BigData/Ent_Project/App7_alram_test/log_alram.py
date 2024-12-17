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
from PyQt5.QtCore import QTimer

class Alram(QThread):
    def __init__(self, signal, red_base, helmet, info_list): # 시그널이랑 메인뷰에 띄울 QLabel 2개 띄워야함. 붉은 색 + 그림. 
        super().__init__()
        self.signal = signal
        self.Alram_red = red_base
        self.helmet_alram = helmet
        self.helmet_set, self.reck_set, self.crush_set = True, True, True
        

    def run(self):
        self.signal.ram_setting_info_signal.connect(self.setting_info_receiver)
        self.signal.alram_signal.connect(self.show_popup)

    def setting_info_receiver(self, helmet, reck, crush):
        self.helmet_set = helmet
        self.reck_set = reck
        self.crush_set = crush


    def show_popup(self, case):
        image_path = os.path.join(current_dir, 'img', 'helmet.png')
        image_path = os.path.abspath(image_path)
        pixmap = QPixmap(image_path)
        
        if case == "helmet" and self.helmet_set:
            blink_time = 300
            self.Alram_red.setStyleSheet("background-color: rgba(255, 0, 0, 125);")  # alpha 값도 최대 255
            self.helmet_alram.setPixmap(pixmap)
            # 유감스럽게도 for문이 안돌아감.
            QTimer.singleShot(blink_time*1, lambda: self.Alram_red.setStyleSheet("background-color: rgba(255, 0, 0, 0);"))
            QTimer.singleShot(blink_time*1, lambda: self.helmet_alram.clear())

            QTimer.singleShot(blink_time*2, lambda: self.Alram_red.setStyleSheet("background-color: rgba(255, 0, 0, 125);"))
            QTimer.singleShot(blink_time*2, lambda: self.helmet_alram.setPixmap(pixmap))
            QTimer.singleShot(blink_time*3, lambda: self.Alram_red.setStyleSheet("background-color: rgba(255, 0, 0, 0);"))
            QTimer.singleShot(blink_time*3, lambda: self.helmet_alram.clear())

            QTimer.singleShot(blink_time*4, lambda: self.Alram_red.setStyleSheet("background-color: rgba(255, 0, 0, 125);"))
            QTimer.singleShot(blink_time*4, lambda: self.helmet_alram.setPixmap(pixmap))
            QTimer.singleShot(blink_time*5, lambda: self.Alram_red.setStyleSheet("background-color: rgba(255, 0, 0, 0);"))
            QTimer.singleShot(blink_time*5, lambda: self.helmet_alram.clear())



            # message_label.setText("헬멧 미착용 경고!")
            # message_label.setStyleSheet("color: red; font-size: 60px;")  

            # sound_file_path = r"C:\Users\a\Desktop\App6\bbibbi.wav"


            
            # image_label.setAlignment(Qt.AlignCenter)  # 중앙 정렬
            # layout.addWidget(image_label)  # 이미지 설정




        
        # dialog = QDialog()
        # dialog.setWindowTitle("Warning")
        # dialog.resize(500, 300)

        # layout = QVBoxLayout()

        # # 메시지 내용 및 색깔 설정
        # message_label = QLabel()
        # image_label = QLabel()

        # # 현재 스크립트 파일의 경로
        # current_dir = os.path.dirname(os.path.realpath(__file__))

        # # 'APP6' 폴더 내의 'bbibbi.wav' 파일 경로
        # sound_file_path = os.path.join(current_dir, 'bbibbi.wav')
        # sound_file_path = os.path.abspath(sound_file_path)

        # if case == 'helmet':
        #     # message_label.setText("헬멧 미착용 경고!")
        #     # message_label.setStyleSheet("color: red; font-size: 60px;")  

        #     # sound_file_path = r"C:\Users\a\Desktop\App6\bbibbi.wav"


        #     image_path = os.path.join(current_dir, 'img', 'helmet.png')

        #     # 절대 경로로 변환
        #     image_path = os.path.abspath(image_path)

        #     pixmap = QPixmap(image_path)
        #     image_label.setPixmap(pixmap)  # 이미지 설정
        #     image_label.setAlignment(Qt.AlignCenter)  # 중앙 정렬
        #     layout.addWidget(image_label)  # 이미지 설정

        # elif case == 'car':
        #     message_label.setText("사고 발생 경고!")
        #     message_label.setStyleSheet("color: orange; font-size: 60px bold;")  # 주황색
        #     # sound_file_path = r"C:\Users\a\Desktop\App6\bbibbi.wav"
        #     #소리 재생
        #     QSound.play(sound_file_path)
        #     image_label.clear()
            
        # elif case == 'reck':
        #     message_label.setText("위험 경고! 즉시 확인하세요!")
        #     message_label.setStyleSheet("color: red; font-size: 60px bold;")  # 빨간색
        #     # sound_file_path = r"C:\Users\a\Desktop\App6\bbibbi.wav"
        #     #소리 재생
        #     QSound.play(sound_file_path)
        #     image_label.clear()

        # if case != 'helmet':  # 헬멧 미착용 경고가 아닐 때만 텍스트 추가
        #     h_layout = QHBoxLayout()
        #     h_layout.addWidget(message_label, alignment=Qt.AlignCenter)  # 메시지 중앙 배치
        #     layout.addLayout(h_layout)

        

        # # OK 버튼 추가
        # ok_button = QPushButton("확인")
        # ok_button.clicked.connect(dialog.accept)
        # layout.addWidget(ok_button,alignment=Qt.AlignCenter)

        # dialog.setLayout(layout)
        
        # dialog.exec_()
