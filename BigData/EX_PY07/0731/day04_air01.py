import pandas as pd
from tabulate import tabulate

dust = pd.read_excel('dust.xlsx')

print(dust.head())

dust.rename(columns={'날짜':'date', '아황산가스':'so2', '일산화탄소':'co', '오존':'o3', '이산화질소':'no2'}, inplace=True)

print(tabulate(dust.head(), headers='keys', tablefmt='pretty')) 

dust['date'] = dust['date'].str[:10]

print(tabulate(dust.head(), headers='keys', tablefmt='psql'))
dust['date'] = pd.to_datetime(dust['date'])

dust['year'] = dust['date'].dt.year
dust['month'] = dust['date'].dt.month
dust['day'] = dust['date'].dt.day
print(dust.columns)

dust = dust[['date','year','month','day','so2','co','o3','no2','PM10','PM2.5']]



print(dust.isna().sum())

print('결측치를 포함한 데이터 출력')
print(dust[dust.isna().any(axis=1)])
# print(dust[dust.isna().any(axis=0)])  # 오류 출력

print('결측치 채우기')

dust.ffill(inplace=True)
print(dust.isnull().sum())

print(dust.iloc[132:134])