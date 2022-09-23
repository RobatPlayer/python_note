import socket

# 在终端输入ipconfig可以获得本机ip  172.24.173.20
# 127.0.0.1 表示本机ip不论在哪个路由器下都是可以的
'''服务端,放在云服务器中，有固定的IP'''
# 1.监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 配置
sock.bind(('123.206.15.88', 8001))  # 固定IP以及端口
sock.listen(5)  # 最多支持5人排队，超出直接请求错误
while True:  # 因为要服务端要一直被请求，所有有无限循环
    # addr 是客户端的地址，conn是客户端和服务端创建的连接
    conn, addr = sock.accept()  # 2.等待用户来连接，没有连接就会一直等，下面的代码都无法执行（阻塞）

    client_data = conn.recv(1024)  # 3.等待接收客户端发来的数据，客户端不发消息这段代码也会卡住
    print(client_data.decode('utf-8'))  # 接收到的是字节类型

    conn.sendall('hello world'.encode('utf-8'))  # 4.转化为字节类型，给客户端回消息

    conn.close()  # 5.之后关闭连接
    '''可以设置一个时间自动跳出循环'''
    break

sock.close()  # 6.停止服务端程序

'''客户端，一定要先运行服务端，等待客户端连接'''
# 1.向指定IP发请求
client = socket.socket()  # 创建client对象
client.connect(('123.206.15.88', 8001))  # 向服务端发起连接，连接不成功会等待（阻塞）

client.sendall('hello'.encode('utf-8'))  # 2.发送消息

reply = client.recv(1024)  # 3.等待消息的回复（阻塞）
print(reply.decode('utf-8'))

client.close()  # 4.关闭连接
