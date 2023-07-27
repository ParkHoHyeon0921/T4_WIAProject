import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5.Qt import *

from AddWidget.AddCodePostABC import AddCodePostABC
from AddWidget.AddCommentPostABC import AddCommentPostABC
from AddWidget.AddPost import AddPostABC
from Client.ClientSocket import ClientSocket
from Main.Login import LoginFunction


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('../UI/MainView.ui', self)
        self.user_info()
        self.lb_click.mousePressEvent = lambda x: self.stackedWidget_main.setCurrentIndex(1)
        # comment 임시 설정값임
        comment = ["I was using a 2D list and ran into an issue. The changes I made to my list in the function was being applied to the list outside the function. I need to be able to edit the list inside the function, but I want to keep the original list.", """`def function(lst2):
    lst2[0][2] += 5
lst1 = [[9, 6, 4], [6, 8, 3]]
function(lst1)
print(lst1)""", "This is the output:", """`[[9, 6, 9], [6, 8, 3]]""", "I tried a few stuff and found that doing this works:", """`def function(lst3):
    lst3[0][2] += 5
    print(lst3)

lst1 = [[9, 6, 4], [6, 8, 3]]
lst2 = []
for i in lst1:
    lst2.append(i[:])
function(lst2)
print(lst1)""", """However, I'm working with a pretty big matrix and I need to use the function many times, so repeatedly looping through the matrix seems very inefficient.

I'm pretty sure there are much more elegant solutions I don't know about. I'm also curious about why this happens when other variables are local to functions.  """]
        for i in range(10):
            addpost = AddPostABC('0', '0', f'code help{i}', comment, '박호현', ['python', 'pyqt5'])
            addpost.setParent(self.scrollAreaWidgetContents_2)
            addpost.mousePressEvent = lambda x=None, y=addpost: self.post_info(y)
            self.scrollArea_2.widget().layout().insertWidget(len(self.scrollArea_2.widget().layout())-1, addpost)
        self.controller = ClientSocket()
        self.controller.clientsocket_Set()
        self.btn_login.clicked.connect(self.login_page)
        self.btn_python.clicked.connect(self.code_add)
        self.btn_comm_send.clicked.connect(self.ted_code_view)


    def post_info(self, post):
        """게시판 정보 기능"""
        answer_cnt_ = int(post.label_8.text()) + 1
        post.label_8.setText(f'{answer_cnt_}')
        self.post_open(post)

    def code_add(self):
        list_ = ['<', '\'', '>']
        self.ted_code.append(f'{list_[0]}{list_[-1]}')


    def post_open(self, post):
        """글 선택시 해당 글 페이지로 넘어감"""
        self.stackedWidget_main.setCurrentIndex(2)
        self.lb_title.setText(post.post_info['title'])
        for i in post.post_info['comment']:
            if i[0] != '`':
                addcommnt = AddCommentPostABC(i)
                self.verticalLayout_7.insertWidget(len(self.verticalLayout_7) - 1, addcommnt)
            else:
                addcode = AddCodePostABC(i[1:])
                self.verticalLayout_7.insertWidget(len(self.verticalLayout_7) - 1, addcode)

    def ted_code_view(self):
        """게시판에 불러온 글 데이터 업로드"""
        code_lsit_ = list()
        list_ = ['<', '\'', '>']
        msg_list = self.ted_code.toPlainText().split("<")
        for i in msg_list:
            if len(i.split(">")) > 1:
                list_[1] = list_[1]+i.split(">")[0]
        print(list_[1])
        print(msg_list)

        # for i in post.post_info['comment']:
        #     if i[0] != '`':
        #         addcommnt = AddCommentPostABC(i)
        #         self.verticalLayout_7.insertWidget(len(self.verticalLayout_7) - 1, addcommnt)
        #     else:
        #         addcode = AddCodePostABC(i[1:])
        #         self.verticalLayout_7.insertWidget(len(self.verticalLayout_7) - 1, addcode)
        # for i in msg_list:
        #     if i != '':
        #         code_lsit_.append(i)
        # print(code_lsit_)

        # for i in post.post_info['comment']:
        #     if i[0] != '`':
        #         addcommnt = AddCommentPostABC(i)
        #         self.verticalLayout_7.insertWidget(len(self.verticalLayout_7) - 1, addcommnt)
        #     else:
        #         addcode = AddCodePostABC(i[1:])
        #         self.verticalLayout_7.insertWidget(len(self.verticalLayout_7) - 1, addcode)


    def login_page(self):
        """로그인 페이지"""
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