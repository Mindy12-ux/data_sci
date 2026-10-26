# 집단간 차이 분석
# 단일 표본 t검정
# 정규분포의 표본에 대한 기대값을 조사하는 검정방법이다. 예상평균값과 표본 자료 간의 평균의 차이를 검정한다.
# 하나의 집단에 대한 표본 평균이 예측된 평균과 같은지 여부를 확인한다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# 실습 1 : 과거 5년 간 에이콘 아카데미 교육생의 남성 집단의 평균 키 검정
# 귀무 : 해당 집단의 평균 키가 177cm이다. (모수)
# 대립 : 해당 집단의 평균 키가 177cm가 아니다. (양측 검정)
# 대랍 : 해당 집단의 평균 키가 177cm보다 크다(작다) (단측 검정)

one_sample = [167.0, 182.7, 169.7, 176.8, 180.0]
print(np.array(one_sample).mean())  # 평균 키가 175.24인 경우, 177.0과 비교했을 때 유의미한 차이가 있는가. 

# 단일표본 t-검정(One-Sample t-test)
# 하나의 표본집단 평균이 특정 기준값(모집단의 평균)과 통계적으로 유의한 차이가 있는지 검정.
result = stats.ttest_1samp(one_sample, popmean=177.0)   # (데이터, 모수의 평균값)
print(result)
# statistic=-0.58775, pvalue=0.5882740, df = 4
# 해석 : 유의 수준 0.05 < pvalue=0.5882740 이므로, 귀무 가설이 채택된다.

print()
result2 = stats.ttest_1samp(one_sample, popmean=160.0)   # 모수의 평균값 : 16   0.0
print(result2)
# statistic=5.0894525, pvalue=0.007034142
# 해석 : 유의 수준 0.05 < pvalue=0.007034142 이므로, 귀무 가설이 기각된다.

sns.displot(one_sample, bins=10, kde=False, color='skyblue', edgecolor='black')
plt.axvline(np.mean(one_sample), color='green', linestyle='-', label='표본평균')
plt.axvline(177, color='red', linestyle='--', label='가설평균 177cm')
plt.title('교육생 키 분포')
plt.xlabel('키(cm)')
plt.ylabel('빈도(명)')
plt.legend()
plt.show()