### 판다스
   파이썬 => 일반 프로그래밍
   판다스 => 데이터 분석 프로그래밍
            자료형 -> Series, DataFrame
            int64 float64  object(타입이 섞여있을 때)
            datetime, category, datadelta 
            다양한 파일들 ==> DataFrame
            read_(파일종류) : read_csv / read_excel / read_json

### Series
   Series / DataFrame  ==> 구성 : index + values / index+columns + values

### DataFrame
   -  DF 생성 / 저장
   - 행/열 인덱스 변경 전체변경 or 일부변경 == rename(index={}, columns = {})
   - 행/열 삭제 ==> drop() => 행/열 방향 --- axis = 0 행 인덱스 / axis = 1 열 컬럼
   - 특별한 매개변수 ==> inplace = False : 원본 DF 변경 여부 설정
   True면 원본 수정 / False면 복사본만 제공
   - 추출 
      * 시리즈에서 원소/요소 추출
      * 데이터프레임에서 원소.요소 추출, 형 추출, 열 추출 ==> 행 : iloc[] / loc[] 
   - 추가
      * 행 / 열 추가
   - 값 변경
      * 원소 / 행 / 열



   [행/열 인덱스 변경 방법]
   1. rename() : 부분 변경
   2. 속성 사용
      - index=[새로운 인덱스]
      - columnds=[새로운 칼럼] 

   [행/열 삭제 방법]
   1. drop 
   - 행 삭제 -> axis=0, 삭제하고 싶은 인덱스 지정
               -> index=삭제하고싶은 인덱스 
   - 열 삭제 -> axis = 1, 삭제하고 싶은 인덱스
               -> columns = 삭제하고 싶은 인덱스
   * inplace : 진짜 바꿔? 원본을 바꿔 ??? True = 바꾼다 . False 복사본 제거


   [행/열 추가 메서드]
   1. 행 추가 ==> loc[새로운 행] = 새로운 값
                              => 1개 : 전부 동일한 값
                              => 열의 수만큼 값
   2. 열 추가 ==> [새로운 행] = 새로운 값
                           => 1개 :> 전부 동일한 값
                           => 행의 수만큼 값


   [원소 선택 / 추가 메서드]
   1. 열 선택 ==> 변수명[열인덱스]
   2. 행 선택 ==> 변수명.loc[행인덱스] / 변수명iloc[행인덱스]
   3. 원소 선택 ==> 변수명.loc[행인덱스, 열인덱스] 
                  변수명.iloc[행인덱스, 열인덱스] 
                  변수명.loc[행인덱스][열인덱스] 
                  변수명.iloc[행인덱스][열인덱스]



   MutiIndex
         
      xs

   - 결측치


   [그룹화] #  Day06
   groupby 메서드
   groupby object라는 개체로 결과를 반환
    -- 결측치 처리 ==> 성별에 따라 치환 ==> 성별에 따른 그룹화
   # -- Group 객체의 속성
   groups 속성 : 그룹화된 그룹에 속하는 인덱스 정보 저장 Dict형태
   groupObj.groups => 그룹에 속해져있는 키와 값 딕셔너리 식으로 줄줄이 출력 -->
   indices 속성 : 각 그룹의 인덱스 속성을 저장 Dict형태
   get_group() 메서드 : 그룹화된 그룹들 중에서 특정 그룹 데이터 읽기 메서드 // 속성을 읽어오는 메서드
   groupObj.count()그룹별로 집계연산 수행

   [멀티인덱스] # Day06멀티인덱스

   



   #matplotlib
   plot(x, y, 'go--', linewidth=2, markersize=12)
   plot(x, y, color='green', marker='o', linestyle='dashed',
     linewidth=2, markersize=12)




[히스토그램] Day08


