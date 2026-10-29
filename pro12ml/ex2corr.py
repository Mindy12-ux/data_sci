# 공분산 / 상관계수 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/drinking_water.csv')
print(data.head(5))
print(data.describe())

print('평균 / 표준편차')
print(np.mean(data.친밀도), ' ', np.std(data.친밀도))
print(np.mean(data.적절성), ' ', np.std(data.적절성))
print(np.mean(data.만족도), ' ', np.std(data.만족도))

# plt.hist([np.std(data.친밀도), np.std(data.적절성), np.std(data.만족도)])
# plt.show()

print('\n공분산 --- ')
print(np.cov(data.친밀도, data.적절성)) # numpy함수, 0.41642182, 양수 관계 - 친밀도가 늘어날 때 적절성도 함께 늘어난다.
print(np.cov(data.친밀도, data.만족도)) # 0.37566252, 양수 관계 - 친밀도가 늘어날 때 만족도도 늘어난다.
print()
print(data.cov())   # pandas DataFrame 함수
#           친밀도     적절성    만족도
# 친밀도  0.941569  0.416422  0.375663
# 적절성  0.416422  0.739011  0.546333
# 만족도  0.375663  0.546333  0.686816

print('\n상관계수 --- ')
print(np.corrcoef(data.친밀도, data.적절성))    # numpy함수, 0.49920861
print(np.corrcoef(data.친밀도, data.만족도))    # 0.46714498
print()
print(data.corr())    # pandas DataFrame 함수
#           친밀도     적절성    만족도
# 친밀도  1.000000  0.499209  0.467145
# 적절성  0.499209  1.000000  0.766853
# 만족도  0.467145  0.766853  1.000000
print(data.corr(method='pearson'))  # 연속형 변수, 정규성을 따름
# print(data.corr(method='spearman')) # 연속형 변수, 정규성을 따르지 않음
# print(data.corr(method='kendall'))  

print('\n만족도에 따른 다른 특성 사이의 관계')
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))

# 시각화
data.plot(kind='scatter', x='만족도', y='적절성')
plt.show()
plt.close()

from pandas.plotting import scatter_matrix
attr = ['친밀도', '적절성', '만족도']
scatter_matrix(data[attr], figsize=(10, 6))
plt.show()
plt.close()

import seaborn as sns
sns.heatmap(data.corr(), annot=True)
plt.show()

# heatmap에 텍스트 표시 추가사항 적용해 보기  ---------------
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()