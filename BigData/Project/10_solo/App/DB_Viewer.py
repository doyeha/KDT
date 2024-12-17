import sqlite3

from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from PyQt5.QtCore import (QThread, pyqtSignal)

from collections import deque

# 여기서 DB에 들어가면 안되니까? saviwer을 saver로 바꾸고
# 저 Saver에서 정보를 받아서 띄우자.  
class DB_Viewer(QThread):
    def __init__(self, signal, showtable):
        super().__init__()
        self.signal = signal
        self.showtable = showtable
        self.data_list = []

    def run(self):
        self.signal.load_data_signal.connect(self.load_data)    # 세이버에서 신호 받아오기.


    def load_data(self, datatup):
        # self.showtable.clearContents()
        self.showtable.clear()
        self.showtable.setRowCount(0)
        # self.Cur.execute("SELECT * FROM insta")
        # self.Cur.execute("SELECT * FROM insta")
        # data = self.Cur.fetchall()
        self.data_list.append(datatup)
        # save_link 하면 하나의 튜플 형식으로 전달이 된다.
        for row_index, row_data in enumerate(self.data_list):
            self.showtable.insertRow(row_index)
            for col_index, per_data in enumerate(row_data):
                item = QTableWidgetItem(str(per_data))
                self.showtable.setItem(row_index,col_index, item)



