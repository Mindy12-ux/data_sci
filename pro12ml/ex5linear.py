# 전통적 방법의 선형회귀(기계학습 중 지도학습)
# 각 데이터에 대한 잔차제곱합이 최소가 되는 추세선(회귀선)을 만들고,
# 이를 통헤 독립변수가 종속변수에 얼마나 영향을 주는지 인과관계를 분석
# 독립변수 : 연속형, 종속변수 : 연속형 - 두 변수는 상관관계 및 인과관계가 있어야 함
# 정량적인 모델을 생성

import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(1)

x, y, _ = make_regression(n_samples=50, n_features=1, bias=50, coef=True, noise=50)
print(x)    # 2차원
print(y)    # 1차원

r = np.corrcoef(x.ravel(), y)[0,1]
print(f'상관계수 : {r:.4f}')    # 매우 강한 양의 상관관계

print('\n모델 작성 방법 1 : LinearRegression 사용 - 모델 생성')
from sklearn.linear_model import LinearRegression
model = LinearRegression()
fit_model = model.fit(x, y) # 내부에서 아래와 같은 작업을 진행
# 1) 독립변수(x)와 종속변수(y)를 입력받음.
# 2) 예측값과 실제값 사이의 오차제곱합이 최소가 되도록 계산.
# 3) 최적의 회귀계수(기울기, 절편)를 구함
# 4) 계산된 계수를 모델에 저장
# 단순선형회귀 모델에서는 y = wx + b와 같은 단순한 형태의 수식을 가진 모델이 만들어진다.
# 참고 : LinearRegression은 신경망과 다름. 가중치를 갱신하기 위해 반복학습을 하지 않는다. 단순 계산을 통해 가중치를 갱신한다.

print('기울기(가중치 또는 weight, slope) : ', fit_model.coef_)  # 79.52463976
print('절편(편향 또는 bias) : ', fit_model.intercept_)         # 60.92221225816935
# yhat = 79.52463976 * x + 60.9222122 일차방정식 완성

# 예측값 확인
y_newpred1 = fit_model.predict(x[[0]])   # 기존 데이터 0번째를 입력값으로 줌. 학습을 2차원으로 했기 때문에 예측 데이터로 2차원으로 넣어줘야 함.
print('예측값 1: ', y_newpred1)  # 41.09112298
y_newpred2 = fit_model.predict(np.array([[0.12345], [0.3], [0.5]]))
print('예측값 2: ',y_newpred2)  # [ 70.73952904  84.77960419 100.68453214]