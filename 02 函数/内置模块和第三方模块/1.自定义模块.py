'''
from hello.cit import decor
import os

# python找模块时只会在指定路径查找

print(decor())
# 添加路径
import sys

print(sys.path)  # 这个就是默认路径 ，可以重新添加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 1.自定义模块名称千万不能和内部模块以及第三方模块重复
# 2.项目执行的文件一般都在根目录下，如果不在根目录中，需要自己手动在sys.path中添加
# 3.pycharm会默认将项目目录加入到sys.path中

# 模块导入的方式
# import 导入，导入的是一个模块，还可以导入一个包
import hello as me  # 导入一个包，默认加载的是__init__文件

print(me.hahah())

# 如果使用from导入，可以导入到函数级别
from hello.cit import decor
from hello.cit import *  # 这样就是全部导入

from hello import cit  # 也可以导入到模块级别

print(decor())
print(may())

# 1.如果导入的是模块，需要加.  如果导入函数可以直接用
# 2.但是from不能导入根目录下的模块
# 3.这两种方式都不会节省内存
# 4.都可以都过as别名，放在名字重复

# 可以通过.来找 ，叫相对导入，不能用在根目录运行的文件
from .import jkaf  #一个点表示上级目录
from ..message import klk
'''
