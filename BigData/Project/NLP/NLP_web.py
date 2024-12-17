import os
import re
import pandas as pd
from torch import nn
from konlpy.tag import Okt
from collections import Counter
from torch import optim
import torch
from konlpy.tag import Okt


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

# json -> 리스트 -> "단어" : idx 형식의 딕셔너리로 변환
import json
with open('vocab_kdy.json', 'r') as f:
    vocab_team1 = json.load(f)

vocab_dict = {}
for idx, word in enumerate(vocab_team1):
    vocab_dict[word] = idx
# print(vocab_dict)


n_vocab = len(vocab_dict)
hidden_dim = 64
embedding_dim = 128
n_layers = 2
classifier = SentenceClassifier(
    n_vocab= n_vocab, hidden_dim=hidden_dim, embedding_dim=embedding_dim, n_layers=n_layers
)

criterion = nn.BCEWithLogitsLoss()
optimizer = optim.RMSprop(classifier.parameters(), lr=0.001)

# 저장 경로
model = classifier
SAVE_PATH = r'C:\Git\KDT\BigData\Project\NLP\models/'
SAVE_FILE = 'NLP_model_train_wbs.pth'

# 경로상 폴더 존재 여부 체크
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# 모델 저장
torch.save(model, os.path.join(SAVE_PATH, SAVE_FILE))  # state_dict 저장

# 모델 저장
torch.save(model, os.path.join(SAVE_PATH, SAVE_FILE))  # state_dict 저장

model.eval()  # 모델 평가 모드로 전환
model



# Okt 객체 생성
tokenizer = Okt()

# 예측 함수
def predict(text, tokenizer=tokenizer):
    model = classifier
    model.eval()
    
    # 1. 입력 텍스트를 토큰화 (Okt 사용)
    tokens = tokenizer.morphs(text)  # 또는 tokenizer.tokens(text)
    print(tokens)
    # 2. 토큰을 ID로 변환 (예: token_to_id)
    input_ids = [vocab_dict.get(token, vocab_dict["<unk>"]) for token in tokens]
    
    # 3. 입력 길이에 맞게 패딩
    max_length = 32  # 원하는 최대 길이
    pad_id = vocab_dict["<pad>"]
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

    

    # 7. 예측 결과 출력
    print(f"Predicted label: {prediction.item()}")



# 예측 수행
predicted_class = predict("눈 아파 집 가고싶어 눈 따가워")
print(f'Predicted class: {predicted_class}')