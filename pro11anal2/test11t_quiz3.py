# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

# 귀무가설 : 총무부와 영업부 직원의 연봉의 평균에는 차이가 존재하지 않는다. 
# 대립가설 : 총무부와 영업부 직원의 연봉의 평균에는 차이가 존재한다.

import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

sql = """
    select jikwonno, busername, jikwonpay from jikwon 
    inner join buser on jikwon.busernum = buser.buserno 
    where busername in ('영업부','총무부'); 
"""

try:

    conn = pymysql.connect(**config)
    data = pd.read_sql(sql, conn)

    # print(data)

    buser3 = data[data['busername'] == '영업부']
    print(buser3)

    buser1 = np.array(data.loc[data['busername'] == '영업부', data.columns[2]])
    buser2 = np.array(data.loc[data['busername'] == '총무부', data.columns[2]])
    # print(buser1)
    # print(buser2)
    
    # buser1 = data.loc[data['busername'] == '영업부', data.columns[2]]

finally:
    conn.close()