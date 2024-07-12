def add(n1,n2): return n1 + n2

## 현재 실행 중인 경우
if print(__name__) == '__main__':
    print("Test")
    print(f"add = > {add(10,3)}")