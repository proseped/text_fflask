import pymysql

# 连接MySQL数据库
db = pymysql.connect(host="192.168.19.147", user="prose", passwd="120511", database="database_py")

# 创建游标
cursor = db.cursor()

sql = """CREATE TABLE IF NOT EXISTS students_01
        (
        id int primary key,
        name varchar(30) not null,
        age int default 10
        );
        """

cursor.execute(sql)
db.close()
