# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

#---------------------------------------------------------------------
# 모듈 로딩
#---------------------------------------------------------------------
import os.path              # 파일 및 폴더 관련
import cgi, cgitb           # cgi 프로그래밍 관련
import joblib               # AI 모델 관련
import sys, codecs          # 인코딩 관련
from pydoc import html      # html 코드 관련 : html을 객체로 처리?
import torch
import torch.nn as nn 
import torch.nn.functional as F 
import codecs
import numpy as np
# 동작관련 전역 변수-------------------------------------------------------------------
SCRIPT_MODE = True      # Jupyter Mode : False, WEB Mode : True
cgitb.enable()          # Web상에서 진행상태 메시지를 
                        # 콘솔에서 확인할수 있도록 하는 기능
                        
# 모델 파일 명
#MODEL_FILE = 'C:\EX_PY06\TORCH_DL\WORK\model_param\model_crime_wbs.pth'
# ------------------------------------------------------------------------------------
# 사용자 정의 함수
# WEB에서 사용자에게 보여주고 입력받는 함수 
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드
# ------------------------------------------------------------------------------------

# 학습 모델 예측 
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



# 체포 확률을 예측하는 함수
def predict_arrest_probability(text, model):
    data = np.array([float(x) for x in text.split()]).reshape(1,-1)
    input_tensor = torch.FloatTensor([data])
    with torch.no_grad():
        
        prediction = model(input_tensor)
    return prediction.item()

# 모델 로드 함수
# def load_model(model_path):
#     model = CrimeBCFModel(4,12,1,[200,200,400,400,200])
#     model.load_state_dict(torch.load(model_path,weights_only=True))
#     model.eval()
#     return model

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="en">
         <head>
          <meta charset="UTF-8">
          <title>---AI언어판별---</title>
         </head>
         <body>
          <form>
            <textarea name="text" rows="10" colos="40" >{text}</textarea>
            <p><input type="submit" value="언어감지">{msg}</p>
          </form>
         </body>
        </html>""")


# 모델 경로 설정
#model = torch.load(MODEL_FILE,weights_only=True)
# if os.path.exists(MODEL_FILE):
#     model = load_model(MODEL_FILE)
# else:
#     print(f'모델 파일을 찾을 수 없습니다: {MODEL_FILE}')
# model = load_model(MODEL_FILE)

# 기능 구현 -----------------------------------------------------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# # (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = os.path.dirname(__file__)+ './Arrest_train_wbs.pth' # 웹상에서는 절대경로만
else:
    pklfile = './Arrest_train_wbs.pth'
    
model = torch.load(pklfile, weights_only=False)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# 입력된 값들 가져오기
text = form.getvalue("text", default="")

# # 사용자가 입력한 데이터를 숫자 변환
# input_data = []
# try:
#     input_data = [float(data[field]) for field in data if data[field]]
# except ValueError:
#     pass

# (3-3) 판별하기
msg =""
if text != "":
    resultLang = predict_arrest_probability(text, model)
    msg = f"{resultLang}"

# 사용자에게 웹 화면 제공
showHTML(text, msg)