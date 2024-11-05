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
from torchvision.models import ResNet18_Weights

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

def load_model(model_path):
    model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 6)  # 6개의 클래스
    # model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu'), weights_only=True))

    model.eval()
    return model

def detectRANK(image_field, model):
    if image_field is None or image_field.filename == "":
        return "이미지가 업로드되지 않았습니다."

    image_data = image_field.file.read()
    image = Image.open(io.BytesIO(image_data)).convert('RGB')

    data_transform = transforms.Compose([
        transforms.Resize(180,180),
        # transforms.CenterCrop(224),
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
model = load_model(pklfile)

# 사용자 입력 데이터 처리
form = cgi.FieldStorage()
image_field = form.getfirst("image", None)

try:
    if image_field is not None and hasattr(image_field, 'file'):
        result = detectRANK(image_field, model)
        msg = f"예측 결과: {result}"
    else:
        # result = detectRANK(image_field, model)
        msg = f"이미지가 업로드되지 않았습니다."   # {image_field}
except Exception as e:
    msg = f"에러 발생: {str(e)}"

# 사용자에게 웹 화면 제공
showHTML("", msg)
