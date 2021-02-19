# author:丑牛
# datetime:2020/10/27 9:29
from socket import *


client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
client.send('hello'.encode('utf-8'))
data = client.recv(1024)
print(data.decode('utf-8'))
client.close()