import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# LinearRegression 사용

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
x1 = np.array(data.지상파).reshape(-1, 1)
y1 = np.array(data.운동)

print()
# 모델 생성
model1 = LinearRegression()
fit_model1 = model1.fit(x1, y1)
print('기울기(가중치 또는 weight, slope) : ', fit_model1.coef_)  
print('절편(편향 또는 bias) : ', fit_model1.intercept_) 

print()
# 예측
new_x1 = np.array([[1.4], [0.5], [4.1]])
new_pred1 = fit_model1.predict(new_x1)
print('예측값 : ', new_pred1)

for hour, workout in zip(new_x1.ravel(), new_pred1):
    print(f'지상파 시청 시간 : {hour:.2f}시간 -> 운동량 : {workout:.2f}')

print('\n2) 독립변수 : 지상파, 종속변수 : 종편 ------')

x2 = np.array(data.지상파).reshape(-1, 1)
y2 = np.array(data.종편)

print()
# 모델 생성
model2 = LinearRegression()
fit_model2 = model2.fit(x2, y2)
print('기울기(가중치 또는 weight, slope) : ', fit_model2.coef_) 
print('절편(편향 또는 bias) : ', fit_model2.intercept_) 

print()
# 예측
new_x2 = np.array([[1.4], [0.5], [4.1]])
new_pred2 = fit_model2.predict(new_x2)
print('예측값 : ', new_pred2)

for hour, jong in zip(new_x2.ravel(), new_pred2):
    print(f'지상파 시청 시간 : {hour:.2f}시간 -> 종편 시청 시간 : {jong:.2f}')


# 시각화
plt.scatter(x1, y1)
plt.plot(x1, fit_model1.coef_.ravel() * x1 + fit_model1.intercept_, c='r')
plt.title('지상파 시청 시간 - 운동량')
plt.show()

plt.scatter(x2, y2)
plt.plot(x2, fit_model2.coef_.ravel() * x2 + fit_model2.intercept_, c='r')
plt.title('지상파 시청 시간 - 종편 시청 시간')
plt.show()