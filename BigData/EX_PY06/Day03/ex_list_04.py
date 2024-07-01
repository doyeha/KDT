# ------------------------------------------------------------------
# List 데이터 자료형 살펴보기
#  - List와 str
# ------------------------------------------------------------------
msg = "Happy"
# str => list형변환
datas = list(msg)
print(datas)
toa = ""
for i in datas:
    toa = toa + str(i)
    print(i, toa)
print(type(toa), toa)
 # str은 수정, 추가 불가능 = 리스트화 후 다시 str형으로 변경.


msg = ['Happy']
datas = list(7)   # 문자열 하나는 글자수대로 쪼개지는데 인트는 그냥 딱 1개니까. 뭉탱이가 들어와야하는 리스트에 적용이 안된다. iterable Error
print(datas)

map(int, [12,3]) # map도 유사하게 여러개가 와야한다.
map(int, '3') # 문자는 그 자체로 iterable.



"""졸려요 지ㅏㅂ갈래요 졸려욜어라ㅣ으아아아앙ㄱ"""


