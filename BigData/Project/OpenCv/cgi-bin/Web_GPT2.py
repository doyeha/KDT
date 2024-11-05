# 필요한 라이브러리 로딩
import os
import cgi
import cgitb
import joblib
import sys
import codecs
import torch
import numpy as np
from torchvision import models, transforms
from PIL import Image
import io
import torch.nn as nn

# 전역 변수 설정
SCRIPT_MODE = True
cgitb.enable()

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>AI 모델 이미지 예측</title>
      <style>
        .container {{
            margin-top: 20px;
        }}
        #preview {{
            margin-top: 20px;
            max-width: 100%;
            height: auto;
        }}
      </style>
     </head>
     <body>
      <div class="container">
        <form enctype="multipart/form-data" method="post">
          <p>이미지 업로드: <input type="file" id="imageInput" name="image" accept="image/*" /></p>
          <img id="preview" alt="이미지 미리보기">
          <p><input type="submit" value="예측"></p>
          <p>{msg}</p>
        </form>
      </div>

      <script>
        // 이미지 미리보기 기능
        document.getElementById('imageInput').addEventListener('change', function(event) {{
            const file = event.target.files[0];
            const reader = new FileReader();

            reader.onload = function(e) {{
                document.getElementById('preview').src = e.target.result;
            }};

            if (file) {{
                reader.readAsDataURL(file);
            }}
        }});
      </script>
     </body>
    </html>""")

# from torchvision.models import resnet18, ResNet18_Weights

# from torchvision.models import resnet18
# import torch.nn as nn

# def load_image(image_path):
#     image = Image.open(image_path).convert('RGB')
#     return image

# preprocess = transforms.Compose([
#     # transforms.Resize((224, 224)),  # 이미지 크기 조정 (모델에 따라 조정 필요)
#     transforms.ToTensor()          # 텐서로 변환    
#     # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # 정규화 (VGG16 모델에 맞춘 값)
# ])

# def predict(image_path, model):
#     image = load_image(image_path)   # 이미지 로드
#     image = preprocess(image)         # 전처리 적용
#     image = image.unsqueeze(0)        # 배치 차원 추가
#     image = image         # 디바이스로 이동

#     with torch.no_grad():             # 그라디언트 계산 비활성화
#         outputs = model(image)        # 모델에 이미지 입력
#         probabilities = torch.softmax(outputs, dim=1)  # 소프트맥스 적용
#         # print(probabilities)          # 각 클래스에 대한 확률 출력
#         _, predicted = torch.max(probabilities.data, 1)  # 예측 클래스

#     return probabilities, predicted.item()

# # 모델 로드

# model = torch.load(r'C:\Git\KDT\BigData\Project\OpenCv\models\6class_final_model_train_wbs.pth',weights_only=False ,map_location=torch.device('cpu'))  # 가중치 불러오기
# model.eval()  # 모델 평가 모드로 전환
# # model
# # 예측할 이미지 경로
# image_path = r'C:\Git\KDT\BigData\Project\OpenCv\Data_all\test\BearGGu (7).jpg'
# # print(r"C:\Users\Doyeon\Desktop\KDT\OpenCV\test\u76.jpg")
# # 예측 수행
# predicted_class = predict(image_path, model)
# print(f'Predicted class: {predicted_class}')  





def detectRANK(image_field, model):
    if image_field is None or image_field.filename == "":
        return "이미지가 업로드되지 않았습니다."

    image_data = image_field.file.read()
    image = Image.open(io.BytesIO(image_data)).convert('RGB')

    data_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    image_tensor = data_transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)

    class_names = ['베어꾸', '춘식', '곰됴리', '망곰', '리트리버', '와다다']
    return class_names[predicted.item()]

# 웹 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 모델 로딩
pklfile = r'C:\Git\KDT\BigData\Project\OpenCv\models\6class_final_model_train_wbs.pth'
model = torch.load(pklfile,map_location=torch.device('cpu'))
# 모델 저장
# torch.save(model.state_dict(), 'model_weights.pth')

# 모델 로드
# model.load_state_dict(torch.load('model_weights.pth')) # map_location=torch.device('cpu')

# 사용자 입력 데이터 처리
form = cgi.FieldStorage()
image_field = form.getfirst("image", None)

try:
    if image_field is not None and hasattr(image_field, 'file'):
        result = detectRANK(image_field, model)
        msg = f"예측 결과: {result}"
    else:
        result = detectRANK(image_field, model)
        msg = f"이미지가 업로드되지 않았습니다. {result}"
except Exception as e:
    msg = f"에러 발생: {str(e)}"

# 사용자에게 웹 화면 제공
showHTML("", msg)
