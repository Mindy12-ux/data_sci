# 와인의 등급, 맛, 산도 등의 정보로 레드와인/화이트와인 분류 - 조기종료, 모델 저장

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split

np.random.seed(42)
torch.manual_seed(42)

# 데이터 읽기
wdf = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/wine.csv', header=None)
print(wdf.head(2))
print(wdf.info())   # 마지막 열이 label(class)
print(wdf.iloc[:, 12].unique())     # [1 0]
print(len(wdf[wdf.iloc[:, 12] == 0]))   # 4898, 값이 True인 행의 개수를 세는 것.
print(len(wdf[wdf.iloc[:, 12] == 1]))   # 1599
# print(wdf.iloc[:, 12] == 0)             # 0       False 
                                        # 1       False, True, False 값이 나옴

# feature / label 분리
dataset = wdf.values
# print(dataset)
x = dataset[:, 0:12].astype(np.float32)
y = dataset[:, -1].astype(np.float32)
print(x[:2])
print(y[:2])

# train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, shuffle=True, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)     # (4547, 12) (1950, 12) (4547,) (1950,)

# 스케일링 (표준화)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train).astype(np.float32)
x_test_scaled = scaler.fit_transform(x_test).astype(np.float32)

# split train data into train/validation datasets
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, stratify=y_train, random_state=12)
print('train  :', x_train_scaled.shape, y_train.shape)
print('val : ', x_val.shape, y_val.shape)
print('test :', x_test_scaled.shape, y_test.shape)

