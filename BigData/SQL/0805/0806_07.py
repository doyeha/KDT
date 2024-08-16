import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234',db='sqlclass_db', charset = 'utf8')

curs = conn.cursor()

sql = """
    update customer
    set region = '서울특별시'
    where region = '서울'
"""

a = curs.execute(sql)

print(a)

curs.close()
conn.close()

