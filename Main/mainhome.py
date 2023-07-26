import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5.Qt import *

from AddWidget.AddPost import AddPostABC
from Client.ClientSocket import ClientSocket
from Main.Login import LoginFunction


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('../UI/MainView.ui', self)
        self.user_info()
        self.lb_click.mousePressEvent = lambda x: self.stackedWidget_main.setCurrentIndex(1)
        for i in range(10):
            addpost = AddPostABC('0', '0', f'code help{i}', f'this is comment{i}', '박호현', ['python', 'pyqt5'])
            addpost.setParent(self.scrollAreaWidgetContents_2)
            addpost.mousePressEvent = lambda x=None, y=addpost: self.post_info(y)
            self.scrollArea_2.widget().layout().insertWidget(len(self.scrollArea_2.widget().layout())-1, addpost)
        self.controller = ClientSocket()
        self.controller.clientsocket_Set()
        self.btn_login.clicked.connect(self.login_page)


    def post_info(self, post):
        print(post.post_info)
        answer_cnt_ = int(post.label_8.text()) + 1
        post.label_8.setText(f'{answer_cnt_}')


    def login_page(self):
        self.login = LoginFunction(self.controller)
        self.login.exec()
        self.user_email = self.login.data_[0]
        self.user_pw = self.login.data_[1]
        self.user_name = self.login.data_[2]
        self.user_ip = self.login.data_[3]
        self.user_sex = self.login.data_[4]
        self.user_img = self.login.data_[5]
        self.user_state = self.login.data_[6]
        self.stackedWidget_main.setCurrentIndex(1)
        return


    def user_info(self):
        self.user_email = None
        self.user_pw = None
        self.user_name = None
        self.user_ip = None
        self.user_sex = None
        self.user_sex = None
        self.user_img = None
        self.user_state = None


        # self.login.close()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainview = MainView()
    mainview.show()
    sys.exit(app.exec_())