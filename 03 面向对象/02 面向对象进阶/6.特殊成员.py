# __方法__
import requests


class Ob:
    # 1.初始化方法
    def __init__(self, name, sex):  #
        print('第二步，初始化对象，在空对象中创建数据')
        self.name = name
        self.sex = sex

    # 2.构造方法
    def __new__(cls, *args, **kwargs):
        print('第一步，先创建空对象并返回')  # 不写也会在父类里面创建
        return object.__new__(cls)

    # 3.__call__方法：在对象后面加括号会自动执行call方法
    def __call__(self, *args, **kwargs):
        print('执行了call方法')

    # 4.__str__方法  和str(对象)搭配（不使用str也行），调用str方法，这个返回什么，就会将其转化为字符串返回,
    def __str__(self):
        return f'我叫{self.name}，性别{self.sex}'

    # 5.__dict__方法  print(obj.__dict__) 会将实例对象的属性转化成字典

    # 6.__getitem__  , __setitem__  ,  __delitem__
    def __getitem__(self, item):  # 如果加上这个方法，那么对象就会支持 obj['item']
        return item

    def __setitem__(self, key, value):  # 如果加上这个方法，那么对象就会支持 obj['key']=456
        print(key, value)

    def __delitem__(self, key):  # 如果加上这个方法，那么对象就会支持 del obj['key']
        print(key)

    # 7.  __enter__  ，  __exit__ 一般都是成对出现的，with上下文管理器先执行enter，在执行exit
    def __enter__(self):
        print('打开了')
        return 666

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('关闭了')

    # 8.__add__方法  可以支持两个类对象相加，将+后面的值当做参数传递进去，并返回值
    def __add__(self, other):
        return f'{self.name}-{other.name}'

    def __sub__(self, other):  # 相减
        pass

    def __mul__(self, other):  # 相乘
        pass

    def __divmod__(self, other):  # 相除
        pass

    # 9.__iter__方法  单独在下面
    def __iter__(self):
        pass

# 1,2
obj = Ob('杜孝先', '男')  # 在创建对象要经历new和init两个步骤

# 3
obj()

# 4
print(obj)  # 如果直接打印对象会得到一个<__main__.Ob object at 0x000001B0D09AAD00>，加上str在打印就会变成方法返回的内容

# 5
print(str(obj))
print(obj.__dict__)

# 6：字典的对象支持字典['键'],对象默认是不支持的，加上上面三个方法就会支持
print(obj['key'])
obj['hello'] = '456'
del obj['nihao']

# 7. 文件操作支持with open ，对象默认不支持  AttributeError: __enter__  AttributeError: __exit__
# with对象 as file  wiht内部会执行__enter__方法，这个方法返回值是什么，file就是什么
# 当with缩进里面的代码执行完了，会自动执行__exit__方法
with obj as file:
    print(file)  # file=666

# 8.整型支持相加，但是类对象不支持，加入__add__方法就支持了
print(obj + Ob('老冯', '男'))

# 面试题：完善这个代码
'''
class Content:
    def do_something(self):
        print('内部执行')


with Content() as ctx:  
    print('内部执行')
    ctx.do_something()  # ctx没有这个方法，类对象才有
'''


class Content:
    def __enter__(self):
        pass
        return self  # 将ctx变成原对象

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def do_something(self):
        print('内部执行')


with Content() as ctx:
    print('内部执行')
    ctx.do_something()

