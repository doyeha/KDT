# -------------------------------------------------------
# 제어문 - 중첩 조건문 살펴보기
# - 조건문 안에 조건문이 들어 있는 혀애
# -------------------------------------------------------
# [실습] 입력 받은 데이터를 검사 후 데이터가 존재하는 경우와 그렇지 않은 경우에 대한 처리
# - 좋아하는 연예인 이름 입력 처리
name = input("좋아하는 연예인 이름을 적어주세요.").strip()
print(f"len(name) : {len(name)}개")
# 입력 데이터 존재 여부 체크
if len(name)>0:
    if name.isalpha():
        print(f"당신은 {name}을 좋아하는 군요!")
    else:
        print("이름을 입력해주세요.")
else:
    print("입력된 데이터가 없습니다.")
