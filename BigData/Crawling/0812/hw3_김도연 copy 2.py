from urllib.request import urlopen
from bs4 import BeautifulSoup
import re






coffee_shop_list = []
i = 1
url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
temp = soup.select('div.tableType01 > table > tbody> tr ')

for i in range(1,4):
    idx = 1
    for line in temp:
        print('-'*50)
        print(f'[{idx}]')

        print(line.select_one('td.noline.center_t').text)
        print(line.select_one('a').text)
        print(line.select_one('td:nth-child(4)').text)
        print(line.select_one('td:nth-child(6)').text)

        # a = line.select_one('td.noline.center_t').text
        # temp.append(a)
        # b = line.select_one('a').text
        # temp.append(b)
        # c = line.select_one('td:nth-child(4)').text
        # temp.append(c)
        # d = line.select_one('td:nth-child(6)').text
        # temp.append(d)

        idx += 1
    # print(temp)
    # coffee_shop_list.append(temp)

# print(coffee_shop_list)




