# 상관관계 문제)
# https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 또한 sales와 관계를 알기 위해 sales에 상관 관계를 정렬한 후 TV, radio, newspaper에 대한 영향을 해석하시오.
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv')

print(data.head(5))

attr = ['tv', 'radio', 'newspaper', 'sales']
data = data[attr]

print('\n매체 간 상관관계 파악')
print(data[['tv', 'radio', 'newspaper']].corr())
#                 tv     radio  newspaper
# tv         1.000000  0.054809   0.056648      tv 사용이 증가할 때 라디오 사용은 0.054809만큼 증가, tv 사용이 증가할 때 신문 사용은 0.054809만큼 증가
# radio      0.054809  1.000000   0.354104
# newspaper  0.056648  0.354104   1.000000

print('\nsales에 상관 관계를 정렬한 후 TV, radio, newspaper에 대한 영향 분석')
co_re =  data.corr()
sales_corr = co_re['sales'].sort_values(ascending=False)
sales_corr = co_re['sales'].drop('sales')  # 자기 자신과의 상관계수 1.0은 제외
print(sales_corr)

print('\n상관관계 분석 결과 ---- ')
for name , r in sales_corr.items():
    if r > 0:
        msg = '양의 상관관계'
    elif r < 0:
        msg = '음의 상관관계'
    else:
        msg = '상관관계 없음'

    print(f'{name} : r={r:.3f}, {msg}')

print('\nSales와 양의 상관관계가 가장 높은 광고 매체 : ', sales_corr.idxmax())

# sales        1.000000
# tv           0.782224
# radio        0.576223
# newspaper    0.228299
# 해석 : sales와 tv의 상관계수가 가장 높다. tv 사용이 증가할 때 매출은 0.782224 증가한다.

# 히트맵
sns.heatmap(data[['tv', 'radio', 'newspaper', 'sales']].corr(), annot=True)
plt.show()
plt.close()