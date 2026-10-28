# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 귀무 가설 : 기름 종류에 따른 기름 흡수량에 차이가 없다.
# 대립 가설 : 기름 종류에 따른 기름 흡수량에 차이가 있다.

from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib.request

data = pd.read_table('oil.txt')
print(data.columns)

# 칼럼 수정
data[['kind', 'quantity']] = data['kind quantity'].str.split(' ', expand=True)
data = data.drop(columns=['kind quantity'])
print(data)
print()

# 정수 변환 / 결측치 채우기
data['kind'] = pd.to_numeric(data['kind'], errors='coerce')
data['quantity'] = pd.to_numeric(data['quantity'], errors='coerce')
data['quantity'] = data['quantity'].fillna(data['quantity'].mean())

# 치즈 종류별로 데이터 분리
x1 = np.array(data.loc[data["kind"] == 1, "quantity"])
x2 = np.array(data.loc[data["kind"] == 2, "quantity"])
x3 = np.array(data.loc[data["kind"] == 3, "quantity"])
x4 = np.array(data.loc[data["kind"] == 4, "quantity"])
print(x1)
print(x2)
print(x3)
print(x4)
print()

# 정규성 검정
print(stats.shapiro(x1).pvalue) # 0.868040
print(stats.shapiro(x2).pvalue) # 0.5923924
print(stats.shapiro(x3).pvalue) # 0.48601083
print(stats.shapiro(x4).pvalue) # 0.41621616, 모두 정규성 만족
print()

# 등분산성 검정
print(stats.levene(x1, x2, x3, x4).pvalue)  # 0.3268969, 등분산성 만족
print()

# ANOVA 검정
print(stats.f_oneway(x1, x2, x3, x4))
# statistic=0.2669351,  pvalue=0.84824366
# 해석 : pvalue 0.84824366 > 0.05 이므로 귀무 가설을 수용한다.
# 결론 : 기름 종류에 따른 기름 흡수량에 차이가 없다.

print('\n사후검정')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=data['quantity'], groups=data['kind'])
print(tukResult)  

# 시각화
tukResult.plot_simultaneous(xlabel='기름 흡수량', ylabel='기름 종류')
plt.show()