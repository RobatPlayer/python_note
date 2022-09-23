import socket

client = socket.socket()
client.setblocking(False)
client.connect(('127.0.0.1', 8001))
client.sendall('hello'.encode('utf-8'))
reply = client.recv(1024)  # 非阻塞
print(reply.decode('utf-8'))
client.close()
