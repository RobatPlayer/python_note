# 1.super的作用？
'''使用super()会按照继承关系向上找成员'''

# 2.看图分析类A的继承关系
''' A-->B-->C-->M-->D-->F-->J-->G-->H
mro(A)=[A]+marge(mro(B)+mro(F)+[B,F])
[A]+marge([B,C,M,D,G]+[F,J,G,H]+[B,F])
[A]+[B]+[C]+[M]+[D]+[F]+[J]+[G]+[H]
[A,B,C,M,D,F,J,G,H]
'''


# 3.看代码写结果

class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def message(self):
        return "{}-{}".format(self.name, self.age)


class Bar(Foo):
    def __init__(self, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email

    def total(self):
        data = "{}-{}-{}".format(self.name, self.age, self.email)
        return data


obj1 = Foo("武沛齐", 20)  # name='武沛齐' age=20
print(obj1.message)  # 武沛齐-20

obj2 = Bar("xx@live.com", "root", 100)  # email='xx.com'  name='root' age=100
print(obj2.message)  # root-100
obj2.total()  # 没有输出


# 4.看代码写结果

class Foo(object):
    def __call__(self, *args, **kwargs):
        return 666


data_list = [
    "武沛齐",
    dict,
    lambda: 123,
    True,
    Foo,
    Foo()
]

for item in data_list:
    if callable(item):
        val = item()
        print(val)
    else:
        print(item)
'''
武沛齐
{}
123
True
Foo的一个实例对象
666
'''

# 5.如何主动触发一个异常？
'''使用raise 异常()'''

# 6.反射的作用？
'''可以使用字符串来调用方法'''


# 7.看代码写结果

class Person(object):
    title = "北京"

    def __init__(self, name, wx):
        self.name = name
        self.wx = wx

    def show(self):
        message = "姓名{}，微信：{}".format(self.name, self.wx)
        return message

    @property
    def message(self):
        return 666

    @staticmethod
    def something():
        return 999


obj = Person("武沛齐", "wupeiqi666")  # name='武沛齐'  wx='wupeiqi666'

print(getattr(obj, 'wx'))  # wupeiqi666
print(getattr(obj, 'message'))  # 666
print(getattr(obj, 'show')())  # 姓名武沛齐，微信wupeiqi666
print(getattr(obj, 'something')())  # 999
