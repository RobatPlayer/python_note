import functools


def auth(fun):
    @functools.wraps(fun)  # 如果在这里加上这行代码，虽然下面被装饰的函数已经被替代，但是下面仍然会输出原函数的注释以及名字
    def inner(*args, **kwargs):
        '''你好'''
        res = fun(*args, **kwargs)
        return res

    return inner


def admin():
    '''这是判断大小的函数
    能赋值'''
    # 也可以输出
    '''不可以赋值'''
    pass


@auth
def my():
    '''我是注释'''
    pass


print(admin.__name__)  # 输出函数的名字，字符串形式

print(admin.__doc__)  # 输出函数里面的注释   只会显示第一个''''''里面的内容

# 如果函数被装饰
print(my.__name__)  # 被装饰之后函数的名字就会发生了改变

print(my.__doc__)  # 同时注释也不再是原函数的注释

# @functools.wraps(fun)   如果加上这行代码，虽然被装饰的函数已经被替代，但是仍然会输出原函数的注释以及名字
print(my.__name__)
print(my.__doc__)
