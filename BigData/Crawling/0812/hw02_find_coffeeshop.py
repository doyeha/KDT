from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

coffee_shop_list = []

for i in range(1,51):

    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.select('div.tableType01 > table > tbody> tr')

    idx = 1 

    for line in temp:
        temp_list = []
        # print(line)
        # print('-'*50)
        # print(f'[{idx}]')

        # print(line.select_one('td.noline.center_t').text)
        # print(line.select_one('a').text)
        # print(line.select_one('td:nth-child(4)').text)
        # print(line.select_one('td:nth-child(6)').text)

        a = line.select_one('td.noline.center_t').text
        temp_list.append(a)
        b = line.select_one('a').text
        temp_list.append(b)
        c = line.select_one('td:nth-child(4)').text
        temp_list.append(c)
        d = line.select_one('td:nth-child(6)').text
        temp_list.append(d)
        idx += 1
        coffee_shop_list.append(temp_list)



import pandas as pd

coffee_DF = pd.DataFrame(coffee_shop_list, index=[i for i in range(1,496)], columns=['지역', '매장명', '주소', '전화번호'])
coffee_DF.to_excel('Hollys.xlsx')
coffee_DF.to_csv('Hollys.csv')
while True:
    city = input('검색할 매장의 지역을 입력하세요 : ')
    city = city.split(' ')
    if city == 'quit':
        break
    elif len(city) == 1:
        temp = coffee_DF[coffee_DF['주소'].str.contains(city[0])]
        print(temp)
    elif len(city) == 2:
        temp = coffee_DF[(coffee_DF['주소'].str.contains(city[0])) & (coffee_DF['주소'].str.contains(city[1])) ]
        print(temp)
    else:
        print('조건에 맞는 곳이 없거나 너무 많은 키워드를 입력하셨습니다.')


# 오토인덱스 기능
# 프레임 틀 추가 필요