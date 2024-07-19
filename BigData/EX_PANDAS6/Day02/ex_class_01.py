# ------------------------------------------------------------------
# 클래스 (Class)
# - 객체지향언어(OOP)에서 데이터를 정의하는 자료형
# - 데이터를 정의할 수 있는 데이터가 가진 속성과 기능 명시
# - 구성요소 : 속성/atrribute/field + 기능/method
# ------------------------------------------------------------------
# 클래스 정의 : 햄버거를 나타내는 클래스
# 클래스 이름 : 
# 클래스 속성 : 번, 패티, 야채, 치즈 
# 클래스 기능 : 

# ------------------------------------------------------------------
class Burger:
    # kind = "맥도날드"

    def __init__(self, bread, patty, veg, kind): # 힙 영역에 객체 생성 시 속성값 저장 기능
        self.bread = bread
        self.patty = patty
        self.veg = veg
        self.kind= kind

    # 클래스 기능, 메서드!
    def printInfo(self):
        print(f"브 랜드 : {self.kind}")
        print(f"빵 종류 : {self.bread}")
        print(f"패티 종류 : {self.patty}")
        print(f"야채 종류 : {self.veg}")
        
    # 속성을 변경하거나 읽어오는 메서드 => getter/setter 메서드
    def get_bread(self):
        return self.bread
    
    def set_bread(self, bread):
        self.bread = bread
    





# 객체 생성
# bergur1 = Burger() # 첫 실행 . __init__ missing 4 required 어쩌고 뜬다
burger1 = Burger("브리오슈", "불고기", "양상추 양파 토마토", '롯데리아')
# 치즈버거 객체 생성
burger2 = Burger("참깨곡물빵", "쇠고기패티", "치즈 양상추 양파 토마토", '맥도날드')

# 버거 정보 확인
burger1.printInfo()
# 속성 읽는 방법 : (1) 직접 접근 읽기 (2)간접 접근 읽기 - getter 메서드 사용
print(burger1.bread, burger1.get_bread())

# 속성 변경 방법 : (1) 직접 접근 읽기 (2)간접 접근 읽기 - getter 메서드 사용
burger1.bread = '들깨빵'
burger1.set_bread = '올리브빵'
burger2.printInfo()





