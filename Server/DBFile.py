import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

class DBFile:
    def __init__(self):
        self.pgdb = pg.connect(
            host='10.10.20.104',
            dbname='data',
            user='postgres',
            password='1234',
            port=5432
        )

        self.engine = create_engine('postgresql://postgres:1234@10.10.20.104:5432/data')
        self.cursor = self.pgdb.cursor()


    def join_user(self, email):
        """
        :data_list = 현재 가입된 유저 정보 확인(로그인 및 회원가입시 중복체크)
        """
        df = pd.read_sql(f"SELECT *  FROM USERS WHERE USER_EMAIL = '{email}'", self.engine)
        # df = pd.read_sql(f"SELECT *  FROM USERS", self.engine)
        print(df.head())
        return df.values


    # def insert_data_Function(self, id, pw_, name):
    #     cursor = self.pgdb.cursor()
    #     cursor.execute(f"INSERT INTO USERS (USER_EMAIL, USER_PW, USER_NM) VALUES ('{id}', '{pw_}', '{name}')")
    # #     # self.pgdb.commit()

if __name__ == '__main__':
    DB_file = DBFile()
    print(DB_file.join_user('ghgusghgus2085@gmail.com'))
    # DB_file.insert_data_Function('HI', '1234', "박호현")