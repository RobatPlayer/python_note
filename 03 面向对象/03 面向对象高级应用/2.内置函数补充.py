# 1.classmethod,staticmethod,property

# 2.callable
# 函数，类后面加括号，还有callable方法
def do(hamdle):
    hamdle()  # 这个参数加括号有三种情况， 参数是函数，参数是类，参数是对象且类中有callable方法


# 3.super().方法 按照mro继承关系向上找成员
class Base:
    def message(self, num):
        print('hello', num)


class Foo(Base):
    def fun(self, pwd):
        print('world')
        super().message(pwd + 10)  # 这个会执行逐级寻找message方法


f1 = Foo()
f1.fun(123)
'''应用场景：在已经实现功能的基础上不改变源代码而加入一些扩展功能'''
# 比如修改列表的append
lst = [123]
lst.append(2)


class My_list(list):
    def append(self, num):
        print('我的自定义功能')  # 加入自定义功能
        return super().append(num)


obj = My_list([11, 22, 33])  # 类中没有init方法，去list中找
obj.append(200)
print(obj)
for i in obj:
    print(i)
print(dir(obj))
print(dir(obj.__iter__()))

# 4.type 获取对象的类
print(type(obj))  # <class '__main__.My_list'>

# 5.isinstance 判断对象  是否是子类或子类实例对象

# 6.issubclass 判断类   是否是某个类的子孙类
