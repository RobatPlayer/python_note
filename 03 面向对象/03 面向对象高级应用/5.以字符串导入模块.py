# import_module和反射   import_module可以通过字符串导入模块
import random
from requests import exceptions
from importlib import import_module

m = import_module('random')
print(m.randint(1, 100))

n = import_module('request.exceptions')  # 这个最小就是导入到模块了，不能导入成员
