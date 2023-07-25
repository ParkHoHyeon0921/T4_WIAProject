import pickle
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

from Client.ClientSocket import ClientSocket
from ChatRoom import ChatRoom

class LoginFunction(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('../UI/Login.ui', self)
        self._default_set()

    @pyqtSlot(list)
    def recv_from_Control(self, recv_list):
        """서버에게 받은 값을 리스트형태로 받음"""
        print(recv_list, "서버에서 Login파일로 슬롯 받은 DB데이터입니다.")
        self.login_check_func(recv_list)

    def login_check_func(self, data_):
        """로그인 체크 기능 추후 로그인 체크기능으로 수정해야합니다."""
        print(data_, "로그인 체크 기능으로 받은 데이터입니다.")
        self.label_5.clear()
        if data_[0] == 'not find':
            self.label_5.setText("이메일이 일치하지 않습니다.")
            self.lineEdit.setFocus()
        else:
            if self.lineEdit_2.text() == data_[1]:
                room_num = "2" #임의로 지정
                self.chatroom = ChatRoom(data_[2], room_num, self.controller)
            else:
                self.label_4.setText("비밀번호가 일치하지 않습니다.")
                self.lineEdit_2.clear()
                self.lineEdit_2.setFocus()

    def controller_to_send(self, header, msg):
        """
        :param msg: 서버에게 보내는 메시지
        :return:
        """
        self.controller.client_Send_Func(header, msg)

    def lineEdit_Func(self):
        """라인 에딧 텍스트의 값을 엔터시 클라이언트를 통해 서버에게 값을 전달함."""
        if self.lineEdit_2.text() == '':
            self.label_4.setText("비밀번호를 입력하지 않았습니다.")
            self.lineEdit_2.setFocus()

        if self.lineEdit.text() != '':
            user_email = self.lineEdit.text()
            self.controller_to_send("Server", f"None:None:DB/Login/{user_email}")
        else:
            self.label_5.setText("이메일을 입력하지 않았습니다.")
            self.lineEdit.setFocus()



    def _default_set(self):
        """윈도우 초기 설정값"""
        self._controller_connect_Function()
        self._btn_connect()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.lineEdit.setFocus()

    def _controller_connect_Function(self):
        """컨트롤러와 이어주는 기능"""
        self.controller = ClientSocket()
        self.controller.clientsocket_Set()
        self.controller.db_signal.connect(self.recv_from_Control)

    def _btn_connect(self):
        """버튼 연결 기능"""
        self.pushButton.clicked.connect(self.lineEdit_Func)
        self.pushButton_2.clicked.connect(self.close)

        self.lineEdit.returnPressed.connect(self.lineEdit_Func)
        self.lineEdit_2.returnPressed.connect(self.lineEdit_Func)
        self.lineEdit.textChanged.connect(self.lineEdit_text_check)

    def lineEdit_text_check(self, e):
        """이메일 입력시 예외처리"""
        text_list = [':', ';', ',', '{', '}', '(', ')', '[', ']', '\\', '/', '>', '<', '-', '=', '+', '?', '!', '%', '\'', '\"']
        for i in self.lineEdit.text():
            if i in text_list:
                self.lineEdit.setText(self.lineEdit.text()[:-1])
    def closeEvent(self, e):
        """로그인 종료시 소켓 닫히게 설정."""
        self.controller_to_send("Server", f"None:None:Socket/Stop")
        self.controller.client_socket.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainapp = LoginFunction()
    mainapp.show()
    sys.exit(app.exec_())





