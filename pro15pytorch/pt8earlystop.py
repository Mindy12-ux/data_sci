# 딥러닝으로 다중선형회귀 - autompg dataset
# 조기 종료 (Early Stopping) : loss에 대한 성능이 어느 순간 개선되지 않을 때 학습을 중단
# 불필요한 학습을 줄이고, Overfitting을 방지하기 위한 방법 중 하나

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import r2_score

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split

# 재현성 설정
torch.manual_seed(123)
np.random.seed(123)

# data loading
datas = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/auto-mpg.csv', na_values='?')
print(datas.head(2))
del datas['car name']
print(datas[datas.isna().any(axis=1)])
datas = datas.dropna()
print(datas.isna().sum())

# 편의상 일부 칼럼 제거
datas.drop(
    ['cylinders', 'displacement', 'acceleration', 'model year', 'origin'],
    axis='columns', inplace=True
)
print(datas.head(1))

# train / test split : 샘플링으로 처리
train_dataset = datas.sample(frac=0.7, random_state=123)
test_dataset = datas.drop(train_dataset.index)
print(train_dataset[:1], train_dataset.shape)   # (274, 3)
print(test_dataset[:1], test_dataset.shape)     # (118, 3)

# 표준화 계산 : (요소값 - 평균) / 표준편차
train_stat = train_dataset.describe()
train_stat.pop('mpg')   # mpg는 종속변수라서 뺌
print(train_stat)
train_stat = train_stat.transpose()
print(train_stat)

def stdscale_func(x):
    return (x - train_stat['mean']) / train_stat['std']

# train 데이터 표준화
st_train_data = stdscale_func(train_dataset)
st_train_data = st_train_data.drop(['mpg'], axis='columns')
print(st_train_data[:3])

# test 데이터 표준화
st_test_data = stdscale_func(test_dataset)
st_test_data = st_test_data.drop(['mpg'], axis='columns')
print(st_test_data[:3])

# label 분리
train_label = train_dataset.pop('mpg')
print(train_label[:3])
test_label = test_dataset.pop('mpg')
print(test_label[:3])

# tensor로 변환
x_data = torch.tensor(st_train_data.values, dtype=torch.float32)
y_data = torch.tensor(train_label.values, dtype=torch.float32).view(-1, 1)  # 2차원 텐서화

x_test = torch.tensor(st_test_data.values, dtype=torch.float32)
y_test = torch.tensor(test_label.values, dtype=torch.float32).view(-1, 1)  # 2차원 텐서화

dataset = TensorDataset(x_data, y_data)

# train / validation split
dataset_size = len(dataset)
vali_size = int(dataset_size * 0.2)
train_size = dataset_size - vali_size

train_subset, vali_subset = random_split(
    dataset, [train_size, vali_size], generator=torch.Generator().manual_seed(123)
)
print(len(dataset), len(train_subset), len(vali_subset))    # 274 220 54

# DataLoader 생성
batch_size = 32

train_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=True)
vali_loader = DataLoader(vali_subset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
print(len(train_loader), len(vali_loader), len(test_loader))    # 7 2 4

# 모델 정의

# 모델 학습

