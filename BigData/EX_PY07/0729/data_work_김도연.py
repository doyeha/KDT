import	csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
f	=	open('subwaytime.csv',	encoding='utf-8-sig')
data	=	csv.reader(f)
next(data)
next(data)
"""
인덱스 11 ~ 13 하차의 것만 사용.
각 지하철 노선별 많이 내리는 지하철 역 분석
1~7호선별로 역 1개.
하차 인원은 1000명 단위로 콤마 찍어서 구분할 것 
막대 그래프 표시
x는 노선 + 지하철 역
y축은 인원수 

"""

# 인덱스 11에서 1호선인 것 만 뽑아서 하차 시간대에 있는 하차자들 총 합산.
max_passenger = [0]*7
max_statioin = [0]*7
for row in data:    # 열 싹 돌려보기
    for i in range(1,8):    # 호선 체크
        if (row[1] == f'{i}호선') & (max_passenger[i-1]<int(row[11])+int(row[13])):
            a = int(row[11])+int(row[13])
            max_passenger[i-1] = a
            
            max_statioin[i-1] = f'{i}호선 {row[3]}'
            # max_statioin.insert(row[3])
# print(max_passenger)
for i in range(1,8):
    print(f'출근 시간대 {i}호선 최대 하차역 : {max_statioin[i-1]}역, 하차인원 : ' + '{0:,}'.format(max_passenger[i-1]),'명')
    


plt.bar(max_statioin, max_passenger)
plt.xticks(rotation=70,	fontsize=8)
plt.title("출근 시간대 지하철 노선별 최대 하차 인원 및 하차역")
plt.tight_layout()
plt.show()