# cols = ["motor", "screw", "pgain", "vgain", "class"]  # 모터 위치, 스크류 위치, P게인(비례 이득), V게인(속도 이득), 응답 시간(타깃)

#  - 타깃/피처 (숫자만 사용: pgain, vgain)
#    x = df[["pgain", "vgain"]].astype(float)   
#    y = df["class"].values
#  - 학습/테스트 분할 ( 8:2 )
#  - 스케일링 (StandardScaler)
#  - 다항 특성 (degree=2) + LinearRegression 또는 Ridge 학습
#  - 성능 평가 
#  - 시각화

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split

# 데이터셋 로드
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/servo/servo.data', header=None)
data.columns = ["motor", "screw", "pgain", "vgain", "class"] 
print(data.head(3))
print(data.info())

# Train/Test 분리
train_set, test_set = train_test_split(data, test_size=0.2)

x = train_set[["pgain", "vgain"]].astype(float)   
y = train_set["class"].values

x_test = test_set[["pgain", "vgain"]].astype(float)   
y_test = test_set["class"].values
# print(len(x_test)) # 34

# StandardScaler 객체 생성
scaler = StandardScaler()

# 독립변수 표준화
x_scaled = scaler.fit_transform(x)
x_test_scaled = scaler.transform(x_test)

# 2차 다항회귀
poly = PolynomialFeatures(degree=2)
x_quad = poly.fit_transform(x_scaled)
x_test_quad = poly.transform(x_test_scaled)

model = LinearRegression().fit(x_quad, y)

# 예측
ypred = model.predict(x_test_quad)
print('예측값 : ', np.round(ypred[:5], 2))
print('실제값 : ', np.round(y_test[:5], 2))
print('r2_score : ', r2_score(y_test, ypred))

# 시각화 / x가 범주형이므로 scatter로 나타내줌.
plt.scatter(x["pgain"], y, label="Train Actual")

plt.scatter(
    x_test["pgain"],
    ypred,
    color="red",
    label="Test Prediction"
)

plt.xlabel("pgain")
plt.ylabel("class")
plt.title("pgain vs class")
plt.legend()
plt.show()

# 시각화 (2) : x의 범위를 촘촘하게 만들어서 y를 plot으로 만들수도 있음.
pgain_range = np.linspace(
    x["pgain"].min(),
    x["pgain"].max(),
    100
)

# vgain은 평균값으로 고정
vgain_fixed = x["vgain"].mean()

# 그래프용 데이터 생성
x_plot = np.column_stack((
    pgain_range,
    np.full(100, vgain_fixed)
))

# 기존 scaler와 poly를 이용해 변환
x_plot_scaled = scaler.transform(x_plot)
x_plot_quad = poly.transform(x_plot_scaled)

# 그래프용 예측값 생성
y_plot_pred = model.predict(x_plot_quad)

# 그래프 출력
plt.scatter(x["pgain"], y, label="Actual")
plt.plot(pgain_range, y_plot_pred, color="red", label="Prediction")

plt.xlabel("pgain")
plt.ylabel("class")
plt.title("pgain vs class")
plt.legend()
plt.show()