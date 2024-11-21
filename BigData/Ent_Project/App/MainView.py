from PyQt5.QtWidgets import *
from PyQt5 import uic
from setting import *
import sys

class MainView(QDialog):
    # def __init__(self) -> None:
        # self.dlg = loadUi("MainView.ui")
        # self.dlg.show()
        
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("MainView.ui")

        # self.setting_button.
        self.show()
        
app = QApplication(sys.argv)

my_win = MainView()

app.exec()