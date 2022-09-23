# os
import os
import functools

# 获取当前目录下所有文件       os.listdir()
print(os.listdir('G:\路飞'))

# 遍历一个文件夹所有.py文件
data = os.walk('G:\路飞')
# print(data)   返回的是一个生成器
for path, folder, file_name_lst in data:  # 第一个元素是路径，第二个是路径下面的文件夹名字，第三个元素是文件名字
    # print(path)
    for name in file_name_lst:
        file_abs_path = os.path.join(path, name)
        # print(file_abs_path)  # 这样就可以获得所有的文件名以及路径
        if file_abs_path.rsplit('.')[-1] == 'py':
            print(file_abs_path)

# shutill
import shutil

# sys
import sys

# 1.获取当前解释器版本
print(sys.version)
# 2.导入模块路径
print(sys.path)

# 3.获取执行命令时传入的参数   sys.argv
print(sys.argv)

# random
import random

print(random.sample([11, 22, 33, 44, 512, 1], 3))  # random.sample  随机抽取三个元素

data = [11, 22, 33, 44, 512, 1]
random.shuffle(data)  # random.shuffle(data)  重新洗牌，洗的是原列表
print(data)

# hashlib 加密模块
import hashlib

hash = hashlib.md5('afjaiehofafnakefa'.encode('utf-8'))  # 这里也可以添加  145beb1d50a34c95823872630545bfb2 很难解密
hash.update('张三'.encode('utf-8'))  # 要转换成字节加密
resulu = hash.hexdigest()
print(resulu)  # 615db57aa314529aaa0fbe95b3e95bd3


def md5(pwd, salt='eagaegaegaeafaefaegf'):
    ''' 这个是定义md5加密的函数 '''
    hash = hashlib.md5(salt.encode('utf-8'))
    hash.update(pwd.encode('utf-8'))
    result = hash.hexdigest()
    return result


def pass_md5(pwd):
    hash = hashlib.md5('wfeafaefaefaef'.encode('utf-8'))
    hash.update(pwd.encode('utf-8'))
    return hash.hexdigest()


print(md5('456789'))  # faf71443205c92fdf04fe839e4513e68
