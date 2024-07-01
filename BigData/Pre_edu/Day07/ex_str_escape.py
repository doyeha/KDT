# print (" '안녕'이라고 한다. ") 가능.
# print (' "안" 녕') 가능.
# print ("안"녕"")  불가능. 인용구 사용 희망 시 서로 다른 ' " 에 넣을 것.
# ------------------------------------------------------------
# 이스케이프 문자 
# - 문자열 안에서 특별한 의미를 가지는 문자
# - 형식 : \알파벳1개
# - 대표 : \n = 줄바꿈 즉, 엔터키
#          \t - 탭키 입력, 일정 간격
#          \' - 인용구의 부호
#          \" - 인용구의 부호
#          \\ - \ 기호 자체 의미
#          \u - 유니코드 의미
# ------------------------------------------------------------

msg = "오늘은 좋은 날 행복한 날"

#[실습] 출력시 오늘은 좋은 날 출력 후 아래 줄에 행복한 날 출력하기.
msg1 = "오늘은 좋은 날 \n 행복한 날"

print(f'{msg[:8]} \n {msg[-5:]}')
print(msg1)
print(msg1, len(msg1))

msg2 = "오늘은\n좋은날\n행복한\n날"
print(msg2, len(msg2))

#[실습] 문자열 안에 인용구 표현하기.
# 나는 오늘 '행복'하다.
msg1 = "나는 오늘 '행복'하다!"
msg2 = '나는 오늘 "행복"하다!'
msg3 = "나는 오늘 \"행복\"하다!"
msg4 = '나는 오늘 \'행\'★★★\'복\'하다!'
print(f'{msg1}\n{msg2}\n{msg3}\n{msg4}')

# [실습]파일이나 폴더의 경로 문자열처리
# 파일이나 폴더의 경로를 나타내는 기호  \ 의미
file = "C:\\Users\\kjy19\\Downloads\\memo.py" #\User의 \U인줄 알고 난리.
print(file)

# [실습] 문자열내에서 이스케이프 문자를 무시하도록 설정
# raw의 약자 r. 
file = r"C:\Users\kjy19\Downloads\memo.py" #\User의 \U인줄 알고 난리.
print(file)