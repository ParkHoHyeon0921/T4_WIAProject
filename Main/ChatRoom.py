import sys
import time

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.Qt import *

from PyQt5.uic import loadUi

from Main.OtherAddRoom import OtherAddRoom
from UserAddRoom import UserAddRoom

class ChatRoom(QWidget):
    def __init__(self, name, room, client):
        super().__init__()
        self.user_name = name
        self.room_name = room
        self.client = client
        self.client.chat_signal.connect(self._recv_from_everyone)
        loadUi('../UI/ChatRoom.ui', self)
        self.btn_clicked_controller()
        self._default_Set()
        dummy_chat = UserAddRoom('dummy', None, '', None)
        dummy_chat.setParent(self.scrollAreaWidgetContents)
        self.scrollArea.widget().layout().addWidget(dummy_chat)
    def btn_clicked_controller(self):
        """버튼 클릭 연결 컨트롤러"""
        self.pushButton.clicked.connect(self.enter_to_lineEdit)
        self.pushButton_2.clicked.connect(self.close)
        self.lineEdit.returnPressed.connect(self.enter_to_lineEdit)

    def enter_to_lineEdit(self):
        """엔터입력시 라인에딧 텍스트를 서버에게 전달합니다."""
        if self.lineEdit.text() == '':
            pass
        else:
            msg = self.lineEdit.text()
            print(msg)
            self.lineEdit.clear()
            user_add = UserAddRoom(self.user_name, None, msg, None)
            user_add.setParent(self.scrollAreaWidgetContents)
            self.scrollArea.widget().layout().insertWidget(len(self.verticalLayout_2)-1, user_add)

            self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
            self.send_to_everyone(msg)

    def send_to_everyone(self, data):
        """방에 속해있는 사람들에게 말합니다."""
        header = 'Team'
        msg = '{}:{}:Chat/{}'.format(self.user_name, self.room_name, data)
        self.client.client_Send_Func(header, msg)

    def _default_Set(self):
        """기본 설정"""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.label.setText(f"{self.room_name}번방")
        self.lineEdit.setFocus()


    @pyqtSlot(str)
    def _recv_from_everyone(self, data):
        """방에 속한 사람이 말한것을 듣습니다."""
        print(data, "{}번 방에서 말합니다.".format(self.room_name))
        data_list = data.split(':')
        who_name = data_list[1]
        msg_type = data_list[3]
        msg = msg_type.split('/')[1]
        print(msg)
        if self.user_name != who_name:
            chat_add = OtherAddRoom(who_name, None, msg, None)
            chat_add.setParent(self.scrollAreaWidgetContents)
            self.scrollArea.widget().layout().insertWidget(len(self.verticalLayout_2) - 1, chat_add)
            self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chatroom = ChatRoom('박호현', '2', '내')
    chatroom.show()
    sys.exit(app.exec())