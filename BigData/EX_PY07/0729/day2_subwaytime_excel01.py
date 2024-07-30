

import pandas as pd
from tabulate import tabulate


df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
# print(df.head())
# print(df.columns)
# print(df[('호선명','Unnamed: 1_level_1')])
commute_time_df = df.iloc[:,[1,3,10,12,14]]
# print(tabulate(commute_time_df.head(), headers='keys', tablefmt = 'psql'))


# print(df[('지하철역','Unnamed: 3_level_1')])
# print(commute_time_df.dtypes)

# commute_time_df[('07:00:00~07:59:59','승차')] = commute_time_df[('07:00:00~07:59:59','승차')].apply(lambda x : x.replace(',',''))
# commute_time_df[('08:00:00~08:59:59','승차')] = commute_time_df[('08:00:00~08:59:59','승차')].apply(lambda x : x.replace(',',''))
# commute_time_df[('09:00:00~09:59:59','승차')] = commute_time_df[('09:00:00~09:59:59','승차')].apply(lambda x : x.replace(',',''))
# print(tabulate(commute_time_df.head(), headers='keys', tablefmt='psql'))

commute_time_df = commute_time_df.astype({('07:00:00~07:59:59','승차'):'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59','승차'):'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59','승차'):'int64'})
print(tabulate(commute_time_df.dtypes))




row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)
passenger_number_list = row_sum_df.to_list()
print(row_sum_df)