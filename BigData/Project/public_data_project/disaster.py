import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import csv

""" 파일 따로 저장하는 방법 Ex
fout = open('C:\Git\KDT\BigData\EX_PY07\daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig')
wr = csv.writer(fout)
fout.close()
"""

file_name = 'GlobalLandTemperatures.csv'

Climate = pd.read_csv(file_name, encoding = 'utf-8')

Climate['dt'] = pd.to_datetime(Climate['dt'])
# print(Climate.columns)
# print(Climate.info())

Climate.drop(Climate[(Climate['dt'].dt.year) < 1980], axis=1, inplace=True)

print(Climate.head())




import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import csv


file_name = 'Climate_year_DF.xlsx'
storm = 'pacific.csv'
Climate = pd.read_excel(file_name)
Cyclone = pd.read_csv(storm)
Cyclone['Date']	=	pd.to_datetime(Cyclone['Date'],	format='%Y%m%d')
Cyclone = Cyclone[(Cyclone['Date'].dt.year>=1980) & (Cyclone['Date'].dt.year<=2010)]
Cyclone.drop(['Low Wind NE','Low Wind SE','Low Wind SW','Low Wind NW','Moderate Wind NE','Moderate Wind SE','Moderate Wind SW','Moderate Wind NW','High Wind NE','High Wind SE','High Wind SW','High Wind NW'], axis=1, inplace=True)
Cyclone['Name']= Cyclone['Name'].str.rstrip().str.lstrip()
Created_Cyclone = []
for y in range(1980,2011):
    Created_Cyclone.append(len(Cyclone[Cyclone['Date'].dt.year == y]['ID'].unique()))
Created_Cyclone
CC = {}
idx = 0
for i in range(1980,2011):
    CC[f'{i}'] = Created_Cyclone[idx]
    idx+=1
CC = list(CC.keys())