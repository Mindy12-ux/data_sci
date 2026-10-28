# 일원분선분석(One-way ANOVA)으로 그룹 간 평균 차이 검정

# 서초구에 있는 3개 지역(서초동, 반포동, 양재동) GS 편의점에 근무하는 알바생의 급여에 대한 평균 차이 검정

# 귀무 가설 : 3개 지역의 GS 편의점 알바생의 급여에 대한 평균은 차이가 없다.
# 대립 가설 : 3개 지역의 GS 편의점 알바생의 급여에 대한 평균은 차이가 있다.

from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib.request

url = 'https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/group3.txt'
# 읽기 1)
# data = pd.read_csv(url, header=None)
# print(data.values) # 이렇게 읽으면 넘파이처럼 배열로 읽힘

# 읽기 2)
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
# print(data)  # [[243.   1.]
print(data.shape)   # (22, 2)

# 세 그룹의 월급 자료 얻기 - 평균을 구하기 위해
gr1 = data[data[:, 1] == 1, 0]  # 지역이 1인 지점의 월급
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]
print(gr1, ' ', np.mean(gr1))   # 316.625
print(gr2, ' ', np.mean(gr2))   # 256.444
print(gr3, ' ', np.mean(gr3))   # 278.0

print()
# 정규성 확인
print(stats.shapiro(gr1).pvalue)    # 0.3336828975503454
print(stats.shapiro(gr2).pvalue)    # 0.6561053974090567
print(stats.shapiro(gr3).pvalue)    # 0.8324811461768902, 셋 다 정규성 만족

# 정규성을 심각하게 위반하고 표본도 작다면, 분포 형태에 의존하지 않는 비모수 검정을 사용한다.
# One-way ANOVA의 대안 - 크루스칼-왈리스검정 (kruskal-wallis test)
# stats.kruskal(group1, group2, group3)

print()
# 등분산성 확인
print(stats.levene(gr1, gr2, gr3).pvalue)   # 0.045846, 엄밀히 따지면 0.05보다 작지만, 이번 예제처럼 차이가 얼마나지 않는다면 그냥 넘어가도 된다.
print(stats.bartlett(gr1, gr2, gr3).pvalue) # 0.350803

# ANOVA에서 등분산성을 만족하지 못한 경우
# Welch's ANOVA (웰치 분산분석) : 보편적으로 사용하는 강력한 대안
# 데이터 변환 : 원래 데이터의 척도를 변화시켜 분산분석 수행. (로그 변환, 제곱근 변환, 표준화 등)

# 일원분산분석 방법 1 : anova_lm()
df = pd.DataFrame(data=data, columns=['pay', 'group'])
# print(df)
lmodel = ols('pay ~ C(group)', data=df).fit()  # C(group) : group은 범주형임을 명시적으로 표현
print(anova_lm(lmodel, type=1))
#             df        sum_sq      mean_sq         F    PR(>F)
# C(group)   2.0  15515.766414  7757.883207  3.711336  0.043589
# Residual  19.0  39716.097222  2090.320906       NaN       NaN
# 해석 : pvalue 0.043589 < 0.05 이므로 귀무가설을 기각한다.
# 결론 : 3개 지역의 GS 편의점 알바생의 급여에 대한 평균은 차이가 있다.

# 일원분산분석 방법 2 : f_oneway()
f_stat, pv = stats.f_oneway(gr1, gr2, gr3)
print('f_stat : ', f_stat)  # 3.71133598
print('p_value : ', pv)     # 0.04358933
# 결과 위와 동일 / 다만 anova_lm을 사용하면 표까지 얻을 수 있다는 장점이 있다.

# 최종 결론 : 3개 지역의 GS 편의점 알바생의 급여에 대한 평균은 차이가 있다. -> 얼마나?

print()
# 서초동, 반포동, 양재동 지역 간 평균 차이가 궁금하다면? -> 사후 검정
df['region'] = df['group'].map({1:'서초동', 2:'반포동', 3:'양재동'}) # 지역명 추가

from statsmodels.stats.multicomp import pairwise_tukeyhsd
# tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.region)
print(tukResult)    # 차이가 심할 때 reject이 true가 된다.

# 시각화
tukResult.plot_simultaneous(xlabel='급여 평균', ylabel='지역')
plt.show()
