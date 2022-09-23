# 在fun（）函数执行前输出before，在执行后输出after
'''
def fun():
    print('我是fun函数')
    value = (11, 22, 33)
    return value


# 第一版
def outer(origin):
    def inner():
        print('before')
        res = origin()
        print('after')
        return res

    return inner


fun = outer(fun)
result = fun()
'''
# 第二版
'''
Python支持特殊语法： @函数名
如果在函数名前加@，会在函数内部自动执行  函数名（xxx）
@函数名
def xxx():
    pass   python会自动执行   函数名(xxx)  作为参数，执行结束后会将结果赋值给xxx  相当于xxx= 函数名（xxx）
'''

'''
def outer(origin):
    def inner():
        print('before')
        res = origin()
        print('after')
        return res

    return inner


@outer  # 相当于fun = outer(fun)   需要把outer函数放在上面
def fun():
    print('我是fun函数')
    value = (11, 22, 33)
    return value


result = fun()  # 首先会执行fun（）函数上面的@outer  此时 fun=inner  然后result=inner()
print(result)

'''

'''
# 在f三个函数执行前输出before，在执行后输出after
def outer(origin):
    def inner():
        print('before')
        res = origin()
        print('after')
        return res

    return inner


@outer
def fun1():
    print('我是fun1函数')
    value = (11, 22, 33)
    return value


@outer
def fun2():
    print('我是fun2函数')
    value = (11, 22, 33)
    return value


@outer
def fun3():
    print('我是fun3函数')
    value = (11, 22, 33)
    return value


fun1()
fun2()
fun3()

'''


# 总结如果多个函数可以使用装饰器

# 如果函数有参数了，可以在inner函数加入动态参数  ,也要在origin函数加入动态参数  ，这样就可以支持任意参数的函数
def outer(origin):
    def inner(*args, **kwargs):
        print('before')
        res = origin(*args, **kwargs)
        print('after')
        return res

    return inner


@outer
def fun1(a1):
    print('我是fun1函数')
    value = (11, 22, 33)
    return value


@outer
def fun2(a1, a2):
    print('我是fun2函数')
    value = (11, 22, 33)
    return value


@outer
def fun3(a1):
    print('我是fun3函数')
    value = (11, 22, 33)
    return value


fun1(11)
fun2(1, [123, 456])
fun3(a1=132)


# 装饰器实例,可以在不修改原函数和不改变调运方式的前提下   这个代码要求背过....面试常用
def outher(orign):
    def inner(*args, **kwargs):
        res = orign(*args, **kwargs)
        return res

    return inner


@outer
def fun():
    pass
