import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

# 단순 선형회귀 모델
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.metrics import r2_score

# 데이터 : feature, label은 2차원 형태로 입력
# PyTorch의 Linear 계층은 입력 shape을 보통 (데이터갯수, feature수) 형태로 받음
xdata = np.array([1,2,3,4,5], dtype='float32').reshape(-1, 1)
ydata = np.array([1.2, 2.0, 3.0, 3.5, 5.5], dtype='float32').reshape(-1,1)
print('상관계수 : ', np.corrcoef(xdata.ravel(), ydata.ravel()))     #  0.97494708

# numpy 배열을 PyTorch Tensor로 변환
# x_tensor = torch.tensor(xdata, dtype=torch.float32, requires_grad=True), requires_grad=True 생략 가능(nn.Linear() 내부에 이미 설정됨)
x_tensor = torch.tensor(xdata, dtype=torch.float32)
y_tensor = torch.tensor(ydata, dtype=torch.float32)

# 모델 정의(MLP : DeepLearning) : Neural Network의 구조 설계
# 완전연결층(fully connected Layer, FC Layer, Dense Layer)을 사용
model = nn.Sequential(
    nn.Linear(1, 5),    # feature 1개 -> 은닉 노드 5개(레이어 1개)
    nn.ReLU(),          # activation function (활성화 함수)    
    nn.Linear(5, 1)     # 은닉 노드 5개 -> 출력 1개. 출력층에 activaiton이 없으면 linear 출력
)

# 활성화 함수는 신경망의 각 층 사이에 비선형성을 도입하여, 심층 신경망이 더 복잡해지도록 함
print(model)
# Sequential(
#   (0): Linear(in_features=1, out_features=5, bias=True)
#   (1): ReLU()
#   (2): Linear(in_features=5, out_features=1, bias=True)
# )

# 손실함수와 옵티마이저 정의
criterion = nn.MSELoss()    # regression(정량적 모델) 평균 제곱 오차 이용
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 확률적 경사하강법
# lr(Learning rate) : 신경망의 학습 속도를 조절. 너무 크거나 작으면 학습이 제대로 이루어지지 않을 수 있다.

# 모델 학습 : 예측값 계산 -> 손실 계산 -> gradient 초기화-> 역전파로 gradient 계산 -> optimizer로 w, b 갱신
epochs= 100     # 전체 학습 데이터를 100번 반복학습
batch_size = 1  # 한번의 가중치 갱신에 데이터를 1개씩 처리

# aa = torch.tensor([10,20,30,40,50])
# indices = torch.randperm(len(aa))
# print(indices)      # tensor([2, 1, 3, 0, 4])
# print(aa[indices])  # tensor([30, 20, 40, 10, 50])

for epoch in range(epochs):
    # shuffle=True 효과를 주려면 매 epoch마다 데이터 인덱스를 섞어준다.
    indices = torch.randperm(len(x_tensor))     # x_data 인덱스를 무작위 순서로 섞는다.
    total_loss = 0

    # for idx in indices:     # batch_size = 1 이므로 한 개씩 꺼냄 
    #     x_batch = x_tensor[idx].unsqueeze(0)    # [...] -> [[...]]
    #     y_batch = y_tensor[idx].unsqueeze(0)
    for i in range(0, len(x_tensor), batch_size):
        # batch_size 만큼 인덱스를 슬라이싱
        batch_indices = indices[i:i+batch_size]

        x_batch = x_tensor[batch_indices]
        y_batch = y_tensor[batch_indices]

        # 첫 번째 epoch에서 배치 구성 확인하기 (batch_size 만큼 데이터가 묶여서 처리된다.)
        if epoch == 0:
            print('batch_indices : ', batch_indices)
            print('x_batch : ', x_batch)
            print('y_batch : ', y_batch)
            print('x_batch_shape : ', x_batch.shape)
            print('----------------------------------')

        pred = model(x_batch)               # 1) 예측값 계산 : 내부적으로 weight * x + bias 계산
        loss = criterion(pred, y_batch)     # 2) 손실값 계산(틀린정도)
        optimizer.zero_grad()               # 3) 이전 gradient 초기화
        loss.backward()                     # 4) 역전파
        optimizer.step()                    # 5) 파라미터 갱신(w, b)

        total_loss += loss.item()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch[{epoch + 1} / {epochs}], loss:{total_loss / len(x_tensor):.5f}')

# 모델 평가 : 평가 또는 예측 시에는 gradient 계산이 필요 없으므로 torch.no_grad() 사용
with torch.no_grad():
    pred_tensor = model(x_tensor)   # 학습된 모델에 전체 데이터를 넣어 예측
    loss_eval = criterion(pred_tensor, y_tensor)

print('loss_eval : ', loss_eval.item())

# 예측 결과 확인
# pred_tensor.detach() : pred_tensor를 자동미분그래프에서 분리
pred = pred_tensor.detach().numpy()
print('pred : ', pred.ravel())
print('real : ', ydata.ravel())

print('결정계수 : ', r2_score(ydata, pred))

# 시각화
plt.scatter(xdata, ydata, color='r', marker='o', label='실제 데이터')
plt.plot(xdata, pred, 'b--', label='예측 회귀선')
plt.xlabel('feature')
plt.ylabel('label')
plt.legend()
plt.show()

print()
# 새로운 값으로 예측(추론 단계)
new_x = np.array([1.5, 5.7, -3.0], dtype='float32').reshape(-1, 1)  # 입력 형태 맞춰주기
new_x_tensor = torch.tensor(new_x, dtype=torch.float32)

with torch.no_grad():   # 학습이 끝난 상태이므로 역전파 X
    new_pred_tensor = model(new_x_tensor)

new_pred = new_pred_tensor.numpy()
print('새값 예측 결과 : ', new_pred.ravel())
