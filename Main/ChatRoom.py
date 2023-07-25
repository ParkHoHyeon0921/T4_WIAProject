import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.Qt import *

from PyQt5.uic import loadUi
from UserAddRoom import UserAddRoom

class ChatRoom(QWidget):
    def __init__(self, name, room, client):
        super().__init__()
        self.user_name = name
        self.room_name = room
        self.client = client
        # self.client.chat_signal.connect(self._recv_from_everyone)
        loadUi('../UI/ChatRoom.ui', self)
        self.btn_clicked_controller()
        self._default_Set()
    def btn_clicked_controller(self):
        self.pushButton.clicked.connect(self.enter_to_lineEdit)
        self.pushButton_2.clicked.connect(self.close)
        self.lineEdit.returnPressed.connect(self.enter_to_lineEdit)

    def enter_to_lineEdit(self):
        if self.lineEdit.text() == '':
            pass
        else:
            msg = self.lineEdit.text()
            print(msg)
            self.lineEdit.clear()
            user_add = UserAddRoom(self.user_name, None, msg, None)
            user_add.setParent(self.scrollAreaWidgetContents)
            self.scrollArea.widget().layout().insertWidget(len(self.verticalLayout_2)-1, user_add)
            list_ = self.scrollArea.findChildren(QWidget)
            list_widget = list()
            for i in list_:
                if i.objectName() == 'widget':
                    list_widget.append(i)
            self.scrollArea.ensureWidgetVisible(list_widget[-1])
            # self.send_to_everyone(msg)

    def send_to_everyone(self, data):
        """방에 속해있는 사람들에게 말합니다."""
        header = 'Team'
        msg = '{}:{}:Chat/{}'.format(self.user_name, self.room_name, data)
        self.client.client_Send_Func(header, msg)

    def _default_Set(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.label.setText(f"{self.room_name}번방")
        self.lineEdit.setFocus()


    # @pyqtSlot(str)
    # def _recv_from_everyone(self, data):
    #     """방에 속한 사람이 말한것을 듣습니다."""
    #     print(data, "{}번 방에서 말합니다.".format(self.room_name))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chatroom = ChatRoom('박호현', '2', '내')
    chatroom.show()
    sys.exit(app.exec())