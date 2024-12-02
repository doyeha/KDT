from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class My_Win:
    def __init__(self) -> None:
        self.dlg = loadUi("MainView.ui")
        self.dlg.show()
        

        setting_button = QPushButton('&setting_button', self)
        setting_button.clicked.connect(loadUi("setting.ui"))

        # self.dlg = loadUi

app = QApplication(sys.argv)

my_win = My_Win()

app.exec()