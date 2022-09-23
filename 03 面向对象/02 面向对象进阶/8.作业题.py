# 1.列举面向对象的成员并简述他们的特点。
'''
变量：实例对象，归属于变量，只能通过实例对象调用；类对象，归属于类，可以通过实例对象和类调用
方法：绑定方法，可以实例化对象，默认有self一个参数；类方法，默认有一个参数cls；静态方法，默认没有参数
属性：在方法前加@property就变成了属性，不加括号也能调用
'''

# 2. @staticmethod和@classmethod的作用是什么？
'''
如果在方法前加入@staticmethod修饰，那么就变成了静态方法，默认没有参数，如果加上@classmethod就变成了类方法，默认有一个cls参数
'''

# 3.面向对象中如何让成员变为私有。
'''在成员前面加两个下划线__'''

# 4.`__new__`方法的作用？
'''创建一个空对象，将这个空对象传给__init__方法'''

# 5.简述你理解的：迭代器、生成器、可迭代对象。
'''
可迭代对象里面包含__iter__方法，且返回值是一个迭代器对象
迭代器对象里面含有__iter__方法和__next__方法，可以用for in循环遍历
生成器是一种特殊的迭代器对象
'''


# 6.看代码写结果
class Foo(object):
    a1 = 1

    def __init__(self, num):
        self.num = num

    def show_data(self):
        print(self.num + self.a1)


obj1 = Foo(666)
obj2 = Foo(999)

print(obj1.num)  # 666
print(obj1.a1)  # 1

obj1.num = 18
obj1.a1 = 99

print(obj1.num)  # 18
print(obj1.a1)  # 99

print(obj2.a1)  # 1
print(obj2.num)  # 999
print(obj2.num)  # 999
print(Foo.a1)  # 1
print(obj1.a1)  # 99


# 7.看代码写结果，注意返回值。

class Foo(object):

    def f1(self):
        return 999

    def f2(self):
        v = self.f1()
        print('f2')
        return v

    def f3(self):
        print('f3')
        return self.f2()

    def run(self):
        result = self.f3()
        print(result)


obj = Foo()
v1 = obj.run()
print(v1)


# f3
# f2
# 999
# None


# 8.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):

    def f1(self):
        print('f1')

    @staticmethod
    def f2():
        print('f2')


obj = Foo()
obj.f1()  # f1
obj.f2()  # f2

Foo.f1(obj)  # 少obj
Foo.f2()  # f2


# 9.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):

    def f1(self):
        print('f1')
        self.f2()
        self.f3()

    @classmethod
    def f2(cls):
        print('f2')

    @staticmethod
    def f3():
        print('f3')


obj = Foo()
obj.f1()


# f1
# f2
# f3


# 10.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Base(object):
    @classmethod
    def f2(cls):
        print('f2')

    @staticmethod
    def f3():
        print('f3')


class Foo(Base):
    def f1(self):
        print('f1')
        self.f2()
        self.f3()


obj = Foo()
obj.f1()


# f1
# f2
# f3

# 11.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):
    a1 = 1
    __a2 = 2

    def __init__(self, num):
        self.num = num
        self.__salary = 1000

    def show_data(self):
        print(self.num + self.a1)


obj = Foo(666)

print(obj.num)  # 666
print(obj.a1)  # 1
# print(obj.__salary)  #不行，这是私有成员
# print(obj.__a2)  #不行
print(Foo.a1)  # 1
# print(Foo.__a2)  #不行
obj.show_data()  # 667


# 12.看代码写结果

class Foo(object):

    def __init__(self, age):
        self.age = age

    def display(self):
        print(self.age)


data_list = [Foo(8), Foo(9)]
print(data_list[0].age)  # 8
data_list[1].display()  # 9

for item in data_list:
    print(item.age, item.display())


# 8
# 8,None
# 9
# 9,None

# 13.看代码写结果

class Base(object):
    def __init__(self, a1):
        self.a1 = a1

    def f2(self, arg):
        print(self.a1, arg)


class Foo(Base):
    def f2(self, arg):
        print('666')


obj_list = [Base(1), Foo(2), Foo(3)]

for item in obj_list:
    item.f2(1)


# 1,1
# 666
# 666

# 14.看代码写结果

class Foo(object):
    def __init__(self, num):
        self.num = num


v1 = [Foo for i in range(10)]
v2 = [Foo(5) for i in range(10)]
v3 = [Foo(i) for i in range(10)]

print(v1)  # [FOO类，FOO类...]
print(v2)  # [Foo(5)，Foo(5)，Foo(5)....]
print(v3)  # [FOO(1),FOO(2),FOO(3)...]


#
# 15.看代码写结果

class StarkConfig(object):

    def __init__(self, num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)


config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
for item in config_obj_list:
    print(item.num)


# 1
# 2
# 3

# 16.
# 看代码写结果

class StarkConfig(object):

    def __init__(self, num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)


config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
for item in config_obj_list:
    item.changelist(666)


# 1 666
# 2 666
# 3 666

# 17.看代码写结果

class StarkConfig(object):

    def __init__(self, num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)

    def run(self):
        self.changelist(999)


class RoleConfig(StarkConfig):

    def changelist(self, request):
        print(666, self.num)


class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self, k, v):
        self._registry[k] = v


site = AdminSite()

site.register('武沛齐', StarkConfig(19))
site.register('root', StarkConfig(20))
site.register("admin", RoleConfig(33))

print(len(site._registry))  # 3

for k, row in site._registry.items():
    row.changelist(5)


# 19 5
# 20 5
# 666 33

# 18.看代码写结果（如有报错，请标注报错位置）

class StarkConfig(object):
    def __init__(self, num):
        self.num = num

    def run(self):
        self()

    def __call__(self, *args, **kwargs):
        print(self.num)


class RoleConfig(StarkConfig):
    def __call__(self, *args, **kwargs):
        print(345)

    def __getitem__(self, item):
        return self.num[item]


v1 = RoleConfig('alex')
v2 = StarkConfig("wupeiqi")

'''这里注意一下'''
print(v1[1])  # l  alex[1] 字符串[1]=l


# print(v2[2])  # 报错，没有__gieitem__方法

# 19.补全代码

class Context:
    def __enter__(self):
        return self

    def do_something(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with Context() as ctx:
    ctx.do_something()


# 20.看代码写结果

class Department(object):
    def __init__(self, title):
        self.title = title


class Person(object):
    def __init__(self, name, age, depart):
        self.name = name
        self.age = age
        self.depart = depart

    def message(self):
        msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
        print(msg)


d1 = Department('人事部')
d2 = Department('销售部')

p1 = Person('武沛齐', 18, d1)
p2 = Person('alex', 18, d1)

p1.message()  # 我是武沛齐,年龄18,属于人事部
p2.message()  # 我是alex,年龄18,属于人事部


#
# 21.分析代码关系，并写出正确的输出结果。

class Node(object):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, node):
        self.children.append(node)

    def __getitem__(self, item):
        return self.children[item]


root = Node("中国")

root.add(Node("河南省"))
root.add(Node("河北省"))

print(root.title)  # 中国
print(root[0])  # 类对象 title=河南省
print(root[0].title)  # 河南省
print(root[1])  # 类对象 title=河北省
print(root[1].title)  # 河北省


# 22.分析代码关系，并写出正确的输出结果。

class Node(object):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, node):
        self.children.append(node)

    def __getitem__(self, item):
        return self.children[item]


root = Node("中国")  # 创建一个实例对象 lst=[]

root.add(Node("河南省"))  # 调用add方法 self.children=[实例对象(title=河南省)] 而河南省的列表是空的
root.add(Node("河北省"))  # 调用add方法 self.children=[实例对象(title=河南省)，实例对象(title=河北省)]
root.add(Node("陕西省"))  # 调用add方法 self.children=[实例对象(title=河南省)，实例对象(title=河北省)，实例对象(title=陕西省)]
root.add(Node("山东省"))  # 调用add方法 self.children=[实例对象(title=河南省)，实例对象(title=河北省)，实例对象(title=陕西省)，实例对象(title=山东省)]

root[1].add(Node("石家庄"))  # 调用getitem方法 self.children=[实例对象(title=河南省)，实例对象(title=河北省)，实例对象(title=陕西省)，实例对象(title=山东省)]
root[1].add(Node("保定"))  # 相当于河北省:[石家庄，保定，廊坊]
root[1].add(Node("廊坊"))

root[3].add(Node("潍坊"))  # 山东省[:潍坊，烟台，威海]
root[3].add(Node("烟台"))
root[3].add(Node("威海"))

root[1][1].add(Node("雄安"))  # 河北省:石家庄，保定：[雄安，望都]，廊坊]
root[1][1].add(Node("望都"))

print(root.title)  # 中国
print(root[0].title)  # 河南省
print(root[1].title)  # 河北省
print(root[1][0].title)  # 石家庄
print(root[1][2].title)  # 廊坊
print(root[1][1][0].title)  # 雄安
