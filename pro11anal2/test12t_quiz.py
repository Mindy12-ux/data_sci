# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 수집된 자료 :  
#   중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
#   기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

# 귀무 가설 : 학급의 학업능력에는 변화가 없다.
# 대립 가설 : 학급의 학업능력에는 변화가 있다.

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

mid = np.array([80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80])
final = np.array([90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95])

# 정규성 검정
diff = final - mid
print("정규성 검증 : ", stats.shapiro(diff).pvalue) # 0.3010927070

result = stats.ttest_rel(mid, final)
print(f't 통계량 : {result.statistic:.5f}') # -2.62811
print(f'p-value : {result.pvalue:.5f}')    # 0.02349

# 해석 : pvalue 0.02349 < 0.05 이므로 귀무 가설이 기각된다.
# 결론 : 학급의 학업능력에는 변화가 있다.