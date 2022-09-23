'''客户端，一定要先运行服务端，等待客户端连接'''
import os
import time
import socket

# 向指定IP发请求
client = socket.socket()  # 创建client对象
client.connect(('127.0.0.1', 8001))  # 向服务端发起连接，连接不成功会等待（阻塞）

file_path = input('请输入上传文件的路径：')

# 先发送文件大小
file_size = os.stat(file_path).st_size  # 获取文件大小
client.sendall(str(file_size).encode('utf-8'))  # 发送消息

print('准备')
time.sleep(2)
print('开始上传')
file_object = open(file_path, mode='rb')
read_size = 0
while True:
    chunk = file_object.read(1024)  # 每次读取1024字节
    client.sendall(chunk)
    read_size += len(chunk)
    if read_size == file_size:
        break
client.close()  # 关闭连接
