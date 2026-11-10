# Random forest는 분류, 회귀 모두 가능, sklearn 모듈은 대개 그러힘
# 캘리포니아 주택 가격 데이터로 회귀 분석

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
# print(housing.DESCR)

pd.set_option('display.max_columns', None)
df = housing.frame
print(df.head(3))
print(df.info())

x = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

rfmodel = RandomForestRegressor(n_estimators=200, random_state=42)
rfmodel.fit(x_train, y_train)

# 예측 및 평가
y_pred = rfmodel.predict(x_test)
print(f'MSE : {mean_squared_error(y_test, y_pred):.3f}')   # MSE : 0.254
print(f'r2(설명력) : {r2_score(y_test, y_pred):.3f}')       # r2(설명력) : 0.807

# 변수 중요도 시각화
impo = rfmodel.feature_importances_
indices = np.argsort(impo)[::-1]
plt.figure(figsize=(8, 5))
plt.bar(range(x.shape[1]), impo[indices], align='center')
plt.xticks(range(x.shape[1]), x.columns[indices], rotation=45)
plt.xlabel('feature name')
plt.ylabel('feature importance')
plt.tight_layout()
plt.show()

ranking = pd.DataFrame({
    'feature':x.columns[indices], 'importance':impo[indices]
})
print(ranking)