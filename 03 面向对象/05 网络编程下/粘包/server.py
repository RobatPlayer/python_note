'''服务端'''
import os
import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

coon, addr = sock.accept()  # 等待连接

# 固定读取四字节
header = coon.recv(4)  # 这里也可以判断一下是否完全读取4个字节
data_len = struct.unpack('i', header)[0]  # 转换之后是个元组，取第一个值就是总长度
# file_size=os.stat(file_path).st_size  这个是获取文件大小
has_rec_len = 0  # 定义已经读取的长度
data = b''  # 创建一个空字节的对象，用于写入传递的数据
while True:
    length = data_len - has_rec_len  # 获取剩余的长度
    if length > 1024:
        lent = 1024  # 如果剩余长度大于1024，那么就最多读取1024
    else:
        lent = length  # 如果小于1024就读取本身
    chunk = coon.recv(lent)
    data += chunk  # 写入读取的数据
    has_rec_len += len(chunk)  # 写入已经读取的长度
    if has_rec_len == data_len:  # 判断是否完全读取
        break
print(data.decode('utf-8'))
coon.close()
sock.close()
