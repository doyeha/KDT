from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html.read(), 'html.parser')


soup = BeautifulSoup(html.text, 'html.parser')
temp = soup.select('a', {'class' : 'tltle'})
# temp = soup.select('contentarea > div > table > tbody > tr > a')
print(temp)

#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2)