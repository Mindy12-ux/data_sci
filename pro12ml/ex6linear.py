print('모델 작성 방법 3 : linregress 사용 - 모델 생성')

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# IQ에 따른 시험 점수 예측
score_iq = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/score_iq.csv')
print(score_iq.head(5))
print(score_iq.info())

x = score_iq.iq
y = score_iq.score
print(x[:3])
print(y[:3])

print('상관 계수 : ', np.corrcoef(x, y)[0,1])
print(score_iq[['iq','score']].corr())  # 0.88222

# plt.scatter(x, y)
# plt.show()

print()
# 단순선형회귀분석 모델 생성 - 인과관계가 있다는 가정 하에 진행
model = stats.linregress(x, y)
print(model)
# LinregressResult(slope=0.6514309, intercept=-2.856447, rvalue=0.8822203 
# pvalue=2.84768952e-50, stderr=0.02857793, intercept_stderr=3.546211
# 단순선형회귀분석만 가능 (다중회귀 X), 예측함수 predict을 제공하지 않음

print('가중치 : ', model.slope)     # 0.6514309
print('편향 : ', model.intercept)   # -2.8564471
print('p값 : ', model.pvalue)       # 2.84768952e-50 < 0.05 이므로 두 변수 사이에는 인과관계가 존재한다.

plt.scatter(x, y)
plt.plot(x, model.slope * x + model.intercept, c='r')
plt.show()

# predict은 지원하지 않으므로, 값을 예측하려면 아래의 방법을 사용해야 함.
newdf = pd.DataFrame({'iq':[55, 66, 77, 88, 150]})
print('점수 예측 : \n', np.polyval([model.slope, model.intercept], newdf).ravel().round())


