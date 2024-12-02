from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
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

# from ui.resources_rc import *
# import resources.resources_rc as resources_rc
# import resources.resources_rc
# from resources import resources_rc
sys.path.append(r'C:\Git\KDT\BigData\Ent_Project\App6\resources') 
from resources import *
# import resources.resources_rc


form_class = uic.loadUiType("./ui/setting.ui")[0]

class settingsView(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


# if __name__ == "__main__" :
#     app = QApplication(sys.argv) 
#     myWindow = settingsView() 
#     myWindow.show()
#     app.exec_()