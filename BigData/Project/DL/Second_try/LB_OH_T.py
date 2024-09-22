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

from ProBinModel import *


DataDF = pd.read_csv('Data.csv', index_col=0)

### 전처리 ------------------------------------------------------------------------------------------------
# VIN drop
DataDF.drop('VIN', inplace=True, axis=1)

# 컬럼 이름 간략하게 + Location 1000 이하 삭제 // Street도 세분화해서 Location 총 9개로 축약
DataDF['Location'] = DataDF['Location Description']
DataDF.drop('Location Description', inplace=True, axis=1)
go_location = ['Commercial_Roads','Residential_Roads','Public_Spaces','PARKINGZONE','HOUSE','Alcohol','STORE','CAR','AIRPORT']
VehicleDF = DataDF[DataDF['Location'].isin(go_location)]




# 인코딩 ---------------------------------------------------------------------------------------------------
Labelencoder = LabelEncoder()

# IUCR : 4개 라벨
# Location : 9개 원핫
VehicleDF['IUCR'] = Labelencoder.fit_transform(VehicleDF['IUCR'])
OHtemp = pd.get_dummies(VehicleDF['Location'])
VehicleDF.drop(['Location'], axis=1, inplace=True)
VehicleDF = pd.concat([VehicleDF, OHtemp], axis=1)



print(VehicleDF)
VehicleDF.to_csv('확인용.csv')
# 트레인 / 테스트 Arrest 비율 맞추기 용----------------------------------------------------------------------
# 체포 확률 20프로 데이터셋으로 ... 맞추기 
TTtestDF = VehicleDF  # 기존 데이터 안 건들이기 목적 복사

TrainFalseDF = VehicleDF[VehicleDF['Arrest'] == False].sample(n=100000, random_state=42) # sample(n=데이터양)
TrainTrueDF = VehicleDF[VehicleDF['Arrest'] == True].sample(n=25000, random_state=42)
TrainDF = pd.concat([TrainFalseDF, TrainTrueDF], axis=1)

# 이미 트레인에 들어간 것 제외하고 테스트 데이터 구성
TTtestDF.drop(TrainFalseDF.index, inplace=True)
TTtestDF.drop(TrainTrueDF.index, inplace=True)

TestFalseDF = TTtestDF[TTtestDF['Arrest'] == False].sample(n=8000, random_state=42)
TestTrueDF = TTtestDF[TTtestDF['Arrest'] == True].sample(n=2094, random_state=42)
TestDF = pd.concat([TestFalseDF, TestTrueDF], axis=1)





## 피쳐 타겟 스플릿----
X_train = TrainDF.loc[:, TrainDF.columns != 'Arrest']
y_train = TrainDF[['Arrest']]

X_test = TestDF.iloc[:, TestDF.columns != 'Arrest']
y_test = TestDF[['Arrest']]

# 확인용
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# print(X_train.columns, X_test.columns)
# print(VehicleDF)

#### 본격 딥러닝...---------------------------------------------------------------------------------------
VehicleDS = BinDataset(X_train, y_train)
VehicleDL = DataLoader(VehicleDS)
# print(VehDL)
for feature, label in VehicleDL:
    print('\n\nfeature.shape, label.shape, feature, label')
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



### 피쳐 중요도 ------------------------------------------------------------------------------------------
# from sklearn.ensemble import RandomForestClassifier
# import pandas as pd


# # 모델 훈련
# RFCmodel = RandomForestClassifier()
# RFCmodel.fit(X_train, y_train)

# # 피쳐 중요도 추출
# importances = RFCmodel.feature_importances_

# # 데이터프레임으로 변환
# feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': importances})
# feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# # print(feature_importance_df)
# # type(feature_importance_df)
# print(feature_importance_df)

# plt.barh(feature_importance_df.loc[:,'Feature'], feature_importance_df.loc[:,'Importance'])
# plt.title("IUCR(4) LB // Location(9) OH // Time(H), col = 17")
# plt.show()



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


