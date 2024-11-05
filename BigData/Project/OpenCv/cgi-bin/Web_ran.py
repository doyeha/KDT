#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cgi
import cgitb
import sys
import codecs
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image

# 동작 관련 전역 변수
cgitb.enable()  # Web 상에서 진행상태 메시지를 콘솔에서 확인할 수 있도록 하는 기능

# WEB 인코딩 설정
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 모델 로드 (12.pth 사용)
model = models.resnet18()  # ResNet18 모델 초기화
model.fc = torch.nn.Linear(in_features=512, out_features=5)
model.load_state_dict(torch.load(r'C:\Git\KDT\BigData\Project\OpenCv\models\6class_final_model_train_wbs.pth', weights_only=False))  # 모델 가중치 로드
model.eval()  # 평가 모드로 설정

# 클래스 레이블 
labels = ['베어꾸','춘식','곰됴리','망곰','리트리버','와다다']

# HTML 함수
def updateHTML():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>이미지 업로드</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh; /* 화면 전체 높이 */
                margin: 0;
                font-family: Arial, sans-serif; /* 기본 글꼴 */
                text-align: center; /* 가운데 정렬 */
            }
            form {
                border: 1px solid #ccc;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
            }
            input[type="file"] {
                margin-top: 10px;
            }
            button {
                margin-top: 10px;
                padding: 10px 15px;
                background-color: #007BFF; /* 기본 버튼 색상 */
                color: white; /* 버튼 텍스트 색상 */
                border: none; /* 버튼 테두리 제거 */
                border-radius: 5px; /* 모서리 둥글게 */
                cursor: pointer; /* 커서 포인터 */
            }
            button:hover {
                background-color: #0056b3; /* 버튼 hover 색상 */
            }
        </style>
    </head>
    <body>
        <form method="post" enctype="multipart/form-data">
            <h1>이미지 업로드</h1>
            <input type="file" name="file" accept="image/*" required>
            <button type="submit">업로드</button>
        </form>
    </body>
    </html>
    """

def resultHTML(prediction):
    return f"""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>예측 결과</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh; /* 화면 전체 높이 */
                margin: 0;
                font-family: Arial, sans-serif; /* 기본 글꼴 */
                text-align: center; /* 가운데 정렬 */
            }}
            .result {{
                border: 1px solid #ccc;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
            }}
            button {{
                margin-top: 10px;
                padding: 10px 15px;
                background-color: #007BFF; /* 기본 버튼 색상 */
                color: white; /* 버튼 텍스트 색상 */
                border: none; /* 버튼 테두리 제거 */
                border-radius: 5px; /* 모서리 둥글게 */
                cursor: pointer; /* 커서 포인터 */
            }}
            button:hover {{
                background-color: #0056b3; /* 버튼 hover 색상 */
            }}
        </style>
    </head>
    <body>
        <div class="result">
            <h1>예측된 클래스</h1>
            <p>{prediction}</p>
            <form method="post" action="/cgi-bin/web.py">  <!-- 수정된 부분 -->
                <button type="submit">다시 업로드</button>
            </form>
        </div>
    </body>
    </html>
    """

# 이미지 전처리 변환 정의
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def predict(image):
    # 이미지 전처리
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)  # 배치 차원 추가

    # GPU 사용 시
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    input_batch = input_batch #.to(device)
    # model.to(device)

    with torch.no_grad():  # 기울기 계산 비활성화
        output = model(input_batch)

    # 예측 결과 얻기
    _, predicted_idx = torch.max(output, 1)
    return labels[predicted_idx.item()]

# 메인 함수
if __name__ == "__main__":
    print("Content-Type: text/html;charset=utf-8\n")  # HTML 헤더 출력
    form = cgi.FieldStorage()

    # POST 요청인지 확인
    if "file" in form and form["file"].file:  # 파일이 업로드되었을 경우
        image = Image.open(form["file"].file).convert("RGB")
        prediction = predict(image)
        print(resultHTML(prediction))
    else:  # 파일이 업로드되지 않았거나 GET 요청일 경우
        print(updateHTML())
