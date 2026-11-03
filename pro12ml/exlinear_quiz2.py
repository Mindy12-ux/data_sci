# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
#             Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오
# 조건 : NaN이 있는 경우 삭제!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 데이터 가져오기
data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/Consumo_cerveja.csv', decimal=',', thousands='.')
print(data.head(5), data.shape) # (941, 7)
data = data.dropna()
print(data.shape)   # (365, 7)
print(data.info())

df = pd.DataFrame(data[['Temperatura Media (C)', 'Precipitacao (mm)', 'Consumo de cerveja (litros)']])
print(df.head(2))

# ----------------------------------------------
# Train / Test 분리
train_set, test_set = train_test_split(df, test_size=0.3, random_state=12)
print(train_set.head(5))
print(test_set.head(5))

# 모델 만들 때 'X=[평균기온, 강수량]'으로 넣어줘도 됨. 
# 1) 평균 기온-맥주 소비량
# 독립변수 : train_set.iloc[:, [0]], 종속변수 : train_set.iloc[:, [2]]
model1 = LinearRegression().fit(X=train_set.iloc[:,[0]], y=train_set.iloc[:,[2]])
print('slope : ', model1.coef_)        # 821.8455     
print('bias : ', model1.intercept_)    # 7934.0351

pred1 = model1.predict(test_set.iloc[:, [0]])
print('예측값 : ', np.round(pred1[:5].flatten(), 1))
print('실제값 : ', test_set.iloc[:, [2]][:5].values.flatten())
# 예측값 :  [25718.8 24979.1 24272.3 21165.7 25209.2]
# 실제값 :  [24213. 26021. 21406. 20681. 24867.]

print(f'r2_score(결정계수) : {r2_score(test_set.iloc[:,[2]], pred1)}')  # 0.3329

# 시각화
plt.scatter(train_set.iloc[:,0], train_set.iloc[:, 2], color='red')
plt.plot(np.array(test_set.iloc[:, [0]]), model1.predict(test_set.iloc[:, [0]]))
plt.show()

# 2) 강수량-맥주 소비량
# 독립변수 : train_set.iloc[:, [1]], 종속변수 : train_set.iloc[:, [2]]
model2 = LinearRegression().fit(X=train_set.iloc[:,[1]], y=train_set.iloc[:,[2]])
print('slope : ', model2.coef_)        # -76.0812     
print('bias : ', model2.intercept_)    # 25620.751

pred2 = model2.predict(test_set.iloc[:, [1]])
print('예측값 : ', np.round(pred2[:5].flatten(), 1))
print('실제값 : ', test_set.iloc[:, [2]][:5].values.flatten())
# 예측값 :  [25057.7 25620.8 24160.  25590.3 25620.8]
# 실제값 :  [24213. 26021. 21406. 20681. 24867.]

print(f'r2_score(결정계수) : {r2_score(test_set.iloc[:,[2]], pred2)}')  # 0.00297

# 시각화
plt.scatter(train_set.iloc[:,1], train_set.iloc[:, 2], color='red')
plt.plot(np.array(test_set.iloc[:, [1]]), model2.predict(test_set.iloc[:, [1]]))
plt.show()