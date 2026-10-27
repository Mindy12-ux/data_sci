# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
# 수집된 자료 :  
# 남자 : 0.9 2.2 1.6 2.8 4.2 3.7 2.6 2.9 3.3 1.2 3.2 2.7 3.8 4.5 4 2.2 0.8 0.5 0.3 5.3 5.7 2.3 9.8
# 여자 : 1.4 2.7 2.1 1.8 3.3 3.2 1.6 1.9 2.3 2.5 2.3 1.4 2.6 3.5 2.1 6.6 7.7 8.8 6.6 6.4

# 귀무가설 : 성별 간 혈관 내의 콜레스테롤 양에 차이가 없다.
# 대립가설 : 성별 간 혈관 내의 콜레스테롤 양에 차이가 있다.

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

print('남자의 콜레스테롤 평균 : ', np.mean(male))
print('여자의 콜레스테롤 평균 : ', np.mean(female))

# 정규성 검정
print('male 정규성 : ', stats.shapiro(male).pvalue) # 0.0167092
print('female 정규성 : ', stats.shapiro(female).pvalue) # 0.00080136, 둘 다 정규성을 만족하지 못함.

# 둘 다 정규성을 만족하지 못하므로 비모수 검정인 Mann-whitney test를 수행한다.
print('Mann-whitney test : ', stats.mannwhitneyu(male, female))
# statistic=221.5, pvalue=0.845479
# 해석 : pvalue=0.845479 > 0.05 이므로 귀무가설을 채택한다.
# 결론 : 성별 간 혈관 내의 콜레스테롤 양에 차이가 없다.

