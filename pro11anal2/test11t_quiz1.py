# [two-sample t 검정 : 문제1] 
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.
# 수집된 자료 :  
# blue : 70 68 82 78 72 68 67 68 88 60 80
# red : 60 65 55 58 67 59 61 68 77 66 66

# 귀무가설 : 포장지 색상에 따른 제품의 매출액 차이가 존재하지 않는다.
# 대립가설 : 포장지 색상에 따른 제품의 매출액 차이가 존재한다.

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

print('blue의 매출액 평균 : ', np.mean(blue))   # 72.81818
print('red의 매출액 평균 : ', np.mean(red))     #  63.818181

# 정규성 검정
print('blue 정규성 : ', stats.shapiro(blue).pvalue) # 0.510231
print('red 정규성 : ', stats.shapiro(red).pvalue)   # 0.53479332, 둘 다 만족

# 등분산성 검정
print('등분산성 : ', stats.levene(blue, red).pvalue)    #  0.43916444, 만족

# 독립 표본 t-검정
print('독립 표본 t-검정 : ', stats.ttest_ind(blue, red, equal_var=True))
# statistic=2.9280203, pvalue=0.008316545
# 해석 : pvalue 0.008316545 < 0.05 이므로 귀무가설을 기각한다.
# 결론 : 2포장지 색상에 따른 제품의 매출액 차이가 존재한다.
