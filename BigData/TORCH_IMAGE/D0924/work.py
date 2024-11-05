import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

train = pd.read_csv(r"C:\Users\kjy19\OneDrive\Desktop\TORCH_IMAGE\data\mnist_train.csv")
test = pd.read_csv(r"C:\Users\kjy19\OneDrive\Desktop\TORCH_IMAGE\data\mnist_test.csv")

# 맨뒤의 숫자 하나가 타겟 (라벨화된 범주화 타겟이라고 생각하면 좀 나으려나?)
# print(train.shape)  # (59999, 785)  피쳐가 784개

# trainDF = train.loc[:, -1]
testDF = test.loc[:,-1]

# print(trainDF)
print(testDF)