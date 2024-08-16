from urllib.request import urlopen
from bs4 import BeautifulSoup
import re






page_number = 1
# url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
# html = urlopen(url)
# soup = BeautifulSoup(html, 'html.parser')

# # for i in range(1,51):
#     url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
#     html = urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     one = soup.select(contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody)
#     print(one)

url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
# tbody = soup.select('table', {'class':'tb_store'})
#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody

tbody = soup.find_all('tbody')

# tr = tbody.find_all('a')
# idx = 1
# for i in tbody:
#     print(f'[{idx}]', i.text)
#     print('-'*50)
#     idx += 1

# for i in tbody:
#     print('\n\n\n------------------------------------------------------------------------------------')
#     print(i)

# print(tbody.find_all('td'))
coffeeshop=[]
temp = []
print(tbody)
# print(tbody.find_all('tr'))

# a = tbody.find_all('tr').text.split('\n')
# for i in a:
#     if i != '':
#         temp.append(i)
#     coffeeshop.append(temp)
# print(coffeeshop)



#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody

#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a

# print(soup.select('contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td.noline.center_t'))
# list_1 = soup.find('div', {'id' : 'tableType01'})
# print(list_1)
# print(one)
#contents > div.content > fieldset > fieldset > div.tableType01

#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td.noline.center_t