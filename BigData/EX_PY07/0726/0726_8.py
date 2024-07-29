import pandas as pd

weather_df = pd.read_csv(r'C:\Git\KDT\BigData\EX_PY07\0726\daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)
print(weather_df['날짜'].dtype)

weather_df.columns=['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)

