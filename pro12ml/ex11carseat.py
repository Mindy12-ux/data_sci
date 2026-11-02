# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음) Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

# 다중선형모델의 적절성 선행 조건 실습 - ols 사용
# 선형성, 정규성, 등분산성, 독립성을 기본적으로 확인함.

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/Carseats.csv')
print(df.head(5),df.shape)  # (400, 11)
print(df.info())
df = df.drop([df.columns[6],df.columns[9],df.columns[10]],axis=1)
print(df.corr())

lm = smf.ols(formula='Sales ~ Income+Advertising+Price+Age', data=df).fit()
print(lm.summary()) # 4개 독립변수의 p값이 모두 0.05보다 작기 때문에 유의한 변수라고 할 수 있다.
# Skew(왜도 - 0이면 좌우대칭, 양수인 경우 오른쪽으로 꼬리가 긴 것.):0.218(대체로 대칭적인 분포)
# Kurtosis(첨도):2.903 (3에 근사하므로 정규분포와 유사하다고 볼 수 있음.)  
# 수정된 결정계수 - 0.364(이정도면 양호한 편)
print(f'수정된 결정계수는 {lm.rsquared_adj:.4f}이므로 양호하다.')

print('\n선형회귀 모델의 적절성 조건 체크 후 모델 사용')
print(df.columns)   # ['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'Age', 'Education']
# 우리가 사용한 0,2, 3, 5, 6번째 칼럼을 사용하여 잔차 구하기

# 잔차항 구하기
df_lm = df.iloc[:, [0,2,3,5,6]]
print(df_lm.head(5))
fitted = lm.predict(df_lm)  # 예측값을 얻음
residual = df_lm['Sales'] - fitted
print('잔차(residual) :\n', residual[:5])
print('잔차 평균: ', np.mean(residual)) # -1.4388e-15

print('\n1) 잔차의 정규성 : 잔차가 정규성을 따르는지 확인')
from scipy.stats import shapiro
import statsmodels.api as sm

stat, pv = shapiro(residual)
print(f'통계량 : {stat:.5f}, pv : {pv:.5f}')
print('정규성 만족' if pv >= 0.05 else '정규성 위배')

# Q-Q plot
sm.qqplot(residual, line='s')
plt.title('Q-Q plot으로 정규성 확인')
plt.show()

print('\n2) 선형성 검정')
from statsmodels.stats.diagnostic import linear_reset
reset_result = linear_reset(lm, power=2, use_f=True)
print(f'reset_reuslt : {reset_result.pvalue:.5f}')
print('선형성 만족' if reset_result.pvalue >= 0.05 else '선형성 위배')

# plot
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0], '--', color='gray')
plt.show()

print('\n3) 등분산성 검정')
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, sm.add_constant(df_lm['Sales']))
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print(f'p-value : {bp_pvalue:.4f}')
print('등분산성 만족' if bp_pvalue >= 0.05 else '등분산성 위배')
# 시각화는 선형성 그래프 참고

print('\n4) 독립성 검정 : 독립변수 간의 값이 서로 관련되지 않아야 한다.')
# 잔차가 자기상관(인접 관측치의 오차가 관련됨)이 있는지 확인.
# Durbin-Watson : 잔차의 자기상관(auto-correlation) 검정 지표(model.summary로 확인 가능).
# 값의 범위는 0 ~ 4이고 2이면 정상(자기 상관이 없음). 2보다 크면 양의 자기상관이 있고, 2보다 작으면 음의 자기상관이 있는 것이다.

print('Durbin-Watson : ', sm.stats.stattools.durbin_watson(residual))   # 1.931498
# 예제의 Income, Advertising, Price, Age 간에는 서로 관련이 없다.

# plot
plt.plot(np.arange(len(residual)), residual, marker='o', linestyle='-')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('관측순서')
plt.ylabel('잔차')
plt.title('독립성 확인 : 잔차 순서 그래프')
plt.grid(alpha=0.3)
plt.show()
# 잔차가 0을 중심으로 불규칙하게 움직이므로 독립성을 만족한다.

print('\n5) 다중공선성 검정 : 독립변수들 간에 값이 서로 관련되지 않아야 한다.')
# VIF(variance_inflation_factor, 분산 인플레 요인, 분산 팽창 지수)
from statsmodels.stats.outliers_influence import variance_inflation_factor
df_ind = df[['Income','Advertising', 'Price', 'Age']]   # 독립변수들
vifdf = pd.DataFrame()
vifdf['변수'] = df_ind.columns
vifdf['vif_value'] = [variance_inflation_factor(df_ind.values, i) for i in range(df_ind.shape[1])]

print(vifdf)    # 10을 초과하지 않으면 만족, 다중공선성 문제가 발생하지 않음
#            변수  vif_value
# 0       Income   5.971040
# 1  Advertising   1.993726
# 2        Price   9.979281
# 3          Age   8.267760

# plot
sns.barplot(x='변수', y='vif_value', data=vifdf)
plt.axhline(10, color='red', linestyle='--')
plt.title('다중공선성 확인')
plt.ylabel('vif_value')
plt.show()

print('===========')
# 유의한 모델이므로 완성된 모델 저장하고 읽어 모델 재사용하기
# 방법 1

import joblib
joblib.dump(lm, 'carseat.model')
# 이후부터는 아래처럼 읽어 사용하면 됨(lm은 없어도 됨)
mymodel = joblib.load('carseat.model')

print(mymodel.summary())

print('새로운 값으로 예측')
new_df = pd.DataFrame({'Income':[35,62], 'Advertising':[6,3], \
                    'Price':[105, 88], 'Age':[32,55]})
new_pred = mymodel.predict(new_df)
print('sales 예측 결과 : ', new_pred.values)    # [8.71289 8.49715]