# SQLite : 개인용 DB, 파이썬에 기본 내장. 경량 DBMS
# 서버를 운영하지 않고 시스템 내에서 별도의 자원을 사용할 필요가 없다.

import sqlite3

print(sqlite3.sqlite_version)
print("--------------------")
# conn = sqlite3.connect('exam.db')   # 파일에 데이터 보관
conn = sqlite3.connect(':memory:')  # RAM에서만 작업. 휘발성
# conn : db 연결 담당

try:
    cur = conn.cursor() # SQL 처리를 위한 객체 생성, sql 실행을 담당

    # 테이블 생성
    cur.execute("create table if not exists friends(name text, phone text, addr text)")

    # 자료 입력
    cur.execute("insert into friends values('홍길동', '111-1111', '서초1동')")
    cur.execute("insert into friends values(?, ?, ?)", ('이기자', '111-2222', '서초2동'))
    # ?를 적어놓고 외부에서 들어오는 값과 매핑시켜주는 방법을 더 많이 이용한다. 위 예제에서는 튜블을 사용함.
    inputdatas = ('신기해', '111-1234','서초3동')
    cur.execute("insert into friends values(?,?,?)", inputdatas)
    inputdatas2 = (('신기한', '111-3333','역삼1동'), ('신기루', '111-4444','역삼2동'))
    cur.executemany("insert into friends values(?,?,?)", inputdatas2)

    conn.commit()

    # 자료 보기

except Exception as e:
    print("err : ", e)
    conn.rollback()
finally:        # 에러 여부와 관계없이 반드시 수행되는 문장
    conn.close()