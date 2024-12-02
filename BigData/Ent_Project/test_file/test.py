from PyQt5 import QtWidgets, uic
import sys
form_window = uic.loadUiType("test.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.decreaseNum)

    def decreaseNum(self):
        txt = self.le.text()
        num = int(txt)
        txt2 = str(num-1)
        self.le.setText(txt2)
        print("가능?")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())