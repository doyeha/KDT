jumin = input("주민번호를 입력해주세요 ex)990103-1079700 :")
jumin = jumin.split("-")
year = jumin[0][:2] # 99
gender = jumin[1][:1] # 1

if gender == "1":
    age="19" + year
    age = 2024 - int(age)
    gender = "남성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
elif gender == "2":
    age="19"+str(year)
    age = 2024 - int(age)
    gender = "여성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
elif gender == "3":
    age="20"+str(year)
    age = 2024 - int(age)
    gender = "남성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
elif gender == "4":
    age="20"+str(year)
    age = 2024 - int(age)
    gender = "여성"
    print(f" 성 별 : {gender} \n 나 이 : {age}세")
else:
    ("주민번호를 다시 입력해주세요.")
