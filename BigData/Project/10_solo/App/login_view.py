from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
import sys
import threading

import time 
# py 파일 import
from signal_col import signal_collection

# 크롤링 - 셀레니움 관련 import 
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_th import crawling_sele

# 작성된 ui 깡통 끌어오기 
form_class = uic.loadUiType("./ui/LoginView.ui")[0]

# 로그인화면 (첫 화면 로그인 버튼 클릭 시 메인뷰로 넘어감.)
class login_view(QMainWindow, form_class):
    def __init__(self, signal):
        super().__init__()
        self.setupUi(self)
        self.signal = signal
        self.crawling = crawling_sele(self.signal)
        self.ID = None
        self.PW = None
        self.setGeometry(1600, 400, 0, 0)
        self.crawling.start()
        self.signal.open_driver_Mainview_signal.emit(True)
        self.signal.login_success_signal.connect(self.login_success)
        self.PW_input.setEchoMode(QLineEdit.Password)

        

    def Login_info(self):
        self.ID = self.ID_input.text()
        self.PW = self.PW_input.text()
        print(f"입력된 ID : {self.ID}, PW : {self.PW}")

    def open_selenium(self):
        pass
        
    # 로그인 버튼 클릭 시 login_view 닫고 MainView Show()로 넘어가기.
    def Login_commit(self):
        self.Login_info()
        if (self.ID != None) and (self.PW != None):
            print("아이디 비밀번호 전달")
            self.signal.idpw_signal.emit(self.ID, self.PW, True)
    
        
    def login_success(self, con):
        if con:
            time.sleep(2)   # 로그인 할 시간.
            self.signal.go_Mainview_signal.emit(True)
            self.close()
            
        else:
            pass


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     # app.setAttribute(Qt.AA_EnableHighDpiScaling, False)
#     myWindow = login_view()
#     # loginWindow = login_view()
#     myWindow.show()
#     # loginWindow.show()
#     app.exec_()

# ID_input
# PW_input
# login_button

