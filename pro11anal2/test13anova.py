# 분산분석 (ANOVA, ANalysis Of VAriance)
# 세 개 이상의 모집단에 대한 가설검정
# 분산이 발생한 과정을 분석하여 요인에 의한 분산 / 요인을 통해 나누어진 각 집단 내의 분산으로 나누고,
# 요인에 의한 분산이 의미 있는 크기를 가지는지를 검정하는 것을 의미한다.

# 세 집단 이상의 평균 비교에서 독립인 두 집단의 평균 비교를 반복하여 실시할 경우, 제 1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석을 이용하게 된다.
# 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나눠진 각 집단 내의 분산으로 나누고, 
# 요인에 의한 분산이 의미 있는 크기를 가지는지를 검정한다.

# 분산분석은 3개 이상의 그룹 간 평균에 유의미한 차이가 있는지를 분산을 이용해 통계적으로 검증하는 방법.
# f값 = 집단간분산 / 집단내분산

# 서로 독립인 세 집단의 평균 차이 검정
# 실습) 세 가지 교육 방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기 시험을 실시. three_sample.csv
# 독립변수(범주형) : 요인은 한 개(교육 방법), 다만 방법의 종류가 3가지(그룹이 3개)
# 종속변수(연속형) : 실기시험의 평균 점수

# 귀무 가설 : 세 가지 교육방법에 따른 실기시험 평균 점수에 차이가 없다.
# 대립 가설 : 세 가지 교육방법에 따른 실기시험 평균 점수에 차이가 있다.

from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols     # 추정 및 검정, 회귀, 시계열 분석 등의 기능을 제공하는 라이브러리
# ols (Ordinary Least Squares - 최소제곱법 회귀)

data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/three_sample.csv')
print(data.head(5),' ', len(data))
print(data.describe())

# 이상치(outlier) 시각화
# import matplotlib.pyplot as plt
# plt.boxplot(data.score)
# plt.show()

# 이상치 값과 개수 확인 - IQR 이용 ---------------------
q1 = data['score'].quantile(0.25)
q3 = data['score'].quantile(0.75)
iqr = q3 - q1

# 이상치 기준
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print(f'Q1:{q1}, Q3:{q3}, IQR:{iqr}')
print('이상치 하한값 : ', lower)    # 25.75
print('이상치 상한값 : ', upper)    # 111.75
outlier = data[(data['score'] < lower) | (data['score'] > upper)]
# outlier :       no  method  survey  score
#            7    8       2       1    500
#            59  60       1       0    438

print("outlier : ", outlier)
print("outlier 개수 : ", len(outlier))
# ----------------------------------------------------
data = data.query('score  <= 100')  # 시험점수이므로, 100점 이내의 값만 취한다.
print(len(data))
print(data.describe())

# 교육 방법별 만족 건수 - 교차표 이용
ctab = pd.crosstab(data['method'], data['survey'])
ctab.index = ['방법1', '방법2', '방법3']
ctab.columns = ['만족', '불만족']
print(ctab)
# -----------------------------------------------------

print('ANOVA 검정')
# F-통계값을 얻기 위해 회귀분석모델 사용 
import statsmodels.api as sm
lin_model = ols("data['score'] ~ data['method']", data=data).fit()  # 회귀분석 모델 객체 생성
result = sm.stats.anova_lm(lin_model, type=1)
print(result)
#                   df    sum_sq(제곱합)  mean_sq(제곱평균)     F(F값)    PR(>F) (pvalue)
# data['method']   1.0      27.980888     27.980888(MSR)      0.122228      0.727597
# Residual        76.0   17398.134497    228.922822(MSE)           NaN           NaN
# F 검정통계량=0.122228, p-value=0.727597
# 해석 : p-value 0.727597 > 0.05 이므로, 귀무 가설을 채택한다.
# 결론 : 세 가지 교육방법에 따른 실기시험 평균 점수에 차이가 없다.

f_value = result.loc["data['method']", 'F']
p_value = result.loc["data['method']", 'PR(>F)']
print(f_value)
print(p_value)

# 교육 방법별 평균 점수
print('\n교육 방법별 평균 점수 : \n')
print(data.groupby('method')['score'].mean())
# method
# 1    67.384615
# 2    68.357143
# 3    68.875000

# ANOVA는 각 method별 1:1 평균 비교는 일려주지 않는다. 
# 이때 사후분석을 이용하면 두 개의 그룹 간 평균 분석이 가능하다.
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tuResult = pairwise_tukeyhsd(endog=data['score'], groups=data['method'])
print(tuResult)
# Multiple Comparison of Means - Tukey HSD, FWER=0.05 
# ====================================================
# group1 group2 meandiff p-adj   lower   upper  reject
# ----------------------------------------------------
#      1      2   0.9725 0.9702 -8.9458 10.8909  False  : 유의미한 차이가 없으면 False
#      1      3   1.4904 0.9363 -8.8183  11.799  False  : 유의미한 차이가 있으면 True
#      2      3   0.5179 0.9918 -9.6125 10.6483  False
# ----------------------------------------------------

# tukeyhsd 시각화
import matplotlib.pyplot as plt
tuResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
# Tukey HSD : 원래 반복 수가 동일하다는 가정하게 고안된 방법
# 집단 간 평균 차이를 정밀하게 확인 가능
# 각 집단의 표본 수의 차이가 크면 결과의 신뢰가 떨어짐.