

class ConnectDB:

    import pymysql

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.db = 'jqtest'
        self.port = 3306

    def connect_db(self):
        conn = self.pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
        return conn

    def select(self):
        # 调用私有方法：获取数据库连接
        conn = self.connect_db()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = conn.cursor()
        # 执行sql语句
        sql = 'select * from member'
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
        data1 = cursor.fetchone()
        print(data1)
        # 关闭连接·
        cursor.close()
        conn.close()
        print('关闭')

test = ConnectDB()
test.select()