# 단일 모집단의 평균에 대한 가설검정 (one-sample t-test)

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# 실습예제 1)
# A 중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리(국어점수 평균 검정)
# 귀무 : 학생들의 국어 점수 평균은 80점이다.
# 대립 : 학생들의 국어 점수 평균은 80점이 아니다.

data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/student.csv')
print(data.head(5))
print(data.describe())
print(data['국어'].mean())  # 72.9
print(len(data))    # 20        30행이 넘으면 '중심극한정리'에 의해 정규성을 따른다고 가정.
# 중심극한정리 : 표본의 크기가 충분히 커지면 표본평균들의 분포가 정규분포에 가까워진다.
# 30개가 넘지 않으므로 정규성 검정을 선행한다. 

# 정규성 검정 : 수집한 데이터가 정규분포를 따르는지 확인.
# 샤피로-윌크 검정 (Shapiro-Wilk Test)으로 데이터가 정규분포를 가지는지를 확인
# p값은 alpha 0.05보다 커야 정규성을 따른다고 할 수 있다.
print(stats.shapiro(data['국어']))  # Alpha 0.05 > pvalue=0.0129597 => 정규성을 만족하지 못한다.

# 정규성을 만족하지 못한 경우의 대안 : Willcoxon test
from scipy.stats import wilcoxon
wilcoxon_result = wilcoxon(data['국어'] - 80)
print('wilcoxon_result : ', wilcoxon_result)
# statistic=74.0, pvalue=0.3977762
# 해석 : alpha 0.05 < pvalue=0.3977762 이므로 귀무가설 채택

# 정규성을 만족한 경우는 ttest_1smp() 수행
ttest_result = stats.ttest_1samp(data['국어'], popmean=80)
print(ttest_result)
# statistic=-1.3321801, pvalue=0.1985605
# 해석 : alpha 0.05 < pvalue=0.1985605 이므로 귀무가설 채택

# 결론 : 정규성은 부족하나 귀무가설 채택이라는 동일 결론을 얻음
# 만약 표본 수가 크다면 그냥 ttest_1smp을 써도 된다.

print('-------------')
# 실습 예제2)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해보자

data2 = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/babyboom.csv')
print(data2.head(5))
pd.set_option('display.max_columns', None)
print(data2.describe())
print()
fdata = data2[data2.gender == 1]    # 1: 여아, 2: 남아
print(fdata, ' ', len(fdata))       # 18
print('여아 신생아 몸무게 평균 : ', np.mean(fdata.weight))  # 3132.44
# 평균 2800과 3132는 유의미한 차이가 있는가?  t-test로 검정
print('여아 신생아 몸무게 표준편차 : ', np.std(fdata.weight))   # 613.787

# One-sample t-test
result2 = stats.ttest_1samp(fdata['weight'], popmean=2800)
print(result2)
# statistic=2.233187, pvalue=0.03926844, dof = 17
# 해석 1 (p-value값 사용) : 유의수준 0.05 > pvalue=0.03926844 이므로 귀무가설 기각
# 해석 2 (t분포표 사용) : t값 statistic=2.233187, dof : 17, alpha : 0.05, cv(critical value) = 1.740
# => statistic=2.233187 > cv(critical value) = 1.740 이므로 귀무가설 기각, t값이 cv값의 오른쪽(귀무 기각영역)에 있으므로 귀무 기각

print('t-test 선행 조건 : 정규성 확인 (n<30)인 경우에만. ---------- ')
# 정규성 확인방법 1: shapiro test
print(stats.shapiro(fdata['weight']))   
# pvalue=0.01798478 < 0.05이므로 정규성을 만족시키지 못함.

# 정규성 확인방법 2 시각화 : histplot
sns.histplot(fdata['weight'], kde=True)     # 데이터가 정규성을 만족한다면 종 모양이 나와야 함. 이 예제에서는 왜곡된 데이터 분포를 확인할 수 있다.
plt.show()

# 정규성 확인방법 3 시각화 : Q-Q plot(Quantile-Quantile plot)
stats.probplot(fdata['weight'], plot=plt)   # Q-Q plot 상에서 잔차가 정규성을 만족하지 못하고 있다.
plt.show()

# 정규성을 만족하지 못하는 경우 wilcoxon 검정을 시행.
result3 = wilcoxon(fdata['weight'] - 2800)
print(result3)
# statistic=37.0, pvalue=0.034233093261
# 유의 수준 0.05 > pvalue=0.034233093261 이므로 귀무 가설 기각





