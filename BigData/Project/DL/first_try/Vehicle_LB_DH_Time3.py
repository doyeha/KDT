import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
from torchmetrics.classification import F1Score, BinaryF1Score, BinaryConfusionMatrix
import torch.optim.lr_scheduler as lr_scheduler

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder  # 라벨 인코더
from sklearn.preprocessing import OneHotEncoder


TrainDF = pd.read_csv('TrainDF.csv')
TestDF = pd.read_csv('TestDF.csv')


# 짜투리 전처리 location drop

# 데이터 날짜 -> 시간으로 변경
TrainDF['Date'] = TrainDF['Date'].str[-11:]
TrainDF['Time'] = pd.to_datetime(TrainDF['Date'], format='%I:%M:%S %p').dt.strftime('%H:%M:%S')
TrainDF.drop(['Unnamed: 0','Date','Location'], inplace=True, axis=1)
TrainDF['Time'] = pd.to_datetime(TrainDF['Time'], format='%H:%M:%S')
TestDF['Date'] = TestDF['Date'].str[-11:]
TestDF['Time'] = pd.to_datetime(TestDF['Date'], format='%I:%M:%S %p').dt.strftime('%H:%M:%S')
TestDF.drop(['Unnamed: 0','Date','Location'], inplace=True, axis=1)
TestDF['Time'] = pd.to_datetime(TrainDF['Time'], format='%H:%M:%S')

# 시간 텐서화 목적으로 다 나눠버리기 ...~$ㄻㄴㄹㄴㅇ ㅠㅠㅠㅠㅠㅠㅠ
TrainDF['hour'] = TrainDF['Time'].dt.hour
TrainDF['minute'] = TrainDF['Time'].dt.minute
TrainDF['second'] = TrainDF['Time'].dt.second
TrainDF.drop(['Time'], inplace=True, axis=1)

TestDF['hour'] = TestDF['Time'].dt.hour
TestDF['minute'] = TestDF['Time'].dt.minute
TestDF['second'] = TestDF['Time'].dt.second
TestDF.drop(['Time'], inplace=True, axis=1)

# IUCR는 라벨 인코더로, Location Description는 원핫 인코더로.
# IUCR
Labelencoder = LabelEncoder()
TrainDF['IUCR'] = Labelencoder.fit_transform(TrainDF['IUCR'])
TestDF['IUCR'] = Labelencoder.fit_transform(TestDF['IUCR'])

# 
# OHencoder = OneHotEncoder(sparse=False)
OHtemp = pd.get_dummies(TrainDF['Location Description'])
TrainDF.drop(['Location Description'], axis=1, inplace=True)
TrainDF = pd.concat([TrainDF, OHtemp], axis=1)

OHtemp = pd.get_dummies(TestDF['Location Description'])
TestDF.drop(['Location Description'], axis=1, inplace=True)
TestDF = pd.concat([TestDF, OHtemp], axis=1)

# TrainDF['Location Description'] = OHencoder.fit_transform(TrainDF['Location Description'])
# TestDF['Location Description'] = OHencoder.fit_transform(TestDF['Location Description'])

# # 자체 Train_test_split
X_train = TrainDF.iloc[:, TrainDF.columns != TrainDF.columns[1]]
y_train = TrainDF[['Arrest']]

X_test = TestDF.iloc[:, TestDF.columns != TestDF.columns[1]]
y_test = TestDF[['Arrest']]


# print(X_train[['hour']].info())
# print(X_test.info())

####와 드디어 스플릿 했으니까?
### 이제 해야할 일. 퍼셉트론 신경만ㅇ 만들고 .... 러닝 ... 그게 쉬우면 진즉 했겟자 호ㅓ허ㅗ허허허흫헣

class BinClaModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(33,50)
        self.hid_layer1 = nn.Linear(50,80)
        self.hid_layer2 = nn.Linear(80,100)
        self.hid_layer3 = nn.Linear(100,50)
        self.out_layer = nn.Linear(50,1)

    def forward(self,x):
        y = self.in_layer(x)
        y = F.relu(y)

        y = self.hid_layer1(y)
        y = F.relu(y)
        y = self.hid_layer2(y)
        y = F.relu(y)
        y = self.hid_layer3(y)
        y = F.relu(y)

        return F.sigmoid(self.out_layer(y)) # 체포 여부 이진분류니까!


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
    

VehDS = BinDataset(X_train, y_train)
VehDL = DataLoader(VehDS)
# print(VehDL)
for feature, label in VehDL:
    print(feature.shape, label.shape, feature, label)
    break


EPOCH = 50
BATCH_SIZE = 10
BATCH_CNT = X_train.shape[0]//BATCH_SIZE # 선택사항 - 코드에 넣을 수도 있음
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
LR = 0.001

model = BinClaModel()

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, random_state=1)

trainDS = BinDataset(X_train, y_train)
valDS = BinDataset(X_val, y_val)
testDS = BinDataset(X_test, y_test)
trainDL = DataLoader(trainDS, batch_size = BATCH_SIZE)

optimizer = optim.Adam(model.parameters(), lr=LR)
scheduler = lr_scheduler.ReduceLROnPlateau(optimizer, mode = 'max', patience =5, verbose = True)
reqLoss = nn.BCELoss()

from sklearn.ensemble import RandomForestClassifier
import pandas as pd


# 모델 훈련
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 피쳐 중요도 추출
importances = model.feature_importances_

# 데이터프레임으로 변환
feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# print(feature_importance_df)
# type(feature_importance_df)
print(feature_importance_df)

plt.barh(feature_importance_df.loc[:,'Feature'], feature_importance_df.loc[:,'Importance'])
plt.title("IUCR(4) LB // Location(24) OH // Time(H,M,S), col = 33")
plt.show()


"""
## 학습의 효과 확인 - 손실값과 성능평가값 저장 필요
LOSS_HISTORY, SCORE_HISTORY = [[],[]], [[],[]]
CNT = len(trainDL)
print(f'CNT =>{CNT}')

for epoch in range(EPOCH):
    # 학습 모드로 모델 성정
    model.train()

    # 배치크기만큼 데이터 로딩해서 학습 진행
    loss_total, score_total = 0,0
    for featureTS, targetTS in trainDL :
        # 학습 진행
        pre_y = model(featureTS)

        # 손실계산
        loss = reqLoss(pre_y, targetTS)
        loss_total += loss.item()

        # 성능평가 계산
        score = BinaryF1Score()(pre_y, targetTS)
        # 방법2 : score = F1Score(task='binary')(pre_y, targetTS)
        score_total += score.item()

        # 최적화 진행
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    # 에포크 당 검증기능
    # 모델 검증 모드 설정
    model.eval()

    with torch.no_grad():
        # 검증용 데이터셋 생성
        val_feaure_TS = torch.FloatTensor(valDS.featureDF.values.astype(float))
        val_target_TS = torch.FloatTensor(valDS.targetDF.values.astype(float))
        # 평가
        pre_val = model(val_feaure_TS)
        # 손실 계산
        loss_val = reqLoss(pre_val, val_target_TS)
        # 성능 평가
        score_val = BinaryF1Score()(pre_val, val_target_TS)

        scheduler.step(score_val)   # 최댓값 해야함 scheduler에 모드 max 추가.
    
        print(f'scheduler.num_bad_epochs {scheduler.num_bad_epochs}', end=" ")
        print(f'scheduler.patience {scheduler.patience}')
        # 손실 감소 (또는 성능 개선)이 안되는 경우 조기종료
        if scheduler.num_bad_epochs >= scheduler.patience:
            print(f'{scheduler.patience}EPOCH 성능 개선이 없어 조기종료함')
            break

    # 에포크 당 손실과 성능평가값 저장
    LOSS_HISTORY[0].append(loss_total/CNT)
    SCORE_HISTORY[0].append(score_total/CNT)
    LOSS_HISTORY[1].append(loss_val)
    SCORE_HISTORY[1].append(score_val)

    print(f'[{epoch}/{EPOCH}]\n- Train Loss : {LOSS_HISTORY[0][-1]} Score : {SCORE_HISTORY[0][-1]}')
    print(f'- Val Loss : {LOSS_HISTORY[1][-1]} Score : {SCORE_HISTORY[1][-1]}')



"""