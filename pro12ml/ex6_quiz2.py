import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import koreanize_matplotlib

# ols(Ordinary Least Square) 사용

# 데이터 불러오기 / 데이터 전처리
data = pd.read_csv('data.csv')
print(data.info())
data = data.fillna(np.mean(data.지상파))

q1 = data['운동'].quantile(0.25)
q3 = data['운동'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
data = data[(data['운동'] >= lower_bound) & (data['운동'] <= upper_bound)]
print(data)

print('\n1) 독립변수 : 지상파, 종속변수 : 운동량 ------')
# 모델 생성
df1 = data[['지상파', '운동']]
df1.columns = ['x', 'y']

model1 = smf.ols(formula='y ~ x', data=df1).fit()
print(model1.summary())
print('가중치 : ', model1.params['x'])       # 1.66776
print('편향 : ', model1.params['Intercept']) # 0.6184430

print()
# 예측
new_x1 = pd.DataFrame({'x': [1.4, 0.5, 4.1]})
new_pred1 = model1.predict(new_x1)
print('예측값 : \n', new_pred1)

print('\n1) 독립변수 : 지상파, 종속변수 : 종편 ------')
# 모델 생성
df2 = data[['지상파', '종편']]
df2.columns = ['x', 'y']

model2 = smf.ols(formula='y ~ x', data=df2).fit()
print(model2.summary())
print('가중치 : ', model2.params['x'])       # 1.66776
print('편향 : ', model2.params['Intercept']) # 0.6184430

print()
# 예측
new_x2 = pd.DataFrame({'x': [1.4, 0.5, 4.1]})
new_pred2 = model2.predict(new_x2)
print('예측값 : \n', new_pred2)

# 시각화
plt.scatter(df1.x, df1.y)
plt.plot(df1.x, model1.params['x'] * df1.x + model1.params['Intercept'], c='r')
plt.title('지상파 시청 시간 - 운동량')
plt.show()

plt.scatter(df2.x, df2.y)
plt.plot(df2.x, model2.params['x'] * df2.x + model2.params['Intercept'], c='r')
plt.title('지상파 시청 시간 - 종편 시청 시간')
plt.show()