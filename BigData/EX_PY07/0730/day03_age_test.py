temp_string = '1;2,3:456/789'

print(len(temp_string.split(';,')))
print(temp_string.split(';,'))

print(len(temp_string.split(',')))
print(temp_string.split(','))

city = '대구광역시 북구 산격3동'
print(city.split('('))
