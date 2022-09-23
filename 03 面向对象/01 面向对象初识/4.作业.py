import re
import hashlib

# 1.简述面向对象三大特性?
'''
1.封装：将数据封装到对象中
2.继承：子类可以继承父类的方法，如果创建子类对象调用方法优先找对象所在类，如果没有可以去父类找
3.多态：不管是什么数据类型，只要含有某个相同的功能就可以调用
'''


# 2.将以下函数改成类的方式并调用:
class Fun:
    def func(self, a1):
        print(a1)


f1 = Fun()
f1.func('hello')


# 3.面向对象中的self指的是什么?
# 指的是调用这个方法创建的对象

# 4.以下代码体现面向对象的什么特性?

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


obj = Person('武沛齐', 18, '男')


# 封装

# 5.以下代码体现向对象的么特点?

class Message(object):
    def email(self):
        """
        发送邮件
        :return:
        """
        pass

    def msg(self):
        """
        发送短信
        :return:
        """
        pass

    def wechat(self):
        """
        发送微信
        :return:
        """
        pass


# 封装

# 6.

class Foo:
    def func(self):
        print('foo.func')


obj = Foo()
result = obj.func()  # foo.func
print(result)  # None


# 7.看代码写结果

class Base1:
    def f1(self):
        print('base1.f1')

    def f2(self):
        print('base1.f2')

    def f3(self):
        print('base1.f3')
        self.f1()


class Base2:
    def f1(self):
        print('base2.f1')


class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()


obj = Foo()
obj.f0()
'''
foo.f0
base1.f3
base1.f1
'''


# 8.看代码写结果:
class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1()
        print('base.f3')


class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()


obj = Foo()
obj.f2()
'''
foo.f2
foo.f1
base.f3
'''


# 9.补充代码实现
# 需求
# 1. while循环提示 户输 : 户名、密码、邮箱(正则满足邮箱格式)
# 2. 为每个用户创建一个个对象，并添加到user_list中。
# 3. 当列表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
def md5(pwd, salt='asfafajfgahfgafyuafahu'):
    '''这个一个md5加密的函数'''
    hash = hashlib.md5(salt.encode('utf-8'))
    hash.update(pwd.encode('utf-8'))
    return hash.hexdigest()


'''
user_list = []
while True:
    dic = {}
    user = input("请输入用户名:")
    pwd = input("请输入密码:")
    pwd = md5(pwd=pwd)
    email = input("请输入邮箱:")
    email = re.findall('^[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+$', email)
    if not email:
        print('格式错误，请重新输入')
        continue
    dic.update({'用户名': user, '密码': pwd, '邮箱': email[0]})
    user_list.append(dic)
    print(user_list)
    if len(user_list) == 3:
        break
for i in user_list:
    print(f'用户名:{i.get("用户名")},邮箱:{i.get("邮箱")}')
'''


# 10.补充代码: 实现户注册和登录。

class User():
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        while True:
            print('请登录')
            name = input('请输入用户名：')
            pwd = input('请输入密码：')
            for i in self.user_list:
                if name == i.name and pwd == i.pwd:
                    print('登陆成功')
                    return
            else:
                print('账号或密码输入错误，请重新输入')
                continue

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        for _ in range(2):
            name = input('请输入注册的用户名：')
            pwd = input('请输入注册密码：')
            ob = User(name=name, pwd=pwd)  # 创建User实例对象
            self.user_list.append(ob)
            print(self.user_list)
            print('注册成功')
        self.login()  # 注册成功之后跳转到登录

    def run(self):
        """
        主程序
        :return:
        """
        while True:
            chioce = input('登录请输入1  注册请输入2')  # 判断登录还是注册
            if chioce == '1':
                obj.login()  # 调用类里面的登录方法
                break
            elif chioce == '2':
                obj.register()  # 调用注册方法
                break
            else:
                print('输入错误，请重新输入')
                continue


if __name__ == '__main__':
    obj = Account()  # 创建一个实例对象
    obj.run()  # 调用类方法
