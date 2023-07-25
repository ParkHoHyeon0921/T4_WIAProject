class AddPost:
    def __init__(self, title, detail, comment, img):
        super().__init__()
        self.title = title
        self.detail = detail
        self.comment = comment
        self.img = img
        self.insert_detail(self.title, self.detail, self.comment, self.img)

    def insert_detail(self, title, detail, comment, img):
        print("제목은 {}입니다.".format(title))
        code = detail.split(" ")
        print("작성자 코멘트는 {}입니다.".format(comment))
        print("작성자가 올린 이미지는 {}입니다.".format(img))

    def func_list(self, code_):
        """코드 리스트"""
        code_list = ['if', 'for', 'def', 'class']
        for i in code_:
            if i == code_[0]:
                if i in code_list:
                    i.setStyleSheet('color:rgb(255,0,0);')


addwidget = AddPost("이거 코드좀..", "if a == b:", "여기 안 되는것같아요", "img")
print(1)