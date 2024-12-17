from PyQt5.QtCore import QObject, pyqtSignal
import sys
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5 import uic

from PyQt5.QtCore import pyqtSignal
import pandas as pd

    
# 쌍방 import 문제로 시그널 모음집 해서 각자 끌어쓰는 식으로 진행.
class collectionOfSignals(QObject):
    # rect_info_signal = pyqtSignal(str, int, int, int, int)

    # 프리뷰 이미지 영상쓰레드 ->메인 /  메인에서 다시 드로잉으로 
    preview_pixmap_signal = pyqtSignal(QPixmap)
    

    # 영상 thread 시그널 
    pixmap_signal = pyqtSignal(QPixmap)  # 메인 스레드 쓰지말고 시그널만 줘 ....
    info_signal = pyqtSignal(int, float)  # 영상 정보용 시그널 / length, fps
    video_playing_signal = pyqtSignal(int)  # 현재 영상 프레임 번호 전송
    silder_signal = pyqtSignal(int, float, int)  # length, fps, 현재 프레임 번호 전송
    drawing_preview_signal = pyqtSignal(QPixmap)

    accident_signal=pyqtSignal(pd.DataFrame)        # 교통사고 건 전송

    # drawing
    rect_info_signal = pyqtSignal(str,int, int, int, int)

    log_fps_signal = pyqtSignal(int, float, int)
    # drawing - PaintView
    # rect_signal = pyqtSignal(int, int, int, int)

    # log_maker -> MainView로 새로운 리스트아이템 전달
    loglist_signal = pyqtSignal(str)

    alram_signal = pyqtSignal(str)

    # 로그 발생 시 -> 렉, 사고 정보 전달 // 비디오 저장 목적
    aci_info_signal = pyqtSignal(int, str)

    update_alarm_settings_signal = pyqtSignal(dict)


    back_p_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()