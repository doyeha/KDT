import pymysql

db = pymysql.connect(host="172.20.60.119", user="member4", password="1234", db="webdb", charset="utf8")

cursor = db.cursor()

sql = "select * from netflix"

cursor.execute(sql)

cursor.fetchall()
cursor.fetchone()
# cursor.fetchall(100)

db.commit()

db.close()