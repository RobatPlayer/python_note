# 客户端：
# 1.运行程序，连接服务端并获取服务端发送的欢迎使用xx系统信息。
# 2.输入用户名和密码，并将用户名和密码发送到服务端去校验。
# 3.登录失败，重试（Q退出）。
# 4.登录成功，进入系统，提示登录成功

import socket

client = socket.socket()  # 创建client对象
client.connect(('127.0.0.1', 8001))  # 连接服务器
reply = client.recv(1024)  # 接收服务端返回的消息
print(reply.decode('utf-8'))  # 转换成utf-8
while True:
    user = input('请输入用户名(q/Q退出)：')
    if user.upper() == 'Q':
        break
    pwd = input('请输入密码：')
    dic = {'用户名': user, '密码': pwd}
    client.sendall(str(dic).encode('utf-8'))
    result = client.recv(1024)  # 发送请求
    if result.decode('utf-8') == '登录成功':
        print('登陆成功，进入系统')
        break
    else:
        print('登录失败请重试')
        continue

client.close()
