# 서로 대응인 두 집단의 평균 차이 검정

# paired samples t-test, 대응표본 t-검정, 동일집단 표본 t-검정, 쌍체 t-검정

# 처리 이전과 처리 이후를 각각의 모집단으로 판단하여, 
# 동일한 관찰 대상으로부터 처리 이전과 처리 이후를 1:1로 대응시킨 검정 방법이다.
# 대응인 두 집단의 평균 비교는 동일한 관찰 대상으로부터 처리 이전의 관찰과 이후의 관찰을 비교하여 영향을 미친 정도를 밝히는데 주로 사용하고 있다.
# 집단 간 비교가 아니므로 등분산 검정을 할 필요가 없다.

# 단일 표본 : 하나의 집단의 평균을 일반적인 평균(모평균)과 비교
# 독립 표본 : 서로 다른 두 집단의 평균을 비교
# 대응 표본 : 하나의 집단의 변화 전/후 평균 비교

# 실습) 복부 수술 전 9명의 몸무게와 복부 수술 후 몸무게 변화

# 귀무 가설 : 수술 전후 평균 몸무게 차이는 0이다.
# 대립 가설 : 수술 전후 평균 몸무게 차이는 0이 아니다.
# 유의수준(alpha) = 0.05

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

df = pd.DataFrame({
    '수술전': baseline,
    '수술후':follow_up
})

df['감소량'] = df['수술전'] - df['수술후']

print(df)
print(df.describe())
print(f"수술 전 평균 몸무게 : {df['수술전'].mean():.2f}kg") # 78.41kg
print(f"수술 후 평균 몸무게 : {df['수술후'].mean():.2f}kg") # 71.50kg

result = stats.ttest_rel(baseline, follow_up)
print(f't 통계량 : {result.statistic:.5f}') # 3.66812
print(f'p-value : {result.pvalue:.5f}')    # 0.00633

# 해석 
alpha = 0.05
if result.pvalue < alpha:
    print('귀무 기각 : 수술 전후 평균 몸무게에 통계적으로 유의미한 차이가 있다.')

else:
    print('귀무 채택 : 수술 전후 평균 몸무게에는 통계적으로 유의미한 차이가 없다.')

# 귀무 기각 : 수술 전후 평균 몸무게에 통계적으로 유의미한 차이가 있다.

# 몸무게 차이값에 대한 정규성 검정
print('몸무게 감소량 정규성 : ', stats.shapiro(df['감소량']))   # 0.116522, 정규성 만족

# Q-Q plot
stats.probplot(df['감소량'], dist='norm', plot=plt)
plt.grid(True)
plt.show()

# 몸무게 변화량을 시각화
plt.figure(figsize=(8, 5))
for before, after in zip(baseline, follow_up):
    plt.plot(['수술전', '수술후'], [before, after], marker='o')
plt.title('수술 전후 몸무게 변화')
plt.ylabel('몸무게(kg)')
plt.grid(axis='y', alpha=0.3)
plt.show()