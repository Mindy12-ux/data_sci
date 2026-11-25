
# ============================================
# Auto MPG : OLS vs PyTorch Linear Regression vs Deep Learning
# ============================================

import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split

# 재현성 설정
torch.manual_seed(123)
np.random.seed(123)

# ============================================
# 1. 데이터 로딩 및 전처리
# ============================================

datas = pd.read_csv(
    'https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/auto-mpg.csv',
    na_values='?'
)

datas.drop('car name', axis='columns', inplace=True)
datas.dropna(inplace=True)

# 사용할 변수만 선택
datas = datas[['horsepower', 'weight', 'mpg']]

# Train / Test 분리
train_dataset = datas.sample(frac=0.7, random_state=123)
test_dataset = datas.drop(train_dataset.index)

# Label 분리
train_label = train_dataset['mpg'].copy()
test_label = test_dataset['mpg'].copy()

train_features = train_dataset.drop('mpg', axis='columns').copy()
test_features = test_dataset.drop('mpg', axis='columns').copy()

# ============================================
# 2. Train / Validation 분리
# ============================================

# 학습용 데이터에서 Validation 분리
train_indices = np.random.RandomState(123).permutation(len(train_features))

vali_size = int(len(train_indices) * 0.2)

vali_indices = train_indices[:vali_size]
actual_train_indices = train_indices[vali_size:]

x_train_raw = train_features.iloc[actual_train_indices].copy()
x_vali_raw = train_features.iloc[vali_indices].copy()

y_train = train_label.iloc[actual_train_indices].copy()
y_vali = train_label.iloc[vali_indices].copy()

# ============================================
# 3. 표준화
# ============================================

# 실제 학습 데이터 기준으로 평균과 표준편차 계산
train_mean = x_train_raw.mean()
train_std = x_train_raw.std()

x_train_scaled = (x_train_raw - train_mean) / train_std
x_vali_scaled = (x_vali_raw - train_mean) / train_std
x_test_scaled = (test_features - train_mean) / train_std

# ============================================
# 4. Tensor 변환
# ============================================

x_train = torch.tensor(
    x_train_scaled.to_numpy(), dtype=torch.float32
)
y_train_tensor = torch.tensor(
    y_train.to_numpy(), dtype=torch.float32
).view(-1, 1)

x_vali = torch.tensor(
    x_vali_scaled.to_numpy(), dtype=torch.float32
)
y_vali_tensor = torch.tensor(
    y_vali.to_numpy(), dtype=torch.float32
).view(-1, 1)

x_test = torch.tensor(
    x_test_scaled.to_numpy(), dtype=torch.float32
)
y_test = torch.tensor(
    test_label.to_numpy(), dtype=torch.float32
).view(-1, 1)

# DataLoader
train_dataset_tensor = TensorDataset(x_train, y_train_tensor)
vali_dataset_tensor = TensorDataset(x_vali, y_vali_tensor)

train_loader = DataLoader(
    train_dataset_tensor, batch_size=32, shuffle=True
)

vali_loader = DataLoader(
    vali_dataset_tensor, batch_size=32, shuffle=False
)

# ============================================
# 5. 통계학 최소제곱법 (OLS)
# ============================================

ols_model = LinearRegression()

ols_model.fit(
    x_train_scaled,
    y_train
)

ols_pred = ols_model.predict(x_test_scaled)

print('\n========== OLS 결과 ==========')
print('회귀계수:', ols_model.coef_)
print('절편:', ols_model.intercept_)

# ============================================
# 6. PyTorch 순수 선형회귀 모델
# ============================================

class MpgLinearModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 1)

    def forward(self, inputs):
        return self.linear(inputs)


linear_model = MpgLinearModel()

# ============================================
# 7. PyTorch 딥러닝 모델 (MLP)
# ============================================

class MpgModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.hidden_layer1 = nn.Linear(2, 32)
        self.hidden_layer2 = nn.Linear(32, 16)
        self.output_layer = nn.Linear(16, 1)

        self.relu = nn.ReLU()

    def forward(self, inputs):

        net = self.hidden_layer1(inputs)
        net = self.relu(net)

        net = self.hidden_layer2(net)
        net = self.relu(net)

        outputs = self.output_layer(net)

        return outputs


dl_model = MpgModel()

# ============================================
# 8. 학습 함수 (Early Stopping)
# ============================================

criterion = nn.MSELoss()
mae_metric = nn.L1Loss()


def train_model(
    model,
    train_loader,
    vali_loader,
    epochs=5000,
    patience=20
):

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    history = {
        'loss': [],
        'vali_loss': [],
        'mae': [],
        'vali_mae': []
    }

    best_vali_loss = float('inf')
    best_model_state = None
    best_epoch = 0
    wait = 0

    for epoch in range(epochs):

        # Training
        model.train()

        train_loss_sum = 0
        train_mae_sum = 0

        for x_batch, y_batch in train_loader:

            pred = model(x_batch)

            loss = criterion(pred, y_batch)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss_sum += loss.item() * len(x_batch)

            with torch.no_grad():
                mae = mae_metric(pred, y_batch)

            train_mae_sum += mae.item() * len(x_batch)

        train_loss = train_loss_sum / len(train_loader.dataset)
        train_mae = train_mae_sum / len(train_loader.dataset)

        # Validation
        model.eval()

        vali_loss_sum = 0
        vali_mae_sum = 0

        with torch.no_grad():

            for x_batch, y_batch in vali_loader:

                pred = model(x_batch)

                loss = criterion(pred, y_batch)
                mae = mae_metric(pred, y_batch)

                vali_loss_sum += loss.item() * len(x_batch)
                vali_mae_sum += mae.item() * len(x_batch)

        vali_loss = vali_loss_sum / len(vali_loader.dataset)
        vali_mae = vali_mae_sum / len(vali_loader.dataset)

        # History
        history['loss'].append(train_loss)
        history['vali_loss'].append(vali_loss)
        history['mae'].append(train_mae)
        history['vali_mae'].append(vali_mae)

        # Early Stopping
        if vali_loss < best_vali_loss:

            best_vali_loss = vali_loss
            best_model_state = copy.deepcopy(model.state_dict())
            best_epoch = epoch + 1
            wait = 0

        else:
            wait += 1

        if (epoch + 1) % 10 == 0:
            print(
                f'Epoch [{epoch+1}/{epochs}] '
                f'Train Loss: {train_loss:.4f} '
                f'Validation Loss: {vali_loss:.4f}'
            )

        if wait >= patience:
            print(f'\nEarly Stopping! Best Epoch: {best_epoch}')
            break

    model.load_state_dict(best_model_state)

    print('Best Validation Loss:', round(best_vali_loss, 4))

    return history


# ============================================
# 9. 모델 학습
# ============================================

print('\n========== PyTorch 순수 선형회귀 학습 ==========')

linear_history = train_model(
    linear_model,
    train_loader,
    vali_loader
)

print('\n========== PyTorch 딥러닝 학습 ==========')

dl_history = train_model(
    dl_model,
    train_loader,
    vali_loader
)

# ============================================
# 10. 테스트 데이터 예측
# ============================================

linear_model.eval()
dl_model.eval()

with torch.no_grad():

    linear_pred = linear_model(x_test).numpy().ravel()
    dl_pred = dl_model(x_test).numpy().ravel()

y_true = y_test.numpy().ravel()

# ============================================
# 11. 성능 비교
# ============================================

def evaluate_model(y_true, y_pred):

    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    return [mse, mae, r2]


result_df = pd.DataFrame(
    [
        evaluate_model(y_true, ols_pred),
        evaluate_model(y_true, linear_pred),
        evaluate_model(y_true, dl_pred)
    ],
    columns=['MSE', 'MAE', 'R2'],
    index=[
        'OLS (최소제곱법)',
        'PyTorch 선형회귀',
        'PyTorch 딥러닝 MLP'
    ]
)

print('\n========== 최종 성능 비교 ==========')
print(result_df.round(4))

# ============================================
# 12. 시각화 ① Loss 비교
# ============================================

plt.figure(figsize=(12, 5))

plt.plot(
    linear_history['loss'],
    label='Linear Train Loss'
)
plt.plot(
    linear_history['vali_loss'],
    label='Linear Validation Loss'
)

plt.plot(
    dl_history['loss'],
    label='MLP Train Loss'
)
plt.plot(
    dl_history['vali_loss'],
    label='MLP Validation Loss'
)

plt.xlabel('Epoch')
plt.ylabel('MSE Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.grid()
plt.show()

# ============================================
# 13. 시각화 ② 실제값 vs 예측값
# ============================================

plt.figure(figsize=(9, 8))

plt.scatter(y_true, ols_pred, alpha=0.6, label='OLS')
plt.scatter(y_true, linear_pred, alpha=0.6, label='PyTorch Linear')
plt.scatter(y_true, dl_pred, alpha=0.6, label='PyTorch MLP')

min_val = min(
    y_true.min(),
    ols_pred.min(),
    linear_pred.min(),
    dl_pred.min()
)

max_val = max(
    y_true.max(),
    ols_pred.max(),
    linear_pred.max(),
    dl_pred.max()
)

plt.plot(
    [min_val, max_val],
    [min_val, max_val],
    'k--',
    label='Ideal Prediction'
)

plt.xlabel('Actual MPG')
plt.ylabel('Predicted MPG')
plt.title('Actual vs Predicted MPG')
plt.legend()
plt.grid()
plt.show()

# ============================================
# 14. 시각화 ③ 잔차 비교
# ============================================

ols_residual = y_true - ols_pred
linear_residual = y_true - linear_pred
dl_residual = y_true - dl_pred

plt.figure(figsize=(12, 6))

plt.scatter(
    y_true, ols_residual,
    alpha=0.6, label='OLS'
)

plt.scatter(
    y_true, linear_residual,
    alpha=0.6, label='PyTorch Linear'
)

plt.scatter(
    y_true, dl_residual,
    alpha=0.6, label='PyTorch MLP'
)

plt.axhline(y=0, color='black', linestyle='--')

plt.xlabel('Actual MPG')
plt.ylabel('Residual')
plt.title('Residual Comparison')
plt.legend()
plt.grid()
plt.show()

# ============================================
# 15. 시각화 ④ MSE / MAE / R2 비교
# ============================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, metric in zip(axes, ['MSE', 'MAE', 'R2']):

    result_df[metric].plot(
        kind='bar',
        ax=ax,
        title=metric
    )

    ax.set_ylabel(metric)
    ax.tick_params(axis='x', rotation=25)
    ax.grid(axis='y')

plt.tight_layout()
plt.show()
