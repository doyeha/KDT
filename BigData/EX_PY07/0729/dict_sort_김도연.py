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
            sorted_pop = sorted(city.items, key=lambda x : int(x.item[2].replace(',','')), reverse=True)
            idx = 1
            for i in sorted_pop:
                print(f'[{idx}]' + '{:<20}'.format(city.key(i)) + ': {:<}'.format(i[2]))






        # 특정 도시 정보 출력 
        elif choice ==4:
            print(5)
        elif choice ==5:
            print(6)
    break