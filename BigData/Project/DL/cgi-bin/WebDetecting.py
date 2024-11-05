# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch
import torch.functional as F
import torch.nn as nn
from pydoc import html # html 코드 관련 : html을 객체로 처리?
import pandas as pd
from torch.utils.data import Dataset, DataLoader

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 모델 정의
class BinClaModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(8,10)
        self.hid_layer1 = nn.Linear(10,15)
        self.hid_layer2 = nn.Linear(15,20)
        self.hid_layer3 = nn.Linear(20,10)
        self.out_layer = nn.Linear(10,1)

        self.dropout = nn.Dropout(0.5)

    def forward(self,x):
        y = self.in_layer(x)
        y = F.relu(y)
        y = self.dropout(y)
        y = self.hid_layer1(y)
        y = F.relu(y)
        y = self.dropout(y)
        y = self.hid_layer2(y)
        y = F.relu(y)
        y = self.hid_layer3(y)
        y = F.relu(y)

        return torch.sigmoid(self.out_layer(y))

# 모델 로드 함수
def load_model(model_path):
    model = BinClaModel()
    model.load_state_dict(torch.load(model_path, weights_only=False))
    model.eval()
    return model

class BinDataset(Dataset):
    def __init__(self, featureDF, targetDF):
        self.featureDF = featureDF
        self.targetDF = targetDF
        self.n_rows = featureDF.shape[0]
        self.n_features = featureDF.shape[1]

    def __len__(self) : 
        return self.n_rows

    def __getitem__(self, index):
        # 텐서화
        # print("피쳐", self.featureDF.dtypes)
        # print("타겟",self.targetDF.dtypes)
        # self.featureDF.iloc[index].values.astype(float)
        # self.targetDF.iloc[index].values.astype(float)
        feaureTS = torch.FloatTensor(self.featureDF.iloc[index].values.astype(float))
        targetTS = torch.FloatTensor(self.targetDF.iloc[index].values.astype(float))

        
        # 피처와 타겟 반환
        return feaureTS, targetTS

def predict(model, data):
    def preprocessing(text):
        datadict = {'Date':text[0], 'IUCR':text[1], 'District': text[2], 'Ward':text[3], 'Community Area':text[4], 'ATTEMPT':text[5], 'RECOVERY':text[6], 'Location':text[7]}
        return datadict
    
    data=preprocessing(data)
    dataDF=pd.DataFrame([data])
    print(dataDF)
    model.eval()
    input_data = torch.FloatTensor(dataDF.values)  # 입력 데이터와 장치 설정
    with torch.no_grad():
        predictions = model(input_data)

    predicted_classes = torch.argmax(predictions, dim=1)
    return predicted_classes

# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(result):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
<!DOCTYPE html>
    <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>---범죄 체포 예측---</title>
          <h> 내가 범죄를 당했다면? 범인이 체포될것인가 시뮬레이션 </h>
        </head>  

        <body>
            <form>
                <label for="time"> 시간 </label>
                <textarea id = 'time' name="text" rows="1" colos="4" ></textarea>
                
            </form>

            
            <form2>
                <label for="iucr"> IUCR : 당신이 세운 차의 종류 
                    <select id= 'iucr'>
                        <option>0</option>
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                    </select>
                </label>
            </form2>

            
            <form3>              
            <label for="district"> District :
                    <select id ="district">
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
                </label>
            </form3>

            <form4>              
            <label for="ward"> Ward :
                    <select id = 'ward'>
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
                </label>
            </form4>

            <form5>              
            <label for="community"> Community Area :  
                    <select d = 'community'>
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
                </label>
            </form5>

            <form6>              
            <label for="attempt"> ATTEMPT :
                    <select id = "attempt">
                        <option>0</option>
                        <option>1</option>
                    </select> 
            </label> 
            </form6>

            <form7>              
            <label for="recovery"> RECOVERY :
                    <select id ="recovery">
                        <option>0</option>
                        <option>1</option>
                    </select>
                </label>
            </form7> 

            <form8>              
            <label for="location"> Location : 장소
                    <select id = "location">
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
                </label>
            </form8> 
            <p><input type="submit" value="언어감지"></p>
            <p> 결과 : {result}</p>
        </body>
    </html>""")


# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------
# 함수명 : detectLang
# 재 료 : 사용자 입력 데이터
# 결 과 : 판별 언어명(영어, 프랑스~)

# def detectLang(text):

#     # 순서대로 시간, 차량, 구역, 구역2, 커뮤지역, 시도, 회수, 장소
#     # , 기준으로 분류해서 데이터 프레임 식으로 넣어 ...서 예측

#     text = text.split(',')

#     # 판별요청 & 결과 반환
#     # result = 'en' # langModel.predict([freq])
#     langDict = {'Date':text[0], 'IUCR':text[1], 'District': text[2], 'Ward':text[3], 'Community Area':text[4], 'ATTEMPT':text[5], 'RECOVERY':text[6], 'Location':text[7]}
    
    # return langDict

# 기능 구현 ------------------------------------------------

MODEL_PATH = 'C:\Git\KDT\BigData\Project\DL\models\Arrest_train_wbs.pth'

if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    print(f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}")
model = load_model(MODEL_PATH)

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
time = form.getvalue("time", default=0)
iucr = form.getvalue("iucr", default=0)
district = form.getvalue("district", default=0)
ward = form.getvalue("ward", default=0)
community = form.getvalue("community", default=0)
attempt = form.getvalue("attempt", default=0)
recovery = form.getvalue("recovery", default=0)
location = form.getvalue("location", default=0)

data = [time, iucr, district, ward, community, attempt, recovery, location]
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 판별하기
predicted_classes = predict(model, data)



if int(predicted_classes) == 0:
    result = "체포 실패"
else:
    result = "체포"


# (4) 사용자에게 WEB 화면 제공
showHTML(result)

# python -m http.server

"""
from sklearn.metrics import classification_report
# import torch

data = [10.0,0,4.0,10.0,49.0,0,0,9]
data = [15,17.0,0,2.0,3.0,38.0,0,0,3]
def preprocessing(text):
    datadict = {'Date':text[0], 'IUCR':text[1], 'District': text[2], 'Ward':text[3], 'Community Area':text[4], 'ATTEMPT':text[5], 'RECOVERY':text[6], 'Location':text[7]}
    return datadict



data=preprocessing(data)
dataDF=pd.DataFrame([data])
print(dataDF)


model.eval()



input_data = torch.FloatTensor(dataDF.values).to(DEVICE)  # 입력 데이터와 장치 설정
# torch.FloatTensor(self.featureDF.iloc[index].values.astype(float)).to(DEVICE)
# 예측하기 (그래디언트 계산 비활성화)
with torch.no_grad():
    predictions = model(input_data)

# 필요하면 예측 결과를 후처리 (예: 분류에서는 argmax)
predicted_classes = torch.argmax(predictions, dim=1)

# model.predict(dataDF)
predicted_classes[0]
"""