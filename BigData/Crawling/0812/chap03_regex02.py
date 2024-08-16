from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

img_tag = re.compile('/img/gifts/img.*.jpg')
images = soup.find_all('img', {'src':img_tag})

for image in images:
    print(image, end=" -> ['src'] 속성값 ")
    print(image['src'])




html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html,'html.parser')



p


