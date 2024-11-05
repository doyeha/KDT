# 경민씨 코드 _ 참고 및 ML_web 이미 제작해놓은 것 바탕 재구성
# 이게 self 코드임!!!


# 모델 로드
import torch
from joblib import dump, load

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch
import numpy as np 
from pydoc import html
from PIL import Image
from torchvision import transforms
import io
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd 
from torch.utils.data import Dataset, DataLoader

SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()

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
        y = self.dropout(y) # 과적합 방지 dropout

        y = self.hid_layer1(y)
        y = F.relu(y)
        y = self.dropout(y)# 과적합 방지 dropout

        y = self.hid_layer2(y)
        y = F.relu(y)
        
        y = self.hid_layer3(y)
        y = F.relu(y)

        return torch.sigmoid(self.out_layer(y))   

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
        feaureTS = torch.FloatTensor(self.featureDF.iloc[index].values.astype(float)).to(DEVICE)
        targetTS = torch.FloatTensor(self.targetDF.iloc[index].values.astype(float)).to(DEVICE)

        
        # 피처와 타겟 반환
        return feaureTS, targetTS

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
                <label>시간
                    <select name="time">
                        <option value='1.0'>1.0</option><option value='2.0'>2.0</option><option value='3.0'>3.0</option><option value='4.0'>4.0</option><option value='5.0'>5.0</option><option value='6.0'>6.0</option>
                        <option value='7.0'>7.0</option><option value='8.0'>8.0</option><option value='9.0'>9.0</option><option value='10.0'>10.0</option><option value='11.0'>11.0</option><option value='12.0'>12.0</option>
                        <option value='13.0'>13.0</option><option value='14.0'>14.0</option><option value='15.0'>15.0</option><option value='16.0'>16.0</option><option value='17.0'>17.0</option><option value='18.0'>18.0</option>
                        <option value='19.0'>19.0</option><option value='20.0'>20.0</option><option value='21.0'>21.0</option><option value='22.0'>22.0</option><option value='23.0'>23.0</option><option value='24.0'>24.0</option>
                    </select>
                </label>
                
                <!--범죄코드-->
                <label> IUCR : 당신이 세운 차의 종류 
                    <select name= 'IUCR'>
                        <option value='0'>0</option>
                        <option value='1'>1</option>
                        <option value='2'>2</option>    
                        <option value='3'>3</option>
                    </select>
                </label>
            
                <label> District :
                    <select name ="district">
                        <option value='1.0'>1.0</option><option value='2.0'>2.0</option><option value='3.0'>3.0</option><option value='4.0'>4.0</option><option value='5.0'>5.0</option><option value='6.0'>6.0</option>
                        <option value='7.0'>7.0</option><option value='8.0'>8.0</option><option value='9.0'>9.0</option><option value='10.0'>10.0</option><option value='11.0'>11.0</option><option value='12.0'>12.0</option>
                        <option value='14.0'>14.0</option><option value='15.0'>15.0</option><option value='16.0'>16.0</option><option value='17.0'>17.0</option><option value='18.0'>18.0</option><option value='19.0'>19.0</option>
                        <option value='20.0'>20.0</option><option value='22.0'>22.0</option><option value='24.0'>24.0</option><option value='25.0'>25.0</option><option value='31.0'>31.0</option>
                    </select>
                </label>

             
                <label> Ward :
                    <select name = 'ward'>
                        <option value='1.0'>1.0.</option><option value='2.0'>2.0.</option><option value='3.0'>3.0.</option><option value='4.0'>4.0.</option><option value='5.0'>5.0.</option><option value='6.0'>6.0.</option>
                        <option value='7.0'>7.0.</option><option value='8.0'>8.0.</option><option value='9.0'>9.0.</option><option value='10.0'>10.0.</option><option value='11.0'>11.0.</option><option value='12.0'>12.0.</option>
                        <option value='13.0'>13.0.</option><option value='14.0'>14.0.</option><option value='15.0'>15.0.</option><option value='16.0'>16.0.</option><option value='17.0'>17.0.</option><option value='18.0'>18.0.</option>
                        <option value='19.0'>19.0.</option><option value='20.0'>20.0.</option><option value='21.0'>21.0.</option><option value='22.0'>22.0.</option><option value='23.0'>23.0.</option><option value='24.0'>24.0.</option>
                        <option value='25.0'>25.0.</option><option value='26.0'>26.0.</option><option value='27.0'>27.0.</option><option value='28.0'>28.0.</option><option value='29.0'>29.0.</option><option value='30.0'>30.0.</option>
                        <option value='31.0'>31.0.</option><option value='32.0'>32.0.</option><option value='33.0'>33.0.</option><option value='34.0'>34.0.</option><option value='35.0'>35.0.</option><option value='36.0'>36.0.</option>
                        <option value='37.0'>37.0.</option><option value='38.0'>38.0.</option><option value='39.0'>39.0.</option><option value='40.0'>40.0.</option><option value='41.0'>41.0.</option><option value='42.0'>42.0.</option>
                        <option value='43.0'>43.0.</option><option value='44.0'>44.0.</option><option value='45.0'>45.0.</option><option value='46.0'>46.0.</option><option value='47.0'>47.0.</option><option value='48.0'>48.0.</option>
                        <option value='49.0'>49.0.</option><option value='50.0'>50.0.</option>
                    </select>
                </label>
            
                <label> Community Area :  
                    <select name = 'community'>
                        <option value='0.'>0.</option><option value='1.'>1.</option><option value='2.'>2.</option><option value='3.'>3.</option><option value='4.'>4.</option><option value='5.'>5.</option>
                        <option value='6.'>6.</option><option value='7.'>7.</option><option value='8.'>8.</option><option value='9.'>9.</option><option value='10.'>10.</option><option value='11.'>11.</option>
                        <option value='12.'>12.</option><option value='13.'>13.</option><option value='14.'>14.</option><option value='15.'>15.</option><option value='16.'>16.</option><option value='17.'>17.</option>
                        <option value='18.'>18.</option><option value='19.'>19.</option><option value='20.'>20.</option><option value='21.'>21.</option><option value='22.'>22.</option><option value='23.'>23.</option>
                        <option value='24.'>24.</option><option value='25.'>25.</option><option value='26.'>26.</option><option value='27.'>27.</option><option value='28.'>28.</option><option value='29.'>29.</option>
                        <option value='30.'>30.</option><option value='31.'>31.</option><option value='32.'>32.</option><option value='33.'>33.</option><option value='34.'>34.</option><option value='35.'>35.</option>
                        <option value='36.'>36.</option><option value='37.'>37.</option><option value='38.'>38.</option><option value='39.'>39.</option><option value='40.'>40.</option><option value='41.'>41.</option>
                        <option value='42.'>42.</option><option value='43.'>43.</option><option value='44.'>44.</option><option value='45.'>45.</option><option value='46.'>46.</option><option value='47.'>47.</option>
                        <option value='48.'>48.</option><option value='49.'>49.</option><option value='50.'>50.</option><option value='51.'>51.</option><option value='52.'>52.</option><option value='53.'>53.</option>
                        <option value='54.'>54.</option><option value='55.'>55.</option><option value='56.'>56.</option><option value='57.'>57.</option><option value='58.'>58.</option><option value='59.'>59.</option>
                        <option value='60.'>60.</option><option value='61.'>61.</option><option value='62.'>62.</option><option value='63.'>63.</option><option value='64.'>64.</option><option value='65.'>65.</option>
                        <option value='66.'>66.</option><option value='67.'>67.</option><option value='68.'>68.</option><option value='69.'>69.</option><option value='70.'>70.</option><option value='71.'>71.</option>
                        <option value='72.'>72.</option><option value='73.'>73.</option><option value='74.'>74.</option><option value='75.'>75.</option><option value='76.'>76.</option><option value='77.'>77.</option>
                    </select>
                </label>
              
                <label> ATTEMPT :
                    <select name = "attempt">
                        <option value='0'>0</option>
                        <option value='1'>1</option>
                    </select> 
                </label> 
          
                <label> RECOVERY :
                    <select name ="recovery">
                        <option value='0'>0</option>
                        <option value='1'>1</option>
                    </select>
                </label>
          
                <label> Location : 장소
                    <select name = "location">
                        <option value='0'>0</option><option value='1'>1</option><option value='2'>2</option><option value='3'>3</option><option value='4'>4</option><option value='5'>5</option>
                        <option value='6'>6</option><option value='7'>7</option><option value='8'>8</option>
                    </select>    
                </label>
                <input type="submit" value="submit">
            </form> 
            
            <p> 결과 : {result}</p>
        </body>
    </html>""")


# DataFrame화 대기 
def preprocessing(text):
    datadict = {'Date':text[0], 'IUCR':text[1], 'District': text[2], 'Ward':text[3], 'Community Area':text[4], 'ATTEMPT':text[5], 'RECOVERY':text[6], 'Location':text[7]}
    return datadict


if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# # (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = r'C:\Git\KDT\BigData\Project\Web\models\1017_Arrest_wbs.pth' # 웹상에서는 절대경로만
else:
    pklfile = r'C:\Git\KDT\BigData\Project\Web\models\1017_Arrest_wbs.pth'
# model = torch.load(pklfile, weights_only=False)
model = torch.load(pklfile, weights_only=False, map_location=torch.device('cpu'))
# map_location=torch.device('cpu')  = Cuda 사용해서 뽑은 모델이기 때문에 맵 로케이션 지정해주어야함.


form = cgi.FieldStorage()

# 입력 데이터들 
time = float(form.getfirst("time",25))
IUCR = int(form.getfirst("IUCR",0))
district = float(form.getfirst("district",0))
ward = float(form.getfirst("ward",0))
community = float(form.getfirst("community",0))
attempt = int(form.getfirst("attempt",0))
recovery = int(form.getfirst("recovery",0))
location = int(form.getfirst("location",0))

data = [time, IUCR, district, ward, community,attempt,recovery,location]

# 입력 데이터 전처리
data=preprocessing(data)
dataDF=pd.DataFrame([data])
# model.eval()
input_data = torch.FloatTensor(dataDF.values)  # 입력 데이터와 장치 설정
with torch.no_grad():
    predictions = model(input_data)
predicted_classes = torch.argmax(predictions, dim=1)


if time == 25:
    result = "값을 입력해주세요."
elif int(predicted_classes)==0:
    result = "체포 불가능 예상"
else:
    result = "체포 가능 예상"



showHTML(result)