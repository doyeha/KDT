import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)

    station_list = []
    max_num = -1
    max_station = ''

    for row in data[:5]:
        print(row)