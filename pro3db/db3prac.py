import MySQLdb
import json

from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'host':os.getenv('DB_HOST'),
    'user':os.getenv("DB_USER"),
    'password':os.getenv('DB_PASSWORD'),
    'database':os.getenv('DB_NAME'),
    'port':int(os.getenv('DB_PORT')),
    'charset':os.getenv('DB_CHARSET')
}

# port는 숫자 처리, config에는 데이터베이스의 정보가 담김, 데이터베이스와 연동하기 위한 것



def LoginFunc():
    conn = None

    try:
        conn = MySQLdb.connect(**config)  # 데이터베이스와 connection
        cursor = conn.cursor()
        jikwon_no = input('직원번호 : ')
        jikwon_name = input('직원이름 : ')
        if jikwon_no=='' or jikwon_name =='':
            print('로그인 정보를 입력하세요')
            return

        sql = '''
            select 
            j.jikwonno as 직원번호,j.jikwonname as 직원명,
            b.busername as 부서명,j.jikwonjik as 직급,j.jikwongen as 성별
            from jikwon j
            left outer join buser b on j.busernum = b.buserno
            where jikwonno=%s and jikwonname=%s
'''

        # sql실행
        cursor.execute(sql,(jikwon_no, jikwon_name))

        # cursor.execute 메서도는 데이터베이스에 sql쿼리나 명령어를 전달하고 실행하는 함수이다.

        data = cursor.fetchone()

        if data:
            print('로그인 성공')
            print('직원번호 : ', data[0])
            print('직원이름 : ', data[1])
            print('부서명 : ', data[2])
            print('직급 : ', data[3])
            print('성별 : ', data[4])

        else:
            print('로그인 실패 : 입력자료를 확인하세요')

    except Exception as e:
        print('에러 : ', e)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    LoginFunc()










