from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
import sys
# sys.path.append(r'C:\Git\KDT\BigData\Ent_Project\App6\resources') 
# from resources import *

form_class = uic.loadUiType("./ui/MainView.ui")[0]

from login_view import login_view    # 로그인 탭 import 
from signal_col import signal_collection
from DB_saver import DB_Saver
from DB_Viewer import DB_Viewer
from set_labeler import labeler
from minicon import Mini_con


class Main(QMainWindow, form_class):
    def __init__(self, signal):
        super().__init__()
        self.setupUi(self)
        self.signal = signal
        self.saver = DB_Saver(signal, self.insta_table)
        self.viewer = DB_Viewer(signal, self.insta_table)
        self.labeler = labeler(signal, self.system_message)
        self.mini_con = Mini_con(signal)

        # self.login_view = login_view(self.signal)
        # self.signal.go_Mainview_signal.connect(self.open_Main)
    
    def open_Main(self, check):
        # print("신호 받음")
        if check:
            self.saver.start()
            self.viewer.start()
            self.labeler.start()
            self.show()
    
    def open_minicon(self):
        self.mini_con.show()

    # 검색 버튼 클릭
    def start_search(self):
        # 태그 or 사용자 id 검색    / combobox
        search = self.search_type.currentText()
        searh_word = self.searh_word.text()
        # 긁어올 내용   checkBox
        Oner_ID = self.Oner_ID.isChecked()
        MainText = self.MainText.isChecked()
        lover = self.lover.isChecked()
        Hash = self.Hash.isChecked()
        # 수집할 양 - EditLabel
        want_amount = self.want_amount.text()
        if want_amount is None:
            mess_text = "데이터 수집 양을 설정해주세요."
            self.MessageBox(mess_text)
        elif want_amount is not None:
            try:
                want_amount = int(want_amount)
                self.signal.start_crawling_signal.emit(search,searh_word, Oner_ID, MainText, lover, Hash, want_amount)
            except:
                mess_text = "데이터 수집 양 탭에는 숫자만 입력해주세요."
        else:
            pass
            
    def MessageBox(self, mess_text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("입력 오류")
        msg.setInformativeText(mess_text)
        msg.setWindowTitle("오류")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def closeEvent(self, event):
        quit_msg = "프로그램을 종료하시겠습니까?"
        reply = QMessageBox.question(self, 'Exit', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signal.closecon_signal.emit(True)
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    signal = signal_collection()  # signal 객체 생성
    main_view = Main(signal)  # Main 인스턴스 생성
    
    # 여기서 실행하되, 로그인을 먼저 띄워야함.
    login_view = login_view(signal)  # LoginView 생성, signal 주기
    signal.go_Mainview_signal.connect(main_view.open_Main)  # 시그널 연결해두고, 받을 준비 완료.
    # 로그인 화면에서 로그인 버튼 누르면 실행하도록함.
    # 그 다음에 Open_Main이 되면 show()
    login_view.show()  # 로그인 화면 먼저 띄우기
    sys.exit(app.exec_())