import re


m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))

p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

m = re.match('[a-z]+', 'pythoN')
print(m)

m =re.match('[a-z]+', 'PYthon')
print(m)

print('\n\n\n')


print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', 'regexpython'))

print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN'))

print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))


print('\n\n\n 세번째째')


p = re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))


result = p.search('I like apple 123')
print(result)

result = p.findall('I like apple 123')
print(result)


print('\n\n\nMatch 메소드 예제')
tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')

print('tel_checker.match("02-123-4567") : ', tel_checker.match('02-123-4567'))
match_groups = tel_checker.match('02-123-4567').groups()
print('match_groups : ', match_groups)

print("tel_checker.match('053-950-45678) : ",tel_checker.match('053-950-45678'))
print("tel_checker.match('053950-4567') :",tel_checker.match('053950-4567'))



print('\n\n\nMatch 메소드 예제 #2')
tel_number = '053-950-4567'
tel_number = tel_number.replace('-','')
print(tel_number)

tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))


print('\n\n\nmatch 메소드 예제 #3')
tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})')
m = tel_checker.match('02-123-4567')

print('m.group() : ', m.group())
print('m.group(0) : ', m.group(0))
print('m.group(1) : ', m.group(1))
print('m.group(2,3) : ', m.group(2,3))
print('start() : ', m.start())
print('end() : ', m.end())



print('\n\n\ncell_phone')
cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')
print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))



