# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 당신의 차가 도난당했습니다!
# 당신의 차가 언제, 어디에 있었는지에 따라 범인이 체포될 확률이 달라지는군요.
# 시간, 

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
from pydoc import html # html 코드 관련 : html을 객체로 처리?

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="en">
         <head>
          <meta charset="UTF-8">
          <title>---AI언어판별---</title>
         </head>ㅠ                                            
         <body>
          <form>
            <text> 시간 </text>
            <textarea name="text" rows="1" colos="4" >{text}</textarea>
            <p><input type="submit" value="언어감지">{msg}</p>
          </form>
        
          # 
          <form2>
            <h1> IUCR : 당신이 세운 차의 종류 (0~3) </h1>
            <select>
                <option>0</option>
                <option>1</option>
                <option>2</option>
                <option>3</option>
            </select>
         </form2>

         
         <form3>              
           <h1> District :  </h1>
            <select>
                <option>4.</option>
                <option>19.</option>
                <option>2.</option>
                <option>6.</option>
                <option>24.</option>

                <option>7.</option>
                <option>12.</option>
                <option>11.</option>
                <option>15.</option>
                <option>16.</option>

                <option>25.</option>
                <option>8.</option>
                <option>17.</option>
                <option>20.</option>
                <option>22.</option>

                <option>10.</option>
                <option>5.</option>
                <option>1.</option>
                <option>14.</option>
                <option>18.</option>

                <option>9.</option>
                <option>3.</option>
                <option>31.</option>
            </select>
         </form3>

         <form4>              
           <h1> Ward :  </h1>
            <select>
                <option>1.</option>
                <option>2.</option>
                <option>3.</option>
                <option>4.</option>
                <option>5.</option>
                <option>6.</option>
                <option>7.</option>
                <option>8.</option>
                <option>9.</option>
                <option>10.</option>
                <option>11.</option>
                <option>12.</option>
                <option>13.</option>
                <option>14.</option>
                <option>15.</option>
                <option>16.</option>
                <option>17.</option>
                <option>18.</option>
                <option>19.</option>
                <option>20.</option>
                <option>21.</option>
                <option>22.</option>
                <option>23.</option>
                <option>24.</option>
                <option>25.</option>
                <option>26.</option>
                <option>27.</option>
                <option>28.</option>
                <option>29.</option>
                <option>30.</option>
                <option>31.</option>
                <option>32.</option>
                <option>33.</option>
                <option>34.</option>
                <option>35.</option>
                <option>36.</option>
                <option>37.</option>
                <option>38.</option>
                <option>39.</option>
                <option>40.</option>
                <option>41.</option>
                <option>42.</option>
                <option>43.</option>
                <option>44.</option>
                <option>45.</option>
                <option>46.</option>
                <option>47.</option>
                <option>48.</option>
                <option>49.</option>
                <option>50.</option>
            </select>
         </form4>

         <form5>              
           <h1> Community Area :  </h1>
            <select>
                <option>0.</option>
                <option>1.</option>
                <option>2.</option>
                <option>3.</option>
                <option>4.</option>
                <option>5.</option>
                <option>6.</option>
                <option>7.</option>
                <option>8.</option>
                <option>9.</option>
                <option>10.</option>
                <option>11.</option>
                <option>12.</option>
                <option>13.</option>
                <option>14.</option>
                <option>15.</option>
                <option>16.</option>
                <option>17.</option>
                <option>18.</option>
                <option>19.</option>
                <option>20.</option>
                <option>21.</option>
                <option>22.</option>
                <option>23.</option>
                <option>24.</option>
                <option>25.</option>
                <option>26.</option>
                <option>27.</option>
                <option>28.</option>
                <option>29.</option>
                <option>30.</option>
                <option>31.</option>
                <option>32.</option>
                <option>33.</option>
                <option>34.</option>
                <option>35.</option>
                <option>36.</option>
                <option>37.</option>
                <option>38.</option>
                <option>39.</option>
                <option>40.</option>
                <option>41.</option>
                <option>42.</option>
                <option>43.</option>
                <option>44.</option>
                <option>45.</option>
                <option>46.</option>
                <option>47.</option>
                <option>48.</option>
                <option>49.</option>
                <option>50.</option>
                <option>51.</option>
                <option>52.</option>
                <option>53.</option>
                <option>54.</option>
                <option>55.</option>
                <option>56.</option>
                <option>57.</option>
                <option>58.</option>
                <option>59.</option>
                <option>60.</option>
                <option>61.</option>
                <option>62.</option>
                <option>63.</option>
                <option>64.</option>
                <option>65.</option>
                <option>66.</option>
                <option>67.</option>
                <option>68.</option>
                <option>69.</option>
                <option>70.</option>
                <option>71.</option>
                <option>72.</option>
                <option>73.</option>
                <option>74.</option>
                <option>75.</option>
                <option>76.</option>
                <option>77.</option>
            </select>
         </form5>

         <form6>              
           <h1> ATTEMPT :  </h1>
            <select>
                <option>0</option>
                <option>1</option>
            </select>
         </form6>

         <form7>              
           <h1> RECOVERY :  </h1>
            <select>
                <option>0</option>
                <option>1</option>
            </select>
         </form7> 

         <form8>              
           <h1> Location : 장소  </h1>
            <select>
                <option> 0 </option>
                <option> 1 </option>
                <option> 2 </option>
                <option> 3 </option>
                <option> 4 </option>

                <option> 5 </option>
                <option> 6 </option>
                <option> 7 </option>
                <option> 8 </option>
            </select>    
         </form8> 



         </body>
        </html>""")

    
# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------
# 함수명 : detectLang
# 재 료 : 사용자 입력 데이터
# 결 과 : 판별 언어명(영어, 프랑스~)

def detectLang(text):
    # 모든 문자 통일 -> 소문자
    text = text.lower()
    print(f'text=>{text}')
    
    # 문자 1개씩 읽어서 a~z 사이 있는 것만 카운팅
    codeA, codeZ = (ord('a'), ord('z'))
    cnt = [ 0 for n in range(26)]
    print(f'cnt => {cnt}')
    
    for ch in text:
        # 예 : ch가 a인 경우
        print(f'ch=>{ch} :{ord(ch)}')
        if codeA <= ord(ch) <= codeZ:
            cnt[ord(ch)-codeA] += 1
    print(f'cnt=>{cnt}')
    
    # text내의 a~z 빈도 계산
    total = sum(cnt)
    freq = list(map(lambda n: n/total, cnt))
    print(f'freq => {freq}')
    
    # 판별요청 & 결과 반환
    result = 'en' # langModel.predict([freq])
    langDict = {'en':'영어', 'ft':'프랑스어', 'id': '인도네시아어', 'tl':'타갈로그어'}
    
    return langDict['en']



# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = os.path.dirname(__file__)+ '/lang.pkl' # 웹상에서는 절대경로만
else:
    pklfile = './lang.pkl'
    
# langModel = joblib.load(pklfile)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
text = form.getvalue("text", default="")
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 판별하기
msg =""
if text != "":
    resultLang = detectLang(text)
    msg = f"{resultLang}"

# (4) 사용자에게 WEB 화면 제공
showHTML(text,msg)
