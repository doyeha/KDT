
import csv

f = open('age.csv', encoding = 'euc_kr')
data = csv.reader(f)

header = next(data)

print('-'*40)
print('{:-^40}'.format(' age.csv index '))
print('-'*40)

for i in range(len(header)):
    print(f'[{i:3}]: {header[i]}')

f.close()