# 라이브 웹캠으로 실행해서 보기
import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

running = False

def run():
    global running
    cap = cv2.VideoCapture(0)   # 카메라 읽어들이기
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    label.resize(width, height)

    while running:  # 읽어서 계속 송출
        ret,img = cap.read()
        if ret:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            h,w,c=img.shape
            qImg=QtGui.QImage(img.data,w,h,w*c,QtGui.QImage.Format_RGB888)
            pixmap=QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)
        else:
            QtWidgets.QMessageBox.about(win,"Error","Cannot read frame.")
            print("cannot read frame.")
            break
    cap.release()
    print("Thread end.")

def stop():
    global running
    running = False
    print("stoped..")

def start():
    global running
    running = True
    th = threading.Thread(target=run)
    th.start()
    print("started..")

def onExit():
    print("exit")
    stop()

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
btn_start = QtWidgets.QPushButton("Camera On")
btn_stop = QtWidgets.QPushButton("Camera Off")

vbox.addWidget(label)
vbox.addWidget(btn_start)
vbox.addWidget(btn_stop)
win.setLayout(vbox)
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())