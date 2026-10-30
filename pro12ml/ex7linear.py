# 단순선형회귀 : ols를 이용한 결과 이해
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import statsmodels.formula.api as smf

# 음료 : 친밀도 적절성 만족도 데이터 이용
df = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/drinking_water.csv')
print(df.head(5))
print(df.corr())
#           친밀도     적절성    만족도
# 친밀도  1.000000  0.499209  0.467145
# 적절성  0.499209  1.000000  0.766853
# 만족도  0.467145  0.766853  1.000000

# 음료 적절성과 만족도는 양의 상관관계가 매우 강함.
# 음료 적절성이 만족도에 영향을 준다. 즉, 적절성과 만족도는 원인과 결과의 관계이다.(인과관계)
# 귀무 : 음료 적절성과 만족도는 원인과 결과의 관계가 없다.
# 대립 : 음료 적절성과 만족도는 원인과 결과의 관계가 있다.

model = smf.ols(formula='만족도 ~ 적절성', data=df).fit()
print(model.summary())

#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                  만족도   R-squared:                       0.588 => 독립변수가 하나만 있을 때.
# Model:                            OLS   Adj. R-squared:                  0.586 => 독립변수가 2개 이상일 때.
# Method:                 Least Squares   F-statistic:                     374.0 => F 값
# Date:                Fri, 30 Oct 2026   Prob (F-statistic):           2.24e-52 => 모델 전체에 대한 p-value, 인과관계를 판단하는 수치. 0.05보다 크면 해당 모델은 의미가 없는 것.
# Time:                        12:50:55   Log-Likelihood:                -207.44
# No. Observations:                 264   AIC:                             418.9 => 모델 비교용
# Df Residuals:                     262   BIC:                             426.0 => 모델 비교용
# Df Model:                           1                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975] => [] : 신뢰구간
# ------------------------------------------------------------------------------
# Intercept      0.7789      0.124      6.273      0.000       0.534       1.023
# 적절성          0.7393      0.038     19.340    0.000(p값)    0.664       0.815 => 독립변수 각각에 대한 p-value, 지금은 독립변수가 하나밖에 없기 때문에 모델의 pv와 독립변수의 pv가 동일하다.
# ==============================================================================
# Omnibus:                       11.674   Durbin-Watson:                   2.185 => 잔차의 독립성 확인, 2에 근사할수록 좋음
# Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003 
# Skew:                          -0.328   Prob(JB):                     0.000335 => 정규분포 확인, 0에 가까울수록 좋음
# Kurtosis:                       4.012   Cond. No.                         13.4 => 조건수, 다중공선성 확인용. 값이 크면 다중공선성을 의심할 수 있음.
# ==============================================================================

print('parameters : \n', model.params)
# parameters : 
# Intercept    0.778858   (bias)
# 적절성        0.739276   (weight, slope)
print('R-squared : ', model.rsquared)      # R-squared :  0.588063  <-- 1에 가까우면 좋음. 근데 너무 가까우면 기형모델이 됨 
print('pvalue : ', model.pvalues)          # 1.454388e-09, 2.235345e-52
print('예측값 : ', model.predict()[:5])     # [3.7359 2.9966 3.7359 2.2574 2.2574]
print('실제값 : ', df.만족도[:5].values)    # [3 2 4 2 2]

# R_squared, 결정계수(설명력) : 모델의 성능 측정에 사용, 독립변수 x가 종속변수 y를 얼마나 설명하느냐. 상관계수를 제곱한 값임.
# 1에 근사할수록 성능이 좋은 것. R_squared은 모델의 '설명력'을 측정하는 지표이지, '정확도'를 측정하는 지표는 아니다. 
# 인과관계 : p값 (0.05보다 작아야 함) / R-squared : 0.5보다 커야 좋음
# 확률 : 어떤 결과가 나올 비율, 가능도(Log-Likelihood, 우도) : 관측된 결과를 얼마나 잘 설명하는가?
# 표준오차 : 표본에서 얻은 통계량(표본 평균)이 반복적인 추출에 따라 얼마나 흔들리는지, 표본 분포의 표준편차를 의미한다.
#           표본 평균 등이 실제 모집단 값에서 얼마나 벗어날 수 있는지에 대한 불확실성이나 변동성을 나타낸다.
# '적절성'의 t값 = 기울기 / 표준오차 = 0.7393 / 0.038 = 19.340
# t값의 제곱 = F값, 19.304 * 2 = 374.0 (그리고 이 F값으로 p값을 유도한다)
# 다중공선성 : 회귀분석에서 독립변수들 사이에 강한 선형 상관관계가 나타나는 현상
# Omnibus : 유의성

# R_squared, 결정계수(설명력) : 독립변수가 종속변수의 분산을 얼마나 잘 설명하는가?

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, df.적절성 * slope + intercept, c='r')
plt.xlabel('적절성')
plt.show()

print('\n실제값과 예측값 비교')
result_df = pd.DataFrame(
    {'실제값':df['만족도'], '예측값':model.predict(), '잔차':model.resid}
    )
print(result_df.head(10).round(3))

# 회귀모델 평가지표 : 결정계수(설명력), 예측오차(MAE, MSE, RMSE), p-value
# 모델 오차로 평가
print(f'RSS : {model.ssr:.4f}') # 잔차제곱합(Residual Sum of Squares), 74.4092
print(f'MSE : {np.mean(model.resid ** 2):.4f}') # MSE : 잔차제곱의 평균, 0.2819
print(f'RMSE : {np.sqrt(np.mean(model.resid ** 2)):.4f}')   # 0.5309
# RSS는 오차를 제곱해서 전부 더한 값, MSE는 그것을 평균낸 값, RMSE는 다시 원래 단위로 바꾼 값
# 세 지표 모두 작을수록 예측 오차가 작지만, 실제 모델의 오차 규모를 이해하기에는 RMSE가 더 직관적이다.

# 생성된 모델로 새로운 x값에 대한 예측 결과를 출력 (정량적 분석)
new_data = pd.DataFrame({'적절성':[3.123, 4.123, 5.123]})
new_pred = model.predict(new_data)
print(pd.DataFrame({'적절성':new_data['적절성'], '예측 만족도':new_pred}).round(3))
#    적절성  예측 만족도
# 0  3.123   3.088
# 1  4.123   3.827
# 2  5.123   4.566