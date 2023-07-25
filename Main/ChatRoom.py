from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget


class ChatRoom(QWidget):
    def __init__(self, name, room, client):
        super().__init__()
        self.user_name = name
        self.room_name = room
        self.client = client
        self.client.chat_signal.connect(self._recv_from_everyone)
        while True:
            data = input()
            self.send_to_everyone(data)
    def send_to_everyone(self, data):
        """방에 속해있는 사람들에게 말합니다."""
        header = 'Team'
        msg = '{}:{}:Chat/{}'.format(self.user_name, self.room_name, data)
        self.client.client_Send_Func(header, msg)

    @pyqtSlot(str)
    def _recv_from_everyone(self, data):
        """방에 속한 사람이 말한것을 듣습니다."""
        print(data, "{}번 방에서 말합니다.".format(self.room_name))

