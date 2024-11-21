# main.py
from PyQt5 import QtWidgets
from Main_View import Ui_Dialog  # 변환된 UI 파일 임포트      # SettingWindow 클래스 임포트
from setting import Ui_setting

class setting_page(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_setting()      # Ui_setting의 인스턴스 생성
        self.ui.setupUi(self)       # Ui_setting의 setupUi 메서드를 호출하여 UI 초기화
        self.setWindowTitle("Settings")

class Main(QtWidgets.QMainWindow, Ui_Dialog): # Ui_MainWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setting_page = None
        self.setting_button.clicked.connect(self.go_setting)

    def go_setting(self):
        print("세팅창 열어줘")
        if self.setting_page is None:
            self.setting_page = setting_page()  # SettingWindow 인스턴스화
        self.setting_page.show()
        print("세팅창 열기")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
