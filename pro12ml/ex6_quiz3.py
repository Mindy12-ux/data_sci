import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats
import pandas as pd

# linregress 사용

# 데이터 불러오기 / NaN 처리
data = pd.read_csv('data.csv')
print(data.info())
data = data.fillna(np.mean(data.지상파))
print(data)

# 모델 생성
df = data[['지상파', '운동']]
x = df.지상파
y = df.운동
# print(x)
# print(y)

model = stats.linregress(x, y)
print('가중치 : ', model.slope)     # 1.66776
print('편향 : ', model.intercept)   # 0.618443
print('p값 : ', model.pvalue)       # 0.2888491