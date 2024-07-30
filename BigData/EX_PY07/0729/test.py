city = {'Seoul':('South Korea','Asia', '9,655,000'),
        'Tokyo' : ('Japan','Asia','14,110,000'),
        'Beijing': ('China', 'Asia', '21,540,000'),
        'London': ('United Kingdom','Europe','14,800,000'),
        'Berlin': ('Germany', 'Europe','3,426,000'),
        'Mexico City': ('Mexico','America','21,200,000')}

# print(city.keys())

city1 = sorted(list(city.keys()))
# print(city1)


# sorted_city = sorted(city, key= lambda x : list(x.keys()))
# print(sorted_city)

# (len('Mexico City'))
# print(city.index[5])
# print(city['Seoul'][0])

# print(city.keys())

# for i in city.keys():
#     print(city[i][2])
# for i in city.keys():
#     sorted_pop = sorted(city, key=lambda x : int(x[i][2].replace(',','')))

# city[2]
# city
# sorted_pop = sorted(city.values(), key=lambda x : int(x[2].replace(',','')), reverse=True)
# # print(sorted_pop)
# for i in sorted_pop:
#     city[i]

# print(city['Beijing'].items[2])

# sorted_pop = sorted(city.items(), key=lambda item : int(item[1][2].replace(',','')), reverse=True)
# idx = 1
# # print(sorted_pop)
# for i in sorted_pop:
#         # print(f'[{idx}] {i[1][2]}')
#         print(f'[{idx}]', '{:<20}'.format(i[0]), ': {:<}'.format(i[1][2])) #f'{i[1][2]}' ) #
#         idx+=1

print(city.items[2])