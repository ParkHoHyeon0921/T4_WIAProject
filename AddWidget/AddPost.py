import datetime
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
from PyQt5.uic import loadUi


class AddPostABC(QWidget):
    def __init__(self, answer_cnt, view_cnt, title_, comment_, user_name, tag):
        super().__init__()
        loadUi('../UI/ADDPostABC.ui', self)
        self.title = title_
        self.user_name = user_name
        self.label_7.setText(answer_cnt)  # 답변 갯수
        self.label_8.setText(view_cnt)  #  조회수
        self.label_9.setText(title_)  # 제목
        self.label_10.setText(comment_[0])  # 내용
        self.tag = None # list for tag add widget
        self.label_11.setText(user_name)  # 유저이름
        self.post_info = {"answer":answer_cnt, "view":view_cnt, "title":title_, "comment":comment_, 'name':user_name, 'tag_list':tag}
        self.HLayout = QHBoxLayout()
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HLayout.addItem(self.spacer)
        for i in tag:
            label_ = QLabel(f'{i}', self)
            label_.setStyleSheet('background-color:#E1ECF4;'
                                 'color:#7197B9;')
            self.HLayout.insertWidget(len(self.HLayout)-1, label_)
        self.frame_5.setLayout(self.HLayout)
        self.time = '%d:%02d'%(datetime.datetime.now().hour, datetime.datetime.now().minute)
        self.label.setText(self.time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    addpost = AddPostABC()
    addpost.show()
    sys.exit(app.exec_())




