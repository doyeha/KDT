import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


file = r'C:\Git\KDT\BigData\EX_PY07\0726\daegu-utf8.csv'
weatherDF = pd.read_csv(file)
# 입력 받은 두 년도 사이에서, 지정된 특정 달의 평균을 선 그래프로 출력
# 그래프를 그리는 함수 제작 - 
# 1. 최고기온 그리는 거 하나, 최저 기온 그리는거 하나 해서. 한 plot에 2개의 그래프 제작.
# 


def draw_graph(max_temp_list, min_temp_list, year_list , month):
    plt.figure(figsize=(20,5))
    plt.plot(year_list, max_temp_list, marker='s', color='r', label = '최고기온')  # x축 / y축 데이터 입력 /
    for i,txt in enumerate(max_temp_list):
        plt.text(year_list[i], max_temp_list[i]-0.7, f'{txt}',  ha ='center')

    plt.plot(year_list, min_temp_list,marker='s', color='b', label ='최저기온') 
    for i,txt in enumerate(min_temp_list):
        plt.text(year_list[i], min_temp_list[i]+0.3, f'{txt}',  ha ='center',)
    # plt.ylabel() # 기온
    # plt.xlabel()   # 년도
    plt.legend()
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

    plt.title(f"{year_list[0]}년 부터 {year_list[-1]}년까지, {month}월의 기온 변화")
    plt.show()



def main():
    first = int(input('시작 연도를 입력하세요 : '))
    second = int(input('마지막 연도를 입력하세요 : '))
    month = int(input('기온 변화를 측정할 달을 입력하세요 : '))

    # 우선 날짜의 타입 확인
    # weatherDF['날짜'].dtype -> object // 요구사항 1. 문자열 형태의 날짜 열의 데이터를 datetime으로 바꾸자.
    weatherDF['날짜'] = pd.to_datetime(weatherDF['날짜'], format='%Y-%m-%d')
    # first와 second 사이의 년도 DF를 구한다.
    # 위 기간 동안의 DF에서 날짜의 m자리가 month와 일치하는 DF들을 다시 추출.
    # 년도에 맞춰 월 평균을 구한다! 말이 쉽다.

    # decadeDF = weatherDF[(weatherDF['날짜'].dt.year >= first)& (weatherDF['날짜'].dt.year <= second)]
    # de_monDF = decadeDF[decadeDF['날짜'].dt.month == month]

    # 입력받은 기간에 맞는 DF는 완성.
    # 이제 그 년도 별로 최저기온, 최고기온의 평균을 구해야한다.
    min_temp_list = []
    max_temp_list = []

    year_list = [i for i in range(first, second+1)]
    for i in year_list:
        a = weatherDF[(weatherDF['날짜'].dt.year==i) & (weatherDF['날짜'].dt.month==month)]['최저기온(℃)'].mean()
        a = float(round(a,1))
        min_temp_list.append(a)

        b = weatherDF[(weatherDF['날짜'].dt.year==i) & (weatherDF['날짜'].dt.month==month)]['최고기온(℃)'].mean()
        b = float(round(b,1))
        max_temp_list.append(b) 

    print(f'{first}년부터 {second}년까지의 {month}월의 기온 변화')
    print(f'{month}월의 최저 기온 평균 :]\n{min_temp_list}')
    print(f'{month}월의 최고 기온 평균 :]\n{max_temp_list}')
    draw_graph(max_temp_list, min_temp_list, year_list, month)


main()