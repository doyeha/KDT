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
    # print(temp)

for i in coffee_shop_list:
    print(i)

print(len(coffee_shop_list))
# print(coffee_shop_list)




