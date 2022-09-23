# 1.简述二层交换机 & 路由器 & 三层交换机的作用。
'''
二层交换机能维护接口和地址
路由器可以叫交换机连接在一起，从而连接到另一个二层交换机
三层交换机继承了二层交换机和路由器的功能
'''
# 2.简述常见词：IP、子网掩码、DHCP、公网IP、端口、域名的作用。
'''
IP：IP是一个32位的二进制，方便记忆将其分为4组，每组8位,转换为十进制最大为255.255.255.255，又分为网络IP和主机IP
子网掩码：被子网掩码掩盖的IP是网络IP，二进制数都是1，剩余的是主机IP,
DHCP：提供连接到不同的路由器会自动设置IP、子网掩码、网关的功能
端口：IP后面加端口可以访问指定的网页
域名：由于IP和端口太难记忆，域名可以绑定IP对应的端口，方便记忆
'''

# 3.实现远程用户认证系统。


# 服务端：
# 1.客户端连接上服务端，返回欢迎使用xx系统信息。
# 2.等待客户端发送用户名和密码进行校验（用户名和密码在文件中）
# 3.登录失败，返回错误信息。
# 4.登录成功，返回成功提示的内容。

import socket

lst = [{'用户名': '10010', '密码': '123456'}, {'用户名': '10086', '密码': '1111'}]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 配置，创建sock对象
sock.bind(('127.0.0.1', 8001))  # 固定IP以及端口
sock.listen(5)
conn, addr = sock.accept()  # 等待用户端连接，接收连接
conn.sendall('欢迎使用登录系统'.encode('utf-8'))  # 连接成功返回提示信息
client_info = conn.recv(1024)  # 接收客户端发来的信息
client_info = client_info.decode('utf-8')  # 将二进制转换为utf-8
print(client_info)
if not client_info:
    print('系统关闭')
    conn.close()
else:
    for i in lst:
        if eval(client_info) == i:  # eval()将字符串转换成字典
            conn.sendall('登录成功'.encode('utf-8'))
            break
    else:
        conn.sendall('账号或密码输入错误'.encode('utf-8'))

    conn.close()
