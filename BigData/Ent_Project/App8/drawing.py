import cv2
import sys
from PyQt5.QtGui import *

from PyQt5.QtCore import Qt,QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets,QtGui, QtCore
from PyQt5.QtCore import pyqtSignal
from signal_collection import collectionOfSignals
import time

import sys
import os

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

# from MainView import ThreadOfVideo, MainView

# UI 파일 로드
form_class = uic.loadUiType("./ui/drawing.ui")[0]

class Drawing(QMainWindow, form_class):
    def __init__(self, signal, video_file):
        super().__init__()
        self.setupUi(self)
        self.signal = signal
        self.video_file = video_file
        self.drawing_thread = ThreadOfDrawing(self.signal, self.video_file)
        self.rect_x1, self.rect_y1,self.rect_x2 ,self.rect_y2 = None, None, None, None
        self.drawed_rec_info = None
        self.img = QPixmap('./img/base_pic.png')   # 정상 투명배경으로 바꿔 .,..
        self.screen = self.previewArea
        self.screen.setPixmap(self.img)
        self.signal.preview_pixmap_signal.connect(self.preview_img)

        # self.previewArea.setGeometry(30, 180, 2121, 1201)
        # self.drawingArea.setGeometry(30, 180, 2121, 1201)

        # self.drawingArea.raise_()
        self.paint_view = PaintView(self.drawingArea)
        self.paint_view.rect_signal.connect(self.xy_position)
        self.previewArea.stackUnder(self.drawingArea)

        # 처음 라벨
        # self.rect1_info.setText(f"rec 영역 크기 {self.rect1_x1, self.rect1_y1, self.rect1_x2, self.rect1_y2}\n좌표")
        # self.rect1_info.setFont(QtGui.QFont("굴림",10))
        # self.rect2_info.setText(f"rec 영역 크기 {self.rect2_x1, self.rect2_y1, self.rect2_x2, self.rect2_y2}\n좌표")
        # self.rect2_info.setFont(QtGui.QFont("굴림",10))
        # self.rect3_info.setText(f"rec 영역 크기 {self.rect3_x1, self.rect3_y1, self.rect3_x2, self.rect3_y2}\n좌표")
        # self.rect3_info.setFont(QtGui.QFont("굴림",10))

        # yj_ui 추가
        self.setWindowIcon(QIcon("./img/setting_img.png"))


    def preview_img(self, preview_img):
        self.img = preview_img
        self.screen.setPixmap(self.img)
        # self.paint_view.setStyleSheet("z-index: 2;")


    def xy_position(self, x1, y1, x2, y2):
        self.rect_x1,self.rect_y1,self.rect_x2,self.rect_y2 = x1, y1, x2, y2

    def recxy_send(self):
        if self.radioBtn_rec1.isChecked():      self.signal.rect_info_signal.emit("rec1",self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)
        elif self.radioBtn_rec2.isChecked():    self.signal.rect_info_signal.emit("rec2",self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)
        elif self.radioBtn_rec3.isChecked():    self.signal.rect_info_signal.emit("rec3",self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)
        else:                                   pass
        QMessageBox.information(self,'DONE','설정 완료')


class PaintView(QLabel):
    rect_signal = pyqtSignal(int, int, int, int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(2121, 1201)
    # def __init__(self):
    #     super().__init__()
        self.setMouseTracking(True)  # 마우스 이동을 추적하기 위해 필요
        self.signal = collectionOfSignals()
        self.past_x, self.past_y = None, None
        self.present_x,self.present_y = None, None
        self.rect_x1, self.rect_y1,self.rect_x2,self.rect_y2 = None, None, None, None
        self.rect_is = None

    def paintEvent(self, event):
        # 마우스 이벤트에서 그릴 내용을 처리할 수 있도록 paintEvent 구현
        self.painter = QPainter(self)
        self.painter.begin(self)
        self.rect_is = False
        self.painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))

        if self.past_x is not None and self.present_x is not None:
            self.painter.drawRect(self.past_x, self.past_y, self.present_x - self.past_x, self.present_y - self.past_y)
            self.rect_x1 = self.past_x
            self.rect_y1 = self.past_y
            self.rect_x2 = self.present_x - self.past_x
            self.rect_y2 = self.present_y - self.past_y    
            # print(f"x1 : {self.rect_x1}, y1 : {self.rect_y1}, x2 : {self.rect_x2}, y2 : {self.rect_y2}")
            print()
        self.painter.end()


    # 마우스 PRESS
    def mousePressEvent(self, event):
        self.past_x = event.x()
        self.past_y = event.y()

    # 마우스 MOVE
    def mouseMoveEvent(self, event):
        if self.past_x is not None:  # 마우스가 눌린 상태에서만 이동
            self.present_x = event.x()
            self.present_y = event.y()
            self.update()  # 화면 갱신을 위해 update() 호출

    # 마우스 RELEASE
    def mouseReleaseEvent(self, event):
        self.present_x = event.x()
        self.present_y = event.y()
        # self.update()  # 화면 갱신을 위해 update() 호출
        self.past_x = None
        self.past_y = None

        if self.rect_x1 is not None:
            # print("emit 실행 댔음!!")
            self.rect_signal.emit(self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)


class ThreadOfDrawing(QThread, form_class):
    def __init__(self, signal, video_file):
        super().__init__()
        self.video_file = video_file
        self.signal = signal
        # 드로잉 파트 여기서 
        # 그럼 show 한 다음에 여기서 thread를 여기서 진행.
    def run(self):
        if self.video_file:
            cap = cv2.VideoCapture(self.video_file)
            self.preview_ret, self.preview = cap.read()
            self.rgbImage = cv2.cvtColor(self.preview, cv2.COLOR_BGR2RGB)  # 프레임에 색 입히기
            self.convertToQtFormat = QImage(self.rgbImage.data,self.rgbImage.shape[1],self.rgbImage.shape[0],QImage.Format_RGB888,)
            self.pixmap = QPixmap(self.convertToQtFormat)  # 이 부분이 메인스레드에서 처리되어야하는 QPixmap이 있어서 2개 다 잡아먹고 있는거다?
            self.preview_image = self.pixmap.scaled(2121, 1201, QtCore.Qt.IgnoreAspectRatio)  # 프레임 크기 조정 1920, 1080 후보 1
            self.signal.preview_pixmap_signal.emit(self.preview_image)
            cap.release()  # OpenCV 객체 해제

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Drawing()
    myWindow.show()
    sys.exit(app.exec_())
