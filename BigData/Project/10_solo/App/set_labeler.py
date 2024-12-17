from PyQt5.QtCore import pyqtSignal,QThread
from PyQt5.QtWidgets import *


class labeler(QThread):
    def __init__(self, signal, system_message):
        super().__init__()
        self.system_message = system_message
        self.signal = signal

    def run(self):
        self.signal.system_message_signal.connect(self.set_text)
        pass

    def set_text(self,text):
        self.system_message.setText(text)


