from socket import *

import threading
import pickle

from PyQt5.QtCore import QObject, pyqtSignal


class ClientSocket(QObject):
    db_signal = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.buffer = 50000
        self.decode_lange = 'utf-8'
        self.run()

    def clientsocket_Set(self, ip_, port_):
        """클라이언트 소켓 연결"""
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((ip_, port_))

    def client_Send_Func(self, header, msg):
        """
        :param header: 데이터의 타입을 설정
        :param msg: 서버에게 보낼 내용
        :return:
        """
        data = f'{header}:{msg}'
        self.connectsocket.send(f"{f'{data}':{self.buffer}}".encode('utf-8'))  # msg + buffer형태로 서버에 send.

    def _recv_from_server(self):
        """서버에게 받은 recv값"""
        while True:
            msg = self.connectsocket.recv(1024)
            self.db_signal.emit(msg)

    def thread_Func(self):
        """recv 기능 활성화를 위해 쓰레드 설정"""
        recv_thread = threading.Thread(target=self._recv_from_server)
        recv_thread.start()

    def run(self):
        """recv 쓰레드 스타트"""
        self.thread_Function()


