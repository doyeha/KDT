from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')

soup = BeautifulSoup(html, 'html.parser')

# print(soup)

one = soup.find(class_ = 'tombstone-container')
# print(one)
"""
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
"""
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


# idx = 1
# for i in weather_list:
#     # temp = i.find(class_="period-name").text
#     print(f'[{idx}]')

#     temp = i.find('p',class_="period-name").text
#     print(f'[Period] : {temp}')

#     temp = i.find('p', class_="short-desc").text
#     print(f'[Short	desc]: {temp}')
#     try:
#         temp = i.find('p',class_="temp temp-low").text
#         print(f'[Temperature] : {temp}')
#     except:
#         None
#     try:
#         temp = i.find('p',class_="temp temp-high").text
#         print(f'[Temperature] : {temp}')
#     except:
#         None
#     # temp = (i.find('p',class_="title")).text
#     # print(f'[{idx}]\n{temp}')
#     print('------------------------')
#     idx += 1



# #seven-day-forecast-list > li:nth-child(1) > div > p.temp.temp-low