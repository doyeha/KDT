import pymysql
import pandas as pd
from matplotlib import pyplot as plt
import koreanize_matplotlib
import csv

conn = pymysql.connect(host='172.20.139.58', user='member1', password='1234',db='sqlteam4_db', charset = 'utf8')

cur = conn.cursor()
dcur = conn.cursor(pymysql.cursors.DictCursor)

query = """ 
select adult
from public_transport
where city = '전체';
"""

cur.execute(query)
rows = cur.fetchall()
datas = []
for data in rows:
    # print(data[0], type(data[0]))
    data = int(data[0].replace(',',''))
    datas.append(data)
cur.execute('select years from public_transport where city = "전체"')

qr = cur.fetchall()
year = []
for y in qr:
    year.append(y[0])
# print(year)
# print(len(datas), len(year))

######################## 년간 대중교통 전체 이용자 수 변동 그래프 ####################################
plt.plot(year, datas, marker = 'H', linewidth = '2.5')
plt.xlabel('년도')
plt.ylabel('이용자 (단위 : 백만)')
plt.title('대중교통 이용자 년간 변화')
plt.grid(alpha=0.5, linestyle='--')
plt.legend()
plt.show()



################################### 6개 권역 비율 바 차트 ###################################
query_list = []
total_list = []
### '서울', '부산', '대구', '대전', '인천', '광주' 전체비율에서 
for i in range(2015, 2024):
    cur.execute(f"select sum(replace(adult,',','')) from public_transport where city in ('서울', '부산', '대구', '대전', '인천', '광주') and years = {i};")
    list_1 = cur.fetchall()
    list_1 = list_1[0]
    list_1 = int(str(list_1).replace(',','')[1:-3])
    query_list.append(list_1)

    cur.execute(f"select adult from public_transport where city = '전체' and years = {i};")
    list_2 = cur.fetchall()
    list_2 = list_2[0]
    list_2 = int(str(list_2).replace(',','')[2:-2])
    total_list.append(list_2)
    # print(list_2, type(list_2))

# print(query_list)
# print(total_list)
year_list = [i for i in range(2015, 2024)]
# print(year_list)
per_list =[]
idx = 0
for i in range(len(query_list)):
    temp = round(((query_list[idx] / total_list[idx])*100),1)
    temp = str(temp) + '%' 
    per_list.append(temp)
    idx += 1

plt.figure(figsize=(10,5))
plt.xticks(year_list)
plt.grid(alpha=0.5, linestyle='--')

# for rect in bar2:
#     height = rect.get_height()
#     plt.text(rect.get_x()+rect.get_width()/2.0,height,  height, ha = 'center',va='bottom',size=12)
# plt.text(total_list, height + 0.2, )
bar2 = plt.bar(year_list, total_list, color=  'dodgerblue')    # 뒤쪽 / 전체 이용자수 
bar = plt.bar(year_list, query_list, color = 'tomato') # 앞쪽 / 6개 권역 이용자 수

idx= 0
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.0, height+100000,
             per_list[idx], ha = 'center',va='bottom',size=12)
    idx+=1
            #  height, ha = 'center',va='bottom',size=12)
plt.xlabel('년도')
plt.ylabel('이용자 수 (단위 : 천만)')
plt.legend()
plt.title('년간 6대 권역의 대중교통 이용자 분포')
plt.show()

# 색상 파레트 : '#ffc000','#ff9999', '#8fd9b6', '#d395d0','bisque','lightsteelblue', '#F7B7A3'
    # print(list_1)

################################### 서울까지 보자. ###################################
seoul = []
for i in range(2015,2024):
    cur.execute(f"select adult from public_transport where city = '서울' and years = {i};")
    seoul_1 = cur.fetchall()
    seoul_1 = int(str(seoul_1[0])[2:-3].replace(',',''))
    seoul.append(seoul_1)

seoul_per = []
idx = 0
for i in range(len(seoul)):
    temp = round(((seoul[idx] / total_list[idx])*100),1)
    temp = str(temp) + '%' 
    seoul_per.append(temp)
    idx += 1

plt.figure(figsize=(10,5))
plt.xticks(year_list)
plt.grid(alpha=0.5, linestyle='--')

bar1 = plt.bar(year_list, total_list, color =  'dodgerblue')    # 뒤쪽 / 전체 이용자수 
bar2 = plt.bar(year_list, query_list, color = 'tomato') # 앞쪽 / 6개 권역 이용자 수
bar3 = plt.bar(year_list, seoul, color = 'firebrick') # 앞앞쪽 / 서울 권역 이용자 수
idx= 0
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.0, height+100000,
             per_list[idx], ha = 'center',va='bottom',size=12)
    idx+=1


idx = 0
for rect in bar3:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.0, height+100000,
             seoul_per[idx], ha = 'center',va='bottom',size=10)
    idx+=1
            #  height, ha = 'center',va='bottom',size=12)

plt.xlabel('년도')
plt.ylabel('이용자 수 (단위 : 천만)')
plt.legend()
plt.title('(전체 / 6대 권역 / 서울)의 대중교통 이용자 분포')
plt.show()

################################### 6대 권역.. 분포 비율 .. 까지 보자. ###################################
city = ['서울', '부산', '대구', '대전', '인천', '광주']
# [38.99, 8.76, 3.82, 2.25, 6.76, 1.8]
per_list = []
idx = 0
for i in city:
    cur.execute(f"select adult from public_transport where city = '{i}' and years = 2023;")
    city_temp = cur.fetchall()
    city_temp = int(str(city_temp[0])[2:-3].replace(',',''))
    idx += 1
    per_list.append(city_temp)
print(per_list)

# per_list = [3147422, 707216, 308775, 181790, 545542, 145458] # 2023년 각 지역 총 이용자 수
# 각 지역별 % 구하기
total_city = []
for i in range(len(per_list)):
    city_total_temp =  per_list[i] / int(total_list[-1])
    city_total_temp = round((city_total_temp*100),2)
#     print(total_list[-1])
    # print(city_total_temp)

    total_city.append(city_total_temp)
print(total_city)


################################### 월 대중교통 비용 분포 ###################################
monthly_fare = """
select `under 2`, `2~4`, `4 ~ 6`, `6 ~ 8`, `8 ~ 10`, `10 ~ 12`, `over 12`
from monthly_fare
where city = '전체';
"""
cur.execute(monthly_fare)
qr2 = cur.fetchall()
fare = []
qr2 = str(list(qr2))
qr2 = qr2[2:-2]
qr2 = qr2.split(',')


print(qr2, type(qr2))
# col = [`under 2`, `2~4`, `4 ~ 6`, `6 ~ 8`, `8 ~ 10`, `10 ~ 12`, `over 12`]
col = ['2만원 이하', '2 ~ 4만원', '4 ~ 6만원', '6 ~ 8만원', '8 ~ 10만원', '10 ~ 12만원', '12만원 이상']
for i in qr2:
    i = i.replace(' ','')
    i = float(i)
    fare.append(i)
print(fare)
#  explode=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
### 대중교통 월별 소모금 비율 분석
plt.pie(fare, labels=col, autopct='%.1f%%', counterclock=False, wedgeprops = {'width' : 0.75}, explode=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
        startangle=90, shadow=True, colors = [ '#ffc000','#ff9999', '#8fd9b6', '#d395d0','bisque','lightsteelblue', '#F7B7A3'])
plt.title('2022년 기준, 월 평균 대중교통 비용 분포')
plt.show()


cur.close()
conn.close()

# 주제선정 이유
# 
# 이용률 
# 물가지수 (?)
# 요금 상승 기사 첨부



"""
desc = cur.description
for i in range(len(desc)):
    print(desc[i][0], end = ' ')
print()

sql = 
    update customer
    set region = '서울특별시'
    where region = '서울'
    

curs.execute(sql)
print('UPDATE 완료')

sql = 'delete from customer where name = %s'
curs.execute(sql,'홍길동')
print('delete 홍길동')
"""