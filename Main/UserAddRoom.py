import datetime

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.uic import loadUi


class UserAddRoom(QWidget):
    def __init__(self, name, img, msg, time, parent=None):
        super().__init__(parent)
        loadUi('../UI/user_addchat.ui', self)
        self.name = name
        self.img = img
        self.msg = msg
        self.time = time
        self.add_user_widget()
    def add_user_widget(self):
        self.label.setText(self.name)
        # self.label_3.setPixmap(QPixmap(self.img))
        self.textEdit.setText(self.msg)
        self.label_2.setText(f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}')