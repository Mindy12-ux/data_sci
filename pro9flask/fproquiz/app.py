from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
from markupsafe import escape
# 웹에 출력되는 입력값의 특수 문자(예:<,>,&,")를 안전한 HTML 엔티티(예:&lt;,&gt;)로 변환하여 XSS 공격 방지

# 직원번호, 직원명, 부서명, 부서전화, 연봉, 직급 자료 읽어 출력

app = Flask(__name__)

config = {
    'host':'127.0.0.1', 'user':'root', 'password':'123', 'database':'test',
    'port':3306, 'charset':'utf8mb4'
}

def get_connection():
    return pymysql.connect(**config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dbshow")
def dbshow():
    """ 1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)

    : 부서번호, 직원명 순으로 오름 차순 정렬 """

    sql = """
        select jikwonno as 사번, jikwonname as 직원명, busername as 부서명, jikwonjik as 직급, jikwongen as 성별, jikwonpay as 연봉, year(now()) - year(jikwonibsail) as 근무년수
        from jikwon inner join buser on jikwon.busernum = buser.buserno
        order  by  buserno asc, jikwonno asc;
    """

    # sql 실행
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description]

    df = pd.DataFrame(rows, columns=cols)

    if not df.empty:
        jikwondata = df[['사번','직원명','부서명','직급','성별','연봉', '근무년수']].to_html(index=False)
            
    else:
        jikwondata = "직원 정보가 없어요"

    # 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.
    if not df.empty:
        stats_df = (
            df.groupby(['부서명', '직급'])['연봉'].agg(연봉합='sum', 연봉평균='mean')
            .round(2)
            .reset_index()
        )
        statsdata = stats_df.to_html(index=False)

    else:
        statsdata = "통계 대상 자료가 없어요"

    # 성별, 직급별 빈도표를 출력하시오.
    if not df.empty:
        crosstab_df = (
            pd.crosstab(index=df['성별'],columns=df['직급'])
        )
        crosstabdata = crosstab_df.to_html(index=False)

    else:
        crosstabdata = "통계 대상 자료가 없어요"    

    # 부서별 최고 연봉자 출력 : 부서명별로 가장 연봉이 높은 직원 1명씩 출력
    if not df.empty:
        maxpay_df = (
            df.groupby('부서명')['연봉'].agg(최대연봉='max').reset_index()
        )
        maxpaydata = maxpay_df.to_html(index=False)
    
    else:
        maxpaydata = "통계 대상 자료가 없어요" 

    return render_template("dbshow.html", jikwondata=jikwondata, statsdata=statsdata, crosstabdata=crosstabdata, maxpaydata=maxpaydata)


if __name__ == '__main__':
    app.run(debug=True)