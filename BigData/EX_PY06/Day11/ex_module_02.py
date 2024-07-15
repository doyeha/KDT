## ------------------------------------------------------------------
## 모듈 - 파이썬 파일(py) 1개
## - 구성 : 변수, 함수, 클래스가 존재
## -        만드시 모두 다 있지는 않음!
## - 종류 : 내장모듈 / 사용자정의모듈 / 써드파티션모듈 (설치 필수)
## ------------------------------------------------------------------
## 사용법 =? 혀재 파이선 파일에 포함시켜야 사용 가능함
## 모듈 내에서 일부 변수, 함수, 클래스만 포함하는 경우
## - 형식 : from 모듈명 import 변수명/함수명/클래스명
## - 주의 : 파일안에 동일한 변수명 / 함수명 / 클래스가 존재한다면 해당 파일에 
##          변수명 / 함수명 / 클래스 사용됨

from math import pi, factorial
from random import *        # * 의미 : 모든 것. -> random.~ 라고 안해도 됨.
from ex_module_01 import *  # 내 파일도 쌉가넝
# 현재 여기서는 factorial이 색이 다른데, 이건 쓰겟다고 가져와 놓고 안써서 그런다.


## 사용 : 바로 변수명 / 함수() / 클래스명
print(f"내장모듈 math 안에 있는 pi 변수 사용 : {pi}")
## math 중에서도 pi만 가져왔기 때문에 math.pi가 아니라 pi만 사용해도 가능하다.
# print(math.fatorial())
# -> 얘는 math에 들어있었던 것이기때문에 math 중에서도 pi만 가져온 상태에서는 불가능.
# 그냥 factorial을 쓰고 싶다면 ?
"""
from math import pi, factorial
print(math.fatorial())
 이렇게 가져올 바구니에서 담아버리면 끗
"""

## 전역변수
pi = "Apple"
def factorial(): pass

# 이미 math의 pi를 쓰고 잇는데 pi라는 동일한 이름의 전역변수를 사용해버리게 되면, 내 파일 안에 있는 것을 우선적으로 쓴다.



print(random())