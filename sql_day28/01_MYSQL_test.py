import pymysql
# 连接数据库

db = pymysql.connect(host="192.168.19.147", user="prose", passwd="120511", database="student_db")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print(data)

db.close()