import pandas as pd 
import pymysql 

class Mydb:
    # 생성자 함수 
    def __init__(self, 
                 _host = "127.0.0.1", 
                 _port = 3306, 
                 _user = "root", 
                 _password = "1234", 
                 _db = "ezen"):
        self.host = _host
        self.port = _port
        self.user = _user
        self.password = _password
        self.db = _db
    # sql_query()함수 생성
    # 데이터베이스 서버와 연결
    # 커서 생성
    # sql 쿼리문을 요청 
    # 응답 메시지를 받는다. 
    # 모든 작업이 끝나면 데이터베이스와 연결을 종료
    def sql_query(self, query, *data):
        # 서버와 연결 
        _db = pymysql.connect(
            host = self.host, 
            port = self.port, 
            user = self.user, 
            password = self.password, 
            db = self.db
        )
        # 커서 생성 
        cursor = _db.cursor(pymysql.cursors.DictCursor)
        # 매개변수의 query와 data를 execute 함수를 이용하여 요청 
        cursor.execute(query, data)
        # query가 select문이라면?
        if query.upper().strip().startswith('SELECT'):
            data = cursor.fetchall()
            result = pd.DataFrame(data)
        # select문이 아니라면
        else:
            _db.commit()
            result = 'Query OK'
        # 데이터베이스 서버와 연결을 종료
        _db.close()
        return result