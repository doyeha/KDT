import pandas as pd
weather_df = pd.read_csv(r'C:\Git\KDT\BigData\EX_PY07\0726\daegu-utf8.csv', encoding='utf-8-sig')

print('특정 연도와 달의 최고, 최저 기온 평균값 계산')

year_df =  weather_df[weather_df['날짜'].dt.year== 2023]
month_df = year_df(year_df['날짜'].dt.month==8)
print(month_df.head(5) )

