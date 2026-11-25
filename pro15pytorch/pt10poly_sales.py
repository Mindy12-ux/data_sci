# 다항회귀 : 광고비에 따른 매출액 예측

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
import koreanize_matplotlib
import torch.nn as nn
import torch.optim as optim

np.random.seed(7)
torch.manual_seed(7)

'''
# 데이터 파일 작성 - csv
# 광고비가 증가하면 매출도 증가하지만, 어느 정도 이후에는 매출 증가 폭이 둔화되는 자료
ad_cost = np.linspace(0, 100, 80)  # 광고비 데이터
# sales = -0.06 * 광고비² + 7.5 * 광고비 + 40 + noise
sales = -0.06 * (ad_cost ** 2) + 7.5 * ad_cost + 40 + np.random.normal(0, 25, size=len(ad_cost))
df = pd.DataFrame({'광고비':ad_cost, '매출':sales})
print(df.head(3))
df.to_csv('ad_sales.csv', index=False, encoding='utf-8-sig')
'''

# 데이터 파일 읽기 - csv
df = pd.read_csv('ad_sales.csv')
print(df.head(3))
print(df.info())

# 결측치가 있다면 제거
df = df.dropna()
print(df.shape) # (80, 2)

# feature, label 분리
x = df[['광고비']].values.astype(np.float32)
y = df[['매출']].values.astype(np.float32)

# 데이터 시각화
plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.xlabel('광고비')
plt.ylabel('매출')
plt.grid()
plt.show()

# train / test split
indices = np.arange(len(x))
np.random.shuffle(indices)
x = x[indices]
y = y[indices]
train_size = int(len(x) * 0.8)
x_train = x[:train_size]
x_test = x[train_size:]
y_train = y[:train_size]
y_test = y[train_size:]
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (64, 1) (16, 1) (64, 1) (16, 1)

# Scaling
