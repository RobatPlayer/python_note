'''服务端,放在云服务器中，有固定的IP'''
import socket
# 1.监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 配置
sock.bind(('127.0.0.1', 8001))  # 固定IP以及端口
sock.listen(5)  # 最多支持5人排队，超出直接请求错误
while True:  # 因为要服务端要一直被请求，所有有无限循环
    # addr 是客户端的地址，conn是客户端和服务端创建的连接
    conn, addr = sock.accept()  # 2.等待用户来连接，没有连接就会一直等，下面的代码都无法执行（阻塞）

    client_data = conn.recv(1024)  # 3.等待接收客户端发来的数据，客户端不发消息这段代码也会卡住
    print(client_data.decode('utf-8'))  # 接收到的是字节类型

    conn.sendall('hello world'.encode('utf-8'))  # 4.转化为字节类型，给客户端回消息

    conn.close()  # 5.之后关闭连接


sock.close()  # 6.停止服务端程序