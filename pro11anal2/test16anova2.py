# 이원분산분석(two-way ANOVA)  ---------------------------
# 독립변인의 수가 두 개 이상일 때 집단 간 차이가 유의한지를 검증하는 데 사용한다. 
# 상호작용효과(Interaction effect) : 한 변수의 변화가 결과에 미치는 영향이 다른 변수의 수준에 따라 달라지는지를 확인하기 위해 사용된다.
# - 두 개의 요인에 대한 집단(독립변수) 각각이 종속변수(평균)에 영향을 주는지 검정
# - 주효과(개별효과) : 독립변수들이 각각 독립적으로 종속변수에 미치는 영향을 검정하는 것
# - 상호작용효과(교호작용) : 독립변수들이 서로 연관되어 종속변수에 미치는 영향을 검정하는 것
#                          한 독립변수가 종속변수에 미치는 영향이 다른 독립변수의 수준에 따라 달라지는 현상

# 실습 : 독의 종류와 처치방법에 따라 실험 동물의 평균 생존시간에 차이가 있는가?

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import koreanize_matplotlib
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/poison_treat.csv', index_col=0)
# 첫 번째 열을 Dataframe의 인덱스로 사용
print(data.head(5))
print(data.shape)   # (48, 3)

# 데이터 설명
# - poison : 독의 종류 (3개 수준)
# - treat  : 처치방법 (4개 수준)
# - time   : 독에 노출된 실험동물의 생존시간

# 독 3종류 × 처치방법 4종류 = 12개 조합
# 각 조합에서 실험동물 4마리 관측 → 총 48개 자료
# 독이 퍼지는 시간이 아니라 '생존시간'을 분석함

# [주효과 가설 1 : 독의 종류] - 요인
# 귀무(H0) : 독의 종류에 따른 평균 생존시간은 모두 같다.
# 대립(H1) : 독의 종류에 따른 평균 생존시간 중 적어도 하나는 다르다.

# [주효과 가설 2 : 처치방법] - 요인
# 귀무(H0) : 처치방법에 따른 평균 생존시간은 모두 같다.
# 대립(H1) : 처치방법에 따른 평균 생존시간 중 적어도 하나는 다르다.

# [교호작용 가설] - 12개의 조합
# 귀무(H0) : 독의 종류와 처치방법 간 교호작용은 없다.
# 대립(H1) : 독의 종류와 처치방법 간 교호작용은 있다.
# 교호작용이 있다는 의미: 처치방법에 따른 생존시간 차이가 독의 종류에 따라 달라짐

# 주효과: 각각의 독립변수에 따라 종속변수의 평균이 달라지는가?
# 교호작용: 한 독립변수에 따른 평균 차이가 다른 독립변수의 수준에 따라 달라지는가?

print('\n요인별 표본 수 확인')
print('독 종류별 표본수 : ', data.groupby('poison').size())
print('처치방법별 표본수 : ', data.groupby('treat').size())
print('독 종류 X 처치방법 : ', data.groupby(['poison', 'treat']).size())
# 모든 조합에서 표본 수가 4로 동일하다. 균형있게 설계되어 있음

print('\n요인별 기술 통계')
print('\n독 종류별 생존 시간 : \n', data.groupby('poison')['time'].agg(['count','mean']))
print('\n처치방법별 생존 시간 : \n', data.groupby('treat')['time'].agg(['count','mean']))

# 이원분산분석 ----------------
model = ols('time ~ C(poison) * C(treat)', data=data).fit()  # * : 주효과 + 교호작용 분석
result = anova_lm(model, type=1)
print('\n이원분산분석 결과 : \n', result)
#                       df    sum_sq   mean_sq          F        PR(>F)
# C(poison)            2.0  1.033013  0.516506  23.221737  3.331440e-07
# C(treat)             3.0  0.921206  0.307069  13.805582  3.777331e-06
# C(poison):C(treat)   6.0  0.250138  0.041690   1.874333  1.122506e-01
# Residual            36.0  0.800725  0.022242        NaN           NaN

# 해석 
p_poison = result.loc['C(poison)', 'PR(>F)']
p_treat = result.loc['C(treat)', 'PR(>F)']
p_interaction = result.loc['C(poison):C(treat)', 'PR(>F)']
alpha = 0.05

if p_poison < alpha:
    print('독종류 : 귀무 기각 - 독의 종류에 따른 평균 생존시간에 유의미한 차이가 있다.')
else:
    print('독종류 : 귀무 채택 - 독의 종류에 따른 평균 생존시간에 유의미한 차이가 없다.')

if p_treat < alpha:
    print('처치방법 : 귀무 기각 - 처치방법에 따른 평균 생존시간에 유의미한 차이가 있다.')
else:
    print('처치방법 : 귀무 채택 - 처치방법에 따른 평균 생존시간에 유의미한 차이가 없다.')

if p_interaction < alpha:
    print('교호작용 : 귀무 기각 - 처치방법의 효과는 독의 종류에 따라 다르다.')
else:
    print('교호작용 : 귀무 채택 - 처치방법의 효과는 독의 종류에 따라 다르지 않다.')

# 사후 검정(Post-hoc test)
print('\n독 종류별 사후검정')
tkResult1 = pairwise_tukeyhsd(endog=data['time'], groups=data['poison'], alpha=0.05)
print(tkResult1)

tkResult1.plot_simultaneous(xlabel='평균생존시간', ylabel='독 종류')
plt.title('독 종류별 생존 시간')
plt.show()
plt.close()

print('\n처치 방법별 사후검정')
tkResult2 = pairwise_tukeyhsd(endog=data['time'], groups=data['treat'], alpha=0.05)
print(tkResult2)

tkResult2.plot_simultaneous(xlabel='평균생존시간', ylabel='처치방법')
plt.title('처치 방법별 생존 시간')
plt.show()
plt.close()



