'''客户端，一定要先运行服务端，等待客户端连接'''
import socket
# 1.向指定IP发请求
client = socket.socket()  # 创建client对象
client.connect(('127.0.0.1', 8001))  # 向服务端发起连接，连接不成功会等待（阻塞）

client.sendall('hello'.encode('utf-8'))  # 2.发送消息

reply = client.recv(1024)  # 3.等待消息的回复（阻塞）
print(reply.decode('utf-8'))

client.close()  # 4.关闭连接