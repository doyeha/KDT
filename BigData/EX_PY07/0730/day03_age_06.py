import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_pie_chart(city, population_list, label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%',
            startangle=90, colors=plt.cm.Pastel2.colors,textprops={'fontsize':8})
    plt.legend(loc=1)
    plt.title(city + "학령 인구 비율")
    plt.show()

def draw_donut_chart(city, population_list, label_list):
    plt.pie(population_list, labels = label_list, autopct='%.1f%%',
            startangle=90, colors= plt.cm.Pastel2.colors,
            pctdistance=0.85, textprops={'fontsize':6})
    
    center_circle = plt.Circle((0,0), 0.7, facecolor = 'White')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    plt.legend(loc=1)
    plt.title(city+'학령 인구 비율')
    plt.show()

def get_population(row,start,end):
    population = 0
    for num in row[start:end+1]:
        num = num.replace(',','')
        num = int(num)
        population += num
    return population



def school_age_population(city):
    # 특정 지역의 인구 현황
    city_population = 0
    non_school_pop = 0
    school_age_pop = 0

    label_list = ['초등학생','중학생','고등학생','대학생','비학령인구']
    population_list = []

    f = open('age.csv', encoding = 'euc_kr')
    data = csv.reader(f)
    next(data)

    population_list = []
    city_name = ''
    city_population = 0
    voting_population = 0

    for row in data:
        if city in row[0]:
            city_population = row[1]
            city_population = city_population.replace(',','')
            city_population = int(city_population)

            elemantary_pop = get_population(row,9,14)
            population_list.append(elemantary_pop)

            middleschool_pop = get_population(row,15,17)
            population_list.append(middleschool_pop)

            highschool_pop = get_population(row, 18,20)
            population_list.append(highschool_pop)

            university_pop = get_population(row, 21,24)
            population_list.append(university_pop)

            school_age_pop = (elemantary_pop + middleschool_pop + highschool_pop + university_pop)

            non_school_pop = city_population - school_age_pop
            population_list.append(non_school_pop)
            break

    school_age_pop_rate = round((school_age_pop*100)/city_population,1)

    print(f'전체 인구수 : {city_population:,} ,'
          f'학령 인구수 : {school_age_pop:,} ,'
          f'학령 인구 비율 : {school_age_pop_rate}%')
    

    draw_pie_chart(city,population_list, label_list)
    draw_donut_chart(city,population_list, label_list)


city = input('학령 인구를 분석할 도시 이름 : ')
school_age_population(city)