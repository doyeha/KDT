from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.pythonscraping.com/pages/error.html')

except HTTPError as e:
    print(e)
except URLError as e:
    print('the Server could not be found!')
else:
    print('It worked!')

