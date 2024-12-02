import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("log_search.ui")[0]

class logsearch(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = logsearch() 
    myWindow.show()
    app.exec_()