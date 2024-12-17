import sqlite3

from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import (QThread, pyqtSignal)
from PyQt5.QtWidgets import *
import sys 


# form_class = uic.loadUiType("./ui/MainView_test.ui")[0]

# class DB_test(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.con = sqlite3.connect("test.db")
#         self.Cur = self.con.cursor()
#         # self.showtable =  self.findChild(QtWidgets.QTableWidget, "insta_table")
#         self.showtable = self.insta_table
#         self.load_data()

#     def load_data(self):
#         self.showtable.clearContents()
#         self.showtable.setRowCount(0)
#         self.Cur.execute("SELECT * FROM test")
#         data = self.Cur.fetchall()
#         print("data", data)
        
#         # for row_index, row_data in enumerate(data):
#         #     self.showtable.insertRow(row_index)
#         #     for col_idx, col_data in enumerate(row_data):
#         #         self.showtable.setItem(row_index, col_idx, QtWidgets.QTableWidget(str(col_data)))
#         # for row in data:
#         #     print("i", row)
#         #     # row = list(row)
#         #     # i는 튜플. 
#         #     for i in range(len(row)):
#         #         dat = row[i]
#         #         self.showtable.setItem(i, dat, QTableWidgetItem(dat))

#         for row_index, row_data in enumerate(data):
#             self.showtable.insertRow(row_index)
#             for col_index, per_data in enumerate(row_data):
#                 item = QTableWidgetItem(str(per_data))
#                 self.showtable.setItem(row_index,col_index, item)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     main_view = DB_test()  # Main 인스턴스 생성

#     # 로그인 화면에서 로그인 버튼 누르면 실행하도록함.
#     # 그 다음에 Open_Main이 되면 show()
#     main_view.show()  # 로그인 화면 먼저 띄우기
#     app.exec_()
#     # sys.exit()








# https://eggwhite0.tistory.com/64
class Test:
    con = sqlite3.connect("insta copy.db")
    Cur = con.cursor()

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS test(
            Oner_ID TEXT,
            MAINTEXT TEXT,
            HASHTAG TEXT
            );"""
        self.Cur.execute(sql)

    def insert_data(self, data1, data2, data3):
        try:
            sql = "INSERT INTO test VALUES (?, ?, ?)"
            data = (data1, data2, data3)
            self.Cur.execute(sql, data)
        except Exception as e:
            print("에러 발생", e)
        finally:
            self.con.commit()

    def select_data(self, search_word):
        try:
            sql = "SELECT SEARCH_WORD FROM insta WHERE SEARCH_WORD = ?"
            data = (search_word,)
            # 쿼리 실행
            self.Cur.execute(sql, data)
            result = self.Cur.fetchall()
            print("결과값", result)
        except Exception as e:
            print("1차 링크 발송 fetchall에서 오류 : ", e)


    def testtest(self):
        self.Cur.execute("SELECT * FROM insta")
        data = self.Cur.fetchall()  # 데이터를 즉시 다시 확인
        print("insert_linkdata에서 링크 잘 들어갔는지 확인.", data)


    def run(self):
        print("실행")
        SQL = Test()
        SQL.create_table()
        # for i in range(1,10):
        #     SQL.insert_data(f"one_test{i}", f"two_test{i}", f"thr_test{i}")
        SQL.select_data("퇴근")
        # SQL.testtest()

if __name__ == "__main__":
    SQL = Test()
    SQL.run()
