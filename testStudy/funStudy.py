
class connectDB:

    import pymysql

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.db = 'jqtest'
        self.port = 3306

    def connectDb(self):
        conn = self.pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
        self.cursor = conn.cursor()
        self.cursor.execute(self.sql)

    def colseDb(self):
        self.cursor.close()
        self.conn.close()
        print('关闭')

    def select(self):
        self.sql = 'select * from member'
        data1 = self.cursor.fetchone()
        print(data1)

test = connectDB()
test.select()
