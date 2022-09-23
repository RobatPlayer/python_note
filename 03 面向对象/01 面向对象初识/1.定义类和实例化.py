import hashlib


class Message():  # 类名首字母大写
    def fun(self, a, b):  # 在类里面的函数称为方法,第一个参数是self
        print('hello')

    def md5(self, pwd, salt='qrqrqrqrwqrqr'):  # 可以定义多个类方法
        hash = hashlib.md5(salt.encode('utf-8'))
        hash.update(pwd.encode('utf-8'))
        return hash.hexdigest()


msg = Message()  # 类名加括号，称为实例化一个对象 ，创建了一块区域
msg.fun(1, 2)  # 调用类方法
print(msg.md5('10010'))


# 对象和self
class Student():
    def __init__(self, name):  # 这个是特殊的方法，如果执行创建对象Student()，就相当于执行了这个函数，可以加参数
        self.data = name  # self指当前调用这个方法的对象


# 对象就是基于实例化出来的一块区域默认没有数据，经过类的默认方法可以在内存中存储一些数据
''' 
创建对象的目的:
1.可以存储数据
2.可以调用类方法，并将自己作为参数传递
'''
ms = Student('duxiaoxian')  # 如果默认方法加了参数，这里也要加参数


# 实例部分
class Info():
    def __init__(self, name, age, pwd):  # 可以规范用户输入的信息，做约束
        # 实例变量
        self.name = name  # 初始化变量，实例化变量
        self.age = age
        self.password = pwd
        if self.password.isdecimal():  # 还可以做一些规范，将用户输入错误的数据进行修正
            return
        # 将数据封装到对象里面

    # 下面这些都是绑定方法
    def fun(self):
        print(123)

    def func(self):
        self.fun()  # 这一个类中，一个方法也可以调用另外一个方法。因为self都是一个对象


# 如果想要使用绑定方法，可以先创建对象在调用
p1 = Info('杜孝先', 13, '123456')  # 创建对象
p1.fun()
Info.fun(p1)  # 也可以这么调用(不常用)

# 什么时候用面向对象？
# 1.仅仅做数据分装
# 2.先封装对象再对数据做加工处理
# 3.根据模板创建同一类数据且同类数据具有相同的功能
