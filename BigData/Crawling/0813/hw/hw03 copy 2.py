from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request	import urlopen





html = urlopen('https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html, 'html.parser')
# Temp = soup.select('tbody > tr')

# Temp = soup.find_all('a', {'class' : 'title'})
# Temp = soup.select('tbody > tr')
# Temp = soup.select('a', {'class' : 'title'})
# temp = soup.find_all('tbody')
Temp = soup.select('tbody > tr > td > a', {'class' : 'tltle'})
# Temp = soup.find('a', {'class' : 'tltle'}).attrs['href']
# Temp = soup.find_all('tltle')
print(Temp)




# for i in Top50:


    #contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2) > a
#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td.no

#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2) > a
