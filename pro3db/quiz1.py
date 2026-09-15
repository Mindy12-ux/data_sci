# --- DB(RDBMS) 연동 관련 -----------
# 문1) 부서명을 입력해 해당 부서에 근무하는 직원 출력
# 부서명 입력 : _______
# 직원번호 직원명 부서번호 부서전화 직급 성별
#     1   홍길동  10    111-1111     이사 남 
# ...


import MySQLdb
from dotenv import load_datenv
import os

load_dotenv()

config = {
    'host':os.getenv("DB_HOST"),
    'user':os.getenv("DB_USER"),
    'password':os.getenv('DB_PASSWORD'),
    'database':os.getenv('DB_NAME'),
    'port':int(os.getenv('DB_PORT')),
    'charset':os.getenv('DB_CHARSET')
}

def buserFunc():
    conn = None

    try:
        conn = MySQLdb.connect(**config)
        cur = conn.cursor()

        sql = '''
                
'''



    except Exception as e:
        print('에러 : ', e)

    finally:
        if  conn:
            conn.close()

if __name__=="__main__":
    buserFunc()