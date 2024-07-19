# -----------------------------------------------------
# Series/DataFrame에서 사용되는 사용자 정의 함수들
# ------------------------Docs string-----------------------------
# 함수 기능 : DataFrame의 기본 정보와 속성 확인 기능
# 함수 이름 : checkDataFrame
# 매개 변수 : DataFrame 인스턴스 변수명
# 리턴값 / 반환값 : (없음)
# -----------------------------------------------------
def checkDataFrame(object, name):
    print(f'\n[{name}]')
    object.info()
    print(f'[Index] : {object.index}')
    print(f'[Columns] : {object.columns}')
    print(f'[NDim] : {object.ndim}')


