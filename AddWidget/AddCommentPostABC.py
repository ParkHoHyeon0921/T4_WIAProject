import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

class AddCommentPostABC(QWidget):
    """추가되는 블럭중 코멘트 담당 클래스"""
    def __init__(self, msg):
        super().__init__()
        loadUi('../UI/add_Comment_Post.ui', self)
        self.label.setText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainapp = AddCommentPostABC("그냥 내용입니다.")
    mainapp.show()
    app.exec_()