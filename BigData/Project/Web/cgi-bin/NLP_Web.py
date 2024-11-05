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
from konlpy.tag import Okt
from collections import Counter
from nltk.corpus import stopwords
import string    
# json -> 리스트 -> "단어" : idx 형식의 딕셔너리로 변환
import json

SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()


# 커스텀 클래스 
class SentenceClassifier(nn.Module):
    def __init__(
        self,
        n_vocab,
        hidden_dim,
        embedding_dim,
        n_layers,
        dropout=0.5,
        bidirectional = True,
        model_type = 'lstm'
        ):

        super().__init__()

        self.embedding = nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=embedding_dim,
            padding_idx=0
        )

        if model_type == 'rnn':
            self.model = nn.RNN(
                input_size = embedding_dim,
                hidden_size=hidden_dim,
                num_layers= n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True
            )
        elif model_type == 'lstm':
            self.model = nn.LSTM(
                input_size = embedding_dim,
                hidden_size=hidden_dim,
                num_layers= n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True
            )

        if bidirectional:
            self.classifier = nn.Linear(hidden_dim*2, 1)
        else:
            self.classifier = nn.Linear(hidden_dim,1 )
        self.dropout = nn.Dropout(dropout)

    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        output, _ = self.model(embeddings)
        last_output = output[:,-1,:]
        last_output = self.dropout(last_output)
        logits = self.classifier(last_output)
        return logits

#html
# msg가 결과값.
def showHTML(msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="ko">
        <head>
        <meta charset="UTF-8">
        <title>Text Classification</title>
        <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 8px;
        }}
        .question-input {{
            width: 100%;
            padding: 15px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-bottom: 20px;
        }}
        .submit-btn {{
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
        }}
        .submit-btn:hover {{
            background-color: #45a049;
        }}
        .answer-section {{
            margin-top: 20px;
            padding: 20px;
            background-color: #f1f1f1;
            border-radius: 4px;
        }}
        </style>
        </head>

        <body>
        <div class="container">
        <h2>질문을 입력하세요:</h2>
        <form method="post">
            <textarea name="text" class="question-input" rows="10" cols="40">{text}</textarea>
            <br>
            <button type="submit" class="submit-btn">질문하기</button>
        </form>
        
        <div class="answer-section">
            <h3>답변:</h3>
            <p>{msg}</p>
        </div>
        </div>
        </body>
    </html>""")


# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# 2.모듈 로딩
pklfile = r'C:\Git\KDT\BigData\Project\NLP\models\NLP_model_train_wbs.pth'
model = torch.load(pklfile,weights_only=False)

# 3. vocab 가져오기
with open(r'C:\Git\KDT\BigData\Project\NLP\vocab_kdy.json', 'r') as f:
    vocab = json.load(f)  # 현재는 리스트 형식

token_to_id = {token: idx for idx, token in enumerate(vocab)}
id_to_token = {idx: token for idx, token in enumerate(vocab)}

vocab_dict = {}
for idx, word in enumerate(vocab):
    vocab_dict[word] = idx
# print(vocab_dict)

pun=list(string.punctuation)

# 클래스 및 설정
# Okt 객체 생성
tokenizer = Okt()
n_vocab = len(token_to_id)
hidden_dim = 64
embedding_dim = 128
n_layers = 2
model = classifier = SentenceClassifier(
    n_vocab= n_vocab, hidden_dim=hidden_dim, embedding_dim=embedding_dim, n_layers=n_layers
)

"""
import string
text = "아야어-여! 오요.우,유"
pun=list(string.punctuation)
# print(pun)
for p in pun:
    for t in list(text):
        # print(list(text))
        if t in pun:
            text = text.replace(t,"")
"""

# 예측 함수 
def predict(text, tokenizer=tokenizer):
    model.eval()


    pun=list(string.punctuation)

    for p in pun:
        for t in list(text):
            # print(list(text))
            if t in pun:
                text = text.replace(t,"")
    
    # 1. 입력 텍스트를 토큰화 (Okt 사용)
    tokens = tokenizer.morphs(text)  # 또는 tokenizer.tokens(text)
    print(tokens)
    # 2. 토큰을 ID로 변환 (예: token_to_id)
    input_ids = [token_to_id.get(token, token_to_id["<unk>"]) for token in tokens]
    
    # 3. 입력 길이에 맞게 패딩
    max_length = 32  # 원하는 최대 길이
    pad_id = token_to_id["<pad>"]
    input_ids = input_ids[:max_length] + [pad_id] * (max_length - len(input_ids))
    
    # 4. 입력 텐서 생성
    input_tensor = torch.tensor([input_ids])  # 배치 차원 추가
    
    
    # 5. 모델에 입력하여 예측
    with torch.no_grad():
        logits = model(input_tensor)
    
    # 6. 시그모이드 함수로 확률 계산 후 0.5를 기준으로 이진분류
    probs = torch.sigmoid(logits)
    print(probs)
    prediction = (probs > 0.5).long()

    return prediction



form = cgi.FieldStorage()

text = form.getfirst("text","  ")


if text =="  ":
    msg = "값을 입력해주세요."
else:
    if predict(text).item() == 1:
        msg = "안과를 가세요"
    else:
        msg = "안과 이외의 다른 병원을 가셔야겠군요. 다른 이진분류 웹페이지를 이용해주세요!"


showHTML(msg)