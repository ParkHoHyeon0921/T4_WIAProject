from PyQt5.QtCore import pyqtSlot

from ClientSocket import ClientSocket

class LoginFunction:
    def __init__(self):
        self.clientconnect_Function()

    def controller_connect_Function(self):
        """컨트롤러와 이어주는 기능"""
        self.Controller = ClientSocket("127.0.0.1", 7001)
        self.Controller.db_signal.connect(self._recv_from_server)

    def controller_to_send(self, header, msg):
        """
        :param msg: 서버에게 보내는 메시지
        :return:
        """
        self.Controller.send_to_server(header, msg)

    @pyqtSlot(str)
    def _recv_from_server(self, recv_):
        """
        :param recv_: 서버에게 받은 값을 리스트형태로 받음
        """




