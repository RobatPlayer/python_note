import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setblocking(False)  # 如果加上这个代码，下面的阻塞就变成了非阻塞

sock.bind(('127.0.0.1', 8001))
sock.listen(5)
try:
    # 非阻塞 :BlockingIOError,想要获取客户端的连接，没有连接所以会报错
    conn, addr = sock.accept()
except BlockingIOError as e:
    print(e)  # 非阻塞可以在没有客户端连接时做一些别的操作

client_data = conn.recv(1024)  # 非阻塞

print(client_data.decode('utf-8'))
conn.sendall('hello world'.encode('utf-8'))
conn.close()
sock.close()
