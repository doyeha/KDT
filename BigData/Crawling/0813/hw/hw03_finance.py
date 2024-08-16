import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.naver'

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
# temp = soup.select('a.href', {'class' : 'tltle'})

temp = soup.find_all('a', {'class' : 'tltle'})
site_list = []

idx = 1
for t in temp:
    if idx == 11:
        break
    else:
        site_list.append(t.attrs['href'])
        idx += 1

# print(site_list)

# https://finance.naver.com + list(i) 
Top10_info = []
for site in site_list:
    temp_list = []
    url = f'https://finance.naver.com{site}'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    Ent_temp = soup.find('h2').text # 삼성전자
    temp_list.append(Ent_temp)
    code_temp = soup.find('span', {'class' : 'code'}).text   # 회사 옆 코드
    
    temp_list.append(code_temp)
    temp = soup.find('div', {'class':'rate_info'})
    temp = temp.find_all('span', {'class':'blind'})


    idx = 0
    for t in temp:
        if idx in [0,3,4,7,8]:
            # print(t)
            temp_list.append(t.text)
        idx += 1

    Top10_info.append(temp_list)
# print(Top10_info)

# 기업 10개 기업명 / 코드 / 현재가 / 전일가 / 시가 / 고가 / 저가 잘 들어갔나 확인용
# for i in Top10_info:
#     print(i)
# 잘 들어갔다!
def menu(): # 메뉴 출력
    title = '[ 네이버 코스피 상위 10대 기업 목록 ]'
    print('-'*40)
    print(title)
    print('-'*40)
    idx = 1
    for i in Top10_info:
        print('[{:>2}]'.format(idx), end=" ")
        print(i[0])
        idx+=1

def print_Ent(inp):
    inp = inp - 1
    print('https://finance.naver.com'+site_list[inp])
    print('종목명 :', Top10_info[inp][0])
    print('종목코드 :', Top10_info[inp][1])
    print('현재가 :', Top10_info[inp][2])
    print('전일가 :', Top10_info[inp][3])
    print('시가 :', Top10_info[inp][4])
    print('고가 :', Top10_info[inp][5])
    print('저가 :', Top10_info[inp][6])
    print('\n\n')

def main():  # 담에는 위에도 ... 하자
    while True:
        menu()
        inp = int(input('주가를 검색할 기업의 번호를 입력하세요( -1 입력 시 종료 ) : '))    # strip, 숫자 아닐 시 예외처리 


        if inp == -1:
            break
        else:
            print_Ent(inp)

    
main()
# 종목명 종목코드 현재가 전일가 시가 고가 저가 프리늩 .... ㅁㄴ으ㅏㅣㅡㅇㄴ루무ㅢㅏㄴ루ㅏㅣㅓㄶㄹ무ㅏㅣ율무ㅏㅣㄴㅇㄹ휴ㅓㅟㅏㅐㄹㄴㅇ퓨ㅝㅏㅣㅐㄾㅊㅍ뉴이ㅏㅓㅡㄿ니ㅏㅓㅜ

