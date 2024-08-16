# # 커피 가격 300원 . 물품에 따라 재료 소모값이 다르다.
# # 
# # 재료 부족 시 종료
# # 재료 현황 업데이트 및 지속적으로 출력
# # 


# class VendinMachine:
#     def __init__(self, input_dict):
#         self.input_money = 0
#         self.inventory = input_dict


#     # def manu():
#     #             print('1. 블랙 커피')
#     #     print('2. 프림 커피')
#     #     print('3. 설탕 프림 커피')
#     #     print('4. 재료 현황')
#     #     print('5. 종료')

#     # coin = 0
#     # remain_Coffee = 500
#     # remain_cream = 100
#     # remain_sugar = 100
#     # remain_cup = 5
    
#     def run(self): # 기능 구현 및 다른 메소드 호출     
#         put_coin = input('동전을 투입하세요 : ')
#         put_coin = int(put_coin)
#         if put_coin < 300:
#             print('금액이 부족합니다.')
#         else:
#             while True:
#                 coin = 0
#                 remain_Coffee = 500
#                 remain_cream = 100
#                 remain_sugar = 100
#                 remain_cup = 5

#                 coin += put_coin
#                 print("-" * 30)
#                 print(f'       커피자판기 (잔액 : {coin}원)')
#                 print("-" * 30)
#                 print('1. 블랙 커피')
#                 print('2. 프림 커피')
#                 print('3. 설탕 프림 커피')
#                 print('4. 재료 현황')
#                 print('5. 종료')
#                 input_manu = input('메뉴를 선택하세요. : ')
                
#                 if input_manu == 1:
#                     print(f'블랙 커피를 선택하셨습니다. 잔액 : {coin - 300}')
#                     Coffee.pick_coffee(black_coffee)
#                     print(remain_Coffee, remain_cream, remain_sugar, remain_cup)
#                     # print(coffee_machine.inventory)
#                 elif input_manu == 2:
#                     print(f'프림 커피를 선택하셨습니다. 잔액 : {coin - 300}')
#                     Coffee.pick_coffee(cream_coffee)
#                     print(coffee_machine.inventory)
#                 elif input_manu == 3:
#                     print(f'설탕 프림 커피를 선택하셨습니다. 잔액 : {coin - 300}')
#                     Coffee.pick_coffee(sugar_cream_coffee)
#                     print(coffee_machine.inventory)
#                 elif input_manu == 4:
#                     print(coffee_machine.inventory)
#                     print('돌아는 가니 ?')
#                 elif input_manu == 5:
#                     print('기기를 종료합니다')
#                     break

    

class Coffee:
    def __init__(self, coffee, cream, sugar, water):
        self.coffee = coffee
        self.cream = cream
        self.sugar = sugar
        self.water = water


    def pick_coffee(coffee):
        remain_Coffee -= coffee.coffee
        remain_cream -= coffee.cream
        remain_sugar -= coffee.sugar
        remain_cup -= 1


black_coffee = Coffee(30, 0, 0, 10)
cream_coffee = Coffee(30,15,0,100)
sugar_cream_coffee = Coffee(10,10,10,100)


remain_Coffee = 0
remain_cream = 600
remain_sugar = 500
remain_cup = 5

Coffee.pick_coffee(black_coffee)
print(remain_Coffee, remain_cream, remain_sugar, remain_cup)