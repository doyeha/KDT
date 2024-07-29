import pandas as pd

weather_df = pd.read_csv(r'C:\Git\KDT\BigData\EX_PY07\0726\daegu-utf8.csv', encoding='utf-8-sig')

weather_df = weather_df.dropna(axis=0)
print(weather_df.count())
print(weather_df.head(5))


weather_df.to_csv('deagu-utf8-df.csv', index=False, mode='w', encoding='utf-8-sig')

print('특정 연도와 달의 최고,최저 기온 평균값 계산')

year_df = weather_df[wearther_df['날짜'].dt.year == 2023]
month_df = year_df[year_df['날짜'].dt.year == 8]
