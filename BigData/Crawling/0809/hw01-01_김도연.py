from urllib.request import urlopen
from bs4 import BeautifulSoup


# html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')



def parse_use_find(html):
    print('[find 함수 사용]')
    findall_weather_list = html.find_all(class_ = 'tombstone-container')   
    print(f'총 tombstone-container 검색 개수 : {len(findall_weather_list)}개') 
    idx = 1
    for i in findall_weather_list:
        print(f'[{idx}]')
        # temp = i.find(class_="period-name").text

        temp = i.find('p',class_="period-name").text
        print(f'[Period] : {temp}')

        temp = i.find('p', class_="short-desc").text
        print(f'[Short	desc]: {temp}')
        try:
            temp = i.find('p',class_="temp temp-low").text
            print(f'[Temperature] : {temp}')
        except:
            None
        try:
            temp = i.find('p',class_="temp temp-high").text
            print(f'[Temperature] : {temp}')
        except:
            None
        
        temp = (i.find('img')['title'])
        print(f'[title]{temp}')
        print('-'*60)
        idx += 1

def parse_use_select(html):
    print('[select함수 사용]')
    # #seven-day-forecast
    select_weather_list = html.select('ul#seven-day-forecast-list > li > div')   # .'tombstone-container'
    # temp = select_weather_list.select('ul > li')

    # print(temp)
    print(f'총 tombstone-container 검색 개수 : {len(select_weather_list)}개')
    # print(select_weather_list)
    # print('[]')
    idx = 1
    for i in select_weather_list:
        print(f'[{idx}]')
        # print(i)
        temp = i.select_one('p.period-name').text
        print(f'[Period] : {temp}')

        temp = i.select_one('p.short-desc').text
        print(f'[Short	desc]: {temp}')
        
        try:
            temp = i.select_one('p.temp.temp-low').text
            print(f'[Temperature] : {temp}')
        except:
            None
        try:
            temp = i.select_one('p.temp.temp-high').string
            print(f'[Temperature] : {temp}')
        except:
            None
        temp = i.select_one('img')['title']
        print(f'[title] {temp}')  
        print('-'*60)
        idx += 1
# • def	scraping_use_find(html)
# – find(),	find_all() 함수를 이용하여 스크레이핑
# • def	scraping_use_select(html)
# – select(),	select_one()	함수를 이용하여 스크레이핑


def main():
    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    html = BeautifulSoup(page.read(), features='html.parser')

    print('National Weather Service Scraping')
    print('-------------------------------------')

    parse_use_find(html)
    parse_use_select(html)

main()


"""
one = soup.find(class_ = 'tombstone-container')
# print(one)

<div class="tombstone-container">
    # <p class="period-name">Overnight</p>
    <p><img alt="Overnight: Patchy fog after 5am. 
        Otherwise, mostly cloudy, with a low around 55. West southwest wind around 7 mph."
        class="forecast-icon" src="newimages/medium/nfg.png" 
        
        title="Overnight: Patchy fog after 5am.  Otherwise, mostly cloudy, with a low around 55. 
        West southwest wind around 7 mph. "/>
    </p>
    
    # <p class="temp temp-low">Low: 55 °F</p>
    # <p class="short-desc">Patchy Fog</p>
</div>

# print(one.find(class_="period-name"))

weather_list = soup.find_all(class_ = 'tombstone-container')
# print(weather_list)
idx = 1
for i in weather_list:
    print(f'[{idx}]')
    print(i)
    print('-'*30)
    idx += 1
#     print(f'[{idx}]\n{i.find(class_="period-name")}')
#     print(f'[{idx}]\n{i.find(class_="short-desc")}')

#     print(f'[{idx}]\n{i.find(class_= "temp temp-low")}')

#     print('------------------------')
#     idx += 1


idx = 1
for i in weather_list:
    # temp = i.find(class_="period-name").text
    print(f'[{idx}]')

    temp = i.find('p',class_="period-name").text
    print(f'[Period] : {temp}')

    temp = i.find('p', class_="short-desc").text
    print(f'[Short	desc]: {temp}')
    try:
        temp = i.find('p',class_="temp temp-low").text
        print(f'[Temperature] : {temp}')
    except:
        None
    try:
        temp = i.find('p',class_="temp temp-high").text
        print(f'[Temperature] : {temp}')
    except:
        None
    # temp = (i.find('p',class_="title")).text
    # print(f'[{idx}]\n{temp}')
    print('------------------------')
    idx += 1


"""