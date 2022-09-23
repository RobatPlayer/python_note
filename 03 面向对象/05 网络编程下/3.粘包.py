# 对于发送者执行sendall会将数据先发送至自己的网卡的缓冲区，再由缓冲区将数据放松到服务端的缓冲区
# 对于接受者执行recv会从缓冲区获取数据
# 如果使用send发，缓冲区没有内存了只会把一部分数据写入缓冲区，数据就发不全

'''
因为缓冲区的数据不能及时获取，所以导致服务端会出现粘包的现象，即一下子获取多条数据
如何避免粘包的情况发生：可以先约定数据的长度再发送，就像下载文件一样
'''

import struct  # 这个是专门打包的模块
import socket

v1 = struct.pack('i', 199)  # 将数值转换成固定的四个字节  i是固定的，表示int类型
print(v1)

v2 = struct.unpack('i', b'\xc7\x00\x00\x00')[0]  # 将四个字节转换成整数
print(v2)

'''服务端'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

coon, addr = sock.accept()  # 等待连接

# 固定读取四字节
header = coon.recv(4)
data_len = struct.unpack('i', header)[0]  # 转换之后是个元组，取第一个值就是总长度
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

'''客户端'''
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
