# client 
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.13', 7799))
clientsock.send("안녕 반가워".encode())
print('수신자료 : ', clientsock.recv(1024).decode())

clientsock.close()

# server 실행 중 - client 실행 - 서버는 메세지를 수신한 후 종료됨.