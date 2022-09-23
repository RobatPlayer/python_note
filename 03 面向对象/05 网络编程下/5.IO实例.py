# ################### socket服务端 ###################
import select
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)  # 加上就变为了非阻塞
server.bind(('127.0.0.1', 8001))
server.listen(5)

inputs = [server, ]  # socket对象列表 -> [server, 第一个客户端连接conn ]

while True:
    # 当 参数1 序列中的socket对象发生可读时（accetp和read），则获取发生变化的对象并添加到 r列表中。
    # r = []
    # r = [server,]
    # r = [第一个客户端连接conn,]
    # r = [server,]
    # r = [第一个客户端连接conn，第二个客户端连接conn]
    # r = [第二个客户端连接conn,]
    r, w, e = select.select(inputs, [], [], 0.05)
    for sock in r:
        # server
        if sock == server:
            conn, addr = sock.accept()  # 接收新连接。
            print("有新连接")
            # conn.sendall()
            # conn.recv("xx")
            inputs.append(conn)
        else:
            data = sock.recv(1024)
            if data:
                print("收到消息：", data)
            else:
                print("关闭连接")
                inputs.remove(sock)
    # 干点其他事 20s

# 优点：
# 1. 干点那其他的事。
# 2. 让服务端支持多个客户端同时来连接。


# ################### socket客户端 ###################
import socket
import select
import uuid
import os

client_list = []  # socket对象列表

for i in range(5):
    client = socket.socket()
    client.setblocking(False)

    try:
        # 连接百度，虽然有异常BlockingIOError，但向还是正常发送连接的请求
        client.connect(('47.98.134.86', 80))
    except BlockingIOError as e:
        pass

    client_list.append(client)

recv_list = []  # 放已连接成功，且已经把下载图片的请求发过去的socket
while True:
    # w = [第一个socket对象,]
    # r = [socket对象,]
    r, w, e = select.select(recv_list, client_list, [], 0.1)
    for sock in w:
        # 连接成功，发送数据
        # 下载图片的请求
        sock.sendall(b"GET /nginx-logo.png HTTP/1.1\r\nHost:47.98.134.86\r\n\r\n")
        recv_list.append(sock)
        client_list.remove(sock)

    for sock in r:
        # 数据发送成功后，接收的返回值（图片）并写入到本地文件中
        data = sock.recv(8196)
        content = data.split(b'\r\n\r\n')[-1]
        random_file_name = "{}.png".format(str(uuid.uuid4()))
        with open(os.path.join("images", random_file_name), mode='wb') as f:
            f.write(content)
        recv_list.remove(sock)

    if not recv_list and not client_list:
        break

"""
优点：
	1. 可以伪造除并发的现象。
"""
