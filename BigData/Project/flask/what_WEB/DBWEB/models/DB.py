import pymysql

db = pymysql.connect(host="localhost:3306", user="root", password="1234", db="Flask_Proj", charset="utf8")

cursor = db.cursor()

# sql = "select * from netflix"
# cursor.execute(sql)
# cursor.fetchall()
# cursor.fetchone()
# cursor.fetchall(100)

db.commit()

db.close()