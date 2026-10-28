# 어느 음식점의 매출과 날씨 자료를 이용해 온도에 따른 매출액 평균의 차이 검정 -------------------------

# 세 집단 : 추움, 보통, 더움

# 매출 데이터 : tsales.csv
# 날씨 데이터 : tweather.csv

# 귀무가설 : 온도에 따른 매출액 평균 차이가 없다.
# 대립가설 : 온도에 따른 매출액 평균 차이가 있다.

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

pd.set_option('display.max_columns', None)

# 매출 데이터 읽기 / 매출액을 확인해야 하므로 AMT칼럼이 필요함.
sales_data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/tsales.csv', dtype={'YMD':object}) # int -> object으로 변환해 읽기

print(sales_data.head(5))
print(sales_data.info())    # 328 * 3

# 날씨 데이터 읽기 / '강수 여부'를 확인해야 하므로 sumRn 칼럼이 필요함.
wt_data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/tweather.csv')
print(wt_data.head(5))
print(wt_data.info())   # 702 * 9 

print()
# sales_data : YMD 20190514
# wt_data : tm 2018-06-01 이므로 병합을 위한 변환이 필요하다.
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-','')) # wt_data.tm = wt_data['tm']
print(wt_data.head(2))

print()
# 두 데이터 병합
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
print(frame.columns)    # ['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes']
print(len(frame))
# print(frame['AMT'].isnull().sum())

data = frame.iloc[:, [0,1,7,8]]
print(data.head(5))
print('결측치 확인 : ', data.isnull().sum())

# plt.boxplot(data.maxTa)
# plt.show()
# print(data['maxTa'].describe()) # min  -4.900000, mean  18.597866, max  36.800000

# 온도를 세 그룹으로 나누기 (연속형 -> 범주형)
data['ta_group'] = pd.cut(data['maxTa'], bins=[-5, 8, 24, 37], labels=[0, 1, 2])
print(data.head(3), ' ', data['ta_group'].unique())
# 요인 1개(온도) : 그룹 3개(0, 1, 2)

# 정규성 / 등분산성
x1 = np.array(data[data['ta_group'] == 0].AMT)  # 추움 그룹 매출액
x2 = np.array(data[data['ta_group'] == 1].AMT)  # 보통 그룹 매출액
x3 = np.array(data[data['ta_group'] == 2].AMT)  # 더움 그룹 매출액
print(x1[:5])   # [1050500  770000 1054500  969000 1061500]

print()
print(stats.shapiro(x1).pvalue) # 0.2481924, > 0.05 이므로 정규성 만족 O
print(stats.shapiro(x2).pvalue) # 0.0388257, < 0.05 이므로 정규성 만족 X
print(stats.shapiro(x3).pvalue) # 0.3182989, > 0.05 이므로 정규성 만족 O  => 세 개 중에 두개가 만족했으니 정규성은 만족한 것으로 간주.

print(stats.levene(x1, x2, x3).pvalue)  # 0.0390023965 < 0.05 이므로, 등분산성 만족 X

print('\n온도별 매출액 평균')
# pandas 지수 표기법 해제(판다스 데이터프레임 자료이므로, pd에서 옵션을 바꿔줘야 됨)
pd.options.display.float_format = '{:.2f}'.format

spp = data.loc[:, ['AMT', 'ta_group']]
# 평균 보는 방법 1
print(spp.groupby('ta_group').mean())
# 평균 보는 방법 2
print(f'{np.mean(x1):.2f}') # 1032362.32
print(f'{np.mean(x2):.2f}') # 818106.87
print(f'{np.mean(x3):.2f}') # 553710.94

group1, group2, group3 = x1, x2, x3
print(stats.f_oneway(group1, group2, group3))
# statistic=99.190801, pvalue=2.36073710e-34
# 해석 : pvalue 2.36073710e-34 < 0.05 이므로 귀무가설을 기각한다.
# 결론 : 온도에 따른 매출액 평균 차이가 있다.

print()
# 정규성 깨지면 stats.kruskal() 사용, 등분산성이 깨지면 welch's ANOVA
# kruskal-Walli 검정
print(stats.kruskal(group1, group2, group3))

print()
# welch's ANOVA 검정 - 등분산 가정 불필요
print(stats.f_oneway(group1, group2, group3, equal_var=False))

print()
# 검정 방법을 제공하는 라이브러리는 다양하다.
# 예를 들어 다른 라이브러리로 welch's ANOVA 검정 수행
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(dv='AMT', between='ta_group', data=data))
#      Source  ddof1  ddof2      F  p_unc  np2
# 0  ta_group      2 189.65 122.22   0.00 0.38

print('\n사후검정')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['ta_group'])
print(tukResult)  
#        Multiple Comparison of Means - Tukey HSD, FWER=0.05       
# =================================================================
# group1 group2   meandiff   p-adj    lower        upper     reject
# -----------------------------------------------------------------
#      0      1 -214255.4486   0.0  -296755.647 -131755.2503   True
#      0      2 -478651.3813   0.0 -561484.4539 -395818.3088   True
#      1      2 -264395.9327   0.0 -333326.1167 -195465.7488   True
# -----------------------------------------------------------------


# 시각화
tukResult.plot_simultaneous(xlabel='매출액 평균', ylabel='온도 분류')
plt.show()







