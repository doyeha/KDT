# ------------------------------------------------------------------
# 문자열 str 데이터 다루기
#   - 문자열 원소/요소 변경 체크
msg = "Pithon"
#   012345

"""
# [1]원소/요소 값 변경 ==> 미지원! 불가!
msg[1]="y"

# [2]원소/요소 삭제 ==> 명령어 del() || del  ==> 미지원!불가능!
del(msg[1])
del msg[1]
"""

#명령어 del(), del
del(msg)
#print(msg)    #삭제 후 변수 접근 Error!

"""
str 데이터 타입의 특징
1. 인덱싱 & 슬라이싱으로 원소/요소 접근
2. 원소/요소 단위 변경 즉, 수정과 삭제 불가
3. 산술연산자 중에 덧셈(+) => str+str => 문자열 하나로 연결
                  곱셈(*) => str*int => 정수만큼 반복해서 문자열 연결
4. 멤버연산자 in, not in 사용
5. 내장함수 len(), ord(문자 1개), chr(코드 1개)
"""




