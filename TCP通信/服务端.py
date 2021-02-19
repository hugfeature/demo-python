# author:丑牛
# datetime:2020/10/27 9:24
from socket import *


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
conn, client_addr = server.accept()
data = conn.recv(1024)
conn.send(data.upper())
conn.close()