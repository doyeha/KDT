# https://deep-eye.tistory.com/13
import sys
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDesktopWidget
# 원본에서 drawline에서 drawrect으로 변경 후 (x,y, 최종-x, 최종-y)으로 계산 완료
# 문제점 : 창 크기 변동 시 기존 사이즈와 마우스 이동 거리와 비례해서 움직이는 상대 좌표값. 일그러짐.

from PyQt5 import uic
form_class = uic.loadUiType("drawing.ui")[0]

class Drawing(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drawing_box = PaintView(self.drawingArea)
        # self.drawing_box.setup_events()

    def clear():
        pass
        

class PaintView(QLabel):    #(QMainWindow)
    # def setupUi(self):
    #     # self.move(300, 200)
    #     # self.resize(800, 600)
    #     self.setWindowTitle('Centering')
    #     self.centralwidget = QWidget(QMainWindow)
    #     self.centralwidget.setObjectName("centralwidget")
    #     self.gridLayout = QGridLayout(self.centralwidget)
    #     self.gridLayout.setObjectName("gridLayout")
        
    #     # self.screen = QLabel(self.centralwidget)
    #     self.screen = QLabel()
    #     self.screen.setPixmap(QPixmap("back.png"))
    #     self.screen.setScaledContents(True)
    #     self.screen.setObjectName("screen")
        # self.center()
        # self.gridLayout.addWidget(self.screen, 0, 0, 1, 1)
        # self.setCentralWidget(self.centralwidget)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setMouseTracking(True)  # 마우스 이동을 추적하기 위해 필요
        # self.setupUi()
        self.show()
        
        self.img = QPixmap("back.png")
        self.setPixmap((self.img))
        self.past_x = None
        self.past_y = None
        self.present_x = None
        self.present_y = None
        self.rect_x1 = None
        self.rect_y1 = None
        self.rect_x2 = None
        self.rect_y2 = None
        
    # 마우스 MOVE
    def mouseMoveEvent(self,event):
        self.draw_Rect(event.x(),event.y())
        
    # 마우스 RELEASE
    def mouseReleaseEvent(self,event):  
        self.draw_Rect(event.x(),event.y())
        self.past_x = None
        self.past_y = None

    def draw_Rect(self,x,y):
        if self.past_x is None:
            self.past_x = x
            self.past_y = y
        else:
            self.present_x = x
            self.present_y = y

            
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))

            self.rect_x1 = self.past_x
            self.rect_y1 = self.past_y
            self.rect_x2 = self.present_x - self.past_x
            self.rect_y2 = self.present_y - self.past_y

            painter.drawRect(self.past_x,self.past_y,self.present_x - self.past_x,self.present_y - self.past_y)
            painter.end
            

        print(f"좌표값\nx1:{self.rect_x1}\nx2:{self.rect_x2}\ny1:{self.rect_y1}\ny2:{self.rect_y2}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    myWindow = Drawing()
    # # ui = PaintView()
    # sys.exit(app.exec_())
    myWindow.show()
    app.exec_()