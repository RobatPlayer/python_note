# ##读文件    rb 表示读取文件的二进制内容
file = open('file/info.txt', 'r', encoding='utf-8')
date = file.read()
file.close()
print(date)

# 相对路径与绝对路径  window绝对路径\有可能出问题，写两个转义，或者加r

# ##判断路径是否存在
import os

print(os.path.exists('/2.第二章/file/info.txt'))  # 如果存在会返回True

# ##写文件   w写入文件首先会清空文件再写入
# file = open('file/message.txt', mode='w', encoding='utf-8')  # 只打开一遍可以避免w清空内容
# while True:
#     name = input('请输入用户名：')
#     if name == 'q':
#         break
#     pwd = input('请输入密码')
#     date = f'{name}-{pwd}\n'
#     file.write(date)
# file.close()

# ##案例一，去网上下载一点文本信息
import requests

url = 'https://lmg.jj20.com/up/allimg/4k/s/02/2109242301524006-0-lp.jpg'
requ = requests.get(url)
requ.encoding = 'utf-8'
dowload = requ.content
print(dowload)
with open('file/beautiful.png', 'wb') as file:
    file.write(dowload)

# ##文件打开模式  带+表示既可以读又可以写
# r+读写光标在起始位置    w+默认是起始位置   a+光标在末尾

file.seek(0)  # .seek()可以调整光标的位置
