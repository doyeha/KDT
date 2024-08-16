from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

name_list = soup.find_all('span' , {'class' : 'green'})

for i in name_list:
    print(i.text)