import pymysql

# 链接数据库
db = pymysql.connect(host = '139.159.218.173',port = 3306,db = 'gree-dm-application',user = 'root',passwd = 'my-secret-ab',charset = 'utf8')
# 创建游标
cursor = db.cursor()
# 查询语句
cursor.execute('select * from sys_log')
# 执行sql
data = cursor.fetchone()
# 打印出来
print(data)
# 关闭数据库
db.close()