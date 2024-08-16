from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request	import urlopen

driver = webdriver.Chrome()
driver.get('https://finance.naver.com/sise/sise_market_sum.naver')


html = driver.page_source

# html = urlopen('https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html, 'html.parser')
# Temp = soup.select('tbody > tr')

Top50 = driver.find_element(By.XPATH,'//*[@id="contentarea"]/div[3]/table[1]/tbody').text
# # Top10 = driver.find_element(By.CLASS_NAME,'//*[@id="contentarea"]/div[3]/table[1]/tbody/tr[14]/td[1]')
Top50 = Top50.split('\n')
print(Top50)

for i in Top50:
    
# <a href="/item/main.naver?code=005930" class="tltle">삼성전자</a>
#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td.no


