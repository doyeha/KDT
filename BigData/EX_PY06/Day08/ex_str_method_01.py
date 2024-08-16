# ------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
# ------------------------------------------------------------------

msg = "Hello 0705"

# [원소 / 요소 인덱스 찾기 메서드 - find (문자 1개 또는 문자열)]
# H 의 인덱스
idx = msg.find("H")
print(f"H의 인덱스 : {idx}")

# H 의 인덱스
idx = msg.find("7")
print(f"H의 인덱스 : {idx}")

# llo 의 인덱스  -> 시작 위치 인덱스 반환 // 대소문자 일치, 존재하지 않으면 -1 반환
idx = msg.find("llo")
print(f"H의 인덱스 : {idx}") 



# [원소 / 요소 인덱스 찾기 메서드 - index (문자 1개 또는 문자열)]
# H 의 인덱스
idx = msg.index("H")
print(f"H의 인덱스 : {idx}")

# idx = msg.index("h")
# print(f"H의 인덱스 : {idx}")  => 오류 발생

if "h" in msg:
    idx = msg.index("h")
    print(f"h의 인덱스 : {idx}")
else:
    print("h는 존재하지 않습니다.")



# ------------------------------------------------------------------
# 문자열에 동일한 문자가 여러 개 존재하는 경우
# ------------------------------------------------------------------
msg = "Good Luck Good"
#      01234567890123
# "o"의 인덱스 찾기 => 첫 번째 "o" 인덱스
idx = msg.index("o")
print(f"h의 인덱스 : {idx}")

# "o"의 인덱스 찾기 => 두 번째 "o" 인덱스
idx = msg.index("o", idx+1)  # index(찾을 문자 or 문자열, 서치 시작 인덱스 Default=0)
print(f"h의 인덱스 : {idx}")

# "o"의 인덱스 찾기 => 세 번째 "o" 인덱스
idx = msg.index("o", idx+1) 
print(f"h의 인덱스 : {idx}")

# -"o"의 인덱스 찾기 => 네 번째 "o" 인덱스
idx = msg.index("o", idx+1) 
print(f"h의 인덱스 : {idx}")

cnt = msg.count("o")
print(f"h의 개수 : {cnt}")

### 위 내용을 for반복문으로 정리.
c = 0
idx = msg.index("o") 
for i in range(cnt): #cnt로 목표 문자,문자열의 갯수를 구하고 그만큼 반복
    print(f"h의 {i}번째 인덱스 : {idx+c}")
    c += 1

# ------------------------------------------------------------------
# 문자열의 뒷부분부터 찾기 하는 메서드 ==> rfind(), rindex()    // reverse의 r
# ------------------------------------------------------------------
msg = "Happy"

# -'y'의 인덱스 찾기
idx = msg.rindex("y") 
print(f"y의 인덱스 : {idx}")

# "Happy"
# -'p' 첫 번째 인덱스 찾기
idx = msg.rfind("p") 
print(f"p의 인덱스 : {idx}")  # 결과 : 3

# "Hap"
# -'p'의 두 번째 인덱스 찾기
idx = msg.rfind("p",0,idx)  # 위 첫번째 인덱스를 찾으면서 idx가 이미 3임. 그래서 인덱스 0,1,2 Hap 내에서만 보기 때문에 결과는 아래와 같다.
print(f"p의 인덱스 : {idx}")  # 결과 : 2

"""
find() index() 
방향  --->
     "Happy"
인덱스 01234
방향  <----
rfind() rindex()
()구성 : 문자, 시작인덱스, 끝인덱스+1

"""


# - 파일명에서 확장자 txt,jpeg,xlsx, zip 찾기
# - hello.txt => 기준점 .을 찾아서 . 뒤로 슬라이싱 추출
files = ["2024년 상반지 경제분석.docs", "hello.txt", "kakao_1234123123.jpg"]
# self
for i in files:
    print(i[i.index(".")+1:], end = ", " if i == files[-1] else "\n")
# .의 인덱스 추출, +1 로 그 뒤의 요소부터 슬라이싱: 끝까지 추출.
# # day07에 형식 뭐 있었는데 ?

print()
# teacher
for file in files:
    dot = file.find(".")
    print(file[dot+1:])
