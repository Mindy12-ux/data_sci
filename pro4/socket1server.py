# 1회용 서버
from socket import *

# 1) socket 객체 생성
serversock = socket(AF_INET, SOCK_STREAM)   # socket(소켓종류, 소켓유형)

# 2) socket을 이용해 특정 컴퓨터와 바인딩 (서버의 IP와 Port를 연결해줘야 함)
serversock.bind(('192.168.0.13', 8888))

# 3) 연결 대기 상태로 전환  / 리스너 설정 (연결 정보수 최대 5개까지 허용)
serversock.listen(5)
print('서버 서비스 중 ... ')

# 4) 클라이언트의 접속 대기  / 수동적으로 연결을 받음
conn, addr = serversock.accept()
print('client addr : ', addr)

# 5) 클라이언트가 보낸 데이터 수신
msg = conn.recv(1024).decode()      # 1KB 단위로 수신된 데이터를 문자열로 변환 
print('from client message : ', msg)

# 6) 연결 종료
conn.close()
serversock.close()


