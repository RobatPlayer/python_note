'''客户端'''
import socket
import struct

client = socket.socket()
client.connect(('127.0.0.1', 8001))

# 第一条数据
data1 = '杜孝先是我放的'.encode('utf-8')
header1 = struct.pack('i', len(data1))  # 将数据打包，并计算数据的长度，转换成字节
client.sendall(header1)  # 先发送数据长度
client.sendall(data1)  # 在发送数据

# 第二条数据
data2 = '鸡汤来咯'.encode('utf-8')
header2 = struct.pack('i', len(data2))
client.sendall(header2)
client.sendall(data2)

client.close()
