# 1.公有：任意地方都可以调用
# 2.私有：只有在类的内部才能被调用
class Ob:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 在属性前面加两个下划线表示私有成员，这样在外部就不能调用了

    def fun(self):
        return self.__age

    def __abc(self):  # 私有方法
        return 123

    @property
    def __add(self):  # 私有属性
        return 789


obj = Ob('杜孝先', 56)
print(obj.name)
# print(obj.__age) 报错
print(obj.fun())  # 但是可以通过调用公有的方法来获取私有成员


# obj.__abc()  找不到
# obj.__add  找不到

class Stu(Ob):  # 父类私有的方法，子类是无法继承的

    def func(self):
        pass


s1 = Stu(1, 2)
s1.fun()


# s1.__abc 没有

# 不按常规出牌
class Ob:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 在属性前面加两个下划线表示私有成员，这样在外部就不能调用了

    def fun(self):
        return self.__age

    def __abc(self):  # 私有方法
        return 123

    @property
    def __add(self):  # 私有属性
        return 789


obj = Ob('杜孝先', 56)
v1 = obj._Ob__age  # 在方法名前 加一个单下划线，在加上类名就可以调用了
print(v1)
