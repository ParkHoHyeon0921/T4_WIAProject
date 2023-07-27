# import sys
#
# from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel
# from PyQt5.uic import loadUi
#
#
# class AddCodePostABC(QWidget):
#     def __init__(self, msg):
#         super().__init__()
#         loadUi('../UI/add_Code_Post.ui', self)
#
#         formatting_red = 'def'
#         formatting_blue = 'print'
#         for i in msg.split(" "):
#             print(i)
#             if i in formatting_red:
#                 msg = msg.replace(i, f'<font color=#ff0000>{i}</font>')
#             elif formatting_blue in i:
#                 msg = msg.replace(i, f'<font color=blue>{i}</font>')
#         self.label.setText(f"{msg}")

import re, sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QSizePolicy
from PyQt5.uic import loadUi


class PythonSyntaxHighlighter(QSyntaxHighlighter):
    """텍스트 안의 값을 변경해줌"""
    def __init__(self, document):
        super().__init__(document)
        self.highlighting_rules = []

        # 파이썬 키워드 설정
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(255, 0, 0))
        keyword_format_2 = QTextCharFormat()
        keyword_format_2.setForeground(QColor(0, 200, 1))
        python_keywords = ["def", "if", "else", "while", "for", "in", "return", 'class']
        python_keywords_2 = ['print', 'super']
        java_keywords = ["class", "public", "public", "static", "void"]
        for keyword in python_keywords:
            self.highlighting_rules.append((QRegExp(r"\b" + keyword + r"\b"), keyword_format))
        for keyword in python_keywords_2:
            self.highlighting_rules.append((QRegExp(r"\b" + keyword + r"\b"), keyword_format_2))
        for keyword in java_keywords:
            self.highlighting_rules.append((QRegExp(r"\b" + keyword + r"\b"), keyword_format))

    def highlightBlock(self, text):
        for pattern, char_format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, char_format)
                index = expression.indexIn(text, index + length)


class CodeEditor(QTextEdit):
    """값이 담길 텍스트 에딧"""
    def __init__(self):
        super().__init__()
        self.highlighter = PythonSyntaxHighlighter(self.document())
        self.setReadOnly(True)
        self.setStyleSheet('background-color:#e8ddb3; border-color:black;')
        self.setFrameShape(0)
        # self.setVerticalScrollBarPolicy(1)
        # self.setHorizontalScrollBarPolicy(1)
        # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)


class AddCodePostABC(QWidget):
    """추가되는 블록중 코드 담당 클래스"""
    def __init__(self, msg: str):
        super().__init__()
        loadUi('../UI/add_Code_Post.ui', self)
        self.code_editor = CodeEditor()
        self.code_editor.setText(msg)
        text_size = msg.count('\n')+1
        self.verticalLayout.insertWidget(len(self.verticalLayout)-1, self.code_editor)
        self.setFixedHeight(text_size*15)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    msg = 'def function(lst2):\n    lst2[0][2] += 5\n\nlst1 = [[9, 6, 4], [6, 8, 3]]\nfunction(lst1)\nprint(lst1)'
    mainapp = AddCodePostABC(msg)
    mainapp.show()
    sys.exit(app.exec_())