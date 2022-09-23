'''服务端,放在云服务器中，有固定的IP'''
import socket

# 监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 配置
sock.bind(('127.0.0.1', 8001))  # 固定IP以及端口
sock.listen(5)  # 最多支持5人排队，超出直接请求错误
conn, addr = sock.accept()  # addr 是客户端的地址，conn是客户端和服务端创建的连接

# 接收文件大小
client_data = conn.recv(1024)  # 等待接收客户端发来的数据，客户端不发消息这段代码也会卡住
total_file_size = int(client_data.decode('utf-8'))

# 接收文件内容
file_object = open('xxx.png', mode='wb')
recv_size = 0  # 已接收文件大小
while True:
    client_data = conn.recv(1024)  # 每次最多接收1024字节，不是固定的
    file_object.write(client_data)
    file_object.flush()
    recv_size += len(client_data)

    # 上传完成
    if recv_size == total_file_size:
        break

conn.close()  # 之后关闭连接
sock.close()  # 停止服务端程序
