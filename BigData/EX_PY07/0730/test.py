import koreanize_matplotlib
import matplotlib.pyplot as plt
import csv
import re

def split_str(area):
    area_name = re.split('[()]', area)
    return area_name[0]

f = open('gender.csv', encoding='euc_kr')
data = csv.reader(f)
next(data)


gu_list=['대구광역시 중구', '대구광역시 동구', '대구광역시 서구', '대구광역시 남구', '대구광역시 북구',
         '대구광역시 수성구', '대구광역시 달서구', '대구광역시 달성구', '대구광역시 군위군']

"""
for gu in gu_list:
    for row in data:
        city = split_str(row[0])
        city = city.rstrip()
        len(city)
        # print(city)
        print(f'{gu},{len(gu)},{city},{len(city)}')
        if gu == city:
            print("-----")

"""

for gu in gu_list:
    print(f'{gu},{len(gu)}')

    # for row in data:
    #     if city in row[0]:  # 대구광역시 들어가잇는 것만 찾음
    #         city = split_str(city) # 그리고 숫자 제거.
    #         # 
    #         for gu in gu_list:
    #             if gu == city:
    #                 gu_pop_sum += int(row[104].replace(',',''))
    #         total_pop_list.append(gu_pop_sum)
            # gu_pop_sum = 0