# 다중선형회귀 모델 - tv, radio, newspaper가 sales에 얼마나 영향을 주는지 분석
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import r2_score

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split

data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/Advertising.csv')
print(data.head(2))
del data['no']      # python 명령, inplace=True(원본 개체를 직접 수정)
print(data.head(2))

# feature, label 분리
fdata = data[['tv', 'radio','newspaper']]
ldata = data.iloc[:, 3] # sales
print(fdata.head(2))
print(ldata.head(2))

# feature 정규화 - 모델 성능 향상에 효과적임
fnormaldata = minmax_scale(fdata, axis=0, copy=True)    # 0 ~ 1 범위로 정규화
print(fnormaldata[:2])

# train/test split
x_train, x_test, y_train, y_test = train_test_split(fnormaldata, ldata, shuffle=True, test_size=0.3, random_state=123)
print(x_train.shape, x_test.shape)  # (140, 3) (60, 3)

# Tensor로 변환
x_train_tensor = torch.tensor(x_train, dtype=torch.float32)
x_test_tensor = torch.tensor(x_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.to_numpy(), dtype=torch.float32)

# ------------- validation dataset을 운영 (20%를 학습 중 검증 데이터로 사용)  ----------- 
# TensorDataset : x와 y를 하나의 Dataset으로 묶음(쌍으로) -> train/validation으로 나눔
# feature(x)와 label(y)을 같은 인덱스끼리 한 쌍으로 묶어 pytorch Dataset으로 만들어 주는 것 
train_dataset = TensorDataset(x_train_tensor, y_train_tensor)

vali_size = int(len(train_dataset) * 0.2)
train_size = len(train_dataset) - vali_size

train_subset, vali_subset = random_split(
    train_dataset, [train_size, vali_size], generator=torch.Generator().manual_seed(123)
)
print(len(train_dataset), '-->', len(train_subset), len(vali_subset))  # 140 --> 112 28
# ---------------------------------------------------------------------------------------

batch_size = 32     # 미니배치 크기

# dataloader : data를 미니배치 단위로 꺼내주는 역할 
# - 전체 데이터를 모델에게 한 번에 주는 것이 아니라, 지정한 수만큼 잘라서 반복적으로 모델에게 공급
# - GPU나 CPU의 병렬 연산을 극대화할 수 있다.
train_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=True)
vali_loader = DataLoader(vali_subset, batch_size=batch_size, shuffle=False)     # vali는 셔플 잘 안함

test_dataset = TensorDataset(x_test_tensor, y_test_tensor)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# 모델 학습 함수 정의 : 모델을 학습시키고, 매 epoch마다 loss를 기록
def train_modelFunc(model, train_loader, vali_loader, criterion, optimizer, epochs=100):
    # model 학습 -> 예측값 계산 -> 손실 계산 -> gradient 초기화 -> 역전파 -> 파라미터 갱신 -> loss 계산
    history = {
        'loss':[],
        'vali_loss':[]
    }

    for epoch in range(epochs):
        model.train()   # 모델을 학습 모드로 변경함을 알림
        train_loss_sum = 0  # 각 배치의 loss를 누적

        for x_batch, y_batch in train_loader:   # DataLoader에서 데이터를 batch 단위로 가져옴
            # print(x_batch.shape)    # torch.Size([32, 3])
            pred = model(x_batch)           # 1) 예측값 계산
            loss = criterion(pred, y_batch) # 2) 손실값 계산
            optimizer.zero_grad()           # 3) 이전 gradient 초기화
            loss.backward()                 # 4) 역전파
            optimizer.step()                # 5) 파라미터 갱신(w, b 계산은 이 단계에서 이루어짐)

            train_loss_sum += loss.item()   # loss누적

        train_loss = train_loss_sum / len(train_loader)     # 1개의 epoch에서의 평균 loss
        model.eval()        # 검증 / 평가 모드로 전환 (이 단계에서 평가를 수행하진 않음)
        
        vali_loss_sum = 0   # validation 데이터에 대한 loss 누적
        with torch.no_grad():
            for x_vali, y_vali in vali_loader:
                vali_pred = model(x_vali)
                vali_loss = criterion(vali_pred, y_vali)
                vali_loss_sum += vali_loss.item()

        vali_loss = vali_loss_sum / len(vali_loader)    # 1개의 epoch에서 평균 validation loss를 계산

        history['loss'].append(train_loss)
        history['vali_loss'].append(vali_loss)

        # 학습 진행 상황
        if (epoch + 1) % 10 == 0:
            print(
                f'Epoch [{epoch + 1} / {epoch}]'
                f'train loss [{train_loss:.5f}]'
                f'validation loss [{vali_loss:.5f}]'
            )

    return history

# 평가 함수 정의 (test dataset으로 평가)
def evaluate_modelFunc(model, x_test_tensor, y_test_tensor, criterion):
    model.eval()    # 평가 모드로 전환 (이 코드는 안써도 되지만 관습적으로 적는 것을 권장)
    with torch.no_grad():
        pred = model(x_test_tensor)
        loss = criterion(pred, y_test_tensor)

    return loss.item(), pred


print('\n모델 작성 방법 1: Sequential 클래스 사용')
model = nn.Sequential(
    nn.Linear(3, 16), 
    nn.ReLU(),
    nn.Linear(16, 8),
    nn.ReLU(),
    nn.Linear(8, 1)
)
print(model)
# Sequential(
#   (0): Linear(in_features=3, out_features=16, bias=True)
#   (1): ReLU()
#   (2): Linear(in_features=16, out_features=8, bias=True)
#   (3): ReLU()
#   (4): Linear(in_features=8, out_features=1, bias=True)
# )

# 손실 함수와 옵티마이저 정의
critertion = nn.MSELoss()
# optimizer = optim.Adam(model.parameters())  # lr=0.001이 기본값
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 모델 학습
history = train_modelFunc(
    model=model, train_loader=train_loader, vali_loader=vali_loader, 
    criterion=critertion, optimizer=optimizer, epochs=100
)






