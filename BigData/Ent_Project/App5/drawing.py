import sys
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5 import uic

# UI 파일 로드
form_class = uic.loadUiType("drawing.ui")[0]

class Drawing(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drawing_box = PaintView(self.drawingArea)  # drawingArea는 이미 UI에서 정의되었을 것

    def clear(self):
        pass


class PaintView(QLabel):
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
        self.img = QPixmap("back.png")  # 기본 배경 이미지를 로드
        self.setPixmap(self.img)  # QLabel에 이미지를 설정

    def paintEvent(self, event):
        # 마우스 이벤트에서 그릴 내용을 처리할 수 있도록 paintEvent 구현
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))

        if self.past_x is not None and self.present_x is not None:
            painter.drawRect(self.past_x, self.past_y, self.present_x - self.past_x, self.present_y - self.past_y)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Drawing()
    myWindow.show()
    sys.exit(app.exec_())
