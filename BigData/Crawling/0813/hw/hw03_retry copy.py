import requests
from bs4 import BeautifulSoup

site_list = ['/item/main.naver?code=005930', '/item/main.naver?code=000660', '/item/main.naver?code=373220', '/item/main.naver?code=207940', '/item/main.naver?code=005380', '/item/main.naver?code=005935', '/item/main.naver?code=068270', '/item/main.naver?code=000270', '/item/main.naver?code=105560', '/item/main.naver?code=055550']
url = f'https://finance.naver.com{site_list[0]}'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

temp = soup.find('h2').text # 삼성전자
temp = soup.find('span', {'class' : 'code'}).text   # 회사 옆 코드
# temp = soup.find('p', {'class' : 'no_today'}).find('span', {'class' : 'blind'}).text   # 76100 현재가
# temp = soup.find('td', {'class' : 'first'}).find('span', {'class':'blind'}).text    # 75500 전일가
# temp = soup.find('div', {'class':'rate_info'}).find('tr').find('em', {'class':'no_up'}).find('span').text    # 76600 고가

temp = soup.find('div', {'class':'rate_info'})
temp = temp.find_all('span', {'class':'blind'})
# #chart_area > div.rate_info > table > tbody

# temp = soup.find('div', {'class':'rate_info'}).find('tr')   # 전체 확인용
# print(temp)    

print(temp)
# 0 3 4 7 8
# idx = 0
# for t in temp:
#     if idx in [0,3,4,7,8]:
#         print('t')
#         print(t.text)
#     idx += 1



# idx = 1
# for t in temp:
#     if idx == 11:
#         break
#     else:
#         site_list.append(t.attrs['href'])
#         idx += 1

#chart_area > div.rate_info

# 종목명 종목코드 현재가 전일가 시가 고가 저가 프리늩 .... ㅁㄴ으ㅏㅣㅡㅇㄴ루무ㅢㅏㄴ루ㅏㅣㅓㄶㄹ무ㅏㅣ율무ㅏㅣㄴㅇㄹ휴ㅓㅟㅏㅐㄹㄴㅇ퓨ㅝㅏㅣㅐㄾㅊㅍ뉴이ㅏㅓㅡㄿ니ㅏㅓㅜ