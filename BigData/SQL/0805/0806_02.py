import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', password='1234',db='sakila', charset = 'utf8')

cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select *from language')
rows = cur.fetchall()

print(rows)

languageDF = pd.DataFrame(rows)
print(languageDF)
print()

print(languageDF['name'])








cur.close()
conn.close()

