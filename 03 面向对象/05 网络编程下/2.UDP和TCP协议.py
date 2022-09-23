'''
UDP 和 TCP协议都是在传输层定义的

UDP协议：服务端和客户端不需要先创建连接，而是客户端直接向服务端发送数据，服务端能获取就获取到，获取不到就丢弃了
UDP不提供可靠性，一般用于视频通话（网络断断续续，丢包），语音通话，实时游戏画面等。特点是快

TCP协议：先创建连接，在发送数据，发送不成功会重新发送。常见网站，手机app数据获取等
'''

# UDP协议代码
import socket

'''服务端'''
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 这个第二个参数和TCP协议不一样
server.bind(('127.0.0.1', 8001))
while True:
    data, (host, port) = server.recvfrom(1024)  # 获取客户端发送的内容
    print(data, host, port)
    server.sendto('好的'.encode('utf-8'), (host, port))  # 返回给客户端的内容
    break

# 客户端
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    text = input('请输入要发送的内容')
    if text.lower() == 'q':
        break
    client.sendto(text.encode('utf-8'), ('127.0.0.1', 8001))  # 首先发送内容
    data, (host, port) = client.recvfrom(1024)  # 获取服务端返回的内容
    print(data.decode('utf-8'))

client.close()

'''
TCP协议三次握手和四次挥手
三次握手：客户端先发送连接请求，服务端返回请求，客户端还要回复一次，通过三次数据传递才能确定服务端和客户端都能收发消息
四次挥手：客户端先发送关闭请求，服务端返回稍等请求，又返回关闭请求，客户端再回复一次
'''
