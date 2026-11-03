# 보스턴 주택 가격

# CRIM: 자치시(town)별 1인당 범죄율
# ZN: 25,000 평방피트 초과 거주지역의 토지 비율
# INDUS: 자치시별 비소매상업용지 점유 비율
# CHAS: 찰스강(Charles River) 경계 위치 여부 (더미 변수: 강변이면 1, 아니면 0)
# NOX: 산화질소 농도 (1,000만분의 1)
# RM: 주택당 평균 방 개수
# AGE: 1940년 이전에 건축된 자가소유 주택의 비율
# DIS: 5개의 보스턴 고용 센터까지의 가중 거리
# RAD: 방사형 고속도로 접근성 지수
# TAX: 10,000달러당 재산세율
# PTRATIO: 자치시별 교사 1인당 학생 비율
# B: 흑인 거주 비율을 변형한 값 (1000(Bk - 0.63)²)
# LSTAT: 저소득층 인구의 비율(%)
# 타겟(Target) 변수: MEDV (1970년대 미국 보스턴 지역 소유주가 거주하는 주택 가격의 중앙값, 단위: 1,000달러)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# pd.set_option('display.max_columns')
df = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/housing.data', header=None, sep=r'\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX','RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head(5))
print(df.corr())    # LSTAT(저소득층 인구의 비율) & MEDV(집값) : -0.737663

x = df[['LSTAT']].values
y = df[['MEDV']].values
print(x[:3])    # [[4.98] [9.14] .. 
print(y[:3])    # [[24. ] [21.6] ..

# 단항을 통한 단순선형회귀 모델
model = LinearRegression()

# 다항 특성(features, 변수)
quad = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
x_quad = quad.fit_transform(x)      # [[ 1.      4.98   24.8004] [ 1.      9.14   83.5396] .. 
x_cubic = cubic.fit_transform(x)    # [[  1.         4.98      24.8004   123.505992] [  1.         9.14      83.5396   763.551944] .. 
print(x_quad[:3])
print(x_cubic[:3])

# 단순회귀
model.fit(x, y)
x_fit = np.arange(x.min(), x.max(), 1)[:,np.newaxis]
y_lin_fit = model.predict(x_fit)    # 그래프 표시용 데이터
# print('y_lin_fit : ', y_lin_fit)
model_r2 = r2_score(y, model.predict(x))
print('model_r2 : ', model_r2)  # 단순회귀의 설명력 :  0.54414

# 다항회귀(2차)
model.fit(x_quad, y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y, model.predict(x_quad))
print('q_r2 : ', q_r2)  # 2차 다항회귀 설명력 : 0.640716


# 다항회귀(3차)
model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y, model.predict(x_cubic))
print('c_r2 : ', c_r2)

# 시각화
plt.scatter(x, y, label='초기 데이터')
plt.plot(x_fit, y_lin_fit, linestyle=':', label='linear fit(d=1), $R^2=%.2f$'%model_r2, lw=3, c='b')
plt.plot(x_fit, y_quad_fit, linestyle='-', label='quad fit(d=2), $R^2=%.2f$'%q_r2, lw=3, c='r')
plt.plot(x_fit, y_cubic_fit, linestyle='--', label='cubic fit(d=3), $R^2=%.2f$'%c_r2, lw=3, c='k')
plt.xlabel('하위계층비율')
plt.ylabel('주택가격')
plt.legend()
plt.show()


