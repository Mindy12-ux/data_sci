# 원격 데이터베이스와 연동 프로그래밍
# MariaDB : 
# 준비 1) IP(네트워크에서 컴퓨터나 장치를 구분하기 위한 규약) 주소가 필요하다 
# 준비 2) 연결용 Driver file (module) 필요

# pip install mysqlclient

import MySQLdb

# 딕셔너리로 저장

"""
매핑 방법 1)

conn = MySQLdb.connect(     # db 연결담당 객체 생성
    host = '127.0.0.1', # 192.168.0.13, localhost
    user = 'root',
    password = '123',
    database = 'test',
    port = 3306     # MariaDB / MySQL 서버가 기본적으로 사용하는 포트 번호
)
"""

# 아예 연결 정보를 딕셔너리로 저장
# 매핑 방법 2)
"""
config_data = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}
"""

# 매핑 방법 3)
# 보안을 위해 딕셔너리만 json 파일로 저장해놓을 수 있다.
# 별도로 저장된 json 파일 읽기
# json 파일에 저장된 내용은 큰따옴표만 사용할 것.
import json

with open('dbconnect.json', mode = 'r', encoding='utf-8') as f:
    config_data = json.load(f)


def myFunc():
    try:


        conn = MySQLdb.connect(**config_data)   # ** : 딕셔너리 형태로 입력
        # conn.autocommit(True)  # 자동 커밋
        # conn.autocommit(False) # 수동 커밋 : 기본값
        cur = conn.cursor()

        # 자료 추가 방법 1)
        # isql = "insert into sangdata(code, sang, su, dan) values(5, '마스크', 5, '3000')" # 숫자는 따옴표를 둘러도 되고 안둘러도 됨.
        # cur.execute(isql)
        # conn.commit()

        # 자료 추가 방법 2)
        """
        isql = "insert into sangdata values(%s, %s, %s, %s)"    # %s : 문자열을 의미, sql문은 전체가 문자열이므로 이렇게 처리함.
        # ins_data = (6, '커피', 10, 5000)    # tuple type
        ins_data = 6, '커피', 10, 5000    # tuple type

        cur.execute(isql, ins_data)
        conn.commit()   # 원격 DB에 변경사항이 저장됨
        """

        # 자료 수정
        """
        usql = "update sangdata set sang=%s, su = %s, dan = %s where code = %s"
        up_data = '물티슈', 3, 1000, 5  # 튜플이므로 괄호를 두르지 않아도 됨.
        cur.execute(usql, up_data)
        conn.commit()
        """

        """
        usql = "update sangdata set sang=%s, su = %s, dan = %s where code = %s"
        up_data = '콜라', 11, 3000, 6  # 튜플이므로 괄호를 두르지 않아도 됨.
        # insert, updatem delete의 반환값 받기, 성공하면 성공갯수, 실패하면 0을 반환
        cou = cur.execute(usql, up_data)
        print("수정 개수 :", cou)
        conn.commit()
        """

        # 자료 삭제
        code = '6'; 
        # dsql = "delete from sangdata where code=" + code 
        # print(dsql)
        # 참고 : secure coding 가이드라인에 맞게 프로그래밍 해야 한다. / sql injection
        # 문자열 더하기로 프로그램을 짜면 sql injection 해킹의 대상이 될 수 있으므로 위험함.

        # dsql = "delete from sangdata where code='{0}'".format(code) 추천 방법 1

        dsql = "delete from sangdata where code=%s" # 추천 방법 2 : 권장방법
        # cur.execute(dsql, (code,)) # 반드시 code를 튜플로 줘야 함
        cou = cur.execute(dsql, (code,)) # 삭제 후 반환값 얻기
        if cou != 0:
            print('삭제 성공')
        else:
            print('삭제 실패')

        conn.commit()

        
        # 자료 읽기
        # sql = "select * from sangdata"
        sql = " select code, sang, su, dan from sangdata"
        cur.execute(sql)

        # 튜플에서 자료 꺼내서 읽는 여러 가지 방법
        for data in cur.fetchall():
            print("%s %s %s %s"%data)
        print()

        cur.execute(sql)
        for data in cur:
            print(data[0], data[1], data[2], data[3])
        print()

        for code, sang, su, dan in cur:     # 이때의 code, sang, su, dan은 칼럼명이 아닌 변수명임. 반드시 칼럼명과 일치하지 않아도 됨.
            print(code, sang, su, dan)
        print()
            
        for a, b, 수량, 단가 in cur:
            print(a, b, 수량, 단가 * 1000)

        
    except Exception as e:
        print('처리 오류 :', e)
        conn.rollback()

    finally:
        conn.close()
        

if __name__ == '__main__':  # 해당 모듈이 메인 모듈임을 보여주기 위한 코드. 없어도 실행은 됨
    myFunc()



