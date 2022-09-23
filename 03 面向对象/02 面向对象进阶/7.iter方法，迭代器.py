'''
迭代器类型的定义:
1.当类中定义__init__和__next__方法时
2.__iter__方法需要返回对象本身self
3.__next__方法返回下一个数据，如果没有了数据会抛出 StopIteration 异常
'''


# 迭代：为for循环提供一步一步获取数据的功能
# 创建迭代器类型
class It(object):
    def __init__(self):
        self.conuter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.conuter += 1
        if self.conuter == 3:
            raise StopIteration()  # 抛出异常
        return self.conuter


obj1 = It()  # 创建迭代器对象

# v1 = obj1.__next__()
# print(v1)
# v2 = obj1.__next__()
# print(v2)
# v3 = obj1.__next__()
# print(v3)

# 使用next函数
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))

obj2 = It()
for i in obj2:  # 在循环时，首先会执行__iter__方法，并获取返回值，然后会一直反复的执行next(对象)，每执行一次就会把值赋给i
    print(i)  # 抛出异常终止循环


# 生成器
def func():
    yield 1
    yield 2


# 创建了生成器对象，在Python内部其实是根据generator这个类创建的对象，生成器内部也声明了__iter__和__next__方法
obj = func()  # 可以认为生成器是一种特殊的迭代器


# 可迭代对象
# 如过一个类中有__iter__方法且返回值是一个迭代器对象，那么称这个类创建的对象是可迭代对象
class It(object):
    def __init__(self):
        self.conuter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.conuter += 1
        if self.conuter == 3:
            raise StopIteration()  # 抛出异常
        return self.conuter


class Foo:
    def __iter__(self):
        #  return '迭代器对象或者生成器对象'
        return It()  # 迭代器对象


f1 = Foo()  # f1是可迭代对象，如果一个对象是可迭代对象，那么这个对象可以被for循环
for i in f1:  # 循环可迭代对象，会先执行f1.__iter__获取迭代器对象，不断执行next方法
    print(i)

print(dir(range(100)))  # 查看功能  有__iter__但没有__next__，说明range()是一个可迭代对象
print(dir(range(100).__iter__()))  # 查看对象的返回值，即迭代器对象  有__next__，__iter__  迭代器对象


# 生成自定义range
# 还要定义一个迭代器对象
class Iter_Range:
    def __init__(self, num):  # 自定义变量
        self.num = num
        self.conut = -1

    def __iter__(self):
        return self  # 返回本身

    def __next__(self):
        self.conut += 1
        if self.conut == self.num:
            raise StopIteration  # 当没有数据要抛出StopIteration异常
        return self.conut


# 先定义一个可迭代对象
class Xrange:
    def __init__(self, max_num):  # 传入最大值参数
        self.max_num = max_num

    def __iter__(self):  # 调用iter方法
        return Iter_Range(self.max_num)  # 返回一个迭代器对象


print(range(10))
print(Xrange(10))
for i in Xrange(10):
    print(i, end=' ')
print()


# 基于生成器
class Arange:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        counter = 0
        while counter < self.max_num:
            yield counter  # 生成器对象带有next
            counter += 1


lst = list([11, 22, 33])
print(dir(lst))  # __iter__ 说明列表是一个可迭代对象
print(dir(lst.__iter__()))  # __next__,__iter__ 说明创建的是一个迭代器对象
v2 = lst.__iter__()
print(v2.__next__())
print(v2.__next__())
print(v2.__next__())
# print(v2.__next__())  StopIteration

from collections.abc import Iterable, Iterator

v1 = [1, 2, 3]
v11 = v1.__iter__()
print(isinstance(v1, Iterator))  # 判断是否是迭代器  判断依据是里面是否有__iter__和__next__
print(isinstance(v11, Iterator))

print(isinstance(v1, Iterable))  # 判断是否是可迭代对象，判断依据是里面是否有__iter__且返回迭代器对象
print(isinstance(v11, Iterable))  # 这个__iter__返回的是自己，所以判定是迭代器对象
