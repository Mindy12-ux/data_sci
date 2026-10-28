# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

# 귀무 가설 : 부서별 연봉의 평균에 차이가 없다.
# 대립 가설 : 부서별 연봉의 평균에 차이가 있다.


import pymysql
import numpy as np
import pandas as pd
import csv
from scipy import stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

sql = """
    select jikwonno, busername, jikwonpay from jikwon inner join buser on jikwon.busernum = buser.buserno
    where jikwonpay is not null; 
"""

try:
    conn = pymysql.connect(**config)
    data = pd.read_sql(sql, conn)
    print(data)

finally:
    conn.close()

# 부서별로 구분
x1 = np.array(data.loc[data["busername"] == '총무부', "jikwonpay"])
x2 = np.array(data.loc[data["busername"] == '영업부', "jikwonpay"])
x3 = np.array(data.loc[data["busername"] == '전산부', "jikwonpay"])
x4 = np.array(data.loc[data["busername"] == '관리부', "jikwonpay"])
print(x1.mean())    # 5414.28
print(x2.mean())    # 4908.33
print(x3.mean())    # 5328.57
print(x4.mean())    # 6262.5
print()

# 정규성 검정
print(stats.shapiro(x1).pvalue) # 0.026044, 정규성 X
print(stats.shapiro(x2).pvalue) # 0.025608, 정규성 X
print(stats.shapiro(x3).pvalue) # 0.419407, 정규성 O
print(stats.shapiro(x4).pvalue) # 0.907802, 정규성 O
print()

# 등분산성 검정
print(stats.levene(x1, x2, x3, x4).pvalue)  # 0.7980753, 등분산성 만족
print()

# 비모수 검정 수행 : 크루스칼-왈리스검정(kruskal-wallis test)
print(stats.kruskal(x1, x2, x3, x4))
# statistic=1.671252, pvalue=0.64334387
# 해석 : pvalue 0.64334387 > 0.05 이므로 귀무가설을 수용한다.
# 결론 : 부서별 연봉의 평균에 차이가 없다.

print('\n사후검정')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=data['jikwonpay'], groups=data['busername'])
print(tukResult)  

# 시각화
tukResult.plot_simultaneous(xlabel='연봉 평균', ylabel='부서명')
plt.show()