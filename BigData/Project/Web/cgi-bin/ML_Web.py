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


SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()

# line31        

def showHTML(pred,Global_Sales):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style></style>
</head>
<body>
    <h1>비디오게임 배급사 찾기</h1>
    <h4>당신이 좋아하는 게임의 배급사를 찾아봅시다. 아래 칸에 정보를 입력해주세요.</h4>
    <form>
        <table>
            <tr><th>NA_Sales</th><th>EU_Sales</th><th>JP_Sales</th><th>Global_Sales</th><th>Genre</th><th>Publisher</th></tr>
        
            <tr>
                <td><textarea name="NA_Sales" placeholder="달러 기준 금액 ex)10.1"></textarea></td>
                <td><textarea name="EU_Sales" placeholder="달러 기준 금액 ex)60.1"></textarea></td>
                <td><textarea name="JP_Sales" placeholder="달러 기준 금액 ex)20"></textarea></td>
                <td><text name="Global_Sales">{Global_Sales}</text></td>
                <td>
                    
                    <select name="Genre" size="1">   <!--size는 기본적으로 뜨는 옵션 갯수, disabled은 사용 못하게 잠궈버리는 것.-->
                        <option value="0">Sports</option>
                        <option value="1">Platform</option>
                        <option value="2">Racing</option>
                        <option value="3">Role-Playing</option>
                        <option value="4" selected="True">Puzzle</option>
                        <option value="5">Misc</option>
                        <option value="6">Shooter</option>
                        <option value="7">Simulation</option>
                        <option value="8">Action</option>
                        <option value="9">Fighting</option>
                        <option value="10">Adventure</option>
                        <option value="11">Strategy</option>
                    </select>
                </td>
                <td><textarea name="Publisher" placeholder="1~110까지의 숫자"></textarea></td>
                </tr>
            </table>
        <input type="submit" value="Submit">
    </form>
    
    
    <p>예측 플랫폼 : {pred}</p>
</body>
</html>""")
    # # HTML 파일 읽기
    # with open('.\cgi-bin\ML_web.html', 'r', encoding='utf-8') as file:
    #     html_content = file.read()
    
    # # {Global_Sales} 및 {pred} 부분을 실제 값으로 대체
    # html_content = html_content.replace('{{Global_Sales}}', str(Global_Sales))
    # html_content = html_content.replace('{{pred}}', str(pred))

    # # 출력
    # print("Content-Type: text/html; charset=utf-8")
    # print(html_content)


# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = r'C:\Git\KDT\BigData\Project\Web\models\Machine_wbs.pth'
else:
    pklfile = r'C:\Git\KDT\BigData\Project\Web\models\Machine_wbs.pth'


model = load('C:\Git\KDT\BigData\Project\Web\models\ML_model.joblib')

def model_pred(data, model):
       y_pred = model.predict(data)
       proba = model.predict_proba(data)
       if y_pred[0][0] == True:
              y_pred = 'Nintendo'
       elif y_pred[0][1] == True:
              y_pred = 'PS'
       elif y_pred[0][2] == True:
              y_pred = 'Xbox'
       else:
              y_pred = 'other'
       return [y_pred, proba]


form = cgi.FieldStorage()
# "Genre"는 name 속성 값
na_sales = float(form.getfirst("NA_Sales",0))
eu_sales = float(form.getfirst("EU_Sales",0))
jp_sales = float(form.getfirst("JP_Sales",0))
publisher = int(form.getfirst("Publisher",0))
selected_genre = int(form.getfirst("Genre",0))


publisher_list = [False,False,False,False,False,  False,False,False,False,False, False,False]

publisher_list[publisher] = True


selected_genre_list = [False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False,
                  False,False,False,False,False,  False,False,False,False,False]

selected_genre_list[selected_genre-1]=True

Global_Sales = na_sales+eu_sales+jp_sales
data =[[na_sales, eu_sales,jp_sales,Global_Sales]]
data[0].extend(publisher_list)
data[0].extend(selected_genre_list)


# if na_sales ==0 and eu_sales ==0 and jp_sales==0:
#     pred = "값을 넣어주세요."
# else:
#     pred = model_pred(data, model)

if na_sales != 0 and eu_sales!=0 and jp_sales!=0:
    pred = model_pred(data, model)
    pred = pred[0]
else:
    pred = "값을 넣어주세요."
    



# 예측 수행
# predicted_class = model_pred(data, model)
# print(f'Predicted class: {predicted_class}')

showHTML(pred, Global_Sales)