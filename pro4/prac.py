# 서버 서비스는 계속 유지
from socket import *
import sys

# HOST = '192.168.0.13'  # '127.0.0.1', 'local host'
HOST = '192.168.0.13'  # 사용 가능한 주소 모두 가능
PORT = 77
serversoc = socket(AF_INET, SOCK_STREAM)

try:
    serversoc.bind((HOST, PORT))
    serversoc.listen(5)
    print('서버(무한 루핑) 서비스 중 ... ')

    while True:
        info = serversoc.accept() 
        print('client info : ', info)
        #print(info.recv(1024).decode())     # 수신 메세지 출력
        # 메세지 송신 to client



except Exception as e:
    print('에러 : ', e)
    sys.exit()

finally:
    info.close()
    serversoc.close()

