# client 
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.13', 8888))
clientsock.send("안녕 서버".encode())

clientsock.close()

# server 실행 중 - client 실행 - 서버는 메세지를 수신한 후 종료됨.
