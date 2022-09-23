# 请基于TCP协议实现一个网盘系统，包含客户端、服务端，各自需求如下：

# - 客户端
# 1.用户注册，注册成功之后，在服务端的指定目录下为此用户创建一个文件夹，该文件夹下以后存储当前用户的数据（类似于网盘）。
# 2.用户登录
# 3.查看网盘目录下的所有文件（一级即可），ls命令
# 4.上传文件，如果网盘已存在则重新上传（覆盖）。
# 5.下载文件（进度条）
# 先判断要下载本地路径中是否存在该文件。不存在，直接下载；存在，则让用户选择是否续传（继续下载）。续传，在上次的基础上继续下载。
# 不续传，从头开始下载。

# - 服务端
# 1.支持注册，并为用户初始化相关目录。
# 2.注册成功之后，将所有用户信息存储到特定的Excel文件中
# 3.支持登录
# 4.支持查看当前用户网盘目录下的所有文件。
# 5.支持上传
# 6.支持下载
import os
import time
import hashlib
from datetime import datetime
from openpyxl import workbook
from openpyxl.styles import Alignment, Border, Side, Font, PatternFill, GradientFill
from openpyxl import load_workbook


def download(client, num):
    '''这是下载文件的函数'''
    while True:
        data = accep(client=client)  # 获取服务端发来的文件名请求
        name = input(data)  # 文件名
        path = os.path.dirname(os.path.abspath(__file__))
        network_disk = os.path.join(path, '网盘', f'{num}的网盘')  # 拼接路径
        data = os.listdir(network_disk)  # 得到所有的文件
        if name.lower() == 'q':
            send(client=client, text=name)
            break
        if name not in data:
            print('没有找到该文件')
            send(client=client, text='None')
            continue
        send(client=client, text=name)  # 将文件名发给服务端

        has_read_size = 0
        byte_lst = []
        while has_read_size < 4:  # 如果已读的数据长度小于4
            chunk = client.recv(4 - has_read_size)  # 那么就读取剩余的数据长度
            has_read_size += len(chunk)  # 改变变量
            byte_lst.append(chunk)  # 将已经读取的数据放入字节列表中
        header = b''.join(byte_lst)  # 将列表用空字节连接起来，就变成了头部信息。即文件大小
        file_size = struct.unpack('i', header)[0]  # 解包，取元组第一个元素即是文件大小

        path = os.path.dirname(os.path.abspath(__file__))
        download_path = os.path.join(path, '网盘', f'{num}的网盘', 'My_Download')
        if not os.path.exists(download_path):
            os.makedirs(download_path)  # 创建一个下载路径
        file_name = os.path.join(download_path, name)
        print(f'默认下载路径是{download_path}')
        has_download_size = 0
        file = open(file_name, mode='wb')
        print('正在读取文件')
        while has_download_size < file_size:
            if file_size - has_download_size < 1024:
                size = file_size - has_download_size
            else:
                size = 1024
            chunk = client.recv(size)  # 读取服务端发来的数据
            file.write(chunk)
            has_download_size += len(chunk)
            schedule = has_download_size / file_size
            schedule = '%.2f%%' % (schedule * 100)  # 转换成百分数
            print(f'\r已下载{schedule}', end=' ')
            # time.sleep(0.03)
            time.sleep(0.5)
        print()
        print('下载成功')
        file.close()
        break


def download(conn, num):
    '''这是服务端下载文件的函数'''
    while True:
        send(conn=conn, text='请输入要下载文件的名字(q/Q退出)')  # 发送获取文件名字的请求
        name = text_info(conn=conn)  # 接受返回的名字
        if name.lower() == 'q':
            break
        if name == 'None':
            continue
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(path, '网盘', f'{num}的网盘', name)  # 得到文件路径

        file_size = os.stat(file_path).st_size  # 得到文件大小
        conn.sendall(struct.pack('i', file_size))  # 将文件大小打包发送给客户端
        has_send_size = 0
        file = open(file_path, mode='rb')
        while has_send_size < file_size:
            if file_size - has_send_size < 1024:
                size = file_size - has_send_size
            else:
                size = 1024
            chunk = file.read(size)
            conn.sendall(chunk)  # 将已读取的数据发送到客户端
            has_send_size += len(chunk)
        file.close()
        break
