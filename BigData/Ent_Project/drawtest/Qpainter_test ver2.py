from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt

# 상자 여러개 그려지는 ver

class Screen(QMainWindow):
    def setupUi(self):
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
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
        self.img = QPixmap("back.png")  # 초기 이미지 로드
        self.start_x = None
        self.start_y = None

    def mousePressEvent(self, event):
        # 마우스 클릭 시 좌표 저장
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseReleaseEvent(self, event): 
        # 마우스 놓을 때 현재 좌표와 함께 사각형 그리기
        end_x = event.x()
        end_y = event.y()
        self.draw_rectangle(self.start_x, self.start_y, end_x, end_y)

    def draw_rectangle(self, x1, y1, x2, y2):
        # QPainter로 사각형 그리기
        painter = QPainter(self.img)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.drawRect(x1, y1, x2 - x1, y2 - y1)
        painter.end()

        # QLabel에 업데이트된 이미지 표시
        self.screen.setPixmap(self.img)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Screen()
    MainWindow.show()
    sys.exit(app.exec_())
