import os
import shutil

# 1.获取当前运行文件的路径
abs = os.path.abspath(__file__)
print(abs)

# 2.获取当前文件上一级目录
path = os.path.dirname(abs)
print(path)  # 得到的是上一级目录
file_path = path + '/file.info.txt'  # 获取到文件的绝对目录

# 3.路径拼接，根据系统不同创建不同的路径
file = os.path.join(path, 'file', 'info.txt')
print(file)

# 4.判断路径是否存在
print(os.path.exists('file'))

# 5.创建文件夹   os.makedirs()
if not os.path.exists(file):
    os.makedirs('路径')

# 6.判断是否是文件夹  os.path.isdir()
print(os.path.isdir(file))

# 7.删除文件或文件夹   shutil.rmtree(路径)
# shutil.rmtree('file/xxxx')  没有会报错

# 8.拷贝文件夹  shutil.copytree?(要拷贝文件的路径，拷贝到路径)
# shutil.copytree('路径', 'file/路径')

# 9.拷贝文件   shutil.copy( ) 和上面道理一样
# shutil.copy()

# 10.重命名（移动）  shutil.move( )
# shutil.move( )
