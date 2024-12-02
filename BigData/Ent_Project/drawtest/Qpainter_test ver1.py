
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui, QtCore


# 오류 있음. 실행 불가능 ver 1

class Screen(QMainWindow):
    def setupUi(self):
        self.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.screen = QLabel(self.centralwidget)
        self.screen.setPixmap(QPixmap("back.png"))
        self.screen.setScaledContents(True)
        self.screen.setObjectName("screen")
        
        self.gridLayout.addWidget(self.screen, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
    
    def __init__(self):
        super().__init__() 
        self.setupUi()
        # self.img = QPixmap("back.png")  # 나중에 이걸 영상 첫 프레임으로 설정
        # 
        self.show()

        self.img = QPixmap("back.png")  # 나중에 이걸 영상 첫 프레임으로 설정
        self.painter = QtGui.QPainter(self.img)

        self.past_x = None
        self.past_y = None
        self.start_x = None
        self.start_y = None
        self.present_x = None
        self.present_y = None
        


    # def mouseClickEvent(self, event):
    def mousePressEvent(self,event):
        # self.painter.begin
        self.start_x = event.x()
        self.start_y = event.y()

    # 마우스 MOVE
    def mouseMoveEvent(self, event):
        self.present_x = event.x()
        self.present_y = event.y()

    # 마우스 RELEASE
    def mouseReleaseEvent(self,event): 
        self.present_x = event.x()
        self.present_y = event.y()
        self.draw_rectangle(event.x(),event.y())
        self.start_x = None
        self.start_y = None



    def draw_rectangle(self, x, y):
        # if self.past_x is None:
        #     self.start_x = x
        #     self.start_y = y
        # else:
            self.painter.begin()
            self.present_x = x
            self.present_y = y
            self.painter= QtGui.QPainter(self.img)
            self.painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
            self.painter.drawRect(self.start_x,self.start_y, self.present_x - self.start_x,self.present_y - self.start_y)
            self.painter.end()
            self.screen.setPixmap(QtGui.QPixmap(self.img))

    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Screen()
    sys.exit(app.exec_())


        # def draw_Line(self,x,y):
    #     if self.past_x is None:
    #         self.past_x = x
    #         self.past_y = y
    #     else:
    #         self.present_x = x
    #         self.present_y = y

    #         self.img = QPixmap("back.png")
    #         painter = QtGui.QPainter(self.img)
    #         painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
    #         painter.drawLine(self.past_x,self.past_y,self.present_x,self.present_y)
    #         painter.end
    #         self.screen.setPixmap(QtGui.QPixmap(self.img))