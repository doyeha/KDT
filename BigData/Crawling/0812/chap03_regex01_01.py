import re

lookhead1 = re.search('.+(?=won)', '1000 won')
if(lookhead1 != None):
    print(lookhead1.group())
else:
    print('None')
lookhead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookhead2.group())

lookhead3 =re.search('\d{4}(?!-)', '010-1234-5678')
print(lookhead3)



print('\n\n\n후방 탐색')
lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+', 'USD $51')
print(lookbehind2)

lookbehind3 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples')
print(lookbehind3)