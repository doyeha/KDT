import sys
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5 import uic

from PyQt5.QtCore import pyqtSignal

# UI 파일 로드
form_class = uic.loadUiType("drawing.ui")[0]

class Drawing(QMainWindow, form_class):
    rect_info_signal = pyqtSignal(str,int, int, int, int)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.drawing_box = PaintView(self.drawingArea)  # drawingArea는 이미 UI에서 정의되었을 것
        self.paintview = PaintView(self.drawingArea)
        self.rect_x1 = None
        self.rect_y1 = None
        self.rect_x2 = None
        self.rect_y2 = None

        self.drawed_rec_info = None

        self.paintview.rect_signal.connect(self.xy_position)
        
    def xy_position(self, x1, y1, x2, y2):
        self.rect_x1 = x1
        self.rect_y1 = y1
        self.rect_x2 = x2
        self.rect_y2 = y2
        # print(f"x1 : {self.rect_x1}, y1 : {self.rect_y1}, x2 : {self.rect_x2}, y2 : {self.rect_y2}")

    def recxy_send(self):
        if self.radioBtn_rec1.isChecked():
            # print("[rec1]", end=" ")
            self.rect_info_signal.emit("rec1",self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)

        elif self.radioBtn_rec2.isChecked():
            # print("[rec2]", end=" ")
            self.rect_info_signal.emit("rec2",self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)

        elif self.radioBtn_rec3.isChecked():
            # print("[rec3]", end=" ")
            self.rect_info_signal.emit("rec3",self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)

        else:
            pass

        # rec번호 / x1~y2까지의 좌표값을 보내야한다.
        # self.drawed_rec_info = {"rec1":[self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2]}
        # self.xy_position
        # print(f"x1 : {self.rect_x1}, y1 : {self.rect_y1}, x2 : {self.rect_x2}, y2 : {self.rect_y2}")
    
class PaintView(QLabel):
    rect_signal = pyqtSignal(int, int, int, int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)  # 마우스 이동을 추적하기 위해 필요
        self.past_x = None
        self.past_y = None
        self.present_x = None
        self.present_y = None
        self.rect_x1 = None
        self.rect_y1 = None
        self.rect_x2 = None
        self.rect_y2 = None

        self.rect_is = None

        self.img = QPixmap(r"C:\Git\KDT\BigData\Ent_Project\App5.1\back.png")  # 기본 배경 이미지를 로드
        self.setPixmap(self.img)  # QLabel에 이미지를 설정
    

    def paintEvent(self, event):
        # 마우스 이벤트에서 그릴 내용을 처리할 수 있도록 paintEvent 구현
        painter = QPainter(self)
        painter.begin(self)
        self.rect_is = False
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))

        if self.past_x is not None and self.present_x is not None:
            painter.drawRect(self.past_x, self.past_y, self.present_x - self.past_x, self.present_y - self.past_y)
            self.rect_x1 = self.past_x
            self.rect_y1 = self.past_y
            self.rect_x2 = self.present_x - self.past_x
            self.rect_y2 = self.present_y - self.past_y    
            # print("실시간 마우스 위치")
            # print(f"x1 : {self.rect_x1}, y1 : {self.rect_y1}, x2 : {self.rect_x2}, y2 : {self.rect_y2}")
            print()
            # if self.rect_y2 is not None:

      # 잘 받아오고 있으시잖아 ... 보내라구 ./....
        painter.end()


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Drawing()
    myWindow.show()
    sys.exit(app.exec_())
