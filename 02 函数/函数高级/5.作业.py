import functools
import random
import os

'''
# 1.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出"after"
def decor(var):
    @functools.wraps(var)
    def inner(*args, **kwargs):
        res = var(*args, **kwargs)  # 这行就是后面要执行的代码
        print('after')
        return res

    return inner


@decor
def func(a1):
    return a1 + "傻叉"


@decor
def base(a1, a2):
    return a1 + a2 + '傻缺'


@decor
def foo(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4 + '傻蛋'


func('1')


# 2.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。


def decor(var):
    @functools.wraps(var)
    def inner(*args, **kwargs):
        lst = []
        for _ in range(5):
            res = var(*args, **kwargs)
            lst.append(res)
        return lst

    return inner


@decor
def func():
    return random.randint(1, 4)


result = func()  # 内部自动执行5次，并将每次执行的结果追加到列表最终返回给result
print(result)
'''
# 3.请为以下函数编写一个装饰器，添加上装饰器后可以实现： 检查文件所在路径（文件件）是否存在，如果不存在自动创建文件夹（保证写入文件不报错）。

write_path = ('usr/bin')


def decor(var):
    @functools.wraps(var)
    def inner(path):
        if not os.path.exists(write_path):  # 这里判断要设置为上级目录
            os.makedirs(write_path)
        res = var(path)
        return res

    return inner


@decor
def write_user_info(path):
    file_obj = open(f'{path}/xx.text', mode='w', encoding='utf-8')  # 这里写文件的路径加上名字
    file_obj.write("武沛齐")
    file_obj.close()


write_user_info(write_path)


# 4.分析代码写结果：

def get_data():
    scores = []

    def inner(val):
        scores.append(val)
        print(scores)

    return inner


func = get_data()

func(10)  # get_data()(10)-->inner(10)  输出 [10]
func(20)  # [10,20]
func(30)  # [10,20,30]

# 5.

name = "武沛齐"


def food():
    print(name)


def func():
    name = "root"
    food()


func()  # 武沛齐   因为不同函数的变量不能共用

# 6.

name = "武沛齐"


def func():
    name = "root"

    def foo():
        print(name)

    foo()


func()  # root


# 7.


def func(val):
    def inner(a1, a2):
        return a1 + a2 + val

    return inner


data_list = []

for i in range(10):
    data_list.append(func(i))  # func(0)  -->inner

print(data_list)  # [inner,inner....]


# 8.

def func(val):
    def inner(a1, a2):
        return a1 + a2 + val

    return inner


data_list = []

for i in range(10):
    data_list.append(func(i))  # func(0)  -->inner
# 这里执行完变成了   [inner,inner....] 不过对应的val不同
v1 = data_list[0](11, 22)  # inner(11,22)   return =11+22+0
v2 = data_list[2](33, 11)  # inner(33,11)   return =33+11+2

print(v1)  # 33
print(v2)  # 46
