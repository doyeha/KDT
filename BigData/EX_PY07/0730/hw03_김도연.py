import koreanize_matplotlib
import matplotlib.pyplot as plt
import csv
import re

def split_str(area):
    area_name = re.split('[()]', area)
    return area_name[0]


gu_list=['대구광역시','대구광역시 중구', '대구광역시 동구', '대구광역시 서구', '대구광역시 남구',
         '대구광역시 북구','대구광역시 수성구', '대구광역시 달서구',
         '대구광역시 달성군','대구광역시 군위군']

female_list = []
male_list = []

def draw_chart():
    fig,axs = plt.subplots(5,2, figsize = (10,13))
    idx = 0
    fig.suptitle('대구광역시 구별 남녀 인구비율', fontsize=15)
    for i in range(5):
        for j in range(2):
            # male_list[idx]female_list[idx]
            axs[i][j].pie([male_list[idx], female_list[idx]], labels=['남성','여성'],	autopct='%1.1f%%', startangle = 90)
            axs[i][j].set_title(f'{gu_list[idx]}')
            idx += 1
    # fig.tight_layout()
    plt.show()

def print_pop():
    idx = 0
    for gu in gu_list:
        print(f'{gu} : (남:', format(male_list[idx], ',d'), '여:', format(female_list[idx], ',d'),')')
        idx += 1

def main():
    f = open('gender.csv', encoding='euc_kr')
    data = csv.reader(f)
    next(data)
    total_pop_list = []
    gu_pop_sum = 0
    # main_city = '대구광역시'               

    for gu in gu_list:
        # print(gu)
        gu_feme_pop_sum = 0
        gu_me_pop_sum = 0
   
        for row in data:
            city = split_str(row[0]) # 그리고 숫자 제거.
            city = city.rstrip()
            # print(idx, gu)
            # print(city)
            # temp_city = row[0]
            
            if gu == city:
                gu_me_pop_sum = int(row[104].replace(',',''))
                gu_feme_pop_sum = int(row[207].replace(',',''))
                # print(gu_me_pop_sum, gu_feme_pop_sum)
                break
        # print(city)
        female_list.append(gu_feme_pop_sum)
        male_list.append(gu_me_pop_sum)
        # print(male_list,female_list)

    print_pop()
    draw_chart()
main()



"""
f = open('gender.csv', encoding='euc_kr')
data = csv.reader(f)
next(data)
total_pop_list = []
gu_pop_sum = 0
# main_city = '대구광역시'               
idx = 0
for gu in gu_list:
    # print(gu)
    gu_feme_pop_sum = 0
    gu_me_pop_sum = 0

    for row in data:
        city = split_str(row[0]) # 그리고 숫자 제거.
        city = city.rstrip()
        # print(idx, gu)
        # print(city)
        # temp_city = row[0]
        if gu == city:
            gu_me_pop_sum += int(row[104].replace(',',''))
            gu_feme_pop_sum += int(row[207].replace(',',''))
            # print(gu_me_pop_sum, gu_feme_pop_sum)
            break 
    # print(city)
    female_list.append(gu_feme_pop_sum)
    male_list.append(gu_me_pop_sum)
    idx+=1
print(male_list, female_list)
"""