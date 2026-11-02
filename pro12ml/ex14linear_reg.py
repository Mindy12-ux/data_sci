# 과적합(Overfitting)
# 선형회귀 모델이 훈련 데이터에 너무 과하게 학습되어, 데이터에 포함된 노이즈나 지엽적인 특성까지 암기해버리는 현상
# 특징 : 훈련 데이터에 대한 예측 오차는 매우 낮지만, 처음 보는 테스트 데이터나 새로운 데이터가 들어왔을 때는 예측 성능이 크게 떨어진다.

# Linear Regreesion에서 과적합을 해결하는 방법
# 특성(feature) 줄이기, 정규화 적용, 더 많은 데이터 수집하기 등등

# 이 중에서 정규화 적용하기 실습 ---- 
# 회귀계수(파라미터) 값이 너무 커지지 않도록 비용 함수에 패널티를 부과(규제)
# Ridge (L2 규제) : 가중치들의 제곱합을 최소화하여 계수들을 0에 가깝게 작게 만든다.
# Lasso (L1 규제) : 가중치들의 절대값 합을 최소화하며, 중요하지 않은 특성의 계수를 아예 0으로 만들어 제거한다.
# ElasticNet (Ridge + Lasso)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error

iris = load_iris()
# print(iris)
print(iris.keys())  # ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_names'] = iris.target_names[iris.target]
print(iris_df.head(2))
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target target_names
# 0                5.1               3.5                1.4               0.2       0       setosa
# 1                4.9               3.0                1.4               0.2       0       setosa




