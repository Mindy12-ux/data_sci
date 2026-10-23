# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
# 예제파일 : MariaDB의 jikwon table 
# jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
# jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
# 조건 : NA가 있는 행은 제외한다.

import pymysql
import numpy as np
import pandas as pd
import csv
import scipy.stats as stats

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

# 데이터프레임 가져오기
try:
    conn = pymysql.connect(**config)
    sql = """select jikwonno, jikwonname, jikwonpay, jikwonjik from jikwon"""

    df_raw = pd.read_sql(con=conn, sql=sql)
    df_raw.columns =['사번', '직원이름', '연봉', '직급']
    print(df_raw)

    df = df_raw[['연봉', '직급']]
    print(df)

except Exception as e:
    print('처리 오류 : ', e)

# 데이터 범주화

jikwonjik = []

for i in df['직급']:
    if i == '이사':
        jikwonjik.append(1)
    elif i == '부장':
        jikwonjik.append(2)
    elif i == '과장':
        jikwonjik.append(3)
    elif i == '대리':
        jikwonjik.append(4)
    else:
        jikwonjik.append(5)

# print(jikwonjik)

jikwonpay = [] 

for i in df['연봉']:
    if 1000 <= int(i) <= 2999:
        jikwonpay.append(1)
    elif 3000 <= int(i) <= 4999:
        jikwonpay.append(2)
    elif 5000 <= int(i) <= 6999:
        jikwonpay.append(3)
    elif 7000 <= int(i) :
        jikwonpay.append(4) 

# print(jikwonpay)

df = pd.DataFrame(list(zip(jikwonjik, jikwonpay)), columns=['직급', '연봉'])
# print(df)

# crosstab 만들기
ctab = pd.crosstab(df['연봉'], df['직급'])
ctab.columns = ['이사', '부장', '과장', '대리', '사원']
ctab.index = [1, 2, 3, 4]
# print(ctab)

# 가설
# 귀무 가설 : 직급과 연봉에는 유의미한 상관관계가 없다.
# 대립 가설 : 직급과 연봉에는 유의미한 상관관계가 있다.

# chi2 검증 
chi2, pv, df, exp = stats.chi2_contingency(ctab)
print(f'검정 통계치 : {chi2:.4f}')
print(f'p-value : {pv:.4f}')
print(f'자유도 : {df}')
print(f'기대값 : \n{exp}')

# jik = {"이사":1, "부장 ":2, "과장":3, "대리":4,"사원":5}
# df['jik'] = df['jikwonjik'].map(jik)  // 인터넷에 검색해서 나오는 applymap과는 다른 기능. 딕셔너리를 받아 매칭하는 건 Series.map(즉 df['컬럼'].map(...))의 기능이다.

# def get_pay(pay):
#     if 1000 <= pay <=2999:
#         return 1
#     elif 3000 <= pay <=4999:
#             return 2
#     elif 5000 <= pay <=6999:
#             return 3
#     else:
#         return 4

# df['pay'] = df['jikwonpay'].apply(get_pay)
