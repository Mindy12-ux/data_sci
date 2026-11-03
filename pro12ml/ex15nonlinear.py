# 비선형 회귀분석(Non-linear Regression)
# 직선의 회귀선을 곡선으로 변환해 더 정확하게 데이터 변화를 예측할 수 있다.
# 선형 가정이 어긋날 때(비정규성) 대처할 수 있는 방법으로, 다항식 항을 추가하여 다항회귀 모델을 작성한다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

print(np.corrcoef(x, y)[0,1])   # 0.4807

plt.scatter(x, y)
plt.show()

# 선형회귀 모델을 적용
from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis]    # 차원 확대, sklearn을 사용할 때는 입력값을 2차원으로 줘야됨
print(x)    # [[1] [2] ... 

model = LinearRegression().fit(x, y)
y_pred = model.predict(x)
print('예측값 : ', y_pred)  # predict 값을 볼때는 values 안 씀, [2.  2.7 3.4 4.1 4.8]
print('결정계수 : ', r2_score(y, y_pred))   # 0.2311

plt.scatter(x, y)
plt.plot(x, y_pred, c='r')
plt.show()

# 비선형 모델 작성
# 여러 방법 중 가장 일반적인 방법을 사용(PolymonialFeatures, log 변환, curve_fit ... )
from sklearn.preprocessing import PolynomialFeatures        # 다항식 특징(변수)을 추가할 수 있다.
poly  = PolynomialFeatures(degree=2, include_bias=False)    # degree=열의 개수(degree 값이 커질수록 overfitting), include_bias=상수항 존재 여부
x2 = poly.fit_transform(x)
print(x)    # 5 x 1
print(x2)   # 5 x 2, 열이 2개가 됨

model2 = LinearRegression().fit(x2, y)    # 추가된 특징 행렬 값으로 모델 생성
y_pred2 = model2.predict(x2)
print('예측값 : ', y_pred2)                 # [4.14285714 1.62857143 1.25714286 3.02857143 6.94285714]
print('결정계수 : ', r2_score(y, y_pred2))  # 0.98921

plt.scatter(x, y)
plt.plot(x, y_pred2, c='r')
plt.show()





