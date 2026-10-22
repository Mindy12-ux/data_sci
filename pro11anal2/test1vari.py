# 표준 편차, 분산의 중요성
# '두 집단의 성적 평균이 동일하다고 해서, 성적 분포까지 동일하다고 할 수 있는가?'
#  실제로 표준편차의 크기에 따라 성적 편차가 다를 수 있다.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

np.random.seed(42)

# 목표 평균
target_mean = 60
std_dev_small = 10
std_dev_large = 20

# 데이터 생성
class1_raw = np.random.normal(loc=target_mean, scale=std_dev_small, size=100)
class2_raw = np.random.normal(loc=target_mean, scale=std_dev_large, size=100)
print(class1_raw)
print(class2_raw)

# 평균 보정 / 지금 만들어진 평균은 정확히 60이 아니라 근소한 오차가 있음. 평균을 완전한 60으로 만들기 위한 작업임.
class1_adj = class1_raw - np.mean(class1_raw) + target_mean
class2_adj = class2_raw - np.mean(class2_raw) + target_mean
# print(np.mean(class1_raw))

print()
# 정수화 및 범위 제한, np.clip(배열, 최소값, 최대값)
class1 = np.clip(np.round(class1_adj), 10, 100).astype(int)
class2 = np.clip(np.round(class2_adj), 10, 100).astype(int)
print(class1)
print(class2)

# 통계 계산
mean1, mean2 = np.mean(class1), np.mean(class2)
std1, std2 = np.std(class1), np.std(class2)
var1, var2 = np.var(class1), np.var(class2)

print('1반 (성적 편차가 적음)')
print(f'평균 : {mean1}, 표준편차 : {std1}, 분산 : {var1}')
print('2반 (성적 편차가 큼)')
print(f'평균 : {mean2}, 표준편차 : {std2}, 분산 : {var2}')

# 자료를 파일로 저장
df = pd.DataFrame({
    'class':['1반'] * 100 + ['2반'] * 100,      # class 칼럼
    'score':np.concatenate([class1, class2])    # score 칼럼
})
print(df.head(5))
print(df.tail(5))
df.to_csv('test1.csv', index=False, encoding='utf-8-sig')

print('\n시각화 ----- ')
x1 = np.random.normal(1, 0.05, size=100)
x2 = np.random.normal(2, 0.05, size=100)

plt.figure(figsize=(10, 6))
plt.scatter(x1, class1, alpha=0.8, label=f'1반(평균={mean1:2f}, 표준편차={std1:2f})')
plt.scatter(x2, class2, alpha=0.8, label=f'2반(평균={mean2:2f}, 표준편차={std2:2f})')
plt.hlines(target_mean, 0.5, 2.5, colors='red', linestyles='dashed', label=f"공통평균={target_mean}")
plt.xticks([1,2], ['1반','2반'])
plt.ylabel('시험 점수')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.boxplot([class1, class2], label=['1반','2반'])
plt.grid(True)
plt.show()
# 국어 선생님 입장에서 말하기를 ...
# 전통적 주장(귀무 가설) : 지금까지 내가 가르쳐온 반의 국어 평균(편차)은 항상 차이가 없었다.
# 누군가가 실험을 통해 데이터를 수집한 후 두 반의 평균을 비교해보았다. 그리고 두 반의 평균 점수에 차이가 있다는 새로운 의견을 제시하였다. (대립 가설)
# 대립 가설 : 두 반의 국어 점수 평균(편차)에는 유의미한 차이가 존재한다.
# 위 주장에 대해 누가 맞는지 가설 검정을 통해 판정한다. t-test. anova를 사용.

from scipy import stats

# 독립표본 t검정 (t-test)
t_stat, p_value_t = stats.ttest_ind(class1, class2, equal_var=False)    # Welchi's test
print(f't-통계값 : {t_stat:.4f}')
print(f'p값 : {p_value_t:.4f}')

if p_value_t < 0.05:
    print('유의확률(p)가 유의수준(α, 95% 신뢰구간에서 0.05)보다 작으므로 두 반의 평균에는 유의미한 차이가 있다.')

else:
    print('유의확률(p)가 유의수준(α, 95% 신뢰구간에서 0.05)보다 크므로 두 반의 평균에는 유의미한 차이가 있다고 볼 수 없다.')