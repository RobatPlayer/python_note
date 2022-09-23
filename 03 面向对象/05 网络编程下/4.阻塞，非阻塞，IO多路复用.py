'''
try:
    # 非阻塞 :BlockingIOError,想要获取客户端的连接，没有连接所以会报错
    conn, addr = sock.accept()
except BlockingIOError as e:
    print(e)  # 非阻塞可以在没有客户端连接时做一些别的操作
'''
'''因为不知道什么时候会有客户端连接，所以出现了IO多路复用
1.可以利用时间执行别的代码
2.可以让服务端支持多个客户端连接'''
import select

r, w, e = select.select([], [], [], 0.1)
# r,w,e分别代表三个列表，r代表捕获服务端返回的数据，w代表捕获客户端输入的数据，e代表异常

# 补充 socket+非阻塞+IO多路复用(IO操作对象都可以监控，包括文件)
