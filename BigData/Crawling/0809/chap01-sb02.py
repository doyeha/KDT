from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.pythonscraping.com/pages/error.html')

except HTTPError as e:
    print(e)
<<<<<<< HEAD
except URLError as e:
    print('the Server could not be found!')
=======
# except URLError as e:
    # print('the Server could not be found!')
>>>>>>> 43d7979f5e5d243af9d17724ab11cbe06437d597
else:
    print('It worked!')

