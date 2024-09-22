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