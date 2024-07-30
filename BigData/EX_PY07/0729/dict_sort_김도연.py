city = {'Seoul':('South Korea','Asia', '9,655,000'),
        'Tokyo' : ('Japan','Asia','14,110,000'),
        'Beijing': ('China', 'Asia', '21,540,000'),
        'London': ('United Kingdom','Europe','14,800,000'),
        'Berlin': ('Germany', 'Europe','3,426,000'),
        'Mexico City': ('Mexico','America','21,200,000')}

menu = f"""{'-'*40}
1. 전체 데이터 출력
2. 수도 이름 오름차순 출력
3. 모든 도시의 인구수 내림차순 출력
4. 특정 도시의 정보 출력
5. 대륙별 인구수 계산 및 출력
6. 프로그램 종료
{'-'*40}"""
choice = 0
while True:
    while choice != 6:
        print(menu)
        choice = int(input('메뉴를 입력하세요.'))
        # 전체 데이터 출력
        if choice == 1:
            for idx, k in enumerate(city):
                print(f'[{idx+1}] {k}: {list(city[k])}')

        # 수도 이름 오름차순 정렬
        # 수도 이름을 기준으로 오름 차순 정렬, 자리수 맞춤
        elif choice ==2:
            city1 = sorted(list(city.keys()))
            idx = 1
            for i in city1:
                print(f"[{idx}]" + "{:<14}".format(i) + ": {:<20}".format(city[i][0])+ "{:<10}".format(city[i][1]) + "{:<20}".format(city[i][2]))
                idx += 1

        # 모든 도시 인구수 내림차순 출력
        # 자리수 맞춤, 수도이름, 인구수만 출력
        elif choice ==3:
            sorted_pop = sorted(city.items(), key=lambda item : int(item[1][2].replace(',','')), reverse=True)
            idx = 1
            for i in sorted_pop:
                print(f'[{idx}]' + '{:<15}'.format(i[0]) + ': {:>13}'.format(i[1][2]))
                idx+=1

        # 특정 도시 정보 출력 
        elif choice ==4:
            find = input('출력할 도시 이름을 입력하세요 : ')    # 도시 이름 검색. 
            if find not in list(city.keys()):
                print(f'도시 이름 {find}는 key에 없습니다.')
            else:
                print(f'도시 : {find}')
                print(f'국가 : {city[find][0]}, 대륙 : {city[find][1]} 인구수 : {city[find][2]}')

        elif choice ==5:
            # 대륙 아시아 유럽 아메리아 입력하면 그에 해당하는 키 값인 것 추출
            find_two = input('대륙 이름을 입력하세요(Asia, Europe, America) : ')
            print("엄... 미구현")
            # city.items[1][2]
    break