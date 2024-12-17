from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
import sys
# sys.path.append(r'C:\Git\KDT\BigData\Ent_Project\App6\resources') 
# from resources import *

form_class = uic.loadUiType("./ui/mini_condition_set.ui")[0]

class Mini_con(QMainWindow, form_class):
    def __init__(self, signal):
        super().__init__()
        self.setupUi(self)
        self.signal = signal


    def mini_con_send(self):
        hash_amt = self.hash_amt.text()
        text_amt = self.text_amt.text()
        try:
            hash_amt = int(hash_amt)
            text_amt = int(text_amt)
            self.signal.mini_condition_signal(text_amt, hash_amt)
        except:
            pass
        finally:
            self.close()



        
        
        
