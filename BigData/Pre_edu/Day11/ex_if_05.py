# -------------------------------------------------------
# 제어문 - 조건문 살펴보기
# -------------------------------------------------------
# [실습] 여러개 조건을 한꺼번에 검사하는 경우
# - 성별과 나이에 따라서 여탕/남탕
age_gender = input("나이와 성별 입력 (예: 4, 남) : ").strip()

if len(age_gender)>0:
    # 나이와 성별 분리
    # 나이와 성별에 따라서 입장할 탕 출력
    datas = age_gender.split(",")
    print(datas)
    # datas [1] == "여"
    age = int(datas[0].strip())
    gender = datas[1].strip()

    if (age<5 and gender =="남") or gender=="여":
        print("여탕으로 가세요~")
    else:
        print("남탕으로 가세요~")