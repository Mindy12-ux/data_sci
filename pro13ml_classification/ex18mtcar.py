# LogisticRegression : 정성적 분류 모델
# 선형결합을 로그오즈(logit)로 해석하고, 이를 시그모이드 함수를 통해 확률로 변환한다.
# 기본이 이항분류(다항분류도 가능) - 독립변수(feature)는 연속형, 종속변수(label, class)는 범주형 
# 참고 : LogisticRegression을 근거로 뉴럴넷의 뉴런이 사용되고 있다 --> 로지스틱 회귀를 공부하는 궁극적인 이유

#mtcar dataset 사용
import statsmodels.api as sm

mtcarsdata = sm.datasets.get_rdataset('mtcars')
print(mtcarsdata.keys())
mtcars = mtcarsdata.data
print(mtcars.head(3))
print(mtcars.info())

print()
# 연비와 마력수에 따른 변속기 분류(수동, 자동)
mtcar = mtcars.loc[:, ['mpg','hp','am']]
print(mtcar.head(3))
print(mtcar['am'].unique()) # [1(수동) 0(자동)]

# 모델 작성 방법 1 : logit 함수 사용
import numpy as np
import statsmodels.formula.api as smf

formula = 'am ~ hp + mpg'       # '범주형 ~ 연속형 + ... '
result = smf.logit(formula=formula, data=mtcar).fit()
print(result.summary())     # Logit Regression Results

pred = result.predict(mtcar[:10])
print('예측값 : ', pred.values) # [0.25004729 0.25004729 0.55803435 0.35559974 ...
print('예측값 : ', np.around(pred.values))  # np.around : 0.5를 기준으로 0,1을 출력
print('실제값 : ', mtcar['am'][:10].values)
# 예측값 :  [0. 0. 1. 0. 0. 0. 0. 1. 1. 0.]
# 실제값 :  [1  1  1  0  0  0  0  0  0  0 ]

# 혼동행렬 : 인공지능이나 머신러닝의 분류 모델이 예측한 결과가 실제 정답과 얼마나 맞고 얼마나 틀렸는지를 4가지 경우의 수로 정리한 2x2 표이다.

# 현재 모델의 분류 정확도 확인 방법 1) Confusion matrix 사용
print()
print('수치에 대한 집계표(혼동 행렬)')
conf_tab = result.pred_table()
print(conf_tab)
# [[16.  3.]
#  [ 3. 10.]]
# 선형회귀에서는 모델의 성능 평가를 설명력과 RMSE로 측정 / 로지스틱 회귀에서는 모델의 성능을 정확도(혼동행렬)로 측정.
print('분류 정확도 : ', (16 + 10) / len(mtcar)) # 0.8125, '81.25%의 정확도를 가진다'라고 해석한다.
print('분류 정확도 : ', (conf_tab[0,0] + conf_tab[1,1]) / len(mtcar))

# 현재 모델의 분류 정확도 확인 방법 2) Accuracy score(실제값, 예측값) 이용
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print('분류 정확도 : ', accuracy_score(mtcar['am'], np.around(pred2)))  # 0.8125

print('**' * 10)
# 모델 작성 방법 2: glm() <-- 일반화된 선형모델 - pred_table()을 지원하지 않음
result2 = smf.glm(formula=formula, data=mtcar, family=sm.families.Binomial()).fit() 
# logit과 달리 family 파라미터가 있다.
# Binomial() : 이항분포 / Gaussian : 정규분포
print(result2.summary())

glm_pred = result2.predict(mtcar[:10])
print('glm 예측값 : ', np.around(glm_pred.values))
print('glm 실제값 : ', mtcar['am'][:10].values)
# glm 예측값 :  [0. 0. 1. 0. 0. 0. 0. 1. 1. 0.]
# glm 실제값 :  [1  1  1  0  0  0  0  0  0  0 ]

glm_pred2 = result2.predict(mtcar)
print('glm 분류 정확도 : ', accuracy_score(mtcar['am'], np.around(glm_pred2)))  # 0.8125
# logit() : 로지스틱 회귀 전용 모델, 이진 분류, 연결 함수는 logit link
# glm() : 일반화 선형모델, 이진분류/개수 데이터 등, 연결 함수는 분포에 따라 지정

print('새로운 값으로 예측')
import pandas as pd
newdf = pd.DataFrame()
newdf['mpg'] = [10, 30, 120, 130]
newdf['hp'] = [100, 1120, 80, 130]
print(newdf)
new_pred = result2.predict(newdf)
print('new_pred : ', new_pred)
print('예측 결과 : ', np.around(new_pred.values))   # 소수점 지정 가능
print('예측 결과 : ', np.rint(new_pred.values))     # 소수점 지정 불가

# 머신러닝의 포용성(inclusion, tolerance)
# 머신러닝 모델을 평가할 때는 훈련 데이터의 100% 정확도라는 '숫자'에 집착하기보다, 
# '이 모델이 현실의 불확실성과 다양한 변수를 얼마나 유연하게 포용할 수 있는가?'를 고려해야 한다.
# 수학에서는 100%의 답을 원하지만 ML은 정확도가 95%가 될지라도 주변 값을 포용하도록 설계해야 한다.
# 예를 들어, 고양이 분류 모델인 경우, 꼬리가 없는 고양이도 분류할 수 있어야 한다.

# 모델의 일반화
# 편향 - 분산 트레이드오프(Bias-Variance Trade-off)
# 목표 : 편향과 분산의 합이 최소가 되는 지점, 즉 일반화 성능이 가장 좋은 최적의 모델 복잡도를 찾는 것.

# 좋은 모델은 포용성이 있는 일반화된 모델이다. 
