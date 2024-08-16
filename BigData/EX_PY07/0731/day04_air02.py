import pandas as pd
from tabulate import tabulate
weather = pd.read_excel('weather.xlsx')
dust    = pd.read_excel('dust.xlsx')

print(tabulate(weather.head(), headers='keys', tablefmt='psql'))
print(weather.info())

weather.drop(['지점', '지점명'], axis=1, inplace=True)

weather.columns = ['date','temp','wind','rain','humidity']
print(tabulate(weather.head(), headers='keys', tablefmt='pretty'))


weather['date'] = pd.to_datetime(weather['date'].dt.date)
# print(weather.info())
# print(weather.head())

print('날씨 데이터 결측치 개수 확인하기')
print(weather.isna().sum())

print('날씨 데이터에서 결측치를 포함하는 행 출력')
print(weather[weather.isna().any(axis=1)])

weather.ffill(inplace=True)
print(weather.isna().sum())

print(weather.iloc[[368,565,742]])


print('강수량이 0인 항목을 0.01로 변경')
weather['rain'] = weather['rain'].replace(0,0.01)
print(weather['rain'].value_counts())

print('dust, weather의 크기 확인')
print('dust.shape :', dust.shape)
print('weather.shape : ', weather.shape)

print(dust.iloc[740:])
print(weather.iloc[740:])

dust.drop(index=743, inplace=True)
print(dust.shape)

merged_df = pd.merge(dust,weather, on = 'date')
print(merged_df.head ())