import hashlib

# 1.封装
'''
将统一类方法封装到一个类中
将数据封装到对象中，通过init实例化对象
'''


# 2.继承  基类和派生类
class Father:
    def fun(self):
        print(132)


class Son(Father):
    def fun1(self):
        print(456)

    def md5(self, pwd, salt='qrefafaf456af54fa6'):
        hash = hashlib.md5(salt.encode('utf-8'))
        hash.update(pwd.encode('utf-8'))
        return hash.hexdigest()


p1 = Son()  # 实例化对象
p1.fun1()  # 调用方法
print(p1.md5('123456'))
p1.fun()  # 继承父类方法，优先在自己类中找，找不到再去父类找


# Python允许多继承
class School:
    def f1(self):
        print(123)


class Classroom:
    def f1(self):
        print(456)


class Student(Classroom, School):  # 左边比右边优先
    def f3(self):
        print('start')
        self.f1()
        print('over')


st = Student()
st.f3()

# 总结
'''
1.执行对象.方法时，优先去对象关联的类中找，然后才去父类找
2.如果有多继承，先继承左边的，再继承右边的
3.self到底是谁？要去self对应的类中获取成员
'''


# 3.多态
# Python对数据类型没有要求，天生支持多态
class School:
    def f1(self):
        return 123


class Classroom:
    def f1(self):
        return 456


def func(arg):
    print(arg.f1())


v1 = School()
func(v1)
v2 = Classroom()
func(v2)

# 鸭子类型：不管是创建什么类型，只要会呱呱叫就是鸭子，不管传入什么类型的对象，只要有f1方法就行

'''
三大特'''