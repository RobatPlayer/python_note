# 1.绑定方法
# 2.类方法
# 3.静态方法
class School():
    def __init__(self, name):
        self.name = name

    def f1(self):  # 这个是绑定方法
        print('绑定方法')

    @classmethod  # 加上这个装饰器变成类方法
    def f2(cls):  # 至少有一个cls的参数
        print('类方法')

    @staticmethod  # 静态方法
    def f3():  # 没有默认参数
        print('静态方法')


# 绑定方法，主流是通过对象调用
p1 = School('杜孝先')  # 先创建实例化对象
p1.f1()  # 然后调用绑定方法

# 类方法，主流是通过类调用
School.f2()  # 可以使用类调用方法，cls默认指的就是调用这个方法的类
p1.f2()  # 也可以使用对象调用类方法，cls指的就是调用这个方法的对象的类

# 静态方法，主流还是通过类调用
School.f3()  # 可以使用类调用方法
p1.f3()  # 也可以使用对象调用静态方法
'''
在使用过程中用到哪个方法就定义哪个方法，主要取决于用到了哪个参数
'''
# 面试题 ，在类中@classmethod 和@staticmethod的作用
# 如果在方法上添加了@classmethod，那么就会变成类方法，默认带有cls参数
# 如果在方法上添加了@staticmethod，那么就会变成静态方法，默认没有参数
# 如果使用到了cls参数就定义类方法，如果没有参数就定义静态方法
