# 属性是由绑定方法+特殊装饰器组合创造出来的，让以后调用方法时可以不加括号
class Foo:
    def __init__(self, name):
        self.name = name

    def f1(self):
        print(123)

    @property  # 在绑定方法上面加装饰器就变成属性了，以后调用就不用加括号了
    def f2(self):
        return 456


obj1 = Foo('杜孝先')
obj1.f1()
v1 = obj1.f2  # 不用加括号
print(v1)

import requests
from requests.models import Response


# res.text就用到了这个属性

# 关于属性的编写方式有两种
# 1.基于装饰器
class Ffoo:
    def __init__(self, name):
        self.name = name

    @property
    def f1(self):
        print(123)

    @f1.setter  # 方法名加.setter  在下面执行的时候会将值赋予给value
    def f1(self, value):
        return 456

    @f1.deleter
    def f1(self):
        pass


obj = Ffoo('杜孝先')
obj.f1 = 789
del obj.f1
'''
由于属性和实例对象的调用方法方式相同，所以不要吧方法和实例变量重名
如果想创造关联，可以加_
'''


# 2.基于定义变量
class Fff:
    def __init__(self, name):
        self.name = name

    def fun(self, value):
        pass

    def he(self):
        pass

    x = property(fun, he, None, 'me')


obj2 = Fff('杜孝先')
