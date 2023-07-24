class DBClass:
    def __init__(self):
        super().__init__()

    def main_db_Control(self, type_):
        if type_ == 'Login':
            self.login_query_Func(None)
        elif type_ == 'PwChange':
            self.update_Func(None)
    def login_query_Func(self, email):
        pass
        return db_query

    def update_Func(self, before_data, after_data):
        pass