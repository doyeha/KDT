import pymysql
import pandas as pd
import csv

conn = pymysql.connect(host='localhost', user='root', password='1234',db='sakila', charset = 'utf8')

cur = conn.cursor()
cur.execute('select *from language')

desc = cur.description
for i in range(len(desc)):
    print(desc[i][0], end = ' ')
print()

rows = cur.fetchall()
# for data in rows:
#     print(data)
# print()

datas = []
for data in rows:
    datas.append(data)

print(datas)
cur.close()
conn.close()